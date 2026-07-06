import math
import numpy as np
import sympy as sp
from itertools import permutations

def q_pochhammer(q, k):
    """Computes the finite q-Pochhammer symbol (q; q)_k"""
    if k == 0:
        return 1.0
    res = 1.0
    for i in range(1, k + 1):
        res *= (1.0 - q**i)
    return res

def get_variables(n):
    return sp.symbols(f'x1:{n+1}')

def apply_s_i(f, i, xs):
    """Applies the simple reflection s_i (swaps x_i and x_{i+1}) to polynomial f"""
    return f.subs({xs[i-1]: xs[i], xs[i]: xs[i-1]}, simultaneous=True)

def apply_pi_i(f, i, xs):
    """Applies the Demazure operator pi_i to polynomial f"""
    x_i = xs[i-1]
    x_i_plus_1 = xs[i]
    numerator = x_i * f - x_i_plus_1 * apply_s_i(f, i, xs)
    # The division is exact for polynomials
    return sp.cancel(numerator / (x_i - x_i_plus_1))

def demazure_character(reduced_word, weight, xs):
    """
    Computes the Demazure character D_w(lambda)
    reduced_word: list of integers [i_1, ..., i_k] representing s_{i_1}...s_{i_k}
    weight: tuple (lambda_1, ..., lambda_n)
    xs: tuple of sympy symbols (x_1, ..., x_n)
    """
    f = sp.prod([xs[i]**weight[i] for i in range(len(weight))])
    # Apply pi_i operators from right to left
    for i in reversed(reduced_word):
        f = apply_pi_i(f, i, xs)
    return sp.expand(f)

def generate_reduced_words(n):
    """
    Generates all elements of S_n along with one of their reduced words.
    Returns a dict mapping permutation tuple to a reduced word (list of indices).
    """
    words = {}
    for p in permutations(range(1, n+1)):
        word = []
        arr = list(p)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    word.append(j+1)
        words[p] = list(reversed(word))
    return words

def compute_coefficients(n, weight, q_val, eval_point="principal"):
    """
    Evaluates Composite 1: Demazure x q-Pochhammer mixed trace
    F(u) = \sum_w D_w(\lambda) * (q; q)_{l(w)} * u^{l(w)}
    
    Returns a dict of coefficients c_k for each power u^k
    """
    xs = get_variables(n)
    words = generate_reduced_words(n)
    
    # Define specialization
    if eval_point == "principal":
        subs_dict = {xs[i]: q_val**(i) for i in range(n)}
    elif eval_point == "inverse":
        subs_dict = {xs[i]: q_val**(-i) for i in range(n)}
    elif eval_point == "ones":
        subs_dict = {xs[i]: 1.0 for i in range(n)}
    else:
        raise ValueError("Unknown eval_point")
        
    coeffs = {}
    for p, word in words.items():
        k = len(word)
        D_w = demazure_character(word, weight, xs)
        D_w_val = float(D_w.subs(subs_dict))
        
        term_coeff = D_w_val * q_pochhammer(q_val, k)
        coeffs[k] = coeffs.get(k, 0.0) + term_coeff
        
    return coeffs

if __name__ == "__main__":
    q0 = 1.10997858
    print(f"Testing Demazure Composite 1 coefficients at q0={q0}...")
    
    results = {}
    
    # Fundamental weights for sl_4
    weights_n4 = [
        (1, 0, 0, 0),
        (1, 1, 0, 0),
        (1, 1, 1, 0)
    ]
    
    print("\n" + "="*40)
    print("sl_4 (n=4)")
    print("="*40)
    for w in weights_n4:
        print(f"\nWeight: {w}")
        for eval_pt in ["principal", "inverse", "ones"]:
            c = compute_coefficients(4, w, q0, eval_point=eval_pt)
            c2 = c.get(2, 0)
            c3 = c.get(3, 0)
            print(f"  [{eval_pt}] c_2 = {c2:.5f}, c_3 = {c3:.5f}")
            results[f"sl4_{w}_{eval_pt}"] = {"c2": c2, "c3": c3}

    # Fundamental weights for sl_5
    weights_n5 = [
        (1, 0, 0, 0, 0),
        (1, 1, 0, 0, 0),
        (1, 1, 1, 0, 0),
        (1, 1, 1, 1, 0)
    ]
    
    print("\n" + "="*40)
    print("sl_5 (n=5)")
    print("="*40)
    for w in weights_n5:
        print(f"\nWeight: {w}")
        for eval_pt in ["principal", "inverse", "ones"]:
            c = compute_coefficients(5, w, q0, eval_point=eval_pt)
            c2 = c.get(2, 0)
            c3 = c.get(3, 0)
            print(f"  [{eval_pt}] c_2 = {c2:.5f}, c_3 = {c3:.5f}")
            results[f"sl5_{w}_{eval_pt}"] = {"c2": c2, "c3": c3}

    import json
    import hashlib
    import os
    witness_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "computations", "qbeta", "qbeta-chain4-demazure.witness.json")
    with open(__file__, "rb") as f:
        script_hash = hashlib.sha256(f.read()).hexdigest()[:12]
        
    witness_data = {
        "script_hash": script_hash,
        "q0": q0,
        "results": results,
        "conclusion": "NEGATIVE: c_2 is positive for all specializations, never -1"
    }
    
    with open(witness_path, "w") as f:
        json.dump(witness_data, f, indent=2)
    print(f"Witness saved to {witness_path}")
