from gskit.elements import (
    Element,
    ZpElement,
    G1Element, # pairing function as method on G1Element
    G2Element,
    GTElement,
    g1,
    g2,)
from functools import reduce
from itertools import islice
import operator
import subprocess

import json
class ElementEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Element):
            return obj.__json__()
        return json.JSONEncoder.default(self, obj)

import random
import time

element_types = {1:"G1",
                 2:"G2",
                 0:"ZP",
                 3:"GT"}


def generate_variable(var_type):
    if var_type == "G1":
        return G1Element.random()
    elif var_type == "G2":
        return G2Element.random()
    elif var_type == "ZP":
        return ZpElement.random()
    
def generate_constant(const_type):
    if const_type == "G1":
        return G1Element.random()
    elif const_type == "G2":
        return G2Element.random()
    elif const_type == "ZP":
        return ZpElement.random()
    elif const_type == "GT":
        return GTElement.random()

def _generate_eqmul(eq_type, a):
    pass

def generate_equation(eq_type, vars):
    if eq_type == "PPE":
        for var in vars:
            pass
    else:
        return None

    
def generate_snippet_eq(var_qty, eq_qty):
    variables1 = {}
    variables2 = {}
    constants = {}
    eqs = [dict() for _ in range(eq_qty)]
    eqs_str = []
    
    for i in range(var_qty//2):
        var = generate_variable("G1")
        variables1[f"v1_{i}"] = var
    
    for i in range(var_qty//2, var_qty):
        var = generate_variable("G2")
        variables2[f"v2_{i}"] = var
    
    for e in range(eq_qty):
        for k,v in variables1.items():
            const = generate_constant("G2")
            constants[f"c{e}_{k}"] = const
            
            eqs[e][f"{k} * c{e}_{k}"] = v.pair(const)
            
            
        for k,v in variables2.items():
            const = generate_constant("G1")
            constants[f"c{e}_{k}"] = const
            
            eqs[e][f"c{e}_{k} * {k}"] = const.pair(v)
            
        eq = " + ".join(eqs[e].keys()) + f" = t{e}"
        t = reduce(operator.mul, eqs[e].values(), GTElement.zero())
        constants[f"t{e}"] = t
        eqs_str.append(eq)
    
    # Create the snippet
    snippet = (
        "variables:\n" +
        "".join([f"    {var_name}: {element_types[var.type]}\n" for var_name, var in variables1.items()]) +
        "".join([f"    {var_name}: {element_types[var.type]}\n" for var_name, var in variables2.items()]) +
        "\nconstants:\n" +
        "".join([f"    {const_name}: {element_types[const.type]}\n" for const_name, const in constants.items()]) +
        "\n\nequations:\n" +
        "".join([f"    {eq}\n" for eq in eqs_str])
    )

    return snippet, {**variables1, **variables2}, constants
    

def generate_snippet(var_qty, eq_qty):
    if eq_qty > 0:
        return generate_snippet_eq(var_qty, eq_qty)
    variables = {}
    constants = {}
    partials_eq = {}
    
    for i in range(var_qty//2):
        var = generate_variable("G1")
        variables[f"v{i}"] = var
        const = generate_constant("G2")
        constants[f"c{i}"] = const
        
        partials_eq[f"v{i} * c{i}"] = var.pair(const)
        
        
    for i in range(var_qty//2, var_qty):
        var = generate_variable("G2")
        variables[f"v{i}"] = var
        const = generate_constant("G1")
        constants[f"c{i}"] = const
        
        partials_eq[f"c{i} * v{i}"] = const.pair(var)
        
    eq = " + ".join(partials_eq.keys()) + " = t"
    t = reduce(operator.mul, partials_eq.values(), GTElement.zero())
    constants["t"] = t
    
    # Create the snippet
    snippet = (
        "variables:\n" +
        "".join([f"    {var_name}: {element_types[var.type]}\n" for var_name, var in variables.items()]) +
        "\nconstants:\n" +
        "".join([f"    {const_name}: {element_types[const.type]}\n" for const_name, const in constants.items()]) +
        "\n\nequations:\n" +
        f"    {eq}\n"
    )

    return snippet, variables, constants


def save_snippet(snippet, variables, constants, filename):
    with open(filename + ".gs", "w") as f:
        f.write(snippet)
    with open(filename + ".json", "w") as f:
        json.dump({
            **{var_name: var for var_name, var in variables.items()},
            **{const_name: const for const_name, const in constants.items()}
        }, f, cls=ElementEncoder)
        
def ppe_var_qty():
    for i in range(10):
        snippet, variables, constants = generate_snippet(10*(i+1), 0)
        save_snippet(snippet, variables, constants, "generated_snippets/snippet_" + str(i+1))
        
    for i in range(10):
        start_time = time.time()
        process = subprocess.run(["gskit", "prove", "-i", f"generated_snippets/snippet_{i+1}.gs", "-d", f"generated_snippets/snippet_{i+1}.json", "-c", "crs.json", "-o", f"generated_snippets/snippet_proof_{i+1}.py", "-p", f"generated_snippets/snippet_proof_{i+1}.json", "-f"])
        proof_time_stamp = time.time()
        vprocess = subprocess.run(["gskit", "verify", "-i", f"generated_snippets/snippet_{i+1}.gs", "-d", f"generated_snippets/snippet_proof_{i+1}.json", "-o", f"generated_snippets/snippet_verify_{i+1}.py", "-f"])
        verify_time_stamp = time.time()
        
        proof_time = round((proof_time_stamp - start_time)*1000)
        verify_time = round((verify_time_stamp - proof_time_stamp)*1000)
        with open("generated_snippets/times.json", "a") as f:
            print(f"'s{i+1}': {{'proof_time': {proof_time}, 'verify_time': {verify_time}}}", file=f)
        
def ppe_eq_qty():
    for i in range(10):
        snippet, variables, constants = generate_snippet(30, (i+1))
        save_snippet(snippet, variables, constants, "generated_snippets/eq_snippet_" + str(i+1))
        
    for i in range(10):
        start_time = time.time()
        process = subprocess.run(["gskit", "prove", "-i", f"generated_snippets/eq_snippet_{i+1}.gs", "-d", f"generated_snippets/eq_snippet_{i+1}.json", "-c", "crs.json", "-o", f"generated_snippets/eq_snippet_proof_{i+1}.py", "-p", f"generated_snippets/eq_snippet_proof_{i+1}.json", "-f"])
        proof_time_stamp = time.time()
        vprocess = subprocess.run(["gskit", "verify", "-i", f"generated_snippets/eq_snippet_{i+1}.gs", "-d", f"generated_snippets/eq_snippet_proof_{i+1}.json", "-o", f"generated_snippets/eq_snippet_verify_{i+1}.py", "-f"])
        verify_time_stamp = time.time()
        
        proof_time = round((proof_time_stamp - start_time)*1000)
        verify_time = round((verify_time_stamp - proof_time_stamp)*1000)
        with open("generated_snippets/eq_times.json", "a") as f:
            print(f"'s{i+1}': {{'proof_time': {proof_time}, 'verify_time': {verify_time}}}", file=f)


if __name__ == "__main__":
    #ppe_var_qty()
    ppe_eq_qty()

