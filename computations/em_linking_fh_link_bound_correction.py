#!/usr/bin/env python3
"""CORRECTION: the Freedman-He link bound is per-COMPONENT, and has no volume.

Bean qou-b5yi / qou-a9li. A close read of the primary sources (Route 2)
overturns two things this branch had been building on. Both corrections
cut AGAINST work already committed here, and both are recorded rather
than quietly patched.

CORRECTION 1 -- THE INDEX IS WRONG. The Freedman-He asymptotic crossing
number appearing in the link energy bound is `ac(L_k, L)`: ONE component
against the WHOLE link. It is not a pairwise quantity. Komendarczyk
(arXiv:0808.1533, eq. 43, p. 26) states it as

    E_{3/2}(X) >= (pi/16)^(1/4) * ( sum_{k=1..n} ac(L_k, L)|Flux(X_k)| )
                  * min_{k} |Flux(X_k)|

-- the sum runs over the n COMPONENTS, not over the n(n-1)/2 pairs, and
no pair-indexed `ac(L_i, L_j)` appears anywhere in either source.

So the question `em_linking_borromean_acn_probe.py` was built to answer
-- "is the pair minimisation constrained by the third component?" -- is
MALFORMED. That probe computes a per-pair Gauss double integral
(ACN_pair = 1.6426, and a "total link" reading of 3x that = 4.928). Per
eq. (43) both are the wrong object with the wrong sum. The probe's own
note had half-caught the problem ("a pair of Borromean components,
considered on its own, is the UNLINK"); the resolution is not a
corrected pair bound but abandoning the pair indexing.

This probe computes the RIGHT object instead. The per-realisation
Gauss integral for component k against the whole link is just the sum
of its pair integrals, ACN(L_k, L) = sum_{j != k} ACN_pair(k, j), which
under the S_3 symmetry of the Borromean complement is 2 * ACN_pair. The
minimised (topological) value is bounded below by Komendarczyk's genus
estimate, and the realisation value bounds it above:

    2*genus_cx(L_k) - 1  <=  ac(L_k, L)  <=  ACN(L_k, L)[realisation]

CORRECTION 2 -- THERE IS NO VOLUME FACTOR, AND THE "CONVERGENCE" WAS A
MISATTRIBUTION. The `Vol^(-1/3)` that this branch has been treating as
"the Freedman-He template" is NOT in the link bound. It comes from
Khesin Thm 3.6, which is the bound for a SINGLE knotted torus:

    int_T |xi|^2 >= (16/(pi Vol(T)))^(1/3) |Flux|^2 (2 genus(K) - 1)

Equation (43), the bound that actually applies to a multi-component
Borromean configuration, carries `(pi/16)^(1/4)` -- a pure constant --
and no volume at all. The audit doc round-4 claim that an empirical
`kappa ~ A^(-1/3)` scaling had "converged" with an independent
structural reason from Freedman-He is therefore WRONG: the two routes
were never independent, because the second one was misattributed.

Consequence, stated in the direction that hurts: hypotheses H_FH_A and
H_FH_Z revert to BARE POWER LAWS with no literature backing. Under the
anti-fit discipline that is exactly the bar they no longer clear. This
does not make coth-saturation right; it removes its rival's warrant.

WHAT EQ. (43) ACTUALLY PREDICTS is tested here: with a fixed local
Borromean configuration the topological factor is A-INDEPENDENT, so all
A-dependence of kappa must be carried by the flux. The required flux
scaling is computed and reported -- not as a result, but so the size of
what would have to be independently derived is visible.

RESIDUAL GAP: Freedman-He (Ann. of Math. 134 (1991) 189-229) is not in
the corpus or uploads, so FH's own definition of the minimisation domain
for `ac(L_k, L)` is not directly verified. Both corrections rest on
Komendarczyk's statement of it, which is unambiguous on the
per-component indexing and on the complement constraint.
"""

from __future__ import annotations

import mpmath as mp

import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402
# The pair integrals ARE the sibling probe's, as its docstring says; importing
# them keeps one implementation of the kink-split quadrature rather than a
# float64 copy that silently disagreed in the 7th digit.
from em_linking_borromean_acn_probe import (  # noqa: E402
    QUAD_DPS, acn_mp, phi_mp,
)

N_COMPONENTS = 3

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

# Per-pair Gauss ACN for the golden-ratio Borromean realisation, from
# em-linking-borromean-acn.witness.json (recomputed below as a check).
# 8 significant digits is all these carry, and nothing derived from them is
# reported past that.
KAPPA_A3 = mp.mpf("3.2135068")
KAPPA_A41 = mp.mpf("1.5310907")
KAPPA_DIGITS = 8


def main() -> None:
    set_compute_dps(QUAD_DPS)

    def q(x, d=20):
        return mp.nstr(mp.mpf(x), d)

    # The right object: component-vs-whole-link, not pair-vs-pair.
    # Under S_3 symmetry every pair integral is equal, so
    # ACN(L_k, L) = sum_{j != k} ACN_pair = (N-1) * ACN_pair.
    per_pair = acn_mp(phi_mp(), 1)
    acn_component = (N_COMPONENTS - 1) * per_pair
    sum_over_components = N_COMPONENTS * acn_component

    # Realisation-dependence, carried through to the corrected object.
    sweep = {}
    for label, ratio in (("1.2000", mp.mpf("1.2")), ("1.5000", mp.mpf("1.5")),
                         ("1.6180", phi_mp()), ("2.0000", mp.mpf(2)),
                         ("3.0000", mp.mpf(3))):
        p = acn_mp(ratio, 1)
        sweep[f"a/b={label}"] = {
            "acn_pair": p,
            "acn_component_vs_link": (N_COMPONENTS - 1) * p,
        }
    comp_vals = [v["acn_component_vs_link"] for v in sweep.values()]
    spread_pct = (max(comp_vals) - min(comp_vals)) / acn_component * 100

    # Lower bound via Komendarczyk's genus estimate. Non-vanishing
    # mu-bar(12..A) = +/-1 != 0 is now proved sorry-free in
    # QOU/MassTheory/MilnorMagnusCoefficient.lean (milnorMagnusCoeff_eq,
    # milnorMagnusCoeff_ne_zero); the remaining unformalised step is the
    # topological implication mu-bar != 0 => genus >= 1 in the complement
    # (bean qou-my0j).
    genus_lower = 1
    ac_lower = 2 * genus_lower - 1
    sum_lower = N_COMPONENTS * ac_lower

    # What eq. (43) predicts, with no volume factor: the topological
    # contribution is A-independent, so kappa's decline must come from
    # the flux. E ~ ac * Flux^2  =>  Flux ~ sqrt(kappa).
    kappa_ratio = KAPPA_A3 / KAPPA_A41
    flux_ratio_required = mp.sqrt(kappa_ratio)
    # For contrast, what the (now-unsupported) Vol^(-1/3) reading gave.
    vol_ratio_predicted = mp.cbrt(mp.mpf(41) / 3)

    wb = WitnessBuilder("em-linking-fh-link-bound-correction",
                        engine="mpmath")
    wb.set_description(
        "CORRECTION probe (beans qou-b5yi, qou-a9li). A close read of "
        "Komendarczyk eq. (43) and Khesin Thm 3.6 overturns two things "
        "this branch was building on. (1) The Freedman-He asymptotic "
        "crossing number in the LINK bound is ac(L_k, L) -- one "
        "component against the whole link, summed over n COMPONENTS -- "
        "so the per-pair object computed in "
        "em-linking-borromean-acn.witness.json is the wrong index and "
        "the wrong sum. (2) Eq. (43) carries (pi/16)^(1/4), a pure "
        "constant, and NO volume factor; the Vol^(-1/3) treated here as "
        "'the Freedman-He template' is Khesin's SINGLE-knotted-torus "
        "bound, misapplied to a multi-component configuration. This "
        "probe computes the correctly-indexed object and records both "
        "corrections against work already committed on this branch.")
    wb.add_data("correction_1_wrong_index", {
        "source": ("Komendarczyk, arXiv:0808.1533v1, eq. (43), p. 26: "
                   "E_{3/2}(X) >= (pi/16)^(1/4) "
                   "( sum_{k=1..n} ac(L_k,L)|Flux(X_k)| ) "
                   "min_k |Flux(X_k)|"),
        "indexing": ("sum over n COMPONENTS, not n(n-1)/2 pairs; no "
                     "pair-indexed ac(L_i,L_j) occurs in either source"),
        "invalidates": ("em-linking-borromean-acn.witness.json: its "
                        "ACN_pair (1.6426) and its 'total link' reading "
                        "(3x that = 4.928) are both the wrong object. "
                        "The malformed question was 'is the PAIR "
                        "minimisation constrained by the third "
                        "component?' -- there is no pair minimisation."),
        "also_settles": ("the (a)-vs-(b) question that motivated the "
                         "read: (a) 'unconstrained pair minimisation, so "
                         "the pair is an unlink and the infimum is 0' is "
                         "REFUTED, but not because the minimisation is "
                         "constrained-over-pairs -- because ac is not a "
                         "pair quantity at all. Komendarczyk's genus is "
                         "minimised over surfaces in R^3 minus the OTHER "
                         "components, so Brunnian-ness does hold the "
                         "value up, via a complement constraint on a "
                         "single-component Seifert genus."),
    })
    wb.add_data("correction_2_no_volume_factor", {
        "link_bound_prefactor": "(pi/16)^(1/4) -- a pure constant",
        "where_vol_came_from": ("Khesin Thm 3.6, the SINGLE knotted "
                                "torus bound: int_T |xi|^2 >= "
                                "(16/(pi Vol(T)))^(1/3) |Flux|^2 "
                                "(2 genus(K) - 1). Not the link bound."),
        "retracts": ("docs/audits/2026-08-01-em-linking-reads-round1.md "
                     "round 4 claimed the empirical kappa ~ A^(-1/3) "
                     "scaling had CONVERGED with an independent "
                     "structural reason from Freedman-He, and that this "
                     "raised it from 'unexplained fit' to 'candidate "
                     "with a structural reason'. That is WRONG: the two "
                     "routes were never independent, because the second "
                     "was a misattribution. The claim is retracted."),
        "consequence": ("H_FH_A and H_FH_Z revert to BARE POWER LAWS "
                        "with no literature backing -- precisely the bar "
                        "the anti-fit discipline says they must clear "
                        "and now do not. This does NOT make "
                        "coth-saturation correct; it removes its rival's "
                        "warrant. The residual-drift evidence "
                        "(em-linking-residual-structure) already leaned "
                        "the same way, independently."),
    })
    wb.add_data("corrected_object", {
        "definition": ("ACN(L_k, L) = sum_{j != k} ACN_pair(k,j); under "
                       "the S_3 symmetry of the Borromean complement "
                       "every pair integral is equal, so this is "
                       "(n-1) * ACN_pair with n = 3."),
        "acn_pair_golden_realisation": q(per_pair),
        "acn_component_vs_link": q(acn_component),
        "sum_over_components": q(sum_over_components),
        "realisation_spread_pct": q(spread_pct, 12),
        "bracket": {
            "lower_bound_per_component": ac_lower,
            "lower_bound_summed": sum_lower,
            "upper_bound_per_component": q(acn_component),
            "upper_bound_summed": q(sum_over_components),
            "reading": ("2*genus_cx(L_k) - 1 <= ac(L_k,L) <= "
                        "ACN(L_k,L)[realisation]. The realisation value "
                        "bounds the minimised topological value from "
                        "ABOVE; the genus estimate bounds it from "
                        "below. The bracket is wide and is reported as "
                        "a bracket, not collapsed to a number."),
        },
        "genus_step_is_my_inference": (
            "Komendarczyk bounds ac(L_k, L) below by the smallest genus "
            "among surfaces in R^3 minus the other components, with "
            "boundary L_k. For Borromean, L_k is null-homologous there "
            "(pairwise lk = 0) so a surface exists, while mu-bar_123 = "
            "+/-1 != 0 (now proved sorry-free via faithful nilpotent "
            "Magnus realization in QOU/MassTheory/MilnorMagnusCoefficient.lean: "
            "milnorMagnusCoeff_eq, milnorMagnusCoeff_ne_zero) obstructs a "
            "genus-0 spanning disk, giving genus >= 1 and hence ac >= 1. "
            "With non-vanishing proved in Lean, the remaining unformalised "
            "inference is the single topological implication 'mu-bar != 0 "
            "=> genus >= 1 in the complement' (bean qou-my0j)."),
    })
    wb.add_data("what_eq43_actually_predicts", {
        "structure": ("with a fixed local Borromean configuration the "
                      "topological factor sum_k ac(L_k,L) is "
                      "A-INDEPENDENT, and there is no volume factor, so "
                      "ALL A-dependence of kappa must be carried by the "
                      "flux: E ~ ac * Flux^2."),
        "kappa_decline_A3_to_A41": q(kappa_ratio, KAPPA_DIGITS),
        "required_flux_decline": q(flux_ratio_required, KAPPA_DIGITS),
        "vol_third_root_ratio_for_contrast": q(vol_ratio_predicted,
                                               KAPPA_DIGITS),
        "reading": (
            f"kappa falls by {q(kappa_ratio, 4)} across the series, so "
            f"saturating eq. (43) with a constant topological factor "
            f"would require the per-component flux to fall by "
            f"{q(flux_ratio_required, 4)} over the same range. That is a "
            "specific, independently-derivable quantity -- it is NOT "
            "derived here, and nothing is wired. The point of reporting "
            "it is to make the size of the remaining obligation "
            "visible: the FH link bound does not explain kappa(A) by "
            "itself, it relocates the explanation into the flux."),
    })
    wb.add_data("residual_gap", (
        "Freedman-He, Ann. of Math. 134 (1991) 189-229 is not in the "
        "corpus or in library/ (201 PDFs scanned by title metadata, no "
        "match), so FH's own definition of the minimisation domain for "
        "ac(L_k, L) is not directly verified. Both corrections rest on "
        "Komendarczyk's statement of it, which is unambiguous on the "
        "per-component indexing and on the complement constraint, "
        "cross-checked against Khesin Rmk 3.5 and Thm 3.6. Acquiring FH "
        "1991 would close this."))
    wb.set_audit_only("docs/audits/2026-08-01-em-linking-reads-round1.md")
    wb.add_assertion(
        name="component_acn_exceeds_genus_lower_bound",
        computed=int(acn_component >= ac_lower), expected=1, tolerance=0,
        unit="bool",
        source=("Consistency of the bracket: the realisation value must "
                "exceed the genus-derived lower bound, since the "
                "minimised topological value lies between them."))
    wb.add_assertion(
        name="pair_and_component_objects_differ",
        computed=int(abs(acn_component - per_pair) > 1.0), expected=1,
        tolerance=0, unit="bool",
        source=("The correction has teeth: the correctly-indexed "
                "component-vs-link object differs from the per-pair one "
                "by more than 1 crossing, so the earlier probe's number "
                "cannot be reinterpreted as the right quantity."))
    out = wb.save()

    print("CORRECTED OBJECT (component vs whole link, not pair vs pair)")
    print(f"  ACN_pair (golden)          = {q(per_pair, 20)}")
    print(f"  ACN(L_k, L) = 2 * pair     = {q(acn_component, 12)}")
    print(f"  sum over 3 components      = {q(sum_over_components, 12)}")
    print(f"  realisation spread         = {q(spread_pct, 3)}%")
    print(f"  bracket per component      : {ac_lower} <= ac <= "
          f"{q(acn_component, 6)}")
    print("\nrealisation sweep:")
    for k, v in sweep.items():
        print(f"  {k}: pair {q(v['acn_pair'], 12)}  "
              f"component {q(v['acn_component_vs_link'], 12)}")
    print("\nEQ (43) HAS NO VOLUME FACTOR -- Vol^(-1/3) was Khesin's "
          "single-torus bound.")
    print(f"  kappa declines by {q(kappa_ratio, 4)} over A = 3..41")
    print(f"  => required flux decline {q(flux_ratio_required, 4)} "
          "(not derived here)")
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
