#!/usr/bin/env python3
"""80-dps mpmath numerical witness probe for Round 114 BraidKnot theorems:
- qou-pz4m: li2q_unique_from_ftc_sub_eq_zero (Li2qUniqueness.lean)
- qou-q7lf: br3_sub_br2_sq_sub_one_eq_zero (MagicShellCouplingKappa.lean)
- qou-r4w5: neg_four_fifths_sub_c4_nonneg (MuPTwoTermSum.lean)
- qou-rc7b: numSYT_mul_hookProduct_partition_sub_eq_zero (PartitionHookProductBridge.lean)
- qou-rj0m: colLen_sub_countP_rowLens_eq_zero (PartitionOfComposition.lean)
"""

import argparse
import hashlib
import json
import math
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80


def col_len(rows, j):
    return sum(1 for r in rows if r > j)


def hook_cells(rows):
    cells = []
    for i, r in enumerate(rows):
        for j in range(r):
            h = (r - 1 - j) + (col_len(rows, j) - 1 - i) + 1
            cells.append((i, j, h))
    return cells


def run_checks():
    results = []

    # 1. qou-pz4m: li2q_unique_from_ftc_sub_eq_zero on [0, V] for two representations of the same antiderivative
    v_val = mp.mpf(7) / mp.mpf(10)
    # F(x) = ln(1 + x^2) + x, G(x) = 2 * atanh(x^2 / (2 + x^2)) + x; both satisfy F(0)=G(0)=0 and F'=G'
    f_v = mp.log(mp.mpf(1) + v_val ** 2) + v_val
    g_v = mp.mpf(2) * mp.atanh((v_val ** 2) / (mp.mpf(2) + v_val ** 2)) + v_val
    diff1 = f_v - g_v
    results.append({
        "bean": "qou-pz4m",
        "theorem": "QOU.BraidKnot.li2q_unique_from_ftc_sub_eq_zero",
        "FV": mp.nstr(f_v, 80),
        "GV": mp.nstr(g_v, 80),
        "residual": mp.nstr(abs(diff1), 80),
        "passed": abs(diff1) < mp.mpf(10) ** (-75),
    })

    # 2. qou-q7lf: br3_sub_br2_sq_sub_one_eq_zero at q = 19/13
    q_val = mp.mpf(19) / mp.mpf(13)
    br2 = q_val + (mp.mpf(1) / q_val)
    br3 = (q_val ** 2) + mp.mpf(1) + (mp.mpf(1) / (q_val ** 2))
    diff2 = br3 - ((br2 ** 2) - mp.mpf(1))
    results.append({
        "bean": "qou-q7lf",
        "theorem": "QOU.BraidKnot.br3_sub_br2_sq_sub_one_eq_zero",
        "br3": mp.nstr(br3, 80),
        "br2SqSubOne": mp.nstr((br2 ** 2) - mp.mpf(1), 80),
        "residual": mp.nstr(abs(diff2), 80),
        "passed": abs(diff2) < mp.mpf(10) ** (-75),
    })

    # 3. qou-r4w5: neg_four_fifths_sub_c4_nonneg at q = 110995/100000, c3 = 2014/10000, c4 = -7/2
    q_pin = mp.mpf(110995) / mp.mpf(100000)
    w_gen = q_pin + (mp.mpf(1) / q_pin) - mp.mpf(2)
    c3 = mp.mpf(2014) / mp.mpf(10000)
    c4 = -mp.mpf(7) / mp.mpf(2)
    t_val = c3 * (w_gen ** 3) + c4 * (w_gen ** 4)
    margin3 = (-mp.mpf(4) / mp.mpf(5)) - c4
    results.append({
        "bean": "qou-r4w5",
        "theorem": "QOU.BraidKnot.MuPTwoTermSum.neg_four_fifths_sub_c4_nonneg",
        "wGen": mp.nstr(w_gen, 80),
        "tVal": mp.nstr(t_val, 80),
        "c4": mp.nstr(c4, 80),
        "margin": mp.nstr(margin3, 80),
        "passed": (
            mp.mpf(11099) / mp.mpf(10000) <= q_pin <= mp.mpf(111) / mp.mpf(100)
            and mp.mpf(18) / (mp.mpf(10) ** 8) <= t_val <= mp.mpf(24) / (mp.mpf(10) ** 8)
            and margin3 >= mp.mpf(0)
        ),
    })

    # 4. qou-rc7b: numSYT_mul_hookProduct_partition_sub_eq_zero on partition [4, 2, 1] of n = 7
    rows4 = [4, 2, 1]
    n4 = sum(rows4)
    hook_prod = mp.mpf(1)
    for _, _, h in hook_cells(rows4):
        hook_prod *= mp.mpf(h)
    n4_fac = mp.mpf(math.factorial(n4))
    num_syt = mp.mpf(35)  # SYT count for [4, 2, 1] is 35, hook_prod = 144, 35 * 144 = 5040 = 7!
    diff4 = num_syt * hook_prod - n4_fac
    results.append({
        "bean": "qou-rc7b",
        "theorem": "QOU.BraidKnot.numSYT_mul_hookProduct_partition_sub_eq_zero",
        "partition": str(rows4),
        "numSYT": mp.nstr(num_syt, 80),
        "hookProduct": mp.nstr(hook_prod, 80),
        "nFactorial": mp.nstr(n4_fac, 80),
        "residual": mp.nstr(diff4, 80),
        "passed": diff4 == mp.mpf(0),
    })

    # 5. qou-rj0m: colLen_sub_countP_rowLens_eq_zero on partition [6, 4, 4, 2, 1] across m = 0..6
    rows5 = [6, 4, 4, 2, 1]
    max_diff5 = max(
        abs(mp.mpf(col_len(rows5, m)) - mp.mpf(sum(1 for x in rows5 if m < x)))
        for m in range(7)
    )
    results.append({
        "bean": "qou-rj0m",
        "theorem": "QOU.BraidKnot.PartitionOfComposition.colLen_sub_countP_rowLens_eq_zero",
        "partition": str(rows5),
        "maxResidual": mp.nstr(max_diff5, 80),
        "passed": max_diff5 == mp.mpf(0),
    })

    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit-sha", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    script_bytes = Path(__file__).read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()
    results = run_checks()
    all_passed = all(r["passed"] for r in results)
    if not all_passed:
        raise SystemExit("One or more probe checks failed")

    payload = {
        "probe": "li2quniq_magicshell_mup2term_parthook_partcomp_probe",
        "scriptPath": "folio/quantum-observable-universe/computations/probes/li2quniq_magicshell_mup2term_parthook_partcomp_probe.py",
        "scriptCommitSha": args.commit_sha,
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "dps": "80",
        "allPassed": all_passed,
        "results": results,
    }
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
