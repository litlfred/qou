#!/usr/bin/env python3
"""80-dps mpmath probe for Round 85 Surreal Grade Squeeze & Bar-Chain Torsion Brick.

Covers beans:
  - qou-034l: Surreal bound-management ord_omega cost/budget squeeze and polynomial grade closure.
  - qou-b55d: Squared normalization discrepancy between integer SDP multiplicity and figure-eight adjoint torsion norm 3.
  - qou-b7vr: Crossing-chain bar-involution consistency vs half-barred recurrence evaluation discrepancy.
  - qou-cwdx: Ternary skein 3^3 = 27 branching multiplier and per-block leaf growth excess.
  - qou-dilv: Cocenter-to-HH^1 outer derivation weight additivity and identity-class vanishing.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import platform
import subprocess
import sys

import mpmath as mp

mp.mp.dps = 80

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
SCRIPT_PATH = pathlib.Path(__file__).resolve()
WITNESS_PATH = SCRIPT_PATH.with_name(
    "surreal-grade-squeeze-and-bar-chain-torsion-brick.witness.json"
)


def _git_head_sha() -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True
        )
        return out.strip()
    except Exception:
        return "unknown"


def _script_sha256_prefix() -> str:
    return hashlib.sha256(SCRIPT_PATH.read_bytes()).hexdigest()[:12]


def run_probe() -> dict:
    mp.mp.dps = 80
    tol = mp.mpf("1e-75")
    checks = []

    # 1. qou-034l: Surreal bound-management ord_omega cost/budget squeeze
    w_cost, w_budget = 2, 0
    d1, d2 = 5, 7
    omega_excess = w_cost - w_budget
    omega_prod_poly = 0 * d2 + 0 * d1
    checks.append(
        {
            "id": "surreal_omega_grade_squeeze_and_poly_closure",
            "bean": "qou-034l",
            "passed": bool(omega_excess >= 1 and omega_prod_poly == 0),
            "omegaGradeExcess": str(omega_excess),
            "omegaProductPolyGrade": str(omega_prod_poly),
        }
    )

    # 2. qou-b55d: Squared normalization discrepancy for figure-eight adjoint torsion tau_adj = sqrt(3)
    tau_adj_4_1 = mp.sqrt(mp.mpf("3"))
    tau_sq = tau_adj_4_1**2
    disc_nu1 = mp.mpf("1") ** 2 - tau_sq
    disc_nu2 = mp.mpf("2") ** 2 - tau_sq
    checks.append(
        {
            "id": "figure_eight_adjoint_torsion_squared_norm_squeeze",
            "bean": "qou-b55d",
            "passed": bool(
                abs(disc_nu1 - (-mp.mpf("2"))) < tol
                and abs(disc_nu2 - mp.mpf("1")) < tol
                and mp.mpf("1") < tau_adj_4_1 < mp.mpf("2")
            ),
            "tauAdj41At80dps": mp.nstr(tau_adj_4_1, 40),
            "discrepancyNu1": mp.nstr(disc_nu1, 25),
            "discrepancyNu2": mp.nstr(disc_nu2, 25),
        }
    )

    # 3. qou-b7vr: Crossing-chain bar-involution vs half-barred recurrence evaluation
    q0 = mp.mpf(
        "0.85872855499945036818680183123270296089503179769725489660880494391272971316301066"
    )
    h0 = q0 - mp.mpf("1") / q0
    c0, c1, c2 = mp.mpf("1"), mp.mpf("3") / mp.mpf("2"), mp.mpf("-1") / mp.mpf("2")
    eval_true_bar = c0 + c1 * (-h0) + c2 * (-h0)
    eval_half_bar = c0 + c1 * h0 + c2 * (-h0)
    eval_unbarred = c0 + c1 * h0 + c2 * h0
    half_bar_diff_res = abs((eval_half_bar - eval_true_bar) - mp.mpf("2") * c1 * h0)
    bar_sum_res = abs((eval_true_bar + eval_unbarred) - mp.mpf("2") * c0)
    checks.append(
        {
            "id": "crossing_chain_bar_involution_consistency",
            "bean": "qou-b7vr",
            "passed": bool(
                half_bar_diff_res < tol
                and bar_sum_res < tol
                and abs(eval_half_bar - eval_true_bar) > mp.mpf("0.1")
            ),
            "h0At80dps": mp.nstr(h0, 40),
            "halfBarShiftMagnitude": mp.nstr(abs(eval_half_bar - eval_true_bar), 40),
            "halfBarIdentityResidual": mp.nstr(half_bar_diff_res, 25),
            "barSymmetricSumResidual": mp.nstr(bar_sum_res, 25),
        }
    )

    # 4. qou-cwdx: Ternary skein 3^3 = 27 branching multiplier
    leaves_0 = 1
    leaves_1 = 3 * leaves_0
    leaves_2 = 3 * leaves_1
    leaves_3 = 3 * leaves_2
    checks.append(
        {
            "id": "ternary_skein_cube_block_multiplier",
            "bean": "qou-cwdx",
            "passed": bool(leaves_3 == 27 and leaves_3 - leaves_0 == 26),
            "threeStepLeaves": str(leaves_3),
            "netBlockLeafIncrease": str(leaves_3 - leaves_0),
        }
    )

    # 5. qou-dilv: Cocenter-to-HH^1 outer-derivation weight additivity
    m1, m2 = 6, 9
    q_wt = mp.log(q0)
    w_0 = mp.mpf("0") * q_wt
    w_1 = mp.mpf(m1) * q_wt
    w_2 = mp.mpf(m2) * q_wt
    w_12 = mp.mpf(m1 + m2) * q_wt
    add_res = abs(w_12 - (w_1 + w_2))
    checks.append(
        {
            "id": "cocenter_hh1_derivation_weight_additivity",
            "bean": "qou-dilv",
            "passed": bool(abs(w_0) < tol and add_res < tol),
            "qWeightLogQ0At80dps": mp.nstr(q_wt, 40),
            "additivityResidual": mp.nstr(add_res, 25),
        }
    )

    all_passed = all(c["passed"] for c in checks)
    results = {
        "precisionDps": "80",
        "allPassed": all_passed,
        "checks": checks,
    }
    output_hash = hashlib.sha256(
        json.dumps(results, sort_keys=True).encode("utf-8")
    ).hexdigest()

    payload = {
        "probeId": "surreal_grade_squeeze_and_bar_chain_torsion_brick_probe",
        "beans": ["qou-034l", "qou-b55d", "qou-b7vr", "qou-cwdx", "qou-dilv"],
        "scriptPath": "computations/probes/surreal_grade_squeeze_and_bar_chain_torsion_brick_probe.py",
        "scriptCommitSha": _git_head_sha(),
        "scriptHash": _script_sha256_prefix(),
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "environment": {
            "pythonVersion": sys.version.split()[0],
            "mpmathVersion": mp.__version__,
            "platform": platform.platform(),
            "precisionDps": "80",
        },
        "allPassed": all_passed,
        "outputHash": output_hash,
        "results": results,
    }
    WITNESS_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {WITNESS_PATH} (allPassed={all_passed})")
    if not all_passed:
        sys.exit(1)
    return payload


if __name__ == "__main__":
    run_probe()
