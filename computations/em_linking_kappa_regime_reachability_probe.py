#!/usr/bin/env python3
"""Does the kappa(A) series reach the regime its discrimination test needs?

Bean qou-17mq (successor question to the O2 finding in
em-linking-o2-neutralised-kernel.witness.json).

THE QUESTION
============
Bean qou-i6rg extended the mirror series from A <= 13 to A = 63 and called
it "the measurement that selects the hyperbolic kernel or kills it", on the
stated grounds that

  H_coth   kappa = coth(alpha), alpha ~ A^(1/3)   -> kappa SATURATES at 1
  H_FH_*   power law                              -> kappa -> 0

"diverge at large A and in opposite directions, so extending the mirror
series settles them."

That is true ASYMPTOTICALLY. This probe asks the prior question nobody
asked: does A = 63 get anywhere near the regime where they diverge?

It is a reachability question, not a fit. Everything below is computed
from the contest's OWN fitted constants and the committed series; no new
hypothesis is introduced and nothing is scored.

WHAT IT CHECKS
==============
1. The alpha range the series actually spans, under H_coth's own fitted
   scale.
2. Where saturation begins, as an A. Compared against the heaviest known
   nuclide, because a required A beyond the nuclear chart means the test
   cannot be run at all -- not that it was run and was inconclusive.
3. Whether coth is separable from its own short-range asymptotics
   1/alpha and 1/alpha + alpha/3 over the measured range, at the ~3.5%
   scatter the hypotheses are judged on. If it is not, then whatever
   distinguishes H_coth on this data, it is not hyperbolic saturation.
4. The actual predictive spread between H_coth and H_FH_Z across the
   series, against that same scatter -- i.e. the separation the test
   achieved, as opposed to the separation it was designed for.

A SECOND, INDEPENDENT ROUTE TO THE SAME SUBTRACTION
===================================================
Recorded here because it needs no compactness and no O2. On H^3 the radial
Laplacian is u'' + 2 coth(r) u', so the harmonic solutions off the origin
are -C coth(r) + D: the fundamental solution is fixed only up to an
additive constant D. Requiring it to VANISH AT INFINITY -- the standard
normalisation -- selects

  G(r) = -(coth(r) - 1) / 4pi  ~  -(1/2pi) e^(-2r)

so the decaying Green's function of H^3 is already the SUBTRACTED one.
The saturating form -coth(r)/4pi is the D = 0 choice, which does not decay.
So the subtraction the O2 probe derived from finite-volume neutrality is
also just the ordinary boundary condition on H^3.

Relatedly: for a finite-covolume Gamma the critical exponent is
delta(Gamma) = 2, and lattice points satisfy #{d <= R} ~ c e^(2R), which
exactly cancels the e^(-2R) decay -- so the Green's-function Poincare
series diverges (logarithmically in the counting measure). That divergence
IS O2 in analytic form: a finite-volume quotient admits no Green's function
without the -1/vol(M) source correction. Stated here as the standard fact
it is; not re-derived, and nothing downstream rests on it.

EXPLORATORY / audit-only. mpmath, no float64 anywhere.
"""

from __future__ import annotations

import json
import pathlib

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

_UPSTREAM_RECORDS: list = []

from mpmath import mp, mpf, sqrt, coth, acoth  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
SERIES = HERE / "em-linking-mirror-series.witness.json"

set_compute_dps()

UNBOUND_A = {5, 9}

# Heaviest nuclide with a measured mass. Oganesson-294 is the heaviest
# with a confirmed observation; the exact edge does not matter here --
# the comparison below is not close.
HEAVIEST_KNOWN_A = 294


def stats(vals):
    n = len(vals)
    m = sum(vals) / n
    return m, sqrt(sum((v - m) ** 2 for v in vals) / n) / m


def main() -> None:
    set_compute_dps()
    third = mpf(1) / 3

    w = record_upstream(SERIES, _UPSTREAM_RECORDS)
    rows = [{"A": int(r["A"]), "Z": int(r["Z"]),
             "kappa": mpf(str(r["kappa"]))} for r in w["data"]["series"]]
    bound = [r for r in rows if r["A"] not in UNBOUND_A]

    sc = w["data"]["hypothesis_scores_bound_only"]
    c_coth = mpf(str(sc["H_coth: arccoth(kappa) / A^(1/3) const"]["constant"]))
    scatter = mpf(str(
        sc["H_coth: arccoth(kappa) / A^(1/3) const"]["rel_scatter"]))
    c_fhz = mpf(str(sc["H_FH_Z: kappa * Z^(1/3) const"]["constant"]))

    # --- 1. the alpha range actually spanned -----------------------------
    alphas = [(r, c_coth * mpf(r["A"]) ** third) for r in bound]
    a_lo = min(a for _, a in alphas)
    a_hi = max(a for _, a in alphas)

    # --- 2. where saturation begins, as an A -----------------------------
    sat = {}
    for tol, label in ((mpf("0.10"), "10pct"), (mpf("0.05"), "5pct"),
                       (mpf("0.01"), "1pct")):
        a_sat = acoth(1 + tol)
        sat[label] = {
            "alpha_required": mp.nstr(a_sat, 8),
            "A_required": mp.nstr((a_sat / c_coth) ** 3, 8),
            "reachable_in_the_nuclear_chart":
                bool((a_sat / c_coth) ** 3 <= HEAVIEST_KNOWN_A),
        }

    # --- 3. is coth separable from its short-range asymptotics here? -----
    dev_inv, dev_inv3 = [], []
    for _, a in alphas:
        c_exact = coth(a)
        dev_inv.append(abs(c_exact - 1 / a) / c_exact)
        dev_inv3.append(abs(c_exact - (1 / a + a / 3)) / c_exact)
    max_dev_inv = max(dev_inv)
    max_dev_inv3 = max(dev_inv3)

    # --- 4. the separation the test ACHIEVED -----------------------------
    # Both hypotheses at their own fitted constants, compared pair by pair.
    spread = []
    for r in bound:
        p_coth = coth(c_coth * mpf(r["A"]) ** third)
        p_fhz = c_fhz / mpf(r["Z"]) ** third
        spread.append(abs(p_coth - p_fhz) / ((p_coth + p_fhz) / 2))
    max_spread = max(spread)
    mean_spread = sum(spread) / len(spread)
    sep_sigma = max_spread / scatter

    # ------------------------------------------------------------------
    wb = WitnessBuilder("em-linking-kappa-regime-reachability",
                        engine="mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)
    wb.set_description(
        "Reachability check on the kappa(A) discrimination test (bean "
        "qou-i6rg), asking the prior question: does the measured series "
        "reach the regime in which its hypotheses diverge? Computed "
        "entirely from the contest's own fitted constants and the "
        "committed series -- no new hypothesis, nothing scored, nothing "
        "fitted. Also records a second, O2-independent route to the same "
        "kernel subtraction: on H^3 the Green's function normalised to "
        "vanish at infinity is -(coth(r) - 1)/4pi, so the saturating form "
        "is the non-decaying choice of the additive constant.")
    wb.add_data("alpha_range_spanned", {
        "alpha_min": mp.nstr(a_lo, 8),
        "alpha_max": mp.nstr(a_hi, 8),
        "A_min": min(r["A"] for r in bound),
        "A_max": max(r["A"] for r in bound),
        "scale_used": mp.nstr(c_coth, 8),
        "note": ("H_coth's own bound-only fitted scale, taken from the "
                 "committed contest rather than refitted here."),
    })
    wb.add_data("saturation_onset", {
        "criterion": "coth(alpha) within the given tolerance of its limit 1",
        "thresholds": sat,
        "heaviest_known_nuclide_A": HEAVIEST_KNOWN_A,
        "reading": ("Saturation is the feature the discrimination test was "
                    "built to detect. If the A it requires lies beyond the "
                    "nuclear chart, the test cannot be run -- which is a "
                    "different and stronger statement than the test having "
                    "been run and come out close."),
    })
    wb.add_data("separability_from_short_range_asymptotics", {
        "max_rel_dev_coth_vs_inverse_alpha": mp.nstr(max_dev_inv, 8),
        "max_rel_dev_coth_vs_inverse_alpha_plus_alpha_over_3":
            mp.nstr(max_dev_inv3, 8),
        "scatter_hypotheses_are_judged_on": mp.nstr(scatter, 8),
        "coth_separable_from_two_term_expansion_at_this_scatter":
            bool(max_dev_inv3 > scatter),
        "reading": ("Over the measured range coth(alpha) = 1/alpha + "
                    "alpha/3 - alpha^3/45 + ... If coth cannot be told "
                    "apart from that short-range expansion at the scatter "
                    "the contest uses, then whatever advantage H_coth has "
                    "on this data comes from the curvature term alpha^2/3, "
                    "NOT from saturation."),
    })
    wb.add_data("separation_achieved_vs_scatter", {
        "max_rel_spread_H_coth_vs_H_FH_Z": mp.nstr(max_spread, 8),
        "mean_rel_spread": mp.nstr(mean_spread, 8),
        "scatter": mp.nstr(scatter, 8),
        "max_spread_in_units_of_scatter": mp.nstr(sep_sigma, 8),
        "reading": ("The predictive gap the two hypotheses actually open "
                    "across the measured series, in units of the scatter "
                    "they are judged against. A gap of order 1 scatter is "
                    "not a discrimination."),
    })
    wb.add_data("independent_route_to_the_subtraction", {
        "claim": ("The decaying Green's function of H^3 is "
                  "-(coth(r) - 1)/4pi, not -coth(r)/4pi."),
        "why": ("The radial Laplacian on H^3 is u'' + 2 coth(r) u', so "
                "harmonic solutions off the origin are -C coth(r) + D. C "
                "is fixed by the delta normalisation; D is fixed by the "
                "boundary condition. Requiring decay at infinity gives "
                "D = C, i.e. coth(r) - 1 ~ 2 e^(-2r). The saturating form "
                "is D = 0, which does not decay."),
        "significance": ("This reaches the same subtraction as the O2 "
                         "finding by a route that needs neither "
                         "compactness nor finite volume, so the two are "
                         "independent."),
        "poincare_series": ("For finite covolume Gamma the critical "
                            "exponent is delta = 2 and #{d <= R} ~ c "
                            "e^(2R), which exactly cancels the e^(-2R) "
                            "decay, so the Green's-function Poincare "
                            "series diverges. That divergence is O2 in "
                            "analytic form: no Green's function exists on "
                            "a finite-volume quotient without the "
                            "-1/vol(M) source correction. Standard; "
                            "stated, not re-derived, and nothing here "
                            "rests on it."),
    })
    wb.add_data("scope", {
        "class": "(a) scope-limited negative on a TEST, not on a hypothesis",
        "what_is_claimed": ("The A = 63 series does not reach the regime "
                            "in which its hypotheses diverge, so it cannot "
                            "have selected among them on the stated "
                            "grounds."),
        "what_is_NOT_claimed": ("That H_coth is false, that a power law is "
                                "true, or that the metric Coulomb route "
                                "fails. This is about what the measurement "
                                "can resolve, not about which kernel is "
                                "right. Nothing is wired."),
    })

    unreachable = not sat["10pct"]["reachable_in_the_nuclear_chart"]
    verdict = (
        f"The series spans alpha in [{mp.nstr(a_lo,5)}, {mp.nstr(a_hi,5)}]. "
        f"Saturation to within 10% of the limit needs alpha = "
        f"{sat['10pct']['alpha_required']}, i.e. A = "
        f"{sat['10pct']['A_required']} -- "
        + ("BEYOND the heaviest known nuclide (A = "
           f"{HEAVIEST_KNOWN_A}), so the discriminating regime is not "
           "reachable in any nucleus, let alone in this series."
           if unreachable else
           "within the nuclear chart, so the test is in principle "
           "runnable and this probe's premise fails.")
        + f" Over the measured range coth is within "
          f"{mp.nstr(max_dev_inv3 * 100, 4)}% of its two-term short-range "
          f"expansion 1/alpha + alpha/3, against the "
          f"{mp.nstr(scatter * 100, 4)}% scatter the hypotheses are judged "
          f"on. And the two hypotheses' predictions differ by at most "
          f"{mp.nstr(max_spread * 100, 4)}% across the whole series = "
          f"{mp.nstr(sep_sigma, 4)}x that scatter. So bean qou-i6rg's "
          f"'measurement that selects the hyperbolic kernel or kills it' "
          f"could not have done either: what H_coth's advantage tracks on "
          f"this data is the short-range curvature term, not the "
          f"saturation the test was named for.")
    wb.add_data("verdict", verdict)
    wb.set_audit_only(
        "docs/audits/2026-08-25-em-linking-o2-neutrality-applied-to-kappa-contest.md")

    wb.add_assertion(
        name="saturation_regime_unreachable_in_the_nuclear_chart",
        computed=1 if unreachable else 0, expected=1, tolerance=0,
        unit="boolean",
        source=(f"coth within 10% of its limit needs A = "
                f"{sat['10pct']['A_required']}; heaviest known nuclide is "
                f"A = {HEAVIEST_KNOWN_A}."))
    wb.add_assertion(
        name="hypothesis_spread_is_of_order_the_scatter",
        computed=1 if sep_sigma <= 3 else 0, expected=1, tolerance=0,
        unit="boolean",
        source=(f"The separation the test achieved, in units of the noise "
                f"it is judged against: max spread {mp.nstr(max_spread*100,4)}% "
                f"= {mp.nstr(sep_sigma, 6)}x the {mp.nstr(scatter*100,4)}% "
                f"scatter. A gap of order the noise is not a "
                f"discrimination."))
    wb.add_assertion(
        name="series_alpha_max_below_saturation_onset",
        computed=1 if a_hi < acoth(mpf("1.10")) else 0, expected=1,
        tolerance=0, unit="boolean",
        source=(f"alpha_max = {mp.nstr(a_hi, 8)} against the 10% "
                f"saturation onset {sat['10pct']['alpha_required']}."))
    out = wb.save()

    print(f"alpha spanned: [{mp.nstr(a_lo,6)}, {mp.nstr(a_hi,6)}]  "
          f"over A = {min(r['A'] for r in bound)}..{max(r['A'] for r in bound)}")
    print("\nsaturation onset (coth within tol of 1):")
    for k, v in sat.items():
        print(f"  {k:>6}: alpha {v['alpha_required']:>10}  A "
              f"{v['A_required']:>10}  reachable(A<={HEAVIEST_KNOWN_A}): "
              f"{v['reachable_in_the_nuclear_chart']}")
    print(f"\ncoth vs 1/alpha            : max dev "
          f"{mp.nstr(max_dev_inv*100,4)}%")
    print(f"coth vs 1/alpha + alpha/3  : max dev "
          f"{mp.nstr(max_dev_inv3*100,4)}%")
    print(f"scatter judged on          : {mp.nstr(scatter*100,4)}%")
    print(f"\nH_coth vs H_FH_Z spread    : max "
          f"{mp.nstr(max_spread*100,4)}%  mean "
          f"{mp.nstr(mean_spread*100,4)}%  = {mp.nstr(sep_sigma,4)}x scatter")
    print(f"\nverdict:\n{verdict}")
    print(f"\nwitness -> {out}")


if __name__ == "__main__":
    main()
