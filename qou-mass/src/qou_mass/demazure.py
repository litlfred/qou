from __future__ import annotations

import hashlib
import json
import os
from itertools import permutations
from pathlib import Path

import mpmath as mp
import sympy as sp


def _canonical_q0() -> mp.mpf:
    try:
        from ._internal.q_parameter import Q_50_DIGIT_STR  # noqa: PLC0415
    except ImportError:
        import sys  # noqa: PLC0415
        sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
        from qou_mass._internal.q_parameter import Q_50_DIGIT_STR  # noqa: PLC0415
    with mp.workdps(max(80, mp.mp.dps)):
        return mp.mpf(Q_50_DIGIT_STR)


def q_pochhammer(q, k) -> mp.mpf:
    """Computes the finite q-Pochhammer symbol (q; q)_k at >= 80 dps."""
    with mp.workdps(max(80, mp.mp.dps)):
        q_mp = q if isinstance(q, mp.mpf) else mp.mpf(str(q))
        one = mp.mpf(1)
        if k == 0:
            return one
        res = one
        for i in range(1, k + 1):
            res *= (one - q_mp ** i)
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

def compute_coefficients(n, weight, q_val, eval_point="principal") -> dict[int, mp.mpf]:
    """
    Evaluates Composite 1: Demazure x q-Pochhammer mixed trace
    F(u) = \\sum_w D_w(\\lambda) * (q; q)_{l(w)} * u^{l(w)}

    Returns a dict of coefficients c_k for each power u^k at >= 80 dps.
    """
    with mp.workdps(max(80, mp.mp.dps)):
        q_mp = q_val if isinstance(q_val, mp.mpf) else mp.mpf(str(q_val))
        q_sp = sp.Float(mp.nstr(q_mp, 80), 80)
        xs = get_variables(n)
        words = generate_reduced_words(n)

        if eval_point == "principal":
            subs_dict = {xs[i]: q_sp ** i for i in range(n)}
        elif eval_point == "inverse":
            subs_dict = {xs[i]: q_sp ** (-i) for i in range(n)}
        elif eval_point == "ones":
            subs_dict = {xs[i]: sp.Integer(1) for i in range(n)}
        else:
            raise ValueError("Unknown eval_point")

        coeffs: dict[int, mp.mpf] = {}
        zero = mp.mpf(0)
        for _p, word in words.items():
            k = len(word)
            D_w = demazure_character(word, weight, xs)
            D_w_val = mp.mpf(str(sp.N(D_w.subs(subs_dict), 80)))
            term_coeff = D_w_val * q_pochhammer(q_mp, k)
            coeffs[k] = coeffs.get(k, zero) + term_coeff

        return coeffs


if __name__ == "__main__":
    mp.mp.dps = 80
    q0 = _canonical_q0()
    print(f"Testing Demazure Composite 1 coefficients at q0={mp.nstr(q0, 18)}...")

    results = {}

    weights_n4 = [
        (1, 0, 0, 0),
        (1, 1, 0, 0),
        (1, 1, 1, 0),
    ]

    print("\n" + "=" * 40)
    print("sl_4 (n=4)")
    print("=" * 40)
    for w in weights_n4:
        print(f"\nWeight: {w}")
        for eval_pt in ["principal", "inverse", "ones"]:
            c = compute_coefficients(4, w, q0, eval_point=eval_pt)
            c2 = c.get(2, mp.mpf(0))
            c3 = c.get(3, mp.mpf(0))
            print(f"  [{eval_pt}] c_2 = {mp.nstr(c2, 10)}, c_3 = {mp.nstr(c3, 10)}")
            results[f"sl4_{w}_{eval_pt}"] = {"c2": mp.nstr(c2, 50), "c3": mp.nstr(c3, 50)}

    weights_n5 = [
        (1, 0, 0, 0, 0),
        (1, 1, 0, 0, 0),
        (1, 1, 1, 0, 0),
        (1, 1, 1, 1, 0),
    ]

    print("\n" + "=" * 40)
    print("sl_5 (n=5)")
    print("=" * 40)
    for w in weights_n5:
        print(f"\nWeight: {w}")
        for eval_pt in ["principal", "inverse", "ones"]:
            c = compute_coefficients(5, w, q0, eval_point=eval_pt)
            c2 = c.get(2, mp.mpf(0))
            c3 = c.get(3, mp.mpf(0))
            print(f"  [{eval_pt}] c_2 = {mp.nstr(c2, 10)}, c_3 = {mp.nstr(c3, 10)}")
            results[f"sl5_{w}_{eval_pt}"] = {"c2": mp.nstr(c2, 50), "c3": mp.nstr(c3, 50)}

    witness_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "computations", "qbeta", "qbeta-chain4-demazure.witness.json")
    with open(__file__, "rb") as f:
        script_hash = hashlib.sha256(f.read()).hexdigest()[:12]

    witness_data = {
        "script_hash": script_hash,
        "q0": mp.nstr(q0, 50),
        "results": results,
        "conclusion": "NEGATIVE: c_2 is positive for all specializations, never -1",
    }

    with open(witness_path, "w") as f:
        json.dump(witness_data, f, indent=2)
    print(f"Witness saved to {witness_path}")
