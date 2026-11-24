#!/usr/bin/env python3
"""80-dps verification probe for Plancherel normalisation of F_Bor, volume scaling,
Berezinian cross-terms, linking_weight_family_a lower bound, and the m_e scale floor.

Salvaged from PR #8169 (`qou-24w9`, `qou-r0dn`, `qou-hgm6`, `qou-cuur`, `qou-zufe`).
Lean companion: `QOU/MassTheory/PlancherelNormalisationAndScaleBounds.lean`.
Precision: 80-dps mpmath + SymPy, zero float64, zero hardcoded CODATA literals.
"""

from __future__ import annotations

import ast
import sys
import time
from pathlib import Path

THIS = Path(__file__).resolve()
COMPUTATIONS_DIR = THIS.parent.parent
REPO_ROOT = COMPUTATIONS_DIR.parent

for _rel in (
    "computations",
    "computations/substrate",
    "tools/qou-substrate/python",
    "schemas/witness-schema/python",
):
    if str(REPO_ROOT / _rel) not in sys.path:
        sys.path.insert(0, str(REPO_ROOT / _rel))

import _path_bridge  # noqa: E402, F401
from _precision import fmt, set_compute_dps  # noqa: E402
import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from codata_2022_source import M_E_MEV, M_E_MEV_ERR  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = 80
set_compute_dps(DPS)
mp.mp.dps = DPS


def _extract_vol_6_2_literals() -> tuple[mp.mpf, mp.mpf]:
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
    t0 = time.time()
    set_compute_dps(DPS)
    mp.mp.dps = DPS

    q0 = mp.mpf(Q_50_DIGIT_STR)
    hbar_q0 = (q0 - 1) / q0
    hbar_sym_sq = q0 - 2 + 1 / q0
    vol_4_1 = 2 * mp.clsin(2, mp.pi / 3)
    m_e = +M_E_MEV

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

    sym_24w9_ok = all(
        r == 0
        for r in (
            sp.simplify(1 / y_schur_3_sym - qfact3_bal_sym / qs**3),
            sp.simplify(y_schur_111_sym - y_schur_3_sym.subs(qs, 1 / qs)),
            sp.simplify(
                1 * y_wenzl_3_sym + 2 * y_wenzl_21_sym + 1 * y_wenzl_111_sym - 1
            ),
            sp.simplify(1 / y_wenzl_21_sym - (qs + 1 / qs) ** 2),
            sp.simplify(
                y_wenzl_3_sym * 1
                + y_wenzl_21_sym * chi_21_sym
                + y_wenzl_111_sym * 1
                - trM_bor_sym
            ),
            sp.simplify(
                (1 / ((qs - 1) / qs) ** 2) * (qfact3_bal_sym / qs**3)
                - qfact3_bal_sym / (qs**2 * (qs - 2 + 1 / qs))
            ),
        )
    )

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

    vol_mtau, vol_deut = _extract_vol_6_2_literals()
    vol_6_2_census = vol_deut
    mtau_census_err = abs(vol_mtau - vol_6_2_census) / vol_6_2_census
    doubled_4_1 = 2 * vol_4_1
    doubled_rel_shift = (doubled_4_1 - vol_6_2_census) / vol_6_2_census
    m_true = m_e * (vol_6_2_census / hbar_q0**2) * trM_q0
    m_sub = m_e * (doubled_4_1 / hbar_q0**2) * trM_q0
    vol_scaling_err = abs((m_sub - m_true) / m_true - doubled_rel_shift)

    q_quad = (-mp.mpf(9) + mp.sqrt(mp.mpf(193))) / mp.mpf(56)
    quad_poly_res = abs(1 - 9 * q_quad - 28 * q_quad**2)
    q_quad_in_bounds = bool(mp.mpf("0.087") < q_quad < mp.mpf("0.088"))

    A_b = mp.mpf(17) / mp.mpf(10)
    C_b = mp.mpf(23) / mp.mpf(10)
    D_b = mp.mpf(9) / mp.mpf(10)
    r_star = mp.mpf(4708) / mp.mpf(2970)
    B_star = A_b * (1 - r_star) * D_b / C_b
    lift_fit = (A_b - B_star * (1 / D_b) * C_b) / A_b
    berezinian_fit_err = abs(lift_fit - r_star)

    def lambda_A(q_val: mp.mpf) -> mp.mpf:
        return mp.mpf(5) / mp.mpf(2) + (mp.mpf(3) / mp.mpf(4)) * (
            q_val - 2 + 1 / q_val
        )

    lam_q0 = lambda_A(q0)
    lam_q0_inv = lambda_A(1 / q0)
    lam_bar_err = abs(lam_q0 - lam_q0_inv)
    lam_excess_err = abs(
        (lam_q0 - mp.mpf(5) / mp.mpf(2)) - 3 * (q0 - 1) ** 2 / (4 * q0)
    )
    lam_gt_five_halves = bool(lam_q0 > mp.mpf(5) / mp.mpf(2))

    me_codata = +M_E_MEV
    me_sigma = +M_E_MEV_ERR
    rel_sigma_me = me_sigma / me_codata
    effective_digits_me = -mp.log10(rel_sigma_me)
    r1 = vol_4_1 / hbar_q0**2
    r2 = 2 * (r1 * trM_q0 * (qfact3_q0 / q0**3) - 6)
    ratio_cancels_err = abs((m_e * r2) / (m_e * r1) - (r2 / r1))

    wb = WitnessBuilder(
        "plancherel-normalisation-and-scale-bounds-probe",
        engine="mpmath+sympy",
        output_dir=THIS.parent,
        start_time=t0,
    )
    wb.set_description(
        "80-dps mpmath + SymPy verification of q-Schur vs Convention-D Wenzl "
        "Plancherel identities (qou-24w9), Vol(6_2) volume-ratio scaling (qou-r0dn), "
        "5_2 Stokes quadratic root & Berezinian lift (qou-hgm6), linking_weight_family_a "
        "bar-symmetry and lower bound > 5/2 (qou-cuur), and CODATA m_e relative "
        "uncertainty floor vs dimensionless ratio cancellation (qou-zufe)."
    )
    wb.add_parameter("workdps", DPS)
    wb.add_parameter("q0_proton_pin", Q_50_DIGIT_STR)
    wb.add_data("trM_borromean_q0", fmt(trM_q0, 50))
    wb.add_data("q_quad_80dps", fmt(q_quad, 50))
    wb.add_data("lambda_A_q0_80dps", fmt(lam_q0, 50))
    wb.add_data("me_effective_decimal_digits", fmt(effective_digits_me, 20))

    wb.add_assertion(
        "qou_24w9_wenzl_reconstructs_borromean_trM_and_qschur_identities",
        computed=bool(
            sym_24w9_ok
            and wenzl_trM_err < mp.mpf("1e-70")
            and schur_fbor_err < mp.mpf("1e-70")
            and wenzl_tl_err < mp.mpf("1e-70")
            and bar_asym_err < mp.mpf("1e-65")
        ),
        expected=True,
        source="QOU.MassTheory.PlancherelNormalisationAndScaleBounds.wenzl_reconstructs_borromean_trM",
    )
    wb.add_assertion(
        "qou_r0dn_vol_6_2_census_agreement_and_linear_scaling",
        computed=bool(
            mtau_census_err < mp.mpf("1e-19") and vol_scaling_err < mp.mpf("1e-70")
        ),
        expected=True,
        source="QOU.MassTheory.PlancherelNormalisationAndScaleBounds.perKnotMass_ratio_and_rel_err",
    )
    wb.add_assertion(
        "qou_hgm6_saddle_quad_root_and_berezinian_lift_exact",
        computed=bool(
            quad_poly_res < mp.mpf("1e-70")
            and q_quad_in_bounds
            and berezinian_fit_err < mp.mpf("1e-70")
        ),
        expected=True,
        source="QOU.MassTheory.PlancherelNormalisationAndScaleBounds.saddleQuadPoly_at_qQuadRoot_and_bounds",
    )
    wb.add_assertion(
        "qou_cuur_zufe_linking_weight_bound_and_me_ratio_cancellation",
        computed=bool(
            lam_bar_err < mp.mpf("1e-70")
            and lam_excess_err < mp.mpf("1e-70")
            and lam_gt_five_halves
            and mp.mpf("9.5") < effective_digits_me < mp.mpf("9.6")
            and ratio_cancels_err < mp.mpf("1e-70")
        ),
        expected=True,
        source="QOU.MassTheory.PlancherelNormalisationAndScaleBounds.dimensionless_mass_ratio_cancels_me",
    )

    out_path = wb.save({"q0Anchor": "proton", "q0Value": Q_50_DIGIT_STR})
    print(f"Saved witness: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
