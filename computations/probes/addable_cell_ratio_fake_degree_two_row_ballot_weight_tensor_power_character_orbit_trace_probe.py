#!/usr/bin/env python3
"""80-dps mpmath numerical witness probe for Round 66 (qou-3quc, qou-f1qs, qou-mpq5, qou-ognw, qou-uinl).

Verifies at 80 decimal places (mpmath.mp.dps = 80):
1. qou-ognw: Per-cell denominator bridge 1 - q^4 = (1 - q^2)(1 + q^2), ratio identity
   [2]_Q (1 + Q^2) = [4]_Q, and two-row addable-cell ratio sum
   R_{(3,1)}(Q) + Q R_{(2,2)}(Q) + Q^2 R_{(2,1,1)}(Q) = [4]_Q [2]_Q.
2. qou-3quc: Fourth-order coinvariant degree sum across all five 4-box shapes
   1 + 3 Q [3]_Q + 2 Q^2 (1 + Q^2) + 3 Q^3 [3]_Q + Q^6 = [4]_Q! and strict inequality
   with the unshifted sum of squared ratios at Q > 1 (125 != 315 at Q = 2).
3. qou-f1qs: Two-row lattice-vote recurrence and level-sum branching normalisation
   T_5(t) + T_3(t) = t T_4(t), T_3(t) + T_1 = t T_2(t), S_3(t) = t^3, S_4(t) = t S_3(t) = t^4.
4. qou-mpq5: Block-trace additivity and character-sum decomposition across the three 3-box
   blocks giving 6 N^3 on (1, 2, 1), 6 N^2 on (1, 0, -1), and 6 N on (1, -1, 1).
5. qou-uinl: Orbit-constant function counts (N^3, N^2, N) and conjugacy-class character
   projections recovering W_{(3)}(N), W_{(2,1)}(N), and W_{(1,1,1)}(N).
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess
from mpmath import mp

mp.dps = 80

PROBE_PATH = pathlib.Path(__file__).resolve()
REPO_ROOT = PROBE_PATH.parents[2]
WITNESS_DIR = REPO_ROOT / "computations" / "probes"
WITNESS_PATH = (
    WITNESS_DIR
    / "addable-cell-ratio-fake-degree-two-row-ballot-weight-tensor-power-character-orbit-trace.witness.json"
)


def fmt(x: mp.mpf) -> str:
    return mp.nstr(x, 80, strip_zeros=False)


def run_probe() -> dict[str, object]:
    tol = mp.mpf("1e-75")
    q_trans = mp.exp(mp.mpf(1) / mp.mpf(7))
    q_samples = [q_trans, mp.mpf(2), mp.mpf(3), mp.mpf(5)]

    # 1. qou-ognw: Per-cell denominator bridge and two-row addable-cell ratio identity
    ognw_records = []
    ognw_pass = True
    for q in q_samples:
        Q = q * q
        b2 = mp.mpf(1) + Q
        b3 = mp.mpf(1) + Q + Q * Q
        b4 = mp.mpf(1) + Q + Q * Q + Q * Q * Q
        r31 = b3
        r22 = mp.mpf(1) + Q * Q
        r211 = b3
        denom_lhs = mp.mpf(1) - (q ** 4)
        denom_rhs = (mp.mpf(1) - Q) * (mp.mpf(1) + Q)
        ratio_lhs = b2 * r22
        addable_sum = r31 + Q * r22 + Q * Q * r211
        addable_rhs = b4 * b2
        max_res = max(
            abs(denom_lhs - denom_rhs),
            abs(ratio_lhs - b4),
            abs(addable_sum - addable_rhs),
        )
        ok = bool(max_res < tol and abs(mp.mpf(1) - Q) > tol)
        ognw_pass = ognw_pass and ok
        ognw_records.append(
            {
                "q": fmt(q),
                "Q": fmt(Q),
                "addableCellRatioSum21": fmt(addable_sum),
                "productB4B2": fmt(addable_rhs),
                "maxResidual": fmt(max_res),
                "passed": ok,
            }
        )

    # 2. qou-3quc: Fourth-order coinvariant degree sum and squared-ratio contrast
    q3quc_records = []
    q3quc_pass = True
    for q in q_samples:
        Q = q * q
        b1 = mp.mpf(1)
        b2 = mp.mpf(1) + Q
        b3 = mp.mpf(1) + Q + Q * Q
        b4 = mp.mpf(1) + Q + Q * Q + Q * Q * Q
        qfact4 = b1 * b2 * b3 * b4
        r31 = b3
        r22 = mp.mpf(1) + Q * Q
        r211 = b3
        coinv_sum = (
            mp.mpf(1)
            + mp.mpf(3) * Q * b3
            + mp.mpf(2) * (Q ** 2) * r22
            + mp.mpf(3) * (Q ** 3) * b3
            + (Q ** 6)
        )
        unshifted_sq = mp.mpf(1) + (r31 ** 2) + (r22 ** 2) + (r211 ** 2) + mp.mpf(1)
        res = abs(coinv_sum - qfact4)
        gap = abs(qfact4 - unshifted_sq)
        ok = bool(res < tol and gap > mp.mpf("1e-3") and coinv_sum > mp.mpf(0))
        q3quc_pass = q3quc_pass and ok
        q3quc_records.append(
            {
                "Q": fmt(Q),
                "coinvariantDegreeSum4": fmt(coinv_sum),
                "polyFactorial4": fmt(qfact4),
                "unshiftedRatioSqSum4": fmt(unshifted_sq),
                "contrastGap": fmt(gap),
                "maxResidual": fmt(res),
                "passed": ok,
            }
        )

    # 3. qou-f1qs: Two-row lattice-vote recurrence and level-sum normalisation
    f1qs_records = []
    f1qs_pass = True
    for q in q_samples:
        t = q + (mp.mpf(1) / q)
        T1 = mp.mpf(1)
        T2 = t
        T3 = t * t - mp.mpf(1)
        T4 = (t ** 3) - mp.mpf(2) * t
        T5 = (t ** 4) - mp.mpf(3) * (t ** 2) + mp.mpf(1)
        S3 = mp.mpf(1) * T4 + mp.mpf(2) * T2
        S4 = mp.mpf(1) * T5 + mp.mpf(3) * T3 + mp.mpf(2) * T1
        res_b4 = abs((T5 + T3) - t * T4)
        res_b2 = abs((T3 + T1) - t * T2)
        res_s3 = abs(S3 - (t ** 3))
        res_step = abs(S4 - t * S3)
        res_s4 = abs(S4 - (t ** 4))
        max_res = max(res_b4, res_b2, res_s3, res_step, res_s4)
        ok = bool(max_res < tol and S4 > mp.mpf(0))
        f1qs_pass = f1qs_pass and ok
        f1qs_records.append(
            {
                "q": fmt(q),
                "t": fmt(t),
                "levelSum3": fmt(S3),
                "levelSum4": fmt(S4),
                "maxResidual": fmt(max_res),
                "passed": ok,
            }
        )

    # 4. qou-mpq5: Block-trace additivity and character-sum decomposition
    mpq5_records = []
    mpq5_pass = True
    for N_val in [mp.mpf(2), mp.mpf(3), mp.mpf(4), mp.mpf(7)]:
        W3 = N_val * (N_val + mp.mpf(1)) * (N_val + mp.mpf(2))
        W21 = mp.mpf(2) * N_val * (N_val - mp.mpf(1)) * (N_val + mp.mpf(1))
        W111 = N_val * (N_val - mp.mpf(1)) * (N_val - mp.mpf(2))
        sum_id = W3 * mp.mpf(1) + W21 * mp.mpf(2) + W111 * mp.mpf(1)
        sum_swap = W3 * mp.mpf(1) + W21 * mp.mpf(0) + W111 * mp.mpf(-1)
        sum_cycle = W3 * mp.mpf(1) + W21 * mp.mpf(-1) + W111 * mp.mpf(1)
        res_id = abs(sum_id - mp.mpf(6) * (N_val ** 3))
        res_swap = abs(sum_swap - mp.mpf(6) * (N_val ** 2))
        res_cycle = abs(sum_cycle - mp.mpf(6) * N_val)
        max_res = max(res_id, res_swap, res_cycle)
        ok = bool(max_res < tol and sum_id > mp.mpf(0))
        mpq5_pass = mpq5_pass and ok
        mpq5_records.append(
            {
                "N": fmt(N_val),
                "charSumId": fmt(sum_id),
                "charSumSwap": fmt(sum_swap),
                "charSumCycle": fmt(sum_cycle),
                "maxResidual": fmt(max_res),
                "passed": ok,
            }
        )

    # 5. qou-uinl: Orbit-constant function counts and permutation trace projections
    uinl_records = []
    uinl_pass = True
    for N_val in [mp.mpf(2), mp.mpf(3), mp.mpf(4), mp.mpf(7)]:
        c_id = N_val ** 3
        c_swap = N_val ** 2
        c_cycle = N_val
        W3 = N_val * (N_val + mp.mpf(1)) * (N_val + mp.mpf(2))
        W21 = mp.mpf(2) * N_val * (N_val - mp.mpf(1)) * (N_val + mp.mpf(1))
        W111 = N_val * (N_val - mp.mpf(1)) * (N_val - mp.mpf(2))
        proj_3 = mp.mpf(1) * c_id + mp.mpf(3) * c_swap + mp.mpf(2) * c_cycle
        proj_21 = mp.mpf(2) * c_id - mp.mpf(2) * c_cycle
        proj_111 = mp.mpf(1) * c_id - mp.mpf(3) * c_swap + mp.mpf(2) * c_cycle
        max_res = max(
            abs(proj_3 - W3),
            abs(proj_21 - W21),
            abs(proj_111 - W111),
        )
        ok = bool(max_res < tol and c_id > c_swap)
        uinl_pass = uinl_pass and ok
        uinl_records.append(
            {
                "N": fmt(N_val),
                "orbitCountId": fmt(c_id),
                "orbitCountSwap": fmt(c_swap),
                "orbitCountCycle": fmt(c_cycle),
                "proj3": fmt(proj_3),
                "proj21": fmt(proj_21),
                "proj111": fmt(proj_111),
                "maxResidual": fmt(max_res),
                "passed": ok,
            }
        )

    all_passed = bool(
        ognw_pass and q3quc_pass and f1qs_pass and mpq5_pass and uinl_pass
    )

    script_bytes = PROBE_PATH.read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()[:12]
    try:
        commit_sha = (
            subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True
            ).strip()
        )
    except Exception:
        commit_sha = "0" * 40

    payload: dict[str, object] = {
        "probe": "addable_cell_ratio_fake_degree_two_row_ballot_weight_tensor_power_character_orbit_trace_probe",
        "beans": ["qou-3quc", "qou-f1qs", "qou-mpq5", "qou-ognw", "qou-uinl"],
        "precisionDps": 80,
        "scriptPath": str(PROBE_PATH.relative_to(REPO_ROOT))
        if PROBE_PATH.is_relative_to(REPO_ROOT)
        else str(PROBE_PATH.name),
        "scriptHash": script_hash,
        "scriptCommitSha": commit_sha,
        "timestampUtc": datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
        "allPassed": all_passed,
        "results": {
            "qou_ognw_two_row_addable_cell_ratio": {
                "passed": ognw_pass,
                "samples": ognw_records,
            },
            "qou_3quc_fourth_order_coinvariant_sum": {
                "passed": q3quc_pass,
                "samples": q3quc_records,
            },
            "qou_f1qs_two_row_level_sum_branching": {
                "passed": f1qs_pass,
                "samples": f1qs_records,
            },
            "qou_mpq5_block_character_sum": {
                "passed": mpq5_pass,
                "samples": mpq5_records,
            },
            "qou_uinl_orbit_invariant_projections": {
                "passed": uinl_pass,
                "samples": uinl_records,
            },
        },
    }
    return payload


def main() -> None:
    payload = run_probe()
    if WITNESS_DIR.parent.exists():
        WITNESS_DIR.mkdir(parents=True, exist_ok=True)
        WITNESS_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "allPassed": payload["allPassed"],
                "scriptHash": payload["scriptHash"],
                "scriptCommitSha": payload["scriptCommitSha"],
            }
        )
    )
    if not payload["allPassed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
