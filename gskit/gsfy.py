import dis
from functools import wraps
import os
import json
import inspect
from gskit.parser import GSParser
from gskit.ast_builder import ASTTransformer
from gskit.framework import CRS


def gsfy(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        gs_mode = os.environ.get("GS_MODE", None)
        if gs_mode not in ["PROOF", "VERIFY"]:
            print("GS_MODE must be set to PROOF or VERIFY")
            return func(*args, **kwargs)
        
        
        
        source_file = inspect.getfile(func)
        base_name = os.path.splitext(os.path.basename(source_file))[0]
        
        #input_file = os.environ.get("GS_INPUT", f"{base_name}.gs")
        #definitions_file = os.environ.get("GS_DEFINITIONS", f"{base_name}.json")
        output_file = os.environ.get("GS_OUTPUT", f"{base_name}_proof.py")
        proof_output_file = os.environ.get("GS_PROOF_OUTPUT", f"{base_name}_proof.json")
        verify_output_file = os.environ.get("GS_VERIFY_OUTPUT", f"{base_name}_verify.py")
        crs_file = os.environ.get("GS_CRS", f"crs.json")
        
        # Load CRS
        try:
            with open(crs_file, "r") as f:
                crs = json.load(f)
        except Exception as e:
            print(f"Error loading CRS: {e}")
            return func(*args, **kwargs)
            
        
        # Execute the function and capture its local variables dynamically
        local_vars = {}
        
        

        def capture_locals(frame, event, arg):
            """Helper to capture local variables during function execution."""
            if event == "return":
                local_vars.update(frame.f_locals)
            return capture_locals

        # Use sys.settrace to capture locals during execution
        import sys
        sys.settrace(capture_locals)
        result = func(*args, **kwargs)
        sys.settrace(None)

        # Collect variable names from bytecode
        bytecode_vars = {
            instr.argval
            for instr in dis.get_instructions(func)
            if instr.opname in {"LOAD_FAST", "STORE_FAST", "LOAD_GLOBAL", "STORE_GLOBAL"}
        }

        # Match bytecode variables to their runtime values
        collected_values = {var: local_vars.get(var, None) for var in bytecode_vars}
        #print("Variables and Values:", collected_values)
        
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

    return wrapper