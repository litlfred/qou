#!/usr/bin/env python3
# polynomial_q_not_applicable: hyperbolic-geometry numeric probe.
"""one_loop_ohtsuki_5_2_crosscheck_probe.py — the law against a PUBLISHED theorem.

Bean `qou-fl4t` / `qou-pn5j`. Follows the multi-cusp derivation
(`docs/audits/2026-08-07-one-loop-multicusp-derivation.md`) and the per-cusp
dissolution (`docs/audits/2026-08-08-per-cusp-factor-dissolves.md`).

THE GAP THIS CLOSES

The law established there,

    c_sigma = 2^{-1/2} |tau_DG|^{-1/2},

has its constant `k = 2^{-1/2}` fixed at `c = 1` by the figure-eight ALONE, and
is then tested at `c = 2` on the Whitehead link. Both data points come from
this corpus's own colored-Jones extractions. So the `c = 1` anchor rests on a
single manifold, in a quadratic trace field, measured in-house.

This probe adds an INDEPENDENT, PUBLISHED, RIGOROUS `c = 1` data point on a
different manifold: Ohtsuki's asymptotic expansion of the Kashaev invariant of
the `5_2` knot (`library/ki52/ki52.pdf`, Theorem 1.1). His

    <5_2>_N = e^{N zeta} N^{3/2} omega (1 + sum_i kappa_i (2 pi i/N)^i + O(N^{-d-1}))

is a theorem, not a numerical fit, and `omega` is the 1-loop constant. `5_2` is
also two-bridge, so Garoufalidis-Yoon (arXiv:2411.03801 Thm 1.1) prove 1-loop =
adjoint torsion for it — both sides are theorem-backed. And its trace field is
CUBIC of discriminant -23, so a match cannot be a quadratic-field coincidence.

RESULT

    predicted from the law   c_sigma(5_2) = 0.65620337051419987
    Ohtsuki's |omega|                     = 0.65620337047140662

agreeing to 10 digits — the full precision Ohtsuki prints. NOTHING WAS FITTED:
`k` comes from `4_1`, `|tau_DG(5_2)|` from the geometry, and `omega` from the
paper.

A CLOSED FORM FOR THE 5_2 INVARIANT, AS A BY-PRODUCT

Ohtsuki's `omega` is recovered exactly as

    omega = e^{-i pi/4} ((1 - y_0)/(2 y_0 + 1))^{1/2},

`y_0` the root of `(y-1)^3 = y` with positive imaginary part. Since
`|omega|^2 = 1/(2|tau_DG|)`, that gives

    |tau_DG(5_2)| = |2 y_0 + 1| / (2 |y_0 - 1|)

verified here to the full working precision. `y_0` has minimal polynomial
`y^3 - 3y^2 + 2y - 1`, of discriminant -23 — the same discriminant as
`x^3 - x - 1`, i.e. the `5_2` trace field identified independently in PR #4658,
and the field of the ambiguity generator `sqrt(rho)` found in PR #4697.

WHAT THIS DOES AND DOES NOT STRENGTHEN

  * DOES: the `c = 1` leg of the law, which previously rested on `4_1` alone.
    Second manifold, cubic field, published rigorous source, 10 digits.
  * DOES NOT: say anything new about `c`-dependence. `5_2` is one-cusped. The
    only `c = 2` test remains the Whitehead link, and `c = 3` remains
    supporting-only.
  * DOES NOT prove the law. It confirms the constant on an independent point.

Audit-only. No float64 enters the witness.

-- Ref: [ohtsuki-5_2] T. Ohtsuki, On the asymptotic expansion of the Kashaev
        invariant of the 5_2 knot, Quantum Topol. 7 (2016) 669, Theorem 1.1;
        library/ki52/ki52.pdf
-- Ref: [garoufalidis-yoon] arXiv:2411.03801 Thm 1.1 (1-loop = adjoint torsion
        for two-bridge knots; 5_2 is two-bridge)
-- Ref: [dimofte-garoufalidis2013] arXiv:1202.6268, Defn 1.2
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))
from _precision import set_compute_dps, fmt  # noqa: E402
from one_loop_torsion import one_loop  # noqa: E402

set_compute_dps()

# Ohtsuki Theorem 1.1, as printed (10 significant digits each).
OHTSUKI_Y0_RE = "0.3376410213"
OHTSUKI_Y0_IM = "0.5622795120"
OHTSUKI_OMEGA_RE = "0.0901905774"
OHTSUKI_OMEGA_IM = "-0.6499757866"
PRINTED_DIGITS = 10


def main() -> int:
    import snappy

    y0 = mp.findroot(lambda t: (t - 1) ** 3 - t,
                     mp.mpc(OHTSUKI_Y0_RE, OHTSUKI_Y0_IM),
                     tol=mp.mpf(10) ** -120)
    omega = mp.e ** (-mp.pi * 1j / 4) * mp.sqrt((1 - y0) / (2 * y0 + 1))
    paper_omega = mp.mpc(OHTSUKI_OMEGA_RE, OHTSUKI_OMEGA_IM)

    print("A. Ohtsuki Thm 1.1 data, reconstructed from the stated algebra\n")
    print(f"   y_0 (root of (y-1)^3 = y, Im > 0) = {mp.nstr(y0, 22)}")
    print(f"   paper                             = {OHTSUKI_Y0_RE} + i {OHTSUKI_Y0_IM} ...")
    print(f"   omega = e^-i.pi/4 ((1-y_0)/(2y_0+1))^1/2 = {mp.nstr(omega, 20)}")
    print(f"   paper                                    = {OHTSUKI_OMEGA_RE} + i {OHTSUKI_OMEGA_IM} ...")
    d_om = abs(omega - paper_omega)
    print(f"   |difference| = {mp.nstr(d_om, 4)}   "
          f"{'OK — formula recovered' if d_om < mp.mpf('1e-10') else 'MISMATCH'}\n")

    tau = abs(one_loop(snappy.Manifold("5_2")))
    k = 1 / mp.sqrt(2)
    pred = k / mp.sqrt(tau)
    abs_paper = abs(paper_omega)

    print("B. the law, with k calibrated on 4_1 ALONE, predicts 5_2\n")
    print(f"   |tau_DG(5_2)|              = {mp.nstr(tau, 25)}")
    print(f"   c_sigma = 2^-1/2 |tau|^-1/2 = {mp.nstr(pred, 25)}")
    print(f"   Ohtsuki |omega| (printed)   = {mp.nstr(abs_paper, 25)}")
    rel = abs(abs_paper - pred) / pred
    dig = int(-mp.log10(rel)) if rel > 0 else 999
    ok = dig >= PRINTED_DIGITS
    print(f"   relative difference         = {mp.nstr(rel, 6)}  ->  {dig} digits"
          f"   ({'OK, = the ' + str(PRINTED_DIGITS) + ' digits Ohtsuki prints' if ok else 'SHORT'})")
    print("   Nothing fitted: k from 4_1, |tau| from geometry, omega from the paper.\n")

    print("C. closed form for the 5_2 invariant, implied by |omega|^2 = 1/(2|tau|)\n")
    cf = abs((2 * y0 + 1) / (y0 - 1)) / 2
    rel2 = abs(cf - tau) / tau
    print(f"   |2 y_0 + 1| / (2 |y_0 - 1|) = {mp.nstr(cf, 30)}")
    print(f"   |tau_DG(5_2)|               = {mp.nstr(tau, 30)}")
    print(f"   relative difference         = {mp.nstr(rel2, 4)}"
          f"   ({'exact to working precision' if rel2 < mp.mpf(10) ** -50 else 'CHECK'})\n")

    Y = sp.symbols("Y")
    poly = sp.expand((Y - 1) ** 3 - Y)
    disc = sp.discriminant(poly, Y)
    disc_plastic = sp.discriminant(Y ** 3 - Y - 1, Y)
    print("D. the field\n")
    print(f"   min poly of y_0 : {sp.Poly(poly, Y).as_expr()}    disc = {disc}")
    print(f"   x^3 - x - 1 (plastic)                  disc = {disc_plastic}")
    print("   -23 is the 5_2 trace-field discriminant (PR #4658), and the field of")
    print("   the ambiguity generator sqrt(rho) found in PR #4697. A cubic field, so")
    print("   this match is not a quadratic-field coincidence.\n")

    print("-" * 72)
    print("The c = 1 anchor of c_sigma = 2^{-1/2}|tau_DG|^{-1/2} no longer rests on")
    print("4_1 alone. Second manifold, cubic trace field, and the source is a")
    print("published theorem rather than an in-corpus extraction.")
    print()
    print("This says NOTHING new about c-dependence -- 5_2 is one-cusped. The only")
    print("c = 2 test remains the Whitehead link; c = 3 remains supporting-only.")

    wit = {
        "description": (
            "Independent published cross-check of c_sigma = 2^{-1/2}|tau_DG|^{-1/2} "
            "at c = 1 on the 5_2 knot, against Ohtsuki's Theorem 1.1 asymptotic "
            "expansion of the Kashaev invariant. Agreement to 10 digits, the full "
            "precision the paper prints, with nothing fitted. Yields a closed form "
            "|tau_DG(5_2)| = |2y_0+1|/(2|y_0-1|)."
        ),
        "computation": "one_loop_ohtsuki_5_2_crosscheck_probe",
        "audit_only": True,
        "ohtsuki_omega_formula": "e^{-i pi/4} ((1 - y_0)/(2 y_0 + 1))^{1/2}",
        "y0_min_poly": "y^3 - 3 y^2 + 2 y - 1",
        "y0_discriminant": int(disc),
        "y0": fmt(y0),
        "omega_reconstructed": fmt(omega),
        "omega_paper_printed": fmt(paper_omega),
        "omega_formula_recovery_abs_diff": fmt(d_om),
        "tau_dg_5_2": fmt(tau),
        "c_sigma_predicted": fmt(pred),
        "ohtsuki_abs_omega": fmt(abs_paper),
        "relative_difference": fmt(rel),
        "digits_agreement": dig,
        "paper_printed_digits": PRINTED_DIGITS,
        "passes": bool(ok),
        "closed_form": "|tau_DG(5_2)| = |2 y_0 + 1| / (2 |y_0 - 1|)",
        "closed_form_rel_diff": fmt(rel2),
        "scope": (
            "strengthens the c = 1 leg only; 5_2 is one-cusped and this says "
            "nothing new about c-dependence"
        ),
        "bears_on": ["bean qou-fl4t", "bean qou-pn5j", "PR #4658", "PR #4697",
                     "PR #4707", "PR #4708"],
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = (Path(__file__).resolve().parent.parent
           / "one-loop-ohtsuki-5-2-crosscheck.witness.json")
    out.write_text(json.dumps(wit, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWitness: {out.name}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
