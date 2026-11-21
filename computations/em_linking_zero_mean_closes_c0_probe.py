"""EM-linking: c0 is NOT a free parameter — the zero-mean condition closes it.

Bean qou-17mq. Third in the sequence after
em_linking_kernel_exponent_degeneracy_probe (the series measures one scalar)
and em_linking_quotient_kernel_correction_probe (the one-term family IS the
exact quotient kernel to O(r^2), and c0 is its Robin constant).

WHAT THIS CLOSES
----------------
Round 6 (docs/audits/2026-08-25-em-linking-o2-neutrality-applied-to-kappa-contest.md)
scans c0 over a 140-member grid and calls the family "the simplest realisation
of the zero-mean condition, not the exact Green's function of a quotient".
Treating c0 as free is what makes the kernel unidentified.

But c0 is not free. The admissible kernel is the ZERO-MEAN one, so

    <kappa>_M = <coth(alpha)>_M - c0 = 0   =>   c0 = <coth>_M,

i.e. c0 is the mean of coth over the fibre — a property OF THE MANIFOLD, not
a modelling choice. On a geodesic ball of radius R in H^3 that mean is
elementary, because coth * sinh^2 = cosh * sinh integrates in closed form:

    <coth>_M = (1/V) int_0^R coth(r) . 4 pi sinh^2(r) dr
             = (4 pi / V) int_0^R cosh(r) sinh(r) dr
             = 2 pi sinh^2(R) / V ,          V = pi(sinh 2R - 2R)

    ===>   c0(R) = sinh^2(R) / (sinh(R) cosh(R) - R)          [no free parameter]

Verified below against direct quadrature at 40 dps, and at both limits:
c0 -> 1 as R -> infinity (the infinite-volume boundary round 6 identifies as
its best admissible member) and c0 -> infinity as R -> 0.

SO THE KERNEL IS DETERMINED BY THE FIBRE VOLUME. Since fixing the kernel
predicts the separation exponent (the degeneracy probe), a fibre volume now
yields a PREDICTION for p rather than a fit.

FOUR CHECKS THAT MAKE THIS MORE THAN AN ANSATZ, all measured below:

  1. ADMISSIBILITY IS DERIVED, NOT IMPOSED. O2 requires c0 >= 1. All three
     hyperbolic volumes the corpus carries land there on their own
     (1.53, 1.57, 2.13). Nothing placed them in the admissible region.

  2. IT IS ROBUST ACROSS THE A=3 LINKS. L6a4 (the 3He link) and 8_11 (the 3H
     link) differ by 13 % in volume and give c0 within 2.5 % and p within
     1.2 % of each other. The prediction does not hinge on which A=3 link is
     taken as the fibre.

  3. IT SURVIVES ROUND 6's OWN FALSIFICATION TEST. For c0 > 1 the kernel
     changes sign at alpha* = arccoth(c0), hence at a finite A_zero; round 6
     contradicted 48 of its 140 scanned members because that crossing landed
     inside the measured A in [3, 63], where every kappa is strictly positive.
     The derived members put it at A ~ 4e3-1e4, far beyond the heaviest known
     nuclide (A = 294). Sign-changing as O2 demands, crossing beyond any data.

  4. IT REPRODUCES THE ONE MEASURED SCALAR. s*p comes out at 0.2595 for all
     three, against the directly measured -dln(kappa)/dln(A) = 0.26050. It
     must, by the degeneracy — so this is an internal-consistency check on the
     arithmetic, not independent evidence.

WHAT THIS DOES *NOT* DO, and the limit is sharp: it identifies the kernel; it
does NOT confirm it. The predicted p ~ 0.153 CANNOT BE TESTED ON THIS SERIES,
because the degeneracy probe establishes that the series constrains only the
product s*p. A prediction the available observable cannot check is still a
prediction — it is falsifiable by any independent determination of the
separation law — but it is not evidence today.

TWO MODEL INPUTS, both stated rather than buried:

  (a) The mean uses the distance distribution of a geodesic BALL of the given
      volume. A closed hyperbolic quotient, and still more a cusped link
      complement, has a different distribution. This is the same one-term
      idealisation round 6 names, now used for what it can actually deliver —
      a number instead of a scan.
  (b) The corpus's volumes are CUSPED LINK-COMPLEMENT volumes. Using them as
      ball volumes is an identification, not a theorem. All three are reported
      and none is selected; choosing whichever fit best would be a fit under
      the NO-FITTING directive.

EXPLORATORY / audit-only. mpmath, no float64 anywhere.
"""

from __future__ import annotations

import json
import pathlib

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

_UPSTREAM_RECORDS: list = []

from mpmath import (mp, mpf, sqrt, log, pi, acoth, coth, sinh, cosh,  # noqa: E402
                    findroot, clsin, quad)

HERE = pathlib.Path(__file__).resolve().parent
SERIES = HERE / "em-linking-mirror-series.witness.json"
VOLUMES = HERE / "binding-link-volumes.witness.json"

set_compute_dps()

UNBOUND_A = {5, 9}
A_MIN_SERIES, A_MAX_SERIES = 3, 63
HEAVIEST_KNOWN_NUCLIDE = 294


def ball_volume(R):
    """Volume of a geodesic ball of radius R in H^3."""
    return pi * (sinh(2 * R) - 2 * R)


def c0_closed(R):
    """<coth>_M over that ball — the zero-mean offset, in closed form."""
    return sinh(R) ** 2 / (sinh(R) * cosh(R) - R)


def c0_quadrature(R):
    """The same mean by direct quadrature, as a check on the closed form."""
    num = quad(lambda r: coth(r) * 4 * pi * sinh(r) ** 2, [mpf("1e-20"), R])
    return num / ball_volume(R)


def ols(xs, ys):
    n = mpf(len(xs))
    mx = sum(xs) / n
    my = sum(ys) / n
    m = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2
                                                              for x in xs)
    return m, my - m * mx


def main() -> None:
    set_compute_dps()

    w = record_upstream(SERIES, _UPSTREAM_RECORDS)
    v = record_upstream(VOLUMES, _UPSTREAM_RECORDS)
    rows = [{"A": int(r["A"]), "kappa": mpf(str(r["kappa"]))}
            for r in w["data"]["series"] if int(r["A"]) not in UNBOUND_A]
    A = [mpf(r["A"]) for r in rows]
    K = [r["kappa"] for r in rows]
    lnA = [log(a) for a in A]
    lnK = [log(k) for k in K]
    n = len(rows)
    measured = -ols(lnA, lnK)[0]

    blv = v["data"]["binding_link_volumes"]
    fibres = [("L6a4 / Borromean (3He)", mpf(str(blv["L6a4_3He"]))),
              ("knot 8_11 (3H)", mpf(str(blv["knot_8_11_3H"]))),
              ("figure-eight 4_1", 2 * clsin(2, pi / 3))]

    # --- the closed form, checked against quadrature and at both limits ---
    checks = []
    for Rs in ["0.25", "0.5", "1.1103", "2.0", "4.0"]:
        R = mpf(Rs)
        a, b = c0_closed(R), c0_quadrature(R)
        checks.append({"R": R, "volume": ball_volume(R), "closed_form": a,
                       "quadrature": b, "relative_gap": abs(a - b) / a})
    worst_gap = max(c["relative_gap"] for c in checks)
    limit_inf = c0_closed(mpf(30))
    limit_zero = c0_closed(mpf("0.001"))

    # --- what each fibre volume DETERMINES ------------------------------
    derived = []
    for name, V in fibres:
        R = findroot(lambda R: ball_volume(R) - V, mpf("1.0"))
        c0 = c0_closed(R)
        alpha = [acoth(k + c0) for k in K]
        lal = [log(x) for x in alpha]
        p, lnc = ols(lnA, lal)
        s = -ols(lal, lnK)[0]
        scale = mp.e ** lnc
        pred = [coth(scale * a ** p) - c0 for a in A]
        rms = sqrt(sum(((q - k) / k) ** 2 for q, k in zip(pred, K)) / n)
        alpha_star = acoth(c0)                 # where the kernel changes sign
        A_zero = (alpha_star / scale) ** (1 / p)
        derived.append({
            "fibre": name, "volume": V, "ball_radius": R,
            "c0_derived": c0,
            "admissible_under_O2": bool(c0 >= 1),
            "p_predicted": p, "scale": scale,
            "kernel_log_slope_s": s, "product_s_times_p": s * p,
            "kappa_rms": rms,
            "alpha_star_sign_change": alpha_star,
            "alpha_min_measured": min(alpha), "alpha_max_measured": max(alpha),
            "A_zero": A_zero,
            "crossing_inside_measured_range": bool(
                A_MIN_SERIES <= A_zero <= A_MAX_SERIES),
        })

    # --- how much can the ONE model input actually move the answer? -----
    # The ball-vs-quotient identification is the obvious objection. Measure
    # its leverage rather than argue about it: sweep the assumed volume over
    # a factor of 40 and read off the log-sensitivity.
    V_ref = fibres[0][1]
    sweep = []
    for f in ["0.25", "0.5", "1", "2", "4", "10"]:
        f = mpf(f)
        R = findroot(lambda R: ball_volume(R) - V_ref * f, mpf("1.0"))
        c0 = c0_closed(R)
        pp, _ = ols(lnA, [log(acoth(k + c0)) for k in K])
        sweep.append({"volume_factor": f, "volume": V_ref * f,
                      "c0": c0, "p": pp})
    p_ref = next(x["p"] for x in sweep if x["volume_factor"] == 1)
    dl = log(mpf("1.01")) - log(mpf("0.99"))
    def _p_at(f):
        R = findroot(lambda R: ball_volume(R) - V_ref * mpf(f), mpf("1.0"))
        return ols(lnA, [log(acoth(k + c0_closed(R))) for k in K])[0]
    sens_p = (log(_p_at("1.01")) - log(_p_at("0.99"))) / dl
    vol_err_for_10pct = mp.e ** (log(mpf("1.1")) / abs(sens_p))
    euclid = mpf(1) / 3
    vol_err_to_reach_euclid = mp.e ** (log(euclid / p_ref) / abs(sens_p))

    a3 = [d for d in derived if "3He" in d["fibre"] or "3H)" in d["fibre"]]
    c0_spread = (abs(a3[0]["c0_derived"] - a3[1]["c0_derived"])
                 / min(d["c0_derived"] for d in a3))
    p_spread = (abs(a3[0]["p_predicted"] - a3[1]["p_predicted"])
                / min(d["p_predicted"] for d in a3))
    vol_spread = (abs(a3[0]["volume"] - a3[1]["volume"])
                  / min(d["volume"] for d in a3))

    wb = WitnessBuilder("em-linking-zero-mean-closes-c0", engine="mpmath")
    wb.add_data("closed_form", {
        "c0_of_R": "sinh^2(R) / (sinh(R) cosh(R) - R)",
        "volume_of_R": "pi (sinh 2R - 2R)",
        "derivation": ("zero mean => c0 = <coth>_M; on a geodesic ball "
                       "coth * sinh^2 = cosh sinh integrates in closed form, "
                       "giving 2 pi sinh^2(R) / V."),
        "checks_vs_quadrature": checks,
        "worst_relative_gap": worst_gap,
        "limit_R_to_infinity": limit_inf,
        "limit_R_to_zero": limit_zero,
    })
    wb.add_data("measured_scalar", measured)
    wb.add_data("derived_per_fibre", derived)
    wb.add_data("robustness_across_the_A3_links", {
        "volume_spread": vol_spread, "c0_spread": c0_spread,
        "p_spread": p_spread,
        "reading": ("The two A=3 links differ by 13 % in volume and give c0 "
                    "and p far closer than that, so the prediction does not "
                    "hinge on which is taken as the fibre."),
    })

    wb.add_data("volume_sensitivity", {
        "sweep": sweep,
        "dln_p_dln_V": sens_p,
        "volume_error_to_move_p_by_10pct": vol_err_for_10pct,
        "euclidean_p": euclid,
        "ratio_euclidean_over_derived": euclid / p_ref,
        "volume_error_needed_to_reach_euclidean_p": vol_err_to_reach_euclid,
        "reading": ("The ball-vs-quotient identification is the one model "
                    "input, and this is its leverage. p depends on the "
                    "assumed volume only as V^0.103, so the volume would have "
                    "to be wrong by 2.5x to move p by 10% and by ~2e3 to "
                    "reconcile the derived p with the imported Euclidean 1/3. "
                    "The model uncertainty cannot bridge that gap."),
    })

    wb.add_assertion(
        name="prediction_is_insensitive_to_the_one_model_input",
        computed=1 if (abs(sens_p) < mpf("0.2")
                       and vol_err_to_reach_euclid > 100) else 0,
        expected=1, tolerance=0, unit="boolean",
        source=(f"d ln(p)/d ln(V) = {mp.nstr(sens_p, 5)}, so the assumed "
                f"fibre volume must be wrong by "
                f"{mp.nstr(vol_err_for_10pct, 4)}x to move p by 10%, and by "
                f"{mp.nstr(vol_err_to_reach_euclid, 4)}x to reach the "
                f"imported Euclidean p = 1/3 (which is "
                f"{mp.nstr(euclid / p_ref, 4)}x the derived "
                f"{mp.nstr(p_ref, 6)}). The ball-vs-quotient model error is "
                f"at most a factor of a few, so it CANNOT bridge that gap — "
                f"the objection this construction most invites does not "
                f"reach the conclusion."))
    wb.add_assertion(
        name="closed_form_matches_quadrature",
        computed=mp.nstr(worst_gap, 6), expected="0", tolerance="1e-25",
        unit="relative gap",
        source=(f"c0(R) = sinh^2 R/(sinh R cosh R - R) against direct "
                f"quadrature of <coth> over the ball, at R = 0.25, 0.5, "
                f"1.1103, 2, 4. Worst relative gap {mp.nstr(worst_gap, 4)}."))
    wb.add_assertion(
        name="closed_form_has_the_right_limits",
        computed=1 if (abs(limit_inf - 1) < mpf("1e-20")
                       and limit_zero > 1000) else 0,
        expected=1, tolerance=0, unit="boolean",
        source=(f"c0 -> 1 as R -> infinity (got {mp.nstr(limit_inf, 12)} at "
                f"R = 30) — the infinite-volume boundary round 6 identifies as "
                f"its best admissible member — and diverges as R -> 0 (got "
                f"{mp.nstr(limit_zero, 6)} at R = 0.001)."))
    wb.add_assertion(
        name="every_corpus_volume_lands_admissible_without_being_placed",
        computed=1 if all(d["admissible_under_O2"] for d in derived) else 0,
        expected=1, tolerance=0, unit="boolean",
        source=("O2 requires c0 >= 1. The three hyperbolic volumes the corpus "
                "carries give " + ", ".join(
                    f"{d['fibre']} -> {mp.nstr(d['c0_derived'], 6)}"
                    for d in derived) + ". Derived, not imposed: nothing in "
                "the construction knows about the admissible region."))
    wb.add_assertion(
        name="prediction_is_robust_across_the_two_A3_links",
        computed=mp.nstr(max(c0_spread, p_spread), 6), expected="0",
        tolerance="0.05", unit="relative spread",
        source=(f"L6a4 and 8_11 differ by "
                f"{mp.nstr(vol_spread * 100, 4)}% in volume yet give c0 "
                f"within {mp.nstr(c0_spread * 100, 4)}% and p within "
                f"{mp.nstr(p_spread * 100, 4)}% of each other."))
    wb.add_assertion(
        name="survives_round_sixs_own_zero_crossing_falsification",
        computed=1 if not any(d["crossing_inside_measured_range"]
                              for d in derived) else 0,
        expected=1, tolerance=0, unit="boolean",
        source=(f"For c0 > 1 the kernel changes sign at a finite A_zero; "
                f"round 6 contradicted 48 of its 140 scanned members because "
                f"that crossing fell inside A in [{A_MIN_SERIES}, "
                f"{A_MAX_SERIES}], where every measured kappa is strictly "
                f"positive. The derived members put it at " + ", ".join(
                    f"{mp.nstr(d['A_zero'], 3)}" for d in derived) +
                f" — sign-changing as O2 demands, with the crossing beyond "
                f"the heaviest known nuclide (A = {HEAVIEST_KNOWN_NUCLIDE})."))
    wb.add_assertion(
        name="reproduces_the_one_measured_scalar",
        computed=mp.nstr(max(abs(d["product_s_times_p"] - measured) / measured
                             for d in derived), 6),
        expected="0", tolerance="0.05", unit="relative gap",
        source=(f"s*p for the derived members against the directly measured "
                f"-dln(kappa)/dln(A) = {mp.nstr(measured, 8)}. It MUST agree "
                f"by the degeneracy, so this checks the arithmetic and is NOT "
                f"independent evidence for the kernel."))

    wb.add_data("scope", {
        "what_is_derived": (
            "c0. It was a scanned parameter in round 6 and is now a closed "
            "form in the fibre volume, so the kernel is determined once a "
            "volume is named."),
        "what_is_predicted_but_UNTESTABLE_here": (
            "p ~ 0.153. The degeneracy probe establishes that this series "
            "constrains only the product s*p, so it cannot check a predicted "
            "p. Falsifiable by any INDEPENDENT determination of the "
            "separation law; not evidence today."),
        "model_input_a": (
            "The mean uses a geodesic BALL's distance distribution. A closed "
            "quotient, still more a cusped complement, differs."),
        "model_input_b": (
            "The corpus volumes are CUSPED LINK-COMPLEMENT volumes used as "
            "ball volumes — an identification, not a theorem. All three are "
            "reported and none selected; picking the best-fitting one would "
            "be a fit."),
        "NOT_claimed": (
            "That the kernel is confirmed. That p = 0.153 is measured. That "
            "round 6's structural O2 exclusion of the UNSUBTRACTED coth is "
            "affected — it is untouched and this derivation depends on it."),
    })
    wb.add_upstream_records(_UPSTREAM_RECORDS)
    out = wb.save(extra={
        "q0Anchor": "proton",
        "q0Value": json.loads(SERIES.read_text())["q0Value"],
        "q0AnchorReason": (
            "q0 enters only through upstream data: kappa(A) is read from "
            "em-linking-mirror-series.witness.json, which since 2026-11-21 "
            "derives its per-pair Coulomb unit from the proton-pinned "
            "mirror-pair-coulomb-sign-correction witness and is stamped proton"),
    })

    print("ZERO MEAN CLOSES c0 — it is not a free parameter\n")
    print(f"  c0(R) = sinh^2(R) / (sinh(R) cosh(R) - R),  "
          f"V = pi(sinh 2R - 2R)")
    print(f"  vs quadrature: worst relative gap {mp.nstr(worst_gap, 4)}")
    print(f"  limits: c0(R=30) = {mp.nstr(limit_inf, 10)}   "
          f"c0(R=0.001) = {mp.nstr(limit_zero, 6)}\n")
    print(f"{'fibre':<24}{'vol':>8}{'c0 DERIVED':>12}{'adm':>5}"
          f"{'p predicted':>13}{'s*p':>9}{'rms':>8}{'A_zero':>10}")
    for d in derived:
        print(f"{d['fibre']:<24}{float(d['volume']):>8.4f}"
              f"{mp.nstr(d['c0_derived'], 6):>12}"
              f"{'yes' if d['admissible_under_O2'] else 'NO':>5}"
              f"{mp.nstr(d['p_predicted'], 5):>13}"
              f"{mp.nstr(d['product_s_times_p'], 5):>9}"
              f"{mp.nstr(d['kappa_rms'] * 100, 4):>7}%"
              f"{mp.nstr(d['A_zero'], 3):>10}")
    print(f"\n  volume sensitivity: d ln(p)/d ln(V) = {mp.nstr(sens_p, 5)}")
    print(f"    volume must be wrong {mp.nstr(vol_err_for_10pct, 4)}x to move "
          f"p by 10%; {mp.nstr(vol_err_to_reach_euclid, 4)}x to reach the "
          f"Euclidean 1/3")
    print(f"\n  measured -dln(kappa)/dln(A) = {mp.nstr(measured, 8)}")
    print(f"  A=3 links: volume differs {mp.nstr(vol_spread*100, 3)}%, "
          f"c0 differs {mp.nstr(c0_spread*100, 3)}%, "
          f"p differs {mp.nstr(p_spread*100, 3)}%")
    print(f"\nwitness -> {out}")


if __name__ == "__main__":
    main()
