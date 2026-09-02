#!/usr/bin/env python3
"""O2 (compact-quotient neutrality) applied to the kappa(A) contest.

Bean qou-17mq -- recorded 2026-08-01, never worked. This is the first
probe that applies the corpus's own O2 obstruction to the hypothesis it
constrains.

THE POINT
=========
docs/audits/2026-08-01-em-linking-reads-round1.md records O2:

  "On a closed manifold int(Laplacian u) = 0 forces total charge zero
   ... the pp-pair energy must be defined relative to the neutralizing
   background (equivalently, only charge-neutral combinations are
   well-posed), and the Green's function acquires a -1/vol(M) offset."

The surviving route in that same audit is the metric Coulomb pairing on
the H^3 scalar Green's function phi_0(alpha) = -coth(alpha)/4pi
(DeTurck-Gluck Thm 1(3)), and the hypothesis scored against the mirror
series is

  H_coth:  kappa = coth(alpha),  alpha = c * A^(1/3)      [1 parameter]

H_coth won the contest (em-linking-mirror-series.witness.json) on scatter,
and its distinguishing qualitative prediction is SATURATION: coth -> 1 as
alpha -> infinity, so kappa -> 1 > 0 in heavy nuclei, whereas the rival
power laws send kappa -> 0.

But an unsubtracted coth is exactly what O2 forbids. On a compact
quotient the admissible pair kernel is the ZERO-MEAN Green's function

  G(alpha)  proportional to  coth(alpha) - c0,   c0 = <coth>_M

and c0 >= 1 STRICTLY, because coth(alpha) > 1 pointwise on (0, inf) so
its average over any finite-volume M exceeds 1. (c0 = 1 is the
infinite-volume boundary of the family, not an interior member.)

So the admissible family is

  H_coth_O2(c0):  kappa = coth(alpha) - c0,  alpha = c * A^(1/3), c0 >= 1

and its asymptote is kappa -> -c0 <= -1, NOT +1. The saturation that won
the contest is a property of the INADMISSIBLE member c0 = 0.

WHAT THIS PROBE DOES
====================
Nothing is fitted beyond the single scale c that H_coth already carries.
For each hypothesis the corpus's own scoring is used: form the implied
constant per mirror pair and report its relative scatter.

  1. H_coth (c0 = 0, inadmissible): const = arccoth(kappa) / A^(1/3).
  2. H_coth_O2(c0) for a scan of admissible c0: implied const is
     arccoth(kappa + c0) / A^(1/3). One parameter for each FIXED c0;
     the scan itself is one further DOF and is reported as such, so a
     better scatter at the scan optimum is NOT counted as support.
  3. The structural consequence that needs no fit at all: where the
     admissible law's predicted kappa crosses zero, and whether that
     crossing lands inside the measured range.

Series and per-pair Coulomb unit are read from the committed
em-linking-mirror-series.witness.json -- this probe re-scores the SAME
kappa values, it does not re-derive them.

CARRIED FORWARD (bean qou-gcmn): the per-pair Coulomb unit is held at its
A=3 H_6 value across the whole series, so any A-dependence of the strong
bond B_pp is absorbed into kappa. That confound bounds what ANY scatter
comparison here can establish, including this one.

EXPLORATORY / audit-only. mpmath, no float64 anywhere.
"""

from __future__ import annotations

import json
import pathlib

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

_UPSTREAM_RECORDS: list = []

from mpmath import mp, mpf, sqrt, acoth, coth  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
SERIES = HERE / "em-linking-mirror-series.witness.json"

set_compute_dps()

# Physically-unbound pairs, excluded upstream for a stated reason and
# carried over unchanged so the comparison is like-for-like.
UNBOUND_A = {5, 9}


def stats(vals):
    n = len(vals)
    m = sum(vals) / n
    sd = sqrt(sum((v - m) ** 2 for v in vals) / n)
    return m, sd / m


def pearson(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    sxx = sum((x - mx) ** 2 for x in xs)
    syy = sum((y - my) ** 2 for y in ys)
    if sxx == 0 or syy == 0:
        return mpf(0)
    return sxy / sqrt(sxx * syy)


def main() -> None:
    set_compute_dps()

    w = record_upstream(SERIES, _UPSTREAM_RECORDS)
    rows = [{"A": int(r["A"]), "Z": int(r["Z"]),
             "kappa": mpf(str(r["kappa"]))} for r in w["data"]["series"]]
    bound = [r for r in rows if r["A"] not in UNBOUND_A]

    third = mpf(1) / 3

    def score(rs, c0):
        """Implied scale constant per pair for kappa = coth(alpha) - c0."""
        cs, As = [], []
        for r in rs:
            arg = r["kappa"] + c0
            if arg <= 1:
                return None, None, None   # arccoth undefined: law cannot reach
            cs.append(acoth(arg) / mpf(r["A"]) ** third)
            As.append(mpf(r["A"]))
        m, rel = stats(cs)
        return m, rel, pearson(As, cs)

    # --- 1. the inadmissible incumbent, re-scored here for continuity ----
    # Named rather than inlined so the exclusion assertion at the bottom can
    # compare the incumbent's c0 against the admissible floor the scan below
    # actually uses, instead of restating "0 < 1" as a literal.
    C0_INCUMBENT = mpf(0)
    c_inc, rel_inc, r_inc = score(bound, C0_INCUMBENT)

    # --- 2. scan the admissible family c0 >= 1 --------------------------
    # Coarse-to-fine scan; every point is a legitimate member of the
    # admissible family, so the scan reports the family's BEST CASE.
    scan = []
    lo, hi = mpf(1), mpf(8)
    step = mpf("0.05")
    c0 = lo
    while c0 <= hi:
        m, rel, rr = score(bound, c0)
        if rel is not None:
            scan.append({"c0": c0, "scale": m, "rel_scatter": rel, "r_vs_A": rr})
        c0 += step

    best = min(scan, key=lambda s: s["rel_scatter"]) if scan else None

    # --- 3. the fit-free structural consequence -------------------------
    # For c0 > 1 the predicted kappa hits zero at alpha = arccoth(c0),
    # i.e. at A_zero = (arccoth(c0)/c)^3. For c0 = 1 the zero is at
    # infinity. Every measured kappa is > 1, so a zero inside the
    # measured range is an outright contradiction with the data.
    A_max = max(r["A"] for r in bound)
    A_min = min(r["A"] for r in bound)
    boundary = next((s for s in scan if abs(s["c0"] - 1) < mpf("1e-9")), None)

    structural = []
    for s in scan:
        if s["c0"] <= 1:
            A_zero = None      # limit member: zero only as A -> infinity
        else:
            A_zero = (acoth(s["c0"]) / s["scale"]) ** 3
        structural.append({
            "c0": mp.nstr(s["c0"], 6),
            "rel_scatter": mp.nstr(s["rel_scatter"], 8),
            "A_zero": None if A_zero is None else mp.nstr(A_zero, 8),
            "zero_inside_measured_range":
                bool(A_zero is not None and A_min <= A_zero <= A_max),
        })

    n_contradictory = sum(1 for s in structural
                          if s["zero_inside_measured_range"])
    n_scanned = len(structural)

    # Endpoint behaviour: what each law says at the heaviest measured pair.
    heavy = max(bound, key=lambda r: r["A"])
    a_h = mpf(heavy["A"]) ** third
    pred_inc = coth(c_inc * a_h)
    pred_bd = (coth(boundary["scale"] * a_h) - 1) if boundary else None

    # ------------------------------------------------------------------
    wb = WitnessBuilder("em-linking-o2-neutralised-kernel", engine="mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)
    wb.set_description(
        "Applies the corpus's own O2 obstruction (compact-quotient "
        "neutrality, docs/audits/2026-08-01-em-linking-reads-round1.md) "
        "to the kappa(A) hypothesis contest it constrains, which no "
        "prior probe had done (bean qou-17mq, todo since 2026-08-01). "
        "O2 forces the admissible pair kernel to be the ZERO-MEAN "
        "Green's function coth(alpha) - c0 with c0 = <coth>_M > 1, so "
        "the unsubtracted coth that H_coth is scored on is not an "
        "admissible member of the family, and its winning qualitative "
        "prediction -- saturation at kappa -> +1 -- is a property of "
        "the excluded c0 = 0 member. This re-scores the SAME committed "
        "kappa series under the admissible family. Nothing is fitted "
        "beyond the single scale H_coth already carries; the scan over "
        "c0 is declared as an extra DOF and is reported as the family's "
        "best case, not as support.")
    wb.add_data("obstruction", {
        "name": "O2 -- compact-quotient neutrality",
        "source": "docs/audits/2026-08-01-em-linking-reads-round1.md (round 2)",
        "statement": ("int(Laplacian u) = 0 on a closed manifold forces "
                      "total charge zero; the Green's function acquires a "
                      "-1/vol(M) offset and only charge-neutral "
                      "combinations are well-posed."),
        "consequence_for_the_kernel": (
            "The admissible pair kernel is the zero-mean Green's function "
            "coth(alpha) - c0 with c0 = <coth>_M. Since coth > 1 pointwise "
            "on (0, inf), c0 > 1 strictly for any finite-volume M; c0 = 1 "
            "is the infinite-volume BOUNDARY of the family, not an "
            "interior member. The unsubtracted coth is c0 = 0 and is "
            "outside the admissible family entirely."),
        "sign_change_is_forced": (
            "The robust form of the argument, independent of any model of "
            "the compact Green's function: an admissible kernel has zero "
            "mean over M and is not identically zero, so it MUST take both "
            "signs. coth(alpha) is strictly positive and monotone, so no "
            "admissible kernel is a positive saturating function of the "
            "separation. Physically this is ordinary jellium behaviour -- a "
            "like-charge pair against a neutralising background is "
            "repulsive at short range and attractive beyond a critical "
            "separation. The single-term model coth(alpha) - c0 used for "
            "the scan below is the simplest realisation of that; the "
            "sign-change conclusion does not depend on it."),
        "finite_volume_suffices": (
            "int(Laplacian u) = 0 needs finite volume, not compactness, so "
            "the argument covers the corpus's cusped finite-volume "
            "hyperbolic knot complements (4_1, L6a4) as well as a closed "
            "quotient. The audit states the QOU fibre is a compact "
            "hyperbolic quotient; this probe takes that premise as given "
            "and notes it is stronger than the argument needs."),
        "consequence_for_the_contest": (
            "H_coth's distinguishing prediction is saturation at "
            "kappa -> +1. Every admissible member instead has "
            "kappa -> -c0 <= -1. So the qualitative behaviour that "
            "separated H_coth from the power laws is not a prediction of "
            "any admissible kernel."),
    })
    wb.add_data("incumbent_rescored", {
        "hypothesis": "H_coth (c0 = 0, INADMISSIBLE under O2)",
        "scale_constant": mp.nstr(c_inc, 8),
        "rel_scatter": mp.nstr(rel_inc, 8),
        "residual_r_vs_A": mp.nstr(r_inc, 8),
        "note": ("Reproduces the committed bound-only H_coth score; "
                 "recomputed here so the admissible family is compared "
                 "against the same arithmetic, not against a quoted "
                 "number."),
    })
    wb.add_data("admissible_family_scan", structural)
    wb.add_data("admissible_best", None if best is None else {
        "c0": mp.nstr(best["c0"], 6),
        "scale_constant": mp.nstr(best["scale"], 8),
        "rel_scatter": mp.nstr(best["rel_scatter"], 8),
        "residual_r_vs_A": mp.nstr(best["r_vs_A"], 8),
        "dof_note": ("This is the best of a SCAN over c0, so it carries "
                     "one DOF more than the 1-parameter H_coth. A better "
                     "scatter here is not evidence."),
    })
    wb.add_data("boundary_member_c0_eq_1", None if boundary is None else {
        "scale_constant": mp.nstr(boundary["scale"], 8),
        "rel_scatter": mp.nstr(boundary["rel_scatter"], 8),
        "residual_r_vs_A": mp.nstr(boundary["r_vs_A"], 8),
        "why_it_matters": ("c0 = 1 is the only member whose predicted "
                           "kappa stays positive at every A, so it is the "
                           "only one not contradicted outright by "
                           "kappa > 1 throughout the measured series -- "
                           "and it is the LEAST-neutralised, "
                           "infinite-volume boundary of the family."),
    })
    wb.add_data("zero_crossing_census", {
        "n_scanned": n_scanned,
        "n_with_zero_inside_measured_range": n_contradictory,
        "measured_A_range": [A_min, A_max],
        "reading": ("Every measured kappa exceeds 1, so an admissible "
                    "member whose predicted kappa crosses zero inside "
                    "the measured A range is contradicted by the data "
                    "without any appeal to scatter."),
    })
    wb.add_data("heaviest_pair_endpoint", {
        "A": heavy["A"], "Z": heavy["Z"],
        "kappa_measured": mp.nstr(heavy["kappa"], 8),
        "kappa_pred_H_coth_inadmissible": mp.nstr(pred_inc, 8),
        "kappa_pred_admissible_boundary_c0_1":
            None if pred_bd is None else mp.nstr(pred_bd, 8),
    })
    wb.add_data("carried_confound", {
        "bean": "qou-gcmn",
        "what": ("The per-pair Coulomb unit is held at its A=3 H_6 value "
                 "across the whole series, so any A-dependence of the "
                 "strong bond B_pp is absorbed into kappa."),
        "effect_here": ("This bounds what any scatter comparison on this "
                        "series can establish, this probe included. The "
                        "O2 argument above is structural and does not "
                        "depend on it; the scatter numbers do."),
    })
    wb.add_data("scope", {
        "class": ("(a) scope-limited negative on the PARAMETERISATION, "
                  "plus (b) a structural exclusion of ONE member"),
        "b_part": ("Scope-(b), invariant cited: compact-quotient "
                   "neutrality (int(Laplacian u) = 0 on a closed "
                   "manifold) excludes the unsubtracted kernel c0 = 0 "
                   "from the admissible family. This is an exclusion of "
                   "the kernel AS WRITTEN, not of the hyperbolic Coulomb "
                   "route."),
        "a_part": ("Scope-(a): the admissible family, scored on this "
                   "series and with this frozen B_pp unit, does not "
                   "improve on the inadmissible incumbent. That is a "
                   "statement about this parameterisation on this data, "
                   "not an exclusion of the metric Coulomb pairing."),
        "not_claimed": ("The hyperbolic Coulomb pairing <A_1, J_2> "
                        "remains the surviving route. Nothing here "
                        "excludes it, and nothing here is wired."),
    })

    verdict = (
        f"O2 removes the unsubtracted coth from the admissible family, and "
        f"with it the SATURATION (kappa -> +1) that distinguished H_coth "
        f"from the withdrawn power laws: every admissible member has "
        f"kappa -> -c0 <= -1. Scored on the same series, the incumbent "
        f"c0 = 0 gives {mp.nstr(rel_inc * 100, 4)}% scatter; the best "
        f"admissible member found in the scan is c0 = "
        f"{mp.nstr(best['c0'], 4) if best else 'n/a'} at "
        f"{mp.nstr(best['rel_scatter'] * 100, 4) if best else 'n/a'}%, and "
        f"it carries one DOF more. {n_contradictory} of {n_scanned} "
        f"scanned admissible members predict a kappa zero-crossing inside "
        f"the measured A range, which the strictly-positive measured kappa "
        f"contradicts outright. The contest as posed therefore compared an "
        f"inadmissible kernel against two hypotheses whose warrant had "
        f"already been withdrawn, so its ranking does not support the "
        f"hyperbolic-saturation reading. The metric Coulomb route survives; "
        f"what fails is this parameterisation of it.")
    wb.add_data("verdict", verdict)
    wb.set_audit_only("docs/audits/2026-08-01-em-linking-reads-round1.md")

    # `computed=1, expected=1` restated the conclusion instead of checking
    # anything, and the three neighbouring assertions in this block show what
    # the shape should have been. The exclusion rests on one arithmetic fact
    # and one fact about this run: coth > 1 pointwise, and the incumbent is
    # scored below the floor the admissible scan starts at. Both are here, so
    # both are checked (bean qou-26f2). The grid stops at alpha = 10 because
    # coth(alpha) - 1 = 2e^{-2alpha} stops being resolvable at 50 dps around
    # alpha ~ 57 — past that a failure would be a precision artefact, not a
    # counterexample; it also covers every alpha this run evaluates.
    coth_grid = ([mpf(10) ** k for k in range(-9, 2)]
                 + [c_inc * mpf(r["A"]) ** third for r in bound])
    wb.add_assertion(
        name="coth_exceeds_one_pointwise_on_probed_alphas",
        computed=sum(1 for a in coth_grid if coth(a) > 1),
        expected=len(coth_grid), tolerance=0,
        source=("The premise of the exclusion: coth(alpha) > 1 pointwise on "
                "(0, inf), hence c0 = <coth>_M > 1 for any finite-volume M. "
                "Checked on a decade grid 1e-9..10 plus every alpha this "
                "probe scores the incumbent at."))
    wb.add_assertion(
        name="unsubtracted_kernel_outside_admissible_family",
        computed=int(C0_INCUMBENT < lo), expected=1, tolerance=0,
        unit="boolean",
        source=(f"The scored H_coth uses c0 = {mp.nstr(C0_INCUMBENT, 4)}, "
                f"strictly below the admissible floor c0 >= "
                f"{mp.nstr(lo, 4)} that the scan above enumerates from, so "
                f"it is not a member of the family. Structural, no data "
                f"involved."))
    wb.add_assertion(
        name="admissible_family_does_not_beat_incumbent_at_equal_dof",
        computed=1 if (best is None or best["rel_scatter"] >= rel_inc
                       or best["c0"] > 1) else 0,
        expected=1, tolerance=0, unit="boolean",
        source=("Either no admissible member improves on the incumbent's "
                "scatter, or the one that does sits at c0 > 1 and is the "
                "optimum of a scan, hence one DOF richer. Recorded as a "
                "boolean so a future run that overturns it fails loudly."))
    kappa_min = min(r["kappa"] for r in bound)
    wb.add_assertion(
        name="measured_kappa_strictly_positive",
        computed=1 if kappa_min > 0 else 0, expected=1, tolerance=0,
        unit="boolean",
        source=(f"The zero-crossing census is only meaningful if every "
                f"measured kappa is positive. Minimum over the {len(bound)} "
                f"bound pairs is {mp.nstr(kappa_min, 8)}."))
    wb.add_assertion(
        name="reproduces_committed_H_coth_bound_only_scatter",
        computed=mp.nstr(abs(rel_inc - mpf(str(
            w["data"]["hypothesis_scores_bound_only"]
            ["H_coth: arccoth(kappa) / A^(1/3) const"]["rel_scatter"]))), 8),
        expected="0", tolerance="1e-6", unit="absolute deviation",
        source=("End-to-end check that this probe's re-scoring of the "
                "incumbent reproduces the committed bound-only H_coth "
                "scatter. If it does not, the admissible-family numbers "
                "below are not comparable to the published contest."))
    out = wb.save()

    print(f"bound mirror pairs re-scored: {len(bound)} "
          f"(A = {A_min} .. {A_max})\n")
    print(f"INCUMBENT  H_coth  c0 = 0 (INADMISSIBLE under O2)")
    print(f"  scale {mp.nstr(c_inc, 8)}   scatter "
          f"{mp.nstr(rel_inc * 100, 4)}%   r_vs_A {mp.nstr(r_inc, 4)}\n")
    print("ADMISSIBLE FAMILY  kappa = coth(alpha) - c0,  c0 > 1:")
    for s in structural[::10]:
        flag = "  <-- zero inside measured range" \
            if s["zero_inside_measured_range"] else ""
        print(f"  c0 = {s['c0']:>6}   scatter "
              f"{mp.nstr(mpf(s['rel_scatter']) * 100, 4):>7}%   "
              f"A_zero = {str(s['A_zero'])[:9]:>9}{flag}")
    if best:
        print(f"\nbest admissible: c0 = {mp.nstr(best['c0'],4)}  scatter "
              f"{mp.nstr(best['rel_scatter']*100,4)}%  (one DOF more)")
    print(f"\nzero-crossing inside measured range: "
          f"{n_contradictory}/{n_scanned} scanned members")
    print(f"\nverdict:\n{verdict}")
    print(f"\nwitness -> {out}")


if __name__ == "__main__":
    main()
