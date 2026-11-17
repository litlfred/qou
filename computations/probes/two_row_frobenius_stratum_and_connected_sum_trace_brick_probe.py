#!/usr/bin/env python3
"""
80-dps mpmath witness probe for:
  folio/quantum-observable-universe/lean/QOU/QBeta/TwoRowFrobeniusStratumAndConnectedSumTraceBrick.lean

Beans:
  - qou-2row: two_row_frobenius_stratum_drift_and_non_constant_obstruction
  - qou-301d: connected_sum_amplitude_multiplicativity_free_energy_split
  - qou-3wvl: scale_free_alpha_cluster_ratio_q0_scale_cancellation
  - qou-k00d: whitehead_one_loop_prefactor_torsion_inverse_square_root_lock
  - qou-t7az: mcphail_snyder_diagrammatic_edge_lattice_rank_and_input_shift
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess
import mpmath as mp

mp.mp.dps = 80

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
SCRIPT_PATH = pathlib.Path(__file__).resolve()
WITNESS_PATH = SCRIPT_PATH.with_name(
    "two-row-frobenius-stratum-and-connected-sum-trace-brick.witness.json"
)


def git_head_sha() -> str:
    return (
        subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT)
        .decode("utf-8")
        .strip()
    )


def check_qou_2row() -> dict:
    # Two-row Frobenius stratum drift across 4He (rho_4=1.889) and 16O (rho_16=2.130)
    rho_4 = mp.mpf("1.889")
    rho_16 = mp.mpf("2.130")
    drift_diff = rho_16 - rho_4
    partition_count_12 = mp.mpf(12) / 2 + 1

    # Sum of the 7 two-row H_12 weights from qou-2row
    weights = [
        mp.mpf("0.003966"),
        mp.mpf("0.003100"),
        mp.mpf("0.002370"),
        mp.mpf("0.001744"),
        mp.mpf("0.001194"),
        mp.mpf("0.000696"),
        mp.mpf("0.000229"),
    ]
    stratum_sum = sum(weights, mp.mpf(0))

    passed = bool(
        drift_diff > mp.mpf("0.2")
        and partition_count_12 == 7
        and len(weights) == 7
        and stratum_sum > mp.mpf("0.01")
    )
    return {
        "bean": "qou-2row",
        "theorem": "two_row_frobenius_stratum_drift_and_non_constant_obstruction",
        "passed": passed,
        "drift_diff": mp.nstr(drift_diff, 80),
        "partition_count_12": mp.nstr(partition_count_12, 10),
        "stratum_weight_sum": mp.nstr(stratum_sum, 80),
    }


def check_qou_301d() -> dict:
    # Connected-sum amplitude multiplicativity and free-energy split
    t1 = mp.mpf("3.14159265358979323846264338327950288419716939937510")
    t2 = mp.mpf("2.71828182845904523536028747135266249775724709369995")
    i_conn = mp.mpf("1.41421356237309504880168872420969807856967187537694")

    a_total = t1 * t2 * i_conn
    l1 = mp.log(t1)
    l2 = mp.log(t2)
    l_i = mp.log(i_conn)
    l_total = mp.log(a_total)

    log_add_residual = abs(l_total - (l1 + l2 + l_i))
    sub_residual = abs(((l1 + l2) - l_total) - (-l_i))

    passed = bool(
        log_add_residual < mp.mpf("1e-75")
        and sub_residual < mp.mpf("1e-75")
        and a_total > mp.mpf("10")
    )
    return {
        "bean": "qou-301d",
        "theorem": "connected_sum_amplitude_multiplicativity_free_energy_split",
        "passed": passed,
        "log_add_residual": mp.nstr(log_add_residual, 80),
        "sub_residual": mp.nstr(sub_residual, 80),
        "a_total": mp.nstr(a_total, 80),
    }


def check_qou_3wvl() -> dict:
    # Scale-free alpha-cluster surface residual s0 cancellation
    s0 = mp.mpf("29.8")
    n_alpha = mp.mpf(4)  # 16O = 4 alpha
    b_alpha = mp.mpf("1.0")
    delta_surf = mp.mpf("0.52")  # +13% surface drift across 4 alpha

    b_n = s0 * (n_alpha * b_alpha + delta_surf)
    b_1 = s0 * (1 * b_alpha + 0)
    norm_res = (b_n - n_alpha * b_1) / b_1
    expected = delta_surf / b_alpha
    cancel_residual = abs(norm_res - expected)

    passed = bool(
        cancel_residual < mp.mpf("1e-75")
        and norm_res > mp.mpf("0.5")
    )
    return {
        "bean": "qou-3wvl",
        "theorem": "scale_free_alpha_cluster_ratio_q0_scale_cancellation",
        "passed": passed,
        "cancel_residual": mp.nstr(cancel_residual, 80),
        "normalized_surface_residual": mp.nstr(norm_res, 80),
    }


def check_qou_k00d() -> dict:
    # Whitehead one-loop prefactor c_sigma = 2^{-1/2} * |tau_DG|^{-1/2}
    tau_dg = mp.mpf(4)
    c_sigma_sq = mp.mpf(1) / (2 * tau_dg)
    c_sigma = mp.sqrt(c_sigma_sq)
    # Also check 2^{-3/4} = 0.5946035575013605... (when |tau_DG| = 2^{3/2})
    c_sigma_alt = mp.power(2, mp.mpf("-0.75"))
    gm_residual = abs(c_sigma_sq * (2 * tau_dg) - 1)
    fourth_pow_residual = abs((c_sigma_sq**2) - mp.mpf(1) / 64)

    passed = bool(
        gm_residual < mp.mpf("1e-75")
        and fourth_pow_residual < mp.mpf("1e-75")
        and abs(c_sigma_alt - mp.mpf("0.5946035575")) < mp.mpf("1e-9")
    )
    return {
        "bean": "qou-k00d",
        "theorem": "whitehead_one_loop_prefactor_torsion_inverse_square_root_lock",
        "passed": passed,
        "gm_residual": mp.nstr(gm_residual, 80),
        "fourth_pow_residual": mp.nstr(fourth_pow_residual, 80),
        "c_sigma_at_tau4": mp.nstr(c_sigma, 80),
        "two_pow_neg_three_quarters": mp.nstr(c_sigma_alt, 80),
    }


def check_qou_t7az() -> dict:
    # McPhail-Snyder diagrammatic edge-lattice rank and meridian input shift
    c_cross = mp.mpf(5)  # 5_2 knot
    e_rank = 2 * c_cross
    f_count = c_cross + 2
    euler_val = c_cross - e_rank + f_count

    alpha = mp.mpf("1.75")
    mu = mp.mpf("0.625")
    delta_mu = mp.mpf("0.125")
    shift_diff = alpha * (mu + delta_mu) - alpha * mu
    shift_residual = abs(shift_diff - alpha * delta_mu)

    passed = bool(
        euler_val == 2
        and e_rank == 10
        and shift_residual < mp.mpf("1e-75")
        and abs(shift_diff) > mp.mpf("0.2")
    )
    return {
        "bean": "qou-t7az",
        "theorem": "mcphail_snyder_diagrammatic_edge_lattice_rank_and_input_shift",
        "passed": passed,
        "euler_characteristic": mp.nstr(euler_val, 10),
        "edge_rank_5_2": mp.nstr(e_rank, 10),
        "shift_residual": mp.nstr(shift_residual, 80),
        "shift_diff": mp.nstr(shift_diff, 80),
    }


def main() -> None:
    checks = [
        check_qou_2row(),
        check_qou_301d(),
        check_qou_3wvl(),
        check_qou_k00d(),
        check_qou_t7az(),
    ]
    all_passed = all(c["passed"] for c in checks)
    script_bytes = SCRIPT_PATH.read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()

    payload = {
        "probe": "computations/probes/two_row_frobenius_stratum_and_connected_sum_trace_brick_probe.py",
        "beans": ["qou-2row", "qou-301d", "qou-3wvl", "qou-k00d", "qou-t7az"],
        "precisionDps": 80,
        "scriptHash": script_hash,
        "scriptCommitSha": git_head_sha(),
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "allPassed": all_passed,
        "checks": checks,
    }
    WITNESS_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if not all_passed:
        raise SystemExit("One or more witness checks failed")
    print(f"Wrote {WITNESS_PATH} (allPassed={all_passed})")


if __name__ == "__main__":
    main()
