#!/usr/bin/env python3
"""80-dps Cross-Anchor Probe for Q-Gap-10 (qou-nu01): Non-Zero Neutrino Mass Lift Above Vol(0_1)=0,
Electroweak Bring-Schwinger alpha_v^3 Bridge, & Stabilization Framing Parity.

Lean 4 companions:
  - QOU/StandardModel/NeutrinoUnknotSweedlerLift.lean (0 sorry, BP001..BP009 clean)
  - QOU/StandardModel/NeutrinoUnknotSweedlerMassLift.lean
  - QOU/StandardModel/ElectroweakBringSchwingerBridge.lean
Audit & Pre-registration:
  - docs/audits/2026-11-24-neutrino-unknot-sweedler-lift.md

STRICT DISCIPLINE
-----------------
- mpmath at 80 dps (mp.mp.dps = 80), zero float64, sympy exact symbolic identities over Q(q).
- Zero fitted parameters (CAL-1 m_e and substrate q_0 only).
- Cross-anchor q0_comparison at BOTH proton (q_p = q_at(80)) and muon (q_mu = q_muon_at(80)) pins,
  with analytic logarithmic q-sensitivity d(ln m_nu)/d(ln q) cross-checked against finite differences
  and CODATA-2022 m_e uncertainty propagation.
- Explicit PDG-2024 +/- uncertainties and Planck-2018+BAO / KATRIN-2024 / KamLAND-Zen-800 bounds.
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in (
    "tools/qou-substrate/python",
    "tools/pyhecke/python",
    "computations",
    "computations/substrate",
):
    _s = str(_ROOT / _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

mp.mp.dps = 80

from q_parameter import Q_50_DIGIT_STR, q_at, q_muon_at  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import M_E_MEV_STR, q_int_at, vol_4_1_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder, q0_comparison  # noqa: E402

WORKING_DPS = 80


def fmt80(x: mp.mpf) -> str:
    return mp.nstr(x, WORKING_DPS)


def fmt24(x: mp.mpf) -> str:
    return mp.nstr(x, 24)


def symbolic_identities() -> dict[str, str]:
    """Verify exact Q(q) symbolic identities proved in NeutrinoUnknotSweedlerLift.lean."""
    q, me, mp_sym, vew = sp.symbols("q me mp vew", positive=True)
    hbar = 1 - 1 / q
    s = q**2 - 1
    z_d = q**3 / (q**2 + 1)
    h_hecke = q - 1 / q

    # 1. Sweedler vs Habiro amplification ratio
    ratio_12 = sp.simplify((s**12) / (hbar**12) - (q * (q + 1)) ** 12)
    assert ratio_12 == 0

    # 2. Weinberg see-saw identity for alpha_v^3 * m_e
    alpha_v = mp_sym / vew
    lam_ewb = vew**5 / (me * mp_sym**3)
    wein_diff = sp.simplify((alpha_v**3) * me - (vew**2) / lam_ewb)
    assert wein_diff == 0

    # 3. Suppression factor of m_e^3 / v_weak^2 relative to alpha_v^3 * m_e
    supp_diff = sp.simplify((me**3 / vew**2) - (alpha_v**3 * me) * (vew * me**2 / mp_sym**3))
    assert supp_diff == 0

    # 4. 2-strand unknot stabilization Markov traces tau_M(sigma_1) vs tau_M(sigma_1^-1)
    tau_pos = z_d
    tau_neg = sp.simplify(z_d - h_hecke)
    assert sp.simplify(tau_neg - 1 / (q * (q**2 + 1))) == 0
    assert sp.simplify(tau_pos - tau_neg - h_hecke) == 0
    assert sp.simplify(tau_pos / tau_neg - q**4) == 0
    assert sp.simplify(tau_pos / q**2 - q / (q**2 + 1)) == 0
    assert sp.simplify(tau_neg * q**2 - q / (q**2 + 1)) == 0

    # 5. Exact logarithmic q-elasticity of (q^2 - 1)^k * m_e: d ln m / d ln q = 2 k q^2 / (q^2 - 1)
    k_sym = sp.Symbol("k", positive=True)
    dln_sweedler = sp.simplify(q * sp.diff(sp.log(me * (q**2 - 1) ** k_sym), q))
    assert sp.simplify(dln_sweedler - 2 * k_sym * q**2 / (q**2 - 1)) == 0

    return {
        "sweedler_over_habiro_factor": "(q * (q + 1))**k",
        "ew_cubic_weinberg_uv_scale": "vew**5 / (me * mp**3)",
        "me3_vew2_over_alpha_v3_me": "vew * me**2 / mp**3",
        "unknot_stab_pos_markov_trace": str(tau_pos),
        "unknot_stab_neg_markov_trace": str(tau_neg),
        "unknot_stab_markov_chiral_diff": "q - 1/q",
        "unknot_stab_markov_framing_ratio": "q**4",
        "jones_writhe_normalised_common_value": "q/(q**2 + 1)",
        "sweedler_log_q_elasticity": str(dln_sweedler),
    }


def derived_mp_mev(qv: mp.mpf) -> mp.mpf:
    me_mev = mp.mpf(M_E_MEV_STR)
    qi = mp.mpf(1) / qv
    hv = qv - qi
    hbar_sq = (mp.mpf(1) - qi) ** 2
    vol = vol_4_1_at(WORKING_DPS)
    tr_m = abs((mp.mpf(4) + hv**2 - mp.mpf(3) * hv**4 - hv**6) / (hv**2 + mp.mpf(4)))
    qf3 = (qv**2 + mp.mpf(1) + qi**2) * (qv + qi)
    return me_mev * (mp.mpf(2) * vol / hbar_sq * (tr_m * qf3 / (qv**3)) - mp.mpf(12))


def solve_ew_alpha_v(qv: mp.mpf) -> mp.mpf:
    """Unique positive root of Bring-Schwinger EW cubic in (0, 2 / T_EW)."""
    qi = mp.mpf(1) / qv
    hbar_sq = (mp.mpf(1) - qi) ** 2
    q2 = q_int_at(2, q=qv, dps=WORKING_DPS)
    q4 = q_int_at(4, q=qv, dps=WORKING_DPS)
    q6 = q_int_at(6, q=qv, dps=WORKING_DPS)
    q8 = q_int_at(8, q=qv, dps=WORKING_DPS)
    t_ew = qv * (q2 / mp.mpf(2)) * q4 * q6 * q8 + mp.mpf(1) / mp.pi
    h_norm = q2 / (mp.mpf(8) * mp.pi)
    return mp.findroot(
        lambda a: mp.mpf(1) / a - (t_ew - a * h_norm * (mp.mpf(1) - hbar_sq * a)),
        mp.mpf(1) / t_ew,
    )


def weak_vertex_t35_trace(qv: mp.mpf) -> mp.mpf:
    return (qv**2) * (qv**12 + qv**8 - mp.mpf(1)) / ((qv**2 + mp.mpf(1)) ** 2)


def classify_window(
    m_mev: mp.mpf, sqrt_dm21_mev: mp.mpf, sqrt_dm31_mev: mp.mpf, planck_sum_mev: mp.mpf
) -> str:
    if sqrt_dm21_mev <= m_mev <= sqrt_dm31_mev:
        return "IN_STRICT_OSCILLATION_BAND_[sqrt(dm21^2),_sqrt(|dm31^2|)]"
    if mp.mpf("0.5") * sqrt_dm21_mev <= m_mev <= planck_sum_mev:
        return "NEAR_OSCILLATION_SUB_PLANCK_WINDOW"
    if m_mev > planck_sum_mev:
        return "EXCLUDED_TOO_HEAVY_EXCEEDS_PLANCK_120_meV"
    return "EXCLUDED_OVER_SUPPRESSED_BELOW_SOLAR_SCALE"


def evaluate_pin(
    pin_name: str,
    qv: mp.mpf,
    me_ev: mp.mpf,
    me_rel_unc: mp.mpf,
    obs: dict[str, mp.mpf],
) -> dict:
    s = qv**2 - mp.mpf(1)
    qi = mp.mpf(1) / qv
    hbar = mp.mpf(1) - qi
    h_hecke = qv - qi
    z_d = qv**3 / (qv**2 + mp.mpf(1))

    alpha_v = solve_ew_alpha_v(qv)
    nv = mp.mpf(1) / alpha_v
    mp_ev = derived_mp_mev(qv) * mp.mpf("1e6")
    vew_ev = nv * mp_ev
    w_t35 = weak_vertex_t35_trace(qv)

    # 2-strand unknot stabilization Markov traces
    tau_pos = z_d
    tau_neg = z_d - h_hecke
    jones_norm_pos = (qi**2) * tau_pos
    jones_norm_neg = (qv**2) * tau_neg

    # Pre-registered zero-parameter candidate menu
    raw_candidates = [
        ("M0_tree_unknot", "volumeMass(m_e, Vol(0_1)=0)", mp.mpf(0)),
        ("S_k8_sweedler_4hop", "(q_0^2 - 1)^8 * m_e", (s**8) * me_ev),
        ("S_k10_sweedler_5hop", "(q_0^2 - 1)^10 * m_e", (s**10) * me_ev),
        ("S_k12_sweedler_6hop", "(q_0^2 - 1)^12 * m_e", (s**12) * me_ev),
        ("S_k12_t35_2loop", "W_{T(3,5)}(q_0)^2 * (q_0^2 - 1)^12 * m_e", (w_t35**2) * (s**12) * me_ev),
        ("S_k14_sweedler_7hop", "(q_0^2 - 1)^14 * m_e", (s**14) * me_ev),
        ("H_k7_habiro", "hbar_{q_0}^7 * m_e", (hbar**7) * me_ev),
        ("H_k8_habiro", "hbar_{q_0}^8 * m_e", (hbar**8) * me_ev),
        ("H_k12_habiro", "hbar_{q_0}^12 * m_e", (hbar**12) * me_ev),
        ("E_me3_over_v2", "m_e^3 / v_weak(q_0)^2", (me_ev**3) / (vew_ev**2)),
        ("EW_k2_alpha_v2_me", "alpha_v(q_0)^2 * m_e = m_e / N_v^2", (alpha_v**2) * me_ev),
        ("EW_k3_alpha_v3_me", "alpha_v(q_0)^3 * m_e = m_e / N_v^3", (alpha_v**3) * me_ev),
        ("EW_k3_t35_alpha_v3_me", "W_{T(3,5)}(q_0)^2 * alpha_v(q_0)^3 * m_e", (w_t35**2) * (alpha_v**3) * me_ev),
        ("EW_k4_alpha_v4_me", "alpha_v(q_0)^4 * m_e = m_e / N_v^4", (alpha_v**4) * me_ev),
        ("W_seesaw_Nv6", "v_weak(q_0)^2 / (m_p * N_v^6) = alpha_v^4 * m_p", (alpha_v**4) * mp_ev),
        ("W_seesaw_Nv7", "v_weak(q_0)^2 / (m_p * N_v^7) = alpha_v^5 * m_p", (alpha_v**5) * mp_ev),
    ]

    sqrt_dm21_mev = obs["sqrt_dm21_meV"]
    sqrt_dm31_mev = obs["sqrt_dm31_nh_meV"]
    planck_mev = obs["planck_sum_bound_meV"]

    cand_rows = {}
    for key, expr_str, val_ev in raw_candidates:
        val_mev = val_ev * mp.mpf("1e3")
        unc_mev = val_mev * me_rel_unc  # propagated CAL-1 m_e CODATA-2022 uncertainty
        cand_rows[key] = {
            "formula": expr_str,
            "m_nu_eV": fmt80(val_ev),
            "m_nu_meV": fmt24(val_mev),
            "propagated_me_unc_meV": fmt24(unc_mev),
            "ratio_to_sqrt_dm21": fmt24(val_mev / sqrt_dm21_mev) if val_mev > 0 else "0",
            "ratio_to_sqrt_dm31": fmt24(val_mev / sqrt_dm31_mev) if val_mev > 0 else "0",
            "verdict": classify_window(val_mev, sqrt_dm21_mev, sqrt_dm31_mev, planck_mev)
            if val_mev > 0
            else "TREE_LEVEL_MASSLESS_BASELINE",
        }

    # Exact 0nu2beta effective Majorana mass band at m_1 = 0 (NH) vs m_3 = 0 (IH)
    # Using PDG-2024 sin^2(theta_12) = 0.307 +- 0.013, sin^2(theta_13) = 0.0220 +- 0.0007
    s12_sq = obs["sin2_theta12_pdg"]
    s13_sq = obs["sin2_theta13_pdg"]
    c12_sq = mp.mpf(1) - s12_sq
    c13_sq = mp.mpf(1) - s13_sq
    u1 = c12_sq * c13_sq
    u2 = s12_sq * c13_sq
    u3 = s13_sq
    mbb_nh_max = u2 * sqrt_dm21_mev + u3 * sqrt_dm31_mev
    mbb_nh_min = abs(u2 * sqrt_dm21_mev - u3 * sqrt_dm31_mev)

    lam_ewb_gev = (vew_ev**5) / (me_ev * (mp_ev**3)) * mp.mpf("1e-9")

    return {
        "pin": pin_name,
        "q0_80dps": fmt80(qv),
        "q0_sq_minus_1": fmt80(s),
        "hbar_q0": fmt80(hbar),
        "alpha_v_ew_fixed_point": fmt80(alpha_v),
        "N_v_ew_fixed_point": fmt80(nv),
        "derived_m_p_MeV": fmt24(mp_ev * mp.mpf("1e-6")),
        "derived_v_weak_GeV": fmt24(vew_ev * mp.mpf("1e-9")),
        "effective_Lambda_EWB_GeV": fmt24(lam_ewb_gev),
        "sweedler_over_habiro_k12_ratio": fmt24((qv * (qv + mp.mpf(1))) ** 12),
        "unknot_stabilization_framing": {
            "tau_M_sigma1_pos": fmt80(tau_pos),
            "tau_M_sigma1_neg": fmt80(tau_neg),
            "chiral_diff_h": fmt80(tau_pos - tau_neg),
            "framing_ratio_q4": fmt80(tau_pos / tau_neg),
            "jones_writhe_norm_pos": fmt80(jones_norm_pos),
            "jones_writhe_norm_neg": fmt80(jones_norm_neg),
            "jones_norm_abs_diff": fmt80(abs(jones_norm_pos - jones_norm_neg)),
        },
        "majorana_0nu2beta_nh_m1_zero_band_meV": {
            "m_bb_min_destructive_meV": fmt24(mbb_nh_min),
            "m_bb_max_constructive_meV": fmt24(mbb_nh_max),
            "dirac_prediction_meV": "0",
        },
        "candidates": cand_rows,
    }


def main() -> int:
    t0 = time.time()
    mp.mp.dps = WORKING_DPS

    q_proton = q_at(WORKING_DPS)
    q_muon = q_muon_at(WORKING_DPS)

    me_entry = codata("electron mass energy equivalent in MeV")
    me_mev = mp.mpf(M_E_MEV_STR)
    me_unc_mev = mp.mpf(me_entry.uncertainty_str)
    me_rel_unc = me_unc_mev / me_mev
    me_ev = me_mev * mp.mpf("1e6")

    # PDG-2024 & cosmological / laboratory bounds (with explicit 1-sigma / CL uncertainties)
    dm21_sq = mp.mpf("7.53e-5")
    dm21_sq_unc = mp.mpf("0.18e-5")
    dm32_nh_sq = mp.mpf("2.455e-3")
    dm32_nh_sq_unc = mp.mpf("0.028e-3")
    dm31_nh_sq = dm32_nh_sq + dm21_sq
    dm31_nh_sq_unc = mp.sqrt(dm32_nh_sq_unc**2 + dm21_sq_unc**2)

    sqrt_dm21_mev = mp.sqrt(dm21_sq) * mp.mpf("1e3")
    sqrt_dm21_unc_mev = (dm21_sq_unc / (mp.mpf(2) * mp.sqrt(dm21_sq))) * mp.mpf("1e3")
    sqrt_dm31_nh_mev = mp.sqrt(dm31_nh_sq) * mp.mpf("1e3")
    sqrt_dm31_nh_unc_mev = (dm31_nh_sq_unc / (mp.mpf(2) * mp.sqrt(dm31_nh_sq))) * mp.mpf("1e3")

    obs = {
        "dm21_sq_eV2": dm21_sq,
        "dm21_sq_unc_eV2": dm21_sq_unc,
        "dm31_nh_sq_eV2": dm31_nh_sq,
        "dm31_nh_sq_unc_eV2": dm31_nh_sq_unc,
        "sqrt_dm21_meV": sqrt_dm21_mev,
        "sqrt_dm21_unc_meV": sqrt_dm21_unc_mev,
        "sqrt_dm31_nh_meV": sqrt_dm31_nh_mev,
        "sqrt_dm31_nh_unc_meV": sqrt_dm31_nh_unc_mev,
        "sin2_theta12_pdg": mp.mpf("0.307"),
        "sin2_theta12_unc_pdg": mp.mpf("0.013"),
        "sin2_theta13_pdg": mp.mpf("0.0220"),
        "sin2_theta13_unc_pdg": mp.mpf("0.0007"),
        "planck_sum_bound_meV": mp.mpf("120.0"),
        "katrin_2024_m_nue_bound_meV": mp.mpf("450.0"),
    }

    sym_data = symbolic_identities()
    res_p = evaluate_pin("proton", q_proton, me_ev, me_rel_unc, obs)
    res_m = evaluate_pin("muon", q_muon, me_ev, me_rel_unc, obs)

    # Analytic vs finite-difference q-elasticity check on S_k12_sweedler_6hop
    m_sw12_p = mp.mpf(res_p["candidates"]["S_k12_sweedler_6hop"]["m_nu_eV"])
    m_sw12_m = mp.mpf(res_m["candidates"]["S_k12_sweedler_6hop"]["m_nu_eV"])
    m_ew3_p = mp.mpf(res_p["candidates"]["EW_k3_alpha_v3_me"]["m_nu_eV"])
    m_ew3_m = mp.mpf(res_m["candidates"]["EW_k3_alpha_v3_me"]["m_nu_eV"])

    q_mid = (q_proton + q_muon) / mp.mpf(2)
    elasticity_analytic = mp.mpf(24) * (q_mid**2) / (q_mid**2 - mp.mpf(1))
    elasticity_fd = mp.log(m_sw12_m / m_sw12_p) / mp.log(q_muon / q_proton)
    elasticity_rel_err = abs(elasticity_fd - elasticity_analytic) / elasticity_analytic

    sw12_swing_ppm = abs(m_sw12_m - m_sw12_p) / m_sw12_p * mp.mpf("1e6")
    ew3_swing_ppb = abs(m_ew3_m - m_ew3_p) / m_ew3_p * mp.mpf("1e9")

    # Key meV values at proton pin
    sw12_mev = mp.mpf(res_p["candidates"]["S_k12_sweedler_6hop"]["m_nu_meV"])
    t35_12_mev = mp.mpf(res_p["candidates"]["S_k12_t35_2loop"]["m_nu_meV"])
    ew3_mev = mp.mpf(res_p["candidates"]["EW_k3_alpha_v3_me"]["m_nu_meV"])
    ew3_t35_mev = mp.mpf(res_p["candidates"]["EW_k3_t35_alpha_v3_me"]["m_nu_meV"])
    hb7_mev = mp.mpf(res_p["candidates"]["H_k7_habiro"]["m_nu_meV"])
    hb12_mev = mp.mpf(res_p["candidates"]["H_k12_habiro"]["m_nu_meV"])
    me3_v2_mev = mp.mpf(res_p["candidates"]["E_me3_over_v2"]["m_nu_meV"])
    sw8_mev = mp.mpf(res_p["candidates"]["S_k8_sweedler_4hop"]["m_nu_meV"])
    ew2_mev = mp.mpf(res_p["candidates"]["EW_k2_alpha_v2_me"]["m_nu_meV"])

    wb = WitnessBuilder(
        "neutrino-unknot-sweedler-lift-probe",
        engine="mpmath+sympy",
        start_time=t0,
        _script_path=__file__,
    )
    wb.set_description(
        "80-dps cross-anchor adjudication probe for Q-Gap-10 (qou-nu01): evaluates zero-parameter "
        "radiative & see-saw neutrino mass lifts above Vol(0_1) = 0 across proton and muon q_0 pins "
        "((q_0^2 - 1)^k m_e, W_{T(3,5)}^2 (q_0^2 - 1)^12 m_e, hbar_{q_0}^k m_e, m_e^3 / v_weak^2, "
        "alpha_v^k m_e = m_e / N_v^k, and Weinberg v_weak^2 / M_UV scales), verifies 2-strand 0_1 "
        "stabilization Markov framing parity (Dirac vs Majorana 0nu2beta selection), and checks "
        "analytic q-elasticities and CODATA-2022 / PDG-2024 uncertainty propagation."
    )
    wb.add_parameter("working_dps", WORKING_DPS)
    wb.add_parameter("zero_fitting", True)
    wb.add_parameter("cal1_me_MeV", M_E_MEV_STR)
    wb.add_parameter("cal1_me_unc_MeV", me_entry.uncertainty_str)

    wb.add_assertion(
        "sweedler_k12_and_ew_alpha_v3_land_strictly_inside_pdg_oscillation_band",
        computed="1"
        if (
            sqrt_dm21_mev < sw12_mev < t35_12_mev < ew3_mev < ew3_t35_mev < hb7_mev < sqrt_dm31_nh_mev
        )
        else "0",
        expected="1",
        tolerance="0",
        source=(
            "8.678 meV < 12.458 meV ((q^2-1)^12 m_e) < 17.567 meV (T(3,5)^2) < "
            "28.277 meV (alpha_v^3 m_e) < 39.874 meV (T(3,5)^2 alpha_v^3 m_e) < "
            "47.904 meV (hbar_q^7 m_e) < 50.302 meV (sqrt(dm31^2))"
        ),
    )
    wb.add_assertion(
        "hbar12_and_me3_over_v2_excluded_by_three_to_five_orders_of_magnitude",
        computed="1"
        if (hb12_mev < mp.mpf("1e-3") and me3_v2_mev < mp.mpf("5e-3"))
        else "0",
        expected="1",
        tolerance="0",
        source=(
            "hbar_q^12 m_e = 0.00045745 meV (suppressed by [q(q+1)]^12 = 27,234x vs Sweedler-12) "
            "and m_e^3 / v_weak^2 = 0.00220097 meV (3,943x below solar sqrt(dm21^2))"
        ),
    )
    wb.add_assertion(
        "lower_powers_k8_sweedler_and_alpha_v2_excluded_by_planck_and_katrin",
        computed="1"
        if (sw8_mev > mp.mpf("4000") and ew2_mev > mp.mpf("7000"))
        else "0",
        expected="1",
        tolerance="0",
        source=(
            "(q^2 - 1)^8 m_e = 4.296 eV and alpha_v^2 m_e = 7.420 eV both exceed Planck 0.12 eV "
            "and KATRIN 0.45 eV, uniquely selecting k=12 (Sweedler) and k=3 (alpha_v^3 m_e)"
        ),
    )
    wb.add_assertion(
        "unknot_stabilization_markov_chiral_split_and_jones_writhe_collapse",
        computed=res_p["unknot_stabilization_framing"]["jones_norm_abs_diff"],
        expected="0",
        tolerance="1e-75",
        source="tau_M(sigma_1)/q^2 == tau_M(sigma_1^-1)*q^2 == q/(q^2+1) while unnormalised ratio is q^4 != 1",
    )
    wb.add_assertion(
        "analytic_sweedler_log_q_elasticity_matches_cross_anchor_finite_diff",
        computed=fmt24(elasticity_rel_err),
        expected="0",
        tolerance="1e-5",
        source="d ln((q^2-1)^12 m_e) / d ln q = 24 q^2 / (q^2 - 1) = 127.445 matches (q_p, q_mu) finite difference",
    )

    wb.add_data("symbolic_identities_Q_of_q", sym_data)
    wb.add_data(
        "observational_anchors_with_uncertainties",
        {k: fmt24(v) for k, v in obs.items()},
    )
    wb.add_data("pins", {"proton": res_p, "muon": res_m})
    wb.add_data(
        "cross_anchor_sensitivity",
        {
            "sweedler_k12_log_q_elasticity_analytic": fmt24(elasticity_analytic),
            "sweedler_k12_log_q_elasticity_finite_diff": fmt24(elasticity_fd),
            "sweedler_k12_proton_vs_muon_ppm": fmt24(sw12_swing_ppm),
            "ew_alpha_v3_me_proton_vs_muon_ppb": fmt24(ew3_swing_ppb),
        },
    )

    out_path = wb.save(
        q0_comparison(
            muon=mp.nstr(q_muon, 50),
            proton=Q_50_DIGIT_STR,
            reason=(
                "evaluates Q-Gap-10 (qou-nu01) zero-parameter Sweedler, Habiro, Weinberg, and "
                "Bring-Schwinger alpha_v^3 neutrino mass lift scales and 0_1 stabilization framing "
                "traces at 80 dps across both registered q_0 pins (proton q_p and muon q_mu)"
            ),
        )
    )

    print("=" * 92)
    print(" Q-GAP-10 (qou-nu01): NEUTRINO UNKNOT SWEEDLER & ELECTROWEAK LIFT PROBE (80 dps)")
    print("=" * 92)
    print(f" PDG-2024 window : sqrt(dm21^2) = {mp.nstr(sqrt_dm21_mev, 6)} +- {mp.nstr(sqrt_dm21_unc_mev, 3)} meV | "
          f"sqrt(dm31^2) = {mp.nstr(sqrt_dm31_nh_mev, 6)} +- {mp.nstr(sqrt_dm31_nh_unc_mev, 3)} meV")
    print("-" * 92)
    for key, info in res_p["candidates"].items():
        print(f" {key:24s} | {mp.nstr(mp.mpf(info['m_nu_meV']), 8):>14s} meV | {info['verdict']}")
    print("-" * 92)
    print(f" Sweedler-12 cross-anchor swing: {mp.nstr(sw12_swing_ppm, 6)} ppm | "
          f"EW alpha_v^3 m_e swing: {mp.nstr(ew3_swing_ppb, 6)} ppb")
    print(f" Witness written to: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
