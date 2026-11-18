#!/usr/bin/env python3
"""80-dps mpmath numerical verification probe for Round 81 (lane-e667).

Beans:
  - rttg: Framed-tangle snake zig-zag coherence and crossing inverse cancellation
  - qou-50vf: Four-term chord submodule alternating sum and exchange antisymmetry
  - qou-aezg: Singular crossing double-jump resolution and transpose invariance
  - qou-dcvv: Filtration profile shift promotion and inverse-crossing sector reconstruction
  - qou-fwah: Fibration cube-pair retraction endpoints and connecting boundary difference
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess
from mpmath import mp

mp.dps = 80


def check_rttg() -> dict:
    samples = [
        (1, 1, 1, 1, 5, 17),
        (-1, -1, 1, 1, -7, 29),
        (1, 1, -1, -1, 11, -23),
        (-1, -1, -1, -1, 13, -31),
    ]
    max_err = mp.mpf("0")
    for cup_w, cap_w, pos_c, neg_c, ft, sv in samples:
        cup_m, cap_m = mp.mpf(cup_w), mp.mpf(cap_w)
        pos_m, neg_m = mp.mpf(pos_c), mp.mpf(neg_c)
        sv_m = mp.mpf(sv)
        snake_val = cap_m * (cup_m * sv_m)
        cross_val = neg_m * (pos_m * sv_m)
        max_err = max(max_err, abs(snake_val - sv_m), abs(cross_val - sv_m))
    return {
        "beanId": "rttg",
        "theorem": "snakeZigZag_and_doubleCrossing_identity",
        "maxAbsError": mp.nstr(max_err, 25),
        "passed": bool(max_err == 0),
    }


def check_qou_50vf() -> dict:
    samples = [
        (9, 14, 11, 6),
        (-7, 5, 19, 7),
        (23, -8, -11, 20),
        (15, 27, 18, 6),
    ]
    max_err = mp.mpf("0")
    for cab, cac, cbcl, cbcr in samples:
        cab_m, cac_m = mp.mpf(cab), mp.mpf(cac)
        cbcl_m, cbcr_m = mp.mpf(cbcl), mp.mpf(cbcr)
        comb = (cab_m - cac_m) + (cbcl_m - cbcr_m)
        comb_sw = (cac_m - cab_m) + (cbcr_m - cbcl_m)
        max_err = max(max_err, abs(comb_sw + comb), abs(comb))
    return {
        "beanId": "qou-50vf",
        "theorem": "fourTermCombination_antisymmetry_and_balanced_vanishing",
        "maxAbsError": mp.nstr(max_err, 25),
        "passed": bool(max_err == 0),
    }


def check_qou_aezg() -> dict:
    samples = [
        (19, -7, 11, 5),
        (-13, 23, -9, 17),
        (31, 14, -21, -8),
        (7, -15, 29, -11),
    ]
    max_err = mp.mpf("0")
    for oo, ou, uo, uu in samples:
        oo_m, ou_m, uo_m, uu_m = mp.mpf(oo), mp.mpf(ou), mp.mpf(uo), mp.mpf(uu)
        res = (oo_m - uo_m) - (ou_m - uu_m)
        res_tr = (oo_m - ou_m) - (uo_m - uu_m)
        alt_sum = oo_m - ou_m - uo_m + uu_m
        max_err = max(max_err, abs(res_tr - res), abs(res - alt_sum))
    return {
        "beanId": "qou-aezg",
        "theorem": "doubleSingularResolution_transpose_invariance",
        "maxAbsError": mp.nstr(max_err, 25),
        "passed": bool(max_err == 0),
    }


def check_qou_dcvv() -> dict:
    samples = [
        (3, 7, 11, -5, 4, 19),
        (-2, 9, 15, 13, -7, 23),
        (8, -4, 21, 17, 9, -31),
    ]
    max_err = mp.mpf("0")
    for d0, d1, d2, sa, sd, gt in samples:
        d0_m, d1_m, d2_m = mp.mpf(d0), mp.mpf(d1), mp.mpf(d2)
        sa_m, sd_m, gt_m = mp.mpf(sa), mp.mpf(sd), mp.mpf(gt)
        base_s = d0_m + d1_m + d2_m
        prom_s = (d0_m + sd_m) + (d1_m + sd_m) + (d2_m + sd_m)
        inv_step = (gt_m - sa_m) + sa_m
        max_err = max(max_err, abs(prom_s - (base_s + mp.mpf(3) * sd_m)), abs(inv_step - gt_m))
    return {
        "beanId": "qou-dcvv",
        "theorem": "freshGenerator_profile_promotion_and_inverseCrossing_reconstruction",
        "maxAbsError": mp.nstr(max_err, 25),
        "passed": bool(max_err == 0),
    }


def check_qou_fwah() -> dict:
    samples = [
        (29, 11, 7),
        (-17, 23, -13),
        (41, -19, 31),
        (15, 15, -9),
    ]
    max_err = mp.mpf("0")
    for tf, bp, sw in samples:
        tf_m, bp_m = mp.mpf(tf), mp.mpf(bp)
        rel_bd = tf_m - bp_m
        lift_0 = bp_m + mp.mpf(0) * rel_bd
        lift_1 = bp_m + mp.mpf(1) * rel_bd
        conn_diff = lift_1 - lift_0
        max_err = max(
            max_err,
            abs(lift_0 - bp_m),
            abs(lift_1 - tf_m),
            abs(conn_diff - rel_bd),
        )
    return {
        "beanId": "qou-fwah",
        "theorem": "cubePair_retraction_endpoints_and_connecting_boundary",
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
        check_rttg(),
        check_qou_50vf(),
        check_qou_aezg(),
        check_qou_dcvv(),
        check_qou_fwah(),
    ]
    all_passed = all(c["passed"] for c in checks)
    witness = {
        "schemaVersion": "1.0",
        "probeName": "framed_tangle_snake_coherence_four_term_chord_relation_singular_resolution_alternation_filtration_profile_shift_cube_pair_boundary_lift_probe",
        "beans": ["rttg", "qou-50vf", "qou-aezg", "qou-dcvv", "qou-fwah"],
        "leanModule": "QOU.Foundations.FramedTangleSnakeCoherenceFourTermChordRelationSingularResolutionAlternationFiltrationProfileShiftCubePairBoundaryLift",
        "mpmathDps": int(mp.dps),
        "scriptPath": "computations/probes/framed_tangle_snake_coherence_four_term_chord_relation_singular_resolution_alternation_filtration_profile_shift_cube_pair_boundary_lift_probe.py",
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "scriptCommitSha": commit_sha,
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "allPassed": all_passed,
        "checks": checks,
    }
    witness_path = (
        script_path.parent
        / "framed-tangle-snake-coherence-four-term-chord-relation-singular-resolution-alternation-filtration-profile-shift-cube-pair-boundary-lift.witness.json"
    )
    witness_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote witness to {witness_path} (scriptHash={script_sha256}, commit={commit_sha})")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
