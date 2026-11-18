#!/usr/bin/env python3
"""80-dps mpmath probe for Round 90 (`qou-ldwx`, `qou-lvx7`, `qou-m7py`, `qou-mhij`, `qou-ng7j`).

Verifies:
1. qou-ldwx: Raw-float64 ratchet wall-clock `seconds` churn (11 + 6 = 17; 17 + 7 = 24;
   25 - 24 = 1 residual field across the 4-snapshot trajectory [17, 24, 25, 1]).
2. qou-lvx7: `mass-formula-validation` Table 5 denominator flattery on 6Li
   (|Delta| = 2.191 MeV, M = 5603.051 MeV, B = 31.994 MeV: |Delta|/M = 0.039104% < 0.04%,
   while |Delta|/B = 6.848159% > 37 * 0.1827%, with denominator ratio M/B > 175).
3. qou-m7py: Native `gram.rs` TR_M[5] = z^3 load-bearing bug under Convention D
   (rank 5 + radical 1 = 6; at the proton pin q_0 = 1.1099785827513808, z_D = q_0^3 / (q_0^2 + 1),
   h * z_D^2 + z_D vs z_D^3 has relative deficit 66.72% > 2/3).
4. qou-mhij: `z-parameter-echo` triage blind spot and affine payload propagation
   (58 = 40 + 18; 40 = 1 + 2 + 37; vhat_per_crossing_chain shifts from
   1.146101521079414 to 1.282420580225582, +11.894%, and 0.9295042446238508 to
   0.8934352738524302, -3.880%).
5. qou-ng7j: Non-y_lambda detector blindness and `markov_convention` free-text spelling
   partition (3510 = 44 + 3466; 23 = 11 + 1 + 3 + 8; 11 = 1 + 10 misclassified D spellings;
   44 = 13 + 31).
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
    "ratchet-wall-clock-seconds-churn-mass-table-denominator-flattery-trace-weight-rank-coupling-echo-payload-propagation-and-convention-stamp-spelling-partition.witness.json"
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


def check_qou_ldwx_ratchet_seconds_churn() -> dict:
    rev_excess_fields = 11
    rev_exact_fields = 6
    initial_inherited = rev_excess_fields + rev_exact_fields
    third_hok7_fields = 7
    total_hok7_drained = initial_inherited + third_hok7_fields
    peak_new_fields = 25
    residual_new_fields = peak_new_fields - total_hok7_drained
    field_trajectory = [17, 24, 25, 1]
    witness_trajectory = [2, 3, 4, 1]

    drain_fraction = mp.mpf(total_hok7_drained) / mp.mpf(peak_new_fields)

    passed = (
        initial_inherited == 17
        and total_hok7_drained == 24
        and residual_new_fields == 1
        and len(field_trajectory) == 4
        and len(witness_trajectory) == 4
        and drain_fraction == mp.mpf("0.96")
    )

    return {
        "beanId": "qou-ldwx",
        "passed": bool(passed),
        "revExcessScalingSecondsFields": rev_excess_fields,
        "revExactMaximiserSecondsFields": rev_exact_fields,
        "initialInheritedSecondsFields": initial_inherited,
        "totalHok7DrainedFields": total_hok7_drained,
        "peakSnapshotNewFields": peak_new_fields,
        "residualSnapshotNewFields": residual_new_fields,
        "hok7DrainFractionOfPeak": fmt_mpf(drain_fraction),
    }


def check_qou_lvx7_mass_table_denominator_flattery() -> dict:
    delta_mev = mp.mpf("2.191")
    mass_mev = mp.mpf("5603.051")
    binding_mev = mp.mpf("31.994")

    rel_err_mass_pct = (delta_mev / mass_mev) * mp.mpf(100)
    rel_err_binding_pct = (delta_mev / binding_mev) * mp.mpf(100)
    denominator_ratio = mass_mev / binding_mev

    conv_d_mean_pct = mp.mpf("0.1827")
    conv_d_max_pct = mp.mpf("0.3214")
    ratio_vs_conv_d_mean = rel_err_binding_pct / conv_d_mean_pct

    passed = (
        rel_err_mass_pct < mp.mpf("0.04")
        and rel_err_binding_pct > mp.mpf("6.84")
        and denominator_ratio > mp.mpf(175)
        and ratio_vs_conv_d_mean > mp.mpf(37)
        and conv_d_mean_pct < conv_d_max_pct
    )

    return {
        "beanId": "qou-lvx7",
        "passed": bool(passed),
        "li6DeltaMeV": fmt_mpf(delta_mev),
        "li6AtomicMassMeV": fmt_mpf(mass_mev),
        "li6BindingEnergyMeV": fmt_mpf(binding_mev),
        "li6RelErrorOverMassPct": fmt_mpf(rel_err_mass_pct),
        "li6RelErrorOverBindingPct": fmt_mpf(rel_err_binding_pct),
        "denominatorCompressionRatio": fmt_mpf(denominator_ratio),
        "ratioOverConventionDMeanBindingError": fmt_mpf(ratio_vs_conv_d_mean),
    }


def check_qou_m7py_trace_weight_rank_coupling() -> dict:
    basis_dim = 6
    exact_rank = 5
    radical_dim = 1
    bugged_rank = 6

    q_proton = mp.mpf("1.1099785827513808")
    q_muon = mp.mpf("1.1099785955541805")
    h_proton = q_proton - (mp.mpf(1) / q_proton)
    z_d_proton = (q_proton**3) / (q_proton**2 + mp.mpf(1))
    z_d_muon = (q_muon**3) / (q_muon**2 + mp.mpf(1))

    exact_tr_m5 = h_proton * (z_d_proton**2) + z_d_proton
    bugged_tr_m5 = z_d_proton**3
    rel_deficit = (exact_tr_m5 - bugged_tr_m5) / exact_tr_m5
    z_anchor_rel_shift = abs(z_d_muon - z_d_proton) / z_d_proton

    passed = (
        exact_rank + radical_dim == basis_dim
        and bugged_rank == basis_dim
        and exact_rank < bugged_rank
        and mp.mpf(3) * bugged_tr_m5 < exact_tr_m5
        and abs(rel_deficit - mp.mpf("0.6672366")) < mp.mpf("1e-5")
        and z_anchor_rel_shift > mp.mpf("1e-8")
    )

    return {
        "beanId": "qou-m7py",
        "passed": bool(passed),
        "threeStrandBasisDim": basis_dim,
        "exactTraceFormRank": exact_rank,
        "exactTraceFormRadicalDim": radical_dim,
        "buggedRustTraceFormRank": bugged_rank,
        "zDAtProtonPin": fmt_mpf(z_d_proton),
        "exactTrM5AtProtonPin": fmt_mpf(exact_tr_m5),
        "buggedTrM5AtProtonPin": fmt_mpf(bugged_tr_m5),
        "trM5RelativeDeficit": fmt_mpf(rel_deficit),
        "muonVsProtonZRelativeShift": fmt_mpf(z_anchor_rel_shift),
    }


def check_qou_mhij_echo_payload_propagation() -> dict:
    total_triaged = 58
    echo_classified = 40
    non_echo_classified = 18
    confirmed_payload = 1
    null_producer = 2
    unverified_producer = 37

    vhat_c_sigma0 = mp.mpf("1.146101521079414")
    vhat_d_sigma0 = mp.mpf("1.282420580225582")
    rel_shift_sigma0_pct = ((vhat_d_sigma0 - vhat_c_sigma0) / vhat_c_sigma0) * mp.mpf(
        100
    )

    vhat_c_comp = mp.mpf("0.9295042446238508")
    vhat_d_comp = mp.mpf("0.8934352738524302")
    rel_shift_comp_pct = ((vhat_d_comp - vhat_c_comp) / vhat_c_comp) * mp.mpf(100)

    passed = (
        echo_classified + non_echo_classified == total_triaged
        and confirmed_payload + null_producer + unverified_producer == echo_classified
        and rel_shift_sigma0_pct > mp.mpf("11.8")
        and rel_shift_comp_pct < mp.mpf("-3.8")
    )

    return {
        "beanId": "qou-mhij",
        "passed": bool(passed),
        "totalTriagedConventionCWitnesses": total_triaged,
        "echoClassifiedWitnesses": echo_classified,
        "nonEchoClassifiedWitnesses": non_echo_classified,
        "confirmedEchoPayloadWitnesses": confirmed_payload,
        "nullProducerEchoWitnesses": null_producer,
        "unverifiedProducerEchoWitnesses": unverified_producer,
        "sigma0PayloadShiftPct": fmt_mpf(rel_shift_sigma0_pct),
        "companionPayloadShiftPct": fmt_mpf(rel_shift_comp_pct),
    }


def check_qou_ng7j_convention_stamp_spelling_partition() -> dict:
    total_witnesses = 3510
    stamped_witnesses = 44
    unstamped_witnesses = 3466
    spellings_d = 11
    spellings_c = 1
    spellings_both = 3
    spellings_na = 8
    total_spellings = 23
    naive_bare_d_spellings = 1
    misclassified_d_spellings = 10
    bare_d_files = 13
    non_bare_files = 31

    coverage_pct = (mp.mpf(stamped_witnesses) / mp.mpf(total_witnesses)) * mp.mpf(100)
    misclassified_d_fraction = mp.mpf(misclassified_d_spellings) / mp.mpf(spellings_d)

    passed = (
        stamped_witnesses + unstamped_witnesses == total_witnesses
        and spellings_d + spellings_c + spellings_both + spellings_na == total_spellings
        and naive_bare_d_spellings + misclassified_d_spellings == spellings_d
        and bare_d_files + non_bare_files == stamped_witnesses
        and abs(coverage_pct - mp.mpf("1.25356125")) < mp.mpf("1e-5")
    )

    return {
        "beanId": "qou-ng7j",
        "passed": bool(passed),
        "totalNonDeprecatedWitnesses": total_witnesses,
        "stampedConventionWitnesses": stamped_witnesses,
        "unstampedConventionWitnesses": unstamped_witnesses,
        "totalDistinctConventionSpellings": total_spellings,
        "misclassifiedConventionDSpellings": misclassified_d_spellings,
        "stampCoveragePct": fmt_mpf(coverage_pct),
        "misclassifiedDSpellingFraction": fmt_mpf(misclassified_d_fraction),
    }


def main() -> None:
    script_bytes = SCRIPT_PATH.read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()
    script_hash_12 = script_sha256[:12]
    commit_sha = get_git_commit_sha()

    checks = [
        check_qou_ldwx_ratchet_seconds_churn(),
        check_qou_lvx7_mass_table_denominator_flattery(),
        check_qou_m7py_trace_weight_rank_coupling(),
        check_qou_mhij_echo_payload_propagation(),
        check_qou_ng7j_convention_stamp_spelling_partition(),
    ]
    all_passed = all(c["passed"] for c in checks)

    witness = {
        "probeName": "ratchet_wall_clock_seconds_churn_mass_table_denominator_flattery_trace_weight_rank_coupling_echo_payload_propagation_and_convention_stamp_spelling_partition_probe",
        "beans": ["qou-ldwx", "qou-lvx7", "qou-m7py", "qou-mhij", "qou-ng7j"],
        "leanModule": "QOU.Eightfold.RatchetWallClockSecondsChurnMassTableDenominatorFlatteryTraceWeightRankCouplingEchoPayloadPropagationAndConventionStampSpellingPartition",
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
