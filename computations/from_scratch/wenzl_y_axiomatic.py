#!/usr/bin/env python3
"""From-scratch Wenzl y_λ derivation via Markov axioms — general n.

For H_n(q), we have one Wenzl coefficient y_λ per partition λ ⊢ n.
The number of partitions of n is p(n): p(3)=3, p(4)=5, p(5)=7,
p(6)=11, p(7)=15, ...

Given p(n) unknowns y_λ, we need p(n) linear equations from the
Markov axioms.  For each chosen test element x ∈ H_n with known
tr_M(x), we get the equation

    Σ_λ y_λ · χ_λ(x) = tr_M(x).

The Markov axioms determine tr_M(x) for any x via:

  (M1) tr_M(1) = 1
  (M2) tr_M(xy) = tr_M(yx)                     [cyclic]
  (M3) tr_M(x σ_{n-1}) = z · tr_M(x_{H_{n-1}})  for x ∈ H_{n-1}
  (M4) σ_i² = (q - q⁻¹) σ_i + 1                 [Hecke quadratic]

where z := 1/(q^{1/2} + q^{-1/2}) is the Markov parameter.

This module implements (M1)-(M4) recursively, then solves the
linear system for y_λ given a set of test elements.

NO dependencies on existing folio-assistant compute infrastructure.
"""
from __future__ import annotations
import sympy as sp
from typing import List, Tuple
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from hoefsmit_general import (
    q, partitions_of, syts_of_shape, hoefsmit_sigma_matrix,
    chi_lambda_braid,
)

# Markov parameter
z = 1 / (q**sp.Rational(1, 2) + q**sp.Rational(-1, 2))


def markov_trace_axiomatic(braid_word: list, n: int, depth: int = 0) -> sp.Expr:
    """Compute tr_M of a braid word in H_n(q) via Markov peel.

    Strategy:
      1. If word is empty: return 1.
      2. If any σ_i⁻¹ appears (negative entry), expand σ_i⁻¹ = σ_i - h.
      3. If any σ_i² appears for ANY i, apply Hecke quadratic.
      4. If σ_{n-1} not in word, recurse to H_{n-1}.
      5. If σ_{n-1} at end and rest doesn't involve σ_{n-1}: peel.
      6. Otherwise use cyclic to move σ_{n-1} to the end.

    `depth` tracks recursion depth to prevent unbounded loops.
    """
    if depth > 200:
        raise RuntimeError(f"markov_trace recursion too deep on {braid_word}")
    if not braid_word:
        return sp.Integer(1)
    h_val = q - 1/q
    # Step 2: expand any negative entry
    for i, g in enumerate(braid_word):
        if g < 0:
            pre, suf = braid_word[:i], braid_word[i + 1:]
            return (markov_trace_axiomatic(pre + [-g] + suf, n, depth + 1)
                    - h_val * markov_trace_axiomatic(pre + suf, n, depth + 1))
    # Step 3: any σ_i² (i, i adjacent in word for any i)
    for i in range(len(braid_word) - 1):
        if braid_word[i] == braid_word[i + 1] and braid_word[i] > 0:
            k = braid_word[i]
            pre, suf = braid_word[:i], braid_word[i + 2:]
            return (h_val * markov_trace_axiomatic(pre + [k] + suf, n, depth + 1)
                    + markov_trace_axiomatic(pre + suf, n, depth + 1))
    # Step 4: σ_{n-1} not in word
    if (n - 1) not in [abs(g) for g in braid_word]:
        return markov_trace_axiomatic(braid_word, n - 1, depth + 1)
    # Step 5: σ_{n-1} at end, rest doesn't involve it
    if braid_word[-1] == n - 1 and (n - 1) not in [abs(g) for g in braid_word[:-1]]:
        return z * markov_trace_axiomatic(braid_word[:-1], n - 1, depth + 1)
    # Step 6: σ_{n-1} appears but not at end. Use cyclic to rotate
    # the rightmost element to the front (tr(x · y) = tr(y · x)),
    # which guarantees progress: each rotation moves the rightmost
    # closer to a peelable form, and σ_i² gets caught by step 3.
    rightmost = braid_word[-1]
    rest = braid_word[:-1]
    return markov_trace_axiomatic([rightmost] + rest, n, depth + 1)


def build_chi_matrix(n: int, test_elements: List[List[int]]):
    """Build matrix M[i, λ] = χ_λ(test_elements[i]) for λ ⊢ n."""
    parts = partitions_of(n)
    M = sp.zeros(len(test_elements), len(parts))
    for i, w in enumerate(test_elements):
        for j, lam in enumerate(parts):
            M[i, j] = chi_lambda_braid(lam, w)
    return M, parts


def derive_wenzl_y(n: int, test_elements: List[List[int]] = None,
                   numerical: bool = False, q_value=None) -> dict:
    """Solve for y_λ via Markov axioms, given test elements.

    If test_elements is None, default to a chain of generator products.
    If numerical=True, substitute q→q_value first, solve numerically.
    """
    parts = partitions_of(n)
    if test_elements is None:
        # Use one representative per conjugacy class of S_n (cycle type =
        # partition of n).  The Markov trace on a Hecke element depends
        # on the underlying braid word, but reps from DIFFERENT cycle
        # types give linearly independent χ_λ rows.
        #
        # For S_5 (n=5):
        #   id              = (1^5)         → []
        #   single-trans    = (2,1,1,1)     → [n-1]
        #   2 disjoint trans = (2,2,1)      → [1, n-1]  (σ_1, σ_{n-1} commute)
        #   3-cycle         = (3,1,1)       → [n-2, n-1]
        #   3-cycle + trans = (3,2)         → [1, 2, n-1] (σ_1σ_2 commutes with σ_{n-1})
        #   4-cycle         = (4,1)         → [n-3, n-2, n-1]
        #   5-cycle         = (5)           → [1, 2, 3, n-1] for n=5
        if n == 3:
            test_elements = [[], [2], [1, 2]]
        elif n == 4:
            test_elements = [[], [3], [2, 3], [1, 2, 3], [1, 3]]
        elif n == 5:
            test_elements = [
                [],                    # id (1^5)
                [4],                   # σ_4 (2,1^3)
                [1, 4],                # (2,2,1) — disjoint transpositions
                [3, 4],                # σ_3σ_4 = (3,1,1)
                [1, 2, 4],             # (3,2) — σ_1σ_2 (3-cycle) · σ_4
                [2, 3, 4],             # σ_2σ_3σ_4 = (4,1)
                [1, 2, 3, 4],          # σ_1σ_2σ_3σ_4 = (5)
            ]
        else:
            # Fallback: chain + extras (may be rank-deficient for n≥5)
            test_elements = [[]]
            for k in range(n - 1, 0, -1):
                test_elements.append(list(range(k, n)))
            test_elements = test_elements[:len(parts)]

    print(f"Test elements (M = {len(test_elements)} eqs, λ-count = {len(parts)}):")
    for w in test_elements:
        print(f"  {w}")
    print()

    # Build chi matrix and tr_M vector
    print("Computing χ_λ on test elements (this may take a minute for n=5)...")
    M, parts_list = build_chi_matrix(n, test_elements)
    print("Computing tr_M on test elements via axioms...")
    rhs = sp.Matrix([markov_trace_axiomatic(w, n) for w in test_elements])

    print("\nMarkov-axiom values:")
    for w, val in zip(test_elements, rhs):
        print(f"  tr_M({w}) = {sp.simplify(val)}")
    print()

    if numerical and q_value is not None:
        print(f"Solving linear system numerically at q = {float(q_value):.6f} ...")
        import numpy as np
        M_num = np.array([[float(M[i, j].subs(q, q_value).evalf(30))
                            for j in range(len(parts_list))]
                           for i in range(len(test_elements))])
        rhs_num = np.array([float(rhs[i].subs(q, q_value).evalf(30))
                             for i in range(len(test_elements))])
        y_num = np.linalg.solve(M_num, rhs_num)
        return {parts_list[i]: float(y_num[i]) for i in range(len(parts_list))}
    print("Solving linear system M y = tr_M (symbolic) ...")
    y_vars = sp.symbols(f'y0:{len(parts_list)}')
    eqs = [(M.row(i) * sp.Matrix(y_vars))[0, 0] - rhs[i]
           for i in range(len(test_elements))]
    sol = sp.solve(eqs, y_vars, dict=True)
    if not sol:
        print("  No solution found — system may be singular")
        return None
    sol = sol[0]
    y_map = {parts_list[i]: sp.simplify(sol[y_vars[i]]) for i in range(len(parts_list))}
    return y_map


if __name__ == "__main__":
    print("=" * 78)
    print("Verification: Wenzl y_λ for H_3 from Markov axioms")
    print("=" * 78)
    y3 = derive_wenzl_y(3)
    if y3:
        for lam, y in y3.items():
            q0 = sp.Rational(11099785827513808, 10**16)
            y_q0 = float(y.subs(q, q0).evalf(30))
            print(f"  y_{lam} at q_0 = {y_q0:.6f}")
    print()
    print("Expected (from y-lambda-wenzl-witness.json):")
    print("  y_(3,)      ≈  0.4154")
    print("  y_(2, 1)    ≈  0.2809")
    print("  y_(1, 1, 1) ≈  0.0227")
