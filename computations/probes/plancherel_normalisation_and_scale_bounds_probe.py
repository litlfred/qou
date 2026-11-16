#!/usr/bin/env python3
"""Plancherel Normalisation of F_Bor, Hyperbolic Volume Scaling, Berezinian Cross-Terms, and the m_e Scale Floor.

50-dps mpmath + symbolic SymPy verification probe for five tasks under epic `qou-2002`:
  - `qou-24w9`: q-Schur vs Wenzl/Markov Plancherel weight provenance of F_Bor's /q^3,
    exact three-way reconstruction of tr_M(beta_Bor) by convention-D Wenzl weights,
    collapse of 1/y^Wenzl_(2,1) = [2]_q^2 = delta^(n-1), and net q^-2 bar-asymmetry
    across m_mu * F_Bor.
  - `qou-r0dn`: Vol(6_2) 50-dps SnapPy census agreement in m_tau_knot_prediction.py
    and vol_density_deuteron_perknot_probe.py, exact per-knot volume-ratio scaling,
    and quantification of the retired 2*Vol(4_1) (-7.75003%) and 8th-digit (+1.055e-7)
    discrepancies.
  - `qou-hgm6`: 50-dps mpmath evaluation of the 5_2 Stokes offset quadratic-balance
    root q_quad = (-9 + sqrt(193))/56 and order-18 root q*(18), super-Berezinian
    cross-term lift (A - B*D^-1*C)/A = 1 - rho scatter and surjectivity witness,
    and scale-free rho_binding mirror constancy identity.
  - `qou-cuur`: Algebraic bar-symmetry, positivity above 5/2, and non-inversion of
    linking_weight_family_a lambda_A(q) = 5/2 + (3/4)*(q - 2 + q^-1).
  - `qou-zufe`: CODATA electron-mass relative uncertainty floor sigma(m_e)/m_e =
    3.13112e-10 (~9.504 decimal digits) capping dimensional MeV predictions vs
    exact m_e cancellation in dimensionless mass ratios.

Companion Lean 4 formalization:
  `folio/quantum-observable-universe/lean/QOU/MassTheory/PlancherelNormalisationAndScaleBounds.lean`
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTATIONS_DIR = HERE.parent
REPO_ROOT = COMPUTATIONS_DIR.parent

for p in (
    COMPUTATIONS_DIR,
    COMPUTATIONS_DIR / "substrate",
    REPO_ROOT / "tools" / "qou-substrate" / "python",
):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

import _path_bridge  # noqa: E402, F401
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps()

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from codata_2022_source import M_E_MEV, M_E_MEV_ERR  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def _extract_vol_6_2_literals() -> tuple[mp.mpf, mp.mpf]:
    """Read the Vol(6_2) string literals directly from m_tau_knot_prediction.py
    and vol_density_deuteron_perknot_probe.py via AST."""
    m_tau_path = COMPUTATIONS_DIR / "m_tau_knot_prediction.py"
    m_tau_tree = ast.parse(m_tau_path.read_text())
    vol_mtau = None
    for node in ast.walk(m_tau_tree):
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            if node.target.id == "KNOT_VOL_TABLE" and isinstance(node.value, ast.Dict):
                for k_node, v_node in zip(node.value.keys, node.value.values):
                    if (
                        isinstance(k_node, ast.Constant)
                        and k_node.value == "6_2"
                        and isinstance(v_node, ast.Constant)
                    ):
                        vol_mtau = mp.mpf(str(v_node.value))

    deut_path = COMPUTATIONS_DIR / "vol_density_deuteron_perknot_probe.py"
    deut_tree = ast.parse(deut_path.read_text())
    vol_deut = None
    for node in ast.walk(deut_tree):
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == "VOL_6_2":
                    if (
                        isinstance(node.value, ast.Call)
                        and node.value.args
                        and isinstance(node.value.args[0], ast.Constant)
                    ):
                        vol_deut = mp.mpf(str(node.value.args[0].value))

    assert vol_mtau is not None and vol_deut is not None
    return vol_mtau, vol_deut


def main() -> int:
    set_compute_dps()
    q0 = mp.mpf(Q_50_DIGIT_STR)
    hbar_q0 = (q0 - 1) / q0
    hbar_sym_sq = q0 - 2 + 1 / q0
    vol_4_1 = 2 * mp.clsin(2, mp.pi / 3)
    m_e = +M_E_MEV

    # =========================================================================
    # 1. Bean qou-24w9: Symbolic & 50-dps Plancherel Normalisation of F_Bor
    # =========================================================================
    qs = sp.Symbol("q", positive=True)
    qfact3_bal_sym = (qs + 1 / qs) * (qs**2 + 1 + qs ** (-2))
    y_schur_3_sym = qs**3 / qfact3_bal_sym
    y_schur_111_sym = qs ** (-3) / qfact3_bal_sym

    y_wenzl_3_sym = (qs**2 + qs ** (-2)) / (qs + 1 / qs) ** 2
    y_wenzl_21_sym = 1 / (qs + 1 / qs) ** 2
    y_wenzl_111_sym = sp.Integer(0)

    chi_21_sym = (
        -(qs**12)
        + 3 * qs**10
        - 3 * qs**8
        + 4 * qs**6
        - 3 * qs**4
        + 3 * qs**2
        - 1
    ) / qs**6
    h_sym = qs - 1 / qs
    trM_bor_sym = (4 + h_sym**2 - 3 * h_sym**4 - h_sym**6) / (h_sym**2 + 4)

    res_schur_fbor = sp.simplify(1 / y_schur_3_sym - qfact3_bal_sym / qs**3)
    res_schur_duality = sp.simplify(
        y_schur_111_sym - y_schur_3_sym.subs(qs, 1 / qs)
    )
    res_wenzl_norm = sp.simplify(
        1 * y_wenzl_3_sym + 2 * y_wenzl_21_sym + 1 * y_wenzl_111_sym - 1
    )
    res_wenzl_21_tl = sp.simplify(1 / y_wenzl_21_sym - (qs + 1 / qs) ** 2)
    res_wenzl_trM = sp.simplify(
        y_wenzl_3_sym * 1
        + y_wenzl_21_sym * chi_21_sym
        + y_wenzl_111_sym * 1
        - trM_bor_sym
    )
    hbar_q_sym = (qs - 1) / qs
    hbar_sym2_sym = qs - 2 + 1 / qs
    res_bar_asym = sp.simplify(
        (1 / hbar_q_sym**2) * (qfact3_bal_sym / qs**3)
        - qfact3_bal_sym / (qs**2 * hbar_sym2_sym)
    )

    sym_24w9_ok = all(
        r == 0
        for r in (
            res_schur_fbor,
            res_schur_duality,
            res_wenzl_norm,
            res_wenzl_21_tl,
            res_wenzl_trM,
            res_bar_asym,
        )
    )

    # 50-dps evaluation at proton pin q0
    qfact3_q0 = (q0 + 1 / q0) * (q0**2 + 1 + 1 / q0**2)
    y_schur_3_q0 = q0**3 / qfact3_q0
    y_wenzl_3_q0 = (q0**2 + 1 / q0**2) / (q0 + 1 / q0) ** 2
    y_wenzl_21_q0 = 1 / (q0 + 1 / q0) ** 2
    chi_21_q0 = (
        -(q0**12)
        + 3 * q0**10
        - 3 * q0**8
        + 4 * q0**6
        - 3 * q0**4
        + 3 * q0**2
        - 1
    ) / q0**6
    h_q0 = q0 - 1 / q0
    trM_q0 = (4 + h_q0**2 - 3 * h_q0**4 - h_q0**6) / (h_q0**2 + 4)
    wenzl_recon_q0 = y_wenzl_3_q0 * 1 + y_wenzl_21_q0 * chi_21_q0
    wenzl_trM_err = abs(wenzl_recon_q0 - trM_q0)
    schur_fbor_err = abs(1 / y_schur_3_q0 - qfact3_q0 / q0**3)
    wenzl_tl_err = abs(1 / y_wenzl_21_q0 - (q0 + 1 / q0) ** 2)
    bar_asym_err = abs(
        (1 / hbar_q0**2) * (qfact3_q0 / q0**3)
        - qfact3_q0 / (q0**2 * hbar_sym_sq)
    )

    # =========================================================================
    # 2. Bean qou-r0dn: Vol(6_2) Census Agreement & Volume Scaling Law
    # =========================================================================
    vol_6_2_census = mp.mpf("4.40083251612304610144120386564")
    vol_mtau, vol_deut = _extract_vol_6_2_literals()
    mtau_census_err = abs(vol_mtau - vol_6_2_census) / vol_6_2_census
    deut_census_err = abs(vol_deut - vol_6_2_census) / vol_6_2_census

    retired_mtau_lit = mp.mpf("4.0597664956578801590")
    retired_deut_lit = mp.mpf("4.40083298054544839393")
    retired_mtau_rel_shift = (retired_mtau_lit - vol_6_2_census) / vol_6_2_census
    retired_deut_rel_shift = (retired_deut_lit - vol_6_2_census) / vol_6_2_census
    doubled_4_1_diff = abs(retired_mtau_lit - 2 * vol_4_1)

    # Exact volume scaling check
    m_true = m_e * (vol_6_2_census / hbar_q0**2) * trM_q0
    m_sub = m_e * (retired_mtau_lit / hbar_q0**2) * trM_q0
    vol_scaling_err = abs(
        (m_sub - m_true) / m_true - retired_mtau_rel_shift
    )

    # =========================================================================
    # 3. Bean qou-hgm6: 50-dps Saddle Offset, Berezinian Lift, & rho_binding
    # =========================================================================
    q_quad = (-mp.mpf(9) + mp.sqrt(mp.mpf(193))) / mp.mpf(56)
    quad_poly_res = abs(1 - 9 * q_quad - 28 * q_quad**2)
    q_quad_in_bounds = bool(mp.mpf("0.087") < q_quad < mp.mpf("0.088"))

    # Berezinian lift (A - B*D^-1*C)/A = 1 - rho at 50 dps
    mu3_mp = mp.mpf("0.4708")
    c3_single_mp = mp.mpf("0.297")
    r_star = mu3_mp / c3_single_mp
    rho_needed = 1 - r_star
    h_minus_1 = q0 - 1
    natural_rhos = [
        hbar_q0,
        -hbar_q0,
        h_minus_1,
        -h_minus_1,
        h_minus_1**2,
        -(h_minus_1**2),
        (1 + q0) / 2 - 1,
        c3_single_mp / mu3_mp,
        -(c3_single_mp / mu3_mp),
        mp.mpf(1),
        mp.mpf(-1),
        mp.mpf(2),
        mp.mpf(-2),
    ]
    n_natural_hits = sum(
        1 for rho in natural_rhos if abs((1 - rho) - r_star) < mp.mpf("0.02")
    )
    A_b, C_b, D_b = mp.mpf("1.7"), mp.mpf("2.3"), mp.mpf("0.9")
    B_star = A_b * (1 - r_star) * D_b / C_b
    lift_fit = (A_b - B_star * (1 / D_b) * C_b) / A_b
    berezinian_fit_err = abs(lift_fit - r_star)

    # =========================================================================
    # 4. Bean qou-cuur: linking_weight_family_a Algebraic Non-Inversion
    # =========================================================================
    def lambda_A(q_val: mp.mpf) -> mp.mpf:
        return mp.mpf("2.5") + mp.mpf("0.75") * (q_val - 2 + 1 / q_val)

    lam_q0 = lambda_A(q0)
    lam_q0_inv = lambda_A(1 / q0)
    lam_bar_err = abs(lam_q0 - lam_q0_inv)
    lam_excess_err = abs(
        (lam_q0 - mp.mpf("2.5")) - 3 * (q0 - 1) ** 2 / (4 * q0)
    )
    lam_gt_five_halves = bool(lam_q0 > mp.mpf("2.5") > mp.mpf("2.461"))

    # =========================================================================
    # 5. Bean qou-zufe: CODATA m_e Relative Uncertainty Floor & Ratio Cancel
    # =========================================================================
    me_codata = +M_E_MEV
    me_sigma = +M_E_MEV_ERR
    rel_sigma_me = me_sigma / me_codata
    effective_digits_me = -mp.log10(rel_sigma_me)

    # Dimensionless ratio cancellation
    r1 = vol_4_1 / hbar_q0**2
    r2 = 2 * (r1 * trM_q0 * (qfact3_q0 / q0**3) - 6)
    ratio_cancels_err = abs((m_e * r2) / (m_e * r1) - (r2 / r1))

    wb = WitnessBuilder(
        "plancherel-normalisation-and-scale-bounds-probe",
        engine="mpmath+sympy",
        output_dir=HERE,
    )
    wb.set_description(
        "50-dps mpmath + symbolic SymPy verification of q-Schur vs Wenzl "
        "Plancherel normalisation of F_Bor (qou-24w9), Vol(6_2) SnapPy census "
        "agreement and volume scaling (qou-r0dn), 50-dps Stokes quadratic root "
        "and super-Berezinian lift (qou-hgm6), algebraic bar-symmetry and lower "
        "bound of linking_weight_family_a (qou-cuur), and CODATA m_e relative "
        "uncertainty floor vs dimensionless ratio cancellation (qou-zufe)."
    )
    wb.add_parameter("dps", 50)
    wb.add_parameter("q0_proton_pin", fmt(q0, 50))
    wb.add_data(
        "qou_24w9_plancherel_normalisation",
        {
            "symbolic_identities_all_zero": sym_24w9_ok,
            "trM_borromean_q0": fmt(trM_q0, 50),
            "wenzl_reconstructed_trM_q0": fmt(wenzl_recon_q0, 50),
            "wenzl_trM_abs_err": fmt(wenzl_trM_err, 12),
            "inv_y_schur_3_q0": fmt(1 / y_schur_3_q0, 50),
            "inv_y_wenzl_3_q0": fmt(1 / y_wenzl_3_q0, 50),
            "inv_y_wenzl_21_eq_two_bracket_sq_q0": fmt(1 / y_wenzl_21_q0, 50),
            "bar_asymmetry_identity_abs_err": fmt(bar_asym_err, 12),
        },
    )
    wb.add_data(
        "qou_r0dn_vol_6_2_census",
        {
            "vol_6_2_snappy_census": fmt(vol_6_2_census, 30),
            "m_tau_table_rel_err_vs_census": fmt(mtau_census_err, 12),
            "deuteron_probe_rel_err_vs_census": fmt(deut_census_err, 12),
            "retired_mtau_literal_rel_shift": fmt(retired_mtau_rel_shift, 15),
            "retired_deut_literal_rel_shift": fmt(retired_deut_rel_shift, 15),
            "retired_mtau_vs_2_vol_4_1_abs_diff": fmt(doubled_4_1_diff, 12),
            "volume_scaling_law_abs_err": fmt(vol_scaling_err, 12),
        },
    )
    wb.add_data(
        "qou_hgm6_fifty_dps_probes",
        {
            "q_quad_50dps": fmt(q_quad, 50),
            "q_quad_polynomial_residual": fmt(quad_poly_res, 12),
            "q_quad_in_0p087_0p088": q_quad_in_bounds,
            "r_star_50dps": fmt(r_star, 50),
            "rho_needed_50dps": fmt(rho_needed, 50),
            "natural_substrate_readings_landing_rstar": n_natural_hits,
            "berezinian_surjectivity_fit_abs_err": fmt(berezinian_fit_err, 12),
        },
    )
    wb.add_data(
        "qou_cuur_linking_weight_family_a",
        {
            "lambda_A_q0_50dps": fmt(lam_q0, 50),
            "bar_symmetry_abs_err": fmt(lam_bar_err, 12),
            "excess_over_five_halves_abs_err": fmt(lam_excess_err, 12),
            "strictly_exceeds_five_halves_and_codata_target": lam_gt_five_halves,
        },
    )
    wb.add_data(
        "qou_zufe_me_scale_floor",
        {
            "me_codata_MeV": fmt(me_codata, 15),
            "me_sigma_MeV": fmt(me_sigma, 15),
            "me_relative_uncertainty_floor": fmt(rel_sigma_me, 15),
            "me_effective_decimal_digits": fmt(effective_digits_me, 12),
            "dimensionless_ratio_me_cancellation_abs_err": fmt(
                ratio_cancels_err, 12
            ),
        },
    )

    wb.add_assertion(
        "qou_24w9_wenzl_reconstructs_borromean_trM_and_qschur_matches_fbor",
        computed=bool(
            sym_24w9_ok
            and wenzl_trM_err < mp.mpf("1e-48")
            and schur_fbor_err < mp.mpf("1e-48")
            and wenzl_tl_err < mp.mpf("1e-48")
            and bar_asym_err < mp.mpf("1e-45")
        ),
        expected=True,
    )
    wb.add_assertion(
        "qou_r0dn_vol_6_2_matches_census_and_scales_linearly",
        computed=bool(
            mtau_census_err < mp.mpf("1e-19")
            and deut_census_err < mp.mpf("1e-29")
            and abs(retired_mtau_rel_shift - mp.mpf("-0.077500340928"))
            < mp.mpf("1e-9")
            and vol_scaling_err < mp.mpf("1e-48")
        ),
        expected=True,
    )
    wb.add_assertion(
        "qou_hgm6_saddle_quad_root_and_berezinian_lift_50dps_exact",
        computed=bool(
            quad_poly_res < mp.mpf("1e-48")
            and q_quad_in_bounds
            and n_natural_hits == 0
            and berezinian_fit_err < mp.mpf("1e-48")
        ),
        expected=True,
    )
    wb.add_assertion(
        "qou_cuur_linking_weight_family_a_bar_symmetric_and_gt_five_halves",
        computed=bool(
            lam_bar_err < mp.mpf("1e-48")
            and lam_excess_err < mp.mpf("1e-48")
            and lam_gt_five_halves
        ),
        expected=True,
    )
    wb.add_assertion(
        "qou_zufe_me_relative_uncertainty_floor_and_ratio_cancellation",
        computed=bool(
            abs(rel_sigma_me - mp.mpf(16) / mp.mpf(51099895069))
            < mp.mpf("1e-48")
            and mp.mpf("9.5") < effective_digits_me < mp.mpf("9.6")
            and ratio_cancels_err < mp.mpf("1e-48")
        ),
        expected=True,
    )

    out_path = wb.save({"q0Anchor": "proton", "q0Value": fmt(q0, 50)})
    print(f"Saved witness: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
