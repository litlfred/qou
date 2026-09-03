#!/usr/bin/env python3
"""Where does alpha ~ A^(1/3) come from, and does the geometry agree?

Bean qou-17mq, third finding. Upstream of both earlier ones: they scored
KERNELS against kappa(A); this asks about the SEPARATION LAW fed into
every one of them.

THE OBSERVATION
===============
em_linking_coth_separation_probe.py is explicit about its own premise, and
unusually honest about its limits (four caveats, null transforms scored,
"this cannot confirm anything; it can only fail"). But caveat (3) reads:

  "(3) A^(1/3) was fixed in advance as the standard nuclear radius law,
   not selected post hoc."

Fixing a law in advance protects against POST-HOC SELECTION, which is real
and worth having. It does not make the law DERIVED. And this one is not
merely underived -- it is imported from the wrong geometry. The same file
says of the kernel:

  "H_coth has NO free parameter in the kernel -- coth is forced by the
   Green's function."

So the kernel is hyperbolic by construction while the separation law fed
into it is the Euclidean liquid-drop nuclear radius. That is a layer
straddle in one quantity.

WHAT THE GEOMETRY WOULD REQUIRE
===============================
In H^3 a ball of radius R has volume pi(sinh(2R) - 2R) ~ (pi/2) e^(2R), so
R ~ (1/2) ln(2V/pi): hyperbolic size grows LOGARITHMICALLY in volume. If
the carrier's volume is extensive (V ~ A), the hyperbolic separation scale
goes like ln A -- not A^(1/3). This probe scores that self-consistent law
against the imported one, on the same series and with the same statistic.

Note the scale constant absorbs any multiplicative factor, so ln A and
(1/2)ln A are the SAME hypothesis here and must score identically; that
identity is asserted below as a self-check on the scoring.

WHY THE CORPUS CANNOT SETTLE IT INTERNALLY
==========================================
binding-link-volumes.witness.json carries hyperbolic link volumes for
A = 2 and A = 3 only (Hopf, 8_11, L6a4), and its own description records
that "A-dependence is not in a single binding-link volume". There is no
per-isotope hyperbolic geometry in the corpus beyond A = 3, so no competing
alpha(A) law can currently be DERIVED from framework data -- whatever law
is used here is imported.

THE DIAGNOSTIC, LABELLED AS ONE
===============================
A scan over alpha ~ A^p asks what the data prefers. That is a fit with one
more DOF than any fixed-p hypothesis and is reported as a diagnostic, never
as support.

EXPLORATORY / audit-only. mpmath, no float64 anywhere.
"""

from __future__ import annotations

import json
import pathlib

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

_UPSTREAM_RECORDS: list = []

from mpmath import mp, mpf, sqrt, acoth, log  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
SERIES = HERE / "em-linking-mirror-series.witness.json"

set_compute_dps()

UNBOUND_A = {5, 9}


def stats(vals):
    n = len(vals)
    m = sum(vals) / n
    return m, sqrt(sum((v - m) ** 2 for v in vals) / n) / m


def main() -> None:
    set_compute_dps()
    third = mpf(1) / 3

    w = record_upstream(SERIES, _UPSTREAM_RECORDS)
    rows = [(int(r["A"]), int(r["Z"]), mpf(str(r["kappa"])))
            for r in w["data"]["series"] if int(r["A"]) not in UNBOUND_A]

    def score(f):
        """Implied scale per pair for kappa = coth(c * f(A))."""
        return stats([acoth(k) / f(mpf(A)) for A, _, k in rows])

    laws = {
        "A^(1/3)  -- EUCLIDEAN nuclear-radius law, imported":
            lambda A: A ** third,
        "ln A     -- HYPERBOLIC self-consistent (H^3, V ~ A)":
            lambda A: log(A),
        "(1/2)ln A -- same hypothesis, scale absorbed":
            lambda A: log(A) / 2,
        "A^(1/4)": lambda A: A ** mpf("0.25"),
        "A^(1/2)": lambda A: sqrt(A),
    }
    scored = {}
    for name, f in laws.items():
        m, s = score(f)
        scored[name] = {"scale": mp.nstr(m, 8), "rel_scatter": mp.nstr(s, 8)}

    euclid = mpf(scored["A^(1/3)  -- EUCLIDEAN nuclear-radius law, imported"]
                 ["rel_scatter"])
    hyper = mpf(scored["ln A     -- HYPERBOLIC self-consistent (H^3, V ~ A)"]
                ["rel_scatter"])
    half = mpf(scored["(1/2)ln A -- same hypothesis, scale absorbed"]
               ["rel_scatter"])
    cost_of_consistency = hyper / euclid

    # --- diagnostic: what power does the data prefer? -------------------
    best_p, best_s = None, None
    p = mpf("0.05")
    while p <= mpf("1.00"):
        _, s = score(lambda A, p=p: A ** p)
        if best_s is None or s < best_s:
            best_p, best_s = p, s
        p += mpf("0.01")

    # Pure-Coulomb comparator, from the committed contest: H_FH_A is
    # kappa * A^(1/3) = const, i.e. kappa = 1/(c A^(1/3)) -- the 1/r law
    # with a Euclidean nuclear radius, no curvature term.
    pure_coulomb = mpf(str(
        w["data"]["hypothesis_scores_bound_only"]
        ["H_FH_A: kappa * A^(1/3) const"]["rel_scatter"]))

    wb = WitnessBuilder("em-linking-alpha-scaling-provenance", engine="mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)
    wb.set_description(
        "Provenance and self-consistency check on the separation law "
        "alpha(A) that every kernel hypothesis on this front is fed. The "
        "law alpha ~ A^(1/3) is imported by em_linking_coth_separation_"
        "probe.py as 'the standard nuclear radius law' -- a Euclidean "
        "liquid-drop result -- while the kernel it feeds is hyperbolic "
        "('coth is forced by the Green's function'). This scores the "
        "geometrically self-consistent alternative (H^3 volume growth "
        "gives R ~ (1/2)ln V, so alpha ~ ln A for extensive V) against "
        "the imported one on the same series with the same statistic.")
    wb.add_data("the_import", {
        "law": "alpha proportional to A^(1/3)",
        "quoted_justification": ("'(3) A^(1/3) was fixed in advance as the "
                                 "standard nuclear radius law, not selected "
                                 "post hoc.' -- em_linking_coth_separation_"
                                 "probe.py, honest_caveats"),
        "what_that_establishes": ("Protection against post-hoc selection, "
                                  "which is real and worth having."),
        "what_it_does_not_establish": ("That the law is derived. A^(1/3) is "
                                       "the Euclidean liquid-drop nuclear "
                                       "radius; it is imported "
                                       "phenomenology, not framework "
                                       "output."),
        "the_straddle": ("The same file states the kernel has 'NO free "
                         "parameter -- coth is forced by the Green's "
                         "function', i.e. the kernel is hyperbolic by "
                         "construction. Feeding a Euclidean size law into "
                         "a hyperbolic kernel mixes two geometries inside "
                         "one quantity."),
    })
    wb.add_data("what_the_geometry_requires", {
        "fact": ("In H^3 a ball of radius R has volume pi(sinh 2R - 2R) ~ "
                 "(pi/2)e^(2R), so R ~ (1/2)ln(2V/pi)."),
        "consequence": ("For extensive volume V ~ A the hyperbolic "
                        "separation scale grows like ln A, not A^(1/3)."),
        "caveat": ("V ~ A is itself an assumption. The corpus cannot check "
                   "it: see corpus_cannot_settle_it below."),
    })
    wb.add_data("law_scores", scored)
    wb.add_data("cost_of_geometric_self_consistency", {
        "euclidean_A_one_third": mp.nstr(euclid, 8),
        "hyperbolic_log_A": mp.nstr(hyper, 8),
        "ratio": mp.nstr(cost_of_consistency, 8),
        "reading": ("Using the geometry consistently costs a factor "
                    f"{mp.nstr(cost_of_consistency, 4)} in scatter. So "
                    "H_coth's fit quality depends on the geometric "
                    "mixture, not on the hyperbolic kernel alone."),
    })
    wb.add_data("corpus_cannot_settle_it", {
        "available": ("binding-link-volumes.witness.json carries hyperbolic "
                      "link volumes for A = 2 and A = 3 only: Hopf (0, "
                      "Seifert-fibred), 8_11 (8.2863), L6a4 (7.3277)."),
        "its_own_verdict": ("'the A-dependence is not in a single "
                            "binding-link volume' -- that witness's "
                            "description."),
        "consequence": ("There is no per-isotope hyperbolic geometry in the "
                        "corpus beyond A = 3, so no alpha(A) law can "
                        "currently be DERIVED from framework data. "
                        "Whatever law is used on this front is imported "
                        "from outside it."),
    })
    wb.add_data("preferred_power_DIAGNOSTIC", {
        "best_p": mp.nstr(best_p, 4),
        "rel_scatter_at_best_p": mp.nstr(best_s, 8),
        "rel_scatter_at_p_equals_one_third": mp.nstr(euclid, 8),
        "DOF_WARNING": ("This scan is a fit with one more DOF than any "
                        "fixed-p hypothesis. It is a diagnostic, never "
                        "support."),
        "reading": ("The optimum sits essentially ON the Euclidean "
                    "exponent, and its scatter is indistinguishable from "
                    "the p = 1/3 value, so the data is consistent with "
                    "exactly 1/3 and does not resolve a different power. "
                    "The data independently prefers the Euclidean nuclear "
                    "radius law."),
    })
    wb.add_data("deflationary_reading", {
        "claim": ("The kappa(A) profile is close to what plain Coulomb "
                  "repulsion in a Euclidean nucleus of radius R ~ A^(1/3) "
                  "gives, with the hyperbolic kernel contributing a small "
                  "curvature correction."),
        "pure_coulomb_scatter": mp.nstr(pure_coulomb, 8),
        "coth_scatter": mp.nstr(euclid, 8),
        "improvement_factor": mp.nstr(pure_coulomb / euclid, 8),
        "calibration": ("The curvature term does buy something real -- "
                        f"{mp.nstr(pure_coulomb*100,4)}% falls to "
                        f"{mp.nstr(euclid*100,4)}% for one shared "
                        "parameter. But a factor "
                        f"{mp.nstr(pure_coulomb/euclid,3)} in scatter is "
                        "suggestive, not decisive, and is comparable to "
                        "what the frozen-B_pp confound (qou-gcmn) could "
                        "account for on its own."),
        "NOT_claimed": ("That the geometry is Euclidean, that there is no "
                        "hyperbolic content, or that H_coth is refuted. "
                        "The measured range does not resolve the "
                        "question; that is the point."),
    })
    wb.add_data("scope", {
        "class": ("(a) scope-limited negative on an INPUT ASSUMPTION shared "
                  "by every hypothesis on this front"),
        "what_is_claimed": ("alpha ~ A^(1/3) is imported Euclidean "
                            "phenomenology, not derived; the framework "
                            "carries no data from which to derive a rival; "
                            "and geometric self-consistency costs "
                            f"{mp.nstr(cost_of_consistency,3)}x in fit."),
        "what_is_NOT_claimed": ("That A^(1/3) is wrong. The data prefers "
                                "it. What is claimed is that its warrant "
                                "is phenomenological rather than "
                                "framework-derived, and that this has "
                                "not been stated."),
    })

    verdict = (
        f"The separation law every kernel on this front is fed, alpha ~ "
        f"A^(1/3), is the EUCLIDEAN liquid-drop nuclear radius, imported "
        f"and labelled 'fixed in advance' -- which guards against post-hoc "
        f"selection but is not derivation. The kernel it feeds is "
        f"hyperbolic by construction, so the two mix geometries. Scored on "
        f"the same series: the imported law gives "
        f"{mp.nstr(euclid*100,4)}% scatter, the geometrically "
        f"self-consistent ln A law gives {mp.nstr(hyper*100,4)}% -- "
        f"consistency costs {mp.nstr(cost_of_consistency,3)}x. The corpus "
        f"cannot adjudicate: it carries hyperbolic link volumes at A = 2 "
        f"and 3 only. A free-power diagnostic lands at p = "
        f"{mp.nstr(best_p,3)}, indistinguishable from 1/3, so the data "
        f"independently prefers the Euclidean exponent. Deflationary "
        f"reading, stated plainly: kappa(A) is close to plain Coulomb in a "
        f"Euclidean nucleus ({mp.nstr(pure_coulomb*100,4)}% for the pure "
        f"1/r law), with the hyperbolic curvature term worth a factor "
        f"{mp.nstr(pure_coulomb/euclid,3)} on one shared parameter -- "
        f"suggestive, not decisive, and comparable to the frozen-B_pp "
        f"confound. Nothing here refutes H_coth; what it removes is the "
        f"impression that the hyperbolic reading was ever load-bearing "
        f"for the fit.")
    wb.add_data("verdict", verdict)
    wb.set_audit_only(
        "docs/audits/2026-08-25-em-linking-o2-neutrality-applied-to-kappa-contest.md")

    wb.add_assertion(
        name="scale_absorbs_multiplicative_factor",
        computed=1 if abs(hyper - half) < mpf("1e-30") else 0,
        expected=1, tolerance=0, unit="boolean",
        source=("ln A and (1/2)ln A are the same hypothesis once the scale "
                "constant is free, so they must score identically. A "
                "self-check on the scoring, not a result."))
    wb.add_assertion(
        name="geometric_consistency_costs_fit",
        computed=1 if cost_of_consistency > 2 else 0, expected=1,
        tolerance=0, unit="boolean",
        source=(f"Hyperbolic-consistent ln A scores "
                f"{mp.nstr(hyper*100,4)}% against the imported A^(1/3) at "
                f"{mp.nstr(euclid*100,4)}%, a factor "
                f"{mp.nstr(cost_of_consistency,4)}."))
    wb.add_assertion(
        name="data_prefers_the_euclidean_exponent",
        computed=1 if abs(best_p - third) < mpf("0.05") else 0,
        expected=1, tolerance=0, unit="boolean",
        source=(f"Free-power optimum p = {mp.nstr(best_p,4)} against the "
                f"Euclidean 1/3. Diagnostic with one extra DOF; recorded "
                f"as a boolean so a future run that moves it fails "
                f"loudly."))
    out = wb.save()

    print("alpha(A) law scores (same series, same statistic):\n")
    for name, s in sorted(scored.items(),
                          key=lambda kv: mpf(kv[1]["rel_scatter"])):
        print(f"  {mp.nstr(mpf(s['rel_scatter'])*100,4):>7}%  {name}")
    print(f"\ngeometric self-consistency costs "
          f"{mp.nstr(cost_of_consistency,4)}x in scatter")
    print(f"free-power diagnostic: p = {mp.nstr(best_p,4)} at "
          f"{mp.nstr(best_s*100,4)}%  (1/3 gives {mp.nstr(euclid*100,4)}%)")
    print(f"pure Coulomb 1/r (H_FH_A): {mp.nstr(pure_coulomb*100,4)}%  ->  "
          f"coth {mp.nstr(euclid*100,4)}%, factor "
          f"{mp.nstr(pure_coulomb/euclid,3)}")
    print(f"\nverdict:\n{verdict}")
    print(f"\nwitness -> {out}")


if __name__ == "__main__":
    main()
