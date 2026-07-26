#!/usr/bin/env python3
r"""
wlambda_covariance_epic_A2_nu_nm1_closed_form.py — the second (TAIL) instance in closed form:
`ν_{n-1} = Cov_Planch(N_{n-1}, ω₃)` (qou-x631, qou-ogrk, A2 / FMP tail sub-target).

Companion to the `ν_n` closed form (2026-07-26-tail-first-instance). Extends the same locality
mechanism to the next top hook value `v = n-1`, whose carriers are the `n-1` "one-cell-off-the-cross"
diagrams — the single row `(n)`, the single column `(1^n)`, and the two-corner shapes `(a,2,1^{c})`
— each with `N_{n-1} = 1`. The exact `Fraction` covariance is identified (exact polynomial fit against
the carrier-family central binomial `C(2n-6,n-3)`, verified on all `n = 4..40`) as

    ν_{n-1} = (n-1)(n-4)(n³ - 11n² + 32n - 30) · C(2n-6, n-3) / (3·n!)

**Sign structure (the point).** With `C(2n-6,n-3) > 0`, `(n-1) > 0`, `(n-4) ≥ 0` (`n ≥ 4`), the sign
is that of the cubic `n³ - 11n² + 32n - 30`, which has a *single* real root at `ρ ≈ 7.078` (two
complex). Hence

    ν_{n-1} < 0   for n = 5, 6, 7    (−4/3, −5/3, −1/6),
    ν_{n-1} = 0   at n = 4,
    ν_{n-1} > 0   for n ≥ 8.

This **sharpens the (TAIL) conjecture** `ν_v ≥ 0 for v > n/2 + O(1)`: for the `v = n-1` slice the
positive tail is *empty* (the last sign change is at the very top, `T(n) = n`) for all `n ≤ 7`, and
only from `n = 8` does `v = n-1` join the positive tail. So the `+O(1)` offset is genuinely nontrivial
— it cannot be absorbed into `n/2`, and the tail-onset at this slice is pinned by the single real root
`ρ ≈ 7.078` of the cubic.

HONESTY. A derived + exactly-verified closed form (carrier family exhaustively confirmed `n ≤ 25`;
formula exact `n ≤ 40`) — the second derived (TAIL) instance after `ν_n`. It does NOT prove (TAIL),
FMP, A2, or the kernel; it constrains the tail-onset. scope-(a); no fit wired; nothing wired; no `c_k`;
L2 unchanged (2/7).

# Ref: [manuscript] docs/audits/2026-07-26-covariance-kernel-A2-nu-nm1-closed-form.md
# Ref: [ivanov-olshanski] https://arxiv.org/abs/math/0304010
"""
from __future__ import annotations

import math
import sys
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

NMAX = 40


def parts(n, m=None):
    m = n if m is None else m
    if n == 0:
        yield (); return
    for i in range(min(n, m), 0, -1):
        for r in parts(n - i, i):
            yield (i,) + r


def conj(l):
    return [sum(1 for p in l if p > j) for j in range(l[0])] if l else []


def hook_mult(l):
    l = list(l); c = conj(l); cnt = {}
    for i, row in enumerate(l):
        for j in range(row):
            h = (row - j) + (c[j] - i) - 1
            cnt[h] = cnt.get(h, 0) + 1
    return cnt


def dim(l):
    l = list(l); c = conj(l); d = 1
    for i, row in enumerate(l):
        for j in range(row):
            d *= (row - j) + (c[j] - i) - 1
    return math.factorial(sum(l)) // d


def contentsq(l):
    return sum((j - i) ** 2 for i, row in enumerate(l) for j in range(row))


def nu_v_exact(n, v):
    """ν_v = Cov_Planch(N_v, ω₃) = E₂[N_v·ω₃]  (E₂[ω₃]=0)."""
    fact = math.factorial(n)
    tot = Fr(0)
    carriers = []
    C2 = n * (n - 1) // 2
    for l in parts(n):
        hc = hook_mult(l)
        Nv = hc.get(v, 0)
        if Nv == 0:
            continue
        d = dim(l)
        tot += Fr(d * d * Nv * (contentsq(l) - C2), fact)
        carriers.append((l, Nv))
    return tot, carriers


def is_carrier_family(l):
    """single row (n), single column (1^n), or two-corner (a,2,1^c)."""
    l = list(l)
    if len(l) == 1:                       # single row (n)
        return True
    if all(x == 1 for x in l):            # single column (1^n)
        return True
    return l[1] == 2 and l[0] >= 2 and all(x == 1 for x in l[2:])


def closed_form(n):
    return Fr((n - 1) * (n - 4) * (n ** 3 - 11 * n ** 2 + 32 * n - 30) * math.comb(2 * n - 6, n - 3),
              3 * math.factorial(n))


def main() -> int:
    print("=== Covariance-kernel epic (qou-x631) — ν_{n-1} closed form (TAIL, v=n-1) ===\n")
    formula_ok = True
    carrier_ok = True
    sign = {}
    for n in range(4, NMAX + 1):
        exact, carriers = nu_v_exact(n, n - 1)
        cf = closed_form(n)
        formula_ok &= (exact == cf)
        if n <= 25:
            carrier_ok &= all(is_carrier_family(l) and Nv == 1 for l, Nv in carriers)
            carrier_ok &= (len(carriers) == n - 1)
        sign[n] = '+' if exact > 0 else ('0' if exact == 0 else '-')
        if n <= 9 or n in (20, 30, 40):
            print(f"n={n:2d}: ν_{n-1} = {str(exact):>20}  closed-form match={exact == cf}  sign={sign[n]}")

    print(f"\nclosed form  ν_(n-1) = (n-1)(n-4)(n³-11n²+32n-30)·C(2n-6,n-3)/(3·n!)")
    print(f"  exact match n=4..{NMAX}: {formula_ok}")
    print(f"  carrier family (row+column+(a,2,1^c), each N=1, count n-1) verified n≤25: {carrier_ok}")
    print(f"  sign onset: {''.join(sign[n] for n in range(4, 12))}  (n=4..11) — <0 for n=5,6,7, >0 for n≥8")
    print(f"  ⇒ (TAIL) tail is EMPTY (T(n)=n) for n≤7 at this slice; onset pinned by cubic root ρ≈7.078")

    ok = formula_ok and carrier_ok
    print(f"\nRESULT: ν_(n-1) closed form derived + exactly verified, carrier family confirmed: {ok}")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-covariance-epic-A2-nu-nm1-closed-form", engine="python-exact")
        w.set_description(
            "Second (TAIL) instance in closed form (qou-x631, qou-ogrk, A2/FMP): "
            "ν_{n-1}=Cov_Planch(N_{n-1},ω₃)=(n-1)(n-4)(n³-11n²+32n-30)·C(2n-6,n-3)/(3·n!). Carriers of "
            "hook length n-1 are the n-1 one-cell-off-the-cross diagrams (single row (n), single column "
            "(1^n), two-corner (a,2,1^c)), each N_{n-1}=1 (verified n≤25). Closed form exact n≤40. Sign "
            "= sign of the cubic n³-11n²+32n-30 (single real root ρ≈7.078): ν_{n-1}<0 for n=5,6,7, =0 at "
            "n=4, >0 for n≥8. SHARPENS (TAIL) ν_v≥0 for v>n/2+O(1): the v=n-1 tail is EMPTY (T(n)=n) for "
            "n≤7, so the +O(1) offset is nontrivial. Second derived TAIL instance after ν_n. Does NOT "
            "prove (TAIL)/FMP/A2/kernel. scope-(a); no fit wired; nothing wired; no c_k; L2 2/7.")
        w.add_data("nu_nm1_closed_form", "(n-1)(n-4)(n^3-11n^2+32n-30)*C(2n-6,n-3)/(3*n!)")
        w.add_data("exact_match_n_le_40", bool(formula_ok))
        w.add_data("carrier_family_verified_n_le_25", bool(carrier_ok))
        w.add_data("sign_negative_for", "n=5,6,7")
        w.add_data("sign_zero_at", "n=4")
        w.add_data("sign_positive_for", "n>=8")
        w.add_data("cubic_single_real_root", "rho ~ 7.078 (n^3-11n^2+32n-30)")
        w.add_data("tail_onset_sharpening", "T(n)=n (empty tail) for n<=7 at slice v=n-1; +O(1) nontrivial")
        w.add_assertion(
            "covariance_epic_A2_nu_nm1_closed_form",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("ν_{n-1}=(n-1)(n-4)(n³-11n²+32n-30)C(2n-6,n-3)/(3n!): exact n≤40, carrier family "
                    "(row+col+(a,2,1^c)) confirmed n≤25. Sign flips at n=8 (cubic root ρ≈7.078), "
                    "sharpening (TAIL). No fit wired; no c_k."))
        out = w.save()
        print(f"\nWitness: {out}")
    except ImportError as e:
        print(f"\n(witness skipped — witness_base unavailable: {e})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
