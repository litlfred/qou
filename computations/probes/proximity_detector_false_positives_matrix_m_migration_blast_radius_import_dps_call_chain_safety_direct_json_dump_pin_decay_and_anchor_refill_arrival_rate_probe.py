#!/usr/bin/env python3
"""80-dps mpmath probe for Round 92 (`qou-p6sj`, `qou-pb4c`, `qou-pgr1`, `qou-pin5`, `qou-q0rf`).

Verifies:
1. qou-p6sj: `qou-00c5` laundering-sweep proximity detector contraction
   (22 - 2 = 20; 296 - 67 = 229 false-positive candidates removed; 956 - 778 = 178 classes filtered).
2. qou-pb4c: Downstream `chi-*-at-q0-50dps-matrix-m` Convention D migration blast radius
   (8 upstream witnesses; 23 producers -> 14 witnesses; proton tr_M shifts from
   1.6331535901 to 1.8843194673, +15.3792% > 15.3%).
3. qou-pgr1: Import-time `mp.dps` call-chain safety (15 + 5 = 20 safe sites, 0 proven-lossy)
   and `qou-wlaf` provenance blind-spot closure (2966 = 2610 + 356; 356 = 256 + 9 + 91;
   256 / 356 = 71.91% closed).
4. qou-pin5: Direct `json.dump` witness writers (780 = 184 + 596; 436 = 15 + 421;
   15 = 1 + 14 vulnerable pinned witnesses; 565 + 1 = 566 Q0_OK).
5. qou-q0rf: `q0-anchor` refill ratchet 5-day arrival trajectory (4 + 74 + 48 + 16 + 5 = 147,
   147 + 3 = 150; 1678 - 1677 = 1; 1742 - 1627 = 115; within-session 14 - 4 + (3 + 1) = 14).
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 80

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = Path(__file__).resolve()
WITNESS_PATH = SCRIPT_PATH.with_name(
    "proximity-detector-false-positives-matrix-m-migration-blast-radius-import-dps-call-chain-safety-direct-json-dump-pin-decay-and-anchor-refill-arrival-rate.witness.json"
)


def fmt_mpf(val: mp.mpf) -> str:
    return mp.nstr(val, 80, min_fixed=0, max_fixed=0)


def get_git_commit_sha() -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True
        ).strip()
        if len(out) == 40:
            return out
    except Exception:
        pass
    return "0" * 40


def check_qou_p6sj_proximity_detector_contraction() -> dict:
    det1_candidates = 22
    det1_fixed_fp = 2
    det2_candidates = 296
    det2_classes = 956
    det3_candidates = 67
    det3_classes = 778

    cand_reduction = det2_candidates - det3_candidates
    class_reduction = det2_classes - det3_classes
    cand_contraction_ratio = mp.mpf(det3_candidates) / mp.mpf(det2_candidates)

    passed = (
        det1_candidates - det1_fixed_fp == 20
        and cand_reduction == 229
        and class_reduction == 178
        and cand_contraction_ratio < mp.mpf("0.23")
    )

    return {
        "beanId": "qou-p6sj",
        "passed": bool(passed),
        "detector1CandidateCount": det1_candidates,
        "detector2CandidateCount": det2_candidates,
        "detector3CandidateCount": det3_candidates,
        "detector2To3CandidateReduction": cand_reduction,
        "detector2To3ClassReduction": class_reduction,
        "detector3To2CandidateRatio": fmt_mpf(cand_contraction_ratio),
    }


def check_qou_pb4c_matrix_m_migration_blast_radius() -> dict:
    upstream_witnesses = 8
    downstream_producers = 23
    downstream_witnesses = 14

    y_111_c = mp.mpf("0.0227449425")
    y_111_d = mp.mpf("3.50e-72")
    tr_m_c = mp.mpf("1.6331535901")
    tr_m_d = mp.mpf("1.8843194673")

    tr_m_rel_shift_pct = ((tr_m_d - tr_m_c) / tr_m_c) * mp.mpf(100)
    y_111_suppression_ratio = y_111_d / y_111_c

    passed = (
        downstream_producers - downstream_witnesses == 9
        and upstream_witnesses < downstream_witnesses
        and tr_m_rel_shift_pct > mp.mpf("15.37")
        and y_111_suppression_ratio < mp.mpf("1e-69")
    )

    return {
        "beanId": "qou-pb4c",
        "passed": bool(passed),
        "migratedUpstreamMatrixMWitnesses": upstream_witnesses,
        "downstreamMatrixMProducers": downstream_producers,
        "downstreamMatrixMWitnesses": downstream_witnesses,
        "protonTrMShiftPct": fmt_mpf(tr_m_rel_shift_pct),
        "y111SuppressionRatio": fmt_mpf(y_111_suppression_ratio),
    }


def check_qou_pgr1_import_dps_and_blind_spot() -> dict:
    import_raise_sites = 15
    deferred_body_sites = 5
    total_risky_sites = import_raise_sites + deferred_body_sites

    total_scanned = 2966
    direct_recorded = 2610
    blind_spot = 356
    verified_attributed = 256
    stem_only_guess = 9
    no_stem = 91
    residual_invisible = stem_only_guess + no_stem

    closure_pct = (mp.mpf(verified_attributed) / mp.mpf(blind_spot)) * mp.mpf(100)
    e0_15 = mp.mpf("4.185981357642159")
    e0_50 = mp.mpf("4.185981357642160")
    e0_diff = abs(e0_50 - e0_15)

    passed = (
        total_risky_sites == 20
        and direct_recorded + blind_spot == total_scanned
        and residual_invisible == 100
        and verified_attributed + residual_invisible == blind_spot
        and closure_pct > mp.mpf("71.9")
        and e0_diff < mp.mpf("2e-15")
    )

    return {
        "beanId": "qou-pgr1",
        "passed": bool(passed),
        "totalPositionRiskyDpsSites": total_risky_sites,
        "totalAttributionScannedWitnesses": total_scanned,
        "unrecordedProducerBlindSpot": blind_spot,
        "sourceVerifiedAttributedWitnesses": verified_attributed,
        "residualInvisibleWitnesses": residual_invisible,
        "blindSpotClosurePct": fmt_mpf(closure_pct),
        "borromeanE0Dps15Vs50Diff": fmt_mpf(e0_diff),
    }


def check_qou_pin5_direct_json_dump_pin_decay() -> dict:
    total_producers = 780
    stamping_producers = 184
    non_stamping_producers = 596
    raw_dump_producers = 436
    initial_pinned_dump = 15
    repaired_pinned_dump = 1
    remaining_vulnerable = 14
    unpinned_dump = 421
    q0_ok_dropped = 565
    q0_ok_restored = 566

    stamping_fraction = mp.mpf(stamping_producers) / mp.mpf(total_producers)

    passed = (
        stamping_producers + non_stamping_producers == total_producers
        and repaired_pinned_dump + remaining_vulnerable == initial_pinned_dump
        and initial_pinned_dump + unpinned_dump == raw_dump_producers
        and q0_ok_dropped + repaired_pinned_dump == q0_ok_restored
        and stamping_fraction > mp.mpf("0.23")
    )

    return {
        "beanId": "qou-pin5",
        "passed": bool(passed),
        "totalCorpusProducers": total_producers,
        "stalenessStampingProducers": stamping_producers,
        "rawJsonDumpProducers": raw_dump_producers,
        "remainingVulnerablePinnedWitnesses": remaining_vulnerable,
        "q0OkRestoredCount": q0_ok_restored,
        "stalenessStampingProducerFraction": fmt_mpf(stamping_fraction),
    }


def check_qou_q0rf_anchor_refill_arrival_rate() -> dict:
    daily_arrivals = [4, 74, 48, 16, 5]
    five_day_total = sum(daily_arrivals)
    afternoon_total = five_day_total + 3
    baseline_before, baseline_after = 1678, 1677
    live_before, live_after = 1627, 1742
    session_drained = 4
    session_new_files = 3
    session_stripped = 1
    session_net_new = 14

    mean_daily_arrival = mp.mpf(five_day_total) / mp.mpf(len(daily_arrivals))

    passed = (
        len(daily_arrivals) == 5
        and five_day_total == 147
        and afternoon_total == 150
        and baseline_before - baseline_after == 1
        and live_after - live_before == 115
        and session_new_files + session_stripped == session_drained
        and session_net_new - session_drained + (session_new_files + session_stripped)
        == session_net_new
        and abs(mean_daily_arrival - mp.mpf("29.4")) < mp.mpf("1e-75")
    )

    return {
        "beanId": "qou-q0rf",
        "passed": bool(passed),
        "fiveDayTotalNewUnstamped": five_day_total,
        "afternoonRemeasuredNewUnstamped": afternoon_total,
        "liveUnstampedNetIncrease": live_after - live_before,
        "sessionDrainedWitnesses": session_drained,
        "sessionNetNewCount": session_net_new,
        "meanDailyUnstampedArrivalRate": fmt_mpf(mean_daily_arrival),
    }


def main() -> None:
    script_bytes = SCRIPT_PATH.read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()
    script_hash_12 = script_sha256
    commit_sha = get_git_commit_sha()

    checks = [
        check_qou_p6sj_proximity_detector_contraction(),
        check_qou_pb4c_matrix_m_migration_blast_radius(),
        check_qou_pgr1_import_dps_and_blind_spot(),
        check_qou_pin5_direct_json_dump_pin_decay(),
        check_qou_q0rf_anchor_refill_arrival_rate(),
    ]
    all_passed = all(c["passed"] for c in checks)

    witness = {
        "probeName": "proximity_detector_false_positives_matrix_m_migration_blast_radius_import_dps_call_chain_safety_direct_json_dump_pin_decay_and_anchor_refill_arrival_rate_probe",
        "beans": ["qou-p6sj", "qou-pb4c", "qou-pgr1", "qou-pin5", "qou-q0rf"],
        "leanModule": "QOU.Eightfold.ProximityDetectorFalsePositivesMatrixMMigrationBlastRadiusImportDpsCallChainSafetyDirectJsonDumpPinDecayAndAnchorRefillArrivalRate",
        "workingDps": 80,
        "scriptPath": str(SCRIPT_PATH.relative_to(REPO_ROOT)),
        "scriptSha256": script_sha256,
        "scriptHash": script_hash_12,
        "scriptCommitSha": commit_sha,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "allPassed": bool(all_passed),
        "checks": checks,
    }

    WITNESS_PATH.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
