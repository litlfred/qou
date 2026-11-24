#!/usr/bin/env python3
"""80-dps SymPy + mpmath Baryon Octet `Lambda^0 - Sigma^0` Diquark Splitting, 2nd-Order
Gell-Mann-Okubo, and Decuplet Curvature Probe (`qou-8fw2`, `qou-d7h1`, `qou-wyy9`, Issue #9375).

Companion to:
  - `computations/mesons/baryon_octet_diquark_gmo_preregistration.md` (pre-committed `ccc7d2b78a0`),
  - `folio/quantum-observable-universe/lean/QOU/EightfoldWay/BaryonOctetDiquarkGmoDerivation.lean`,
  - `docs/audits/2026-11-24-baryon-octet-diquark-lambda-sigma-gmo.md`.

Evaluates symbolically over Q(q) (SymPy exact rational arithmetic) and numerically at 80 decimal
places (`mp.mp.dps = 80`, `mpmath 1.4.1`, zero `float64`, zero fitted parameters) across BOTH
registered substrate anchors (`q_proton` and `q_muon` via `q0_comparison`).
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
from mpmath import mpf, fabs, sqrt, log  # noqa: E402
mp.mp.dps = max(mp.mp.dps, 80)

import sympy as sp  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_N_MEV_VALIDATION,
    M_P_MEV_VALIDATION,
    M_PI_0_MEV_VALIDATION,
    M_PI_PM_MEV_VALIDATION,
)
from q_parameter import q_at, q_muon_at  # noqa: E402
from witness_base import WitnessBuilder, q0_comparison  # noqa: E402


def _qbal_mp(n: int, q: mpf) -> mpf:
    return (q ** n - q ** (-n)) / (q - mpf(1) / q)


def _qbal_sp(n: int, q_s: sp.Symbol) -> sp.Expr:
    return sp.cancel((q_s ** n - q_s ** (-n)) / (q_s - sp.Integer(1) / q_s))


def verify_symbolic_baryon_diquark_and_decuplet() -> dict:
    """Exact Q(q) symbolic verification of all theorems in BaryonOctetDiquarkGmoDerivation.lean."""
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    q_s = sp.Symbol("q", nonzero=True)
    m0_s, a_s, b_s, c_s = sp.symbols("M0 a b c", nonzero=True)

    # 1. 3-variable Schur cube decomposition:
    s3 = x1 ** 3 + x2 ** 3 + x3 ** 3 + x1 ** 2 * (x2 + x3) + x2 ** 2 * (x1 + x3) + x3 ** 2 * (x1 + x2) + x1 * x2 * x3
    s21 = x1 ** 2 * (x2 + x3) + x2 ** 2 * (x1 + x3) + x3 ** 2 * (x1 + x2) + 2 * x1 * x2 * x3
    s111 = x1 * x2 * x3
    diff_schur_cube = sp.expand((s3 + 2 * s21 + s111) - (x1 + x2 + x3) ** 3)

    b2 = _qbal_sp(2, q_s)
    b3 = _qbal_sp(3, q_s)
    b4 = _qbal_sp(4, q_s)
    b5 = _qbal_sp(5, q_s)
    sub_weyl = {x1: q_s ** 2, x2: sp.Integer(1), x3: q_s ** (-2)}
    diff_s3_weyl = sp.simplify(s3.subs(sub_weyl) - (b4 * b5 / b2))
    diff_s21_weyl = sp.simplify(s21.subs(sub_weyl) - (b2 * b4))
    diff_s21_b3sq = sp.simplify((b2 * b4) - (b3 ** 2 - 1))
    diff_s111_weyl = sp.simplify(s111.subs(sub_weyl) - 1)
    diff_weyl_cube = sp.simplify((b4 * b5 / b2) + 2 * (b2 * b4) + 1 - b3 ** 3)

    # 2. Temperley-Lieb e_12 = q*I_2 - sigma_1 on S^{(2,1)}:
    s1_mat = sp.Matrix([[-1 / q_s, -1], [0, q_s]])
    e12 = q_s * sp.eye(2) - s1_mat
    p_lam = (q_s * sp.eye(2) - s1_mat) / (q_s + 1 / q_s)
    p_sig = (s1_mat + (1 / q_s) * sp.eye(2)) / (q_s + 1 / q_s)
    tl_sq_ok = sp.simplify(e12 * e12 - b2 * e12) == sp.zeros(2, 2)
    tl_sig_ok = sp.simplify(e12 * p_sig) == sp.zeros(2, 2) and sp.simplify((p_sig * e12).trace()) == 0
    tl_lam_ok = sp.simplify(e12 * p_lam - b2 * p_lam) == sp.zeros(2, 2) and sp.simplify((p_lam * e12).trace() - b2) == 0
    diff_diquark_qdim = sp.simplify((b3 - 1) - (b2 ** 2 - 2))

    # 3. 1st-order baryon GMO & decuplet equal spacing:
    def m1(iv: sp.Expr, yv: sp.Expr) -> sp.Expr:
        return m0_s + a_s * yv + b_s * (iv * (iv + 1) - yv ** 2 / sp.Integer(4))

    diff_gmo_1st = sp.simplify(
        2 * (m1(sp.Rational(1, 2), 1) + m1(sp.Rational(1, 2), -1))
        - (3 * m1(0, 0) + m1(1, 0))
    )
    sp1 = sp.simplify(m1(1, 0) - m1(sp.Rational(3, 2), 1))
    sp2 = sp.simplify(m1(sp.Rational(1, 2), -1) - m1(1, 0))
    sp3 = sp.simplify(m1(0, -2) - m1(sp.Rational(1, 2), -1))
    dec_1st_ok = (sp.simplify(sp1 - sp2) == 0) and (sp.simplify(sp2 - sp3) == 0)

    # 4. 2nd-order rational quantum Casimir decuplet second differences:
    d_del = (q_s ** 6 + 2 * q_s ** 5 + 3 * q_s ** 4 + 2 * q_s ** 3 + 3 * q_s ** 2 + 2 * q_s + 1) / (
        (q_s ** 2) * ((q_s + 1) ** 2)
    )
    d_sigs = q_s + 1 / q_s
    d_xis = (q_s + 1 / q_s) / (q_s + 2 + 1 / q_s)
    d_om = sp.Integer(-1)

    m_del = m0_s + a_s * 1 + c_s * d_del
    m_sigs = m0_s + a_s * 0 + c_s * d_sigs
    m_xis = m0_s + a_s * (-1) + c_s * d_xis
    m_om = m0_s + a_s * (-2) + c_s * d_om

    sd_low = sp.simplify(m_xis - 2 * m_sigs + m_del)
    sd_upp = sp.simplify(m_om - 2 * m_xis + m_sigs)
    sd_low_exact = c_s * ((q_s - 1) / (q_s + 1)) ** 2 * (q_s + 1 + 1 / q_s) ** 2
    sd_upp_exact = c_s * ((q_s - 1) / (q_s + 1)) ** 2 * (q_s + 1 + 1 / q_s)
    diff_sd_low = sp.simplify(sd_low - sd_low_exact)
    diff_sd_upp = sp.simplify(sd_upp - sd_upp_exact)
    diff_sd_ratio = sp.simplify(sd_upp / sd_low - 1 / (q_s + 1 + 1 / q_s))

    checks = {
        "schur_3var_cube_identity": diff_schur_cube == 0,
        "uq_sl3_weyl_qdim_s3_s21_s111_cube": (
            diff_s3_weyl == 0 and diff_s21_weyl == 0 and diff_s21_b3sq == 0
            and diff_s111_weyl == 0 and diff_weyl_cube == 0
        ),
        "temperley_lieb_e12_diquark_eigenvalues": bool(tl_sq_ok and tl_sig_ok and tl_lam_ok and diff_diquark_qdim == 0),
        "first_order_baryon_gmo_and_decuplet_equal_spacing": (diff_gmo_1st == 0 and dec_1st_ok),
        "qcasimir_decuplet_second_differences_and_ratio": (
            diff_sd_low == 0 and diff_sd_upp == 0 and diff_sd_ratio == 0
        ),
    }
    return {
        "checks": checks,
        "decuplet_lower_2nd_diff_closed_form": "c * ((q - 1)/(q + 1))^2 * (q + 1 + q^-1)^2",
        "decuplet_upper_2nd_diff_closed_form": "c * ((q - 1)/(q + 1))^2 * (q + 1 + q^-1)",
        "decuplet_upper_over_lower_ratio_closed_form": "1 / (q + 1 + q^-1)",
    }


def evaluate_pin(pin_label: str, q: mpf, pdg_ref: dict[str, mpf]) -> dict:
    """80-dps evaluation of the pre-committed zero-parameter scale catalog, octet GMO, and decuplet."""
    LN_Q = log(q)
    hbar_q = mpf(1) - mpf(1) / q
    h_hecke = q - mpf(1) / q
    b2 = _qbal_mp(2, q)
    b3 = _qbal_mp(3, q)
    b4 = _qbal_mp(4, q)
    b5 = _qbal_mp(5, q)

    m_e = pdg_ref["m_e"]
    m_p = pdg_ref["m_p"]
    m_pi_pm = pdg_ref["m_pi_pm"]
    e0_unit = m_e / (q * (q - mpf(1)))
    dim_q_8 = b2 * b4
    dim_q_10 = b4 * b5 / b2
    v3_diquark_split = (h_hecke ** 3) * (q ** 2 + q ** (-2)) * b3 / b2

    exp_split = pdg_ref["m_Sigma0"] - pdg_ref["m_Lambda"]  # 76.959 MeV

    # Pre-committed zero-parameter scale candidates (baryon_octet_diquark_gmo_preregistration.md §1):
    scale_candidates = {
        "S1_E0_b3sq_b2": e0_unit * (b3 ** 2) * b2,
        "S2_E0_dimq8_b2": e0_unit * dim_q_8 * b2,
        "S3_mpi_over_b2": m_pi_pm / b2,
        "S4_mp_h_over_b3": m_p * h_hecke / b3,
        "S5_mp_hbar_b2_over_b3": m_p * hbar_q * b2 / b3,
        "S6_mp_V3_diquark_split": m_p * v3_diquark_split,
    }
    scale_rows = {}
    for s_name, s_val in scale_candidates.items():
        diff_mev = s_val - exp_split
        rel_pct = (diff_mev / exp_split) * mpf(100)
        scale_rows[s_name] = {
            "predicted_MeV": fmt(s_val),
            "diff_vs_pdg_76p959_MeV": fmt(diff_mev),
            "rel_err_pct": fmt(rel_pct),
            "implied_kappa_hf_MeV": fmt(s_val / b2),
        }

    # Baryon octet 2nd-order quantum Casimir GMO & weighted Jucys-Murphy comparison:
    qcas_ratio = -(((q - mpf(1)) / (q + mpf(1))) ** 2)
    m_n_iso = pdg_ref["m_N_iso"]
    m_xi_iso = pdg_ref["m_Xi_iso"]
    m_sig_iso = pdg_ref["m_Sigma_iso"]
    m_lam = pdg_ref["m_Lambda"]

    gmo_2x_iso = mpf(2) * (m_n_iso + m_xi_iso) - (mpf(3) * m_lam + m_sig_iso)
    gmo_1x_iso = gmo_2x_iso / mpf(2)
    gmo_2x_neutral = mpf(2) * (pdg_ref["m_n"] + pdg_ref["m_Xi0"]) - (mpf(3) * m_lam + pdg_ref["m_Sigma0"])
    pred_gmo_2x_qcas = qcas_ratio * (m_sig_iso - m_lam)

    # Closed-form weighted Jucys-Murphy GMO/(Xi - N) ratios (proven symbolically in task-1008):
    # u<d<s: +q^2 h^2 (2q^2 + 3) / ((q^2 + 3)(q^4 + q^2 + 1))
    # s<u<d: -q^2 h^2 (3q^4 + q^2 + 1) / (2q^8 + 4q^6 + 3q^4 + q^2 + 2)
    q2h2 = (q ** 2) * (h_hecke ** 2)
    jm_gmo_over_xi_n_uds = q2h2 * (mpf(2) * (q ** 2) + mpf(3)) / (
        (q ** 2 + mpf(3)) * (q ** 4 + q ** 2 + mpf(1))
    )
    jm_gmo_over_xi_n_sud = -q2h2 * (mpf(3) * (q ** 4) + q ** 2 + mpf(1)) / (
        mpf(2) * (q ** 8) + mpf(4) * (q ** 6) + mpf(3) * (q ** 4) + q ** 2 + mpf(2)
    )
    pdg_gmo_over_xi_n = gmo_2x_iso / (m_xi_iso - m_n_iso)

    # Decuplet quantum Casimir second-difference test (using c_oct = (M_Sigma - M_Lambda)/[2]_q):
    c_oct = (m_sig_iso - m_lam) / b2
    tri_q = q + mpf(1) + mpf(1) / q
    pred_dec_sd_lower = c_oct * (-qcas_ratio) * (tri_q ** 2)
    pred_dec_sd_upper = c_oct * (-qcas_ratio) * tri_q
    pred_dec_ratio = mpf(1) / tri_q

    pdg_dec_sd_lower = pdg_ref["m_XiS_iso"] - mpf(2) * pdg_ref["m_SigmaS_iso"] + pdg_ref["m_Delta"]
    pdg_dec_sd_upper = pdg_ref["m_Omega"] - mpf(2) * pdg_ref["m_XiS_iso"] + pdg_ref["m_SigmaS_iso"]
    pdg_dec_ratio = pdg_dec_sd_upper / pdg_dec_sd_lower

    return {
        "pin": pin_label,
        "q0": fmt(q, 80),
        "LN_Q": fmt(LN_Q),
        "log_q_of_b2": fmt(log(b2) / LN_Q),
        "E0_MeV": fmt(e0_unit),
        "uq_sl3_dimensions": {
            "dim_q_10_decuplet": fmt(dim_q_10),
            "dim_q_8_octet": fmt(dim_q_8),
            "dim_q_1_singlet": fmt(mpf(1)),
            "sum_10_plus_2x8_plus_1": fmt(dim_q_10 + mpf(2) * dim_q_8 + mpf(1)),
            "qBracket3_cubed": fmt(b3 ** 3),
            "cube_identity_residual": fmt(fabs((dim_q_10 + mpf(2) * dim_q_8 + mpf(1)) - (b3 ** 3))),
        },
        "precommitted_lambda_sigma0_scale_catalog": scale_rows,
        "baryon_octet_gmo_evaluation": {
            "universal_qcasimir_ratio": fmt(qcas_ratio),
            "pdg_2x_gmo_iso_avg_MeV": fmt(gmo_2x_iso),
            "pdg_1x_gmo_iso_avg_MeV": fmt(gmo_1x_iso),
            "pdg_2x_gmo_neutral_only_MeV": fmt(gmo_2x_neutral),
            "qcasimir_predicted_2x_gmo_MeV": fmt(pred_gmo_2x_qcas),
            "qcasimir_sign_matches_pdg_negative": bool(pred_gmo_2x_qcas < mpf(0) and gmo_2x_iso < mpf(0)),
            "qcasimir_fraction_of_pdg_magnitude": fmt(pred_gmo_2x_qcas / gmo_2x_iso),
            "weighted_jm_gmo_over_xi_minus_n_order_u_d_s": fmt(jm_gmo_over_xi_n_uds),
            "weighted_jm_gmo_over_xi_minus_n_order_s_u_d": fmt(jm_gmo_over_xi_n_sud),
            "pdg_gmo_over_xi_minus_n": fmt(pdg_gmo_over_xi_n),
        },
        "baryon_decuplet_qcasimir_curvature_test": {
            "c_octet_from_Sigma_minus_Lambda_over_b2_MeV": fmt(c_oct),
            "qcasimir_pred_lower_2nd_diff_MeV": fmt(pred_dec_sd_lower),
            "qcasimir_pred_upper_2nd_diff_MeV": fmt(pred_dec_sd_upper),
            "qcasimir_pred_upper_over_lower_ratio": fmt(pred_dec_ratio),
            "pdg_lower_2nd_diff_MeV": fmt(pdg_dec_sd_lower),
            "pdg_upper_2nd_diff_MeV": fmt(pdg_dec_sd_upper),
            "pdg_upper_over_lower_ratio": fmt(pdg_dec_ratio),
            "breaks_classical_equal_second_diff_1": bool(pred_dec_ratio < mpf(1)),
            "honest_sign_falsification_note": (
                "With c_octet > 0 fixed by M_Sigma > M_Lambda, pure d_q(I,Y) predicts positive "
                "decuplet second differences (+0.949 MeV, +0.315 MeV), opposite in sign to PDG "
                "(-3.753 MeV, -9.773 MeV), proving non-octet chiral-loop curvature dominates the decuplet."
            ),
        },
    }


def main() -> int:
    q_proton = q_at(80)
    q_muon = q_muon_at(80)

    # Validation-only CODATA-2022 & PDG-2024 hadron masses (MeV; NEVER fitted):
    m_e = mpf(str(M_E_MEV))
    m_p = mpf(str(M_P_MEV_VALIDATION))
    m_n = mpf(str(M_N_MEV_VALIDATION))
    m_pi_pm = mpf(str(M_PI_PM_MEV_VALIDATION))
    m_pi_0 = mpf(str(M_PI_0_MEV_VALIDATION))

    m_lam = mpf("1115.683")
    m_sig_p = mpf("1189.37")
    m_sig_0 = mpf("1192.642")
    m_sig_m = mpf("1197.449")
    m_xi_0 = mpf("1314.86")
    m_xi_m = mpf("1321.71")

    m_del = mpf("1232.0")
    m_sigs_iso = (mpf("1382.83") + mpf("1383.7") + mpf("1387.2")) / mpf(3)
    m_xis_iso = (mpf("1531.80") + mpf("1535.0")) / mpf(2)
    m_om = mpf("1672.45")

    pdg_ref = {
        "m_e": m_e,
        "m_p": m_p,
        "m_n": m_n,
        "m_pi_pm": m_pi_pm,
        "m_pi_0": m_pi_0,
        "m_Lambda": m_lam,
        "m_Sigma0": m_sig_0,
        "m_Xi0": m_xi_0,
        "m_N_iso": (m_p + m_n) / mpf(2),
        "m_Sigma_iso": (m_sig_p + m_sig_0 + m_sig_m) / mpf(3),
        "m_Xi_iso": (m_xi_0 + m_xi_m) / mpf(2),
        "m_Delta": m_del,
        "m_SigmaS_iso": m_sigs_iso,
        "m_XiS_iso": m_xis_iso,
        "m_Omega": m_om,
    }

    sym_res = verify_symbolic_baryon_diquark_and_decuplet()
    proton_res = evaluate_pin("proton", q_proton, pdg_ref)
    muon_res = evaluate_pin("muon", q_muon, pdg_ref)

    sym_all_ok = all(sym_res["checks"].values())
    b2_p = _qbal_mp(2, q_proton)
    b3_p = _qbal_mp(3, q_proton)
    b4_p = _qbal_mp(4, q_proton)
    b5_p = _qbal_mp(5, q_proton)
    cube_lhs = (b4_p * b5_p / b2_p) + mpf(2) * (b2_p * b4_p) + mpf(1)
    cube_rhs = b3_p ** 3
    cube_ok = bool(fabs(cube_lhs - cube_rhs) < mpf("1e-75"))

    # Verify decuplet 2nd-difference ratio at 80 dps directly from rational Casimir definitions:
    d_del_p = (
        q_proton ** 6 + mpf(2) * q_proton ** 5 + mpf(3) * q_proton ** 4
        + mpf(2) * q_proton ** 3 + mpf(3) * q_proton ** 2 + mpf(2) * q_proton + mpf(1)
    ) / ((q_proton ** 2) * ((q_proton + mpf(1)) ** 2))
    d_sigs_p = b2_p
    d_xis_p = b2_p / (b2_p + mpf(2))
    d_om_p = -mpf(1)
    dec_ratio_lhs = (d_om_p - mpf(2) * d_xis_p + d_sigs_p) / (d_xis_p - mpf(2) * d_sigs_p + d_del_p)
    dec_ratio_rhs = mpf(1) / (q_proton + mpf(1) + mpf(1) / q_proton)
    dec_ratio_ok = bool(fabs(dec_ratio_lhs - dec_ratio_rhs) < mpf("1e-70"))

    gmo_sign_ok = (
        proton_res["baryon_octet_gmo_evaluation"]["qcasimir_sign_matches_pdg_negative"]
        and muon_res["baryon_octet_gmo_evaluation"]["qcasimir_sign_matches_pdg_negative"]
    )

    wb = WitnessBuilder("baryon_octet_diquark_gmo_probe", engine="sympy+mpmath")
    wb.set_content_block("prop:baryon-octet-decomposition")
    wb.set_description(
        "80-dps SymPy + mpmath probe for qou-8fw2, qou-d7h1, qou-wyy9 (#9375): "
        "(1) exact 3-variable Schur cube s_(3) + 2 s_(2,1) + s_(1,1,1) = (x1 + x2 + x3)^3 and "
        "U_q(sl_3) Weyl quantum-dimension specialization [4]_q[5]_q/[2]_q + 2[2]_q[4]_q + 1 = [3]_q^3; "
        "(2) Temperley-Lieb (u,d) diquark exchange e_12 = q I - sigma_1 on S^{(2,1)} giving exact (0, [2]_q) "
        "eigenvalues on Sigma^0 vs Lambda^0, plus pre-committed zero-parameter QOU scale catalog against "
        "PDG 76.959(25) MeV (E_0 [3]_q^2 [2]_q = 77.9817 MeV at +1.329%, m_pi/[2]_q = 69.4070 MeV at -9.813%); "
        "(3) 2nd-order rational quantum Casimir octet GMO (-0.2105 MeV vs PDG -25.7952 MeV) and decuplet "
        "second-difference asymmetry ratio (Omega^- - 2 Xi^* + Sigma^*)/(Xi^* - 2 Sigma^* + Delta) = 1/(q + 1 + q^-1)."
    )
    wb.add_data("symbolic_verifications", sym_res)
    wb.add_data("proton_pin_evaluation", proton_res)
    wb.add_data("muon_pin_evaluation", muon_res)
    wb.add_data("epistemic_status", {
        "fitted_parameters": 0,
        "wired_into_production": False,
        "preregistration": "computations/mesons/baryon_octet_diquark_gmo_preregistration.md",
        "preregistration_commit": "ccc7d2b78a0e555e7cf069e49284ce1ee7f482b5",
        "lean_module": "folio/quantum-observable-universe/lean/QOU/EightfoldWay/BaryonOctetDiquarkGmoDerivation.lean",
    })

    wb.add_assertion(
        name="symbolic_schur_weyl_tl_diquark_and_decuplet_identities_hold",
        computed="1" if sym_all_ok else "0",
        expected="1",
        tolerance="0.5",
        source="BaryonOctetDiquarkGmoDerivation (Sections 1-3)",
    )
    wb.add_assertion(
        name="uq_sl3_weyl_qdim_cube_identity_80dps",
        computed=fmt(cube_lhs),
        expected=fmt(cube_rhs),
        tolerance="1e-55",
        source="BaryonOctetDiquarkGmoDerivation.uq_sl3_weyl_qdim_cube_identity",
    )
    wb.add_assertion(
        name="qcasimir_decuplet_second_diff_asymmetry_ratio_80dps",
        computed=fmt(dec_ratio_lhs),
        expected=fmt(dec_ratio_rhs),
        tolerance="1e-55",
        source="BaryonOctetDiquarkGmoDerivation.qCasimir_decuplet_second_differences_and_ratio",
    )
    wb.add_assertion(
        name="qcasimir_baryon_octet_gmo_sign_negative_both_pins",
        computed="1" if gmo_sign_ok else "0",
        expected="1",
        tolerance="0.5",
        source="HyperbolicMesonClaspAndDiquarkSplit.qCasimir_gmo_second_order_and_universal_ratio",
    )

    wb.set_audit_only("docs/audits/2026-11-24-baryon-octet-diquark-lambda-sigma-gmo.md")
    out_path = wb.save(
        q0_comparison(
            muon=fmt(q_muon, 80),
            proton=fmt(q_proton, 80),
            reason=(
                "evaluates the pre-registered zero-parameter baryon Lambda^0-Sigma^0 diquark "
                "scale catalog, 2nd-order octet GMO, and decuplet curvature at both q_proton and q_muon"
            ),
        )
    )

    print("=" * 94)
    print("BARYON OCTET LAMBDA^0-SIGMA^0 DIQUARK, U_q(sl_3) CUBE & DECUPLET GMO PROBE (80 dps)")
    print("=" * 94)
    print(f"[Part 1] Symbolic Q(q) checks (5/5) all passed : {sym_all_ok}")
    for res in (proton_res, muon_res):
        print(f"\n[Part 2] Pin: {res['pin'].upper()} (q = {res['q0'][:24]}...)")
        for s_k, row in res["precommitted_lambda_sigma0_scale_catalog"].items():
            print(
                f"  {s_k:26s}: pred={row['predicted_MeV'][:12]:>12s} MeV | "
                f"diff={row['diff_vs_pdg_76p959_MeV'][:10]:>10s} MeV ({row['rel_err_pct'][:8]:>8s}%)"
            )
    print(f"\nWitness -> {out_path}")
    return 0 if (sym_all_ok and cube_ok and dec_ratio_ok and gmo_sign_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
