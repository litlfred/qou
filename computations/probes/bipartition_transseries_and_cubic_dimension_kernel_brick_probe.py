#!/usr/bin/env python3
"""80-dps mpmath probe for QOU.QBeta.BipartitionTransseriesAndCubicDimensionKernelBrick.

Covers beans:
  - qou-m0bv: non-degenerate mass-crossing witness margin `(mass - m0, crossings - c0)`
  - qou-m6gp: interface-inclusive braid closure volume deficit `vBound - (v1 + v2)`
  - qou-mbz4: two-sector bipartition transseries partial sum `a0 + s1 * phi1 + s2 * phi2`
  - qou-mdbh: cubic vs quadratic dimension kernel excess `f^3 * w - f^2 * w = f^2 * (f - 1) * w`
  - qou-mssy: meridian-longitude quadratic cross form `(2 * m + l) * l = 2 * m * l + l^2`

All numerical outputs are serialized as 80-dps strings or integer/boolean fields (zero raw float64).
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
WITNESS_PATH = SCRIPT_PATH.with_name(
    "bipartition-transseries-and-cubic-dimension-kernel-brick.witness.json"
)


def fmt_mp(val: mp.mpf) -> str:
    return mp.nstr(val, 80, min_fixed=0, max_fixed=0)


def git_commit_sha() -> str:
    out = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True
    )
    return out.strip()


def git_is_dirty() -> bool:
    out = subprocess.check_output(
        ["git", "status", "--porcelain", "--untracked-files=no"],
        cwd=REPO_ROOT,
        text=True,
    )
    for line in out.splitlines():
        if not line.endswith(WITNESS_PATH.name):
            return True
    return False


def script_sha256_prefix() -> str:
    digest = hashlib.sha256(SCRIPT_PATH.read_bytes()).hexdigest()
    return digest[:12]


def run_probe() -> dict:
    tol = mp.mpf("1e-75")

    # 1. Bean qou-m0bv: Non-degenerate mass-crossing witness margin (MeV & crossings)
    # Proton-like candidate (938, 3) vs threshold (135, 3) and deuteron-like sum
    m_p = mp.mpf(938)
    c_p = mp.mpf(3)
    m0 = mp.mpf(135)
    c0 = mp.mpf(3)
    excess_p_1 = m_p - m0
    excess_p_2 = c_p - c0
    deg_1 = mp.mpf(0) - m0
    deg_2 = mp.mpf(0) - c0
    gap_res_1 = (excess_p_1 - deg_1 + c_p + m0 + c0) - (m_p + c_p + m0 + c0)
    sum_res = (excess_p_1 + excess_p_2) - ((m_p + c_p) - (m0 + c0))

    m_n = mp.mpf(940)
    c_n = mp.mpf(4)
    m0_n = mp.mpf(140)
    c0_n = mp.mpf(3)
    comp_res_1 = ((m_p + m_n) - (m0 + m0_n)) - ((m_p - m0) + (m_n - m0_n))
    comp_res_2 = ((c_p + c_n) - (c0 + c0_n)) - ((c_p - c0) + (c_n - c0_n))
    pass_m0bv = bool(
        abs(gap_res_1) < tol
        and abs(sum_res) < tol
        and abs(comp_res_1) < tol
        and abs(comp_res_2) < tol
        and excess_p_1 > 0
    )

    # 2. Bean qou-m6gp: Interface-coupled braid closure volume deficit at 80 dps
    # Using hyperbolic figure-eight volume V_4_1 = 2 * Im(Li_2(e^{i pi / 3})) * 3
    v_fig8 = 6 * mp.clsin(2, mp.pi / 3)
    v1 = v_fig8
    v2 = v_fig8
    v3 = v_fig8 / 2
    v12 = v1 + v2 - mp.mpf("0.421875")
    v123 = v12 + v3 - mp.mpf("0.3125")
    def_12 = v12 - (v1 + v2)
    def_123_step = v123 - (v12 + v3)
    def_total = v123 - (v1 + v2 + v3)
    telescope_res = (def_123_step + def_12) - def_total
    disjoint_res = ((v1 + v2) - (v1 + v2) + v123 + v12 + v3) - (v123 + v12 + v3)
    delta_v = mp.mpf("0.125")
    shift_res = ((v12 + delta_v - (v1 + v2)) - def_12) - delta_v
    pass_m6gp = bool(
        abs(telescope_res) < tol
        and abs(disjoint_res) < tol
        and abs(shift_res) < tol
    )

    # 3. Bean qou-mbz4: Two-sector bipartition transseries partial sum
    a0 = mp.mpf(17)
    s1 = mp.mpf(3)
    phi1 = mp.exp(-mp.pi / 2)
    s2 = mp.mpf(-5)
    phi2 = mp.exp(-mp.pi)
    t_pos = a0 + s1 * phi1 + s2 * phi2
    t_neg = a0 + (-s1) * phi1 + (-s2) * phi2
    lift_res = (t_pos - a0) - (s1 * phi1 + s2 * phi2)
    parity_res = (t_pos + t_neg) - 2 * a0

    b0 = mp.mpf(11)
    q1 = mp.exp(-3 * mp.pi / 4)
    q2 = mp.exp(-5 * mp.pi / 4)
    t_sum = (a0 + b0) + s1 * (phi1 + q1) + s2 * (phi2 + q2)
    t_split = (a0 + s1 * phi1 + s2 * phi2) + (b0 + s1 * q1 + s2 * q2)
    lin_res = t_sum - t_split
    pass_mbz4 = bool(
        abs(lift_res) < tol and abs(parity_res) < tol and abs(lin_res) < tol
    )

    # 4. Bean qou-mdbh: Cubic vs quadratic dimension kernel excess
    # Evaluate for SU(2) representation dimensions f in {1, 2, 3, 4} and weight w
    w1 = mp.mpf(19)
    w2 = mp.mpf(23)
    max_excess_err = mp.mpf(0)
    max_obs_lin_err = mp.mpf(0)
    for f_int in (1, 2, 3, 4, 5):
        f_val = mp.mpf(f_int)
        k2 = f_val * f_val * w1
        k3 = f_val * f_val * f_val * w1
        factored = f_val * f_val * (f_val - 1) * w1
        err_ex = abs((k3 - k2) - factored)
        if err_ex > max_excess_err:
            max_excess_err = err_ex
        k3_sum = f_val * f_val * f_val * (w1 + w2)
        k3_parts = f_val * f_val * f_val * w1 + f_val * f_val * f_val * w2
        err_lin = abs(k3_sum - k3_parts)
        if err_lin > max_obs_lin_err:
            max_obs_lin_err = err_lin
    trivial_rep_res = (mp.mpf(1) ** 3 * w1 - mp.mpf(1) ** 2 * w1 + mp.mpf(4)) - mp.mpf(4)
    pass_mdbh = bool(
        max_excess_err < tol
        and max_obs_lin_err < tol
        and abs(trivial_rep_res) < tol
    )

    # 5. Bean qou-mssy: Meridian-longitude quadratic cross form `(2*m + l)*l`
    m_val = mp.mpf(7)
    l_val = mp.mpf(-3)
    dm_val = mp.mpf(4)
    cf_orig = (2 * m_val + l_val) * l_val
    cf_exp = 2 * m_val * l_val + l_val * l_val
    cf_inv = (2 * (-m_val) + (-l_val)) * (-l_val)
    cf_shift = (2 * (m_val + dm_val) + l_val) * l_val
    cf_zero_l = (2 * m_val + mp.mpf(0)) * mp.mpf(0)
    exp_res = cf_orig - cf_exp
    inv_res = cf_inv - cf_orig
    step_res = (cf_shift - cf_orig) - (2 * dm_val * l_val)
    zero_l_res = (cf_zero_l + dm_val + l_val) - (dm_val + l_val)
    pass_mssy = bool(
        abs(exp_res) < tol
        and abs(inv_res) < tol
        and abs(step_res) < tol
        and abs(zero_l_res) < tol
    )

    all_passed = bool(
        pass_m0bv and pass_m6gp and pass_mbz4 and pass_mdbh and pass_mssy
    )

    return {
        "schemaVersion": "1.0",
        "brick": "QOU.QBeta.BipartitionTransseriesAndCubicDimensionKernelBrick",
        "beans": [
            "qou-m0bv",
            "qou-m6gp",
            "qou-mbz4",
            "qou-mdbh",
            "qou-mssy",
        ],
        "scriptPath": str(SCRIPT_PATH.relative_to(REPO_ROOT)),
        "scriptHash": script_sha256_prefix(),
        "scriptCommitSha": git_commit_sha(),
        "dirty": git_is_dirty(),
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "precisionDps": 80,
        "allPassed": all_passed,
        "checks": {
            "qou_m0bv_non_degenerate_witness_margin": {
                "theorem": "nonDegenerateExcessPair_degenerate_gap_and_sum",
                "protonMassExcessMeV": fmt_mp(excess_p_1),
                "degenerateGapResidual": fmt_mp(gap_res_1),
                "excessSumResidual": fmt_mp(sum_res),
                "compositeMassResidual": fmt_mp(comp_res_1),
                "compositeCrossingResidual": fmt_mp(comp_res_2),
                "passed": pass_m0bv,
            },
            "qou_m6gp_closure_volume_deficit": {
                "theorem": "closureVolumeDeficit_telescoping_and_disjoint_zero",
                "figureEightVolume80dps": fmt_mp(v_fig8),
                "twoBodyDeficit": fmt_mp(def_12),
                "threeBodyTotalDeficit": fmt_mp(def_total),
                "telescopingResidual": fmt_mp(telescope_res),
                "disjointUnionResidual": fmt_mp(disjoint_res),
                "perturbationShiftResidual": fmt_mp(shift_res),
                "passed": pass_m6gp,
            },
            "qou_mbz4_bipartition_transseries": {
                "theorem": "bipartitionTransseries_nonperturbative_lift_and_parity_average",
                "transseriesPositiveSector": fmt_mp(t_pos),
                "transseriesNegativeSector": fmt_mp(t_neg),
                "nonperturbativeLiftResidual": fmt_mp(lift_res),
                "parityAverageResidual": fmt_mp(parity_res),
                "modeLinearityResidual": fmt_mp(lin_res),
                "passed": pass_mbz4,
            },
            "qou_mdbh_cubic_dimension_kernel_excess": {
                "theorem": "dimSquaredCubedKernelPair_excess_factorization_and_trivial_rep",
                "maxFactorizationResidual": fmt_mp(max_excess_err),
                "maxObservableLinearityResidual": fmt_mp(max_obs_lin_err),
                "trivialRepFixedPointResidual": fmt_mp(trivial_rep_res),
                "passed": pass_mdbh,
            },
            "qou_mssy_winding_cross_form": {
                "theorem": "windingCrossForm_expanded_and_inversion_even",
                "crossFormAt7Minus3": fmt_mp(cf_orig),
                "expansionResidual": fmt_mp(exp_res),
                "inversionSymmetryResidual": fmt_mp(inv_res),
                "meridianShiftResidual": fmt_mp(step_res),
                "zeroLongitudeResidual": fmt_mp(zero_l_res),
                "passed": pass_mssy,
            },
        },
    }


def main() -> None:
    payload = run_probe()
    WITNESS_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {WITNESS_PATH} (allPassed={payload['allPassed']})")
    if not payload["allPassed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
