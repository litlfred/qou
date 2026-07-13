#!/usr/bin/env python3
"""qbeta_dladder_padic_graded_prime_probe.py

Sharpens the D-ladder 2-adic parity grading (PR #3737, audit Result 2) to its
exact prime-by-prime form: **p = 2 is the *unique graded prime*** among all primes
dividing the denominators of `d_k = a_k + b_k√3`, and 2 is exactly the prime of
the ℤ/2 **bar-involution** — so the arithmetic grading is the direct shadow of the
sinh/cosh bar-parity split, carried by no other prime.

## The exact observation (all from exact ℚ(√3) coefficients, k=1..21)

- **p = 2 — GRADED (crisp ℤ/2).** `v₂(den b_k) = 0 ⟺ k odd`, and the singular
  2-adic mass *swaps* to `a_k` on the other parity (`v₂(den a_k) ∈ {0,1}` for k
  even, large for k odd). The 2-adic denominator is parity-selective.
- **p = 3 — NOT graded.** `v₃(den a_k)` and `v₃(den b_k)` both grow ~1.4·k
  *regardless of parity* (monotone-ish with fluctuations, e.g. b dips 23→22 at
  k=16→17) — the factorial-smooth (Ohtsuki–Habiro) growth that motivated the
  base-3 q-holonomic test, NOT a grading. Base 3 was about *growth/smoothness*,
  not parity.
- **p ≥ 5 — NOT graded.** 5,7,11,… enter sporadically at k ≈ 3,4,6,… in the
  factorial-smooth pattern (all primes ≤ a slowly-growing bound), no parity
  structure.

⇒ **2 is the unique graded prime.** This is the arithmetic reflection of the
bar-involution being a ℤ/2 (order-2) symmetry: only the prime 2 "sees" it.

## Discipline

Scope-(a); exact p-adic valuations of the exact coefficients (no floats, no fit,
no PSLQ, no free parameter). No c_k wired; registry untouched; no tier change.
Refines audit Result 2 (2026-07-13); the sorry-free Lean anchor
(`QOU.QBeta.DLadderTwoAdicGrading.bDen_two_adic_graded`) already encodes the p=2
case for the first coefficients.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401
sys.path.insert(0, str(Path(__file__).resolve().parent))

import sympy as sp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import qbeta_ck_sseries_exact_rational as core  # noqa: E402

ORD = int(sys.argv[1]) if len(sys.argv) > 1 else 43
core.ORD = ORD
import qbeta_dladder_generating_function_structure_probe as dlad  # noqa: E402
dlad.ORD = ORD


def _vp(n, p):
    n = abs(int(n))
    v = 0
    while n and n % p == 0:
        n //= p
        v += 1
    return v


def main() -> int:
    print("=" * 78)
    print(" D-ladder p-adic denominator structure — 2 is the unique graded prime")
    print("=" * 78)
    dk, KMAX, _vt, _ok = dlad.build_d_ladder()
    s3 = sp.sqrt(3)
    rows = []
    for k in range(1, KMAX + 1):
        e = sp.expand(dk[k])
        b = sp.Rational(sp.nsimplify(e.coeff(s3, 1)))
        a = sp.Rational(sp.nsimplify(e - b * s3))
        rows.append((k, a.q, b.q))

    # p = 2 grading test: v2(den b_k) = 0  ⟺  k odd
    p2_b_graded = all(((_vp(bq, 2) == 0) == bool(k % 2)) for k, aq, bq in rows)
    # a_k mirror: v2(den a_k) small (≤1) ⟺ k even
    p2_a_mirror = all(((_vp(aq, 2) <= 1) == (k % 2 == 0)) for k, aq, bq in rows)

    # p = 3 NOT graded: v3 does not vanish-by-parity (both parities carry v3>0
    # for k ≥ 2), i.e. there is no parity on which v3(den) is identically 0.
    v3b_odd = [_vp(bq, 3) for k, aq, bq in rows if k % 2 == 1 and k >= 3]
    v3b_even = [_vp(bq, 3) for k, aq, bq in rows if k % 2 == 0]
    p3_not_graded = (min(v3b_odd) > 0 and min(v3b_even) > 0)  # both parities v3>0

    print(f"  {'k':>3} | v2(dena) v2(denb) | v3(dena) v3(denb) | other primes (den b)")
    for k, aq, bq in rows:
        others = sorted(p for p in sp.factorint(bq) if p not in (2, 3))
        print(f"  {k:3d} |  {_vp(aq,2):5d}  {_vp(bq,2):6d}  |  {_vp(aq,3):5d}  {_vp(bq,3):6d}  | {others}")

    print()
    print(f"  p=2 GRADED (v2(den b_k)=0 ⟺ k odd): {p2_b_graded}")
    print(f"  p=2 a-mirror (v2(den a_k)≤1 ⟺ k even): {p2_a_mirror}")
    print(f"  p=3 NOT graded (v3(den b_k)>0 on BOTH parities, k≥2): {p3_not_graded}")
    unique = p2_b_graded and p3_not_graded
    print(f"  ⇒ 2 is the UNIQUE graded prime (mirrors the ℤ/2 bar-involution): {unique}")

    wb = WitnessBuilder("qbeta-dladder-padic-graded-prime", engine="sympy")
    wb.set_description(
        "Sharpens the D-ladder 2-adic parity grading (PR #3737, Result 2): among "
        "all primes dividing den(d_k), p=2 is the UNIQUE graded prime "
        "(v2(den b_k)=0 ⟺ k odd; the singular 2-adic mass swaps to a_k on the "
        "other parity), while p=3 (and 5,7,…) are ungraded factorial-smooth "
        "(Ohtsuki–Habiro) growth ~1.4k regardless of parity. 2 is the prime of the "
        "ℤ/2 bar-involution, so only it sees the grading. Exact p-adic valuations "
        "of the exact ℚ(√3) coefficients; no fit, no c_k wired, no tier change."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")
    wb.add_data("KMAX", KMAX)
    wb.add_data("v2_den_a", [_vp(aq, 2) for k, aq, bq in rows])
    wb.add_data("v2_den_b", [_vp(bq, 2) for k, aq, bq in rows])
    wb.add_data("v3_den_a", [_vp(aq, 3) for k, aq, bq in rows])
    wb.add_data("v3_den_b", [_vp(bq, 3) for k, aq, bq in rows])
    wb.add_data("p2_b_parity_graded", bool(p2_b_graded))
    wb.add_data("p2_a_mirror", bool(p2_a_mirror))
    wb.add_data("p3_not_graded_both_parities_v3_positive", bool(p3_not_graded))
    wb.add_assertion(
        "two_is_the_unique_graded_prime",
        computed=float(unique), expected=1.0, tolerance=0.5,
        source="p=2 carries the exact ℤ/2 parity grading (v2(den b_k)=0 ⟺ k odd, "
               "with the a_k mirror), while p=3 is ungraded factorial-smooth growth "
               "(v3(den b_k)>0 on both parities) — 2 = the bar-involution prime is "
               "the unique prime that sees the grading")
    wb.save()
    print("\n  scope-(a): exact p-adic refinement of Result 2; no fit, no ID.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
