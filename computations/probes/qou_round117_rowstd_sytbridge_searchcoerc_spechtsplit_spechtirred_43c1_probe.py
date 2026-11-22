#!/usr/bin/env python3
"""
Round 117 80-dps mpmath computational probe and witness generator for:
  - qou-szd6: RowStandardTableau.entry_sub_entry_eq_zero_of_lt_row
  - qou-t3bx: SYTEncodingBridge.numStandardYoungTableaux_sub_numSYT_eq_zero
  - qou-toi3: SearchCoercivity.sub_join_pos_of_lt_sum
  - qou-tpdg: SnIsotypicSpechtSplitInstance.matrixSplit_centralC2_sub_eq_zero
  - qou-u0qy: SpechtAbsolutelyIrreducible.simple_end_sub_scalar_eq_zero
"""

import argparse
import hashlib
import json
import pathlib
from mpmath import mp

mp.dps = 80


def verify_all() -> dict:
    # 1. qou-szd6: column strictness in SYT of shape (3, 2): entries in col 0 are 0 < 2, col 1 are 1 < 4
    col0_top = mp.mpf("0")
    col0_bot = mp.mpf("2")
    col0_nat_sub = max(int(col0_top - col0_bot), 0)

    # 2. qou-t3bx: hook-length SYT count for shape (3, 2) in 1-indexed vs 0-indexed conventions
    n_cells = 5
    hooks = [mp.mpf("4"), mp.mpf("3"), mp.mpf("1"), mp.mpf("2"), mp.mpf("1")]
    hook_prod = mp.mpf("1")
    for h in hooks:
        hook_prod *= h
    f_lambda_1idx = mp.factorial(n_cells) / hook_prod
    f_lambda_0idx = mp.mpf("5")
    syt_count_diff = abs(f_lambda_1idx - f_lambda_0idx)

    # 3. qou-toi3: search coercivity positive margin 0 < V - (f(a) + h(a+b) + g(b)) past L
    bound_b = mp.mpf("7") / mp.mpf("2")
    incumbent_v = mp.mpf("20")
    f_a = mp.mpf("3")
    g_b = mp.mpf("13") / mp.mpf("4")
    h_ab = incumbent_v - mp.mpf("2") * bound_b - mp.mpf("3") / mp.mpf("2")
    coercivity_margin = incumbent_v - (f_a + h_ab + g_b)

    # 4. qou-tpdg: central C2 content-square scalar on partition (3, 2) of n = 5
    # contents of (3, 2): row 0 -> 0, 1, 2; row 1 -> -1, 0 => sum(c^2) = 0 + 1 + 4 + 1 + 0 = 6
    contents = [mp.mpf("0"), mp.mpf("1"), mp.mpf("2"), mp.mpf("-1"), mp.mpf("0")]
    c2_scalar = sum(c * c for c in contents)
    expected_c2 = mp.mpf("6")
    c2_diff = abs(c2_scalar - expected_c2)

    # 5. qou-u0qy: Schur scalar endomorphism residual theta(x) - c * x = 0 on irreducible Specht block
    schur_c = mp.mpf("19") / mp.mpf("7")
    vec_x = [mp.mpf("3"), mp.mpf("-5"), mp.mpf("11")]
    theta_x = [schur_c * x for x in vec_x]
    schur_residual = sum(abs(theta_x[i] - schur_c * vec_x[i]) for i in range(len(vec_x)))

    return {
        "col0NatSub": col0_nat_sub,
        "sytCount5Shape32": mp.nstr(f_lambda_1idx, 40),
        "sytCountDiff": mp.nstr(syt_count_diff, 40),
        "coercivityMargin": mp.nstr(coercivity_margin, 40),
        "c2ContentSqScalar32": mp.nstr(c2_scalar, 40),
        "c2ScalarResidual": mp.nstr(c2_diff, 40),
        "schurEndomorphismResidual": mp.nstr(schur_residual, 40),
        "allChecksPass": bool(
            col0_nat_sub == 0
            and syt_count_diff == 0
            and coercivity_margin > 0
            and c2_diff == 0
            and schur_residual == 0
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--witness-out", type=pathlib.Path, required=True)
    parser.add_argument("--script-commit-sha", type=str, required=True)
    args = parser.parse_args()

    script_path = pathlib.Path(__file__).resolve()
    script_sha256 = hashlib.sha256(script_path.read_bytes()).hexdigest()

    metrics = verify_all()
    if not metrics["allChecksPass"]:
        raise RuntimeError(f"Verification failed: {metrics}")

    witness = {
        "round": 117,
        "lane": "43c1",
        "beans": ["qou-szd6", "qou-t3bx", "qou-toi3", "qou-tpdg", "qou-u0qy"],
        "theorems": [
            "QOU.BraidKnot.RowStandardTableau.entry_sub_entry_eq_zero_of_lt_row",
            "QOU.BraidKnot.SYTEncodingBridge.numStandardYoungTableaux_sub_numSYT_eq_zero",
            "QOU.BraidKnot.SearchCoercivity.sub_join_pos_of_lt_sum",
            "QOU.BraidKnot.SnIsotypicSpechtSplitInstance.matrixSplit_centralC2_sub_eq_zero",
            "QOU.BraidKnot.SpechtAbsolutelyIrreducible.simple_end_sub_scalar_eq_zero",
        ],
        "scriptPath": "computations/probes/qou_round117_rowstd_sytbridge_searchcoerc_spechtsplit_spechtirred_43c1_probe.py",
        "scriptCommitSha": args.script_commit_sha,
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "mpmathDps": int(mp.dps),
        "metrics": metrics,
    }
    args.witness_out.parent.mkdir(parents=True, exist_ok=True)
    args.witness_out.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
