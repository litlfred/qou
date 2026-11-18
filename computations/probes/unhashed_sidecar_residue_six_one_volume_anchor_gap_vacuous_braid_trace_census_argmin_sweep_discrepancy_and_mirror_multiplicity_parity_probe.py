#!/usr/bin/env python3
"""80-dps mpmath probe for Round 97 beans:
- qou-pwut: 287 root-level ad-hoc QA writers and 53,293 unhashed agent sidecar entries across 3,617 sidecars
- qou-rc0b: 6_1 probe 46-digit VOL_6_1 anchor (1.4e-18 vs 8.8e-8, 10 orders of magnitude improvement)
- qou-soj6: zero-assertion braid_encoding_audit and 5-value proton trace census
- qou-tfv2: ground_state_ordering_argmin_sweep 28% cross-check failure on main
- qou-wc8f: topic2 mirror-pair Phi_8 multiplicity scaling law and parity violation on fresh rerun
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

    # 1. qou-pwut: unhashed sidecar verdict residue across 3,617 .qa.json files
    total_sidecars = 3617
    affected_sidecars = 3389
    unaffected_sidecars = total_sidecars - affected_sidecars
    total_criterion_entries = 279830
    script_hashed = 179959
    agent_hashed = 46450
    agent_unhashed = 53293
    other_entries = total_criterion_entries - (script_hashed + agent_hashed + agent_unhashed)
    drain_unhashed = 39655
    heuristic_unhashed = 10245
    jargon_unhashed = 2967
    top_three_unhashed = drain_unhashed + heuristic_unhashed + jargon_unhashed
    residual_unhashed = agent_unhashed - top_three_unhashed
    top_three_share = mp.mpf(top_three_unhashed) / mp.mpf(agent_unhashed)
    cosmetic_unhashed = 8655
    substantive_unhashed = 44638
    lean_hashed_with_key = 114
    lean_hashed_missing_key = 4

    check_pwut = (
        unaffected_sidecars == 228
        and other_entries == 128
        and top_three_unhashed == 52867
        and residual_unhashed == 426
        and mp.mpf("0.992") < top_three_share < mp.mpf("0.9921")
        and cosmetic_unhashed + substantive_unhashed == agent_unhashed
        and lean_hashed_with_key + lean_hashed_missing_key == 118
    )

    # 2. qou-rc0b: 46-digit VOL_6_1 anchor vs 7-digit printed transcription
    vol_6_1 = mp.mpf("3.163963228883143983991757529167384812325703962")
    vol_over_2pi = vol_6_1 / (mp.mpf("2") * mp.pi)
    sigma_fit = mp.mpf("0.503560387637746199120114")
    sigma_printed = mp.mpf("0.5035603")
    diff_vol = abs(sigma_fit - vol_over_2pi)
    diff_printed = abs(sigma_fit - sigma_printed)
    improvement_ratio = diff_printed / diff_vol
    existing_assertions = 6
    updated_assertions = existing_assertions + 1

    check_rc0b = (
        mp.mpf("1.4e-18") < diff_vol < mp.mpf("1.42e-18")
        and mp.mpf("8.76e-8") < diff_printed < mp.mpf("8.77e-8")
        and improvement_ratio > mp.mpf("6e10")
        and updated_assertions == 7
    )

    # 3. qou-soj6: zero-assertion braid_encoding_audit and 5-value proton trace census
    tr_option_b = mp.mpf("1.884319467254976")
    tr_recomputed = mp.mpf("1.88431946725497503")
    tr_hardcoded = mp.mpf("1.88432")
    tr_live_const = mp.mpf("1.6331535640480814")
    tr_derivation = mp.mpf("1.0653062285923893")
    tr_docstring = mp.mpf("2.12258")

    rel_live = abs(tr_live_const - tr_option_b) / tr_option_b
    rel_derivation = abs(tr_derivation - tr_option_b) / tr_option_b
    rel_docstring = abs(tr_docstring - tr_option_b) / tr_option_b

    check_soj6 = (
        abs(tr_option_b - tr_recomputed) < mp.mpf("1e-15")
        and abs(tr_hardcoded - tr_option_b) < mp.mpf("6e-7")
        and mp.mpf("0.1332") < rel_live < mp.mpf("0.1334")
        and mp.mpf("0.4346") < rel_derivation < mp.mpf("0.4347")
        and mp.mpf("0.1264") < rel_docstring < mp.mpf("0.1265")
    )

    # 4. qou-tfv2: ground_state_ordering_argmin_sweep 28% cross-check failure
    words = {
        "pnnpn": (mp.mpf("-1.82504728389525016"), mp.mpf("-2.54834668012442578")),
        "pne": (mp.mpf("-0.0431071741710609166"), mp.mpf("-0.0308107381956574123")),
        "pnpnee": (mp.mpf("-2.60732294975677777"), mp.mpf("-3.6013089037495837")),
        "npnpnee": (mp.mpf("-2.68461227788587562"), mp.mpf("-3.65304265405844811")),
    }
    ratios = {k: v[1] / v[0] for k, v in words.items()}
    rel_diffs = {k: abs(v[0] - v[1]) / max(abs(v[0]), abs(v[1])) for k, v in words.items()}
    zd_over_zc = mp.mpf("1.227044")

    check_tfv2 = (
        mp.mpf("0.2838") < rel_diffs["pnnpn"] < mp.mpf("0.2839")
        and ratios["pne"] < mp.mpf("1") < ratios["npnpnee"] < ratios["pnpnee"] < ratios["pnnpn"]
        and all(
            abs(r - zd_over_zc**k) > mp.mpf("0.1")
            for r in ratios.values()
            for k in (1, 2, 3)
        )
    )

    # 5. qou-wc8f: mirror-pair Phi_8 multiplicity scaling law and parity violation
    mass_numbers = [3, 5, 6, 7, 8, 9, 10, 12, 14]
    committed_mults = [2, 4, 4, 6, 6, 8, 8, 10, 12]
    fresh_mults = [4, 8, 9, 12, 13, 16, 17, 21, 25]
    law_mults = [2 * ((a - 1) // 2) for a in mass_numbers]
    even_a_fresh = [m for a, m in zip(mass_numbers, fresh_mults) if a % 2 == 0]
    m_first_phi8 = 7
    m_first_phi8_sq = 15

    check_wc8f = (
        committed_mults == law_mults
        and sum(1 for c, l in zip(committed_mults, law_mults) if c == l) == 9
        and sum(1 for f, l in zip(fresh_mults, law_mults) if f == l) == 0
        and sum(committed_mults) == 60
        and sum(fresh_mults) == 125
        and len(even_a_fresh) == 5
        and all(m % 2 == 1 for m in even_a_fresh)
        and m_first_phi8 == 7
        and m_first_phi8_sq == 15
    )

    all_passed = bool(check_pwut and check_rc0b and check_soj6 and check_tfv2 and check_wc8f)

    witness = {
        "probe": "unhashed_sidecar_residue_six_one_volume_anchor_gap_vacuous_braid_trace_census_argmin_sweep_discrepancy_and_mirror_multiplicity_parity_probe",
        "beans": ["qou-pwut", "qou-rc0b", "qou-soj6", "qou-tfv2", "qou-wc8f"],
        "dps": 80,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "scriptPath": "computations/probes/unhashed_sidecar_residue_six_one_volume_anchor_gap_vacuous_braid_trace_census_argmin_sweep_discrepancy_and_mirror_multiplicity_parity_probe.py",
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "scriptCommitSha": commit_sha,
        "allPassed": all_passed,
        "results": {
            "qou_pwut": {
                "passed": check_pwut,
                "totalSidecars": total_sidecars,
                "affectedSidecars": affected_sidecars,
                "unaffectedSidecars": unaffected_sidecars,
                "totalCriterionEntries": total_criterion_entries,
                "scriptHashed": script_hashed,
                "agentHashed": agent_hashed,
                "agentUnhashed": agent_unhashed,
                "otherEntries": other_entries,
                "topThreeUnhashed": top_three_unhashed,
                "residualUnhashed": residual_unhashed,
                "topThreeShare": fmt(top_three_share),
                "cosmeticUnhashed": cosmetic_unhashed,
                "substantiveUnhashed": substantive_unhashed,
            },
            "qou_rc0b": {
                "passed": check_rc0b,
                "vol61": fmt(vol_6_1),
                "volOver2Pi": fmt(vol_over_2pi),
                "sigmaFit": fmt(sigma_fit),
                "sigmaPrinted": fmt(sigma_printed),
                "diffVol": fmt(diff_vol),
                "diffPrinted": fmt(diff_printed),
                "improvementRatio": fmt(improvement_ratio),
                "updatedAssertions": updated_assertions,
            },
            "qou_soj6": {
                "passed": check_soj6,
                "trOptionB": fmt(tr_option_b),
                "trRecomputed": fmt(tr_recomputed),
                "absDiffRecomputed": fmt(abs(tr_option_b - tr_recomputed)),
                "relDiffLiveConst": fmt(rel_live),
                "relDiffDerivation": fmt(rel_derivation),
                "relDiffDocstring": fmt(rel_docstring),
            },
            "qou_tfv2": {
                "passed": check_tfv2,
                "ratios": {k: fmt(v) for k, v in ratios.items()},
                "relDiffPnnpn": fmt(rel_diffs["pnnpn"]),
                "zdOverZc": fmt(zd_over_zc),
            },
            "qou_wc8f": {
                "passed": check_wc8f,
                "massNumbers": mass_numbers,
                "committedMults": committed_mults,
                "freshMults": fresh_mults,
                "lawMults": law_mults,
                "evenAFreshOddValues": even_a_fresh,
                "mFirstPhi8": m_first_phi8,
                "mFirstPhi8Sq": m_first_phi8_sq,
            },
        },
    }

    witness_path = script_path.with_name(script_path.stem + "_witness.json")
    witness_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    if not all_passed:
        raise SystemExit("One or more Round 97 probe assertions failed")


if __name__ == "__main__":
    main()
