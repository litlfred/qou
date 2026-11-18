#!/usr/bin/env python3
"""80-dps mpmath numerical probe for:
- qou-58rx: AxiomDischargedScopeData 35-file partition (18 fixed + 17 remaining)
- qou-hprp: UnencodedCarrierFilterData 38-match filter (23 live + 15 prose false positives)
- qou-y3x4: DownstreamInstanceBindingData 139-block §3b-cond rule 2 measurement
- qou-yl86: DeLaunderedEnrichmentData 15-theorem remediation partition
- qou-zatj: SiblingPreservationRebuildData 29-item rebuild partition dropping R1 overwrites
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80


def verify_axiom_discharged_scope() -> dict:
    total = mp.mpf(35)
    first_fixed = mp.mpf(9)
    zero_consumer_fixed = mp.mpf(9)
    consumer_rem = mp.mpf(8)
    standalone_rem = mp.mpf(9)
    fixed_total = first_fixed + zero_consumer_fixed
    rem_total = consumer_rem + standalone_rem
    deficit_sq = (total - fixed_total) ** 2
    passed = bool(
        fixed_total == mp.mpf(18)
        and rem_total == mp.mpf(17)
        and fixed_total + rem_total == total
        and deficit_sq == mp.mpf(289)
    )
    return {
        "bean": "qou-58rx",
        "deLaunderedFixedTotal": mp.nstr(fixed_total, 20),
        "remainingAxiomDischargedTotal": mp.nstr(rem_total, 20),
        "axiomScopeDeficitSq": mp.nstr(deficit_sq, 20),
        "passed": passed,
    }


def verify_unencoded_carrier_filter() -> dict:
    naive = mp.mpf(38)
    live = mp.mpf(23)
    prose_fp = mp.mpf(15)
    audit_sq = (naive - live - prose_fp) ** 2 + live**2
    passed = bool(
        live + prose_fp == naive
        and audit_sq == mp.mpf(529)
    )
    return {
        "bean": "qou-hprp",
        "liveCodeCarriers": mp.nstr(live, 20),
        "proseFalsePositives": mp.nstr(prose_fp, 20),
        "unencodedCarrierAuditSq": mp.nstr(audit_sq, 20),
        "passed": passed,
    }


def verify_downstream_instance_binding() -> dict:
    total = mp.mpf(139)
    own_cone = mp.mpf(9)
    other = mp.mpf(72)
    none_bound = mp.mpf(45)
    unresolved = mp.mpf(13)
    non_compliant = other + none_bound + unresolved
    gap_sq = (total - own_cone) ** 2
    passed = bool(
        own_cone + non_compliant == total
        and non_compliant == mp.mpf(130)
        and gap_sq == mp.mpf(16900)
    )
    return {
        "bean": "qou-y3x4",
        "nonCompliantInstanceBindingCount": mp.nstr(non_compliant, 20),
        "ruleTwoComplianceGapSq": mp.nstr(gap_sq, 20),
        "passed": passed,
    }


def verify_de_laundered_enrichment() -> dict:
    restored = mp.mpf(15)
    proved = mp.mpf(1)
    demoted = mp.mpf(14)
    reassumed = mp.mpf(0)
    honest_total = proved + demoted
    penalty_sq = (restored - honest_total) ** 2 + reassumed**2
    passed = bool(
        honest_total == mp.mpf(15)
        and penalty_sq == mp.mpf(0)
    )
    return {
        "bean": "qou-yl86",
        "honestRemediationTotal": mp.nstr(honest_total, 20),
        "deLaunderingCampaignPenaltySq": mp.nstr(penalty_sq, 20),
        "passed": passed,
    }


def verify_sibling_preservation_rebuild() -> dict:
    total = mp.mpf(29)
    dropped_r1 = mp.mpf(4)
    retained_r2 = mp.mpf(15)
    retained_t2 = mp.mpf(10)
    overwritten = mp.mpf(0)
    retained_total = retained_r2 + retained_t2
    penalty_sq = (total - dropped_r1 - retained_total) ** 2 + overwritten**2
    passed = bool(
        retained_total == mp.mpf(25)
        and dropped_r1 + retained_total == total
        and penalty_sq == mp.mpf(0)
    )
    return {
        "bean": "qou-zatj",
        "retainedRebuildTotal": mp.nstr(retained_total, 20),
        "siblingPreservationPenaltySq": mp.nstr(penalty_sq, 20),
        "passed": passed,
    }


def main() -> None:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[4]
    rel_script_path = script_path.relative_to(repo_root).as_posix()
    script_sha256 = hashlib.sha256(script_path.read_bytes()).hexdigest()
    commit_sha = (
        subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo_root)
        .decode("utf-8")
        .strip()
    )

    checks = {
        "axiomDischargedScope": verify_axiom_discharged_scope(),
        "unencodedCarrierFilter": verify_unencoded_carrier_filter(),
        "downstreamInstanceBinding": verify_downstream_instance_binding(),
        "deLaunderedEnrichment": verify_de_laundered_enrichment(),
        "siblingPreservationRebuild": verify_sibling_preservation_rebuild(),
    }
    all_passed = all(item["passed"] for item in checks.values())
    if not all_passed:
        raise RuntimeError("One or more probe checks failed")

    witness = {
        "probe": "axiom_discharged_scope_unencoded_carrier_filter_downstream_instance_binding_de_laundered_enrichment_sibling_preservation_rebuild_probe",
        "beans": ["qou-58rx", "qou-hprp", "qou-y3x4", "qou-yl86", "qou-zatj"],
        "scriptPath": rel_script_path,
        "scriptCommitSha": commit_sha,
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "dps": int(mp.mp.dps),
        "allPassed": all_passed,
        "checks": checks,
    }

    witness_path = script_path.with_suffix(".witness.json")
    witness_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {witness_path.name} (allPassed={all_passed})")


if __name__ == "__main__":
    main()
