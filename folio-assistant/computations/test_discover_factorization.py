#!/usr/bin/env python3
"""Smoke test for `discover_factorization` (F4 Phase 3).

Verifies that:
1. Words with disjoint generator-index ranges split into per-component
   factors.
2. Each factor has correctly re-based generator indices.
3. The sum of factor strand counts equals n.
4. Round-trip via `chi_via_factorization` matches direct Hoefsmit on
   the original word — confirming the factorization is mathematically
   equivalent (not just structurally split).
5. Entangled words (no tensor structure) return a single op.

Usage:
    python3 test_discover_factorization.py
"""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import pyhecke_native as p  # type: ignore[import]

from knot_operation_cache import (
    discover_factorization,
    chi_via_factorization,
    clear_chi_memo,
)
from q_parameter import Q as Q0_FLOAT


def main() -> int:
    print("=" * 70)
    print("F4 Phase 3: discover_factorization smoke test")
    print("=" * 70)
    ok_all = True
    q = float(Q0_FLOAT)

    # ── Case 1: three disjoint singletons σ_1 ⊕ σ_3 ⊕ σ_5 on n=6.
    word = [(1, 1), (1, 3), (1, 5)]
    factors = discover_factorization(word, n=6, discovered_by="test")
    n1_ok = len(factors) == 3
    n2_ok = all(f.n == 2 for f in factors)
    n3_ok = all(f.braid_word_normal_form == [(1, 1)] for f in factors)
    print(f"  {'OK' if n1_ok and n2_ok and n3_ok else 'FAIL':<4} "
          f"σ_1⊕σ_3⊕σ_5 → {len(factors)} factors of strand counts "
          f"{[f.n for f in factors]}, words {[f.braid_word_normal_form for f in factors]}")
    ok_all &= (n1_ok and n2_ok and n3_ok)

    # ── Case 2: round-trip via chi_via_factorization on σ_1⊕σ_3⊕σ_5.
    for lam in [[6], [4, 2], [3, 2, 1], [2, 1, 1, 1, 1]]:
        clear_chi_memo()
        composed = chi_via_factorization(lam, factors, q)
        direct = float(p.chi_lambda_braid(list(lam), word, q))
        diff = abs(composed - direct)
        ok = diff < max(1e-8, 1e-8 * abs(direct))
        ok_all &= ok
        print(f"  {'OK' if ok else 'FAIL':<4} σ_1⊕σ_3⊕σ_5 round-trip "
              f"λ={lam!s:<22} direct={direct:+.10f} composed={composed:+.10f} diff={diff:.2e}")

    # ── Case 3: 3+3 split — σ_1·σ_2 ⊕ σ_4·σ_5 on n=6.
    word_a = [(1, 1), (1, 2), (1, 4), (1, 5)]
    factors_a = discover_factorization(word_a, n=6, discovered_by="test")
    case3_struct = (
        len(factors_a) == 2
        and factors_a[0].n == 3 and factors_a[1].n == 3
        and factors_a[0].braid_word_normal_form == [(1, 1), (1, 2)]
        and factors_a[1].braid_word_normal_form == [(1, 1), (1, 2)]
    )
    print(f"  {'OK' if case3_struct else 'FAIL':<4} σ_1σ_2⊕σ_4σ_5 → "
          f"{len(factors_a)} factors, structure {[(f.n, f.braid_word_normal_form) for f in factors_a]}")
    ok_all &= case3_struct
    for lam in [[6], [4, 2], [3, 2, 1]]:
        clear_chi_memo()
        composed = chi_via_factorization(lam, factors_a, q)
        direct = float(p.chi_lambda_braid(list(lam), word_a, q))
        diff = abs(composed - direct)
        ok = diff < max(1e-8, 1e-8 * abs(direct))
        ok_all &= ok
        print(f"  {'OK' if ok else 'FAIL':<4} 3+3 round-trip "
              f"λ={lam!s:<10} direct={direct:+.10f} composed={composed:+.10f} diff={diff:.2e}")

    # ── Case 4: entangled word σ_1·σ_2·σ_1·σ_3 on n=4 → single op.
    word_e = [(1, 1), (1, 2), (1, 1), (1, 3)]
    factors_e = discover_factorization(word_e, n=4, discovered_by="test")
    case4_ok = (
        len(factors_e) == 1
        and factors_e[0].n == 4
        and factors_e[0].braid_word_normal_form == word_e
    )
    print(f"  {'OK' if case4_ok else 'FAIL':<4} entangled σ_1σ_2σ_1σ_3 (n=4) → "
          f"{len(factors_e)} op (full braid preserved)")
    ok_all &= case4_ok

    # ── Case 5: empty word → single empty op.
    factors_empty = discover_factorization([], n=3, discovered_by="test")
    case5_ok = len(factors_empty) == 1 and factors_empty[0].braid_word_normal_form == []
    print(f"  {'OK' if case5_ok else 'FAIL':<4} empty word on n=3 → single empty op")
    ok_all &= case5_ok

    # ── Case 6: trailing identity strand — σ_1·σ_2 on n=4.
    # generator range {1, 2} → strands {1, 2, 3} connected; strand 4 isolated.
    # Two factors: 3-strand (σ_1·σ_2) and 1-strand (identity).
    word_t = [(1, 1), (1, 2)]
    factors_t = discover_factorization(word_t, n=4, discovered_by="test")
    case6_struct = (
        len(factors_t) == 2
        and factors_t[0].n == 3 and factors_t[1].n == 1
        and factors_t[0].braid_word_normal_form == [(1, 1), (1, 2)]
        and factors_t[1].braid_word_normal_form == []
    )
    print(f"  {'OK' if case6_struct else 'FAIL':<4} σ_1σ_2 on n=4 → "
          f"3-strand σ_1σ_2 + 1-strand identity")
    ok_all &= case6_struct

    print()
    print(f"Result: {'all pass' if ok_all else 'FAILURES'}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
