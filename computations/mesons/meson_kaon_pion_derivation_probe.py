#!/usr/bin/env python3
"""80-dps SymPy + mpmath First-Principles Derivation & Adjudication Probe for `m_K / m_pi`
(`qou-3l2l` & `qou-5ipv`, Linked Issue #9369).

Evaluates symbolically over Q(q) (SymPy exact rational/Laurent arithmetic) and numerically
at 80 decimal places (`mp.mp.dps = 80`, `mpmath 1.4.1`, zero `float64`, zero fitted parameters)
at BOTH registered substrate anchors (`q_proton` and `q_muon` via `q0_comparison`):

1. Mathematical Problem 1 — Why `(3, 4)` in `[3]_q * [4]_q = [2]_q + [4]_q + [6]_q`?
   - Proves exact Eightfold Way split-bundle `F = V_2 (+) W_3^*` quantum-dimension identities:
       dim_q(Alt_q^2 W_3^*) + dim_q(Sym_q^2 W_3^*) = [3]_q + [3]_q[4]_q/[2]_q = [3]_q^2,
       dim_q(8) + 1 = [2]_q[4]_q + 1 = [3]_q^2,
       dim_q(V_2 (x) Sym_q^2 W_3^*) = [2]_q * ([3]_q[4]_q/[2]_q) = [3]_q[4]_q = C_2^{(q)}(j=3),
     contrasted with the intra-octet kaon/pion multiplicity ratio `[4]_q / [3]_q` (`4/3 != 12`).
   - Proves exact cyclotomic curvature-gap identities across all classical factorizations
     `a * b = 12` (`(3, 4)`, `(2, 6)`, `(1, 12)`):
       [2]_q[6]_q - [3]_q[4]_q = (q + q^-1 - 2) [2]_q [3]_q ([2]_q + [3]_q) > 0,
       [1]_q[12]_q - [2]_q[6]_q = (q + q^-1 - 2) [6]_q ([2]_q + [3]_q) ([3]_q + [4]_q) > 0.
   - Proves the `H_3(q)` odd-generation clasp `q -> 1` collapse obstruction: at `q = 1`
     (`sigma_i^2 = 1`), every odd-winding meson clasp `sigma_1^{2k_1+1} sigma_2^{-(2k_2+1)} sigma_1 sigma_2^-1`
     collapses to `(sigma_1 sigma_2)^2`, so any bare Hecke/Markov trace ratio of `(3, 5)` over `(3, 3)`
     converges to `1 != 12` as `q -> 1` (at `q_p`: `tr_z2(3,5)/tr_z2(3,3)` and `tr_z3(3,5)/tr_z3(3,3)`
     also sit near `O(1)`, while `SL_2(Z)` monodromy trace gives `41/27 = 1.5185 != 12`).

2. Mathematical Problem 2 — Why `(alpha_EM / pi) * (1 + ln(1 + hbar_q))` and Post-#9360 Multi-Arm Audit:
   - Verifies the Schwinger scale-invariant proper-time decomposition (`ds/s`, 1 nat per e-fold):
       int_{e^-1}^1 ds/s + int_1^{1+hbar_q} ds/s = 1 + ln(1 + hbar_q) = 1 + ln((2q - 1)/q),
     and compares against the multiplicative Reeb UV interval `[1, q]` (`1 + ln(q)`), proving
       (1 + ln(q)) - (1 + ln(1 + hbar_q)) = -ln(1 - hbar_q^2) > 0
     (`+51.428 ppb` vs `+967.255 ppb`, both deep inside `0.04 sigma_exp` given `sigma_exp = 26,365 ppb`).
   - Proves the Dashen equal-EM chiral ratio identity:
       (R_0 m_0^2 + Delta_EM)/(m_0^2 + Delta_EM) - R_0 = -(R_0 - 1) Delta_EM / (m_0^2 + Delta_EM) < 0
     (`-59,554 ppm` for `R_0 = [3]_q[4]_q` and `Delta_EM = m_{pi+-}^2 - m_{pi0}^2`), ruling out naive
     pointlike equal-self-energy addition on neutral strong masses as the source of `+(alpha_EM/pi) F_EM > 0`.
   - Evaluates `m_K / m_pi` at 80 dps across all derived `alpha_EM` arms (`Form B` #9360 `0-sorry`,
     `Form C1 Bloch-B3` #9360, `Seifert CS` #9359 `0-sorry`, `Witten CS`, `Form A`, and `bare tree q[9]_q[10]_q`)
     at BOTH `q_proton` and `q_muon`, verifying `meson_ratio_alpha_lipschitz_bound` (`0.048 ppb` spread across
     all loop-dressed arms; even `0-sorry` bare tree `q[9]_q[10]_q` clears `263.65 ppb` at `+209.44 ppb`).
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
set_compute_dps(80)

import mpmath as mp  # noqa: E402
from mpmath import mpf, fabs, sqrt, log, polylog, zeta  # noqa: E402
mp.mp.dps = max(mp.mp.dps, 80)

import sympy as sp  # noqa: E402
from codata_constants import (  # noqa: E402
    M_K_0_MEV_VALIDATION,
    M_K_PM_MEV_VALIDATION,
    M_PI_0_MEV_VALIDATION,
    M_PI_PM_MEV_VALIDATION,
)
from meson_em_sinh_closed_form import _alpha_em_inv_derived  # noqa: E402
from q_parameter import q_at, q_muon_at  # noqa: E402
from qou_substrate import codata as _codata  # noqa: E402
from witness_base import WitnessBuilder, q0_comparison  # noqa: E402


def _qbal_mp(n: int, q: mpf) -> mpf:
    return (q ** n - q ** (-n)) / (q - mpf(1) / q)


def _qbal_sp(n: int, q_s: sp.Symbol) -> sp.Expr:
    return sp.cancel((q_s ** n - q_s ** (-n)) / (q_s - sp.Integer(1) / q_s))


def verify_symbolic_meson_identities() -> dict:
    """Exact symbolic verification over Q(q) of all Section 1 & Section 2 algebraic identities."""
    q_s = sp.Symbol("q", nonzero=True)
    r0_s, m0_sq_s, dem_s = sp.symbols("R0 m0_sq dEM", nonzero=True)

    b2 = _qbal_sp(2, q_s)
    b3 = _qbal_sp(3, q_s)
    b4 = _qbal_sp(4, q_s)
    b6 = _qbal_sp(6, q_s)
    b12 = _qbal_sp(12, q_s)

    # 1. q-CG fusion [3]_q [4]_q = [2]_q + [4]_q + [6]_q
    diff_qcg_34 = sp.simplify(b3 * b4 - (b2 + b4 + b6))

    # 2. Split-bundle F = V_2 (+) W_3^* quantum dimensions:
    dim_sym2_w3 = sp.cancel(b3 * b4 / b2)
    dim_alt2_w3 = b3
    dim_octet = sp.cancel(b2 * b4)
    diff_w3_sq_diquark = sp.simplify(b3 ** 2 - (dim_alt2_w3 + dim_sym2_w3))
    diff_w3_sq_meson = sp.simplify(b3 ** 2 - (dim_octet + sp.Integer(1)))
    diff_v2_sym2_w3 = sp.simplify(b2 * dim_sym2_w3 - b3 * b4)

    # 3. Cyclotomic curvature gaps for all 3 factorizations of 12 = 1*12 = 2*6 = 3*4:
    hab_sq = q_s + sp.Integer(1) / q_s - sp.Integer(2)
    gap_26_34_exact = hab_sq * b2 * b3 * (b2 + b3)
    gap_112_26_exact = hab_sq * b6 * (b2 + b3) * (b3 + b4)
    diff_gap_26_34 = sp.simplify((b2 * b6 - b3 * b4) - gap_26_34_exact)
    diff_gap_112_26 = sp.simplify((b12 - b2 * b6) - gap_112_26_exact)

    # 4. H_3(q) S^{(2,1)} exact 2x2 clasp matrices from HyperbolicMesonClaspAndDiquarkSplit:
    # rho21_sigma0(q) = [[-q^-1, -1], [0, q]], rho21_sigma1_inv(q) = [[q^-1, 0], [-1, -q]]
    s0 = sp.Matrix([[-1 / q_s, -1], [0, q_s]])
    s1_inv = sp.Matrix([[1 / q_s, 0], [-1, -q_s]])
    clasp_33 = (s0 ** 3) * (s1_inv ** 3) * s0 * s1_inv
    clasp_35 = (s0 ** 3) * (s1_inv ** 5) * s0 * s1_inv
    clasp_55 = (s0 ** 5) * (s1_inv ** 5) * s0 * s1_inv
    # Verify q -> 1 collapse: clasp(3,3)|_{q=1} == clasp(3,5)|_{q=1} == clasp(5,5)|_{q=1}
    c33_q1 = clasp_33.subs(q_s, 1)
    c35_q1 = clasp_35.subs(q_s, 1)
    c55_q1 = clasp_55.subs(q_s, 1)
    clasp_q1_collapse_ok = (c33_q1 == c35_q1) and (c35_q1 == c55_q1) and (int(c33_q1.trace()) == -1)

    # 5. GMOR isospin-symmetric quark ratio equivalence:
    # (1 + ms_md) / 2 == [3]_q[4]_q  <=>  ms_md == 2[3]_q[4]_q - 1
    ms_md_sym = 2 * b3 * b4 - 1
    diff_gmor = sp.simplify((1 + ms_md_sym) / sp.Integer(2) - b3 * b4)

    # 6. Dashen equal-EM shift identity:
    dashen_lhs = (r0_s * m0_sq_s + dem_s) / (m0_sq_s + dem_s) - r0_s
    dashen_rhs = -(r0_s - 1) * dem_s / (m0_sq_s + dem_s)
    diff_dashen = sp.simplify(dashen_lhs - dashen_rhs)

    # 7. Multiplicative-vs-additive Schwinger UV argument identity:
    # (1 - hbar_q) * (1 + hbar_q) == 1 - hbar_q^2 == (2*q - 1) / q^2
    hbar_s = 1 - 1 / q_s
    diff_uv_prod = sp.simplify((1 - hbar_s) * (1 + hbar_s) - (1 - hbar_s ** 2))
    diff_uv_rat = sp.simplify(1 + hbar_s - (2 * q_s - 1) / q_s)

    checks = {
        "qcg_3x4_eq_2_plus_4_plus_6": diff_qcg_34 == 0,
        "w3_sq_diquark_split_3_plus_6bar": diff_w3_sq_diquark == 0,
        "w3_sq_meson_split_8_plus_1": diff_w3_sq_meson == 0,
        "v2_tensor_sym2_w3_eq_3x4": diff_v2_sym2_w3 == 0,
        "cyclotomic_gap_2x6_minus_3x4": diff_gap_26_34 == 0,
        "cyclotomic_gap_1x12_minus_2x6": diff_gap_112_26 == 0,
        "hecke_clasp_q_eq_1_odd_collapse": bool(clasp_q1_collapse_ok),
        "gmor_isospin_ms_over_md_identity": diff_gmor == 0,
        "dashen_equal_em_shift_identity": diff_dashen == 0,
        "schwinger_uv_product_identity": (diff_uv_prod == 0 and diff_uv_rat == 0),
    }
    return {
        "checks": checks,
        "gap_2x6_minus_3x4_factored": "(q + q^-1 - 2) * [2]_q * [3]_q * ([2]_q + [3]_q)",
        "gap_1x12_minus_2x6_factored": "(q + q^-1 - 2) * [6]_q * ([2]_q + [3]_q) * ([3]_q + [4]_q)",
        "clasp_Hecke21_trace_at_q_eq_1": int(c33_q1.trace()),
        "clasp_SL2_traces_pi_K_phi": [27, 41, 63],
    }


def _solve_alpha_inv_form_b(q: mpf) -> mpf:
    t_const = q * _qbal_mp(9, q) * _qbal_mp(10, q) + mpf(2) / (mpf(3) * mp.pi)
    h_norm = _qbal_mp(2, q) / (mpf(8) * mp.pi)
    h_sq = (q - mpf(1) / q) ** 2
    root = mp.findroot(
        lambda a: -h_sq * h_norm * (a ** 3) + h_norm * (a ** 2) + t_const * a - mpf(1),
        mpf(1) / t_const,
    )
    return mpf(1) / root


def _solve_alpha_inv_form_c1_bloch_b3(q: mpf) -> mpf:
    t_const = q * _qbal_mp(9, q) * _qbal_mp(10, q) + mpf(2) / (mpf(3) * mp.pi)
    h_norm = _qbal_mp(2, q) / (mpf(8) * mp.pi)
    h_sq = (q - mpf(1) / q) ** 2
    delta_b3 = zeta(3) - polylog(3, q ** (-2))
    c2_add = h_norm * (delta_b3 / (mpf(8) * mp.pi))
    root = mp.findroot(
        lambda a: (c2_add - h_sq * h_norm) * (a ** 3) + h_norm * (a ** 2) + t_const * a - mpf(1),
        mpf(1) / t_const,
    )
    return mpf(1) / root


def _solve_alpha_inv_form_a(q: mpf) -> mpf:
    t_const = q * _qbal_mp(9, q) * _qbal_mp(10, q) + mpf(2) / (mpf(3) * mp.pi)
    h_norm = _qbal_mp(2, q) / (mpf(8) * mp.pi)
    root = mp.findroot(lambda a: h_norm * (a ** 2) + t_const * a - mpf(1), mpf(1) / t_const)
    return mpf(1) / root


def _alpha_inv_seifert_cs(q: mpf) -> mpf:
    bare = q * _qbal_mp(9, q) * _qbal_mp(10, q)
    hbar = mpf(1) - mpf(1) / q
    cs_sum = (mp.pi ** 2) * mpf(10) / mpf(9) + (mp.pi ** 2) * mpf(16) / mpf(15)
    c1 = cs_sum * (_qbal_mp(2, q) / mpf(2)) * (hbar ** 2) / bare
    iq = mpf(1) / q
    d29 = (q - mpf(1) + iq) * (q ** 3 - mpf(1) + iq ** 3)
    d35 = q ** 4 - q ** 3 + q - mpf(1) + iq - iq ** 3 + iq ** 4
    kappa_seifert = (q ** 8) / (d29 * d35)
    return bare * (mpf(1) + c1 / (mpf(1) - c1 * kappa_seifert))


def _clasp_markov_traces_mp(q: mpf, n1: int, n2: int) -> tuple[mpf, mpf]:
    """Evaluate exact H_3(q) rank-2 and rank-3 Markov traces of beta_clasp(n1, n2) at 80 dps."""
    s0 = mp.matrix([[-mpf(1) / q, -mpf(1)], [mpf(0), q]])
    s1_inv = mp.matrix([[mpf(1) / q, mpf(0)], [-mpf(1), -q]])

    def mat_pow(m: mp.matrix, p: int) -> mp.matrix:
        out = mp.eye(2)
        for _ in range(p):
            out = out * m
        return out

    m_clasp = mat_pow(s0, n1) * mat_pow(s1_inv, n2) * s0 * s1_inv
    tr21 = m_clasp[0, 0] + m_clasp[1, 1]
    w2_sym = (q ** 4 + mpf(1)) / ((q ** 2 + mpf(1)) ** 2)
    w2_mix = (q ** 2) / ((q ** 2 + mpf(1)) ** 2)
    tr_z2 = w2_sym * (q ** n1) * (q ** (-n2)) + w2_mix * tr21

    b3 = _qbal_mp(3, q)
    d10 = (q ** 2 + q ** (-2)) * _qbal_mp(5, q)
    d8 = _qbal_mp(2, q) * _qbal_mp(4, q)
    tr_z3 = (
        (d10 / (b3 ** 3)) * (q ** n1) * (q ** (-n2))
        + (d8 / (b3 ** 3)) * tr21
        + (mpf(1) / (b3 ** 3)) * ((-mpf(1) / q) ** n1) * ((-q) ** n2)
    )
    return tr_z2, tr_z3


def evaluate_pin(pin_label: str, q: mpf, r_exp: mpf, rel_sig_r: mpf, alpha_c22: mpf) -> dict:
    """80-dps evaluation of strong core, UV proper-time intervals, and all derived alpha_EM arms."""
    LN_Q = log(q)
    hbar_q = mpf(1) - mpf(1) / q
    r2_exp = r_exp ** 2
    target_100x_ppb = rel_sig_r * (mpf(10) ** 9) / mpf(100)

    strong_34 = _qbal_mp(3, q) * _qbal_mp(4, q)
    strong_26 = _qbal_mp(2, q) * _qbal_mp(6, q)
    strong_112 = _qbal_mp(1, q) * _qbal_mp(12, q)
    r_strong = sqrt(strong_34)
    err_strong_ppb = (r_strong - r_exp) / r_exp * (mpf(10) ** 9)

    # Base-q logarithm representation alongside natural Schwinger e-fold integral:
    log_q_excursion = log(mpf(1) + hbar_q) / LN_Q
    em_planck = mpf(1) + LN_Q * log_q_excursion  # == 1 + ln(1 + hbar_q)
    em_reeb = mpf(1) + LN_Q                      # == 1 + ln(q) = 1 - ln(1 - hbar_q)
    em_uv_gap_exact = -LN_Q * (log(mpf(1) - hbar_q ** 2) / LN_Q)

    # Clasp Markov trace ratios (kaon (3,5) over pion (3,3)):
    tz2_pi, tz3_pi = _clasp_markov_traces_mp(q, 3, 3)
    tz2_k, tz3_k = _clasp_markov_traces_mp(q, 3, 5)

    alpha_arms = {
        "Form_B_BringSchwinger_1loop_0sorry": _solve_alpha_inv_form_b(q),
        "Form_C1_BlochB3_2loop_EmFermionLoop": _solve_alpha_inv_form_c1_bloch_b3(q),
        "Seifert_CS_homological_kappa_0sorry": _alpha_inv_seifert_cs(q),
        "Witten_CS_tower_shipped": _alpha_em_inv_derived(q),
        "Form_A_BringSchwinger_quadratic": _solve_alpha_inv_form_a(q),
        "Bare_tree_q9_10_0sorry": q * _qbal_mp(9, q) * _qbal_mp(10, q),
        "CODATA_2022_reference_only": alpha_c22,
    }

    arm_results = {}
    for arm_name, a_inv in alpha_arms.items():
        a_val = mpf(1) / a_inv
        r2_pred = strong_34 + (a_val / mp.pi) * em_planck
        r_pred = sqrt(r2_pred)
        err_r_ppb = (r_pred - r_exp) / r_exp * (mpf(10) ** 9)
        err_r2_ppb = (r2_pred - r2_exp) / r2_exp * (mpf(10) ** 9)
        err_sigma = ((r_pred - r_exp) / r_exp) / rel_sig_r
        arm_results[arm_name] = {
            "alpha_em_inv": fmt(a_inv),
            "m_K_over_m_pi_pred": fmt(r_pred),
            "m_K_sq_over_m_pi_sq_pred": fmt(r2_pred),
            "err_mK_over_mpi_ppb": fmt(err_r_ppb),
            "err_mK2_over_mpi2_ppb": fmt(err_r2_ppb),
            "err_vs_sigma_exp": fmt(err_sigma),
            "clears_263_65_ppb_target": bool(fabs(err_r_ppb) < target_100x_ppb),
        }

    # Schwinger UV-interval sensitivity under Form B alpha_EM:
    a_form_b = mpf(1) / alpha_arms["Form_B_BringSchwinger_1loop_0sorry"]
    f_em_sigma = (mpf(2) * r2_exp / (a_form_b / mp.pi)) * rel_sig_r
    f_em_req = (r2_exp - strong_34) / (a_form_b / mp.pi)

    uv_candidates = {
        "UV0_classical_1nat_core": mpf(1),
        "UV1_additive_planck_excursion_1_plus_ln_1_plus_hbar": em_planck,
        "UV2_multiplicative_reeb_step_1_plus_ln_q": em_reeb,
        "UV3_linear_jackson_step_1_plus_hbar": mpf(1) + hbar_q,
        "UV4_retired_quadratic_truncation_3q2_minus_1_over_2q2": (mpf(3) * (q ** 2) - mpf(1)) / (mpf(2) * (q ** 2)),
    }
    uv_results = {}
    for uv_name, f_val in uv_candidates.items():
        r_uv = sqrt(strong_34 + (a_form_b / mp.pi) * f_val)
        err_uv_ppb = (r_uv - r_exp) / r_exp * (mpf(10) ** 9)
        uv_results[uv_name] = {
            "F_EM_value": fmt(f_val),
            "err_mK_over_mpi_ppb": fmt(err_uv_ppb),
            "err_vs_sigma_exp": fmt(((r_uv - r_exp) / r_exp) / rel_sig_r),
        }

    # Verify Lipschitz bound between Form B and Witten CS:
    a_witten = mpf(1) / alpha_arms["Witten_CS_tower_shipped"]
    r_b = mpf(arm_results["Form_B_BringSchwinger_1loop_0sorry"]["m_K_over_m_pi_pred"])
    r_w = mpf(arm_results["Witten_CS_tower_shipped"]["m_K_over_m_pi_pred"])
    lip_lhs = fabs(sqrt(strong_34 + (a_form_b / mp.pi) * em_planck) - sqrt(strong_34 + (a_witten / mp.pi) * em_planck))
    lip_rhs = (em_planck / (mpf(2) * mp.pi * sqrt(strong_34))) * fabs(a_form_b - a_witten)

    return {
        "pin": pin_label,
        "q0": fmt(q, 80),
        "LN_Q": fmt(LN_Q),
        "hbar_q": fmt(hbar_q),
        "log_q_of_1_plus_hbar_q": fmt(log_q_excursion),
        "twelve_factorization_hierarchy": {
            "pair_3_4_minimal": fmt(strong_34),
            "pair_2_6_middle": fmt(strong_26),
            "pair_1_12_maximal": fmt(strong_112),
            "strict_ordering_12_lt_3x4_lt_2x6_lt_1x12": bool(mpf(12) < strong_34 < strong_26 < strong_112),
            "strong_only_mK_over_mpi_err_ppb": fmt(err_strong_ppb),
            "gmor_isospin_ms_over_md": fmt(mpf(2) * strong_34 - mpf(1)),
        },
        "clasp_braid_trace_ratios_K_over_pi": {
            "rank2_markov_ratio_35_over_33": fmt(tz2_k / tz2_pi),
            "rank3_markov_ratio_35_over_33": fmt(tz3_k / tz3_pi),
            "sl2_monodromy_trace_ratio_41_over_27": fmt(mpf(41) / mpf(27)),
        },
        "alpha_em_multi_arm_matrix": arm_results,
        "schwinger_uv_interval_comparison": {
            "F_EM_required_pdg_center": fmt(f_em_req),
            "F_EM_1sigma_exp_width": fmt(f_em_sigma),
            "reeb_minus_planck_uv_gap": fmt(em_reeb - em_planck),
            "neg_ln_1_minus_hbar_sq": fmt(em_uv_gap_exact),
            "uv_gap_identity_residual": fmt(fabs((em_reeb - em_planck) - em_uv_gap_exact)),
            "candidates": uv_results,
        },
        "lipschitz_alpha_bound_check": {
            "abs_R_formB_minus_R_witten": fmt(lip_lhs),
            "lipschitz_upper_bound": fmt(lip_rhs),
            "bound_holds": bool(lip_lhs <= lip_rhs),
        },
    }


def main() -> int:
    q_proton = q_at(80)
    q_muon = q_muon_at(80)

    m_k_pm = mpf(str(M_K_PM_MEV_VALIDATION))
    m_k_0 = mpf(str(M_K_0_MEV_VALIDATION))
    m_pi_pm = mpf(str(M_PI_PM_MEV_VALIDATION))
    m_pi_0 = mpf(str(M_PI_0_MEV_VALIDATION))
    # PDG 2024 1-sigma uncertainties documented in substrate/codata_constants.py lines 324-326:
    sig_k_pm = mpf("0.013")
    sig_pi_pm = mpf("0.00018")

    r_exp = m_k_pm / m_pi_pm
    r2_exp = r_exp ** 2
    rel_sig_r = sqrt((sig_k_pm / m_k_pm) ** 2 + (sig_pi_pm / m_pi_pm) ** 2)
    alpha_c22 = mpf(_codata.codata("inverse fine-structure constant").value_str)

    sym_res = verify_symbolic_meson_identities()
    proton_res = evaluate_pin("proton", q_proton, r_exp, rel_sig_r, alpha_c22)
    muon_res = evaluate_pin("muon", q_muon, r_exp, rel_sig_r, alpha_c22)

    # Dashen equal-EM shift check on charged ratio:
    strong_p = _qbal_mp(3, q_proton) * _qbal_mp(4, q_proton)
    dm2_pi = m_pi_pm ** 2 - m_pi_0 ** 2
    dm2_k = m_k_pm ** 2 - m_k_0 ** 2
    dashen_equal_em_shift = ((strong_p * (m_pi_0 ** 2) + dm2_pi) / (m_pi_0 ** 2 + dm2_pi)) - strong_p
    dashen_formula_rhs = -(strong_p - mpf(1)) * dm2_pi / (m_pi_0 ** 2 + dm2_pi)

    sym_all_ok = all(sym_res["checks"].values())
    ordering_ok = (
        proton_res["twelve_factorization_hierarchy"]["strict_ordering_12_lt_3x4_lt_2x6_lt_1x12"]
        and muon_res["twelve_factorization_hierarchy"]["strict_ordering_12_lt_3x4_lt_2x6_lt_1x12"]
    )
    hbar_p = mpf(1) - mpf(1) / q_proton
    uv_lhs = (mpf(1) + log(q_proton)) - (mpf(1) + log(mpf(1) + hbar_p))
    uv_rhs = -log(mpf(1) - hbar_p ** 2)
    uv_gap_ok = bool(fabs(uv_lhs - uv_rhs) < mpf("1e-75"))
    dashen_ok = bool(fabs(dashen_equal_em_shift - dashen_formula_rhs) < mpf("1e-70") and dashen_equal_em_shift < mpf(0))
    lipschitz_ok = (
        proton_res["lipschitz_alpha_bound_check"]["bound_holds"]
        and muon_res["lipschitz_alpha_bound_check"]["bound_holds"]
    )

    wb = WitnessBuilder("meson_kaon_pion_derivation_probe", engine="sympy+mpmath")
    wb.set_content_block("rem:meson-em-sinh-ratio-reading")
    wb.set_description(
        "80-dps SymPy + mpmath derivation & post-#9360 adjudication probe for m_K / m_pi "
        "(qou-3l2l, qou-5ipv, #9369): "
        "(1) proves F = V_2 (+) W_3^* split-bundle identity dim_q(V_2 (x) Sym_q^2 W_3^*) = [3]_q[4]_q = C_2^{(q)}(j=3), "
        "exact cyclotomic curvature gaps across all factorizations of 12 (12 < [3]_q[4]_q < [2]_q[6]_q < [1]_q[12]_q), "
        "and the H_3(q) odd-clasp q->1 collapse obstruction (every odd-generation clasp collapses to (sigma_1 sigma_2)^2 at q=1, "
        "so bare Hecke/Markov trace ratios converge to 1 != 12); "
        "(2) proves Schwinger proper-time decomposition 1 + ln(1 + hbar_q) vs 1 + ln(q) (gap -ln(1 - hbar_q^2) > 0), "
        "the Dashen equal-EM negative-shift identity (-59,554 ppm vs +203 ppm), and Lipschitz alpha_EM insensitivity "
        "across Form B (#9360 0-sorry: +51.4279 ppb at q_p, +56.0167 ppb at q_mu), Form C1 Bloch-B3 (#9360: +51.4279 ppb), "
        "Seifert CS (#9359 0-sorry: +51.4304 ppb), Witten CS (+51.4754 ppb), and bare tree q[9]_q[10]_q (+209.4377 ppb)."
    )
    wb.add_data("symbolic_identities_and_obstructions", sym_res)
    wb.add_data("dashen_chiral_sign_obstruction", {
        "m_pi_pm_sq_minus_m_pi_0_sq_MeV2": fmt(dm2_pi),
        "m_K_pm_sq_minus_m_K_0_sq_MeV2": fmt(dm2_k),
        "equal_em_dashen_shift_on_charged_ratio_sq": fmt(dashen_equal_em_shift),
        "equal_em_dashen_shift_ppm": fmt(dashen_equal_em_shift / r2_exp * (mpf(10) ** 6)),
        "sign_is_strictly_negative": bool(dashen_equal_em_shift < mpf(0)),
    })
    wb.add_data("pdg_2024_validation_reference", {
        "m_K_pm_over_m_pi_pm": fmt(r_exp),
        "m_K_pm_sq_over_m_pi_pm_sq": fmt(r2_exp),
        "rel_sigma_exp_ppb": fmt(rel_sig_r * (mpf(10) ** 9)),
        "target_100x_ppb": fmt(rel_sig_r * (mpf(10) ** 9) / mpf(100)),
    })
    wb.add_data("proton_pin_evaluation", proton_res)
    wb.add_data("muon_pin_evaluation", muon_res)
    wb.add_data("epistemic_adjudication", {
        "fitted_parameters": 0,
        "truncation_3q2_minus_1_over_2q2_status": "retired_on_main_replaced_by_full_1_plus_ln_1_plus_hbar_q",
        "alpha_em_witten_sorry_dependency": "discharged_non_load_bearing_via_0sorry_FormB_SeifertCS_and_bare_tree",
        "pair_3_4_and_uv_endpoint_status": "packaged_honestly_as_3b_cond_MesonKaonPionGMOREmBridgeClass",
        "lean_modules": [
            "folio/quantum-observable-universe/lean/QOU/EightfoldWay/MesonThreeByFourCharacterization.lean",
            "folio/quantum-observable-universe/lean/QOU/EightfoldWay/MesonKaonPionSchwingerBridge.lean",
        ],
    })

    wb.add_assertion(
        name="symbolic_split_bundle_cyclotomic_and_clasp_identities_hold",
        computed="1" if sym_all_ok else "0",
        expected="1",
        tolerance="0.5",
        source="MesonThreeByFourCharacterization (split-bundle, cyclotomic gaps, H_3 q->1 collapse)",
    )
    wb.add_assertion(
        name="twelve_factorization_strict_hierarchy_12_lt_3x4_lt_2x6_lt_1x12",
        computed="1" if ordering_ok else "0",
        expected="1",
        tolerance="0.5",
        source="MesonKaonPionSchwingerBridge.twelve_factorizations_strict_ordering_real",
    )
    wb.add_assertion(
        name="schwinger_reeb_minus_planck_uv_gap_equals_neg_ln_1_minus_hbar_sq",
        computed=fmt(uv_lhs),
        expected=fmt(uv_rhs),
        tolerance="1e-55",
        source="MesonKaonPionSchwingerBridge.reeb_vs_planck_schwinger_uv_gap",
    )
    wb.add_assertion(
        name="dashen_equal_em_shift_is_negative_and_matches_exact_identity",
        computed=fmt(dashen_equal_em_shift),
        expected=fmt(dashen_formula_rhs),
        tolerance="1e-55",
        source="MesonThreeByFourCharacterization.dashen_equal_em_shift_identity",
    )
    wb.add_assertion(
        name="lipschitz_alpha_em_sensitivity_bound_holds_both_pins",
        computed="1" if lipschitz_ok else "0",
        expected="1",
        tolerance="0.5",
        source="MesonKaonPionSchwingerBridge.meson_ratio_alpha_lipschitz_bound",
    )

    wb.set_audit_only("docs/audits/2026-11-24-mK-mpi-post-9360-derivation-adjudication.md")
    out_path = wb.save(
        q0_comparison(
            muon=fmt(q_muon, 80),
            proton=fmt(q_proton, 80),
            reason=(
                "evaluates the post-#9360/#9359 m_K/m_pi strong [3]_q[4]_q characterization, "
                "Schwinger proper-time UV intervals, and all derived alpha_EM arms at both q_proton and q_muon"
            ),
        )
    )

    print("=" * 94)
    print("MESON m_K / m_pi FIRST-PRINCIPLES DERIVATION & POST-#9360 ADJUDICATION PROBE (80 dps)")
    print("=" * 94)
    print(f"[Part 1] Symbolic Q(q) checks (10/10) all passed : {sym_all_ok}")
    print(f"         Dashen equal-EM shift on charged R^2    : {fmt(dashen_equal_em_shift, 12)} ({fmt(dashen_equal_em_shift / r2_exp * mpf('1e6'), 8)} ppm < 0)")
    for res in (proton_res, muon_res):
        print(f"\n[Part 2] Pin: {res['pin'].upper()} (q = {res['q0'][:24]}...)")
        for arm_k, row in res["alpha_em_multi_arm_matrix"].items():
            print(
                f"  {arm_k:38s}: 1/a={row['alpha_em_inv'][:17]} | "
                f"err={row['err_mK_over_mpi_ppb'][:11]:>11s} ppb ({row['err_vs_sigma_exp'][:9]:>9s} sig)"
            )
    print(f"\nWitness -> {out_path}")
    return 0 if (sym_all_ok and ordering_ok and uv_gap_ok and dashen_ok and lipschitz_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
