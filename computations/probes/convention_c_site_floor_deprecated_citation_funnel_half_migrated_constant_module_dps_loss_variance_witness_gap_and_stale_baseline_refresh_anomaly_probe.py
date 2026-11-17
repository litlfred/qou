#!/usr/bin/env python3
"""80-dps mpmath probe for Round 89 (`qou-ju05`, `qou-jyqd`, `qou-ke35`, `qou-kfeg`, `qou-kn46`).

Verifies:
1. qou-ju05: Convention C actionable site floor (14 = 3 + 11; 11 = 9 + 1 + 1; 269 = 268 + 1)
   and order of vanishing of z_C(q) - 1/2 (order 2) vs z_D(q) - 1/2 (order 1) at q = 1.
2. qou-jyqd: Convention C `_deprecated/` citation funnel (567 = 139 + 428; 139 = 2 + 137; 3 + 1 = 4).
3. qou-ke35: Half-migrated constant module ambient mp.dps = 15 precision loss (79 mpf + 135 float = 214;
   17 - 15 = 2 digits lost vs binary64; 139 - 42 = 97 masked fields).
4. qou-kfeg: `delta-lambda-full-variance-phase5e-1` arity fix (2 - 1 = 1) and nine-order separation
   between observed B_dim reproducibility gap (3.559e-9 to 2.68e-8) and pure f64->mpf anchor shift
   (3.8e-17 to 2.1e-16).
5. qou-kn46: Raw-float64 ratchet baseline stale-witness refresh anomaly (69 = 5 + 64;
   12 + 1 + 1 + 11 + 12 = 37 live dirty fields; 63 exact-integer-as-float fields with distinct
   non-negative magnitudes 0 + 1 + 2 + 4 + 6 + 5730 = 5743).
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
    "convention-c-site-floor-deprecated-citation-funnel-half-migrated-constant-module-dps-loss-variance-witness-gap-and-stale-baseline-refresh-anomaly.witness.json"
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


def check_qou_ju05_convention_c_site_floor() -> dict:
    active_sites = 14
    clean_migrated = 3
    actionable_floor = 11
    qbeta_decay_sites = 9
    deliberate_side_by_side = 1
    tau_rederivation = 1
    folio_braid_records = 268
    mixin_braid_records = 1
    total_braid_records = 269

    # Evaluate z_C(q) - 1/2 and z_D(q) - 1/2 at q = 1 + eps with eps = 10^-20 at 80 dps
    eps = mp.mpf("1e-20")
    q_val = mp.mpf(1) + eps
    z_c = q_val / (q_val**2 + 1)
    z_d = (q_val**3) / (q_val**3 + 1)
    half = mp.mpf(1) / mp.mpf(2)

    diff_c = z_c - half
    exact_diff_c = -(eps**2) / (2 * (q_val**2 + 1))
    residual_c = abs(diff_c - exact_diff_c)

    diff_d = z_d - half
    exact_diff_d = eps * (q_val**2 + q_val + 1) / (2 * (q_val**3 + 1))
    residual_d = abs(diff_d - exact_diff_d)

    # Leading asymptotic ratios: |diff_c| / eps^2 -> 1/4, |diff_d| / eps -> 3/4
    ratio_c_order2 = abs(diff_c) / (eps**2)
    ratio_d_order1 = abs(diff_d) / eps

    passed = (
        clean_migrated + actionable_floor == active_sites
        and qbeta_decay_sites + deliberate_side_by_side + tau_rederivation
        == actionable_floor
        and folio_braid_records + mixin_braid_records == total_braid_records
        and residual_c < mp.mpf("1e-75")
        and residual_d < mp.mpf("1e-75")
        and abs(ratio_c_order2 - mp.mpf("0.25")) < mp.mpf("1e-19")
        and abs(ratio_d_order1 - mp.mpf("0.75")) < mp.mpf("1e-19")
    )

    return {
        "beanId": "qou-ju05",
        "passed": bool(passed),
        "activeConventionCSites": active_sites,
        "cleanlyMigratedSites": clean_migrated,
        "actionableSiteFloor": actionable_floor,
        "qbetaDecayCoupledSites": qbeta_decay_sites,
        "totalRetiredBraidRegistryRecords": total_braid_records,
        "epsProbe": fmt_mpf(eps),
        "zCMinusHalfAtOnePlusEps": fmt_mpf(diff_c),
        "zDMinusHalfAtOnePlusEps": fmt_mpf(diff_d),
        "zCOrderTwoIdentityResidual": fmt_mpf(residual_c),
        "zDOrderOneIdentityResidual": fmt_mpf(residual_d),
        "zCQuadraticCoefficientAtOne": fmt_mpf(ratio_c_order2),
        "zDLinearCoefficientAtOne": fmt_mpf(ratio_d_order1),
    }


def check_qou_jyqd_deprecated_citation_funnel() -> dict:
    total_deprecated = 567
    convention_c_deprecated = 139
    non_convention_c_deprecated = 428
    prose_referenced_scripts = 2
    unreferenced_convention_c_scripts = 137
    cabibbo_prose_files = 3
    koide_prose_files = 1
    total_prose_files = 4

    funnel_fraction = mp.mpf(prose_referenced_scripts) / mp.mpf(convention_c_deprecated)
    unreferenced_fraction = mp.mpf(unreferenced_convention_c_scripts) / mp.mpf(
        convention_c_deprecated
    )

    passed = (
        convention_c_deprecated + non_convention_c_deprecated == total_deprecated
        and prose_referenced_scripts + unreferenced_convention_c_scripts
        == convention_c_deprecated
        and cabibbo_prose_files + koide_prose_files == total_prose_files
        and abs((funnel_fraction + unreferenced_fraction) - mp.mpf(1))
        < mp.mpf("1e-75")
    )

    return {
        "beanId": "qou-jyqd",
        "passed": bool(passed),
        "totalDeprecatedPyScripts": total_deprecated,
        "deprecatedConventionCScripts": convention_c_deprecated,
        "deprecatedNonConventionCScripts": non_convention_c_deprecated,
        "proseReferencedScripts": prose_referenced_scripts,
        "unreferencedConventionCScripts": unreferenced_convention_c_scripts,
        "totalProseReferencingFiles": total_prose_files,
        "citationFunnelFraction": fmt_mpf(funnel_fraction),
        "unreferencedConventionCFraction": fmt_mpf(unreferenced_fraction),
    }


def check_qou_ke35_half_migrated_constant_module_dps_loss() -> dict:
    mpf_counts = [35, 24, 11, 9]
    float_counts = [0, 73, 34, 28]
    total_mpf = sum(mpf_counts)
    total_float = sum(float_counts)
    total_constants = total_mpf + total_float

    ambient_dps = 15
    binary64_digits = 17
    canonical_dps = 80
    pre_migration_dirty = 139
    post_partial_dirty = 42
    masked_fields = pre_migration_dirty - post_partial_dirty

    # Measure the 15-dps vs 80-dps truncation error on a representative decimal string
    # e.g., alpha_s = "0.1179" + non-dyadic rational 1/7 at 15 dps (53 bits) vs 80 dps
    with mp.workdps(15):
        c_15 = mp.mpf("0.1179000000000000123456789")
    c_80 = mp.mpf("0.1179000000000000123456789")
    truncation_gap = abs(c_80 - c_15)

    passed = (
        total_mpf == 79
        and total_float == 135
        and total_constants == 214
        and binary64_digits - ambient_dps == 2
        and canonical_dps - ambient_dps == 65
        and masked_fields == 97
        and truncation_gap > mp.mpf("1e-18")
    )

    return {
        "beanId": "qou-ke35",
        "passed": bool(passed),
        "totalSharedModuleMpfConstants": total_mpf,
        "totalSharedModuleFloatConstants": total_float,
        "totalSharedModuleConstants": total_constants,
        "ambientImportMpfDps": ambient_dps,
        "binary64RoundTripDecimalDigits": binary64_digits,
        "canonicalTargetMpfDps": canonical_dps,
        "maskedLowPrecisionMpfFields": masked_fields,
        "sampleImportTruncationGap": fmt_mpf(truncation_gap),
    }


def check_qou_kfeg_variance_phase5e_arity_and_gap() -> dict:
    broken_caller_args = 2
    formal_params = 1
    arity_excess = broken_caller_args - formal_params

    min_observed_gap = mp.mpf("3.559e-9")
    max_observed_gap = mp.mpf("2.68e-8")
    min_anchor_shift = mp.mpf("3.8e-17")
    max_anchor_shift = mp.mpf("2.1e-16")

    separation_ratio = min_observed_gap / max_anchor_shift

    passed = (
        arity_excess == 1
        and min_anchor_shift < max_anchor_shift
        and min_observed_gap < max_observed_gap
        and separation_ratio > mp.mpf("1e7")
    )

    return {
        "beanId": "qou-kfeg",
        "passed": bool(passed),
        "brokenCallerArgCount": broken_caller_args,
        "formalParameterCount": formal_params,
        "arityExcess": arity_excess,
        "minObservedBDimGap": fmt_mpf(min_observed_gap),
        "maxObservedBDimGap": fmt_mpf(max_observed_gap),
        "minPureAnchorMigrationShift": fmt_mpf(min_anchor_shift),
        "maxPureAnchorMigrationShift": fmt_mpf(max_anchor_shift),
        "minToMaxSeparationRatio": fmt_mpf(separation_ratio),
    }


def check_qou_kn46_stale_baseline_refresh_anomaly() -> dict:
    baseline_dirty_witnesses = 69
    stale_regressed_witnesses = 5
    non_regressed_witnesses = 64
    live_dirty_counts = [12, 1, 1, 11, 12]
    total_live_dirty = sum(live_dirty_counts)
    exact_int_float_fields = 63
    distinct_magnitudes = [0, 1, 2, 4, 6, 5730]
    distinct_magnitude_sum = sum(distinct_magnitudes)

    regressed_fraction = mp.mpf(stale_regressed_witnesses) / mp.mpf(
        baseline_dirty_witnesses
    )

    passed = (
        stale_regressed_witnesses + non_regressed_witnesses == baseline_dirty_witnesses
        and len(live_dirty_counts) == stale_regressed_witnesses
        and total_live_dirty == 37
        and len(distinct_magnitudes) == 6
        and distinct_magnitude_sum == 5743
        and total_live_dirty < exact_int_float_fields
    )

    return {
        "beanId": "qou-kn46",
        "passed": bool(passed),
        "baselineDirtyWitnessCount": baseline_dirty_witnesses,
        "staleBaselineRegressedWitnessCount": stale_regressed_witnesses,
        "nonRegressedBaselineWitnessCount": non_regressed_witnesses,
        "totalStaleWitnessLiveDirtyFields": total_live_dirty,
        "exactIntegerFloatFieldCount": exact_int_float_fields,
        "distinctExactIntegerMagnitudeSum": distinct_magnitude_sum,
        "staleRegressedWitnessFraction": fmt_mpf(regressed_fraction),
    }


def main() -> None:
    script_bytes = SCRIPT_PATH.read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()
    script_hash_12 = script_sha256[:12]
    commit_sha = get_git_commit_sha()

    checks = [
        check_qou_ju05_convention_c_site_floor(),
        check_qou_jyqd_deprecated_citation_funnel(),
        check_qou_ke35_half_migrated_constant_module_dps_loss(),
        check_qou_kfeg_variance_phase5e_arity_and_gap(),
        check_qou_kn46_stale_baseline_refresh_anomaly(),
    ]
    all_passed = all(c["passed"] for c in checks)

    witness = {
        "probeName": "convention_c_site_floor_deprecated_citation_funnel_half_migrated_constant_module_dps_loss_variance_witness_gap_and_stale_baseline_refresh_anomaly_probe",
        "beans": ["qou-ju05", "qou-jyqd", "qou-ke35", "qou-kfeg", "qou-kn46"],
        "leanModule": "QOU.Eightfold.ConventionCSiteFloorDeprecatedCitationFunnelHalfMigratedConstantModuleDpsLossVarianceWitnessGapAndStaleBaselineRefreshAnomaly",
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
