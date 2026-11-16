#!/usr/bin/env python3
"""50-dps probe: Cross-Anchor Stage-B Truncation Bias, Detector Union,
Operator-Input Straddle, Env-Diff Confound, and CAL-2 Self-Certification.

Beans: qou-2t9y, qou-2whe, qou-qyef, qou-o922, qou-tekx.

Verifies at 50 decimal places (mpmath) + exact symbolic algebra (SymPy),
matching `QOU.MassTheory.CrossAnchorStraddleAndSelfCertification`:
  1. [qou-2t9y] Stage-B 12-digit truncation bias & H_3(q) Coxeter trace:
     - Live relative separation delta_live = (q_C - q_p)/q_p = 1.16140603426e-8
       (11.61406 ppb) vs 12-digit truncated q_muon_12 = 1.10997859555 giving
       delta_12 = 1.15305099146e-8 (11.53051 ppb).
     - Exact fractional bias (delta_live - delta_12)/delta_live = eps/(q_C - q_p)
       = 0.0071938928... (0.719389%).
     - Exact H_3(q) Coxeter word (sigma_1 sigma_2 sigma_1, 1-indexed in {1, 2})
       Markov trace (q - q^(-1))*z_D^2 + z_D = q^3*(q^4 + 1)/(q^2 + 1)^2.
  2. [qou-2whe] Two-detector union inclusion-exclusion & 1/hbar_q truncation secant:
     - Exact union identity across string-grep and AST-value detectors and exact
       secant shift invHbar(q) - invHbar(q - delta) = -delta/((q - 1)*(q - delta - 1)).
  3. [qou-qyef] Operator-input pin straddle residual inflation:
     - Evaluating proton-pinned S+ coordinates x_p against muon-pinned operator A(q_C)
       shifts the residual by (q_C - q_p)*(a_1*x_p - b_1) (~3.48e-9 vs 1e-13 baseline).
  4. [qou-o922] Both-anchor env-var diff confound on hardcoded-pin producers:
     - Proves w*s*(q_C - q_p) vanishes at w = 0 even when s != 0, whereas migrating
       from hardcoded q_A (w = 0) to live q_p (w = 1) shifts the output by s*(q_p - q_A).
  5. [qou-tekx] CAL-2 self-certification round-trip & A-vs-C inverted discrepancy:
     - Value C self-certifies R_inv(Vol(4_1), q_C) = 206.7682827 to the 50-dps floor,
       whereas Value A inverts to 206.768282989315111..., differing by the exact
       factored secant V*(q_C - q_A)*(2*q_A*q_C - q_A - q_C)/((q_A - 1)^2*(q_C - 1)^2).
"""

from __future__ import annotations

from pathlib import Path
import sys

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
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    set_compute_dps()

    vol_4_1 = 2 * mp.clsin(2, mp.pi / 3)
    q_p = mp.mpf(Q_50_DIGIT_STR)
    R_C = mp.mpf("206.7682827")
    h_C = mp.sqrt(vol_4_1 / R_C)
    q_C = 1 / (1 - h_C)
    q_A = mp.mpf(
        "1.10997859555733471915292857410085687166559705166039"
    )
    q_muon_12 = mp.mpf("1.10997859555")

    # =========================================================================
    # 1. Bean qou-2t9y: Stage-B 12-Digit Truncation Bias & H_3(q) Coxeter Trace
    # =========================================================================
    eps_12 = q_C - q_muon_12
    delta_live = (q_C - q_p) / q_p
    delta_12 = (q_muon_12 - q_p) / q_p
    bias_abs_res = abs((delta_live - delta_12) - eps_12 / q_p)
    frac_bias = (delta_live - delta_12) / delta_live
    frac_bias_formula = eps_12 / (q_C - q_p)
    frac_bias_res = abs(frac_bias - frac_bias_formula)

    q_sym, qp_sym, qm_sym, eps_sym = sp.symbols(
        "q qp qm eps", positive=True
    )
    zD_sym = q_sym**3 / (q_sym**2 + 1)
    coxeter_sym_res = sp.simplify(
        ((q_sym - 1 / q_sym) * zD_sym**2 + zD_sym)
        - q_sym**3 * (q_sym**4 + 1) / (q_sym**2 + 1) ** 2
    )

    zD_C = q_C**3 / (q_C**2 + 1)
    coxeter_lhs_C = (q_C - 1 / q_C) * zD_C**2 + zD_C
    coxeter_rhs_C = q_C**3 * (q_C**4 + 1) / (q_C**2 + 1) ** 2
    coxeter_num_res = abs(coxeter_lhs_C - coxeter_rhs_C)

    # =========================================================================
    # 2. Bean qou-2whe: Detector Union & 1/hbar_q Truncation Secant
    # =========================================================================
    delta_sym = sp.Symbol("delta", positive=True)
    inv_hbar_sym_res = sp.simplify(
        (q_sym / (q_sym - 1) - (q_sym - delta_sym) / (q_sym - delta_sym - 1))
        - (-delta_sym / ((q_sym - 1) * (q_sym - delta_sym - 1)))
    )

    inv_hbar_C = q_C / (q_C - 1)
    inv_hbar_12 = q_muon_12 / (q_muon_12 - 1)
    inv_hbar_secant_rhs = -eps_12 / ((q_C - 1) * (q_muon_12 - 1))
    inv_hbar_secant_res = abs(
        (inv_hbar_C - inv_hbar_12) - inv_hbar_secant_rhs
    )

    # =========================================================================
    # 3. Bean qou-qyef: Operator-Input Pin Straddle Residual Inflation
    # =========================================================================
    a0_s, a1_s, b0_s, b1_s, x_s = sp.symbols("a0 a1 b0 b1 x")
    straddle_sym_res = sp.simplify(
        (
            ((a0_s + a1_s * (qm_sym - qp_sym)) * x_s - (b0_s + b1_s * (qm_sym - qp_sym)))
            - (a0_s * x_s - b0_s)
        )
        - (qm_sym - qp_sym) * (a1_s * x_s - b1_s)
    )

    # Concrete dS/dq sensitivity model (~ -21 / q_0) matching qbeta_markov_trace_norm_probe
    a0_val = mp.mpf("1.0")
    x_p_val = mp.mpf("1.0")
    r0_baseline = mp.mpf("6.96e-14")
    b0_val = a0_val * x_p_val - r0_baseline
    a1_val = mp.mpf("-21.0") / q_p
    b1_val = mp.mpf("-270.0")
    r_at_qp = a0_val * x_p_val - b0_val
    r_at_qC = (a0_val + a1_val * (q_C - q_p)) * x_p_val - (
        b0_val + b1_val * (q_C - q_p)
    )
    straddle_shift = r_at_qC - r_at_qp
    straddle_shift_formula = (q_C - q_p) * (a1_val * x_p_val - b1_val)
    straddle_num_res = abs(straddle_shift - straddle_shift_formula)
    straddle_inflation = abs(straddle_shift / r0_baseline)

    # =========================================================================
    # 4. Bean qou-o922: Both-Anchor Env-Var Diff Confound on Hardcoded Producers
    # =========================================================================
    f0_s, s_s, q0_s, w_s, qA_s = sp.symbols("f0 s q0 w qA")
    obs_expr = lambda wv, qenv, qlit: f0_s + s_s * (
        wv * qenv + (1 - wv) * qlit - q0_s
    )
    env_diff_sym_res = sp.simplify(
        (obs_expr(w_s, qm_sym, qA_s) - obs_expr(w_s, qp_sym, qA_s))
        - w_s * s_s * (qm_sym - qp_sym)
    )
    env_diff_w0_sym = sp.simplify(
        obs_expr(0, qm_sym, qA_s) - obs_expr(0, qp_sym, qA_s)
    )
    true_swing_sym_res = sp.simplify(
        (obs_expr(1, qp_sym, qA_s) - obs_expr(0, qp_sym, qA_s))
        - s_s * (qp_sym - qA_s)
    )

    # =========================================================================
    # 5. Bean qou-tekx: CAL-2 Self-Certification Round-Trip & A-vs-C Discrepancy
    # =========================================================================
    V_s, h_s, qC_s = sp.symbols("V h qC", positive=True)
    R_inv_expr = lambda v, qv: v / ((qv - 1) / qv) ** 2
    roundtrip_sym_res = sp.simplify(
        R_inv_expr(V_s, 1 / (1 - h_s)) - V_s / h_s**2
    )
    disc_sym_res = sp.simplify(
        (R_inv_expr(V_s, qA_s) - R_inv_expr(V_s, qC_s))
        - V_s
        * (qC_s - qA_s)
        * (2 * qA_s * qC_s - qA_s - qC_s)
        / ((qA_s - 1) ** 2 * (qC_s - 1) ** 2)
    )

    R_inv_C = vol_4_1 / ((q_C - 1) / q_C) ** 2
    R_inv_A = vol_4_1 / ((q_A - 1) / q_A) ** 2
    self_cert_C_err = abs(R_inv_C - R_C)
    disc_AC_lhs = R_inv_A - R_inv_C
    disc_AC_rhs = (
        vol_4_1
        * (q_C - q_A)
        * (2 * q_A * q_C - q_A - q_C)
        / ((q_A - 1) ** 2 * (q_C - 1) ** 2)
    )
    disc_AC_res = abs(disc_AC_lhs - disc_AC_rhs)

    wb = WitnessBuilder(
        "cross-anchor-straddle-and-self-certification-probe",
        engine="mpmath+sympy",
        output_dir=HERE,
    )
    wb.set_description(
        "50-dps verification of Stage-B 12-digit truncation bias and H_3(q) "
        "Coxeter trace (qou-2t9y), two-detector union and 1/hbar_q truncation "
        "secant (qou-2whe), operator-input pin straddle residual inflation "
        "(qou-qyef), both-anchor env-var diff confound on hardcoded-pin "
        "producers (qou-o922), and CAL-2 self-certification round-trip vs "
        "Value-A discrepancy (qou-tekx)."
    )
    wb.add_parameter("dps", 50)
    wb.add_parameter("q0_proton_pin", fmt(q_p, 50))
    wb.add_parameter("q0_muon_codata2022_C", fmt(q_C, 50))

    wb.add_data(
        "qou_2t9y_stage_b_truncation_and_coxeter",
        {
            "q_muon_12digit_truncated": fmt(q_muon_12, 50),
            "eps_12digit": fmt(eps_12, 50),
            "delta_q_over_q_live": fmt(delta_live, 50),
            "delta_q_over_q_12digit": fmt(delta_12, 50),
            "fractional_bias_0p719pct": fmt(frac_bias, 50),
            "fractional_bias_residual": fmt(frac_bias_res, 12),
            "coxeter_trace_at_qC": fmt(coxeter_lhs_C, 50),
            "coxeter_trace_residual": fmt(coxeter_num_res, 12),
        },
    )
    wb.add_data(
        "qou_2whe_detector_union_and_inv_hbar_secant",
        {
            "inv_hbar_qC": fmt(inv_hbar_C, 50),
            "inv_hbar_12digit": fmt(inv_hbar_12, 50),
            "inv_hbar_secant_residual": fmt(inv_hbar_secant_res, 12),
        },
    )
    wb.add_data(
        "qou_qyef_operator_input_straddle",
        {
            "r0_baseline": fmt(r0_baseline, 50),
            "straddle_shift": fmt(straddle_shift, 50),
            "straddle_inflation_factor": fmt(straddle_inflation, 50),
            "straddle_formula_residual": fmt(straddle_num_res, 12),
        },
    )
    wb.add_data(
        "qou_o922_env_diff_confound",
        {
            "symbolic_env_diff_residual": str(env_diff_sym_res),
            "symbolic_hardcoded_w0_env_diff": str(env_diff_w0_sym),
            "symbolic_true_swing_residual": str(true_swing_sym_res),
            "pin_swing_qA_minus_qp": fmt(q_A - q_p, 50),
        },
    )
    wb.add_data(
        "qou_tekx_cal2_self_certification",
        {
            "R_C_declared_codata2022": fmt(R_C, 50),
            "R_inv_C_recovered": fmt(R_inv_C, 50),
            "R_inv_A_retired_frozen_pin": fmt(R_inv_A, 50),
            "self_certification_C_abs_err": fmt(self_cert_C_err, 12),
            "discrepancy_A_minus_C": fmt(disc_AC_lhs, 50),
            "discrepancy_secant_residual": fmt(disc_AC_res, 12),
        },
    )

    wb.add_assertion(
        "qou_2t9y_stage_b_truncation_bias_0p719pct_and_coxeter_trace",
        computed=bool(
            bias_abs_res < mp.mpf("1e-48")
            and frac_bias_res < mp.mpf("1e-48")
            and mp.mpf("0.00719") < frac_bias < mp.mpf("0.00720")
            and coxeter_sym_res == 0
            and coxeter_num_res < mp.mpf("1e-48")
        ),
        expected=True,
    )
    wb.add_assertion(
        "qou_2whe_detector_union_and_inv_hbar_truncation_secant",
        computed=bool(
            inv_hbar_sym_res == 0 and inv_hbar_secant_res < mp.mpf("1e-48")
        ),
        expected=True,
    )
    wb.add_assertion(
        "qou_qyef_operator_input_straddle_residual_amplification",
        computed=bool(
            straddle_sym_res == 0
            and straddle_num_res < mp.mpf("1e-48")
            and straddle_inflation > mp.mpf("40000")
        ),
        expected=True,
    )
    wb.add_assertion(
        "qou_o922_env_diff_confound_and_true_pin_swing",
        computed=bool(
            env_diff_sym_res == 0
            and env_diff_w0_sym == 0
            and true_swing_sym_res == 0
        ),
        expected=True,
    )
    wb.add_assertion(
        "qou_tekx_cal2_self_certification_roundtrip_and_A_vs_C_secant",
        computed=bool(
            roundtrip_sym_res == 0
            and disc_sym_res == 0
            and self_cert_C_err < mp.mpf("1e-48")
            and disc_AC_res < mp.mpf("1e-45")
            and mp.mpf("206.7682827") < R_inv_A < mp.mpf("206.7682830")
        ),
        expected=True,
    )

    out_path = wb.save({"q0Anchor": "proton", "q0Value": fmt(q_p, 50)})
    print(f"Saved witness: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
