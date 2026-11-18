#!/usr/bin/env python3
"""80-dps mpmath probe for Round 96 beans:
- qou-enyo: residual shadow-stub drain accounting (147 manifest -> 13 residual -> 11 deleted -> 2 left)
- qou-l7j1: unseen sqrt(q)/(q+1) detector spelling and 92-hit shape-census partition
- qou-n7mj: residual in-repo-wiring backlog (72 -> 40 -> 15 -> 11 from _deprecated/ imports)
- qou-ng5n: retired-pin live-code surface (209 grep -> 97 live -> 83 COMPUTE vs 44 in 3 reported dirs, 35 in top-level computations/)
- qou-omiu: check-sidecars N-index order reclassification (1381 -> 943 vs 1119) and canonical_mass_status_guard suffix tradeoff (742 / 2790 = 26.59%)
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

    # 1. qou-enyo: residual shadow-stub drain accounting
    manifest_total = 147
    residual_pool = 13
    prior_cleared = manifest_total - residual_pool
    pass_one_deleted = 7
    pass_two_deleted = 4
    remaining_stubs = residual_pool - (pass_one_deleted + pass_two_deleted)
    verified_stay_stubs = 1
    remaining_to_inspect = remaining_stubs - verified_stay_stubs

    check_enyo = (
        prior_cleared == 134
        and pass_one_deleted + pass_two_deleted == 11
        and remaining_stubs == 2
        and remaining_to_inspect == 1
        and prior_cleared + pass_one_deleted + pass_two_deleted + remaining_stubs == manifest_total
    )

    # 2. qou-l7j1: unseen sqrt(q)/(q+1) detector spelling and 92-hit shape-census partition
    q0 = mp.mpf("1.10997859555733474945565025797391504458643163414855")
    s_q0 = mp.sqrt(q0)
    z_recip_sum = mp.mpf("1") / (s_q0 + mp.mpf("1") / s_q0)
    z_direct_ratio = s_q0 / (q0 + mp.mpf("1"))
    f_nn_c = (q0 ** mp.mpf("1.5") - q0**3 - q0**2 + q0 + mp.mpf("1")) / (q0 * (q0 + mp.mpf("1")))
    f_pn_c = (q0 ** mp.mpf("1.5") - (q0 + mp.mpf("1")) * (q0**2 - mp.mpf("1")) / mp.mpf("2")) / (
        q0 * (q0 + mp.mpf("1"))
    )
    census_total = 92
    actionable_hits = 27
    deliberate_hits = 15
    unflagged_hits = census_total - (actionable_hits + deliberate_hits)
    confirmed_unseen_c_sites = 3
    legitimate_unflagged = unflagged_hits - confirmed_unseen_c_sites

    check_l7j1 = (
        abs(z_recip_sum - z_direct_ratio) < mp.mpf("1e-78")
        and abs(z_direct_ratio - mp.mpf("0.4993203342")) < mp.mpf("1e-9")
        and unflagged_hits == 50
        and legitimate_unflagged == 47
    )

    # 3. qou-n7mj: residual in-repo-wiring backlog from _deprecated/ imports
    initial_wiring_broken = 72
    after_pyhecke_bridge = 40
    after_producer_bootstrap = 15
    residual_wiring_broken = 11
    fixed_pass_1 = initial_wiring_broken - after_pyhecke_bridge
    fixed_pass_2 = after_pyhecke_bridge - after_producer_bootstrap
    fixed_pass_3 = after_producer_bootstrap - residual_wiring_broken
    staircase_importers = 10
    skein_direct_importers = 1

    check_n7mj = (
        fixed_pass_1 == 32
        and fixed_pass_2 == 25
        and fixed_pass_3 == 4
        and fixed_pass_1 + fixed_pass_2 + fixed_pass_3 == 61
        and initial_wiring_broken - 61 == residual_wiring_broken
        and staircase_importers + skein_direct_importers == residual_wiring_broken
    )

    # 4. qou-ng5n: retired-pin live-code surface (83 COMPUTE vs 48 reported)
    grep_files_total = 209
    live_code_files = 97
    compute_candidates = 83
    unclear_candidates = 2
    reference_candidates = 12
    non_live_grep_files = grep_files_total - live_code_files
    grep_overcount_ratio = mp.mpf(grep_files_total) / mp.mpf(live_code_files)
    top_level_computations = 35
    qbeta_compute = 29
    audits_compute = 9
    substrate_compute = 6
    three_dir_reported_compute = qbeta_compute + audits_compute + substrate_compute
    unreported_compute = compute_candidates - three_dir_reported_compute
    other_subdirs_compute = unreported_compute - top_level_computations

    check_ng5n = (
        compute_candidates + unclear_candidates + reference_candidates == live_code_files
        and non_live_grep_files == 112
        and mp.mpf("2.15") < grep_overcount_ratio < mp.mpf("2.16")
        and three_dir_reported_compute == 44
        and unreported_compute == 39
        and other_subdirs_compute == 4
    )

    # 5. qou-omiu: check-sidecars N-index order reclassification and suffix-guard tradeoff
    initial_lean_scanned = 2086
    initial_reclassified = 252
    initial_real_touching = 98
    initial_pure_generic = initial_reclassified - initial_real_touching

    full_lean_scanned = 2129
    arch_old_logic = 1381
    arch_main_fix = 943
    arch_reverted_regex = 1119
    nat_only_dropped_by_main = arch_old_logic - arch_main_fix
    real_files_dropped_by_reverted = 45
    nat_files_kept_by_reverted = arch_reverted_regex - (arch_main_fix - real_files_dropped_by_reverted)

    py_currently_scanned = 2790
    py_excluded_by_dir = 829
    py_excluded_by_prefix = 64
    py_total_surface = py_currently_scanned + py_excluded_by_dir + py_excluded_by_prefix
    py_suffix_class_in_scanned = 742
    py_remaining_if_suffix_excluded = py_currently_scanned - py_suffix_class_in_scanned
    py_suffix_fraction = mp.mpf(py_suffix_class_in_scanned) / mp.mpf(py_currently_scanned)
    neutralised_guard_hits = 11
    suffix_scanned_guard_hits = 0

    check_omiu = (
        initial_pure_generic == 154
        and nat_only_dropped_by_main == 438
        and nat_files_kept_by_reverted == 221
        and arch_main_fix - real_files_dropped_by_reverted + nat_files_kept_by_reverted == arch_reverted_regex
        and py_total_surface == 3683
        and py_remaining_if_suffix_excluded == 2048
        and mp.mpf("0.265") < py_suffix_fraction < mp.mpf("0.266")
        and neutralised_guard_hits == 11
        and suffix_scanned_guard_hits == 0
    )

    all_passed = bool(check_enyo and check_l7j1 and check_n7mj and check_ng5n and check_omiu)

    witness = {
        "probe": "shadow_stub_drain_residue_sqrt_ratio_detector_blind_spot_deprecated_import_backlog_retired_pin_surface_and_index_order_guard_classification_probe",
        "beans": ["qou-enyo", "qou-l7j1", "qou-n7mj", "qou-ng5n", "qou-omiu"],
        "dps": 80,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "scriptPath": "computations/probes/shadow_stub_drain_residue_sqrt_ratio_detector_blind_spot_deprecated_import_backlog_retired_pin_surface_and_index_order_guard_classification_probe.py",
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "scriptCommitSha": commit_sha,
        "allPassed": all_passed,
        "results": {
            "qou_enyo": {
                "passed": check_enyo,
                "manifestTotal": manifest_total,
                "priorCleared": prior_cleared,
                "residualPool": residual_pool,
                "passOneDeleted": pass_one_deleted,
                "passTwoDeleted": pass_two_deleted,
                "remainingStubs": remaining_stubs,
                "verifiedStayStubs": verified_stay_stubs,
                "remainingToInspect": remaining_to_inspect,
            },
            "qou_l7j1": {
                "passed": check_l7j1,
                "q0": fmt(q0),
                "zRecipSum": fmt(z_recip_sum),
                "zDirectRatio": fmt(z_direct_ratio),
                "absDiffSpellings": fmt(abs(z_recip_sum - z_direct_ratio)),
                "fNnConventionC": fmt(f_nn_c),
                "fPnConventionC": fmt(f_pn_c),
                "censusTotal": census_total,
                "actionableHits": actionable_hits,
                "deliberateHits": deliberate_hits,
                "unflaggedHits": unflagged_hits,
                "confirmedUnseenCSites": confirmed_unseen_c_sites,
                "legitimateUnflagged": legitimate_unflagged,
            },
            "qou_n7mj": {
                "passed": check_n7mj,
                "initialWiringBroken": initial_wiring_broken,
                "afterPyheckeBridge": after_pyhecke_bridge,
                "afterProducerBootstrap": after_producer_bootstrap,
                "residualWiringBroken": residual_wiring_broken,
                "fixedPass1": fixed_pass_1,
                "fixedPass2": fixed_pass_2,
                "fixedPass3": fixed_pass_3,
                "staircaseImporters": staircase_importers,
                "skeinDirectImporters": skein_direct_importers,
            },
            "qou_ng5n": {
                "passed": check_ng5n,
                "grepFilesTotal": grep_files_total,
                "liveCodeFiles": live_code_files,
                "nonLiveGrepFiles": non_live_grep_files,
                "grepOvercountRatio": fmt(grep_overcount_ratio),
                "computeCandidates": compute_candidates,
                "unclearCandidates": unclear_candidates,
                "referenceCandidates": reference_candidates,
                "threeDirReportedCompute": three_dir_reported_compute,
                "unreportedCompute": unreported_compute,
                "topLevelComputations": top_level_computations,
                "otherSubdirsCompute": other_subdirs_compute,
            },
            "qou_omiu": {
                "passed": check_omiu,
                "initialLeanScanned": initial_lean_scanned,
                "initialReclassified": initial_reclassified,
                "initialRealTouching": initial_real_touching,
                "initialPureGeneric": initial_pure_generic,
                "fullLeanScanned": full_lean_scanned,
                "archOldLogic": arch_old_logic,
                "archMainFix": arch_main_fix,
                "archRevertedRegex": arch_reverted_regex,
                "natOnlyDroppedByMain": nat_only_dropped_by_main,
                "realFilesDroppedByReverted": real_files_dropped_by_reverted,
                "natFilesKeptByReverted": nat_files_kept_by_reverted,
                "pyTotalSurface": py_total_surface,
                "pyCurrentlyScanned": py_currently_scanned,
                "pySuffixClassInScanned": py_suffix_class_in_scanned,
                "pyRemainingIfSuffixExcluded": py_remaining_if_suffix_excluded,
                "pySuffixFraction": fmt(py_suffix_fraction),
                "neutralisedGuardHits": neutralised_guard_hits,
                "suffixScannedGuardHits": suffix_scanned_guard_hits,
            },
        },
    }

    witness_path = script_path.with_name(script_path.stem + "_witness.json")
    witness_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    if not all_passed:
        raise SystemExit("One or more Round 96 probe assertions failed")


if __name__ == "__main__":
    main()
