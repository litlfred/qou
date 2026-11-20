#!/usr/bin/env python3
"""Measure the CAL-2-proxy (Q_beta) dataset delta: AME-2020 vs the CODATA-2022
registry — and what it moves downstream.

WHAT THIS IS
------------
`codata_constants.Q_BETA_MEV` is the free-neutron beta-decay Q-value that the
framework uses as the numerical proxy for CAL-2 (the decay width `D_beta`; see
AGENTS.md "Canonical derivation chain", where `Q_beta = hbar / D_beta` is the
CAL-2 proxy — NOT CAL-3, which is the pion width `D_pi` with proxy `m_pi`).
Two experimental determinations of that one quantity live in the corpus:

  AME-2020 direct            Q_BETA_MEV_AME                     = 0.78233341(61)
  CODATA-2022 registry       (m_n - m_p) - m_e                  = 0.78233355931(38)

They differ by ~191 ppb, i.e. 0.2 sigma — statistically indistinguishable.
The choice between them is therefore NOT an accuracy question and MUST NOT be
made on which produces a better residual (AGENTS.md "NO FITTING, EXCEPT
CAL-1/2/3": selection against the target is a fit even with no tuned
parameter, and a more accurate route ranks BELOW a more cleanly derived one).
It is a DATASET-CONSISTENCY question, which is the reason the owner gave when
ruling the muon pin to CODATA 2022 on 2026-08-22: CAL-1, CAL-2 and CAL-3 must
come from one experimental dataset.

This probe MEASURES the delta and its downstream consequences so that decision
can be made on evidence. It changes no default, writes no calibration, and
wires nothing.

WHAT IT MEASURES
----------------
  1. The two determinations, their separation in ppb and in combined sigma.
  2. That the registry value is route-independent: `Delta_np - m_e` and
     `m_n(direct) - m_p - m_e` agree exactly, so the registry number does not
     depend on the proton entry (which the 2026-08-09 vintage-straddle audit
     found to be the stale member of the vendored snapshot).
  3. The `c_k` ladder (k = 3..7) extracted under EACH determination, so the
     downstream move is a measured table rather than a propagated estimate.
     `c_3` is amplified by `1/u^3` with `u = b*hbar_q^2 ~ 0.00852`, so a 191 ppb
     input move is a percent-level output move.
  4. The L2 dashboard `Q_beta` row under each, under BOTH normalisations --
     a fixed (AME) sigma, which isolates the residual, and each
     determination's own sigma, which is what `per_observable_100x_status.py`
     reports and is authoritative. They DISAGREE IN SIGN; see the note in
     section 4 of the body. Reporting only the first is how this probe got
     the direction backwards on its first run.

CONVENTION SCOPE (load-bearing)
-------------------------------
The `c_k` ladder is CONVENTION-C-frame. Convention D is canonical (owner
ruling 2026-08-15) and the canonical producer `qbeta_ck_cache.py` REFUSES to
run under D because the ladder eigenphase `alpha = (z-1)h/2` is C-derived and
substituting `z_D` is proved invalid (`QOU.QBeta.decayLadder_zC_threeRow_ne_zero`,
`QOU.QBeta.eigenphase_bar_defect_of_fullBar`, both sorry-free). The ladder
awaits re-derivation under D (bean `qou-cds1`).

So every `c_k` number below is reproduced in the SAME historical C frame the
committed cache uses, and is labelled C-conditional. The probe's claim is a
DIFFERENCE between two datasets computed in one fixed frame; it is not a claim
that either `c_k` value is canonical. Both columns are equally C-conditional,
so the delta between them is the meaningful output.

PRECISION
---------
mpmath end to end at the corpus compute precision; `float()` appears only
inside f-strings for display (AGENTS.md "PROBES ARE NOT EXEMPT").

-- Ref: [leitner2026] beans qou-0e2p, qou-cds1, qou-99qc; PRs #7164, #7118;
   docs/audits/2026-08-09-codata-registry-vintage-straddle.md
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

del _sys, _bridge

import sys  # noqa: E402
from pathlib import Path  # noqa: E402

from mpmath import mp, mpf, cos, sqrt  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
import codata_2022_source as C22  # noqa: E402


def ladder(q, me, Q_anchor):
    """Extract c_3..c_7 in the historical convention-C frame.

    Mirrors `qbeta_ck_cache.py`'s extraction exactly (same `Q_A`, same
    Kashiwara `cos` N=1 factor, same Lean-proved `c_2 = -1`, same greedy
    recursion `c_k = (Q_anchor/Q_prev - 1)/u^k`), with the anchor as a
    parameter so the two datasets can be run through one code path.
    """
    h = q - 1 / q
    hbar_q = (q - 1) / q
    b = sqrt((h ** 2 + 3) / (h ** 2 + 4))
    u = b * hbar_q ** 2

    # convention C, historical frame only (see module docstring)
    z = sqrt(q) / (1 + q)
    alpha = (z - 1) * h / 2

    Q_A = me * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
    Q_N1 = Q_A * cos(alpha - b * hbar_q ** 2 / 2)
    Q_N2 = Q_N1 * (1 + mpf(-1) * u ** 2)

    out = {"u": u, "Q_A": Q_A, "Q_N1": Q_N1, "Q_N2": Q_N2, "c": {}}
    Q_prev = Q_N2
    for k in range(3, 8):
        c_k = (Q_anchor / Q_prev - 1) / u ** k
        out["c"][k] = c_k
        Q_prev = Q_prev * (1 + c_k * u ** k)
    out["Q_final"] = Q_prev
    return out


def main() -> int:
    set_compute_dps()
    wb = WitnessBuilder("qbeta-cal2-proxy-dataset-delta", engine="mpmath")

    q = mpf(Q_50_DIGIT_STR)
    me = mpf(str(M_E_MEV))

    ame = mpf(str(C22.Q_BETA_MEV_AME))
    ame_err = mpf(str(C22.Q_BETA_MEV_AME_ERR))
    reg = mpf(str(C22.Q_BETA_MEV_DERIVED_FROM_CODATA_DIRECT))
    # route 2: the registry's own neutron-proton difference, minus m_e
    reg_via_dnp = mpf(str(C22.M_N_MINUS_P_MEV)) - mpf(str(C22.M_E_MEV))
    reg_err = mpf(str(C22.M_N_MINUS_P_MEV_ERR)) if hasattr(
        C22, "M_N_MINUS_P_MEV_ERR") else mpf("0.00000038")

    checks = []

    print("=" * 74)
    print(" CAL-2 proxy (Q_beta) dataset delta: AME-2020 vs CODATA-2022 registry")
    print("=" * 74)
    print()
    print("  NOTE ON LABELLING: Q_beta is the CAL-2 proxy (Q_beta = hbar/D_beta),")
    print("  not CAL-3.  CAL-3 is the pion width D_pi with proxy m_pi.  The")
    print("  producer `build_cal_3_q_beta_witness.py` and bean qou-0e2p both say")
    print("  'CAL-3'; that is a mislabel against AGENTS.md's canonical table.")
    print()

    # ---- 1. the two determinations -------------------------------------
    d_abs = reg - ame
    d_ppb = d_abs / ame * mpf(10) ** 9
    sigma_comb = sqrt(ame_err ** 2 + reg_err ** 2)
    d_sigma = d_abs / sigma_comb

    print("  AME-2020 direct      Q_beta = %s  +/- %s" % (
        mp.nstr(ame, 12), mp.nstr(ame_err, 3)))
    print("  CODATA-2022 registry Q_beta = %s  +/- %s" % (
        mp.nstr(reg, 12), mp.nstr(reg_err, 3)))
    print("  separation                  = %+0.4f ppb   = %+0.3f sigma (combined)"
          % (float(d_ppb), float(d_sigma)))
    print()

    # ---- 2. route independence of the registry value -------------------
    route_gap = abs(reg - reg_via_dnp)
    print("  route check: (m_n_direct - m_p - m_e) vs (Delta_np - m_e)")
    print("    route A = %s" % mp.nstr(reg, 20))
    print("    route B = %s" % mp.nstr(reg_via_dnp, 20))
    print("    |gap|   = %s" % mp.nstr(route_gap, 5))
    routes_agree = route_gap < mpf(10) ** (-12)
    checks.append(("registry value is route-independent "
                   "(does not inherit the stale proton)", routes_agree))
    print()

    checks.append(("the two determinations agree within 1 sigma "
                   "(this is NOT an accuracy choice)", abs(d_sigma) < 1))

    # ---- 3. the ladder under each --------------------------------------
    L_ame = ladder(q, me, ame)
    L_reg = ladder(q, me, reg)
    u = L_ame["u"]

    print("  ladder (CONVENTION C, historical frame -- see docstring), proton pin")
    print("  u = b*hbar_q^2 = %s" % mp.nstr(u, 10))
    print()
    print("   k |        c_k (AME) |   c_k (registry) |      delta |   delta %")
    print("  ---+------------------+------------------+------------+---------")
    ck_rows = []
    for k in range(3, 8):
        a = L_ame["c"][k]
        r = L_reg["c"][k]
        dk = r - a
        pct = dk / a * 100 if a != 0 else mpf(0)
        print("  %2d | %16s | %16s | %+10.4f | %+7.2f%%" % (
            k, mp.nstr(a, 11), mp.nstr(r, 11), float(dk), float(pct)))
        ck_rows.append({
            "k": k,
            "c_k_ame": mp.nstr(a, 30),
            "c_k_registry": mp.nstr(r, 30),
            "delta": mp.nstr(dk, 20),
            "delta_pct": fmt(pct),
        })
    print()

    # The k >= 4 rungs come out identically ZERO under BOTH datasets.  That is
    # not a coincidence of this probe, it is `QOU.QBeta.greedy_rung_exact` /
    # `greedy_later_rungs_vanish` (sorry-free) showing through: the greedy
    # recursion sets `Q_next = Q_prev*(1 + (Q_anchor/Q_prev - 1)) = Q_anchor`
    # identically, so the residual at rung 4 is exactly 0 and every later rung
    # inherits it.  Reported explicitly because it bounds the blast radius:
    # the ladder has exactly ONE extracted rung, so `c_3` is the whole of the
    # downstream move and there is no compounding through k = 4..7.
    later_all_zero = all(L_ame["c"][k] == 0 and L_reg["c"][k] == 0
                         for k in range(4, 8))
    checks.append(("only ONE rung is extracted: c_4..c_7 vanish identically "
                   "under both datasets (greedy_rung_exact)", later_all_zero))

    # c_3 is the headline: the 1/u^3 amplification
    c3_a, c3_r = L_ame["c"][3], L_reg["c"][3]
    amp_predicted = d_ppb * mpf(10) ** -9 / u ** 3
    amp_measured = c3_r - c3_a
    print("  c_3 amplification check:  (dQ/Q)/u^3 = %+0.6f   measured dc_3 = %+0.6f"
          % (float(amp_predicted), float(amp_measured)))
    # the greedy recursion makes this exact to first order only; 2% band
    rel = abs((amp_measured - amp_predicted) / amp_predicted)
    checks.append(("dc_3 is the 1/u^3 amplification of the input move",
                   rel < mpf("0.02")))

    # the near-match c_3 ~ -2 = J_Hopf(q=1), reported under both
    for lab, c3 in (("AME", c3_a), ("registry", c3_r)):
        gap = abs(mpf(-2) - c3) / 2 * 100
        print("    c_3(%-8s) = %s   |-2 - c_3|/2 = %6.4f %%"
              % (lab, mp.nstr(c3, 12), float(gap)))
    print()

    # ---- 4. L2 dashboard Q_beta row ------------------------------------
    # The dashboard scores the framework's PREDICTED Q_beta against the
    # experimental target.  Under the greedy ladder the prediction is
    # re-anchored to whichever target it was extracted from, so the honest
    # comparison of the two datasets at dashboard level is the N=2
    # (derived-tier, c_2 = -1, ladder-free) prediction, which is the only
    # rung that does NOT consume the anchor.
    QN2 = L_ame["Q_N2"]  # identical in both: independent of the anchor
    checks.append(("derived-tier Q_N2 is anchor-independent",
                   L_ame["Q_N2"] == L_reg["Q_N2"]))
    err_a = (QN2 - ame) / ame * mpf(10) ** 9
    err_r = (QN2 - reg) / reg * mpf(10) ** 9

    # TWO different targets, and conflating them inverts the conclusion.
    #
    # (i) FIXED-sigma: hold the 100x target at the AME sigma for both. This
    #     isolates the effect of the RESIDUAL alone, and it is NOT what the
    #     dashboard reports.
    # (ii) EACH-sigma: each determination is scored against 1/100 of ITS OWN
    #     experimental sigma. This is what `per_observable_100x_status.py`
    #     computes and is the authoritative L2 metric.
    #
    # They disagree in DIRECTION, because the registry value is the more
    # precise determination (sigma 3.8e-7 vs AME's 6.1e-7), so switching to
    # it tightens its own target by ~1.6x -- faster than the residual
    # improves. Under (i) the miss looks better; under (ii), the real one, it
    # gets WORSE. Reporting only (i) is how this probe first got it backwards.
    target_fixed = ame_err / ame * mpf(10) ** 9 / 100
    target_ame = ame_err / ame * mpf(10) ** 9 / 100
    target_reg = reg_err / reg * mpf(10) ** 9 / 100

    print("  L2 dashboard, derived-tier (N=2) Q_beta prediction vs each target")
    print("    Q_N2                = %s MeV  (anchor-independent)" % mp.nstr(QN2, 14))
    print("    residual vs AME      = %+12.2f ppb" % float(err_a))
    print("    residual vs registry = %+12.2f ppb" % float(err_r))
    print("    residual change      = %+12.2f ppb  (%s)"
          % (float(err_r - err_a),
             "further" if abs(err_r) > abs(err_a) else "closer"))
    print()
    print("    (i) FIXED-sigma target %0.4f ppb -- isolates the residual"
          % float(target_fixed))
    print("        only, and is NOT the dashboard metric:")
    print("          miss vs AME      = %8.1fx" % float(abs(err_a) / target_fixed))
    print("          miss vs registry = %8.1fx" % float(abs(err_r) / target_fixed))
    print()
    print("    (ii) EACH-sigma -- what per_observable_100x_status.py reports,")
    print("         and the authoritative L2 metric:")
    print("          AME      target %0.4f ppb -> miss %8.1fx"
          % (float(target_ame), float(abs(err_a) / target_ame)))
    print("          registry target %0.4f ppb -> miss %8.1fx"
          % (float(target_reg), float(abs(err_r) / target_reg)))
    print("          => the registry is the MORE PRECISE determination, so its")
    print("             own 100x target tightens faster than the residual")
    print("             improves, and the Q_beta miss gets WORSE.")
    print()
    print("    NOTE: whichever direction this moves is an OUTCOME, not a reason.")
    print("    Ranking the two datasets by either number would be a fit")
    print("    (AGENTS.md: accuracy is a diagnostic, never a tie-breaker). The")
    print("    point of reporting both is that the sign is not even stable")
    print("    across two defensible normalisations -- which is precisely why")
    print("    it must not be the basis of the decision.")
    print()
    # keep the old name pointing at the fixed-sigma convention it always meant
    target_ppb = target_fixed

    # ---- witness --------------------------------------------------------
    wb.set_description(
        "Measures the CAL-2-proxy (Q_beta) dataset delta between the AME-2020 "
        "direct value 0.78233341(61) and the CODATA-2022 registry value "
        "(m_n - m_p) - m_e = 0.78233355931(38), and the downstream move it "
        "produces in the convention-C c_k ladder and the L2 derived-tier "
        "Q_beta residual. Audit-only: changes no default, wires nothing. The "
        "two determinations agree to 0.2 sigma, so this is a dataset-"
        "consistency question (one experimental dataset across CAL-1/2/3, "
        "per the 2026-08-22 muon ruling), NOT an accuracy question; the "
        "residual direction is reported as an outcome and must not be used "
        "to rank the routes."
    )
    wb.set_audit_only("docs/audits/2026-09-12-qbeta-cal2-proxy-dataset-delta.md")
    wb.add_parameter("convention", "C (historical ladder frame; D has no "
                                   "derived ladder -- bean qou-cds1)")
    wb.add_parameter("q0_anchor", "proton (experimental pin, AGENTS.md 2026-08-07)")
    wb.add_parameter("q0", Q_50_DIGIT_STR)
    wb.add_data("Q_beta_ame_MeV", mp.nstr(ame, 30))
    wb.add_data("Q_beta_ame_err_MeV", mp.nstr(ame_err, 10))
    wb.add_data("Q_beta_registry_MeV", mp.nstr(reg, 30))
    wb.add_data("Q_beta_registry_err_MeV", mp.nstr(reg_err, 10))
    wb.add_data("separation_ppb", fmt(d_ppb))
    wb.add_data("separation_sigma", fmt(d_sigma))
    wb.add_data("registry_route_gap", mp.nstr(route_gap, 5))
    wb.add_data("u", mp.nstr(u, 30))
    wb.add_data("ck_rows", ck_rows)
    wb.add_data("QN2_derived_tier_MeV", mp.nstr(QN2, 30))
    wb.add_data("QN2_residual_vs_ame_ppb", fmt(err_a))
    wb.add_data("QN2_residual_vs_registry_ppb", fmt(err_r))
    # (i) fixed-sigma -- isolates the residual; NOT the dashboard metric
    wb.add_data("L2_target_fixed_sigma_ppb", fmt(target_fixed))
    wb.add_data("L2_miss_vs_ame_fixed_sigma", fmt(abs(err_a) / target_fixed))
    wb.add_data("L2_miss_vs_registry_fixed_sigma", fmt(abs(err_r) / target_fixed))
    # (ii) each-sigma -- the authoritative L2 metric
    wb.add_data("L2_target_ame_ppb", fmt(target_ame))
    wb.add_data("L2_target_registry_ppb", fmt(target_reg))
    wb.add_data("L2_miss_vs_ame", fmt(abs(err_a) / target_ame))
    wb.add_data("L2_miss_vs_registry", fmt(abs(err_r) / target_reg))
    wb.add_data(
        "L2_direction_note",
        "The two normalisations DISAGREE IN SIGN. Under a fixed (AME) sigma "
        "the miss improves; under each determination's own sigma -- which is "
        "what per_observable_100x_status.py reports and is authoritative -- "
        "it gets WORSE, because the registry is the more precise "
        "determination and its own 100x target tightens ~1.6x, faster than "
        "the residual improves. Measured on the dashboard: Q_beta miss "
        "164.0x -> 223.9x. Neither number is a reason to choose a dataset.",
    )

    ok = True
    print("  checks")
    for label, passed in checks:
        print("    [%s] %s" % ("PASS" if passed else "FAIL", label))
        wb.add_assertion(label, computed="1" if passed else "0",
                         expected="1", tolerance="0.5")
        ok = ok and bool(passed)

    out = wb.save()
    print()
    print("Witness: %s" % out)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
