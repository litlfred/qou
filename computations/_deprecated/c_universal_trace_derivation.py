#!/usr/bin/env python3
"""
Closed-form derivation of c — the universal triple Markov trace at H_9(q).

Per the ⟨Φ_q⟩ structural reduction, the binding-energy coupling α
depends on c = |tr_M(triple-atom-braid)| at q=1 MN, which (per
gs_filtration_e2_probe.py) is universal across triple-types
(ppp/ppn/pnn/nnn all give 8.83e-04 at q=1 MN).

This script computes c **explicitly** via the Schur-Weyl sum:
    c = Σ_{λ ⊢ 9, len ≤ 2} w_λ(q_0) · χ^λ_MN(σ_triple)

emitting:
  - per-partition contributions (5 partitions: (9), (8,1), (7,2), (6,3), (5,4))
  - the underlying cycle type σ_triple
  - structural form of the partial sum

Goal: a closed-form Laurent polynomial in q evaluated at q_0.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath
import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from per_braid_tower_hybrid import q0
from murnaghan_nakayama import (
    cycle_type_of_permutation, permutation_from_braid_word,
    atomic_braid_word, mn_character,
)
from schur_weyl_mpmath import q_factorial_mp


def hook_product_q(lam: tuple, q: mpmath.mpf) -> mpmath.mpf:
    if not lam:
        return mpmath.mpf(1)
    qi = 1 / q
    rows = len(lam)
    hp = mpmath.mpf(1)
    for i in range(rows):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, rows) if lam[r] > j)
            h = arm + leg + 1
            hp *= (q ** h - qi ** h) / (q - qi)
    return hp


def schur_at_two_vars(lam: tuple, q: mpmath.mpf) -> mpmath.mpf:
    """s_λ(q, q^{-1}) for length ≤ 2; vanishes for length > 2."""
    if not lam:
        return mpmath.mpf(1)
    if len(lam) == 1:
        n = lam[0]
        return sum(q ** (n - 2 * k) for k in range(n + 1))
    if len(lam) == 2:
        a, b = lam
        # s_(a,b)(q, q^{-1}) = (q^(a+1)·q^(-b) - q^b·q^(-(a+1))) / (q - q^{-1})
        numer = q ** (a + 1) * q ** (-b) - q ** b * q ** (-(a + 1))
        return numer / (q - 1 / q)
    return mpmath.mpf(0)


def w_lambda(lam: tuple, q: mpmath.mpf) -> mpmath.mpf:
    s = schur_at_two_vars(lam, q)
    if s == 0:
        return mpmath.mpf(0)
    return s / hook_product_q(lam, q)


def main():
    print("=" * 88)
    print("Closed-form derivation of c = universal triple Markov trace")
    print("=" * 88)
    print(f"  q_0 = {float(q0):.10f}")
    print()

    # Compute the cycle type of the atom-triple braid (3 nucleons of
    # one type — at q=1 MN, type doesn't matter, just cycle structure)
    Z, N = 3, 0
    n_strands = 3 * (Z + N)
    word = atomic_braid_word(Z, N, include_inter=True)
    perm = permutation_from_braid_word(word, n_strands)
    cyc = cycle_type_of_permutation(perm)
    print(f"  Atom-triple braid (Z=3, N=0; H_9):")
    print(f"    n_strands = {n_strands}")
    print(f"    permutation cycle type σ = {cyc}")
    print()

    # Enumerate length-≤-2 partitions of 9
    parts = []
    for first in range(9, -1, -1):
        if first == 0:
            break
        if first <= 9 and first >= (9 - first):
            parts.append((first,) if 9 - first == 0 else (first, 9 - first))
    parts = [p for p in parts if sum(p) == 9 and (len(p) == 1 or p[0] >= p[1])]
    # Manual enumeration: (9), (8,1), (7,2), (6,3), (5,4)
    parts = [(9,), (8, 1), (7, 2), (6, 3), (5, 4)]
    print(f"  Length-≤-2 partitions of 9: {parts}")
    print()

    print(f"  {'λ':<10} {'w_λ(q_0)':>20} {'χ^λ_MN(σ)':>10} {'contribution':>20}")
    print("  " + "-" * 70)
    total = mpmath.mpf(0)
    contribs = []
    for lam in parts:
        w = w_lambda(lam, q0)
        chi = mn_character(lam, cyc)
        contrib = w * mpmath.mpf(chi)
        total += contrib
        print(f"  {str(lam):<10} {float(w):>20.6e} {chi:>10} "
              f"{float(contrib):>20.6e}")
        contribs.append({"partition": list(lam),
                          "w_lambda_q0": float(w),
                          "chi_MN": int(chi),
                          "contribution": float(contrib)})

    print("  " + "-" * 70)
    print(f"  c = Σ contributions = {float(total):.10e}")
    print()
    print(f"  (Compare with empirical 8.832670e-04)")
    print()

    # Symbolic version: compute c as a Laurent polynomial in q
    print("  ── Symbolic Schur-Weyl sum (c as polynomial in q) ──")
    q_sym = sp.Symbol("q", positive=True)
    qi_sym = 1 / q_sym

    def hook_q_sym(lam):
        rows = len(lam)
        hp = sp.Integer(1)
        for i in range(rows):
            for j in range(lam[i]):
                arm = lam[i] - j - 1
                leg = sum(1 for r in range(i + 1, rows) if lam[r] > j)
                h = arm + leg + 1
                hp *= (q_sym ** h - qi_sym ** h) / (q_sym - qi_sym)
        return hp

    def schur_2var_sym(lam):
        if len(lam) == 1:
            n = lam[0]
            return sum(q_sym ** (n - 2 * k) for k in range(n + 1))
        a, b = lam
        return (q_sym ** (a + 1) * qi_sym ** b
                  - q_sym ** b * qi_sym ** (a + 1)) / (q_sym - qi_sym)

    sym_total = sp.Integer(0)
    print(f"  {'λ':<10} {'w_λ(q) symbolic':<60}")
    print("  " + "-" * 70)
    for lam in parts:
        w_sym = sp.cancel(schur_2var_sym(lam) / hook_q_sym(lam))
        chi = mn_character(lam, cyc)
        sym_total += w_sym * sp.Integer(int(chi))
        print(f"  {str(lam):<10} {sp.simplify(w_sym)}")

    sym_total_simplified = sp.cancel(sym_total)
    print()
    print(f"  Symbolic c(q) = {sym_total_simplified}")
    print()
    eval_q0 = float(sym_total_simplified.subs(q_sym, sp.Rational(str(q0))))
    print(f"  Symbolic c at q_0 = {eval_q0:.10e}  (consistency check)")

    out = {
        "computation": "c-universal-trace-derivation",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q_0": float(q0),
        "cycle_type": list(cyc),
        "partitions": [list(p) for p in parts],
        "per_partition_contributions": contribs,
        "c_numerical": float(total),
        "c_symbolic_at_q0": eval_q0,
        "c_symbolic_form": str(sym_total_simplified),
        "interpretation": (
            "Closed-form Schur-Weyl sum for the universal triple Markov "
            "trace c. Sum is over length-≤-2 partitions of 9 (five "
            "partitions) with q-Plancherel weights and MN characters "
            "on the atom-triple braid cycle type. Result is a Laurent "
            "polynomial in q evaluated at q_0."
        ),
    }
    p_out = (Path(__file__).parent.parent.parent
             / "docs/audits/2026-05-02-c-universal-trace-derivation.witness.json")
    p_out.write_text(json.dumps(out, indent=2, default=str))
    print()
    print(f"Witness: {p_out.relative_to(Path(__file__).parent.parent.parent)}")


if __name__ == "__main__":
    main()
