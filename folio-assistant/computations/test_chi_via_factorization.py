#!/usr/bin/env python3
"""Smoke test for `chi_via_factorization` (F4 composer, Phase 2).

Verifies that the LR-based composer agrees with direct Hoefsmit on
the concatenated braid:

  χ_λ(β_1 ⊗ β_2) ≟ direct χ_λ(β_1 · shift(β_2))

where `shift(β_2)` shifts every generator index of β_2 by n_1 so
the two sub-braids act on disjoint strands.

Usage:
    python3 test_chi_via_factorization.py
"""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import pyhecke_native as p  # type: ignore[import]

from knot_operation_cache import chi_via_factorization, factor_op_from_word
from q_parameter import Q as Q0_FLOAT


def shift_word(word: list[tuple[int, int]], delta: int) -> list[tuple[int, int]]:
    """Add `delta` to every generator index in a braid word."""
    return [(s, g + delta) for (s, g) in word]


def run_case(name: str, lam: list[int], n1: int, word1: list, n2: int, word2: list,
             q: float = float(Q0_FLOAT), tol: float = 1e-8) -> bool:
    op1 = factor_op_from_word(n1, word1, discovered_by="test")
    op2 = factor_op_from_word(n2, word2, discovered_by="test")

    # Direct: shift word2 by n1, concatenate, call Hoefsmit.
    direct_word = list(word1) + shift_word(word2, n1)
    direct = float(p.chi_lambda_braid(list(lam), direct_word, q))

    composed = chi_via_factorization(lam, [op1, op2], q)

    diff = abs(direct - composed)
    ok = diff < max(tol, tol * abs(direct))
    print(f"  {'OK' if ok else 'FAIL':<4} {name:<40} "
          f"direct={direct:+.10f} composed={composed:+.10f} diff={diff:.2e}")
    return ok


def main() -> int:
    print("=" * 70)
    print("F4 composer smoke test: chi_via_factorization vs direct Hoefsmit")
    print("=" * 70)
    print(f"q_0 = {Q0_FLOAT}")
    print()

    ok_all = True

    # n_1 = n_2 = 2, λ ⊢ 4.
    print("Two 2-strand factors → 4-strand:")
    for lam in [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]:
        ok_all &= run_case(
            f"λ={lam}, β_1=σ_1, β_2=σ_1",
            lam, n1=2, word1=[(1, 1)], n2=2, word2=[(1, 1)],
        )

    print()
    print("Two 3-strand factors → 6-strand:")
    for lam in [[6], [5, 1], [3, 3], [2, 2, 1, 1]]:
        ok_all &= run_case(
            f"λ={lam}, β_1=σ_1·σ_2, β_2=σ_1·σ_2",
            lam, n1=3, word1=[(1, 1), (1, 2)], n2=3, word2=[(1, 1), (1, 2)],
        )

    print()
    print("Asymmetric factors (n_1=2, n_2=3 → n=5):")
    for lam in [[5], [3, 2], [2, 1, 1, 1]]:
        ok_all &= run_case(
            f"λ={lam}, β_1=σ_1, β_2=σ_1·σ_2",
            lam, n1=2, word1=[(1, 1)], n2=3, word2=[(1, 1), (1, 2)],
        )

    # Empty factor (β_1 = identity on 2 strands).
    print()
    print("With identity factor (β_1 = empty word on 2 strands):")
    for lam in [[5], [3, 2]]:
        ok_all &= run_case(
            f"λ={lam}, β_1=identity, β_2=σ_1·σ_2",
            lam, n1=2, word1=[], n2=3, word2=[(1, 1), (1, 2)],
        )

    print()
    print(f"Result: {'all pass' if ok_all else 'FAILURES'}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
