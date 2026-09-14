#!/usr/bin/env python3
"""qbeta_phib_dual_validity_window_probe.py — WHERE the modular-dual half of
Faddeev Φ_b is numerically inert at the real substrate, and where it is not.

Bean `qou-pdix` (the S1 blocker: derive the Q_β ladder eigenphase α). Its
2026-09-12 route triage recommends **attack B — Faddeev Φ_b / modular double**
as "the textbook bridge for this exact modulus gap" and "the cheapest
formalize-first step of the four". This probe measures what that attack can
actually see at the substrate.

INFRASTRUCTURE / MEASUREMENT. No α derived, no c_k value, no wiring, no fit.

## What is already on main, and what this adds

`qbeta_modular_double_reciprocity.py` (scope-(b), landed 2026-09-07 — five days
BEFORE the triage that recommends attack B) proves

    log q · log q̃ = 4π²        identically in y, where b² = iy

so at the substrate `|log q| = ln q₀ = 0.10434` forces `|log q̃| = 378.36` and
`q̃ ≈ 4.8e-165`. That is a statement about the dual MODULUS.

It is NOT by itself a licence to drop the dual half, and reading it that way is
the trap this probe exists to close. The dual half of the modular-double product
is

    D_b(z) = ∏_{k≥0} ( 1 + e^{−2πi b^{−2}(k+½)} · e^{2π z / b} )

and while the first factor is suppressed by `q̃`, the second GROWS in `z`:
`|1/b| = √(2π/t) ≈ 7.76` at the substrate, so `|e^{2πz/b}| = e^{2π z Re(1/b)}`
with `Re(1/b) ≈ 5.487`. The two compete, and the competition has a FINITE
window — it is not "1e-165, therefore ignore".

`phi_b_substrate_regime.py` supplies `compact_half_product`, explicitly "the
numerator half of the modular-double product only (q̃-half dropped)". This probe
measures the `z`-window in which that drop is safe.

## Derived first (before any evaluation), from the corpus b-map

With `b = √(t/2π)·e^{+iπ/4}` and `t = ln q₀` (the corpus's `b_+` substrate
branch, `phi_b_substrate_regime.b_for_q0`):

    b^{−2} = (2π/t)·e^{−iπ/2} = −i·(2π/t)
    ⇒ the dual phase factor is  e^{−2πi b^{−2}(k+½)} = e^{−(4π²/t)(k+½)},
      real and positive, with |·| = e^{−|log q̃|(k+½)}     ... (i)
    1/b = √(2π/t)·e^{−iπ/4}  ⇒  Re(1/b) = √(2π/t)/√2      ... (ii)

so the k-th dual factor departs from 1 by a term of modulus

    ε_k(z) = exp( −(4π²/t)(k+½) + 2π z Re(1/b) ),

which is largest at k = 0 and monotone increasing in z. Setting ε_0(z) = 10^{−d}
gives the DERIVED window

    z*(d) = [ (4π²/t)/2 − d·ln 10 ] / ( 2π Re(1/b) ).          ... (*)

Every constant in (*) comes from the b-map; none is fitted. The probe computes
(*) and then measures the true departure by evaluating the dual half directly.

## Why this matters for qou-pdix

For |z| < z* the dual half is 1 to the working precision, so at the substrate
Φ_b and the corpus's compact half-product are the SAME FUNCTION there. Any
α-derivation that evaluates Φ_b at the substrate inside that window is therefore
using the compact object, and attack B buys nothing it did not already have —
the modular double is invisible in exactly the region the substrate anchors sit
in. The dual only becomes visible at |z| past z*, which is where the b_+ branch
is also furthest from the anchors.

## What the corpus already held, and what this ADDS

This is a REFINEMENT of an existing corpus claim, not a new one.
`qbeta_fmap_modular_dual_missing_probe.py` already states the conclusion:
"|q~| ~ 0 at the substrate => dual NEGLIGIBLE => Phi_b ~ phi_q here". That
probe reasons from the SIZE of q~ alone -- it evaluates no product, writes no
witness, and contains no occurrence of an argument variable at all. What is
added here is that the inference is not valid as stated, because the k-th
dual factor is 1 + q~^(k+1/2) * e^{2 pi z / b} and the SECOND factor grows in
z at 2 pi Re(1/b) = 34.48 per unit. The existing conclusion is correct inside
a window and carries no statement of one; this supplies the window in closed
form and measures where it ends.

Scope (a): a scope-limited statement about the b_+ substrate branch under the
corpus's own b-map and product convention. It is not a claim about alpha.

**It does NOT weaken attack B on the root-of-unity face, where that attack is
correctly aimed.** The same existing probe measures |q~| = 1 at q = e^{4 pi i/5}
-- the dual is ORDER ONE there, the compact form genuinely fails, and that is
where the Q_beta decay saddle sits. Nothing here touches that. The finding is
narrower and should be quoted narrowly: the modular double is inert AT THE REAL
SUBSTRATE for O(1) arguments, so a bridge motivated by "Phi_b sees both sides"
buys nothing THERE.

Arithmetic: mpmath end to end, proton pin (AGENTS.md 2026-08-07 directive).
No float64 anywhere; `float()` appears nowhere.
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: E402, F401

from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402


def b_plus(q0):
    """Corpus b-map, b_+ branch: b = sqrt(t/2pi) * e^{+i pi/4}, t = ln q0.

    Matches phi_b_substrate_regime.b_for_q0(branch=+1) exactly.
    """
    t = mp.log(q0)
    return mp.sqrt(t / (2 * mp.pi)) * mp.e ** (mp.mpc(0, 1) * mp.pi / 4)


def dual_half_product(z, b, kmax=400):
    """Dual (q-tilde) half of the modular double, the factor the corpus drops:

        D_b(z) = prod_{k>=0} ( 1 + e^{-2 pi i b^{-2} (k+1/2)} * e^{2 pi z / b} ).

    Returned as an mpmath mpc. No truncation heuristic is used for the headline
    numbers: kmax is far beyond where the terms underflow.
    """
    b = mp.mpmathify(b)
    z = mp.mpmathify(z)
    two_pi_i = 2 * mp.pi * mp.mpc(0, 1)
    binv2 = 1 / b ** 2
    growth = mp.e ** (2 * mp.pi * z / b)
    prod = mp.mpc(1)
    for k in range(kmax):
        kk = k + mp.mpf(1) / 2
        term = mp.e ** (-two_pi_i * binv2 * kk) * growth
        prod *= 1 + term
        if mp.fabs(term) < mp.mpf(10) ** (-mp.mp.dps - 10):
            break
    return prod


def main() -> int:
    mp.mp.dps = 60
    q0 = q_at(60)
    t = mp.log(q0)
    b = b_plus(q0)

    # --- the derived quantities of (i), (ii), (*) -------------------------
    log_qtilde = 4 * mp.pi ** 2 / t          # |log q~|, the reciprocity value
    re_binv = mp.re(1 / b)
    slope = 2 * mp.pi * re_binv              # d/dz of ln|e^{2 pi z / b}|

    def z_star(d):
        """Derived window (*): where the k=0 dual term reaches 10^{-d}."""
        return (log_qtilde / 2 - d * mp.log(10)) / slope

    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}\n         {detail}")

    print("=" * 78)
    print(" Faddeev Phi_b: the z-window where the modular-dual half is inert")
    print("=" * 78)
    print(f"  q0 (proton pin) = {mp.nstr(q0, 20)}")
    print(f"  t = ln q0       = {mp.nstr(t, 20)}")
    print(f"  b (b_+ branch)  = {mp.nstr(b, 16)}")
    print(f"  |log q~| = 4pi^2/t = {mp.nstr(log_qtilde, 16)}")
    print(f"  Re(1/b)         = {mp.nstr(re_binv, 16)}")
    print(f"  slope 2pi Re(1/b) = {mp.nstr(slope, 16)}")
    print()

    # --- check 1: the derived dual phase factor is REAL and matches (i) ----
    binv2 = 1 / b ** 2
    phase0 = mp.e ** (-2 * mp.pi * mp.mpc(0, 1) * binv2 * mp.mpf(1) / 2)
    predicted0 = mp.e ** (-log_qtilde / 2)
    rel0 = mp.fabs(phase0 - predicted0) / mp.fabs(predicted0)
    check(
        "dual_phase_factor_matches_the_derived_form",
        rel0 < mp.mpf(10) ** (-45),
        f"k=0 dual phase computed {mp.nstr(phase0, 12)} vs derived "
        f"e^-|log q~|/2 = {mp.nstr(predicted0, 12)}; rel {mp.nstr(rel0, 6)}. "
        f"It is REAL and positive, so the suppression is a pure modulus effect "
        f"-- confirming (i) from the b-map rather than assuming it.",
    )

    # --- check 2: the reciprocity is reproduced independently --------------
    recip = mp.fabs(t) * log_qtilde
    four_pi2 = 4 * mp.pi ** 2
    rel_recip = mp.fabs(recip - four_pi2) / four_pi2
    check(
        "reciprocity_reproduced_independently_of_its_own_producer",
        rel_recip < mp.mpf(10) ** (-50),
        f"|log q| * |log q~| = {mp.nstr(recip, 25)} vs 4pi^2 = "
        f"{mp.nstr(four_pi2, 25)}; rel {mp.nstr(rel_recip, 6)}. Recomputed here "
        f"from the b-map alone, matching qbeta_modular_double_reciprocity.",
    )

    # --- check 3: the DERIVED window (*) predicts the MEASURED departure ---
    # Derived BEFORE evaluating: at z = z*(d) the dual half should sit 10^-d
    # from 1. Measure at three decades and compare.
    rows = []
    worst = mp.mpf(0)
    for d in (16, 30, 50):
        zs = z_star(d)
        D = dual_half_product(zs, b)
        departure = mp.fabs(D - 1)
        target = mp.mpf(10) ** (-d)
        ratio = departure / target
        rows.append(
            {
                "decades_d": d,
                "z_star_derived": mp.nstr(zs, 20),
                "measured_departure": mp.nstr(departure, 12),
                "target_10^-d": mp.nstr(target, 12),
                "ratio_measured_over_target": mp.nstr(ratio, 12),
            }
        )
        print(
            f"    d={d:>3}   z*={mp.nstr(zs, 12):>18}   |D-1|={mp.nstr(departure, 10):>16}"
            f"   ratio={mp.nstr(ratio, 8)}"
        )
        worst = max(worst, mp.fabs(mp.log(ratio) / mp.log(10)))
    # The k-spacing is exp(-4pi^2/t) = 10^-164.3 per step, so the k>=1 tail was
    # DERIVED to be irrelevant before this was measured. Say so: this check
    # confirms the derivation, it does not discover anything. Its substantive
    # content is only that the k=0 inversion and log(1+x) ~ x are exact enough,
    # and both were expected. It would be dishonest to present the 1.0 ratios
    # as evidence FOR the window; the window's content is checks 4 and 5.
    tail_decades = four_pi2 / t / mp.log(10)
    check(
        "k0_inversion_reproduces_the_full_product_as_derived",
        worst < 1,
        f"the derived z*(d) of (*) lands the measured |D_b(z*)-1| within "
        f"{mp.nstr(worst, 6)} decades of its 10^-d target at d=16,30,50. This "
        f"CONFIRMS the derivation rather than testing it: successive k differ by "
        f"exp(-4pi^2/t) = 10^-{mp.nstr(tail_decades, 6)}, so the k>=1 tail was "
        f"known to be irrelevant before measuring, and the ratios are 1.0 for "
        f"that reason. What it rules out is an algebra slip in (*). The "
        f"window formula is derived from the b-map, not fitted to these three "
        f"points; the residual is the k>=1 tail plus the "
        f"linearisation of log(1+x).",
    )

    # --- check 4: INSIDE the window the dual half is 1 to working precision -
    z_probe = z_star(50) / 2
    D_in = dual_half_product(z_probe, b)
    dep_in = mp.fabs(D_in - 1)
    check(
        "inside_the_window_Phi_b_IS_the_compact_half_product",
        dep_in < mp.mpf(10) ** (-50),
        f"at z = z*(50)/2 = {mp.nstr(z_probe, 12)} the dual half departs from 1 "
        f"by {mp.nstr(dep_in, 8)}. So at the substrate, inside the window, Phi_b "
        f"and the corpus's compact half-product are the SAME function -- an "
        f"alpha-derivation evaluating Phi_b there is using the compact object "
        f"and the modular double is invisible to it.",
    )

    # --- check 5: OUTSIDE the window it is NOT inert (the trap) ------------
    z_out = z_star(0) * 2
    D_out = dual_half_product(z_out, b)
    dep_out = mp.fabs(D_out - 1)
    check(
        "outside_the_window_the_dual_is_NOT_negligible",
        dep_out > mp.mpf(1),
        f"at z = 2*z*(0) = {mp.nstr(z_out, 12)} the dual half departs from 1 by "
        f"{mp.nstr(dep_out, 10)} -- order 1 or larger. 'q~ = 4.8e-165, therefore "
        f"drop the dual half' is FALSE as a global statement; the suppression is "
        f"a modulus that the e^{{2 pi z / b}} growth overcomes, since |1/b| = "
        f"{mp.nstr(mp.fabs(1 / b), 10)} at this substrate.",
    )

    all_passed = all(a["passed"] for a in assertions)
    print(f"\n  {sum(a['passed'] for a in assertions)}/{len(assertions)} checks passed")

    wb = WitnessBuilder("qbeta-phib-dual-validity-window", __file__)
    for a in assertions:
        wb.add_assertion(
            a["name"],
            computed="PASS" if a["passed"] else "FAIL",
            expected="PASS",
            tolerance="exact",
            source=a["detail"],
        )
    wb.save(
        {
            "description": (
                "The z-window in which the modular-dual half of Faddeev Phi_b is "
                "numerically inert at the real substrate. Derived from the corpus "
                "b-map (b = sqrt(t/2pi) e^{+i pi/4}, t = ln q0): the k-th dual "
                "factor departs from 1 by exp(-(4pi^2/t)(k+1/2) + 2 pi z Re(1/b)), "
                "giving z*(d) = [(4pi^2/t)/2 - d ln10] / (2 pi Re(1/b)). Measured "
                "against direct evaluation at d=16,30,50. For qou-pdix attack B: "
                "inside the window Phi_b IS the compact half-product, so an alpha "
                "derivation evaluating Phi_b at the substrate there cannot see the "
                "modular double at all. Corrects the reading that q~ ~ 4.8e-165 "
                "licenses dropping the dual half globally -- it does not, because "
                "|1/b| ~ 7.76 makes e^{2 pi z / b} grow. Scope (a), b_+ branch."
            ),
            "bean": "qou-pdix",
            "q0Anchor": "proton",
            "derived_window_formula": (
                "z*(d) = [(4 pi^2 / ln q0)/2 - d*ln(10)] / (2 pi Re(1/b))"
            ),
            "constants": {
                "q0": mp.nstr(q0, 40),
                "t_ln_q0": mp.nstr(t, 40),
                "abs_log_qtilde_4pi2_over_t": mp.nstr(log_qtilde, 40),
                "re_b_inverse": mp.nstr(re_binv, 40),
                "abs_b_inverse": mp.nstr(mp.fabs(1 / b), 40),
                "growth_slope_2pi_re_binv": mp.nstr(slope, 40),
            },
            "window_table": rows,
            "scope": (
                "(a) scope-limited: the b_+ substrate branch under the corpus's own "
                "b-map and product convention. REFINES rather than refutes "
                "qbeta_fmap_modular_dual_missing_probe, which already concludes "
                "'dual negligible at the substrate' from |q~| alone and states no "
                "z-restriction; what is added is that the restriction exists, is "
                "needed, and is closed-form. Does NOT weaken Phi_b routes at "
                "|q| = 1 -- that same probe measures |q~| = 1 there, the dual IS "
                "order-one, and that is where the Q_beta decay saddle sits. "
                "Asserts nothing about alpha."
            ),
        }
    )
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
