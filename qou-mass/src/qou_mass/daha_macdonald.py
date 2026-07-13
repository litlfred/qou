import sys
import numpy as np
import json
import hashlib
import os

def arm_length(partition, i, j):
    """i, j are 0-indexed row and column"""
    return partition[i] - 1 - j

def leg_length(partition, i, j):
    """i, j are 0-indexed row and column"""
    # count how many rows below i have length > j
    count = 0
    for r in range(i + 1, len(partition)):
        if partition[r] > j:
            count += 1
        else:
            break
    return count

def macdonald_principal_eval(partition, q, t):
    """
    Evaluates P_lambda(1, t, t^2, ...) using the hook-length product:
    P_lambda(t^rho; q, t) = t^{n(lambda)} \prod_{x \in lambda} \frac{1 - q^{a(x)} t^{l(x)+1}}{1 - q^{a(x)+1} t^{l(x)}}
    
    Actually, we might need to normalize it so that y_emptyset = 1 and sum y_lambda = 1 (Plancherel),
    or just use this as the weight in the generating function.
    """
    n_lambda = sum(i * partition[i] for i in range(len(partition)))
    res = t**n_lambda
    
    for i, row in enumerate(partition):
        for j in range(row):
            a = arm_length(partition, i, j)
            l = leg_length(partition, i, j)
            num = 1.0 - (q**a) * (t**(l + 1))
            den = 1.0 - (q**(a + 1)) * (t**l)
            res *= (num / den)
            
    return res

if __name__ == "__main__":
    q0 = 1.10997858
    
    # We test various t choices. 
    # For DAHA / Toroidal in this context, t is often q^N, or maybe -q, or 1/q.
    t_choices = {
        "t = q": q0,
        "t = q^2": q0**2,
        "t = 1/q": 1.0/q0,
        "t = -q": -q0,
        "t = -1/q": -1.0/q0
    }
    
    results = {}
    print("Testing DAHA/Macdonald principal evaluations for c_2 (partition [2])")
    
    partition = [2]
    for label, t_val in t_choices.items():
        y_2 = macdonald_principal_eval(partition, q0, t_val)
        print(f"{label}: P_[2](t^rho; q, t) = {y_2:.5f}")
        results[label] = y_2

    witness_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "computations", "qbeta", "qbeta-daha-macdonald.witness.json")
    with open(__file__, "rb") as f:
        script_hash = hashlib.sha256(f.read()).hexdigest()[:12]
        
    witness_data = {
        "script_hash": script_hash,
        "q0": q0,
        "results": results,
        "conclusion": "Checking if any natural t gives -1"
    }
    
    with open(witness_path, "w") as f:
        json.dump(witness_data, f, indent=2)
    print(f"Witness saved to {witness_path}")
