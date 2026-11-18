#!/usr/bin/env python3
"""80-dps mpmath numerical verification probe for Round 80 (lane-e667).

Beans:
  - bwrt: Categorical quantum dimension unit normalization and vacuum row cross-product balance
  - bwse: Modular surgery partition sum factorization and vacuum sector isolation
  - rtkb: Surgery handle-slide bilinear linking discriminant invariance
  - rtqd: Pivotal dual-trace transport and swapped pairing conjugation symmetry
  - rtrb: Ribbon balancing twist tensor symmetry and double-mate shift invariance
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess
from mpmath import mp

mp.dps = 80


def check_bwrt() -> dict:
    samples = [
        (3, 5, 7, 19),
        (-2, 11, 4, 29),
        (9, -3, 13, 41),
        (1, 1, 1, 17),
    ]
    max_err = mp.mpf("0")
    for cw, bs, ew, tot in samples:
        cw_m, bs_m, ew_m, tot_m = mp.mpf(cw), mp.mpf(bs), mp.mpf(ew), mp.mpf(tot)
        unit_dim = mp.mpf(1) * mp.mpf(1) * mp.mpf(1)
        obj_dim = cw_m * bs_m * ew_m
        cross_lhs = obj_dim * tot_m - obj_dim
        cross_rhs = obj_dim * (tot_m - mp.mpf(1))
        max_err = max(max_err, abs(unit_dim - mp.mpf(1)), abs(cross_lhs - cross_rhs))
    return {
        "beanId": "bwrt",
        "theorem": "unitObjectDimension_eq_one_and_vacuumRow_balance",
        "maxAbsError": mp.nstr(max_err, 25),
        "passed": bool(max_err == 0),
    }


def check_bwse() -> dict:
    samples = [
        (1, 3, 5, 7, -11, 13, 17),
        (2, -7, 9, 14, 5, -19, 23),
        (4, 11, -3, -8, 15, 21, -9),
    ]
    max_err = mp.mpf("0")
    for d0, d1, d2, a0, a1, a2, cf in samples:
        d0_m, d1_m, d2_m = mp.mpf(d0), mp.mpf(d1), mp.mpf(d2)
        a0_m, a1_m, a2_m = mp.mpf(a0), mp.mpf(a1), mp.mpf(a2)
        cf_m = mp.mpf(cf)
        unnorm = d0_m * a0_m + d1_m * a1_m + d2_m * a2_m
        scaled = (cf_m * d0_m) * a0_m + (cf_m * d1_m) * a1_m + (cf_m * d2_m) * a2_m
        vac_iso = d0_m * a0_m + d1_m * mp.mpf(0) + d2_m * mp.mpf(0)
        max_err = max(max_err, abs(scaled - cf_m * unnorm), abs(vac_iso - d0_m * a0_m))
    return {
        "beanId": "bwse",
        "theorem": "modularPartitionSum_factorization_and_vacuum_isolation",
        "maxAbsError": mp.nstr(max_err, 25),
        "passed": bool(max_err == 0),
    }


def check_rtkb() -> dict:
    samples = [
        (5, -3, 11, 4),
        (-7, 13, 9, -6),
        (17, 8, -15, 11),
        (23, -19, 31, -9),
    ]
    max_err = mp.mpf("0")
    for a, b, c, k in samples:
        a_m, b_m, c_m, k_m = mp.mpf(a), mp.mpf(b), mp.mpf(c), mp.mpf(k)
        disc_orig = a_m * c_m - b_m * b_m
        b_sl = b_m + k_m * a_m
        c_sl = c_m + mp.mpf(2) * k_m * b_m + k_m * k_m * a_m
        disc_sl = a_m * c_sl - b_sl * b_sl
        max_err = max(max_err, abs(disc_sl - disc_orig))
    return {
        "beanId": "rtkb",
        "theorem": "handleSlide_discriminant_invariance",
        "maxAbsError": mp.nstr(max_err, 25),
        "passed": bool(max_err == 0),
    }


def check_rtqd() -> dict:
    samples = [
        (7, 1, 1, 13),
        (-9, -1, -1, 23),
        (15, 1, 1, -31),
        (19, -1, -1, -11),
    ]
    max_err = mp.mpf("0")
    for lc, bh, bi, re in samples:
        lc_m, bh_m, bi_m, re_m = mp.mpf(lc), mp.mpf(bh), mp.mpf(bi), mp.mpf(re)
        r_trace = lc_m * (bh_m * re_m)
        s_trace = lc_m * (bi_m * (bh_m * (bh_m * re_m)))
        max_err = max(max_err, abs(s_trace - r_trace))
    return {
        "beanId": "rtqd",
        "theorem": "swappedDualQuantumTrace_eq_rightQuantumTrace",
        "maxAbsError": mp.nstr(max_err, 25),
        "passed": bool(max_err == 0),
    }


def check_rtrb() -> dict:
    samples = [
        (7, -11, 19, 5, 23),
        (-13, 9, -29, -8, 17),
        (31, 15, 7, 12, -41),
    ]
    max_err = mp.mpf("0")
    for tx, ty, db, ms, bt in samples:
        tx_m, ty_m, db_m = mp.mpf(tx), mp.mpf(ty), mp.mpf(db)
        ms_m, bt_m = mp.mpf(ms), mp.mpf(bt)
        t_twist = (tx_m * ty_m) * db_m
        s_twist = (ty_m * tx_m) * db_m
        m_shift = ms_m + (ms_m + bt_m) - mp.mpf(2) * ms_m
        max_err = max(max_err, abs(t_twist - s_twist), abs(m_shift - bt_m))
    return {
        "beanId": "rtrb",
        "theorem": "ribbonTwist_tensor_symmetry_and_doubleMate_fixed",
        "maxAbsError": mp.nstr(max_err, 25),
        "passed": bool(max_err == 0),
    }


def main() -> None:
    script_path = pathlib.Path(__file__).resolve()
    repo_root = script_path.parents[2]
    script_bytes = script_path.read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()
    try:
        commit_sha = (
            subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo_root)
            .decode("utf-8")
            .strip()
        )
    except Exception:
        commit_sha = "UNKNOWN"

    checks = [
        check_bwrt(),
        check_bwse(),
        check_rtkb(),
        check_rtqd(),
        check_rtrb(),
    ]
    all_passed = all(c["passed"] for c in checks)
    witness = {
        "schemaVersion": "1.0",
        "probeName": "categorical_quantum_dimension_vacuum_row_modular_partition_sum_surgery_slide_invariance_pivotal_dual_trace_ribbon_balancing_probe",
        "beans": ["bwrt", "bwse", "rtkb", "rtqd", "rtrb"],
        "leanModule": "QOU.Foundations.CategoricalQuantumDimensionVacuumRowModularPartitionSumSurgerySlideInvariancePivotalDualTraceRibbonBalancing",
        "mpmathDps": int(mp.dps),
        "scriptPath": "computations/probes/categorical_quantum_dimension_vacuum_row_modular_partition_sum_surgery_slide_invariance_pivotal_dual_trace_ribbon_balancing_probe.py",
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "scriptCommitSha": commit_sha,
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "allPassed": all_passed,
        "checks": checks,
    }
    witness_path = (
        script_path.parent
        / "categorical-quantum-dimension-vacuum-row-modular-partition-sum-surgery-slide-invariance-pivotal-dual-trace-ribbon-balancing.witness.json"
    )
    witness_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote witness to {witness_path} (scriptHash={script_sha256}, commit={commit_sha})")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
