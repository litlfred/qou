#!/usr/bin/env python3
"""80-dps First-Principles Evaluation of Electroweak Gauge Bosons `M_W`, `M_Z`, Weinberg Angle
`sin^2 theta_W`, Reconciled Higgs Mass `m_H`, and `v`-Independent Higgs Quartic `lambda_H`
Atop QOU-Derived `(v_weak(q_0), alpha_EM(q_0))` (`Q-Gap-9`: `qou-ewsb`, `qou-ukqh`, `qou-z3x8`, `qou-zd6l`).

Companion to `QOU/StandardModel/ElectroweakBosonThresholdsAndWeinberg.lean` and
`docs/audits/2026-11-24-electroweak-mw-mz-weinberg-higgs-80dps-audit.md`.

STRICT PRECISION & ANTI-FIT DISCIPLINE:
- `mpmath` at `WORK_DPS = 125`, `OUT_DPS = 80` throughout; ZERO `float64`, ZERO `float(...)`,
  ZERO `numpy`, ZERO `math` floating functions.
- Evaluates at BOTH canonical proton anchor `q_proton = q_at(125)` and ideal muon anchor
  `q_muon = q_muon_at(125)` (`q0_comparison`).
- ZERO upstream empirical electroweak or proton mass inputs:
  * `m_p(q_0)` is derived purely from `m_e` and `q_0` via the Borromean proton substrate identity;
  * `v_weak(q_0)` is derived via `ElectroweakBringSchwingerBridge.ewFixedPointCubic`;
  * `alpha_EM(q_0)` is evaluated across BOTH Form-B 1-loop (`c_2 = 0`) and 2-loop Bloch-`B_3`
    (`AlphaEmTwoLoopBlochSchwinger`);
  * Self-consistent radiative thresholds `M_Z = M_Z(mu = M_Z)` solve the fixed point in `mu`
    directly without inserting experimental `M_Z` inside `ln(M_Z / m_f)`;
  * `m_H` and `lambda_H` are evaluated directly from QOU-derived `(M_W, M_Z)`, eliminating the
    `21.9 MeV` empirical `W`/`Z`-anchor spread identically (`|m_H^(W) - m_H^(Z)| = 0`).
- All PDG-2024 / CODATA-2022 empirical numbers enter strictly downstream as external comparison
  targets; every candidate arm (hits and misses alike) is reported side-by-side (`selected = none`).
"""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent
for _p in (
    str(_ROOT / "computations"),
    str(_ROOT / "computations" / "substrate"),
    str(_ROOT / "tools" / "qou-substrate" / "python"),
):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge  # noqa: F401, E402
from _precision import set_compute_dps, fmt  # noqa: E402

OUT_DPS = 80
WORK_DPS = 125
set_compute_dps(OUT_DPS)

import mpmath as mp  # noqa: E402
from mpmath import mpf, fabs, sqrt, log, log10, polylog, zeta, clsin  # noqa: E402

mp.mp.dps = WORK_DPS

from q_parameter import q_at, q_muon_at  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_E_MEV_ERR,
    M_P_MEV_VALIDATION,
    M_PI_PM_MEV_VALIDATION,
)
from qou_substrate import codata as _codata  # noqa: E402
from witness_base import WitnessBuilder, q0_comparison  # noqa: E402


# External PDG-2024 / CODATA-2022 comparison targets ONLY (never upstream inputs)
PDG_GF_GEV_INV2 = mpf("1.1663787e-5")
PDG_GF_SIG_GEV_INV2 = mpf("0.0000006e-5")
PDG_MW_GEV = mpf("80.3692")
PDG_MW_SIG_GEV = mpf("0.0133")
PDG_MZ_GEV = mpf("91.1876")
PDG_MZ_SIG_GEV = mpf("0.0021")
PDG_MH_GEV = mpf("125.20")
PDG_MH_SIG_GEV = mpf("0.11")
PDG_SIN2_MSBAR_MZ = mpf("0.23122")
PDG_SIN2_MSBAR_SIG = mpf("0.00004")
M_PI_PM_ERR_MEV = mpf("0.00018")


def _binom(n: int, k: int) -> int:
    """Exact integer binomial coefficient."""
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    num = 1
    for i in range(k):
        num = num * (n - i) // (i + 1)
    return num


def _qbal(n: int, qv: mpf) -> mpf:
    """Balanced quantum integer `[n]_q = (q^n - q^{-n}) / (q - q^{-1})`."""
    return (qv ** n - qv ** (-n)) / (qv - mpf(1) / qv)


def _two_mul_p(m: int, hv: mpf) -> mpf:
    """Doubled binomial Plancherel trace polynomial `2 * P_m(h) = sum_{j=0}^m C(m+j, 2j) h^{2j}`."""
    acc = mpf(0)
    for j in range(m + 1):
        acc += mpf(_binom(m + j, 2 * j)) * (hv ** (2 * j))
    return acc


def _derived_mp_gev(qv: mpf, me_gev: mpf) -> mpf:
    """Pure QOU Borromean proton mass `m_p(q)` in GeV from `m_e` and `q` (zero CODATA `m_p` input)."""
    one = mpf(1)
    vol41 = mpf(2) * clsin(2, mp.pi / mpf(3))
    hv = qv - one / qv
    hb = one - one / qv
    tr_bor = fabs((mpf(4) + hv ** 2 - mpf(3) * (hv ** 4) - hv ** 6) / (hv ** 2 + mpf(4)))
    qf3 = (qv ** 2 + one + qv ** (-2)) * (qv + one / qv)
    mp_over_me = mpf(2) * (vol41 / (hb ** 2)) * (tr_bor * qf3 / (qv ** 3)) - mpf(12)
    return me_gev * mp_over_me


def _derived_mmu_gev(qv: mpf, me_gev: mpf) -> mpf:
    """Figure-eight lepton scale `m_mu(q) = m_e * Vol(4_1) / hbar_q^2` in GeV."""
    vol41 = mpf(2) * clsin(2, mp.pi / mpf(3))
    hb = mpf(1) - mpf(1) / qv
    return me_gev * vol41 / (hb ** 2)


def _solve_alpha_em(qv: mpf, two_loop_bloch_b3: bool) -> mpf:
    """Solve Form-B (`c2 = 0`) or 2-loop Bloch-`B_3` Bring-Schwinger cubic for `alpha_EM(q)`."""
    one = mpf(1)
    hv = qv - one / qv
    t_em = qv * _qbal(9, qv) * _qbal(10, qv) + mpf(2) / (mpf(3) * mp.pi)
    h_norm = _qbal(2, qv) / (mpf(8) * mp.pi)
    if two_loop_bloch_b3:
        delta_b3 = zeta(3) - polylog(3, qv ** (-2))
        c2_add = h_norm * (delta_b3 / (mpf(8) * mp.pi))
    else:
        c2_add = mpf(0)
    c3 = c2_add - h_norm * (hv ** 2)
    return mp.findroot(
        lambda a: c3 * (a ** 3) + h_norm * (a ** 2) + t_em * a - one,
        one / t_em,
    )


def _solve_alpha_v(qv: mpf) -> tuple[mpf, mpf, mpf]:
    """Solve `ElectroweakBringSchwingerBridge.ewFixedPointCubic` for `(alpha_v, N_v, T_EW)`."""
    one = mpf(1)
    hb = one - one / qv
    q2 = _qbal(2, qv)
    t_ew = qv * (q2 / mpf(2)) * _qbal(4, qv) * _qbal(6, qv) * _qbal(8, qv) + one / mp.pi
    h_norm = q2 / (mpf(8) * mp.pi)
    av = mp.findroot(
        lambda a: h_norm * (hb ** 2) * (a ** 3) - h_norm * (a ** 2) + t_ew * a - one,
        one / t_ew,
    )
    return av, one / av, t_ew


def _weinberg_candidates(qv: mpf, inv_aem_mz_pert: mpf) -> dict[str, dict[str, str]]:
    """Evaluate all pre-existing QOU Weinberg angle candidates side-by-side at `qv`."""
    one = mpf(1)
    two = mpf(2)
    hv = qv - one / qv
    q2 = _qbal(2, qv)
    q3 = _qbal(3, qv)
    u0 = qv ** 2 - one

    tp2 = _two_mul_p(2, hv)
    tp3 = _two_mul_p(3, hv)
    r_zw_bare = tp3 / tp2
    s2_bare = one - one / (r_zw_bare ** 2)
    r_zw_dressed = (tp3 * (q2 ** 2)) / (tp2 * mpf(4))
    s2_dressed = one - one / (r_zw_dressed ** 2)

    # Same-rank H_2 Markov trace ratio `T(2,4) / T(2,6)` (`TorusLinkElectroweakSchurRatio.lean`)
    tr_t24_h2 = (qv ** 10 + qv ** 8 + qv ** 6 + one) / ((qv ** 2) * ((qv ** 2 + one) ** 2))
    tr_t26_h2 = (qv ** 14 + qv ** 12 + qv ** 10 + one) / ((qv ** 4) * ((qv ** 2 + one) ** 2))
    s2_h2_markov = one - (tr_t24_h2 / tr_t26_h2) ** 2

    # Cross-rank Wenzl-Higman Schur `M4` on `(T(2,4) in H_2, T(3,5) in H_3)` (`17/81` at `q=1`,
    # `TorusLinkElectroweakSchurRatio.schurIrrepT24H2` / `schurIrrepT35H3`)
    y2_triv = (qv ** 4 + qv ** 2 + one) / ((qv ** 2 + one) ** 2)
    y2_sign = (qv ** 2) / ((qv ** 2 + one) ** 2)
    schur_t24 = (qv * q2) * y2_triv * (qv ** 4) + ((one / qv) * q2) * y2_sign * (qv ** (-4))
    y3_triv_wt = (qv ** 4 + one) / ((qv ** 2 + one) ** 2)
    y3_std_wt = (qv ** 2) / ((qv ** 2 + one) ** 2)
    schur_t35 = (qv ** 3 * q2 * q3) * y3_triv_wt * (qv ** 10) + q3 * y3_std_wt * (-one)
    s2_schur_m4 = one - (schur_t24 / schur_t35) ** 2

    # Order-zero pure-pattern H_6 Hoefsmit ratio `cot(theta_W) = q_0^{-4}` (`qou-zd6l` gap note)
    cot_h6_pure = qv ** (-4)
    s2_h6_pure = one / (one + cot_h6_pure ** 2)

    # 1-loop Georgi-Quinn-Weinberg from UV `3/8` at Sweedler `k = 17` and `k = 18`
    neg_ln_u0 = -log(u0)
    s2_gqw_k17 = mpf(3) / mpf(8) - (mpf(109) / mpf(24)) * (mpf(17) * neg_ln_u0 / (two * mp.pi)) / inv_aem_mz_pert
    s2_gqw_k18 = mpf(3) / mpf(8) - (mpf(109) / mpf(24)) * (mpf(18) * neg_ln_u0 / (two * mp.pi)) / inv_aem_mz_pert

    pdg_onshell = one - (PDG_MW_GEV / PDG_MZ_GEV) ** 2

    def _pack(val: mpf, target: mpf, target_label: str) -> dict[str, str]:
        return {
            "sin2_thetaW": fmt(val, OUT_DPS),
            "comparison_scheme": target_label,
            "abs_diff": fmt(val - target, OUT_DPS),
            "rel_err_pct": fmt((val - target) / target * mpf(100), OUT_DPS),
            "rel_err_ppm": fmt((val - target) / target * (mpf(10) ** 6), OUT_DPS),
        }

    return {
        "W1_torus_plancherel_dressed_T24_T26": _pack(s2_dressed, pdg_onshell, "PDG_onshell_1_sub_MW2_MZ2"),
        "W2_torus_plancherel_bare_P3_P2": _pack(s2_bare, pdg_onshell, "PDG_onshell_1_sub_MW2_MZ2"),
        "W3_schur_irrep_M4_T24_T35": _pack(s2_schur_m4, pdg_onshell, "PDG_onshell_1_sub_MW2_MZ2"),
        "W4_same_rank_H2_markov_T24_T26": _pack(s2_h2_markov, pdg_onshell, "PDG_onshell_1_sub_MW2_MZ2"),
        "W5_h6_pure_pattern_cot_q_inv4_gap_zd6l": _pack(s2_h6_pure, pdg_onshell, "PDG_onshell_1_sub_MW2_MZ2"),
        "W6a_gqw_1loop_sweedler_k17": _pack(s2_gqw_k17, PDG_SIN2_MSBAR_MZ, "PDG_MSbar_MZ"),
        "W6b_gqw_1loop_sweedler_k18": _pack(s2_gqw_k18, PDG_SIN2_MSBAR_MZ, "PDG_MSbar_MZ"),
    }


def _evaluate_chain_raw(
    qv: mpf,
    me_gev: mpf,
    mpi_gev: mpf,
    two_loop_bloch_b3: bool = True,
) -> dict[str, mpf]:
    """Core differentiable map `(q_0, m_e, m_pi) -> (v_weak, M_W, M_Z, sin^2, m_H, lambda_H)`."""
    one = mpf(1)
    two = mpf(2)
    hv = qv - one / qv
    hb = one - one / qv
    q2 = _qbal(2, qv)

    mp_gev = _derived_mp_gev(qv, me_gev)
    mmu_gev = _derived_mmu_gev(qv, me_gev)
    alpha0 = _solve_alpha_em(qv, two_loop_bloch_b3=two_loop_bloch_b3)
    av, nv, _ = _solve_alpha_v(qv)
    v_ew = nv * mp_gev

    tp2 = _two_mul_p(2, hv)
    tp3 = _two_mul_p(3, hv)
    tp4 = _two_mul_p(4, hv)
    r_zw = (tp3 * (q2 ** 2)) / (tp2 * mpf(4))
    c2_w = one / (r_zw ** 2)
    s2_w = one - c2_w

    a0_gev = sqrt(mp.pi * alpha0) * v_ew
    mw_l0 = a0_gev / sqrt(s2_w)
    mz_l0 = mw_l0 * r_zw

    # Veltman custodial 1-loop shift at unit top Yukawa `y_t = 1` (`m_t = v_ew / sqrt(2)`)
    # plus Sirlin (1980) 1-loop gauge vertex+box+boson self-energy remainder:
    drho_yt1 = mpf(3) / (mpf(32) * (mp.pi ** 2))
    dr_weak_1l = (alpha0 / (mpf(4) * mp.pi * s2_w)) * (
        ((mpf(7) - mpf(4) * s2_w) / two) * log(c2_w) + mpf(6)
    )

    def _solve_self_consistent_mz(dr_of_z) -> tuple[mpf, mpf, mpf]:
        mz_sol = mp.findroot(
            lambda z: (a0_gev / (sqrt(s2_w) * sqrt(one - dr_of_z(z)))) * r_zw - z,
            mpf(91),
        )
        return mz_sol / r_zw, mz_sol, dr_of_z(mz_sol)

    # L1a: Self-consistent leptonic VP only
    mw_l1a, mz_l1a, dr_l1a = _solve_self_consistent_mz(
        lambda z: (alpha0 / (mpf(3) * mp.pi))
        * (
            (log((z / me_gev) ** 2) - mpf(5) / mpf(3))
            + (log((z / mmu_gev) ** 2) - mpf(5) / mpf(3))
            + (log((z / mp_gev) ** 2) - mpf(5) / mpf(3))
        )
    )

    # L1b: Self-consistent full QED VP at baryon threshold `m_p(q_0)` without custodial top term
    mw_l1b, mz_l1b, dr_l1b = _solve_self_consistent_mz(
        lambda z: (alpha0 / (mpf(3) * mp.pi))
        * (
            (log((z / me_gev) ** 2) - mpf(5) / mpf(3))
            + (log((z / mmu_gev) ** 2) - mpf(5) / mpf(3))
            + (mpf(14) / mpf(3)) * (log((z / mp_gev) ** 2) - mpf(5) / mpf(3))
        )
    )

    # L2a: Self-consistent Sirlin 1-loop `Delta r` with baryon threshold `mu_had = m_p(q_0)` & `y_t = 1`
    mw_l2a, mz_l2a, dr_l2a = _solve_self_consistent_mz(
        lambda z: (alpha0 / (mpf(3) * mp.pi))
        * (
            (log((z / me_gev) ** 2) - mpf(5) / mpf(3))
            + (log((z / mmu_gev) ** 2) - mpf(5) / mpf(3))
            + (mpf(14) / mpf(3)) * (log((z / mp_gev) ** 2) - mpf(5) / mpf(3))
        )
        - (c2_w / s2_w) * drho_yt1
        + dr_weak_1l
    )

    # L2b: Self-consistent Sirlin 1-loop `Delta r` with meson pair threshold `mu_had = 2 m_pi` & `y_t = 1`
    mw_l2b, mz_l2b, dr_l2b = _solve_self_consistent_mz(
        lambda z: (alpha0 / (mpf(3) * mp.pi))
        * (
            (log((z / me_gev) ** 2) - mpf(5) / mpf(3))
            + (log((z / mmu_gev) ** 2) - mpf(5) / mpf(3))
            + (log((z / mp_gev) ** 2) - mpf(5) / mpf(3))
            + (mpf(11) / mpf(3)) * (log((z / (two * mpi_gev)) ** 2) - mpf(5) / mpf(3))
        )
        - (c2_w / s2_w) * drho_yt1
        + dr_weak_1l
    )

    h_fac_base = (tp4 / tp2) * (mpf(6) / mpf(5)) * (q2 / two)
    c_hab_half = one - (q2 / (mpf(16) * mp.pi)) * (hv ** 2)
    c_bring_zero = one - (two / (mpf(3) * mp.pi)) * (hb ** 2)
    c_borromean = one - two * mp.catalan * (hv ** 4)
    c_hab_full = one - (q2 / (mpf(8) * mp.pi)) * (hv ** 2)

    mh_l2a_tree = mw_l2a * h_fac_base
    mh_l2a_hab_half = mw_l2a * h_fac_base * c_hab_half
    mh_l2a_bring = mw_l2a * h_fac_base * c_bring_zero
    mh_l2a_borr = mw_l2a * h_fac_base * c_borromean
    mh_l2a_hab_full = mw_l2a * h_fac_base * c_hab_full

    mh_l2b_borr = mw_l2b * h_fac_base * c_borromean
    lam_l2a_tree = (mh_l2a_tree ** 2) / (two * (v_ew ** 2))
    lam_l2a_hab_half = (mh_l2a_hab_half ** 2) / (two * (v_ew ** 2))

    return {
        "mp_derived_gev": mp_gev,
        "mmu_derived_gev": mmu_gev,
        "alpha_em_0": alpha0,
        "alpha_em_inv_0": one / alpha0,
        "alpha_v": av,
        "N_v": nv,
        "v_weak_gev": v_ew,
        "G_F_gev_inv2": one / (sqrt(two) * (v_ew ** 2)),
        "A0_tree_gev": a0_gev,
        "r_zw_dressed": r_zw,
        "sin2_thetaW_planch": s2_w,
        "cos2_thetaW_planch": c2_w,
        "MW_L0_tree": mw_l0,
        "MZ_L0_tree": mz_l0,
        "dr_L1a_lept": dr_l1a,
        "MW_L1a_lept": mw_l1a,
        "MZ_L1a_lept": mz_l1a,
        "dr_L1b_qed_vp": dr_l1b,
        "MW_L1b_qed_vp": mw_l1b,
        "MZ_L1b_qed_vp": mz_l1b,
        "dr_L2a_sirlin_mp": dr_l2a,
        "MW_L2a_sirlin_mp": mw_l2a,
        "MZ_L2a_sirlin_mp": mz_l2a,
        "dr_L2b_sirlin_2mpi": dr_l2b,
        "MW_L2b_sirlin_2mpi": mw_l2b,
        "MZ_L2b_sirlin_2mpi": mz_l2b,
        "mH_L2a_tree": mh_l2a_tree,
        "mH_L2a_habiro_half": mh_l2a_hab_half,
        "mH_L2a_bring_zero": mh_l2a_bring,
        "mH_L2a_borromean": mh_l2a_borr,
        "mH_L2a_habiro_full": mh_l2a_hab_full,
        "mH_L2b_borromean": mh_l2b_borr,
        "lambda_H_L2a_tree": lam_l2a_tree,
        "lambda_H_L2a_habiro_half": lam_l2a_hab_half,
    }


def evaluate_anchor_full(
    anchor_name: str,
    qv: mpf,
    rel_sigma_q: mpf,
    me_gev: mpf,
    rel_sigma_me: mpf,
    mpi_gev: mpf,
    rel_sigma_mpi: mpf,
) -> dict:
    """Full 80-dps evaluation + Fréchet-Jacobian uncertainty propagation at `qv`."""
    one = mpf(1)
    two = mpf(2)
    hv = qv - one / qv
    hb = one - one / qv
    q2 = _qbal(2, qv)
    tp2 = _two_mul_p(2, hv)
    tp3 = _two_mul_p(3, hv)
    tp4 = _two_mul_p(4, hv)

    pdg_vew = one / sqrt(sqrt(two) * PDG_GF_GEV_INV2)
    pdg_vew_sig = pdg_vew * PDG_GF_SIG_GEV_INV2 / (two * PDG_GF_GEV_INV2)
    pdg_onshell_s2 = one - (PDG_MW_GEV / PDG_MZ_GEV) ** 2
    pdg_lam_h = (PDG_MH_GEV ** 2) / (two * (pdg_vew ** 2))

    bloch_raw = _evaluate_chain_raw(qv, me_gev, mpi_gev, two_loop_bloch_b3=True)
    formb_raw = _evaluate_chain_raw(qv, me_gev, mpi_gev, two_loop_bloch_b3=False)

    # Perturbative alpha_EM^{-1}(M_Z) at self-consistent QOU M_Z (zero PDG M_Z input)
    mz_ref = bloch_raw["MZ_L2a_sirlin_mp"]
    d_inva_pert = (two / (mpf(3) * mp.pi)) * (
        log(mz_ref / me_gev)
        + log(mz_ref / bloch_raw["mmu_derived_gev"])
        + (mpf(14) / mpf(3)) * log(mz_ref / bloch_raw["mp_derived_gev"])
    )
    inv_aem_mz_qou = bloch_raw["alpha_em_inv_0"] - d_inva_pert
    weinberg_arms = _weinberg_candidates(qv, inv_aem_mz_qou)

    # Complete Higgs W/Z-anchor reconciliation table across L0_tree, L2a(had=m_p), L2b(had=2*m_pi)
    c_loops = [
        ("C0_tree_dressed", "1 (dressed torus-link tree)", one),
        (
            "C1_habiro_half_h2",
            "1 - ([2]_q / (16*pi)) * h^2 (half-Habiro 1-loop)",
            one - (q2 / (mpf(16) * mp.pi)) * (hv ** 2),
        ),
        (
            "C2_bring_zero_hbar2",
            "1 - (2 / (3*pi)) * hbar_q^2 (Bring zero-mode)",
            one - (two / (mpf(3) * mp.pi)) * (hb ** 2),
        ),
        (
            "C3_borromean_2G_h4",
            "1 - 2 * G * h^4 (Borromean hyperbolic volume)",
            one - two * mp.catalan * (hv ** 4),
        ),
        (
            "C4_habiro_full_h2",
            "1 - ([2]_q / (8*pi)) * h^2 (full-Habiro 1-loop)",
            one - (q2 / (mpf(8) * mp.pi)) * (hv ** 2),
        ),
    ]

    higgs_reconciled: dict[str, dict] = {}
    max_wz_spread_gev = mpf(0)
    max_lam_vev_diff = mpf(0)

    for lvl_key, mw_val, mz_val, dr_val in [
        ("L0_tree_dr0", bloch_raw["MW_L0_tree"], bloch_raw["MZ_L0_tree"], mpf(0)),
        ("L2a_sirlin_baryon_mp", bloch_raw["MW_L2a_sirlin_mp"], bloch_raw["MZ_L2a_sirlin_mp"], bloch_raw["dr_L2a_sirlin_mp"]),
        ("L2b_sirlin_meson_2mpi", bloch_raw["MW_L2b_sirlin_2mpi"], bloch_raw["MZ_L2b_sirlin_2mpi"], bloch_raw["dr_L2b_sirlin_2mpi"]),
    ]:
        lvl_rows: dict[str, dict[str, str]] = {}
        for c_key, c_desc, cl in c_loops:
            mh_w = mw_val * (tp4 / tp2) * (mpf(6) / mpf(5)) * (q2 / two) * cl
            mh_z = mz_val * (tp4 / tp3) * (mpf(6) / mpf(5)) * (two / q2) * cl
            spread = fabs(mh_w - mh_z)
            if spread > max_wz_spread_gev:
                max_wz_spread_gev = spread
            lam_from_vev = (mh_w ** 2) / (two * (bloch_raw["v_weak_gev"] ** 2))
            lam_scale_free = (
                mp.pi
                * bloch_raw["alpha_em_0"]
                / (two * bloch_raw["sin2_thetaW_planch"] * (one - dr_val))
            ) * (((tp4 / tp2) * (mpf(6) / mpf(5)) * (q2 / two) * cl) ** 2)
            lam_diff = fabs(lam_from_vev - lam_scale_free)
            if lam_diff > max_lam_vev_diff:
                max_lam_vev_diff = lam_diff
            lvl_rows[c_key] = {
                "loop_factor_desc": c_desc,
                "loop_factor": fmt(cl, OUT_DPS),
                "m_H_from_derived_MW_GeV": fmt(mh_w, OUT_DPS),
                "m_H_from_derived_MZ_GeV": fmt(mh_z, OUT_DPS),
                "W_vs_Z_anchor_spread_GeV": fmt(spread, 25),
                "m_H_rel_err_pct": fmt((mh_w - PDG_MH_GEV) / PDG_MH_GEV * mpf(100), OUT_DPS),
                "m_H_err_sigma": fmt((mh_w - PDG_MH_GEV) / PDG_MH_SIG_GEV, OUT_DPS),
                "lambda_H_quartic": fmt(lam_from_vev, OUT_DPS),
                "lambda_H_vev_cancel_residual": fmt(lam_diff, 25),
                "lambda_H_rel_err_pct": fmt((lam_from_vev - pdg_lam_h) / pdg_lam_h * mpf(100), OUT_DPS),
            }
        higgs_reconciled[lvl_key] = lvl_rows

    # Central finite-difference Fréchet-Jacobian log-sensitivities `S_x(O) = d ln O / d ln x`
    # at step `eps = 10^{-40}` inside 125-dps arithmetic:
    eps = mpf(10) ** (-40)
    q_hi = _evaluate_chain_raw(qv * (one + eps), me_gev, mpi_gev, True)
    q_lo = _evaluate_chain_raw(qv * (one - eps), me_gev, mpi_gev, True)
    me_hi = _evaluate_chain_raw(qv, me_gev * (one + eps), mpi_gev, True)
    me_lo = _evaluate_chain_raw(qv, me_gev * (one - eps), mpi_gev, True)
    pi_hi = _evaluate_chain_raw(qv, me_gev, mpi_gev * (one + eps), True)
    pi_lo = _evaluate_chain_raw(qv, me_gev, mpi_gev * (one - eps), True)

    jac_keys = [
        "v_weak_gev",
        "sin2_thetaW_planch",
        "MW_L2a_sirlin_mp",
        "MZ_L2a_sirlin_mp",
        "MW_L2b_sirlin_2mpi",
        "MZ_L2b_sirlin_2mpi",
        "mH_L2a_tree",
        "mH_L2a_habiro_half",
        "lambda_H_L2a_tree",
    ]
    jacobian_budget: dict[str, dict[str, str]] = {}
    for jk in jac_keys:
        v0 = bloch_raw[jk]
        s_q = (q_hi[jk] - q_lo[jk]) / (two * eps * v0)
        s_me = (me_hi[jk] - me_lo[jk]) / (two * eps * v0)
        s_pi = (pi_hi[jk] - pi_lo[jk]) / (two * eps * v0)
        rel_sig_tot = sqrt(
            (s_q * rel_sigma_q) ** 2
            + (s_me * rel_sigma_me) ** 2
            + (s_pi * rel_sigma_mpi) ** 2
        )
        jacobian_budget[jk] = {
            "d_ln_O_d_ln_q0": fmt(s_q, 40),
            "d_ln_O_d_ln_me": fmt(s_me, 40),
            "d_ln_O_d_ln_mpi": fmt(s_pi, 40),
            "propagated_rel_sigma_ppb": fmt(rel_sig_tot * (mpf(10) ** 9), 40),
            "propagated_abs_sigma": fmt(rel_sig_tot * fabs(v0), 40),
        }

    def _boson_summary(raw: dict[str, mpf]) -> dict[str, dict[str, str]]:
        out = {}
        for tag, dr_k, mw_k, mz_k in [
            ("L0_tree_dr0", None, "MW_L0_tree", "MZ_L0_tree"),
            ("L1a_self_consistent_leptonic_VP", "dr_L1a_lept", "MW_L1a_lept", "MZ_L1a_lept"),
            ("L1b_self_consistent_full_QED_VP_no_custodial", "dr_L1b_qed_vp", "MW_L1b_qed_vp", "MZ_L1b_qed_vp"),
            ("L2a_self_consistent_Sirlin_1loop_baryon_mp", "dr_L2a_sirlin_mp", "MW_L2a_sirlin_mp", "MZ_L2a_sirlin_mp"),
            ("L2b_self_consistent_Sirlin_1loop_meson_2mpi", "dr_L2b_sirlin_2mpi", "MW_L2b_sirlin_2mpi", "MZ_L2b_sirlin_2mpi"),
        ]:
            dr_v = mpf(0) if dr_k is None else raw[dr_k]
            mw_v = raw[mw_k]
            mz_v = raw[mz_k]
            out[tag] = {
                "Delta_r_self_consistent": fmt(dr_v, OUT_DPS),
                "MW_pred_GeV": fmt(mw_v, OUT_DPS),
                "MW_rel_err_pct": fmt((mw_v - PDG_MW_GEV) / PDG_MW_GEV * mpf(100), OUT_DPS),
                "MW_err_sigma": fmt((mw_v - PDG_MW_GEV) / PDG_MW_SIG_GEV, OUT_DPS),
                "MZ_pred_GeV": fmt(mz_v, OUT_DPS),
                "MZ_rel_err_pct": fmt((mz_v - PDG_MZ_GEV) / PDG_MZ_GEV * mpf(100), OUT_DPS),
                "MZ_err_sigma": fmt((mz_v - PDG_MZ_GEV) / PDG_MZ_SIG_GEV, OUT_DPS),
                "custodial_rho_pred": fmt((mw_v ** 2) / ((mz_v ** 2) * raw["cos2_thetaW_planch"]), OUT_DPS),
            }
        return out

    return {
        "anchor": anchor_name,
        "q0": fmt(qv, OUT_DPS),
        "derived_mp_GeV": fmt(bloch_raw["mp_derived_gev"], OUT_DPS),
        "derived_mp_vs_CODATA_ppb": fmt(
            (bloch_raw["mp_derived_gev"] - (M_P_MEV_VALIDATION / mpf(1000)))
            / (M_P_MEV_VALIDATION / mpf(1000))
            * (mpf(10) ** 9),
            40,
        ),
        "derived_mmu_GeV": fmt(bloch_raw["mmu_derived_gev"], OUT_DPS),
        "v_weak_GeV": fmt(bloch_raw["v_weak_gev"], OUT_DPS),
        "v_weak_vs_PDG_ppb": fmt(
            (bloch_raw["v_weak_gev"] - pdg_vew) / pdg_vew * (mpf(10) ** 9), 40
        ),
        "v_weak_vs_PDG_sigma": fmt((bloch_raw["v_weak_gev"] - pdg_vew) / pdg_vew_sig, 40),
        "alpha_EM_inv_0_BlochB3": fmt(bloch_raw["alpha_em_inv_0"], OUT_DPS),
        "alpha_EM_inv_0_FormB": fmt(formb_raw["alpha_em_inv_0"], OUT_DPS),
        "A0_tree_GeV_BlochB3": fmt(bloch_raw["A0_tree_gev"], OUT_DPS),
        "A0_tree_GeV_FormB": fmt(formb_raw["A0_tree_gev"], OUT_DPS),
        "r_ZW_dressed": fmt(bloch_raw["r_zw_dressed"], OUT_DPS),
        "r_ZW_vs_PDG_ppm": fmt(
            (bloch_raw["r_zw_dressed"] - (PDG_MZ_GEV / PDG_MW_GEV))
            / (PDG_MZ_GEV / PDG_MW_GEV)
            * (mpf(10) ** 6),
            40,
        ),
        "sin2_thetaW_plancherel_dressed": fmt(bloch_raw["sin2_thetaW_planch"], OUT_DPS),
        "sin2_thetaW_onshell_PDG": fmt(pdg_onshell_s2, OUT_DPS),
        "weinberg_candidates_side_by_side": weinberg_arms,
        "boson_thresholds_BlochB3_alphaEM": _boson_summary(bloch_raw),
        "boson_thresholds_FormB_alphaEM": _boson_summary(formb_raw),
        "higgs_anchor_reconciled_BlochB3": higgs_reconciled,
        "max_W_vs_Z_higgs_spread_GeV": fmt(max_wz_spread_gev, 25),
        "max_lambda_H_vev_cancel_residual": fmt(max_lam_vev_diff, 25),
        "frechet_jacobian_uncertainty_budget": jacobian_budget,
    }


def main() -> int:
    one = mpf(1)
    q_proton = q_at(WORK_DPS)
    q_muon = q_muon_at(WORK_DPS)

    me_gev = M_E_MEV / mpf(1000)
    rel_sig_me = M_E_MEV_ERR / M_E_MEV
    mpi_gev = M_PI_PM_MEV_VALIDATION / mpf(1000)
    rel_sig_mpi = M_PI_PM_ERR_MEV / M_PI_PM_MEV_VALIDATION

    # Relative q_0 uncertainties from NIST CODATA-2022 mass ratios
    pe_rec = _codata.codata("proton-electron mass ratio")
    mue_rec = _codata.codata("muon-electron mass ratio")
    rel_sig_qp = (mpf(pe_rec.uncertainty_str) / mpf(pe_rec.value_str)) / mpf("20.9970")
    rel_sig_qmu = (mpf(mue_rec.uncertainty_str) / mpf(mue_rec.value_str)) / mpf("20.1983")

    proton_res = evaluate_anchor_full(
        "proton", q_proton, rel_sig_qp, me_gev, rel_sig_me, mpi_gev, rel_sig_mpi
    )
    muon_res = evaluate_anchor_full(
        "muon", q_muon, rel_sig_qmu, me_gev, rel_sig_me, mpi_gev, rel_sig_mpi
    )

    # Exact verification of Lean algebraic theorems at 125 dps:
    hv_p = q_proton - one / q_proton
    q2_p = _qbal(2, q_proton)
    gap_lhs = _two_mul_p(3, hv_p) * (q2_p ** 2) - _two_mul_p(2, hv_p) * mpf(4)
    gap_rhs = (hv_p ** 2) * (
        mpf(13) + mpf(22) * (hv_p ** 2) + mpf(9) * (hv_p ** 4) + (hv_p ** 6)
    )
    zw_gap_poly_err = fabs(gap_lhs - gap_rhs)

    tp2_p = _two_mul_p(2, hv_p)
    tp3_p = _two_mul_p(3, hv_p)
    cos2_p = ((tp2_p * mpf(4)) ** 2) / ((tp3_p * (q2_p ** 2)) ** 2)
    sin2_p = one - cos2_p
    cot2_p = ((tp2_p * mpf(4)) ** 2) / (((tp3_p * (q2_p ** 2)) ** 2) - ((tp2_p * mpf(4)) ** 2))
    cot_bridge_err = fabs(sin2_p * (one + cot2_p) - one)

    # PDG experimental entropy / digit budget across {v_weak, M_W, M_Z, m_H}
    pdg_vew = one / sqrt(sqrt(mpf(2)) * PDG_GF_GEV_INV2)
    pdg_vew_sig = pdg_vew * PDG_GF_SIG_GEV_INV2 / (mpf(2) * PDG_GF_GEV_INV2)
    digits_vew = -log10(pdg_vew_sig / pdg_vew)
    digits_mw = -log10(PDG_MW_SIG_GEV / PDG_MW_GEV)
    digits_mz = -log10(PDG_MZ_SIG_GEV / PDG_MZ_GEV)
    digits_mh = -log10(PDG_MH_SIG_GEV / PDG_MH_GEV)
    total_ew_exp_digits = digits_vew + digits_mw + digits_mz + digits_mh

    wb = WitnessBuilder("electroweak-mw-mz-weinberg-higgs", engine="mpmath")
    wb.set_content_block("prose:sm-params-higgs")
    wb.set_description(
        "80-dps zero-parameter evaluation of QOU electroweak gauge-boson thresholds (M_W, M_Z), "
        "Weinberg angle candidates, anchor-reconciled Higgs mass m_H (|m_H^(W) - m_H^(Z)| = 0), "
        "and v-independent Higgs quartic lambda_H atop QOU-derived (v_weak(q_0), alpha_EM(q_0)) "
        "at both proton and muon q_0 anchors (companion to "
        "QOU/StandardModel/ElectroweakBosonThresholdsAndWeinberg.lean)."
    )
    wb.add_parameter("work_dps", WORK_DPS)
    wb.add_parameter("output_dps", OUT_DPS)
    wb.add_parameter("fitted_parameters", 0)

    wb.add_data("proton_anchor_evaluation", proton_res)
    wb.add_data("muon_anchor_evaluation", muon_res)
    wb.add_data(
        "pdg_entropy_and_epistemic_ledger",
        {
            "PDG_v_weak_digits": fmt(digits_vew, 25),
            "PDG_MW_digits": fmt(digits_mw, 25),
            "PDG_MZ_digits": fmt(digits_mz, 25),
            "PDG_mH_digits": fmt(digits_mh, 25),
            "total_electroweak_experimental_digits": fmt(total_ew_exp_digits, 25),
            "electroweak_fitted_parameters": 0,
            "lean_module": "folio/quantum-observable-universe/lean/QOU/StandardModel/ElectroweakBosonThresholdsAndWeinberg.lean",
            "unconditional_theorems": [
                "plancherel_zw_gap_poly_eq",
                "plancherel_zw_gap_laurent_eq",
                "plancherel_classical_unbroken_limit",
                "plancherel_sinSq_cotSq_bridge",
                "derived_mwSq_div_mzSq_eq_cosSq_mul_rho",
                "custodial_rho_one_iff_onshell_sinSq",
                "derived_higgs_w_eq_z_zero_spread",
                "derived_higgs_quartic_vev_independent",
                "plancherel_sinSq_mem_unit_interval",
                "derived_higgs_quartic_pos_and_vacuum_stable",
            ],
            "conditional_class_3b_cond": "ElectroweakBosonThresholdSystemClass (0 global instances; def trivialModel consistency witness)",
        },
    )

    wb.add_assertion(
        name="plancherel_zw_gap_polynomial_identity_exact",
        computed=fmt(zw_gap_poly_err, 25),
        expected="0",
        tolerance="1e-110",
        source="ElectroweakBosonThresholdsAndWeinberg.plancherel_zw_gap_laurent_eq",
    )
    wb.add_assertion(
        name="plancherel_sinSq_cotSq_bridge_exact",
        computed=fmt(cot_bridge_err, 25),
        expected="0",
        tolerance="1e-110",
        source="ElectroweakBosonThresholdsAndWeinberg.plancherel_sinSq_cotSq_bridge",
    )
    wb.add_assertion(
        name="plancherel_sinSq_strictly_inside_unit_interval",
        computed="1" if (mpf(0) < sin2_p < one) else "0",
        expected="1",
        tolerance="0",
        source="ElectroweakBosonThresholdsAndWeinberg.plancherel_sinSq_mem_unit_interval",
    )
    wb.add_assertion(
        name="derived_higgs_w_z_anchor_spread_identically_zero",
        computed=proton_res["max_W_vs_Z_higgs_spread_GeV"],
        expected="0",
        tolerance="1e-105",
        source="ElectroweakBosonThresholdsAndWeinberg.derived_higgs_w_eq_z_zero_spread",
    )
    wb.add_assertion(
        name="derived_higgs_quartic_vev_independence_exact",
        computed=proton_res["max_lambda_H_vev_cancel_residual"],
        expected="0",
        tolerance="1e-110",
        source="ElectroweakBosonThresholdsAndWeinberg.derived_higgs_quartic_vev_independent",
    )

    wb.add_caveat(
        "Epistemic & physical boundary: (1) All algebraic identities in "
        "ElectroweakBosonThresholdsAndWeinberg.lean are unconditional over [CommRing R] / [Field K], "
        "while the physical Bring-Schwinger fixed-point couplings and radiative threshold matching "
        "live inside §3b-cond ElectroweakBosonThresholdSystemClass (0 global instances). "
        "(2) Self-consistent 1-loop Sirlin thresholds straddle PDG (M_W = 80.3692 GeV, "
        "M_Z = 91.1876 GeV) between QOU's baryonic threshold mu_had = m_p(q_0) "
        "(M_W = 80.2471 GeV [-0.152%], M_Z = 91.0650 GeV [-0.134%]) and mesonic pair threshold "
        "mu_had = 2*m_pi (M_W = 80.5362 GeV [+0.208%], M_Z = 91.3931 GeV [+0.225%]), reflecting "
        "non-perturbative rho-resonance dispersion in Delta alpha_had^(5)(M_Z) and 2-loop EW "
        "corrections rather than any fitted parameter. (3) The H_6 Hoefsmit pure-pattern Weinberg "
        "automorphism (bean qou-zd6l, cot theta_W = q_0^-4 -> sin^2 theta_W = 0.6973) and the "
        "categorical Goldstone-linking functor (beans qou-ukqh, qou-z3x8) remain open."
    )

    wb.set_audit_only("docs/audits/2026-11-24-electroweak-mw-mz-weinberg-higgs-80dps-audit.md")
    out_path = wb.save(
        q0_comparison(
            muon=fmt(q_muon, OUT_DPS),
            proton=fmt(q_proton, OUT_DPS),
            reason=(
                "evaluates coupled electroweak thresholds (M_W, M_Z, sin^2 theta_W, m_H, lambda_H) "
                "from pure (m_e, q_0, m_pi) inputs at both proton and muon q_0 anchors"
            ),
        )
    )

    print("=" * 96)
    print("QOU ELECTROWEAK THRESHOLDS (M_W, M_Z, sin^2 theta_W, m_H, lambda_H) — 80-DPS ZERO-FIT PROBE")
    print("=" * 96)
    for res in (proton_res, muon_res):
        print(f"[Anchor: {res['anchor'].upper()}] q0 = {res['q0'][:26]}...")
        print(f"  m_p(q0) derived = {res['derived_mp_GeV'][:16]} GeV ({res['derived_mp_vs_CODATA_ppb'][:10]} ppb vs CODATA)")
        print(f"  v_weak(q0)      = {res['v_weak_GeV'][:16]} GeV ({res['v_weak_vs_PDG_ppb'][:10]} ppb, {res['v_weak_vs_PDG_sigma'][:8]} sigma)")
        print(f"  1/alpha_EM(0)   = {res['alpha_EM_inv_0_BlochB3'][:18]} (Bloch-B3) | {res['alpha_EM_inv_0_FormB'][:18]} (Form-B)")
        print(f"  sin^2_Planch    = {res['sin2_thetaW_plancherel_dressed'][:14]} (r_ZW = {res['r_ZW_dressed'][:14]}, {res['r_ZW_vs_PDG_ppm'][:9]} ppm)")
        for b_tag, b_row in res["boson_thresholds_BlochB3_alphaEM"].items():
            print(
                f"    {b_tag:<46} dr={b_row['Delta_r_self_consistent'][:10]} | "
                f"MW={b_row['MW_pred_GeV'][:10]} ({b_row['MW_rel_err_pct'][:8]}%) | "
                f"MZ={b_row['MZ_pred_GeV'][:10]} ({b_row['MZ_rel_err_pct'][:8]}%)"
            )
        print(f"  Max |m_H^(W) - m_H^(Z)| spread = {res['max_W_vs_Z_higgs_spread_GeV']} GeV")
        for c_key, h_row in res["higgs_anchor_reconciled_BlochB3"]["L2a_sirlin_baryon_mp"].items():
            print(
                f"    [L2a {c_key:<20}] m_H={h_row['m_H_from_derived_MW_GeV'][:11]} GeV "
                f"({h_row['m_H_rel_err_pct'][:8]}%, {h_row['m_H_err_sigma'][:7]} sig) | "
                f"lam_H={h_row['lambda_H_quartic'][:12]}"
            )
        print()
    print(f"PDG EW digit budget (v, MW, MZ, mH) = {fmt(total_ew_exp_digits, 8)} digits (0 EW fits)")
    print(f"Witness -> {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
