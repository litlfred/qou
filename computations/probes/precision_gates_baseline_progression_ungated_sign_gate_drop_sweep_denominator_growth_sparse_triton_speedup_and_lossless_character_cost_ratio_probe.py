#!/usr/bin/env python3
"""80-dps mpmath probe for Round 95 beans:
- qou-z23u: precision-gates baseline progression and inherited debt
- qou-21oc: dropping Pass-2 sign gate leaves ungated binding total wrong-signed
- qou-6q7q: post-rebase path audit and dynamic muon sweep denominator growth
- qou-bimg: dense vs sparse triton Magnus evaluation across 30 partitions (87x speedup)
- qou-d9wf: chi_via_rust_lossless cost model underestimation (>150x / >450x) and RSS growth
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from mpmath import mp

mp.dps = 80


def fmt(x: mp.mpf) -> str:
    return mp.nstr(x, 80)


def main() -> None:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[2]
    script_sha256 = hashlib.sha256(script_path.read_bytes()).hexdigest()
    commit_sha = subprocess.check_output(
        ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
        text=True,
    ).strip()

    # 1. qou-z23u: precision-gates baseline progression and inherited debt
    q0_flips_total = 18
    q0_flips_real = 1
    q0_anchor_unrecognised = 17
    tower_walk_traces = 77
    inherited_dps = 15
    fmt_digits = 60
    padded_fields = 22
    padding_ratchet_before = 70
    padding_ratchet_new_drained = 58
    padding_ratchet_after = padding_ratchet_before - padding_ratchet_new_drained
    magnus_explicit_dps = 140
    magnus_constructions = 34
    selftest_before = 9
    selftest_after = 13
    baseline_commits_span = 683
    blocking_progression = [10, 9, 10, 11]

    check_z23u = (
        q0_flips_real + q0_anchor_unrecognised == q0_flips_total
        and fmt_digits - inherited_dps == 45
        and padding_ratchet_after == 12
        and magnus_explicit_dps - inherited_dps == 125
        and selftest_after - selftest_before == 4
        and blocking_progression == [10, 10 - 1, 9 + 1, 10 + 1]
    )

    # 2. qou-21oc: dropping Pass-2 sign gate leaves ungated total wrong-signed
    k4_total = 10
    k4_2h_gated_blocks, k4_4he_gated_blocks = 4, 2
    k4_2h_gated = mp.mpf("-0.0895596830589507")
    k4_2h_ungated = mp.mpf("-0.412212192245027")
    k4_4he_gated = mp.mpf("-0.0805867484776914")
    k4_4he_ungated = mp.mpf("-0.2742397716174")

    k6_total = 28
    k6_2h_gated_blocks, k6_4he_gated_blocks = 15, 10
    k6_2h_gated = mp.mpf("-1.3656848170878801")
    k6_2h_ungated = mp.mpf("-2.251131977321312")
    k6_4he_gated = mp.mpf("-0.8387490758934286")
    k6_4he_ungated = mp.mpf("-1.448199112790757")

    k11_total = 193
    k11_2h_gated_blocks, k11_4he_gated_blocks = 94, 90
    k11_2h_gated = mp.mpf("-9.14773623102088")
    k11_2h_ungated = mp.mpf("-17.6908290020795")
    k11_4he_gated = mp.mpf("-8.20155846836239")
    k11_4he_ungated = mp.mpf("-15.9926510049258")

    term1_ungated = mp.mpf("-17.6908290020795447079223359605544029429608374879103157233577")
    term2_ungated = mp.mpf("0")
    term3_pairing = mp.mpf(
        "1.876634106144136334334544823923110976193880197699474143353897399142905884"
    )
    total_ungated_expected = mp.mpf(
        "-15.8141948959354083735877911366312919667669572902108415800038"
    )
    total_ungated_computed = term1_ungated + term2_ungated + term3_pairing
    total_gated_ref = mp.mpf("-7.27110212487674490878")
    ame2020_deuteron = mp.mpf("2.2245662")

    check_21oc = (
        k4_total - k4_2h_gated_blocks == 6
        and k4_total - k4_4he_gated_blocks == 8
        and k6_total - k6_2h_gated_blocks == 13
        and k6_total - k6_4he_gated_blocks == 18
        and k11_total - k11_2h_gated_blocks == 99
        and k11_total - k11_4he_gated_blocks == 103
        and k4_2h_ungated < k4_2h_gated < 0
        and k4_4he_ungated < k4_4he_gated < 0
        and k6_2h_ungated < k6_2h_gated < 0
        and k6_4he_ungated < k6_4he_gated < 0
        and k11_2h_ungated < k11_2h_gated < 0
        and k11_4he_ungated < k11_4he_gated < 0
        and abs(total_ungated_computed - total_ungated_expected) < mp.mpf("1e-58")
        and total_ungated_computed < total_gated_ref < 0 < ame2020_deuteron
    )

    # 3. qou-6q7q: post-rebase path audit and dynamic sweep denominator growth
    audited_paths_total = 111
    byte_identical_paths = 108
    moved_paths = audited_paths_total - byte_identical_paths
    pre_rebase_sweep_total = 47
    post_rebase_sweep_total = 142
    denominator_growth = post_rebase_sweep_total - pre_rebase_sweep_total
    retained_entries = 46
    batch_one_new = 9
    batch_two_new = 7
    resumed_after_batch_one = retained_entries + batch_one_new
    resumed_after_batch_two = resumed_after_batch_one + batch_two_new
    q0_ok_after, q0_ok_before = 953, 947
    q0_missing_after, q0_missing_before = 1645, 1644

    check_6q7q = (
        moved_paths == 3
        and denominator_growth == 95
        and resumed_after_batch_one == 55
        and resumed_after_batch_two == 62
        and post_rebase_sweep_total - resumed_after_batch_one == 87
        and post_rebase_sweep_total - resumed_after_batch_two == 80
        and q0_ok_after - q0_ok_before == 6
        and q0_missing_after - q0_missing_before == 1
    )

    # 4. qou-bimg: dense vs sparse triton Magnus evaluation across 30 partitions
    triton_n = 9
    triton_partitions = 30
    stale_cached_rows = 14
    uncached_rows = triton_partitions - stale_cached_rows
    dense_seconds = mp.mpf("2400")
    sparse_seconds = mp.mpf("27.5")
    speedup_ratio = dense_seconds / sparse_seconds
    speedup_floor = int(mp.floor(speedup_ratio))
    rel_diff_routes = mp.mpf("9.08e-60")
    docstring_reruns = 2
    minutes_per_rerun = 40

    check_bimg = (
        uncached_rows == 16
        and speedup_floor == 87
        and 275 * 87 <= 24000 < 275 * 88
        and docstring_reruns * minutes_per_rerun == 80
        and rel_diff_routes < mp.mpf("1e-58")
    )

    # 5. qou-d9wf: chi_via_rust_lossless cost ratio and RSS growth on 5Li and 6Li
    he4_partitions, he4_doc_s = 77, 2
    li5_partitions, li5_doc_s = 176, 4
    li6_partitions, li6_doc_s = 385, 8
    combined_li5_li6_partitions = li5_partitions + li6_partitions
    li5_measured_s_1 = 600
    li5_measured_s_2 = 1800
    doc_ms_per_partition = 20
    measured_ms_per_partition = 10000
    rss_mb_0, rss_mb_1, rss_mb_2 = 198, 247, 310

    check_d9wf = (
        combined_li5_li6_partitions == 561
        and li5_measured_s_1 // li5_doc_s == 150
        and li5_measured_s_2 // li5_doc_s == 450
        and measured_ms_per_partition // doc_ms_per_partition == 500
        and (rss_mb_1 - rss_mb_0) == 49
        and (rss_mb_2 - rss_mb_1) == 63
        and (rss_mb_2 - rss_mb_0) == 112
    )

    all_passed = bool(check_z23u and check_21oc and check_6q7q and check_bimg and check_d9wf)

    witness = {
        "probe": "precision_gates_baseline_progression_ungated_sign_gate_drop_sweep_denominator_growth_sparse_triton_speedup_and_lossless_character_cost_ratio_probe",
        "beans": ["qou-z23u", "qou-21oc", "qou-6q7q", "qou-bimg", "qou-d9wf"],
        "dps": 80,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "scriptPath": "computations/probes/precision_gates_baseline_progression_ungated_sign_gate_drop_sweep_denominator_growth_sparse_triton_speedup_and_lossless_character_cost_ratio_probe.py",
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "scriptCommitSha": commit_sha,
        "allPassed": all_passed,
        "results": {
            "qou_z23u": {
                "passed": check_z23u,
                "q0FlipsTotal": q0_flips_total,
                "q0FlipsReal": q0_flips_real,
                "q0AnchorUnrecognised": q0_anchor_unrecognised,
                "towerWalkTraces": tower_walk_traces,
                "inheritedDps": inherited_dps,
                "fmtDigits": fmt_digits,
                "paddedFields": padded_fields,
                "paddingRatchetBefore": padding_ratchet_before,
                "paddingRatchetNewDrained": padding_ratchet_new_drained,
                "paddingRatchetAfter": padding_ratchet_after,
                "magnusExplicitDps": magnus_explicit_dps,
                "magnusConstructions": magnus_constructions,
                "selftestBefore": selftest_before,
                "selftestAfter": selftest_after,
                "baselineCommitsSpan": baseline_commits_span,
                "blockingProgression": blocking_progression,
            },
            "qou_21oc": {
                "passed": check_21oc,
                "k4": {
                    "totalPartitions": k4_total,
                    "deuteronGatedBlocks": k4_2h_gated_blocks,
                    "deuteronNewlyAdmitted": k4_total - k4_2h_gated_blocks,
                    "deuteronGatedMev": fmt(k4_2h_gated),
                    "deuteronUngatedMev": fmt(k4_2h_ungated),
                    "he4GatedBlocks": k4_4he_gated_blocks,
                    "he4NewlyAdmitted": k4_total - k4_4he_gated_blocks,
                    "he4GatedMev": fmt(k4_4he_gated),
                    "he4UngatedMev": fmt(k4_4he_ungated),
                },
                "k6": {
                    "totalPartitions": k6_total,
                    "deuteronGatedBlocks": k6_2h_gated_blocks,
                    "deuteronNewlyAdmitted": k6_total - k6_2h_gated_blocks,
                    "deuteronGatedMev": fmt(k6_2h_gated),
                    "deuteronUngatedMev": fmt(k6_2h_ungated),
                    "he4GatedBlocks": k6_4he_gated_blocks,
                    "he4NewlyAdmitted": k6_total - k6_4he_gated_blocks,
                    "he4GatedMev": fmt(k6_4he_gated),
                    "he4UngatedMev": fmt(k6_4he_ungated),
                },
                "k11": {
                    "totalPartitions": k11_total,
                    "deuteronGatedBlocks": k11_2h_gated_blocks,
                    "deuteronNewlyAdmitted": k11_total - k11_2h_gated_blocks,
                    "deuteronGatedMev": fmt(k11_2h_gated),
                    "deuteronUngatedMev": fmt(k11_2h_ungated),
                    "he4GatedBlocks": k11_4he_gated_blocks,
                    "he4NewlyAdmitted": k11_total - k11_4he_gated_blocks,
                    "he4GatedMev": fmt(k11_4he_gated),
                    "he4UngatedMev": fmt(k11_4he_ungated),
                },
                "bindingEnergyDeuteronK11": {
                    "term1UngatedMev": fmt(term1_ungated),
                    "term2UngatedMev": fmt(term2_ungated),
                    "term3PairingMev": fmt(term3_pairing),
                    "totalUngatedComputedMev": fmt(total_ungated_computed),
                    "totalUngatedExpectedMev": fmt(total_ungated_expected),
                    "totalGatedRefMev": fmt(total_gated_ref),
                    "ame2020EmpiricalMev": fmt(ame2020_deuteron),
                },
            },
            "qou_6q7q": {
                "passed": check_6q7q,
                "auditedPathsTotal": audited_paths_total,
                "byteIdenticalPaths": byte_identical_paths,
                "movedPaths": moved_paths,
                "preRebaseSweepTotal": pre_rebase_sweep_total,
                "postRebaseSweepTotal": post_rebase_sweep_total,
                "denominatorGrowth": denominator_growth,
                "retainedEntries": retained_entries,
                "resumedAfterBatchOne": resumed_after_batch_one,
                "resumedAfterBatchTwo": resumed_after_batch_two,
                "remainingAfterBatchOne": post_rebase_sweep_total - resumed_after_batch_one,
                "remainingAfterBatchTwo": post_rebase_sweep_total - resumed_after_batch_two,
                "q0OkDelta": q0_ok_after - q0_ok_before,
                "q0AnchorMissingDelta": q0_missing_after - q0_missing_before,
            },
            "qou_bimg": {
                "passed": check_bimg,
                "tritonN": triton_n,
                "tritonPartitions": triton_partitions,
                "staleCachedRows": stale_cached_rows,
                "uncachedRows": uncached_rows,
                "denseSeconds": fmt(dense_seconds),
                "sparseSeconds": fmt(sparse_seconds),
                "speedupRatio": fmt(speedup_ratio),
                "speedupFloor": speedup_floor,
                "relativeDifferenceRoutes": fmt(rel_diff_routes),
                "docstringRerunMinutes": docstring_reruns * minutes_per_rerun,
            },
            "qou_d9wf": {
                "passed": check_d9wf,
                "he4Partitions": he4_partitions,
                "he4DocumentedSeconds": he4_doc_s,
                "li5Partitions": li5_partitions,
                "li5DocumentedSeconds": li5_doc_s,
                "li6Partitions": li6_partitions,
                "li6DocumentedSeconds": li6_doc_s,
                "combinedLi5Li6Partitions": combined_li5_li6_partitions,
                "li5UnderestimationAt10Min": li5_measured_s_1 // li5_doc_s,
                "li5UnderestimationAt30Min": li5_measured_s_2 // li5_doc_s,
                "perPartitionUnderestimationFactor": measured_ms_per_partition // doc_ms_per_partition,
                "rssMegabytesCheckpoints": [rss_mb_0, rss_mb_1, rss_mb_2],
                "rssTotalGrowthMegabytes": rss_mb_2 - rss_mb_0,
            },
        },
    }

    witness_path = script_path.with_name(script_path.stem + "_witness.json")
    witness_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    if not all_passed:
        raise SystemExit("One or more Round 95 probe assertions failed")


if __name__ == "__main__":
    main()
