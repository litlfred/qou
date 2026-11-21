"""EM-linking: the derived c0 is INVISIBLE to the series that motivated it.

Bean qou-17mq. Fourth in the sequence, and the one that closes the loop:

  1. em_linking_kernel_exponent_degeneracy_probe   -- the kappa(A) series
     constrains only the product s*p; kernel and separation exponent are
     jointly unidentifiable.
  2. em_linking_quotient_kernel_correction_probe   -- the one-term family IS
     the exact quotient kernel to O(r^2), and c0 is its Robin constant.
  3. em_linking_zero_mean_closes_c0_probe          -- c0 is not free at all:
     zero mean forces c0 = <coth>_M, closed form on a geodesic ball.
  4. THIS PROBE                                    -- and the series cannot
     tell the difference. Measured, not asserted.

WHY THIS IS WORTH A PROBE OF ITS OWN
------------------------------------
Probe 3 ends by saying the derivation "identifies the kernel but does not
confirm it", on the strength of probe 1's algebra. That is an argument. This
probe MEASURES it, and the measurement could have come out the other way: if
the derived c0 sat at a sharp optimum of the fit landscape, the series WOULD
have seen it, and probe 3's caution would have been over-modest.

It does not. Scale-free fit quality is flat across the whole admissible-and-
inadmissible c0 range, and the derived value sits interior and unremarkable.

THE METRIC TRAP, RECORDED BECAUSE IT NEARLY BECAME A CLAIM
----------------------------------------------------------
The obvious quality metric -- rms of the residuals of ln(alpha) on ln(A),
where alpha(A) = acoth(kappa(A) + c0) -- is BROKEN, and it is broken in a way
that looks like a strong result:

    c0        0     0.25   0.50      1     1.5      2      3      4    7.5
    rms   .03461  .02725 .02375  .01993  .01755 .01576 .01315 .01131 .00760

Monotone decreasing, a factor of 4.56 end to end. Read naively that ranks the
kernels decisively and picks the largest c0 scanned.

It is an artifact. As c0 -> infinity, acoth(kappa + c0) -> 1/(kappa + c0) ->
1/c0, a CONSTANT; and a constant lies on a power law trivially, with p -> 0.
The p column shrinks in lockstep (0.3291 -> 0.0550) for exactly the same
reason. The metric rewards a kernel for flattening the very quantity whose
variation it is supposed to explain.

Both facts are asserted below, so the diagnosis is falsifiable rather than
narrated: if the rms sequence were not monotone, or if p did NOT shrink
alongside it, the artifact explanation would be wrong.

WHAT A SCALE-FREE METRIC SAYS
-----------------------------
R^2 (fraction of variance in ln alpha explained by ln A) and rms/span are
invariant under the rescaling that produces the artifact:

    c0        0     0.25   0.50      1     1.5      2      3      4    7.5
    R^2    .9779   .9800  .9796  .9773   .9750  .9729  .9696  .9673  .9625

The whole spread is 0.0175 -- SMALLER than the ~0.020 of variance the best
member leaves unexplained. Between-model variation is below within-model
residual, which is the precise sense in which this observable cannot rank
these kernels. The derived c0 = 1.5699 lands at R^2 = 0.9746: interior,
sixth-best of nine (5 scanned members fit better), and 0.0054 from the top
of a range 0.0175 wide.

TWO SIDE FINDINGS ON ROUND 6
----------------------------
Round 6 reports scatter rising MONOTONICALLY in c0 (3.505% at c0 = 0 to
22.32% at c0 = 7.5) and reads that as a numerical case against neutralisation.
With p freed and the metric made scale-free, neither half survives:

  (a) the landscape is FLAT, not monotone; and
  (b) its shallow optimum is at c0 ~ 0.25-0.50 -- INADMISSIBLE, below the O2
      floor c0 >= 1, but also NOT at c0 = 0, so it does not favour the
      incumbent unsubtracted kernel either.

Finding (b) is reported as a location, NOT as a preference: 0.0054 in R^2
over 29 points is not a discriminating margin, and saying otherwise would be
the same error this probe exists to catch.

A TEST THAT CANNOT FAIL, RECORDED SO NOBODY BANKS IT
-----------------------------------------------------
alpha = acoth(kappa + c0) is real only for kappa + c0 > 1, so "does the
derived c0 keep every point invertible?" looks like a falsification test.
It is vacuous: min(kappa) over the bound series is 1.4020 > 1, so the
condition holds for ANY c0 >= 0, admissible or not. Asserted below as a
vacuity record, not as a passed check.

NOTHING IS FITTED AND NOTHING IS WIRED. No kernel is selected -- the finding
is that this observable cannot select one. Series and kappa values are read
from the committed witness and are not re-derived.

EXPLORATORY / audit-only. mpmath, no float64 anywhere.
"""

from __future__ import annotations

import pathlib

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

_UPSTREAM_RECORDS: list = []

from mpmath import (mp, mpf, acoth, clsin, log, sqrt, sinh, cosh,  # noqa: E402
                    pi, findroot)

HERE = pathlib.Path(__file__).resolve().parent
SERIES = HERE / "em-linking-mirror-series.witness.json"
VOLUMES = HERE / "binding-link-volumes.witness.json"

set_compute_dps()

# Physically-unbound, excluded upstream for a stated reason; carried over
# unchanged so this is like-for-like with probes 1 and 3.
UNBOUND_A = {5, 9}

# The same grid probe 1 scans, so the two are directly comparable. Members
# below the O2 floor c0 >= 1 are scanned and LABELLED inadmissible; they are
# here to locate the landscape's shape, never as candidates.
C0_SCAN = ["0", "0.25", "0.50", "1", "1.5", "2", "3", "4", "7.5"]
C0_ADMISSIBLE_FLOOR = mpf(1)


def ball_volume(R):
    """Volume of a geodesic ball of radius R in H^3."""
    return pi * (sinh(2 * R) - 2 * R)


def c0_closed(R):
    """<coth>_M over that ball -- the zero-mean offset (probe 3)."""
    return sinh(R) ** 2 / (sinh(R) * cosh(R) - R)


def radius_of_volume(V):
    """Invert ball_volume. Monotone, so the root is unique."""
    return findroot(lambda r: ball_volume(r) - V, mpf("1.5"))


def fit(ln_x, ln_y):
    """OLS of ln_y on ln_x, with the quality measures that matter.

    Returns (slope, intercept, rms, r_squared, rms_over_span). The last two
    are invariant under y -> c*y, which is exactly the rescaling that makes
    the bare rms misleading here.
    """
    n = mpf(len(ln_x))
    mx = sum(ln_x) / n
    my = sum(ln_y) / n
    slope = (sum((x - mx) * (y - my) for x, y in zip(ln_x, ln_y))
             / sum((x - mx) ** 2 for x in ln_x))
    intercept = my - slope * mx
    res = [y - (intercept + slope * x) for x, y in zip(ln_x, ln_y)]
    ss_res = sum(r ** 2 for r in res)
    ss_tot = sum((y - my) ** 2 for y in ln_y)
    rms = sqrt(ss_res / n)
    span = max(ln_y) - min(ln_y)
    return slope, intercept, rms, 1 - ss_res / ss_tot, rms / span


def main() -> None:
    set_compute_dps()

    w = record_upstream(SERIES, _UPSTREAM_RECORDS)
    v = record_upstream(VOLUMES, _UPSTREAM_RECORDS)

    rows = sorted((int(r["A"]), mpf(str(r["kappa"])))
                  for r in w["data"]["series"]
                  if int(r["A"]) not in UNBOUND_A)
    ln_A = [log(mpf(A)) for A, _ in rows]
    kappas = [k for _, k in rows]
    kappa_min = min(kappas)

    # ---- the scan, with both the broken and the scale-free metrics -------
    scan = []
    for s in C0_SCAN:
        c0 = mpf(s)
        alpha = [acoth(k + c0) for k in kappas]
        p, _, rms, r2, nrms = fit(ln_A, [log(a) for a in alpha])
        scan.append({
            "c0": mp.nstr(c0, 6),
            "admissible": bool(c0 >= C0_ADMISSIBLE_FLOOR),
            "p": mp.nstr(p, 10),
            "rms_ln_alpha": mp.nstr(rms, 10),
            "r_squared": mp.nstr(r2, 12),
            "rms_over_span": mp.nstr(nrms, 10),
            "_p": p, "_rms": rms, "_r2": r2, "_nrms": nrms, "_c0": c0,
        })

    rms_seq = [e["_rms"] for e in scan]
    p_seq = [e["_p"] for e in scan]
    r2_seq = [e["_r2"] for e in scan]
    nrms_seq = [e["_nrms"] for e in scan]

    rms_monotone = all(rms_seq[i] > rms_seq[i + 1] for i in range(len(rms_seq) - 1))
    p_monotone = all(p_seq[i] > p_seq[i + 1] for i in range(len(p_seq) - 1))

    r2_spread = max(r2_seq) - min(r2_seq)
    unexplained_at_best = 1 - max(r2_seq)
    best_idx = max(range(len(scan)), key=lambda i: r2_seq[i])
    best = scan[best_idx]

    # ---- the derived c0, at each fibre volume the corpus carries ---------
    # The same three fibres probe 3 uses, read the same way: the two the
    # corpus assigns to A = 3, plus the figure-eight. The Hopf link (2H) is
    # Seifert-fibred with Vol = 0 and has no ball radius, so it is skipped
    # here exactly as it is there.
    blv = v["data"]["binding_link_volumes"]
    fibre_inputs = [("L6a4 / Borromean (3He)", mpf(str(blv["L6a4_3He"]))),
                    ("knot 8_11 (3H)", mpf(str(blv["knot_8_11_3H"]))),
                    ("figure-eight 4_1", 2 * clsin(2, pi / 3))]

    fibres = []
    for label, V in fibre_inputs:
        if V <= 0:
            continue
        c0 = c0_closed(radius_of_volume(V))
        alpha = [acoth(k + c0) for k in kappas]
        p, _, rms, r2, nrms = fit(ln_A, [log(a) for a in alpha])
        n_better = sum(1 for x in r2_seq if x > r2)
        fibres.append({
            "label": label,
            "volume": mp.nstr(V, 12),
            "c0_derived": mp.nstr(c0, 12),
            "p": mp.nstr(p, 10),
            "r_squared": mp.nstr(r2, 12),
            "rms_over_span": mp.nstr(nrms, 10),
            "scanned_members_fitting_better": n_better,
            "r2_gap_to_best": mp.nstr(max(r2_seq) - r2, 8),
            "_r2": r2, "_c0": c0, "_p": p, "_nbetter": n_better,
        })

    if not fibres:
        raise SystemExit("no usable fibre volume in the upstream witness — "
                         "refusing to report a landscape position with no "
                         "point to place on it")

    # The primary fibre for the headline statements: the one probe 3 leads
    # with. Chosen by NAME, never by which one fits best.
    primary = next((f for f in fibres if "L6a4" in f["label"]
                    or "orromean" in f["label"]), fibres[0])

    interior = all(min(r2_seq) < f["_r2"] < max(r2_seq) for f in fibres)
    below_within = r2_spread < unexplained_at_best

    print("EM-linking: is the derived c0 visible to the kappa(A) series?")
    print(f"  bound points: {len(rows)}  A in [{rows[0][0]}, {rows[-1][0]}]")
    print(f"  min(kappa) = {mp.nstr(kappa_min, 8)}")
    print()
    print(f"  {'c0':>6s} {'adm':>4s} {'p':>10s} {'rms':>9s} {'R^2':>10s} "
          f"{'rms/span':>9s}")
    for e in scan:
        print(f"  {e['c0']:>6s} {'y' if e['admissible'] else 'n':>4s} "
              f"{mp.nstr(e['_p'], 6):>10s} {mp.nstr(e['_rms'], 4):>9s} "
              f"{mp.nstr(e['_r2'], 6):>10s} {mp.nstr(e['_nrms'], 4):>9s}")
    print()
    for f in fibres:
        print(f"  DERIVED {f['label']:<22s} c0={mp.nstr(f['_c0'], 8):>10s} "
              f"p={mp.nstr(f['_p'], 6):>9s} R^2={mp.nstr(f['_r2'], 6):>8s} "
              f"({f['_nbetter']} of {len(scan)} scanned fit better)")
    print()
    print(f"  R^2 spread across scan      : {mp.nstr(r2_spread, 4)}")
    print(f"  variance unexplained at best: {mp.nstr(unexplained_at_best, 4)}")
    print(f"  => between-model < within-model: {below_within}")

    wb = WitnessBuilder("em-linking-derived-c0-is-invisible-to-the-series",
                        engine="mpmath")
    wb.set_description(
        "Bean qou-17mq. MEASURES what probe 3 argued: the zero-mean-derived "
        "c0 is invisible to the kappa(A) series. Scale-free fit quality is "
        "flat across the whole c0 scan (R^2 spread smaller than the variance "
        "the best member leaves unexplained) and the derived value sits "
        "interior. Also records that the bare-rms metric is monotone in c0 "
        "by construction (acoth(kappa+c0) -> 1/c0, a constant, as c0 grows) "
        "and therefore cannot rank kernels, and that the invertibility test "
        "kappa + c0 > 1 is vacuous here. EXPLORATORY. Nothing fitted, "
        "nothing wired, no kernel selected."
    )

    wb.add_assertion(
        name="invertibility_test_is_vacuous_min_kappa_already_exceeds_one",
        computed=1 if kappa_min > 1 else 0,
        expected=1, tolerance=0, unit="boolean",
        source=(f"min(kappa) = {mp.nstr(kappa_min, 12)} > 1 over the "
                f"{len(rows)} bound points, so acoth(kappa + c0) is real for "
                "EVERY c0 >= 0 — admissible or not. Recorded so that 'the "
                "derived c0 keeps the series invertible' is never banked as "
                "a passed test: it is a test that cannot fail."),
    )

    wb.add_assertion(
        name="bare_rms_is_monotone_in_c0_so_it_cannot_rank_kernels",
        computed=1 if rms_monotone else 0,
        expected=1, tolerance=0, unit="boolean",
        source=(f"rms(ln alpha) falls monotonically across the scan, "
                f"{mp.nstr(rms_seq[0], 6)} -> {mp.nstr(rms_seq[-1], 6)} "
                f"(factor {mp.nstr(rms_seq[0] / rms_seq[-1], 4)}). Not "
                "evidence: as c0 grows, acoth(kappa + c0) -> 1/c0, a "
                "constant, and a constant lies on a power law trivially."),
    )

    wb.add_assertion(
        name="and_p_shrinks_in_lockstep_which_is_what_makes_it_an_artifact",
        computed=1 if p_monotone else 0,
        expected=1, tolerance=0, unit="boolean",
        source=(f"p falls monotonically alongside it, "
                f"{mp.nstr(p_seq[0], 6)} -> {mp.nstr(p_seq[-1], 6)}. This is "
                "the falsifiable half of the artifact diagnosis: if the rms "
                "improved while p did NOT collapse toward 0, the flattening "
                "explanation would be wrong and the rms ranking might have "
                "meant something."),
    )

    wb.add_assertion(
        name="scale_free_between_model_spread_is_below_within_model_residual",
        computed=1 if below_within else 0,
        expected=1, tolerance=0, unit="boolean",
        source=(f"R^2 across the whole scan spans {mp.nstr(r2_spread, 6)}, "
                f"against {mp.nstr(unexplained_at_best, 6)} of variance the "
                "best member leaves unexplained. Choosing between these "
                "kernels moves less than the residual within any one of "
                "them — the precise sense in which this observable cannot "
                "rank them. Threshold is a comparison of two measured "
                "quantities, not a chosen tolerance."),
    )

    wb.add_assertion(
        name="every_derived_c0_lands_interior_not_at_an_optimum",
        computed=1 if interior else 0,
        expected=1, tolerance=0, unit="boolean",
        source=("; ".join(
            f"{f['label']}: R^2 {mp.nstr(f['_r2'], 8)}, "
            f"{f['_nbetter']} of {len(scan)} scanned members fit better"
            for f in fibres)
            + ". Could have failed: a derivation that landed at the top or "
              "bottom of the landscape would be visible to the series."),
    )

    wb.add_assertion(
        name="the_shallow_optimum_is_inadmissible_but_is_not_the_incumbent",
        computed=1 if (best["_c0"] < C0_ADMISSIBLE_FLOOR
                       and best["_c0"] > 0) else 0,
        expected=1, tolerance=0, unit="boolean",
        source=(f"the scale-free optimum is at c0 = {best['c0']} "
                f"(R^2 {mp.nstr(best['_r2'], 8)}), below the O2 floor of 1 "
                "and so INADMISSIBLE, but strictly above 0 and so not the "
                "unsubtracted incumbent either. Reported as a LOCATION, not "
                "a preference: the margin over the derived value is "
                f"{mp.nstr(max(r2_seq) - primary['_r2'], 4)} in R^2 over "
                f"{len(rows)} points, which discriminates nothing."),
    )

    wb.add_assertion(
        name="round_six_monotone_scatter_claim_does_not_survive_freeing_p",
        computed=1 if not all(nrms_seq[i] < nrms_seq[i + 1]
                              for i in range(len(nrms_seq) - 1)) else 0,
        expected=1, tolerance=0, unit="boolean",
        source=("round 6 reports scatter rising monotonically in c0 (3.505% "
                "at c0 = 0 to 22.32% at c0 = 7.5) with p PINNED at 1/3. With "
                "p freed and the metric scale-free, rms/span is NOT monotone "
                f"increasing: it runs {mp.nstr(nrms_seq[0], 4)} -> "
                f"{mp.nstr(min(nrms_seq), 4)} -> {mp.nstr(nrms_seq[-1], 4)}, "
                f"a total factor of {mp.nstr(max(nrms_seq) / min(nrms_seq), 4)}. "
                "Independent of, and consistent with, the degeneracy probe's "
                "correction of the same audit."),
    )

    for e in scan:
        for k in ("_p", "_rms", "_r2", "_nrms", "_c0"):
            e.pop(k)
    for f in fibres:
        for k in ("_r2", "_c0", "_p", "_nbetter"):
            f.pop(k)

    wb.save(extra={
        "q0Anchor": "ambiguous",
        "q0AnchorReason": (
            "q0 enters only through upstream data: kappa(A) is read from "
            "em-linking-mirror-series.witness.json, whose producer divides by "
            "a TYPED per-pair Coulomb unit tanh(ln q0)*B_pp = 0.2376702253 "
            "with no recorded pin (the proton-pinned "
            "mirror-pair-coulomb-sign-correction witness it cites now carries "
            "0.2212723003), and that upstream witness is itself unstamped; the "
            "pin of the series this probe fits is therefore undetermined"),
        "n_bound_points": len(rows),
        "A_range": [rows[0][0], rows[-1][0]],
        "kappa_min": mp.nstr(kappa_min, 12),
        "scan": scan,
        "derived_fibres": fibres,
        "landscape": {
            "r_squared_spread": mp.nstr(r2_spread, 12),
            "variance_unexplained_at_best": mp.nstr(unexplained_at_best, 12),
            "between_model_below_within_model": below_within,
            "optimum_c0": best["c0"],
            "optimum_is_admissible": best["admissible"],
        },
        "scope": (
            "SCOPE (a). This construction, alone, cannot rank these kernels "
            "on this observable. It is NOT a structural exclusion of any "
            "kernel: no proved invariant is cited, and a different "
            "observable — one that sees the separation without going "
            "through the kernel — would rank them. That measurement does "
            "not exist in the corpus and is the open item on qou-17mq."
        ),
        "upstream_witness_hashes": _UPSTREAM_RECORDS,
    })

    print()
    print("wrote em-linking-derived-c0-is-invisible-to-the-series.witness.json")


if __name__ == "__main__":
    main()
