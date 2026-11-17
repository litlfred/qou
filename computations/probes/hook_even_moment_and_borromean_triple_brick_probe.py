#!/usr/bin/env python3
"""80-dps mpmath probe for QOU.QBeta.HookEvenMomentAndBorromeanTripleBrick.

Covers beans:
  - qou-ogrk: classical hook-content square excess `hSqSum - (cSqSum + n^2)` and sixth
              hook-moment cofactor `63 * c3 * (3 * n - 8)^2`
  - qou-ohaz: two-regime pair-collision separation-minus-core gap
              `(d0Sq - g * t) - (a0Sq + 4 * nu * t)`
  - qou-omr7: signed two-sector Magnus trace `wPos * tPos - wNeg * tNeg` and weight
              replacement shift
  - qou-ooqh: ordered Borromean 3-body triple count `a * (a - 1) * (a - 2)`, step
              recurrence, and 4He-to-3H fourfold ratio
  - qou-po72: de-Poissonized Cauchy-Schwarz correlation margin `25 * vA * vOmega - 24 * pSq`
              and exact correlation constant `rho_P^2 = 24 / 25`

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
    "hook-even-moment-and-borromean-triple-brick.witness.json"
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

    # 1. Bean qou-ogrk: Hook-content square excess and M_6 sixth-moment cofactor
    # Partition lambda = (3, 2, 1) of n = 6:
    # hooks: (5, 3, 1), (3, 1), (1) -> sum h^2 = 25 + 9 + 1 + 9 + 1 + 1 = 46
    # contents: (0, 1, 2), (-1, 0), (-2) -> sum c^2 = 0 + 1 + 4 + 1 + 0 + 4 = 10
    # n^2 = 36 -> cSqSum + n^2 = 46
    n_val = mp.mpf(6)
    h_sq_sum = mp.mpf(46)
    c_sq_sum = mp.mpf(10)
    c3_val = n_val * (n_val - 1) * (n_val - 2) / 3  # |C_3| = 40
    d_val = 3 * n_val - 8  # 10
    excess_res = h_sq_sum - (c_sq_sum + n_val * n_val)
    m6_pos = 63 * c3_val * d_val * d_val
    m6_neg = 63 * c3_val * (-d_val) * (-d_val)
    refl_res = m6_neg - m6_pos
    c3_a = mp.mpf(15)
    c3_b = mp.mpf(25)
    lin_c3_res = (63 * (c3_a + c3_b) * d_val * d_val) - (
        63 * c3_a * d_val * d_val + 63 * c3_b * d_val * d_val
    )
    pass_ogrk = bool(
        abs(excess_res) < tol
        and abs(refl_res) < tol
        and abs(lin_c3_res) < tol
        and m6_pos > 0
    )

    # 2. Bean qou-ohaz: Two-regime pair-collision viscous core race
    # d^2(t) = d0^2 - (Gamma / pi) * t vs a^2(t) = a0^2 + 4 * nu * t
    d0_sq = mp.mpf("4.0")
    a0_sq = mp.mpf("0.25")
    gamma_over_pi = 2 / mp.pi
    nu_val = mp.mpf("0.015625")
    t_val = mp.mpf("1.75")
    dt_val = mp.mpf("0.5")
    gap_t = (d0_sq - gamma_over_pi * t_val) - (a0_sq + 4 * nu_val * t_val)
    gap_rearranged = (d0_sq - a0_sq) - (gamma_over_pi + 4 * nu_val) * t_val
    gap_0 = (d0_sq - gamma_over_pi * 0) - (a0_sq + 4 * nu_val * 0)
    gap_t_dt = (d0_sq - gamma_over_pi * (t_val + dt_val)) - (
        a0_sq + 4 * nu_val * (t_val + dt_val)
    )
    rate_res = gap_t - gap_rearranged
    init_res = gap_0 - (d0_sq - a0_sq)
    step_res = (gap_t_dt - gap_t) - (-(gamma_over_pi + 4 * nu_val) * dt_val)
    t_cross = (d0_sq - a0_sq) / (gamma_over_pi + 4 * nu_val)
    t_coll = d0_sq / gamma_over_pi
    pass_ohaz = bool(
        abs(rate_res) < tol
        and abs(init_res) < tol
        and abs(step_res) < tol
        and 0 < t_cross < t_coll
    )

    # 3. Bean qou-omr7: Signed two-sector Magnus trace and weight replacement shift
    # Verify sector additivity, control arm vanishing, and weight-correction shift
    w_pos = mp.mpf("1.875")
    w_neg = mp.mpf("1.125")
    dw_pos = mp.mpf("0.375")
    dw_neg = mp.mpf("-0.25")
    p1 = mp.mpf("24.5")
    p2 = mp.mpf("19.75")
    n1 = mp.mpf("18.25")
    n2 = mp.mpf("14.0")
    tr_sum = w_pos * (p1 + p2) - w_neg * (n1 + n2)
    tr_parts = (w_pos * p1 - w_neg * n1) + (w_pos * p2 - w_neg * n2)
    add_res = tr_sum - tr_parts
    ctrl_res = (w_pos * 0 - w_neg * 0 + p1 + p2 + n1 + n2) - (p1 + p2 + n1 + n2)
    tr_shifted = (w_pos + dw_pos) * p1 - (w_neg + dw_neg) * n1
    tr_base = w_pos * p1 - w_neg * n1
    tr_delta = dw_pos * p1 - dw_neg * n1
    shift_w_res = (tr_shifted - tr_base) - tr_delta
    pass_omr7 = bool(
        abs(add_res) < tol and abs(ctrl_res) < tol and abs(shift_w_res) < tol
    )

    # 4. Bean qou-ooqh: Ordered Borromean 3-body triple count a*(a-1)*(a-2)
    def tri_count(a: mp.mpf) -> mp.mpf:
        return a * (a - 1) * (a - 2)

    t2 = tri_count(mp.mpf(2))
    t3 = tri_count(mp.mpf(3))
    t4 = tri_count(mp.mpf(4))
    max_rec_err = mp.mpf(0)
    max_ratio_err = mp.mpf(0)
    for a_int in range(1, 9):
        a_mp = mp.mpf(a_int)
        rec_err = abs(
            (tri_count(a_mp + 1) - tri_count(a_mp)) - 3 * a_mp * (a_mp - 1)
        )
        if rec_err > max_rec_err:
            max_rec_err = rec_err
        rat_err = abs(
            (tri_count(a_mp + 1) - 4 * tri_count(a_mp))
            - 3 * a_mp * (a_mp - 1) * (3 - a_mp)
        )
        if rat_err > max_ratio_err:
            max_ratio_err = rat_err
    deut_zero_res = t2
    alpha_fourfold_res = t4 - 4 * t3
    pass_ooqh = bool(
        max_rec_err < tol
        and max_ratio_err < tol
        and abs(deut_zero_res) < tol
        and abs(alpha_fourfold_res) < tol
        and t3 == 6
        and t4 == 24
    )

    # 5. Bean qou-po72: De-Poissonized Cauchy-Schwarz correlation constant rho_P^2 = 24/25
    # Verify exact cancellation of pi in P^2 / (V_A * V_omega):
    # V_A = 8 / (9 * pi^2), V_omega = 1 / 3, P = 8 / (15 * pi)
    v_a = 8 / (9 * mp.pi ** 2)
    v_omega = mp.mpf(1) / mp.mpf(3)
    p_cov = 8 / (15 * mp.pi)
    rho_p_sq = (p_cov ** 2) / (v_a * v_omega)
    rho_p_sq_res = rho_p_sq - (mp.mpf(24) / mp.mpf(25))
    cs_margin_exact = 24 * v_a * v_omega - 25 * (p_cov ** 2)

    k_val = mp.mpf(7)
    diag_lhs = 25 * k_val * k_val - 24 * (k_val * k_val)
    diag_res = diag_lhs - (k_val * k_val)
    da_val = mp.mpf(3)
    dp_val = mp.mpf(5)
    lin_cs_res = (
        (25 * (k_val + da_val) * k_val - 24 * (k_val * k_val + dp_val))
        - (25 * k_val * k_val - 24 * (k_val * k_val))
    ) - (25 * da_val * k_val - 24 * dp_val)
    pass_po72 = bool(
        abs(rho_p_sq_res) < tol
        and abs(cs_margin_exact) < tol
        and abs(diag_res) < tol
        and abs(lin_cs_res) < tol
    )

    all_passed = bool(
        pass_ogrk and pass_ohaz and pass_omr7 and pass_ooqh and pass_po72
    )

    return {
        "schemaVersion": "1.0",
        "brick": "QOU.QBeta.HookEvenMomentAndBorromeanTripleBrick",
        "beans": [
            "qou-ogrk",
            "qou-ohaz",
            "qou-omr7",
            "qou-ooqh",
            "qou-po72",
        ],
        "scriptPath": str(SCRIPT_PATH.relative_to(REPO_ROOT)),
        "scriptHash": script_sha256_prefix(),
        "scriptCommitSha": git_commit_sha(),
        "dirty": git_is_dirty(),
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "precisionDps": 80,
        "allPassed": all_passed,
        "checks": {
            "qou_ogrk_hook_even_moment_cofactor": {
                "theorem": "hookContentAndMomentPair_classical_locus_and_even_cofactor",
                "staircase321HookContentResidual": fmt_mp(excess_res),
                "sixthMomentCofactorAtN6": fmt_mp(m6_pos),
                "reflectionSymmetryResidual": fmt_mp(refl_res),
                "c3LinearityResidual": fmt_mp(lin_c3_res),
                "passed": pass_ogrk,
            },
            "qou_ohaz_pair_collision_viscous_core_race": {
                "theorem": "pairCoreApproachGap_combined_rate_and_initial",
                "crossingTimeBeforeCollision": fmt_mp(t_cross),
                "inviscidCollisionTime": fmt_mp(t_coll),
                "combinedRateResidual": fmt_mp(rate_res),
                "initialMarginResidual": fmt_mp(init_res),
                "timeStepDecrementResidual": fmt_mp(step_res),
                "passed": pass_ohaz,
            },
            "qou_omr7_magnus_weighted_trace": {
                "theorem": "magnusWeightedTrace_sector_additivity_and_control_zero",
                "sectorAdditivityResidual": fmt_mp(add_res),
                "controlArmZeroResidual": fmt_mp(ctrl_res),
                "weightCorrectionShiftResidual": fmt_mp(shift_w_res),
                "passed": pass_omr7,
            },
            "qou_ooqh_borromean_triple_count": {
                "theorem": "orderedTripleCount_fourfold_ratio_identity",
                "deuteronOrderedTriples": fmt_mp(t2),
                "tritonOrderedTriples": fmt_mp(t3),
                "alphaOrderedTriples": fmt_mp(t4),
                "maxStepRecurrenceResidual": fmt_mp(max_rec_err),
                "maxFourfoldIdentityResidual": fmt_mp(max_ratio_err),
                "passed": pass_ooqh,
            },
            "qou_po72_de_poissonized_cs_margin": {
                "theorem": "csCorrelationMarginScaled_diagonal_and_sign_even",
                "dePoissonizedVarianceVA": fmt_mp(v_a),
                "dePoissonizedCovarianceP": fmt_mp(p_cov),
                "rhoPSquared80dps": fmt_mp(rho_p_sq),
                "rhoPSquaredMinus24Over25": fmt_mp(rho_p_sq_res),
                "scaledCSIdentityResidual": fmt_mp(cs_margin_exact),
                "diagonalUnitResidual": fmt_mp(diag_res),
                "perturbationLinearityResidual": fmt_mp(lin_cs_res),
                "passed": pass_po72,
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
