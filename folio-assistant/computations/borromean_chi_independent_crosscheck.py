#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical cross-validation regression.
"""Independent cross-check of the Borromean Markov-trace closed form.

Verifies the per-representation claims of
`content/quantum-observable-universe/mass-theory/borromean-markov-trace-closed-form.md`
(the merged GAP-A-4 result; categorical derivation in PR #1933 T17 Schur-Weyl
R-matrix, content proposition PR #1942) using a **completely independent
method**: the signed Ocneanu-trace engine `homfly_ocneanu_trace`, whose
seminormal characters are validated against the skein-relation reference
(`homflypt_reference_qa.py`, 5/5).

This closes the verification gap flagged in
`docs/audits/2026-06-04-hidden-fitting-verification-gap-mass-binding-walkthrough.md`
§3a: the `tr_M` cluster previously had no EXTERNAL correctness anchor — only
internal cross-method agreement. The Borromean χ^λ closed forms are now
confirmed by two independent derivations:

  - R-matrix / Schur-Weyl on V^⊗3 → Jones polynomial of 𝓑₃  (main, T17)
  - signed seminormal Hecke characters, skein-validated     (this engine)

Both agree to ≥ 1e-48 at every tested q. Claims checked
(`borromean-markov-trace-closed-form.md` lines 93–111):

  χ^{(3)}(β_Bor)   = 1                       (writhe-0, trivial eigenvalue)
  χ^{(1³)}(β_Bor)  = 1                       (writhe-0, sign eigenvalue)
  χ^{(2,1)}(β_Bor) = (−q¹²+3q¹⁰−3q⁸+4q⁶−3q⁴+3q²−1)/q⁶
                   = 2 − 3h⁴ − h⁶            (h = q − q⁻¹)

β_Bor = (σ₁⁻¹σ₂)³ = [-1,2,-1,2,-1,2] (content convention).
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402
from homfly_ocneanu_trace import _chi  # noqa: E402 — signed seminormal character
from witness_base import WitnessBuilder  # noqa: E402

BETA_BOR = [-1, 2, -1, 2, -1, 2]   # (σ₁⁻¹σ₂)³, content convention
TOL = mp.mpf("1e-40")


def _chi21_qform(q):
    """Content's exact q-rational χ^{(2,1)}(β_Bor) (borromean-...-closed-form.md:106)."""
    return (-q**12 + 3*q**10 - 3*q**8 + 4*q**6 - 3*q**4 + 3*q**2 - 1) / q**6


def _chi21_hform(q):
    """The h-series form 2 − 3h⁴ − h⁶ (same line, h = q − q⁻¹)."""
    h = q - 1/q
    return 2 - 3*h**4 - h**6


def main() -> int:
    mp.mp.dps = 50
    print("Independent Borromean χ^λ cross-check "
          "(seminormal engine vs content q-forms)")
    print("=" * 72)
    q_tests = [mp.mpf(s) for s in ("1.07", "1.23", "1.5", "1.10997858275")]
    rows = []
    worst = mp.mpf(0)
    for q in q_tests:
        chi3 = _chi((3,), BETA_BOR, q)
        chi111 = _chi((1, 1, 1), BETA_BOR, q)
        chi21 = _chi((2, 1), BETA_BOR, q)
        d3 = abs(chi3 - 1)
        d111 = abs(chi111 - 1)
        dq = abs(chi21 - _chi21_qform(q))
        dh = abs(chi21 - _chi21_hform(q))
        worst = max(worst, d3, d111, dq, dh)
        ok = max(d3, d111, dq, dh) < TOL
        print(f"  q={mp.nstr(q,8):<14} χ³−1={mp.nstr(d3,2):>8} "
              f"χ¹³−1={mp.nstr(d111,2):>8}  χ²¹ vs q-form={mp.nstr(dq,2):>8}  "
              f"vs 2−3h⁴−h⁶={mp.nstr(dh,2):>8}  {'OK' if ok else '✗'}")
        rows.append({
            "q": mp.nstr(q, 20),
            "chi_3_minus_1": mp.nstr(d3, 4),
            "chi_1cubed_minus_1": mp.nstr(d111, 4),
            "chi_21_vs_qform": mp.nstr(dq, 4),
            "chi_21_vs_hform": mp.nstr(dh, 4),
            "pass": bool(ok),
        })
    all_ok = worst < TOL
    print("=" * 72)
    print(f"  worst deviation = {mp.nstr(worst, 3)}   "
          f"{'ALL AGREE' if all_ok else 'DISAGREEMENT'} (tol {mp.nstr(TOL,1)})")
    print("  → independent confirmation of borromean-markov-trace-closed-form.md "
          "per-rep claims (PR #1933 T17 / #1942).")

    w = WitnessBuilder("borromean-chi-independent-crosscheck", engine="mpmath")
    w.set_content_block("prop:borromean-markov-trace-closed-form")
    w.add_parameter("dps", 50)
    w.add_parameter("beta_bor", "(sigma1^-1 sigma2)^3")
    w.add_parameter("tolerance", mp.nstr(TOL, 2))
    w.add_data("method_a", "R-matrix/Schur-Weyl → Jones (main, T17/#1933)")
    w.add_data("method_b", "signed seminormal Hecke characters, skein-validated "
                           "(homfly_ocneanu_trace; gate homflypt_reference_qa 5/5)")
    w.add_data("checks", rows)
    w.add_data("worst_deviation", mp.nstr(worst, 6))
    w.add_assertion(
        "two_methods_agree",
        computed=1 if all_ok else 0, expected=1,
        source=("χ^{(3)}=χ^{(1³)}=1 and χ^{(2,1)}=2−3h⁴−h⁶ must agree between "
                "the R-matrix derivation (content) and the skein-validated "
                "seminormal-character engine"))
    out = w.save()
    print(f"  Witness: {out.name}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
