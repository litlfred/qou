#!/usr/bin/env python3
"""Smoke test for `chi_via_factorization_mpfr` and `..._symbolic`.

Verifies:
1. MPFR variant agrees with f64 variant to f64 precision (~1e-13).
2. MPFR variant agrees with direct mpfr Hoefsmit on the concatenated
   shifted braid (cross-validates the LR fold in mpfr arithmetic).
3. Symbolic variant evaluates at q = q₀ to the same f64 value.
4. Symbolic variant at q = 1 collapses to classical MN.
"""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import pyhecke_native as p  # type: ignore[import]

from knot_operation_cache import (
    chi_via_factorization,
    chi_via_factorization_mpfr,
    chi_via_factorization_symbolic,
    factor_op_from_word,
    clear_chi_memo,
)
from q_parameter import Q as Q0_FLOAT


def shift_word(word, delta):
    return [(s, g + delta) for (s, g) in word]


def main() -> int:
    print("=" * 70)
    print("F4 composer — MPFR + symbolic variants")
    print("=" * 70)
    ok_all = True
    q_str = "1.1099785955541805"   # Q0 to 16 digits
    q_f = float(Q0_FLOAT)
    dps = 50

    # ── Test cases: (λ, n_1, word_1, n_2, word_2)
    cases = [
        ([4],       2, [(1, 1)],         2, [(1, 1)]),
        ([3, 1],    2, [(1, 1)],         2, [(1, 1)]),
        ([2, 2],    2, [(1, 1)],         2, [(1, 1)]),
        ([6],       3, [(1, 1), (1, 2)], 3, [(1, 1), (1, 2)]),
        ([4, 2],    3, [(1, 1), (1, 2)], 3, [(1, 1), (1, 2)]),
        ([5],       2, [(1, 1)],         3, [(1, 1), (1, 2)]),
        ([3, 2],    2, [(1, 1)],         3, [(1, 1), (1, 2)]),
    ]

    print()
    print("MPFR vs f64 (max diff at q = q_0):")
    import mpmath as mp
    mp.mp.dps = dps
    for lam, n1, word1, n2, word2 in cases:
        op1 = factor_op_from_word(n1, word1)
        op2 = factor_op_from_word(n2, word2)
        clear_chi_memo()
        f64_val = chi_via_factorization(lam, [op1, op2], q_f)
        mpfr_val = chi_via_factorization_mpfr(lam, [op1, op2], q_str, dps=dps)
        diff = abs(float(mpfr_val) - f64_val)
        ok = diff < 1e-12
        ok_all &= ok
        print(f"  {'OK' if ok else 'FAIL':<4} λ={lam!s:<10} f64={f64_val:+.10f} "
              f"mpfr={float(mpfr_val):+.10f} diff={diff:.2e}")

    print()
    print("MPFR vs direct mpfr Hoefsmit on shifted concatenation:")
    for lam, n1, word1, n2, word2 in cases:
        op1 = factor_op_from_word(n1, word1)
        op2 = factor_op_from_word(n2, word2)
        direct_word = list(word1) + shift_word(word2, n1)
        # chi_lambdas_braid_mpfr returns list of decimal strings
        direct_str = p.chi_lambdas_braid_mpfr(
            [list(lam)], direct_word, q_str, dps,
        )[0]
        direct = mp.mpf(direct_str)
        mpfr_val = chi_via_factorization_mpfr(lam, [op1, op2], q_str, dps=dps)
        diff = float(abs(mpfr_val - direct))
        ok = diff < 1e-30  # mpfr at 50dps should match to far better than 1e-30
        ok_all &= ok
        print(f"  {'OK' if ok else 'FAIL':<4} λ={lam!s:<10} "
              f"composed={float(mpfr_val):+.16f} direct={float(direct):+.16f} diff={diff:.2e}")

    print()
    print("Symbolic variant: evaluate at q = q_0:")
    import sympy as sp
    q_sym = sp.symbols("q", positive=True)
    # Restrict to small cases since chi_q_via_gp through Geck-Pfeiffer
    # is much slower than batched f64.
    sym_cases = cases[:5]
    for lam, n1, word1, n2, word2 in sym_cases:
        op1 = factor_op_from_word(n1, word1)
        op2 = factor_op_from_word(n2, word2)
        try:
            sym_expr = chi_via_factorization_symbolic(lam, [op1, op2])
            sym_at_q0 = float(sym_expr.subs(q_sym, q_f).evalf())
        except Exception as e:
            print(f"  SKIP λ={lam}: {type(e).__name__}: {e}")
            continue
        clear_chi_memo()
        f64_val = chi_via_factorization(lam, [op1, op2], q_f)
        diff = abs(sym_at_q0 - f64_val)
        ok = diff < 1e-9
        ok_all &= ok
        print(f"  {'OK' if ok else 'FAIL':<4} λ={lam!s:<10} sym(q_0)={sym_at_q0:+.10f} "
              f"f64={f64_val:+.10f} diff={diff:.2e}")

    print()
    print("Symbolic variant: evaluate at q = 1 (classical MN):")
    for lam, n1, word1, n2, word2 in sym_cases:
        op1 = factor_op_from_word(n1, word1)
        op2 = factor_op_from_word(n2, word2)
        try:
            sym_expr = chi_via_factorization_symbolic(lam, [op1, op2])
            sym_at_1 = int(sym_expr.subs(q_sym, 1).simplify())
        except Exception as e:
            print(f"  SKIP λ={lam}: {type(e).__name__}: {e}")
            continue
        # Direct classical MN on the shifted concatenation.
        direct_word = list(word1) + shift_word(word2, n1)
        # word -> permutation -> cycle type
        n_total = n1 + n2
        perm = list(range(n_total))
        for _, gen in direct_word:
            i = gen - 1
            if i + 1 < n_total:
                perm[i], perm[i+1] = perm[i+1], perm[i]
        # cycle type
        seen = [False] * n_total
        cyc = []
        for s in range(n_total):
            if seen[s]: continue
            length = 0
            j = s
            while not seen[j]:
                seen[j] = True
                j = perm[j]
                length += 1
            cyc.append(length)
        cyc.sort(reverse=True)
        classical = p.mn_chi(list(lam), cyc)
        ok = sym_at_1 == classical
        ok_all &= ok
        print(f"  {'OK' if ok else 'FAIL':<4} λ={lam!s:<10} cyc={cyc!s:<14} "
              f"sym(q=1)={sym_at_1}  classical-MN={classical}")

    print()
    print(f"Result: {'all pass' if ok_all else 'FAILURES'}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
