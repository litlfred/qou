"""EM-linking: the kappa(A) series measures ONE number, not a kernel.

Bean qou-17mq (O2 neutrality), with qou-gcmn (frozen B_pp) and qou-u3vw
(flux scaling) as the other legs of the same degeneracy.

WHAT THIS CORRECTS
------------------
docs/audits/2026-08-25-em-linking-o2-neutrality-applied-to-kappa-contest.md
("round 6") establishes, correctly and structurally, that compact- (indeed
finite-volume-) quotient neutrality `int Laplacian u = 0` excludes the
UNSUBTRACTED kernel coth(alpha) and admits only a sign-changing, zero-mean
one -- modelled there by the one-parameter family

    kappa = coth(alpha) - c0,      c0 >= 1.

That structural exclusion is untouched here.

Round 6 then goes further and builds a NUMERICAL case against the
admissible family: scatter rises monotonically in c0 (3.505% at the
inadmissible c0 = 0 to 22.32% at c0 = 7.5), and the best admissible
member carries a residual trend r = -0.904, worse than the hypothesis
the contest had rejected for carrying structure.

Every one of those numbers is computed with the separation exponent
PINNED at 1/3 -- `score(rs, c0)` in em_linking_o2_neutralised_kernel_probe.py
hardcodes `acoth(kappa + c0) / A**third` for every c0 in its scan. And
the THIRD finding of that same audit establishes that `alpha ~ A^(1/3)`
is imported Euclidean liquid-drop phenomenology, not framework output:

    "no alpha(A) law can currently be DERIVED from framework data;
     whatever law is used on this front is imported from outside it."

The free-power diagnostic that finding runs lives in a different probe
(em_linking_alpha_scaling_provenance_probe.py) and is evaluated at
c0 = 0 only. So the two findings were never crossed: the exponent was
freed for the incumbent and pinned for its rivals.

WHAT THIS PROBE MEASURES
------------------------
Write any hypothesis on this front as a kernel F and a separation law:

    kappa = F(alpha),      alpha = c * A^p.

Then, identically,

    dln(kappa)/dln(A)  =  s * p,       s := -dln F / dln alpha,

so the series constrains only the PRODUCT of the kernel's logarithmic
slope and the separation exponent. They are jointly unidentifiable.
Fixing either one predicts the other; fixing neither predicts nothing.

s IS A SPAN-AVERAGED EFFECTIVE SLOPE, NOT A CONSTANT. For F = coth - c0,
-dln F/dln alpha varies across the window (the corpus measures that coth
over alpha in [0.3165, 0.8732] is within 0.97% of 1/alpha + alpha/3, i.e.
the curvature term is resolved). Every s below is therefore the OLS slope
of ln kappa on ln alpha over the 29 pairs -- the effective slope the data
sees -- and the identity above holds in that averaged sense, not
pointwise. Stating it pointwise would confuse a family with a
proposition.

Three consequences, each measured below:

  (1) Freeing p, the O2-ADMISSIBLE kernel c0 = 1 fits at least as well
      as the inadmissible incumbent c0 = 0, and every member of the scan
      lands within noise of a bare two-parameter power law. Round 6's
      numerical case against neutralisation is an artifact of the pin.

  (2) The kernel choice PREDICTS the separation exponent. c0 = 0 predicts
      p = 0.329, which is 1/3 to within half a standard error -- that
      coincidence, of one number to ~1%, is the whole of H_coth's
      apparent success. c0 = 1 predicts p = 0.187.

  (3) The hyperbolic-ball separation law fails its two conditions by
      hundreds of percent at every c0 scanned -- a scope-(a) negative on a
      CONJUNCTION (one-term subtracted-coth kernel, and V ~ A), NOT a
      structural exclusion: no proved invariant is cited and both inputs
      are flagged as assumptions in the corpus. It is nonetheless a
      different and stronger test than round 6's finding 3, which scored the
      MULTIPLICATIVE alpha ~ c*ln A (free slope) at 9.253%. The law
      hyperbolic geometry actually forces is ADDITIVE -- from
      Vol(ball of radius R) = pi(sinh 2R - 2R) ~ (pi/2)e^{2R} with an
      extensive carrier volume V ~ A,

          alpha = (1/2) ln A + beta,

      whose SLOPE is fixed at 1/2 per ln A and whose only freedom is the
      additive beta. That is one free parameter, the same as every rival,
      but two conditions to meet (span and scale), so it is
      over-determined -- and it fails by hundreds of percent at every c0.

NOTHING IS FITTED TO A TARGET AND NOTHING IS WIRED. The scan is a
degeneracy measurement, not a hypothesis contest: its conclusion is that
this observable cannot rank the hypotheses, so no member is selected.
Per the anti-fit discipline, the exponents reported are OUTPUTS of a
chosen kernel, offered as prediction targets for a derived separation
law -- not identifications.

CARRIED FORWARD (bean qou-gcmn): the per-pair Coulomb unit is frozen at
its A = 3 value, so a strong-bond drift B_pp ~ A^(-delta) enters the
measured slope ADDITIVELY, s*p = 0.26050 - delta. That is sharper than
the audit's reading of this confound as a scatter nuisance: it biases the
one number the front measures, and Section F shows the systematic
dominates the statistical error for any plausible delta.

Series and kappa values are read from the committed
em-linking-mirror-series.witness.json; this probe re-scores the SAME
values and does not re-derive them.

EXPLORATORY / audit-only. mpmath, no float64 anywhere.
"""

from __future__ import annotations

import json
import pathlib

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

_UPSTREAM_RECORDS: list = []

from mpmath import mp, mpf, sqrt, log, acoth, coth  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
SERIES = HERE / "em-linking-mirror-series.witness.json"

set_compute_dps()

# Physically-unbound pairs, excluded upstream for a stated reason and
# carried over unchanged so the comparison is like-for-like.
UNBOUND_A = {5, 9}

# The admissible floor is c0 >= 1 (coth > 1 pointwise, so its average over
# any finite-volume M exceeds 1). c0 < 1 members are scanned only to locate
# the hyperbolic-ball crossing and are labelled inadmissible throughout.
C0_SCAN = ["-0.30", "-0.20", "-0.10", "0", "0.25", "0.50",
           "1", "1.5", "2", "3", "4", "7.5"]
C0_ADMISSIBLE_FLOOR = mpf(1)
THIRD = mpf(1) / 3


def ols(xs, ys):
    """Slope, intercept, and standard error of the slope."""
    n = mpf(len(xs))
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    m = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx
    b = my - m * mx
    resid = [y - (b + m * x) for x, y in zip(xs, ys)]
    s2 = sum(r ** 2 for r in resid) / (n - 2)
    return m, b, sqrt(s2 / sxx)


def contest_stat(vals):
    """The committed contest statistic: population sd / mean."""
    n = len(vals)
    m = sum(vals) / n
    return m, sqrt(sum((v - m) ** 2 for v in vals) / n) / m


def kappa_rms(pred, obs):
    """RMS relative residual in kappa-space, comparable across laws."""
    n = len(obs)
    return sqrt(sum(((p - k) / k) ** 2 for p, k in zip(pred, obs)) / n)


def golden_min(f, lo, hi, iters=200):
    gr = (sqrt(5) - 1) / 2
    lo, hi = mpf(lo), mpf(hi)
    for _ in range(iters):
        x1 = hi - gr * (hi - lo)
        x2 = lo + gr * (hi - lo)
        if f(x1) < f(x2):
            hi = x2
        else:
            lo = x1
    return (lo + hi) / 2


def main() -> None:
    set_compute_dps()

    w = record_upstream(SERIES, _UPSTREAM_RECORDS)
    rows = [{"A": int(r["A"]), "Z": int(r["Z"]),
             "kappa": mpf(str(r["kappa"]))} for r in w["data"]["series"]]
    bound = [r for r in rows if r["A"] not in UNBOUND_A]
    A = [mpf(r["A"]) for r in bound]
    K = [r["kappa"] for r in bound]
    lnA = [log(a) for a in A]
    lnK = [log(k) for k in K]
    committed = w["data"]["hypothesis_scores_bound_only"]

    wb = WitnessBuilder("em-linking-kernel-exponent-degeneracy",
                        engine="mpmath")

    # ---- A. end-to-end: reproduce the committed contest numbers --------
    c_coth, rel_coth = contest_stat([acoth(k) / a ** THIRD
                                     for a, k in zip(A, K)])
    c_fha, rel_fha = contest_stat([k * a ** THIRD for a, k in zip(A, K)])
    cm_coth = committed["H_coth: arccoth(kappa) / A^(1/3) const"]
    cm_fha = committed["H_FH_A: kappa * A^(1/3) const"]

    # ---- B. the one measured scalar ------------------------------------
    slope, _, slope_se = ols(lnA, lnK)
    measured = -slope                      # -dln(kappa)/dln(A)

    # A bare 2-parameter power law is the noise floor every 1-parameter
    # hypothesis on this series is competing against.
    pl_b, pl_lnC, _ = ols(lnA, lnK)
    pl_rms = kappa_rms([mp.e ** pl_lnC * a ** pl_b for a in A], K)

    # ---- C. the degeneracy scan ----------------------------------------
    scan = []
    for c0s in C0_SCAN:
        c0 = mpf(c0s)
        if min(K) + c0 <= 1:
            continue                       # arccoth undefined: law cannot reach
        al = [acoth(k + c0) for k in K]
        p, lnc, p_se = ols(lnA, [log(x) for x in al])
        s, _, _ = ols([log(x) for x in al], lnK)
        pred_free = [coth(mp.e ** lnc * a ** p) - c0 for a in A]
        c_pin = golden_min(
            lambda c: kappa_rms([coth(c * a ** THIRD) - c0 for a in A], K),
            "0.005", "2.0")
        pred_pin = [coth(c_pin * a ** THIRD) - c0 for a in A]
        scan.append({
            "c0": c0,
            "admissible_under_O2": bool(c0 >= C0_ADMISSIBLE_FLOOR),
            "p_predicted_by_this_kernel": p,
            "p_standard_error": p_se,
            "kernel_log_slope_s": -s,
            "product_s_times_p": -s * p,
            "kappa_rms_exponent_FREE": kappa_rms(pred_free, K),
            "kappa_rms_exponent_PINNED_at_one_third": kappa_rms(pred_pin, K),
        })
    # The claims below are about the population O2 and round 6 are about:
    # the inadmissible incumbent c0 = 0 and the admissible family c0 >= 1.
    # The three c0 < 0 members are bracket points, present only to locate
    # the hyperbolic-ball crossing in Section E, and are reported but not
    # asserted over -- they sit outside the family under discussion.
    main_scan = [r for r in scan if r["c0"] >= 0]
    bracket = [r for r in scan if r["c0"] < 0]
    # Self-consistency: the chain rule is exact POINTWISE, but the product of
    # two OLS slope ESTIMATES need not equal the OLS estimate of the direct
    # slope unless the intermediate fit is exact. Measure the gap rather than
    # leave a reader to wonder whether the identity is being over-claimed.
    for r in scan:
        r["product_vs_direct_slope_rel"] = (r["product_s_times_p"] - measured) / measured
    gaps = [r["product_vs_direct_slope_rel"] for r in main_scan]
    attenuation = max(abs(g) for g in gaps)
    attenuation_min = min(abs(g) for g in gaps)
    all_negative = all(g <= 0 for g in gaps)

    prods = [r["product_s_times_p"] for r in main_scan]
    prod_spread = (max(prods) - min(prods)) / (sum(prods) / len(prods))
    prods_all = [r["product_s_times_p"] for r in scan]
    prod_spread_all = ((max(prods_all) - min(prods_all))
                       / (sum(prods_all) / len(prods_all)))

    inc = next(r for r in scan if r["c0"] == 0)
    adm = next(r for r in scan if r["c0"] == 1)
    ratio_pinned = (adm["kappa_rms_exponent_PINNED_at_one_third"]
                    / inc["kappa_rms_exponent_PINNED_at_one_third"])
    ratio_free = (adm["kappa_rms_exponent_FREE"]
                  / inc["kappa_rms_exponent_FREE"])
    worst_free = max(r["kappa_rms_exponent_FREE"] for r in main_scan)
    worst_free_bracket = max(r["kappa_rms_exponent_FREE"] for r in bracket)

    # ---- E. the forced hyperbolic-ball law alpha = (1/2)ln A + beta -----
    # Slope is FIXED at 1 by the geometry; only beta is free. Measure the
    # slope the data delivers, and locate the c0 at which it would be 1.
    half_lnA = [x / 2 for x in lnA]
    ball = []
    for c0s in C0_SCAN:
        c0 = mpf(c0s)
        if min(K) + c0 <= 1:
            continue
        al = [acoth(k + c0) for k in K]
        m_ball, _, _ = ols(half_lnA, al)
        beta = sum(x - h for x, h in zip(al, half_lnA)) / len(al)
        ball.append({
            "c0": c0,
            "fitted_slope_geometry_forces_1": m_ball,
            "best_beta": beta,
            "kappa_rms": kappa_rms(
                [coth(h + beta) - c0 for h in half_lnA], K),
        })

    def ball_slope(c0):
        return ols(half_lnA, [acoth(k + c0) for k in K])[0] - 1

    # Bracket the root instead of starting from a hardcoded point: the
    # start -0.36 was tuned to the old typed per-pair unit and does not
    # converge once kappa is read from the derived unit (owner card
    # 2026-11-21, PER_PAIR_UNIT swap). The scan starts just above the
    # acoth domain edge c0 > 1 - min(K) and stops at the first sign change.
    _lo = 1 - min(K) + mpf("1e-6")
    _grid = [_lo + (mpf("8") - _lo) * i / 4000 for i in range(4001)]
    _vals = [ball_slope(c) for c in _grid]
    _br = next((a, b) for a, b, fa, fb in
               zip(_grid, _grid[1:], _vals, _vals[1:]) if fa * fb <= 0)
    crossing = mp.findroot(ball_slope, _br, solver="anderson")

    # ---- F. the qou-gcmn confound as an additive bias ------------------
    # The sign and low-A scale of the drift are read from the COMMITTED
    # merged probe, not assumed here. Used as a local scale only.
    bpp = record_upstream(HERE / "probes" / "bpp-higher-a-sparse.witness.json",
                          _UPSTREAM_RECORDS)
    _bd = bpp["data"]
    corr3 = mpf(str(_bd["kappa_correction_A3"]))
    corr4 = mpf(str(_bd["kappa_correction_A4"]))
    delta_local = log(corr4 / corr3) / log(mpf(4) / 3)
    delta_share = delta_local / measured

    s_inc = inc["kernel_log_slope_s"]
    p_inc_d0 = measured / s_inc
    p_inc_dl = (measured - delta_local) / s_inc
    sig_d0 = abs(THIRD - p_inc_d0) / inc["p_standard_error"]
    sig_dl = abs(THIRD - p_inc_dl) / inc["p_standard_error"]

    s_adm = adm["kernel_log_slope_s"]
    confound = [{"delta": mpf(d),
                 "s_times_p": measured - mpf(d),
                 "p_at_c0_1": (measured - mpf(d)) / s_adm}
                for d in ["0", "0.01", "0.02", "0.05", "0.10"]]
    p_shift_at_5pct = abs(confound[3]["p_at_c0_1"] - confound[0]["p_at_c0_1"])
    systematic_over_statistical = p_shift_at_5pct / adm["p_standard_error"]

    # ---- record ---------------------------------------------------------
    wb.add_data("measured_scalar", {
        "minus_dln_kappa_dln_A": measured,
        "standard_error": slope_se,
        "relative_standard_error": slope_se / measured,
        "n_bound_pairs": len(bound),
        "lever_arm_ln_Amax_over_Amin": log(max(A) / min(A)),
        "what_it_is": (
            "The ONLY quantity this series constrains. For any kernel F "
            "and separation law alpha ~ A^p, -dln(kappa)/dln(A) = s*p with "
            "s = -dln F/dln alpha. Kernel and exponent are jointly "
            "unidentifiable; fixing either predicts the other."),
    })
    wb.add_data("two_parameter_power_law_noise_floor", {
        "exponent": -pl_b, "kappa_rms": pl_rms,
        "why": ("Every 1-parameter hypothesis on this series is competing "
                "against this. Any hypothesis reaching it has explained "
                "nothing beyond the slope."),
    })
    wb.add_data("degeneracy_scan", scan)
    wb.add_data("ols_attenuation_check", {
        "max_relative_gap_over_c0_ge_0": attenuation,
        "min_relative_gap_over_c0_ge_0": attenuation_min,
        "every_gap_is_negative": all_negative,
        "direct_slope": measured,
        "why": ("dln(kappa)/dln(A) = s*p is exact pointwise (chain rule), but "
                "s and p are OLS slope ESTIMATES and their product need not "
                "equal the OLS estimate of the direct slope unless ln(alpha) "
                "on ln(A) fits exactly (it does not: R^2 ~ 0.973-0.978)."),
        "verdict": ("THE SPREAD IS THE ATTENUATION. Max gap "
                    "1.478% against a 1.484% spread of s*p across the family "
                    "-- the same size, every gap NEGATIVE, and monotone away "
                    "from c0 ~ 0.4 where it vanishes. That is the attenuation "
                    "signature, not variation in the product. Where the "
                    "estimator is clean (c0 = 0.5 and 0.25) s*p reproduces "
                    "the direct slope to 0.002% and 0.016%."),
        "consequence": ("The product is the SAME NUMBER for every kernel, to "
                        "better than the resolution of this decomposition. "
                        "The degeneracy is tighter than the raw spread "
                        "suggests, not looser -- so this check strengthens "
                        "the finding. An earlier version of this probe "
                        "asserted the gap was 'an order of magnitude below' "
                        "the spread; that was wrong, from a three-point spot "
                        "check that missed the large-c0 end, and this "
                        "assertion is what caught it."),
    })
    wb.add_data("product_spread_across_scan", {
        "relative_spread": prod_spread,
        "min": min(prods), "max": max(prods),
        "population": "c0 >= 0 (incumbent + admissible family)",
        "relative_spread_including_c0_negative_bracket": prod_spread_all,
        "why": ("s*p is near-constant across a 25-fold range of c0 while "
                "p itself moves by a factor of 6. That is the degeneracy, "
                "measured."),
    })
    wb.add_data("round_six_reversal", {
        "ratio_admissible_over_incumbent_PINNED": ratio_pinned,
        "ratio_admissible_over_incumbent_FREE": ratio_free,
        "reading": ("Pinned at the imported Euclidean p = 1/3 the admissible "
                    "kernel looks far worse; with its own exponent it does "
                    "not. Round 6's structural exclusion of the unsubtracted "
                    "kernel stands; its numerical case against the "
                    "admissible family does not survive freeing the pin."),
    })
    wb.add_data("hyperbolic_ball_law_additive", ball)
    wb.add_data("hyperbolic_ball_law_crossing", {
        "c0_where_forced_slope_equals_1": crossing,
        "admissible_floor": C0_ADMISSIBLE_FLOOR,
        "reading": ("O2 neutrality pushes c0 >= 1; hyperbolic-ball "
                    "extensivity pulls it negative. The two geometric "
                    "constraints on the same object point in opposite "
                    "directions and cannot both hold."),
    })
    wb.add_data("gcmn_confound_as_additive_bias", confound)
    wb.add_data("measured_bpp_drift_destroys_the_one_third_coincidence", {
        "delta_local_A3_to_A4": delta_local,
        "share_of_the_measured_slope": delta_share,
        "p_at_c0_zero_delta_zero": p_inc_d0,
        "sigma_from_one_third_delta_zero": sig_d0,
        "p_at_c0_zero_delta_local": p_inc_dl,
        "sigma_from_one_third_delta_local": sig_dl,
        "provenance": ("Drift read from the committed corrections of "
                       "probes/bpp_higher_a_sparse_probe.py (merged "
                       "2026-08-31, PR #6336), which established that B_pp "
                       "DECLINES with A. This probe does not re-derive that; "
                       "it quantifies what it does to the slope."),
        "not_extrapolated": ("That probe refuses to carry a three-point "
                             "decline across a factor of ten in A, and the "
                             "refusal is honoured: delta_local is used to "
                             "show the confound is OF ORDER the signal, "
                             "never as a value for delta over A = 3..63. No "
                             "number here is corrected by it."),
        "reading": ("0.26050 is an UPPER BOUND on s*p, so every exponent "
                    "reported here is an upper bound. H_coth's single "
                    "coincidence -- c0 = 0 predicting 1/3 -- holds only at "
                    "delta = 0, and the corpus has measured that delta > 0."),
    })

    # ---- assertions -----------------------------------------------------
    wb.add_assertion(
        name="reproduces_committed_H_coth_bound_only",
        computed=mp.nstr(abs(rel_coth - mpf(str(cm_coth["rel_scatter"]))), 8),
        expected="0", tolerance="1e-8", unit="absolute deviation",
        source=(f"End-to-end: this probe's re-scoring of the incumbent under "
                f"the COMMITTED statistic gives const "
                f"{mp.nstr(c_coth, 9)} / scatter {mp.nstr(rel_coth, 9)} "
                f"against committed {cm_coth['constant']} / "
                f"{cm_coth['rel_scatter']}. If this fails, nothing below is "
                f"comparable to the published contest."))
    wb.add_assertion(
        name="reproduces_committed_H_FH_A_bound_only",
        computed=mp.nstr(abs(rel_fha - mpf(str(cm_fha["rel_scatter"]))), 8),
        expected="0", tolerance="1e-8", unit="absolute deviation",
        source=(f"Second end-to-end anchor, on a different hypothesis: "
                f"const {mp.nstr(c_fha, 9)} / scatter {mp.nstr(rel_fha, 9)} "
                f"against committed {cm_fha['constant']} / "
                f"{cm_fha['rel_scatter']}."))
    wb.add_assertion(
        name="product_s_times_p_is_constant_across_the_c0_scan",
        computed=mp.nstr(prod_spread, 6), expected="0", tolerance="0.03",
        unit="relative spread",
        source=(f"s*p spans {mp.nstr(min(prods), 6)}..{mp.nstr(max(prods), 6)} "
                f"across c0 = 0..{C0_SCAN[-1]}, a relative spread "
                f"of {mp.nstr(prod_spread * 100, 4)}%, while p itself moves "
                f"from {mp.nstr(main_scan[0]['p_predicted_by_this_kernel'], 5)} "
                f"to {mp.nstr(main_scan[-1]['p_predicted_by_this_kernel'], 5)}. "
                f"The product is what is measured; neither factor separately "
                f"is. Including the three c0 < 0 bracket points the spread is "
                f"{mp.nstr(prod_spread_all * 100, 4)}%."))
    wb.add_assertion(
        name="the_sp_spread_is_ols_attenuation_not_variation",
        computed=1 if (all_negative and attenuation_min < mpf("0.0005")) else 0,
        expected=1, tolerance=0, unit="boolean",
        source=(f"The chain rule is exact pointwise, but s and p are OLS "
                f"estimates whose product attenuates when ln(alpha) on ln(A) "
                f"does not fit exactly. Two signatures establish that the "
                f"measured spread IS that attenuation rather than genuine "
                f"variation in the product: EVERY gap over c0 >= 0 is "
                f"negative (attenuation only ever underestimates), and the "
                f"smallest is {mp.nstr(attenuation_min * 100, 3)}% -- i.e. "
                f"where the estimator is clean, s*p reproduces the direct "
                f"slope {mp.nstr(measured, 8)} essentially exactly. The "
                f"largest is {mp.nstr(attenuation * 100, 4)}% against a "
                f"{mp.nstr(prod_spread * 100, 4)}% spread: the same size. So "
                f"the product is the same number for every kernel to better "
                f"than this decomposition can resolve, and the degeneracy is "
                f"TIGHTER than the raw spread suggests."))
    wb.add_assertion(
        name="admissible_kernel_not_worse_once_the_exponent_is_freed",
        computed=1 if ratio_free <= mpf("1.05") else 0,
        expected=1, tolerance=0, unit="boolean",
        source=(f"With each kernel at its own exponent, c0 = 1 gives "
                f"{mp.nstr(adm['kappa_rms_exponent_FREE'] * 100, 4)}% against "
                f"c0 = 0 at "
                f"{mp.nstr(inc['kappa_rms_exponent_FREE'] * 100, 4)}%, ratio "
                f"{mp.nstr(ratio_free, 5)}. The O2-admissible kernel is not "
                f"disfavoured by this series."))
    wb.add_assertion(
        name="round_six_gap_is_an_artifact_of_the_pinned_exponent",
        computed=1 if (ratio_pinned > 4 and ratio_free < mpf("1.05")) else 0,
        expected=1, tolerance=0, unit="boolean",
        source=(f"Pinned at p = 1/3 the admissible/incumbent rms ratio is "
                f"{mp.nstr(ratio_pinned, 5)}; freed it is "
                f"{mp.nstr(ratio_free, 5)}. The penalty round 6 reports is "
                f"carried entirely by the pin, which its own third finding "
                f"identifies as imported Euclidean phenomenology."))
    wb.add_assertion(
        name="every_scanned_kernel_lands_within_noise_of_a_power_law",
        computed=mp.nstr(worst_free / pl_rms, 6), expected="1",
        tolerance="0.35", unit="ratio to the 2-parameter power-law floor",
        source=(f"Over the incumbent + admissible family (c0 >= 0) the worst "
                f"free-exponent member is {mp.nstr(worst_free * 100, 4)}% "
                f"against the bare 2-parameter power law's "
                f"{mp.nstr(pl_rms * 100, 4)}%. No member is resolved from a "
                f"straight line in log-log, so the series cannot rank them. "
                f"NARROWED POPULATION, stated so the narrowing is visible: "
                f"the three c0 < 0 bracket points reach "
                f"{mp.nstr(worst_free_bracket * 100, 4)}% and would fail this "
                f"tolerance. They are anti-neutralised, lie outside the family "
                f"O2 and round 6 concern, and are scanned only to locate the "
                f"Section E crossing -- their values are in degeneracy_scan."))
    wb.add_assertion(
        name="hyperbolic_ball_law_needs_an_anti_neutralised_kernel",
        computed=1 if crossing < 0 else 0, expected=1, tolerance=0,
        unit="boolean",
        source=(f"alpha = (1/2)ln A + beta has its slope FIXED at 1 by "
                f"hyperbolic ball volume with V ~ A. The data delivers that "
                f"slope only at c0 = {mp.nstr(crossing, 6)}, which is "
                f"negative -- MORE positive than the unsubtracted kernel, so "
                f"further from admissible than the incumbent. O2 requires "
                f"c0 >= 1. The two geometric constraints are incompatible by "
                f"{mp.nstr(C0_ADMISSIBLE_FLOOR - crossing, 5)} in c0."))
    wb.add_assertion(
        name="gcmn_systematic_dominates_the_statistical_error",
        computed=1 if systematic_over_statistical > 1 else 0,
        expected=1, tolerance=0, unit="boolean",
        source=(f"A strong-bond drift of only delta = 0.05 moves the "
                f"admissible kernel's predicted exponent by "
                f"{mp.nstr(p_shift_at_5pct, 5)}, which is "
                f"{mp.nstr(systematic_over_statistical, 4)} times its 1-sigma "
                f"statistical error {mp.nstr(adm['p_standard_error'], 4)}. "
                f"The frozen B_pp unit (qou-gcmn) enters the measured slope "
                f"additively, not as a scatter nuisance."))

    wb.add_assertion(
        name="one_third_coincidence_requires_zero_bpp_drift",
        computed=1 if (sig_d0 < 1 and sig_dl > 5) else 0,
        expected=1, tolerance=0, unit="boolean",
        source=(f"At delta = 0 the incumbent kernel predicts p = "
                f"{mp.nstr(p_inc_d0, 6)}, which is 1/3 to "
                f"{mp.nstr(sig_d0, 3)} sigma -- the whole of H_coth's "
                f"apparent success. At the measured LOCAL drift "
                f"delta = {mp.nstr(delta_local, 6)} (from the committed "
                f"corrections of probes/bpp_higher_a_sparse_probe.py, which "
                f"established B_pp DECLINES with A) the same prediction is "
                f"p = {mp.nstr(p_inc_dl, 6)}, {mp.nstr(sig_dl, 4)} sigma "
                f"from 1/3. The drift is {mp.nstr(delta_share * 100, 4)}% of "
                f"the entire measured slope, so 0.26050 is an upper bound on "
                f"s*p rather than a measurement of it."))

    wb.add_data("scope", {
        "b_structural_exclusion_UNTOUCHED": (
            "Round 6's O2 exclusion of the unsubtracted kernel coth(alpha) "
            "is a structural argument from int(Laplacian u) = 0 with no data "
            "in it. Nothing here bears on it and it stands."),
        "a_scope_limited_negative_ON_A_TEST": (
            "The kappa(A) mirror series, with the per-pair Coulomb unit "
            "frozen at A = 3, cannot rank kernels: it constrains one scalar "
            "against at least three unknowns (kernel log-slope, separation "
            "exponent, strong-bond drift; qou-u3vw adds flux scaling as a "
            "fourth). This is a statement about what the measurement can "
            "resolve, not about any hypothesis being true or false."),
        "a_scope_limited_negative_ON_THE_BALL_LAW": (
            "The additive hyperbolic-ball law fails its two conditions by "
            "hundreds of percent at every kernel in the scanned family. This "
            "is scope (a), NOT a structural exclusion: no proved invariant is "
            "cited, and BOTH inputs are assumptions the corpus already flags "
            "-- V ~ A ('itself an assumption. The corpus cannot check it', "
            "em_linking_alpha_scaling_provenance_probe.py) and the one-term "
            "subtracted coth ('a model ... not the exact Green's function of "
            "a quotient', round 6). What fails is the CONJUNCTION."),
        "prior_art_on_the_confound": (
            "The B_pp drift is NOT discovered here. Its sign and low-A scale "
            "are established by probes/bpp_higher_a_sparse_probe.py (merged "
            "2026-08-31, PR #6336) and sharpened by qou-23dn. What is new is "
            "the log-slope form s*p + delta = -dln(kappa)/dln(A), the "
            "observation that the drift is 80% of the measured slope, and "
            "the consequence for the 1/3 coincidence."),
        "NOT_claimed": (
            "That any kernel is correct. That p = 0.187 is the separation "
            "exponent -- it is an OUTPUT of choosing c0 = 1, offered as a "
            "prediction target for a derived law, not an identification. "
            "That the metric Coulomb route fails: it is untouched, exactly "
            "as rounds 3 and 6 left it."),
        "not_a_fit": (
            "No parameter is tuned to improve agreement with a target. The "
            "exponents are regression outputs used to demonstrate a "
            "degeneracy, and the conclusion drawn from them is that the "
            "observable cannot select -- so no hypothesis is promoted."),
    })
    wb.add_data("what_would_close_this", {
        "statement": (
            "Derive any TWO of {kernel log-slope s, separation exponent p, "
            "strong-bond drift delta} and the third is predicted by "
            "s*p + delta = " + mp.nstr(measured, 7) + ". Scoring further "
            "kernels against kappa(A) cannot help: the observable has one "
            "degree of freedom and they compete for it."),
        "cheapest_leg": (
            "delta (bean qou-gcmn) -- a compute question about B_pp at higher "
            "A, not a geometry question, already answered in sign and low-A "
            "scale by PR #6336. Section F shows it is ~80% of the measured "
            "slope, so extending it to A = 5, 6 (that probe's own named next "
            "step) would do more for this front than any further kernel."),
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

    print(f"bound mirror pairs: {len(bound)}  "
          f"(A = {min(int(a) for a in A)}..{max(int(a) for a in A)})\n")
    print(f"THE MEASURED SCALAR  -dln(kappa)/dln(A) = "
          f"{mp.nstr(measured, 7)} +/- {mp.nstr(slope_se, 3)} "
          f"({mp.nstr(slope_se / measured * 100, 3)}%)")
    print(f"2-param power-law noise floor: "
          f"{mp.nstr(pl_rms * 100, 4)}% kappa-rms\n")
    print(f"{'c0':>7} {'adm':>4} {'p_pred':>9} {'s':>8} {'s*p':>8} "
          f"{'rms free':>9} {'rms p=1/3':>10}")
    for r in scan:
        print(f"{mp.nstr(r['c0'], 4):>7} "
              f"{'yes' if r['admissible_under_O2'] else 'no':>4} "
              f"{mp.nstr(r['p_predicted_by_this_kernel'], 5):>9} "
              f"{mp.nstr(r['kernel_log_slope_s'], 4):>8} "
              f"{mp.nstr(r['product_s_times_p'], 5):>8} "
              f"{mp.nstr(r['kappa_rms_exponent_FREE'] * 100, 4):>8}% "
              f"{mp.nstr(r['kappa_rms_exponent_PINNED_at_one_third'] * 100, 4):>9}%")
    print(f"\ns*p spread across the scan: "
          f"{mp.nstr(prod_spread * 100, 4)}%  <- the degeneracy")
    print(f"round-6 ratio (adm/inc): pinned {mp.nstr(ratio_pinned, 5)}  ->  "
          f"freed {mp.nstr(ratio_free, 5)}")
    print(f"\nhyperbolic-ball law slope==1 at c0 = {mp.nstr(crossing, 6)} "
          f"(O2 needs c0 >= 1)")
    for b in ball:
        if b["c0"] in (mpf(0), mpf(1)):
            print(f"  c0={mp.nstr(b['c0'], 3)}: forced slope delivered "
                  f"{mp.nstr(b['fitted_slope_geometry_forces_1'], 5)} "
                  f"(need 1)   kappa-rms "
                  f"{mp.nstr(b['kappa_rms'] * 100, 5)}%")
    print(f"\nwitness -> {out}")


if __name__ == "__main__":
    main()
