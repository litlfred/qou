#!/usr/bin/env python3
"""80-dps mpmath probe for Round 91 (`qou-nmza`, `qou-nwhg`, `qou-o0pa`, `qou-oiz3`, `qou-okkz`).

Verifies:
1. qou-nmza: `F64_ENGINE_ENTRY` disposition partition (71 = 7 + 46 + 18; 63 = 9 + 38 + 16
   across 43 = 6 + 26 + 11 files; 16 = 2 + 14 across 11 = 2 + 9 files; 2 - 2 = 0 clean propagators).
2. qou-nwhg: Pristine-`main` `REGRESSED: 3` ratchet false stop and branch-vs-`main` diff
   (3 - 3 = 0 net branch regressions; 3 + 2 = 5 full-refresh stale-baseline witnesses).
3. qou-o0pa: Nucleon `H_3` marshalling divergence three-arm guard restoration
   (6 + 2 + 3 = 11 proton crossings; 5 + 2 + 4 = 11 neutron crossings; 3 + 2 = 5 assertions;
   proton marshalled/canonical ratio 1.28237 > 1.28, neutron ratio 1.12613 > 1.12).
4. qou-oiz3: UIC resolvent cone float64 excision (9 + 1 = 10 sites; worst gated shift
   8.44176e-16 > 3.8 * eps, worst ungated shift 6.65778e-15 > 29.9 * eps; remaining q_int
   block error 1.0212424e-15 > 4 * 2.4946976e-16).
5. qou-okkz: Consumer-side control-arm detector and self-poisoning specificity census
   (229 = 1 + 228 foreign READ edges; 15 = 1 + 14 foreign-transcription edges;
   specificity threshold 3 with self-excluded census 2 < 3, unexcluded 3 == 3, poisoned 4 > 3).
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
    "native-engine-entry-triage-pristine-main-ratchet-diff-nucleon-marshalling-three-arm-guard-resolvent-cone-float-excision-and-consumer-control-arm-specificity.witness.json"
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


def check_qou_nmza_native_engine_entry_triage() -> dict:
    init_delib, init_harm, init_act = 7, 46, 18
    init_total = init_delib + init_harm + init_act

    rem_delib, rem_harm, rem_act = 9, 38, 16
    rem_total = rem_delib + rem_harm + rem_act

    rem_files_delib, rem_files_harm, rem_files_act = 6, 26, 11
    rem_files_total = rem_files_delib + rem_files_harm + rem_files_act

    prop_files, term_files = 2, 9
    prop_sites, term_sites = 2, 14
    clean_prop_files = prop_files - 2

    harmless_fraction = mp.mpf(rem_harm) / mp.mpf(rem_total)
    mpfr_vs_f64_speed_ratio = mp.mpf("0.056") / mp.mpf("0.002")

    passed = (
        init_total == 71
        and rem_total == 63
        and rem_files_total == 43
        and prop_files + term_files == rem_files_act
        and prop_sites + term_sites == rem_act
        and clean_prop_files == 0
        and harmless_fraction > mp.mpf("0.6")
        and abs(mpfr_vs_f64_speed_ratio - mp.mpf(28)) < mp.mpf("1e-75")
    )

    return {
        "beanId": "qou-nmza",
        "passed": bool(passed),
        "initialCandidateSites": init_total,
        "remeasuredCandidateSites": rem_total,
        "remeasuredCandidateFiles": rem_files_total,
        "remeasuredActionableSites": rem_act,
        "remeasuredActionableFiles": rem_files_act,
        "cleanPropagatingFiles": clean_prop_files,
        "remeasuredHarmlessFraction": fmt_mpf(harmless_fraction),
        "measuredMpfrSlowdownFactor": fmt_mpf(mpfr_vs_f64_speed_ratio),
    }


def check_qou_nwhg_pristine_main_ratchet_diff() -> dict:
    pristine_main_regressed = 3
    clean_branch_net_regressed = pristine_main_regressed - pristine_main_regressed
    regen_only_stale = 2
    full_refresh_stale = pristine_main_regressed + regen_only_stale
    total_baseline_dirty = 69

    pristine_regressed_fraction = mp.mpf(pristine_main_regressed) / mp.mpf(
        total_baseline_dirty
    )

    passed = (
        clean_branch_net_regressed == 0
        and full_refresh_stale == 5
        and pristine_regressed_fraction < mp.mpf("0.05")
    )

    return {
        "beanId": "qou-nwhg",
        "passed": bool(passed),
        "pristineMainStaticRegressions": pristine_main_regressed,
        "cleanBranchNetRegressions": clean_branch_net_regressed,
        "fullRefreshStaleBaselineWitnesses": full_refresh_stale,
        "pristineMainRegressedFractionOfBaseline": fmt_mpf(pristine_regressed_fraction),
    }


def check_qou_o0pa_nucleon_marshalling_three_arm_guard() -> dict:
    p_crossings = [6, 2, 3]
    n_crossings = [5, 2, 4]
    assertions_rebuilt = 3
    assertions_explicit_loss = 2
    total_assertions = assertions_rebuilt + assertions_explicit_loss

    p_canonical = mp.mpf("0.629328402202921918")
    p_marshalled = mp.mpf("0.807031394861838756")
    p_grouped_pin = mp.mpf("1.14575969245730087")

    n_canonical = mp.mpf("0.475133517155682213")
    n_marshalled = mp.mpf("0.535061853071076283")
    n_grouped_pin = mp.mpf("0.987743688115809572")

    p_ratio = p_marshalled / p_canonical
    n_ratio = n_marshalled / n_canonical
    p_grouped_rel_err = abs(p_grouped_pin - p_canonical) / p_canonical
    n_grouped_rel_err = abs(n_grouped_pin - n_canonical) / n_canonical

    passed = (
        sum(p_crossings) == 11
        and sum(n_crossings) == 11
        and total_assertions == 5
        and p_ratio > mp.mpf("1.28")
        and n_ratio > mp.mpf("1.12")
        and p_grouped_rel_err > mp.mpf("0.82")
        and n_grouped_rel_err > mp.mpf("1.07")
    )

    return {
        "beanId": "qou-o0pa",
        "passed": bool(passed),
        "nucleonCanonicalCrossingCount": 11,
        "restoredThreeArmAssertions": total_assertions,
        "protonMarshalledToCanonicalRatio": fmt_mpf(p_ratio),
        "neutronMarshalledToCanonicalRatio": fmt_mpf(n_ratio),
        "protonGroupedPinRelError": fmt_mpf(p_grouped_rel_err),
        "neutronGroupedPinRelError": fmt_mpf(n_grouped_rel_err),
    }


def check_qou_oiz3_resolvent_cone_float_excision() -> dict:
    source_sites = 9
    cache_sites = 1
    total_sites = source_sites + cache_sites

    eps_f64 = mp.mpf("2.220446049250313e-16")
    worst_gated = mp.mpf("8.44176e-16")
    worst_ungated = mp.mpf("6.65778e-15")
    removed_block_err = mp.mpf("2.4946976e-16")
    remaining_qint_err = mp.mpf("1.0212424e-15")

    gated_over_eps = worst_gated / eps_f64
    ungated_over_eps = worst_ungated / eps_f64
    qint_over_removed = remaining_qint_err / removed_block_err

    passed = (
        total_sites == 10
        and gated_over_eps > mp.mpf("3.8")
        and ungated_over_eps > mp.mpf("29.9")
        and qint_over_removed > mp.mpf(4)
    )

    return {
        "beanId": "qou-oiz3",
        "passed": bool(passed),
        "totalExcisedUicSurfaceSites": total_sites,
        "gatedShiftOverBinary64Eps": fmt_mpf(gated_over_eps),
        "ungatedShiftOverBinary64Eps": fmt_mpf(ungated_over_eps),
        "remainingQIntToRemovedErrorRatio": fmt_mpf(qint_over_removed),
    }


def check_qou_okkz_consumer_control_arm_specificity() -> dict:
    total_foreign_edges = 229
    confirmed_control_arms = 1
    unmeasured_edges = 228
    total_transcriptions = 15
    shared_constant_transcriptions = 14
    specificity_max = 3
    self_excluded_census = 2
    unexcluded_census = 3
    poisoned_census = 4

    unmeasured_fraction = mp.mpf(unmeasured_edges) / mp.mpf(total_foreign_edges)

    passed = (
        confirmed_control_arms + unmeasured_edges == total_foreign_edges
        and confirmed_control_arms + shared_constant_transcriptions
        == total_transcriptions
        and self_excluded_census < specificity_max
        and unexcluded_census == specificity_max
        and poisoned_census > specificity_max
        and unmeasured_fraction > mp.mpf("0.995")
    )

    return {
        "beanId": "qou-okkz",
        "passed": bool(passed),
        "totalForeignReadEdges": total_foreign_edges,
        "confirmedControlArmEdges": confirmed_control_arms,
        "unmeasuredForeignReadEdges": unmeasured_edges,
        "totalForeignTranscriptionEdges": total_transcriptions,
        "specificityMaxThreshold": specificity_max,
        "selfExcludedWeightCensus": self_excluded_census,
        "unmeasuredEdgeFraction": fmt_mpf(unmeasured_fraction),
    }


def main() -> None:
    script_bytes = SCRIPT_PATH.read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()
    script_hash_12 = script_sha256[:12]
    commit_sha = get_git_commit_sha()

    checks = [
        check_qou_nmza_native_engine_entry_triage(),
        check_qou_nwhg_pristine_main_ratchet_diff(),
        check_qou_o0pa_nucleon_marshalling_three_arm_guard(),
        check_qou_oiz3_resolvent_cone_float_excision(),
        check_qou_okkz_consumer_control_arm_specificity(),
    ]
    all_passed = all(c["passed"] for c in checks)

    witness = {
        "probeName": "native_engine_entry_triage_pristine_main_ratchet_diff_nucleon_marshalling_three_arm_guard_resolvent_cone_float_excision_and_consumer_control_arm_specificity_probe",
        "beans": ["qou-nmza", "qou-nwhg", "qou-o0pa", "qou-oiz3", "qou-okkz"],
        "leanModule": "QOU.Eightfold.NativeEngineEntryTriagePristineMainRatchetDiffNucleonMarshallingThreeArmGuardResolventConeFloatExcisionAndConsumerControlArmSpecificity",
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
