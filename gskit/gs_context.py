"""
Global context for modular Groth-Sahai DSL collection.
Allows multiple @gsfy decorated functions to contribute to a single GS proof system.
"""
import os
import json
from typing import Dict, List, Optional
from gskit.parser import GSParser
from gskit.ast_builder import ASTTransformer
from gskit.framework import CRS


class GSContext:
    """
    Global context that collects GS_STRING fragments and variables from multiple
    decorated functions. Provides methods to merge and compile them together.
    """
    
    _instance: Optional['GSContext'] = None
    
    def __init__(self):
        self.gs_strings: List[str] = []  # List of GS_STRING fragments
        self.variable_values: Dict[str, any] = {}  # Collected variable values across all functions
        self.function_registry: List[Dict] = []  # Metadata about each decorated function
        self._finalized = False
        
    @classmethod
    def get_instance(cls) -> 'GSContext':
        """Get or create the singleton instance."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    @classmethod
    def reset(cls):
        """Reset the context (useful for testing or multiple runs)."""
        cls._instance = None
    
    def register_function(self, func_name: str, module_name: str, gs_string: str, 
                          variable_values: Dict[str, any]):
        """
        Register a decorated function's GS_STRING and variables.
        
        Args:
            func_name: Name of the decorated function
            module_name: Name of the module/file containing the function
            gs_string: The GS_STRING from this function
            variable_values: Dictionary of variable names to their values
        """
        if self._finalized:
            raise RuntimeError("Cannot register functions after context is finalized")
        
        self.gs_strings.append(gs_string)
        self.variable_values.update(variable_values)
        self.function_registry.append({
            'func_name': func_name,
            'module_name': module_name,
            'gs_string': gs_string
        })
    
    def merge_gs_strings(self) -> str:
        """
        Merge all GS_STRING fragments into a single combined GS_STRING.
        Handles deduplication of variables and constants.
        
        Returns:
            Combined GS_STRING ready for parsing
        """
        if not self.gs_strings:
            return None
        
        # Parse each fragment to extract components
        parser = GSParser()
        all_vars = {}  # name -> (type, source_module)
        all_consts = {}  # name -> (type, source_module)
        all_eqs = []  # List of equation strings
        
        for i, gs_string in enumerate(self.gs_strings):
            try:
                parsed = parser.parse(gs_string)
                transformer = ASTTransformer()
                ast = transformer.transform(parsed)
                
                # Collect variables
                for var in ast.vars:
                    if var.name in all_vars:
                        # Check for type conflicts
                        existing_type = type(var).__name__
                        new_type = type(var).__name__
                        if existing_type != new_type:
                            raise ValueError(
                                f"Variable '{var.name}' has conflicting types: "
                                f"{existing_type} vs {new_type}"
                            )
                    else:
                        all_vars[var.name] = (var, self.function_registry[i]['module_name'])
                
                # Collect constants
                for const in ast.consts:
                    if const.name in all_consts:
                        existing_type = type(const).__name__
                        new_type = type(const).__name__
                        if existing_type != new_type:
                            raise ValueError(
                                f"Constant '{const.name}' has conflicting types: "
                                f"{existing_type} vs {new_type}"
                            )
                    else:
                        all_consts[const.name] = (const, self.function_registry[i]['module_name'])
                
                # Collect equations from AST
                for eq in ast.eqs:
                    # Reconstruct equation string from AST
                    eq_parts = []
                    for mul_eq in eq.eq_muls:
                        if mul_eq.gamma:
                            eq_parts.append(f"{mul_eq.left} * {mul_eq.right} * {mul_eq.gamma}")
                        else:
                            eq_parts.append(f"{mul_eq.left} * {mul_eq.right}")
                    eq_str = " + ".join(eq_parts) + f" = {eq.target}"
                    all_eqs.append(eq_str)
                            
            except Exception as e:
                raise RuntimeError(
                    f"Error parsing GS_STRING from {self.function_registry[i]['module_name']}: {e}"
                )
        
        # Build the merged GS_STRING
        var_lines = []
        for var_name, (var, _) in all_vars.items():
            # Determine type string from variable class
            if 'G1' in type(var).__name__:
                var_type = 'G1'
            elif 'G2' in type(var).__name__:
                var_type = 'G2'
            elif 'Zp' in type(var).__name__:
                var_type = 'ZP'
            else:
                var_type = 'ZP'  # default
            var_lines.append(f"    {var_name}: {var_type}")
        
        const_lines = []
        for const_name, (const, _) in all_consts.items():
            # Determine type string from constant class
            if 'G1' in type(const).__name__:
                const_type = 'G1'
            elif 'G2' in type(const).__name__:
                const_type = 'G2'
            elif 'GT' in type(const).__name__:
                const_type = 'GT'
            elif 'Zp' in type(const).__name__:
                const_type = 'ZP'
            else:
                const_type = 'ZP'  # default
            const_lines.append(f"    {const_name}: {const_type}")
        
        merged = "variables:\n"
        merged += "\n".join(var_lines) if var_lines else "    # No variables"
        merged += "\n\nconstants:\n"
        merged += "\n".join(const_lines) if const_lines else "    # No constants"
        merged += "\n\nequations:\n"
        merged += "\n    ".join(all_eqs) if all_eqs else "    # No equations"
        merged += "\n"
        
        return merged
    
    def finalize(self, output_file: Optional[str] = None, 
                 proof_output_file: Optional[str] = None,
                 verify_output_file: Optional[str] = None,
                 crs_file: Optional[str] = None) -> Dict:
        """
        Finalize the context by merging all GS_STRINGs and compiling.
        
        Args:
            output_file: Output file for proof compilation
            proof_output_file: Input file for verify mode (contains proof JSON)
            verify_output_file: Output file for verify compilation
            crs_file: Path to CRS JSON file
            
        Returns:
            Dictionary with 'compiled_proof' and/or 'compiled_verify' code
        """
        if self._finalized:
            raise RuntimeError("Context already finalized")
        
        gs_mode = os.environ.get("GS_MODE", None)
        if gs_mode not in ["PROOF", "VERIFY"]:
            raise ValueError("GS_MODE must be set to PROOF or VERIFY")
        
        # Set default file names if not provided
        if output_file is None:
            output_file = os.environ.get("GS_OUTPUT", "combined_proof.py")
        if proof_output_file is None:
            proof_output_file = os.environ.get("GS_PROOF_OUTPUT", "combined_proof.json")
        if verify_output_file is None:
            verify_output_file = os.environ.get("GS_VERIFY_OUTPUT", "combined_verify.py")
        if crs_file is None:
            crs_file = os.environ.get("GS_CRS", "crs.json")
        
        # Load CRS
        try:
            with open(crs_file, "r") as f:
                crs = json.load(f)
        except Exception as e:
            raise RuntimeError(f"Error loading CRS from {crs_file}: {e}")
        
        # Merge GS_STRINGs
        merged_gs_string = self.merge_gs_strings()
        if not merged_gs_string:
            raise RuntimeError("No GS_STRING fragments to merge")
        
        # Parse and transform
        parser = GSParser()
        parsed = parser.parse(merged_gs_string)
        transformer = ASTTransformer()
        ast = transformer.transform(parsed)
        
        # Type check
        ast.type_check()
        
        result = {}
        
        if gs_mode == "PROOF":
            # Create definitions from collected variable values
            definitions = {}
            for var in ast.vars:
                if var.name not in self.variable_values:
                    raise ValueError(f"Variable '{var.name}' not found in collected values")
                definitions[var.name] = self.variable_values[var.name].__json__()
            
            for const in ast.consts:
                if const.name not in self.variable_values:
                    raise ValueError(f"Constant '{const.name}' not found in collected values")
                definitions[const.name] = self.variable_values[const.name].__json__()
            
            compiled = ast.compile_proof(definitions, crs, "elements")
            result['compiled_proof'] = compiled
            
            with open(output_file, 'w') as f:
                f.write(compiled)
            
        else:  # VERIFY mode
            with open(proof_output_file, "r") as f:
                definitions = json.load(f)
            
            compiled = ast.compile_verify(definitions, crs, "elements")
            result['compiled_verify'] = compiled
            
            with open(verify_output_file, 'w') as f:
                f.write(compiled)
        
        self._finalized = True
        return result
    
    def get_merged_string(self) -> str:
        """Get the merged GS_STRING without finalizing."""
        return self.merge_gs_strings()
    
    def clear(self):
        """Clear all collected data (useful for testing)."""
        self.gs_strings.clear()
        self.variable_values.clear()
        self.function_registry.clear()
        self._finalized = False


def finalize_gs_context(output_file: str = None, 
                        proof_output_file: str = None,
                        verify_output_file: str = None,
                        crs_file: str = None) -> Dict:
    """
    Convenience function to finalize the global GS context.
    Call this after all @gsfy decorated functions have been executed.
    
    Args:
        output_file: Output file for proof compilation
        proof_output_file: Input file for verify mode (contains proof JSON)
        verify_output_file: Output file for verify compilation
        crs_file: Path to CRS JSON file
        
    Returns:
        Dictionary with compilation results
    """
    context = GSContext.get_instance()
    return context.finalize(
        output_file=output_file,
        proof_output_file=proof_output_file,
        verify_output_file=verify_output_file,
        crs_file=crs_file
    )

