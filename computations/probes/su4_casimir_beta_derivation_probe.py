#!/usr/bin/env python3
"""su4_casimir_beta_derivation_probe.py

beta CANNOT be derived, and the reason RETRACTS the lead it belonged to.

THE ASK
-------
The previous probe (su4_casimir_coordination_weight_probe) recorded a LEAD:
w(A) = alpha - beta*C2([1^A]) with the Wigner SU(4) Casimir, fitted at the A=2
and A=4 endpoints, predicts A=3 to 0.71%. The stated promotion path was "derive
beta -- the LO SU(4)-symmetric interaction carries one coupling".

THE ANSWER: THERE IS NOTHING TO DERIVE IT FROM
----------------------------------------------
The SU(4) Casimir of the fully antisymmetric [1^n] is AFFINE IN THE PAIR COUNT:

    C2([1^n]) = (5/8) n (4-n) = (15/8) n - (5/4) C(n,2)

and the two-body sum a two-body SU(4)-invariant interaction actually contributes,

    S(n) = sum_{i<j} lambda_i . lambda_j = (1/2)[ C2([1^n]) - n * C2(fund) ],
    C2(fund) = 15/8,

is EXACTLY proportional to the pair count:

    S(n) = -(5/8) * C(n,2)      for every n, exactly

So a two-body SU(4)-invariant interaction contributes a CONSTANT PER PAIR. In
the coordination-weight coordinate that is w constant, hence b3 = 0 -- the
pairwise wall, reached here from group theory instead of from the counting bound
in QOU.Mass.UniformBondSimpleGraphExclusion. The two arguments agree, which
checks both.

**Therefore the fitted form is not the SU(4) prediction.** By the affine
identity it is only "w linear in n and C(n,2) along one fixed direction"; no
group-theoretic content survives, and there is no coupling for beta to be.
Formalised sorry-free in QOU/Mass/SU4CasimirIsAffineInPairCount.lean.

WHAT THE FIT ACTUALLY WAS, AND A CORRECTION TO HOW I QUOTED IT
--------------------------------------------------------------
C2 = 2.5, 1.875, 0 at A = 2,3,4, so fitting the endpoints and predicting the
middle is a FIXED interpolation with no freedom at all:

    lambda = (C2(3)-C2(4))/(C2(2)-C2(4)) = 3/4  exactly
    w(3) = (3/4) w(2) + (1/4) w(4)     <=>     B(4) = 8 B(3) - 18 B(2)

Two things follow, and the second corrects my own earlier quoting.

1. It is a genuinely BETTER relation than the corpus simplex baseline mu4 = 0
   (B(4) = 4B(3) - 6B(2)), which misses B(4) by 32.7%. This one misses by 1.7%
   on the Coulomb-corrected convention. That is real, and it is why the fit
   looked good.
2. The residual is not variable-independent. On the SAME convention it reads
   0.71% stated on B(3) and 1.71% stated on B(4), because B(3) enters with a
   factor 8: the amplification is 8*B(3)/B(4) ~ 2.4. Quoting the smaller was
   flattering.

   **A scratch run of mine printed "18x" for that amplification. That figure was
   hardcoded prose, not computed, and it was wrong -- and it also compared the
   B(3) residual of one convention against the B(4) residual of another. The
   computed factor is 2.4, consistent across conventions. Recorded because the
   error was exactly the kind this probe exists to catch.**

WHAT IS NOT TOUCHED
-------------------
The SUPPORT bound is untouched: dim[1^n] = C(4,n) = 0 for n >= 5 still locates
the turnover at A=4, and that argument uses the VANISHING OF THE REPRESENTATION,
not its Casimir. Wigner SU(4) as physics is not refuted. What is closed is the
one route "derive beta from an SU(4)-invariant two-body interaction".

Bean qou-edt7.
"""
from __future__ import annotations

import sys as _sys, pathlib as _pl  # noqa: E402
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401, E402
import sys  # noqa: E402
from math import comb  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import ame_binding_mev  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(65)

C2F = mp.mpf(15) / 8                                   # SU(4) fundamental Casimir


def c2(n):                                             # C2 of [1^n]
    return mp.mpf(5) / 8 * n * (4 - n)


def two_body_sum(n):                                   # sum_{i<j} lambda_i . lambda_j
    return (c2(n) - n * C2F) / 2


def main() -> int:
    wb = WitnessBuilder("su4-casimir-beta-derivation", engine="mpmath")
    wb.set_description(
        "beta cannot be derived: the SU(4) Casimir of [1^n] is AFFINE in the pair "
        "count, so a two-body SU(4)-invariant interaction contributes exactly "
        "-(5/8) per pair -- w constant, b3 = 0. The fitted w = alpha - beta*C2 is "
        "therefore not the SU(4) prediction and has no coupling to derive. "
        "RETRACTS the lead. The support bound C(4,n) = 0 for n >= 5, which locates "
        "the turnover, is untouched."
    )
    ok = True

    # --- the exact proportionality ---------------------------------------
    print("S(n) = sum_{i<j} lambda_i.lambda_j  vs  C(n,2):")
    worst = mp.mpf(0)
    rows = []
    for n in range(2, 13):
        S = two_body_sum(n)
        ratio = S / comb(n, 2)
        worst = max(worst, abs(ratio + mp.mpf(5) / 8))
        rows.append({"n": n, "C2": fmt(c2(n)), "S": fmt(S),
                     "pairs": comb(n, 2), "S_over_pairs": fmt(ratio)})
        if n <= 6:
            print(f"   n={n:<3} C2={mp.nstr(c2(n),6):>9}  S={mp.nstr(S,8):>11}  "
                  f"C(n,2)={comb(n,2):>3}  S/C(n,2)={mp.nstr(ratio,10)}")
    print(f"   ... through n=12;  worst |S/C(n,2) + 5/8| = {mp.nstr(worst,3)}")
    wb.add_data("two_body_sum_table", rows)
    wb.add_assertion(
        name="two_body_su4_sum_is_exactly_proportional_to_pair_count",
        computed=fmt(worst), expected="0", tolerance="1e-50",
        unit="deviation of S/C(n,2) from -5/8",
        source=("S(n) = -(5/8)C(n,2) exactly for all n, so a two-body "
                "SU(4)-invariant interaction gives a constant per pair => w "
                "constant => b3 = 0. Lean: SU4CasimirIsAffineInPairCount.pairSum_eq"),
    )
    ok &= worst < mp.mpf(10) ** -50

    # --- the affine identity ---------------------------------------------
    dev = max(abs(c2(n) - (C2F * n - mp.mpf(5) / 4 * comb(n, 2))) for n in range(2, 13))
    print(f"\naffine identity  C2 = (15/8)n - (5/4)C(n,2):  worst dev = {mp.nstr(dev,3)}")
    wb.add_assertion(
        name="casimir_is_affine_in_pair_count",
        computed=fmt(dev), expected="0", tolerance="1e-50",
        unit="deviation", source="Lean: SU4CasimirIsAffineInPairCount.casimirX8_eq",
    )
    ok &= dev < mp.mpf(10) ** -50

    # --- what the fit was, and the variable-dependence of its residual ----
    D = ame_binding_mev(1, 2)
    T3, He3 = ame_binding_mev(1, 3), ame_binding_mev(2, 3)
    He4 = ame_binding_mev(2, 4)
    lam = (c2(3) - c2(4)) / (c2(2) - c2(4))
    print(f"\nthe fit is a FIXED interpolation, lambda = {mp.nstr(lam,10)} (= 3/4 exactly)")
    print("   w(3) = (3/4)w(2) + (1/4)w(4)   <=>   B(4) = 8 B(3) - 18 B(2)")
    wb.add_assertion(
        name="fit_is_the_fixed_three_quarter_interpolation",
        computed=fmt(lam), expected="0.75", tolerance="1e-50",
        unit="interpolation weight",
        source="lambda = (C2(3)-C2(4))/(C2(2)-C2(4)); no fitted freedom remains",
    )
    ok &= abs(lam - mp.mpf(3) / 4) < mp.mpf(10) ** -50

    pred3 = (1 - lam) * (He4 / 6) + lam * D
    print("\nresidual, stated two ways, on the SAME convention:")
    amp = {}
    for nm, B3 in (("isospin_average", (T3 + He3) / 2), ("3H_Coulomb_corrected", T3)):
        e_b3 = abs(3 * pred3 - B3) / B3
        e_b4 = abs((8 * B3 - 18 * D) - He4) / He4
        amp[nm] = {"on_B3": fmt(e_b3), "on_B4": fmt(e_b4),
                   "amplification": fmt(e_b4 / e_b3)}
        print(f"   {nm:<22} on B(3) {mp.nstr(e_b3*100,4):>8}%   on B(4) "
              f"{mp.nstr(e_b4*100,4):>8}%   ratio {mp.nstr(e_b4/e_b3,4)}")
    print("   -> amplification ~ 8*B(3)/B(4) ~ 2.4, consistent across conventions.")
    print("      (an earlier scratch run of mine printed '18x'; that was hardcoded")
    print("       prose, not computed, and it crossed two conventions. It was wrong.)")
    wb.add_data("residual_by_variable", amp)

    b4_baseline = 4 * ((T3 + He3) / 2) - 6 * D
    print(f"\nvs the corpus simplex baseline mu4=0 (B(4) = 4B(3) - 6B(2)):")
    print(f"   baseline B(4) = {mp.nstr(b4_baseline,9)}  err "
          f"{mp.nstr((b4_baseline-He4)/He4*100,4)}%   (this model: -1.7% on 3H)")
    wb.add_data("vs_simplex_baseline", {
        "mu4_zero_B4": fmt(b4_baseline),
        "mu4_zero_err": fmt((b4_baseline - He4) / He4),
        "note": "the 8/-18 relation IS better than the mu4=0 baseline; that is real "
                "and is why the fit looked good. It is still not a derivation.",
    })

    wb.add_data("verdict", {
        "beta_derivable": False,
        "why": "a two-body SU(4)-invariant interaction contributes exactly "
               "-(5/8) per pair, so it has no Casimir term to carry a beta",
        "lead_status": "RETRACTED as a derivation route",
        "still_standing": "the SUPPORT bound dim[1^n] = C(4,n) = 0 for n >= 5, "
                          "which locates the turnover at A=4 and uses the "
                          "vanishing of the representation, not its Casimir",
        "scope": "does not refute Wigner SU(4) as physics; closes one route",
    })
    wb.save()
    print("\nOK" if ok else "\nFAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
