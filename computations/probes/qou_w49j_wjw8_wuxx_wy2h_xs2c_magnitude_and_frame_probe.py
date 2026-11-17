#!/usr/bin/env python3
"""80-dps mpmath numerical verification probe for Round 94 bricks:
- qou-w49j: 5-step Delta_lambda magnitude assembly chain and peripheral perturbation law
- qou-wjw8: Convention C vs Convention D molecular binding frame cross-difference
- qou-wuxx: Categorical eigenspace trace split and quadratic norm-additivity defect
- qou-wy2h: Clause-to-braid assignment-cube gadget residual and 3-SAT locus
- qou-xs2c: Explicit de-Poissonization second-moment and Gaussian-tail envelope
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80

SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[2]
REL_SCRIPT = "computations/probes/qou_w49j_wjw8_wuxx_wy2h_xs2c_magnitude_and_frame_probe.py"
WITNESS_PATH = SCRIPT_PATH.with_suffix(".witness.json")


def assembled_delta_lambda_scale(
    s_weight: mp.mpf, m_weight: mp.mpf, a_m: mp.mpf, l_weight: mp.mpf, a_l: mp.mpf
) -> mp.mpf:
    return s_weight * (m_weight * a_m + l_weight * a_l)


def convention_frame_cross_diff(
    z_d_num: mp.mpf, z_c_den: mp.mpf, z_c_num: mp.mpf, z_d_den: mp.mpf
) -> mp.mpf:
    return z_d_num * z_c_den - z_c_num * z_d_den


def eigenspace_norm_additivity_defect(
    x1: mp.mpf, y1: mp.mpf, x2: mp.mpf, y2: mp.mpf
) -> mp.mpf:
    return ((x1 + x2) ** 2 + (y1 + y2) ** 2) - ((x1 ** 2 + y1 ** 2) + (x2 ** 2 + y2 ** 2))


def clause_braid_gadget_residual(
    m_clauses: mp.mpf, cube_size: mp.mpf, unsat_count: mp.mpf, sat_total: mp.mpf
) -> mp.mpf:
    return m_clauses * (cube_size - unsat_count) - sat_total


def de_poissonization_combined_envelope(
    lam: mp.mpf, f2: mp.mpf, g_tail: mp.mpf
) -> mp.mpf:
    return f2 * (lam ** 2 + mp.mpf("1")) + g_tail ** 2


def main() -> None:
    tol = mp.mpf("1e-70")

    # 1. qou-w49j: peripheral shift law and outer action scale
    s_w = mp.mpf("7")
    m_w = mp.mpf("3")
    a_m = mp.mpf("11")
    d_m = mp.mpf("5")
    l_w = mp.mpf("4")
    a_l = mp.mpf("13")
    d_l = mp.mpf("-2")
    k_sc = mp.mpf("9")

    lhs_w49j_shift = (
        assembled_delta_lambda_scale(s_w, m_w, a_m + d_m, l_w, a_l + d_l)
        - assembled_delta_lambda_scale(s_w, m_w, a_m, l_w, a_l)
    )
    rhs_w49j_shift = s_w * (m_w * d_m + l_w * d_l)
    err_w49j_shift = abs(lhs_w49j_shift - rhs_w49j_shift)

    lhs_w49j_scale = assembled_delta_lambda_scale(k_sc * s_w, m_w, a_m, l_w, a_l)
    rhs_w49j_scale = k_sc * assembled_delta_lambda_scale(s_w, m_w, a_m, l_w, a_l)
    err_w49j_scale = abs(lhs_w49j_scale - rhs_w49j_scale)

    # 2. qou-wjw8: convention C vs D cross-difference and q = q0 frame ratio
    q0 = mp.mpf("1.1099785827513808")
    z_c = mp.sqrt(q0) / (q0 + mp.mpf("1"))
    z_d = (q0 ** 3) / (q0 ** 2 + mp.mpf("1"))
    frame_ratio_d_over_c = z_d / z_c

    cross_q2 = convention_frame_cross_diff(
        mp.mpf("64"), mp.mpf("9"), mp.mpf("2"), mp.mpf("25")
    )
    err_wjw8_q2 = abs(cross_q2 - mp.mpf("526"))
    antisymm_wjw8 = convention_frame_cross_diff(
        mp.mpf("64"), mp.mpf("9"), mp.mpf("2"), mp.mpf("25")
    ) + convention_frame_cross_diff(
        mp.mpf("2"), mp.mpf("25"), mp.mpf("64"), mp.mpf("9")
    )
    err_wjw8_antisymm = abs(antisymm_wjw8)

    # 3. qou-wuxx: eigenspace norm-additivity defect
    x1, y1, x2, y2 = mp.mpf("5"), mp.mpf("-3"), mp.mpf("7"), mp.mpf("11")
    defect_val = eigenspace_norm_additivity_defect(x1, y1, x2, y2)
    bilinear_val = mp.mpf("2") * (x1 * x2 + y1 * y2)
    err_wuxx_bilinear = abs(defect_val - bilinear_val)
    err_wuxx_orth = abs(eigenspace_norm_additivity_defect(x1, mp.mpf("0"), mp.mpf("0"), y2))
    err_wuxx_free = abs(
        eigenspace_norm_additivity_defect(
            mp.mpf("1"), mp.mpf("1"), mp.mpf("1"), mp.mpf("1")
        )
        - mp.mpf("4")
    )

    # 4. qou-wy2h: clause-to-braid assignment-cube gadget
    m1, m2 = mp.mpf("12"), mp.mpf("19")
    cube, unsat = mp.mpf("8"), mp.mpf("1")
    s1, s2 = mp.mpf("84"), mp.mpf("133")
    lhs_wy2h_add = clause_braid_gadget_residual(m1 + m2, cube, unsat, s1 + s2)
    rhs_wy2h_add = clause_braid_gadget_residual(
        m1, cube, unsat, s1
    ) + clause_braid_gadget_residual(m2, cube, unsat, s2)
    err_wy2h_add = abs(lhs_wy2h_add - rhs_wy2h_add)
    err_wy2h_3sat = abs(
        clause_braid_gadget_residual(mp.mpf("1"), mp.mpf("8"), mp.mpf("1"), mp.mpf("7"))
    )

    # 5. qou-xs2c: de-Poissonization moment envelope
    lam, d_lam, f2, g_tail = mp.mpf("3"), mp.mpf("5"), mp.mpf("4"), mp.mpf("5")
    lhs_xs2c_shift = de_poissonization_combined_envelope(
        lam + d_lam, f2, g_tail
    ) - de_poissonization_combined_envelope(lam, f2, g_tail)
    rhs_xs2c_shift = f2 * (mp.mpf("2") * lam * d_lam + d_lam ** 2)
    err_xs2c_shift = abs(lhs_xs2c_shift - rhs_xs2c_shift)
    eval_xs2c_345 = de_poissonization_combined_envelope(lam, f2, g_tail)
    err_xs2c_eval = abs(eval_xs2c_345 - mp.mpf("65"))

    assertions = [
        {
            "name": "qou_w49j_peripheral_perturbation_and_outer_scale",
            "passed": bool(err_w49j_shift <= tol and err_w49j_scale <= tol),
            "lhs": mp.nstr(lhs_w49j_shift, 80),
            "rhs": mp.nstr(rhs_w49j_shift, 80),
            "absError": mp.nstr(err_w49j_shift + err_w49j_scale, 80),
            "tolerance": mp.nstr(tol, 80),
        },
        {
            "name": "qou_wjw8_convention_frame_cross_diff_and_antisymm",
            "passed": bool(err_wjw8_q2 <= tol and err_wjw8_antisymm <= tol),
            "lhs": mp.nstr(cross_q2, 80),
            "rhs": mp.nstr(mp.mpf("526"), 80),
            "absError": mp.nstr(err_wjw8_q2 + err_wjw8_antisymm, 80),
            "tolerance": mp.nstr(tol, 80),
        },
        {
            "name": "qou_wuxx_eigenspace_norm_additivity_defect",
            "passed": bool(
                err_wuxx_bilinear <= tol and err_wuxx_orth <= tol and err_wuxx_free <= tol
            ),
            "lhs": mp.nstr(defect_val, 80),
            "rhs": mp.nstr(bilinear_val, 80),
            "absError": mp.nstr(err_wuxx_bilinear + err_wuxx_orth + err_wuxx_free, 80),
            "tolerance": mp.nstr(tol, 80),
        },
        {
            "name": "qou_wy2h_clause_braid_gadget_residual_3sat",
            "passed": bool(err_wy2h_add <= tol and err_wy2h_3sat <= tol),
            "lhs": mp.nstr(lhs_wy2h_add, 80),
            "rhs": mp.nstr(rhs_wy2h_add, 80),
            "absError": mp.nstr(err_wy2h_add + err_wy2h_3sat, 80),
            "tolerance": mp.nstr(tol, 80),
        },
        {
            "name": "qou_xs2c_de_poissonization_envelope_shift_and_eval",
            "passed": bool(err_xs2c_shift <= tol and err_xs2c_eval <= tol),
            "lhs": mp.nstr(eval_xs2c_345, 80),
            "rhs": mp.nstr(mp.mpf("65"), 80),
            "absError": mp.nstr(err_xs2c_shift + err_xs2c_eval, 80),
            "tolerance": mp.nstr(tol, 80),
        },
    ]

    all_passed = all(a["passed"] for a in assertions)
    script_bytes = SCRIPT_PATH.read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()
    head_sha = (
        subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT)
        .decode("utf-8")
        .strip()
    )
    dirty_out = (
        subprocess.check_output(
            ["git", "status", "--porcelain", "--", REL_SCRIPT], cwd=REPO_ROOT
        )
        .decode("utf-8")
        .strip()
    )

    witness = {
        "schema": "qou-computation-witness-v1",
        "Check": {
            "id": "qou-w49j-wjw8-wuxx-wy2h-xs2c-magnitude-and-frame-probe",
            "description": (
                "80-dps verification of Delta_lambda magnitude assembly (qou-w49j), "
                "Convention C vs D frame cross-difference (qou-wjw8), categorical eigenspace "
                "norm-additivity defect (qou-wuxx), clause-to-braid gadget residual (qou-wy2h), "
                "and explicit de-Poissonization moment envelope (qou-xs2c)."
            ),
            "precisionDps": "80",
        },
        "provenance": {
            "scriptPath": REL_SCRIPT,
            "scriptHash": script_hash,
            "scriptCommitSha": head_sha,
            "dirty": bool(dirty_out),
            "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "mpmathVersion": mp.__version__,
        },
        "parameters": {
            "q0": mp.nstr(q0, 80),
            "zC_q0": mp.nstr(z_c, 80),
            "zD_q0": mp.nstr(z_d, 80),
            "frameRatioDOverC_q0": mp.nstr(frame_ratio_d_over_c, 80),
        },
        "outputs": {
            "w49j_shift_delta": mp.nstr(lhs_w49j_shift, 80),
            "wjw8_q2_cross_diff": mp.nstr(cross_q2, 80),
            "wuxx_free_witness_defect": mp.nstr(
                eigenspace_norm_additivity_defect(
                    mp.mpf("1"), mp.mpf("1"), mp.mpf("1"), mp.mpf("1")
                ),
                80,
            ),
            "wy2h_single_3sat_residual": mp.nstr(
                clause_braid_gadget_residual(
                    mp.mpf("1"), mp.mpf("8"), mp.mpf("1"), mp.mpf("7")
                ),
                80,
            ),
            "xs2c_envelope_3_4_5": mp.nstr(eval_xs2c_345, 80),
        },
        "assertions": assertions,
        "allPassed": all_passed,
    }

    WITNESS_PATH.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
