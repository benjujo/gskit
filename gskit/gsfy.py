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
                        source_file: str, base_name: str):
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
            definitions[var.name] = collected_values[var.name].__json__()
        for const in constants:
            definitions[const.name] = collected_values[const.name].__json__()
        
        compiled = r.compile_proof(definitions, crs, "elements")
        with open(output_file, 'w') as f:
            f.write(compiled)
    else:
        with open(proof_output_file, "r") as f:
            definitions = json.load(f)
        
        compiled = r.compile_verify(definitions, crs, "elements")
        with open(verify_output_file, 'w') as f:
            f.write(compiled)
    
    return result


def _process_modular_mode(func: Callable, result: any, collected_values: dict, 
                         source_file: str, base_name: str):
    """
    Modular mode: register with global GSContext instead of compiling immediately.
    """
    gs_string = collected_values.get('GS_STRING', None)
    if not gs_string:
        return result
    
    # Get module name from source file
    module_name = os.path.splitext(os.path.basename(source_file))[0]
    func_name = func.__name__
    
    # Extract variables and constants that are referenced in GS_STRING
    # We need to parse the GS_STRING to know which variables/constants to collect
    parser = GSParser()
    try:
        parsed = parser.parse(gs_string)
        transformer = ASTTransformer()
        ast = transformer.transform(parsed)
        
        # Collect only the variables and constants that appear in GS_STRING
        variable_values = {}
        for var in ast.vars:
            if var.name in collected_values and collected_values[var.name] is not None:
                variable_values[var.name] = collected_values[var.name]
        
        for const in ast.consts:
            if const.name in collected_values and collected_values[const.name] is not None:
                variable_values[const.name] = collected_values[const.name]
        
        # Register with global context
        context = GSContext.get_instance()
        context.register_function(
            func_name=func_name,
            module_name=module_name,
            gs_string=gs_string,
            variable_values=variable_values
        )
        
    except Exception as e:
        print(f"Warning: Error processing GS_STRING in modular mode: {e}")
        # Continue execution even if GS processing fails
    
    return result


def gsfy(func: Optional[Callable] = None, *, modular: bool = False):
    """
    Decorator for Groth-Sahai proof generation.
    
    Supports two modes:
    - Modular mode (default): Registers with global GSContext for composition
    - Legacy mode: Processes and compiles immediately (backward compatible)
    
    Usage:
        @gsfy                    # Modular mode (default)
        @gsfy(modular=True)      # Explicit modular mode
        @gsfy(modular=False)     # Legacy mode
    
    Args:
        func: Function to decorate (when used as @gsfy)
        modular: If True, register with global context; if False, compile immediately
    
    Environment variables (can be set in shell or Python):
        GS_MODE: Must be "PROOF" or "VERIFY" (required for legacy mode)
        GS_OUTPUT: Output file for proof compilation
        GS_PROOF_OUTPUT: Proof JSON file (verify mode)
        GS_VERIFY_OUTPUT: Verify output file
        GS_CRS: CRS file path
    """
    def decorator(f: Callable):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # Check if we're in VERIFY mode and need to inject dummy values for witnesses
            gs_mode = _get_env_or_python_var("GS_MODE", None)
            if gs_mode == "VERIFY":
                # Extract GS_STRING and identify witness variables
                gs_string, witness_vars = _extract_gs_string_and_witnesses(f)
                
                if witness_vars:
                    # Get function signature to see which parameters are witness variables
                    sig = inspect.signature(f)
                    param_names = list(sig.parameters.keys())
                    
                    # Determine which parameters are provided via args
                    # (accounting for 'self' if it's a method)
                    num_positional = len(args)
                    provided_by_args = set(param_names[:num_positional])
                    
                    # Parameters provided via kwargs
                    provided_by_kwargs = set(kwargs.keys())
                    
                    # For witness variables that are function parameters, inject dummy values
                    # if they're not provided (or are None)
                    # In VERIFY mode, witness variables (like 'signature') are not available to the verifier
                    # (they only have Groth-Sahai proof commitments), so we use dummy values to allow
                    # the function to execute and extract constants needed for GS compilation
                    for witness_var in witness_vars:
                        if witness_var in sig.parameters:
                            # Check if provided via positional or keyword arguments
                            is_provided = (witness_var in provided_by_args or 
                                         witness_var in provided_by_kwargs)
                            
                            # Check if it's explicitly None (if provided via kwargs)
                            is_none = (witness_var in kwargs and kwargs[witness_var] is None)
                            
                            # Inject dummy if not provided, or if explicitly None
                            if not is_provided or is_none:
                                dummy_value = _create_dummy_value_for_type(witness_var, gs_string)
                                kwargs[witness_var] = dummy_value
            
            # Execute function and capture locals
            result, local_vars = _capture_function_locals(f, *args, **kwargs)
            
            # Collect variable values
            collected_values = _collect_variable_values(f, local_vars)
            
            # Get source file info
            source_file = inspect.getfile(f)
            base_name = os.path.splitext(os.path.basename(source_file))[0]
            
            # Process based on mode
            if modular:
                return _process_modular_mode(f, result, collected_values, source_file, base_name)
            else:
                return _process_legacy_mode(f, result, collected_values, source_file, base_name)
        
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