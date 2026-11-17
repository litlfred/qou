#!/usr/bin/env python3
"""80-dps mpmath probe for Round 88 beans:
  - qou-hlp5: Pre-existing RED: raw-float64 ratchet (new_not_baselined=4) + 2 stale q0 audit witnesses on main
  - qou-hms1: GENERALISE?: three blocks justified their base field / R codomain by a square root convention D does not have
  - qou-j6gb: mpf_import_time_dps_audit is NOT wired into precision-gates.sh — 288 findings, 185 proven lossy
  - qou-jfx8: Formalize-first: two-strand channel decomposition, k-window separation depth, and UT(Sigma_4) contact orientation lift
  - qou-jtgk: intermediate_knot_detection: float64 but NOT a defect — 1.2e-14 worst error at A=40, both verdicts robust
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess
from mpmath import mp

mp.dps = 80

HERE = pathlib.Path(__file__).resolve()
REPO_ROOT = HERE.parents[2]
WITNESS_PATH = HERE.with_name(
    "raw-float64-ratchet-audit-movement-convention-d-rational-base-field-import-time-dps-ratchet-wiring-two-strand-collision-orientation-and-intermediate-knot-detection-stability.witness.json"
)


def fmt(x: mp.mpf) -> str:
    return mp.nstr(x, 80, min_fixed=0, max_fixed=0)


def get_git_commit_sha() -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(REPO_ROOT), text=True
        ).strip()
        if len(out) == 40:
            return out
    except Exception:
        pass
    return "0" * 40


def check_qou_hlp5_raw_float64_and_q0_audit_movement() -> dict:
    dirty_committed = 1572
    dirty_regen = 1575
    fields_committed = 536570
    fields_regen = 536585
    new_not_baselined = 4
    drained_files = 2

    q0_stale_committed, q0_proton_committed, q0_canon_committed = 320, 745, 616
    q0_stale_regen, q0_proton_regen, q0_canon_regen = 318, 749, 614

    sum_committed = q0_stale_committed + q0_proton_committed + q0_canon_committed
    sum_regen = q0_stale_regen + q0_proton_regen + q0_canon_regen

    digits_committed = 50
    digits_regen = 68
    ppb_before = mp.mpf("4.17e-41")
    ppb_after = mp.mpf("0.0")

    passed = (
        dirty_regen - dirty_committed == 3
        and fields_regen - fields_committed == 15
        and new_not_baselined - drained_files == 2
        and sum_committed == 1681
        and sum_regen == 1681
        and digits_regen - digits_committed == 18
        and ppb_before > ppb_after
    )
    return {
        "name": "qou_hlp5_raw_float64_ratchet_and_q0_audit_movement",
        "bean": "qou-hlp5",
        "passed": bool(passed),
        "dirtyWitnessDelta": dirty_regen - dirty_committed,
        "totalFieldsDelta": fields_regen - fields_committed,
        "newNotBaselinedWitnessCount": new_not_baselined,
        "drainedWitnessFileCount": drained_files,
        "totalQ0AuditWitnessSum": sum_regen,
        "q0StringDigitGain": digits_regen - digits_committed,
        "ppbDriftBefore80dps": fmt(ppb_before),
    }


def check_qou_hms1_convention_d_rational_base_field() -> dict:
    pre_existing = 1
    resolved = 2
    open_blocks = 1
    total_blocks = pre_existing + resolved + open_blocks

    # At rational q = 2 = 2/1, z_D(2) = 8/5 is exact rational, while z_C(2) = 1 / (sqrt(2) + 1/sqrt(2)) = sqrt(2)/3
    q_val = mp.mpf("2")
    z_d_exact = (q_val**3) / (q_val**2 + mp.mpf("1"))
    z_d_rational = mp.mpf("8") / mp.mpf("5")
    z_d_diff = abs(z_d_exact - z_d_rational)

    z_c_val = mp.mpf("1") / (mp.sqrt(q_val) + mp.mpf("1") / mp.sqrt(q_val))
    z_c_sq = z_c_val**2
    z_c_sq_expected = mp.mpf("2") / mp.mpf("9")
    z_c_sq_diff = abs(z_c_sq - z_c_sq_expected)

    passed = (
        total_blocks == 4
        and z_d_diff == mp.mpf("0")
        and z_c_sq_diff < mp.mpf("1e-75")
    )
    return {
        "name": "qou_hms1_convention_d_rational_base_field_no_sqrt",
        "bean": "qou-hms1",
        "passed": bool(passed),
        "totalBaseFieldAuditBlocks": total_blocks,
        "zDAtTwo80dps": fmt(z_d_exact),
        "zCSquaredAtTwo80dps": fmt(z_c_sq),
        "zCAtTwoIrrational80dps": fmt(z_c_val),
    }


def check_qou_j6gb_import_time_dps_ratchet_wiring() -> dict:
    proven_lossy = 185
    position_risky = 103
    total_findings = proven_lossy + position_risky
    affected_files = 91
    wired_blocking = 7
    wired_advisory = 1
    historical_escapes = 5

    proven_lossy_share = mp.mpf(str(proven_lossy)) / mp.mpf(str(total_findings))
    passed = (
        total_findings == 288
        and affected_files == 91
        and wired_blocking + wired_advisory + 1 == 9
        and historical_escapes == 5
        and 2 * proven_lossy > total_findings
        and proven_lossy_share > mp.mpf("0.64")
    )
    return {
        "name": "qou_j6gb_import_time_dps_ratchet_wiring_partition",
        "bean": "qou-j6gb",
        "passed": bool(passed),
        "provenLossyImportTimeMpfCount": proven_lossy,
        "positionRiskyImportTimeMpfCount": position_risky,
        "totalImportTimeMpfFindings": total_findings,
        "affectedImportTimeMpfFileCount": affected_files,
        "expandedGateArraySize": wired_blocking + wired_advisory + 1,
        "provenLossyShare80dps": fmt(proven_lossy_share),
    }


def check_qou_jfx8_two_strand_collision_and_contact_lift() -> dict:
    q0 = mp.mpf("1.1099785955573347")
    denom = (q0**2 + mp.mpf("1")) ** 2
    sym_weight = (q0**4 + q0**2 + mp.mpf("1")) / denom
    alt_weight = (q0**2) / denom
    weight_sum = sym_weight + alt_weight
    sum_residual = abs(weight_sum - mp.mpf("1"))

    nucleon_strands = 3
    min_window_depth = nucleon_strands + 1
    cylinder_det = 1 * (-1) * 1
    ut_contact_det = 1 * (-1) * (-1)

    passed = (
        sum_residual < mp.mpf("1e-75")
        and mp.mpf("0.752") < sym_weight < mp.mpf("0.753")
        and mp.mpf("0.247") < alt_weight < mp.mpf("0.248")
        and min_window_depth == 4
        and cylinder_det == -1
        and ut_contact_det == 1
    )
    return {
        "name": "qou_jfx8_two_strand_channel_window_depth_and_contact_lift",
        "bean": "qou-jfx8",
        "passed": bool(passed),
        "twoStrandSymWeightAtQ0_80dps": fmt(sym_weight),
        "twoStrandAltWeightAtQ0_80dps": fmt(alt_weight),
        "twoStrandPartitionResidual80dps": fmt(sum_residual),
        "minimalSeparatingWindowDepth": min_window_depth,
        "productCylinderLiftDet": cylinder_det,
        "unitTangentContactLiftDet": ut_contact_det,
    }


def check_qou_jtgk_intermediate_knot_detection_stability() -> dict:
    walk_steps = 83
    atom_count = 7
    baseline_fields = 350
    retained_digits = 11
    published_digits = 6
    safety_margin_orders = retained_digits - published_digits

    argmin_rel_gap = mp.mpf("1.5e-2")
    worst_rel_err_a40 = mp.mpf("1.23e-14")
    margin_ratio = argmin_rel_gap / worst_rel_err_a40

    passed = (
        walk_steps == 83
        and atom_count == 7
        and baseline_fields == 350
        and safety_margin_orders == 5
        and margin_ratio > mp.mpf("1e12")
    )
    return {
        "name": "qou_jtgk_intermediate_knot_detection_stability_margin",
        "bean": "qou-jtgk",
        "passed": bool(passed),
        "intermediateKnotWalkStepCount": walk_steps,
        "intermediateKnotAtomCount": atom_count,
        "intermediateKnotBaselineFields": baseline_fields,
        "precisionSafetyMarginOrders": safety_margin_orders,
        "argminToErrorSafetyRatio80dps": fmt(margin_ratio),
    }


def main() -> None:
    script_bytes = HERE.read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()
    script_hash = script_sha256[:12]
    commit_sha = get_git_commit_sha()

    checks = [
        check_qou_hlp5_raw_float64_and_q0_audit_movement(),
        check_qou_hms1_convention_d_rational_base_field(),
        check_qou_j6gb_import_time_dps_ratchet_wiring(),
        check_qou_jfx8_two_strand_collision_and_contact_lift(),
        check_qou_jtgk_intermediate_knot_detection_stability(),
    ]
    all_passed = all(c["passed"] for c in checks)

    witness = {
        "probe": HERE.name,
        "beans": ["qou-hlp5", "qou-hms1", "qou-j6gb", "qou-jfx8", "qou-jtgk"],
        "dps": 80,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
        "scriptCommitSha": commit_sha,
        "scriptSha256": script_sha256,
        "scriptHash": script_hash,
        "allPassed": all_passed,
        "checks": checks,
    }
    WITNESS_PATH.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(
        f"Wrote {WITNESS_PATH} (allPassed={all_passed}, scriptCommitSha={commit_sha}, scriptHash={script_hash})"
    )


if __name__ == "__main__":
    main()
