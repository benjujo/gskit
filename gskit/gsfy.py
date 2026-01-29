import dis
from functools import wraps
import os
import json
import inspect
import sys
import ast
from typing import Optional, Callable, Set, Tuple
from gskit.parser import GSParser
from gskit.ast_builder import ASTTransformer
from gskit.framework import CRS
from gskit.gs_context import GSContext
from gskit.elements import G1Element, G2Element, ZpElement


def _get_env_or_python_var(var_name: str, default: Optional[str] = None) -> Optional[str]:
    """
    Get environment variable, or check if it was set in Python via os.environ or as a global variable.
    This allows setting variables in Python shell before calling decorated functions.
    
    Checks in order:
    1. Environment variables (os.environ)
    2. Global variables in the calling frames (walks up the call stack)
    3. Returns default if not found
    """
    # First check environment variables
    if var_name in os.environ:
        return os.environ.get(var_name)
    
    # Then check global variables in the calling frames
    try:
        frame = inspect.currentframe()
        if frame is not None:
            # Walk up the call stack to check globals in each frame
            current_frame = frame.f_back  # Skip current frame, start with caller
            max_depth = 10  # Limit depth to avoid infinite loops
            depth = 0
            
            while current_frame is not None and depth < max_depth:
                globals_dict = current_frame.f_globals
                if var_name in globals_dict:
                    value = globals_dict[var_name]
                    # Convert to string if it's not already
                    if value is not None:
                        return str(value) if not isinstance(value, str) else value
                current_frame = current_frame.f_back
                depth += 1
    except Exception:
        # If frame inspection fails, just continue
        pass
    finally:
        # Clean up frame reference to avoid circular references
        if 'frame' in locals():
            del frame
    
    return default


def _capture_function_locals(func: Callable, *args, **kwargs):
    """
    Execute function and capture its local variables.
    Returns (result, local_vars_dict)
    """
    local_vars = {}
    
    def capture_locals(frame, event, arg):
        """Helper to capture local variables during function execution."""
        if event == "return":
            local_vars.update(frame.f_locals)
        return capture_locals

    # Use sys.settrace to capture locals during execution
    old_trace = sys.gettrace()
    sys.settrace(capture_locals)
    try:
        result = func(*args, **kwargs)
    finally:
        sys.settrace(old_trace)
    
    return result, local_vars


def _extract_gs_string_and_witnesses(func: Callable) -> Tuple[Optional[str], Set[str]]:
    """
    Extract GS_STRING from function source code and identify witness variables.
    Returns (gs_string, witness_variable_names).
    """
    try:
        source = inspect.getsource(func)
        tree = ast.parse(source)
        
        gs_string = None
        witness_vars = set()
        
        # Walk AST to find GS_STRING assignment
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == 'GS_STRING':
                        if isinstance(node.value, ast.Constant):
                            gs_string = node.value.value
                        elif isinstance(node.value, ast.Str):  # Python < 3.8
                            gs_string = node.value.s
        
        # If we found GS_STRING, parse it to identify witness variables
        if gs_string:
            try:
                parser = GSParser()
                parsed = parser.parse(gs_string)
                transformer = ASTTransformer()
                ast_node = transformer.transform(parsed)
                # Variables are witnesses, constants are not
                witness_vars = {var.name for var in ast_node.vars}
            except Exception:
                # If parsing fails, return what we have
                pass
        
        return gs_string, witness_vars
    except Exception:
        return None, set()


def _create_dummy_value_for_type(var_name: str, gs_string: Optional[str]) -> any:
    """
    Create a dummy value for a witness variable based on its type in GS_STRING.
    """
    if not gs_string:
        # Default to G1Element if we can't determine type
        return G1Element.zero()
    
    try:
        parser = GSParser()
        parsed = parser.parse(gs_string)
        transformer = ASTTransformer()
        ast_node = transformer.transform(parsed)
        
        # Find the variable and its type
        for var in ast_node.vars:
            if var.name == var_name:
                # Determine type from variable class
                var_type = type(var).__name__
                if 'G1' in var_type:
                    return G1Element.zero()
                elif 'G2' in var_type:
                    return G2Element.zero()
                elif 'Zp' in var_type or 'ZP' in var_type:
                    return ZpElement.zero()
                else:
                    return G1Element.zero()  # default
    except Exception:
        pass
    
    # Default fallback
    return G1Element.zero()


def _collect_variable_values(func: Callable, local_vars: dict) -> dict:
    """
    Collect variable names from bytecode and match them to runtime values.
    """
    bytecode_vars = {
        instr.argval
        for instr in dis.get_instructions(func)
        if instr.opname in {"LOAD_FAST", "STORE_FAST", "LOAD_GLOBAL", "STORE_GLOBAL"}
    }
    
    # Match bytecode variables to their runtime values
    collected_values = {var: local_vars.get(var, None) for var in bytecode_vars}
    return collected_values


def _process_legacy_mode(func: Callable, result: any, collected_values: dict, 
                        source_file: str, base_name: str, aliases: Optional[dict] = None):
    """
    Legacy mode: process and compile immediately (backward compatible).
    """
    gs_mode = _get_env_or_python_var("GS_MODE", None)
    if gs_mode not in ["PROOF", "VERIFY"]:
        print("GS_MODE must be set to PROOF or VERIFY")
        return result
    
    print("GS_MODE:", gs_mode)
    
    output_file = _get_env_or_python_var("GS_OUTPUT", f"{base_name}_proof.py")
    proof_output_file = _get_env_or_python_var("GS_PROOF_OUTPUT", f"{base_name}_proof.json")
    verify_output_file = _get_env_or_python_var("GS_VERIFY_OUTPUT", f"{base_name}_verify.py")
    crs_file = _get_env_or_python_var("GS_CRS", "crs.json")
    
    # Load CRS
    try:
        with open(crs_file, "r") as f:
            crs = json.load(f)
    except Exception as e:
        print(f"Error loading CRS: {e}")
        return result
    
    gs_string = collected_values.get('GS_STRING', None)
    if not gs_string:
        return result
    
    parser = GSParser()
    p = parser.parse(gs_string)
    t = ASTTransformer()
    r = t.transform(p)
    r.type_check()
    
    if gs_mode == "PROOF":
        # Create JSON with definitions from consts and vars
        definitions = {}
        variables = r.vars
        constants = r.consts
        
        for var in variables:
            value = collected_values[var.name].__json__()
            # Apply alias if specified
            key = aliases.get(var.name, var.name) if aliases else var.name
            definitions[key] = value
            
        for const in constants:
            value = collected_values[const.name].__json__()
            # Apply alias if specified
            key = aliases.get(const.name, const.name) if aliases else const.name
            definitions[key] = value
        
        compiled = r.compile_proof(definitions, crs, "elements")
        with open(output_file, 'w') as f:
            f.write(compiled)
    else:
        # VERIFY mode: Load everything from proof JSON (witnesses, pis, thetas, etc.)
        # then overwrite constants with locally computed values
        # This prevents tampering - constants are public values computed by the verifier
        with open(proof_output_file, "r") as f:
            definitions = json.load(f)
        
        # Get constants that need to be overwritten
        constants = r.consts
        
        # Overwrite constant values with local computation (not from proof!)
        # This ensures public values cannot be tampered with
        for const in constants:
            if const.name in collected_values and collected_values[const.name] is not None:
                value = collected_values[const.name].__json__()
                # Apply alias if specified (constants may be aliased in the proof JSON)
                key = aliases.get(const.name, const.name) if aliases else const.name
                definitions[key] = value
            else:
                print(f"Warning: Constant '{const.name}' not computed locally")
        
        compiled = r.compile_verify(definitions, crs, "elements")
        with open(verify_output_file, 'w') as f:
            f.write(compiled)
    
    return result


def _find_nested_gsfy_functions(func: Callable) -> list:
    """
    Recursively find all nested functions decorated with @gsfy.
    Returns a list of tuples: (function_name, gs_string)
    """
    nested_gs_strings = []
    
    try:
        source = inspect.getsource(func)
        tree = ast.parse(source)
        
        # Find the function definition node
        func_def = None
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == func.__name__:
                func_def = node
                break
        
        if not func_def:
            return nested_gs_strings
        
        # Recursively walk through nested function definitions
        def visit_nested_functions(node):
            for child in ast.iter_child_nodes(node):
                if isinstance(child, ast.FunctionDef):
                    # Check if this nested function has @gsfy decorator
                    has_gsfy = False
                    for decorator in child.decorator_list:
                        decorator_name = None
                        if isinstance(decorator, ast.Name):
                            decorator_name = decorator.id
                        elif isinstance(decorator, ast.Call) and isinstance(decorator.func, ast.Name):
                            decorator_name = decorator.func.id
                        
                        if decorator_name == 'gsfy':
                            has_gsfy = True
                            break
                    
                    if has_gsfy:
                        # Extract GS_STRING from this nested function
                        for stmt in child.body:
                            if isinstance(stmt, ast.Assign):
                                for target in stmt.targets:
                                    if isinstance(target, ast.Name) and target.id == 'GS_STRING':
                                        gs_string = None
                                        if isinstance(stmt.value, ast.Constant):
                                            gs_string = stmt.value.value
                                        elif isinstance(stmt.value, ast.Str):  # Python < 3.8
                                            gs_string = stmt.value.s
                                        
                                        if gs_string:
                                            nested_gs_strings.append((child.name, gs_string))
                    
                    # Recursively visit nested functions within this function
                    visit_nested_functions(child)
        
        visit_nested_functions(func_def)
        
    except Exception as e:
        print(f"Warning: Error finding nested @gsfy functions: {e}")
    
    return nested_gs_strings


def _process_modular_mode(func: Callable, result: any, collected_values: dict, 
                         source_file: str, base_name: str, aliases: Optional[dict] = None):
    """
    Modular mode: register with global GSContext instead of compiling immediately.
    Recursively searches for nested functions decorated with @gsfy and combines their GS_STRINGs.
    """
    gs_string = collected_values.get('GS_STRING', None)
    if not gs_string:
        return result
    
    # Find all nested @gsfy decorated functions and collect their GS_STRINGs
    nested_gs_functions = _find_nested_gsfy_functions(func)
    
    # Combine all GS_STRINGs: parent + all nested ones
    combined_gs_string = gs_string
    if nested_gs_functions:
        for nested_name, nested_gs_string in nested_gs_functions:
            # Combine with logical AND
            combined_gs_string = f"({combined_gs_string}) /\\ ({nested_gs_string})"
    
    # Get module name from source file
    module_name = os.path.splitext(os.path.basename(source_file))[0]
    func_name = func.__name__
    
    # Extract variables and constants that are referenced in the combined GS_STRING
    # We need to parse the GS_STRING to know which variables/constants to collect
    parser = GSParser()
    try:
        parsed = parser.parse(combined_gs_string)
        transformer = ASTTransformer()
        ast = transformer.transform(parsed)
        
        # Collect only the variables and constants that appear in GS_STRING
        variable_values = {}
        for var in ast.vars:
            if var.name in collected_values and collected_values[var.name] is not None:
                # Apply alias if specified
                key = aliases.get(var.name, var.name) if aliases else var.name
                variable_values[key] = collected_values[var.name]
        
        for const in ast.consts:
            if const.name in collected_values and collected_values[const.name] is not None:
                # Apply alias if specified  
                key = aliases.get(const.name, const.name) if aliases else const.name
                variable_values[key] = collected_values[const.name]
        
        # Register with global context using the combined GS_STRING
        context = GSContext.get_instance()
        context.register_function(
            func_name=func_name,
            module_name=module_name,
            gs_string=combined_gs_string,
            variable_values=variable_values
        )
        
        if nested_gs_functions:
            print(f"Modular mode: Combined {len(nested_gs_functions)} nested @gsfy function(s) into {func_name}")
        
    except Exception as e:
        print(f"Warning: Error processing GS_STRING in modular mode: {e}")
        # Continue execution even if GS processing fails
    
    return result


def gsfy(func: Optional[Callable] = None, *, modular: bool = False, witness: Optional[list] = None, aliases: Optional[dict] = None):
    """
    Decorator for Groth-Sahai proof generation.

    Supports two modes:
    - Modular mode (default): Registers with global GSContext for composition
    - Legacy mode: Processes and compiles immediately (backward compatible)

    Usage:
        @gsfy                                        # Modular mode (default)
        @gsfy(modular=True)                          # Explicit modular mode
        @gsfy(modular=False)                         # Legacy mode
        @gsfy(witness=['signature'])                 # Specify witness variables

        # Aliases - two ways:
        @gsfy(aliases={'signature': 'tag'})          # Decorator-level (fixed)
        func(..., _gs_aliases={'signature': 'tag'})  # Call-site (flexible)

        @gsfy(witness=['x'], aliases={'x': 'r'})     # Combine parameters

    The decorated function also gets a .gs_add() method for GSContext composition:

        ctx = GSContext(crs)

        # Add to context with aliases for this specific call
        obj.method.gs_add(ctx, arg1, arg2, aliases={'old': 'new'})

        # Finalize and compile
        ast = ctx.finalize()

    Args:
        func: Function to decorate (when used as @gsfy)
        modular: If True, register with global context; if False, compile immediately
        witness: List of parameter names that are witness variables (optional in VERIFY mode)
        aliases: Dict mapping internal names to external names (decorator-level, fixed at decoration)
                 e.g., {'signature': 'tag'} means 'signature' in GS_STRING becomes 'tag' externally

    Call-site aliases (more flexible):
        Pass _gs_aliases={'internal': 'external'} as a keyword argument to override decorator aliases.
        This allows the same component to be used with different names in different contexts.
        Example: result = verify(vk, m, sig, _gs_aliases={'signature': 'token'})

    Environment variables (can be set in shell or Python):
        GS_MODE: Must be "PROOF" or "VERIFY" (required for legacy mode)
        GS_OUTPUT: Output file for proof compilation
        GS_PROOF_OUTPUT: Proof JSON file (verify mode)
        GS_VERIFY_OUTPUT: Verify output file
        GS_CRS: CRS file path
    """
    def decorator(f: Callable):
        # Get the original function signature
        sig = inspect.signature(f)

        # Determine witness variables from decorator parameter or GS_STRING
        witness_vars = set(witness) if witness else set()

        # Extract GS_STRING at decoration time
        gs_string_from_source, auto_witness_vars = _extract_gs_string_and_witnesses(f)

        # If no explicit witness list, use auto-detected ones
        if not witness_vars:
            witness_vars = auto_witness_vars

        # Create a modified signature where witness parameters are optional (have defaults)
        new_params = []
        for param_name, param in sig.parameters.items():
            if param_name in witness_vars:
                # Make witness parameters optional with None default
                new_param = param.replace(default=None)
                new_params.append(new_param)
            else:
                new_params.append(param)

        new_sig = sig.replace(parameters=new_params)

        @wraps(f)
        def wrapper(*args, **kwargs):
            # Extract call-site aliases if provided (overrides decorator aliases)
            call_site_aliases = kwargs.pop('_gs_aliases', None)
            effective_aliases = call_site_aliases if call_site_aliases is not None else aliases

            # Check if we're in VERIFY mode and need to inject dummy values for witnesses
            gs_mode = _get_env_or_python_var("GS_MODE", None)

            # Check if any witness parameters are missing or None
            if witness_vars:
                param_names = list(sig.parameters.keys())
                num_positional = len(args)
                provided_by_args = set(param_names[:num_positional])
                provided_by_kwargs = set(kwargs.keys())

                missing_witnesses = []
                for witness_var in witness_vars:
                    if witness_var in sig.parameters:
                        is_provided = (witness_var in provided_by_args or
                                     witness_var in provided_by_kwargs)
                        is_none = (witness_var in kwargs and kwargs[witness_var] is None)

                        if not is_provided or is_none:
                            missing_witnesses.append(witness_var)

                # Handle missing witnesses based on mode
                if missing_witnesses:
                    if gs_mode == "VERIFY":
                        # VERIFY mode: inject dummy values for witnesses
                        gs_string, _ = _extract_gs_string_and_witnesses(f)

                        for witness_var in missing_witnesses:
                            dummy_value = _create_dummy_value_for_type(witness_var, gs_string)
                            kwargs[witness_var] = dummy_value
                    else:
                        # PROOF mode or normal execution: raise standard Python TypeError
                        num_missing = len(missing_witnesses)
                        if num_missing == 1:
                            raise TypeError(
                                f"{f.__name__}() missing 1 required positional argument: '{missing_witnesses[0]}'"
                            )
                        else:
                            args_str = ", ".join(f"'{w}'" for w in missing_witnesses)
                            raise TypeError(
                                f"{f.__name__}() missing {num_missing} required positional arguments: {args_str}"
                            )

            # Execute function and capture locals
            result, local_vars = _capture_function_locals(f, *args, **kwargs)

            # Collect variable values
            collected_values = _collect_variable_values(f, local_vars)

            # Get source file info
            source_file = inspect.getfile(f)
            base_name = os.path.splitext(os.path.basename(source_file))[0]

            # Process based on mode
            if modular:
                return _process_modular_mode(f, result, collected_values, source_file, base_name, effective_aliases)
            else:
                return _process_legacy_mode(f, result, collected_values, source_file, base_name, effective_aliases)

        def gs_add(ctx, *args, aliases: Optional[dict] = None, **kwargs):
            """
            Add this function's GS_STRING and values to a GSContext.

            This executes the function to compute values, then registers
            the GS_STRING and values with the context.

            Args:
                ctx: GSContext to add to
                *args, **kwargs: Arguments to pass to the function
                aliases: Dict mapping GS_STRING names to new names
                         e.g., {'signature': 'sig_attr1'} renames for this call

            Example:
                ctx = GSContext(crs)
                obj.verify.gs_add(ctx, vk, m, sig, aliases={'signature': 'sig1'})
                obj.verify.gs_add(ctx, vk2, m2, sig2, aliases={'signature': 'sig2'})
                ast = ctx.finalize()
            """
            if gs_string_from_source is None:
                raise ValueError(f"Function {f.__name__} has no GS_STRING defined")

            # Execute function to compute local values
            result, local_vars = _capture_function_locals(f, *args, **kwargs)

            # Collect values that appear in the GS_STRING
            collected_values = _collect_variable_values(f, local_vars)

            # Filter to only values referenced in GS_STRING
            # Parse GS_STRING to get variable and constant names
            parser = GSParser()
            parsed = parser.parse(gs_string_from_source)
            transformer = ASTTransformer()
            ast = transformer.transform(parsed)

            gs_names = {v.name for v in ast.vars} | {c.name for c in ast.consts}

            # Build values dict with only GS_STRING names
            values = {}
            for name in gs_names:
                if name in collected_values and collected_values[name] is not None:
                    values[name] = collected_values[name]

            # Add to context
            ctx.add(gs_string_from_source, values, aliases)

            return result

        # Attach gs_add as a method on the wrapper
        wrapper.gs_add = gs_add

        # Store GS_STRING for introspection
        wrapper._gs_string = gs_string_from_source

        # Apply the modified signature to the wrapper
        wrapper.__signature__ = new_sig

        return wrapper

    # Support both @gsfy and @gsfy(modular=True) syntax
    if func is None:
        # Called as @gsfy(modular=True) or @gsfy()
        return decorator
    else:
        # Called as @gsfy (without parentheses)
        return decorator(func)


def crs_gsfy(cls):
    """
    Class decorator that overwrites generators from CRS when GS_MODE is set.
    
    This decorator can be applied to any cryptographic scheme class that uses
    generators (g1, g2). When GS_MODE is set to "PROOF" or "VERIFY", it:
    - Loads the CRS from the GS_CRS environment variable (defaults to "crs.json")
    - Overwrites generator attributes (g1, g2) in the class instance with values from CRS
    
    Usage:
        @crs_gsfy
        class BLS:
            def __init__(self, g2=None):
                if g2 is None:
                    self.g2 = G2Element.random()
                else:
                    self.g2 = g2
        
        @crs_gsfy
        class MyScheme:
            def __init__(self, g1=None, g2=None):
                self.g1 = g1 or G1Element.random()
                self.g2 = g2 or G2Element.random()
    
    Environment variables:
        GS_MODE: Must be "PROOF" or "VERIFY" to activate generator overwriting
        GS_CRS: Path to CRS JSON file (defaults to "crs.json")
    """
    original_init = cls.__init__
    
    def new_init(self, *args, **kwargs):
        # Call original __init__
        original_init(self, *args, **kwargs)
        
        # Check if GS_MODE is set to PROOF or VERIFY
        gs_mode = _get_env_or_python_var("GS_MODE", None)
        if gs_mode in ["PROOF", "VERIFY"]:
            # Load CRS from environment
            crs_file = _get_env_or_python_var("GS_CRS", "crs.json")
            print(f"Warning: Using a preloaded CRS from {crs_file}\nGS_MODE={gs_mode}")
            try:
                with open(crs_file, "r") as f:
                    crs_data = json.load(f)
                crs = CRS.from_json(crs_data)
                
                # Overwrite generators if they exist as instance attributes
                # g1 from CRS (u1[0])
                if hasattr(self, 'g1'):
                    self.g1 = crs.g1
                
                # g2 from CRS (v1[0])
                if hasattr(self, 'g2'):
                    self.g2 = crs.g2
                    
            except Exception as e:
                print(f"Warning: Error loading CRS for generator overwriting: {e}")
                # Continue with original generators if CRS loading fails
    
    cls.__init__ = new_init
    return cls