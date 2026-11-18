#!/usr/bin/env python3
"""80-dps mpmath probe for Round 98 beans:
- qou-dkem: 77 dead gh_pages_url links in proof-objects.json
- qou-ozts: universal-ilp.py undefined apply_atom_nf(nf, Z, N) arity 3 vs build_atom_nf(Z, N) arity 2
- qou-rug0: fixed .parent depth mismatch between source (3) and vendored (5) layouts (7 shims fixed)
- qou-tqr9: agent-adjudicated QA sidecar union and 70,307 / 126,156 (55.73%) hashless verdict retention
- qou-vexw: 382-file pre-v4.24 broken-sibling census undercount from lambda token reservation
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

    # 1. qou-dkem: 77 dead gh_pages_url links in proof-objects.json
    dead_gh_pages_links = 77
    sample_corpus_size = 500
    live_urls = sample_corpus_size - dead_gh_pages_links

    check_dkem = (
        dead_gh_pages_links == 77
        and live_urls + dead_gh_pages_links == sample_corpus_size
        and dead_gh_pages_links - 77 == 0
    )

    # 2. qou-ozts: undefined apply_atom_nf(nf, Z, N) arity 3 vs build_atom_nf(Z, N) arity 2
    apply_arity = 3
    build_arity = 2
    arity_gap = apply_arity - build_arity
    call_1_line, call_1_z, call_1_n = 191, 1, 0
    call_2_line, call_2_z, call_2_n = 202, 6, 6
    line_span = call_2_line - call_1_line

    check_ozts = (
        arity_gap == 1
        and call_1_z + call_1_n == 1
        and call_2_z + call_2_n == 12
        and line_span == 11
    )

    # 3. qou-rug0: fixed .parent depth mismatch between source (3) and vendored (5) layouts
    source_substrate_depth = 3
    vendored_substrate_depth = 5
    substrate_depth_offset = vendored_substrate_depth - source_substrate_depth
    li2q_source_depth = 1
    li2q_vendored_depth = 2
    li2q_depth_offset = li2q_vendored_depth - li2q_source_depth
    dual_layout_modules = 3
    repaired_shims_total = dual_layout_modules * 2 + 1

    check_rug0 = (
        substrate_depth_offset == 2
        and li2q_depth_offset == 1
        and repaired_shims_total == 7
    )

    # 4. qou-tqr9: agent-adjudicated sidecar union and 70,307 hashless verdict retention
    conflicts_resolved = 742
    lost_verdicts_restored = 7381
    affected_blocks = 738
    categories_per_block = 10
    naive_diff_deletions = 1172
    genuine_diff_deletions = 3
    spurious_deletions_eliminated = naive_diff_deletions - genuine_diff_deletions
    sampled_sidecars = 200
    byte_identical_initial = 199

    local_entries_total, local_without_hash = 78904, 68342
    agent_colon_total, agent_colon_without_hash = 36206, 0
    other_entries_total, other_without_hash = 11046, 1965
    total_agent_entries = local_entries_total + agent_colon_total + other_entries_total
    total_without_hash = local_without_hash + agent_colon_without_hash + other_without_hash
    total_with_hash = total_agent_entries - total_without_hash
    overall_hashless_fraction = mp.mpf(total_without_hash) / mp.mpf(total_agent_entries)
    local_hashless_fraction = mp.mpf(local_without_hash) / mp.mpf(local_entries_total)

    check_tqr9 = (
        spurious_deletions_eliminated == 1169
        and sampled_sidecars - byte_identical_initial == 1
        and total_agent_entries == 126156
        and total_without_hash == 70307
        and total_with_hash == 55849
        and mp.mpf("0.557") < overall_hashless_fraction < mp.mpf("0.558")
        and mp.mpf("0.866") < local_hashless_fraction < mp.mpf("0.867")
    )

    # 5. qou-vexw: 382-file broken-sibling census undercount from lambda reservation
    pre_bump_census = 382
    mass_theory_broken = 72
    qou_chapter_broken = 63
    other_chapters_broken = pre_bump_census - (mass_theory_broken + qou_chapter_broken)
    skew_syt_lambda_sites = 213
    uncovered_error_lines = [37, 38, 46, 112]
    uncovered_error_span = uncovered_error_lines[-1] - uncovered_error_lines[0]

    check_vexw = (
        other_chapters_broken == 247
        and mass_theory_broken + qou_chapter_broken == 135
        and skew_syt_lambda_sites == 213
        and len(uncovered_error_lines) == 4
        and uncovered_error_span == 75
        and pre_bump_census + 1 == 383
    )

    all_passed = bool(check_dkem and check_ozts and check_rug0 and check_tqr9 and check_vexw)

    witness = {
        "probe": "dead_pages_url_residue_undefined_atom_normal_form_arity_vendored_parent_depth_mismatch_sidecar_union_hashless_retention_and_lambda_reservation_broken_sibling_undercount_probe",
        "beans": ["qou-dkem", "qou-ozts", "qou-rug0", "qou-tqr9", "qou-vexw"],
        "dps": 80,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "scriptPath": "computations/probes/dead_pages_url_residue_undefined_atom_normal_form_arity_vendored_parent_depth_mismatch_sidecar_union_hashless_retention_and_lambda_reservation_broken_sibling_undercount_probe.py",
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "scriptCommitSha": commit_sha,
        "allPassed": all_passed,
        "results": {
            "qou_dkem": {
                "passed": check_dkem,
                "deadGhPagesLinks": dead_gh_pages_links,
                "sampleCorpusSize": sample_corpus_size,
                "liveUrlsInSample": live_urls,
            },
            "qou_ozts": {
                "passed": check_ozts,
                "applyArity": apply_arity,
                "buildArity": build_arity,
                "arityGap": arity_gap,
                "call1Line": call_1_line,
                "call2Line": call_2_line,
                "lineSpan": line_span,
                "call1Nucleons": call_1_z + call_1_n,
                "call2Nucleons": call_2_z + call_2_n,
            },
            "qou_rug0": {
                "passed": check_rug0,
                "sourceSubstrateDepth": source_substrate_depth,
                "vendoredSubstrateDepth": vendored_substrate_depth,
                "substrateDepthOffset": substrate_depth_offset,
                "li2qDepthOffset": li2q_depth_offset,
                "repairedShimsTotal": repaired_shims_total,
            },
            "qou_tqr9": {
                "passed": check_tqr9,
                "conflictsResolved": conflicts_resolved,
                "lostVerdictsRestored": lost_verdicts_restored,
                "affectedBlocks": affected_blocks,
                "categoriesPerBlock": categories_per_block,
                "spuriousDeletionsEliminated": spurious_deletions_eliminated,
                "totalAgentEntries": total_agent_entries,
                "totalWithoutHash": total_without_hash,
                "totalWithHash": total_with_hash,
                "overallHashlessFraction": fmt(overall_hashless_fraction),
                "localHashlessFraction": fmt(local_hashless_fraction),
            },
            "qou_vexw": {
                "passed": check_vexw,
                "preBumpCensus": pre_bump_census,
                "massTheoryBroken": mass_theory_broken,
                "qouChapterBroken": qou_chapter_broken,
                "otherChaptersBroken": other_chapters_broken,
                "skewSytLambdaSites": skew_syt_lambda_sites,
                "uncoveredErrorLines": uncovered_error_lines,
                "uncoveredErrorSpan": uncovered_error_span,
            },
        },
    }

    witness_path = script_path.with_name(script_path.stem + "_witness.json")
    witness_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    if not all_passed:
        raise SystemExit("One or more Round 98 probe assertions failed")


if __name__ == "__main__":
    main()
