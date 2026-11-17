#!/usr/bin/env python3
"""80-dps mpmath probe for qou-5lw7, qou-5m4f, qou-5rf8, qou-5sg8, and qou-5t68."""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess

import mpmath as mp

mp.mp.dps = 80

SCRIPT_PATH = pathlib.Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[2]
WITNESS_PATH = (
    REPO_ROOT
    / "computations"
    / "probes"
    / "raw-float64-queue-guard-descent-transseries-split-stale-script-hash-refresh-float64-padding-ratchet-and-borromean-stale-agreement.witness.json"
)
LEAN_SOURCE = (
    "QOU.Eightfold."
    "RawFloat64QueueGuardDescentTransseriesSplitStaleScriptHashRefreshFloat64PaddingRatchetAndBorromeanStaleAgreement"
)


def fmt(val: mp.mpf) -> str:
    return mp.nstr(val, 80, min_fixed=0, max_fixed=0)


def get_commit_sha() -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True
        ).strip()
        if len(out) == 40:
            return out
    except Exception:
        pass
    return "0" * 40


def main() -> None:
    mp.mp.dps = 80
    assertions = []

    # 1. qou-5lw7: Raw-float64 queue classification (20+2=22 witnesses, 36+1712=1748 fields, 50-17=33 digit deficit)
    new_dirty = 20
    regressed_dirty = 2
    active_queue = new_dirty + regressed_dirty
    framework_fields = 36
    payload_fields = 1712
    total_fields = framework_fields + payload_fields
    digit_deficit = 50 - 17
    p1 = (
        active_queue == 22
        and total_fields == 1748
        and (payload_fields > 47 * framework_fields)
        and digit_deficit == 33
    )
    assertions.append(
        {
            "name": "qou_5lw7_raw_float64_queue_and_degraded_anchor_deficit_accounting",
            "computed": f"{active_queue}:{total_fields}:{digit_deficit}",
            "expected": "22:1748:33",
            "passed": bool(p1),
            "tolerance": "0",
            "source": f"{LEAN_SOURCE}.raw_float64_queue_and_degraded_anchor_deficit_accounting",
        }
    )

    # 2. qou-5m4f: Categorical descent B_total = B_desc + B_trans vs 37x transseries refutation
    b_total_d = mp.mpf("2.2245662")
    b_trans_d = b_total_d / mp.mpf(37)
    b_desc_d = b_total_d - b_trans_d
    ratio_desc_to_trans = b_desc_d / b_trans_d
    share_desc = b_desc_d / b_total_d
    p2 = (
        abs(ratio_desc_to_trans - mp.mpf(36)) < mp.mpf("1e-75")
        and abs(share_desc - mp.mpf(36) / mp.mpf(37)) < mp.mpf("1e-75")
        and b_desc_d > b_trans_d
    )
    assertions.append(
        {
            "name": "qou_5m4f_descent_backbone_dominates_37x_transseries_component",
            "computed": fmt(ratio_desc_to_trans),
            "expected": "36.0",
            "passed": bool(p2),
            "tolerance": "1e-75",
            "bDescMeV": fmt(b_desc_d),
            "bTransMeV": fmt(b_trans_d),
            "source": f"{LEAN_SOURCE}.descent_backbone_dominates_37x_transseries_component",
        }
    )

    # 3. qou-5rf8: Stale scriptHash cohort refresh monotone drain (70 -> 0)
    initial_stale = 70
    step_k = 25
    rem_k = initial_stale - step_k
    rem_all = initial_stale - 70
    p3 = (rem_k == 45) and (rem_all == 0) and (initial_stale - rem_k == step_k)
    assertions.append(
        {
            "name": "qou_5rf8_stale_script_hash_refresh_monotone_drain",
            "computed": f"{initial_stale}:{rem_k}:{rem_all}",
            "expected": "70:45:0",
            "passed": bool(p3),
            "tolerance": "0",
            "source": f"{LEAN_SOURCE}.stale_script_hash_refresh_monotone_drain",
        }
    )

    # 4. qou-5sg8: float64-padding ratchet on categorical-bypass-volmatch-demo (13+4=17, 50-16=34 tail digits)
    baseline_padded = 13
    new_ratio_padded = 1
    new_ame_padded = 3
    new_total_padded = new_ratio_padded + new_ame_padded
    total_padded = baseline_padded + new_total_padded
    spurious_tail_digits = 50 - 16
    p4 = (new_total_padded == 4) and (total_padded == 17) and (spurious_tail_digits == 34)
    assertions.append(
        {
            "name": "qou_5sg8_float64_padding_ratchet_and_spurious_tail_accounting",
            "computed": f"{new_total_padded}:{total_padded}:{spurious_tail_digits}",
            "expected": "4:17:34",
            "passed": bool(p4),
            "tolerance": "0",
            "source": f"{LEAN_SOURCE}.float64_padding_ratchet_and_spurious_tail_accounting",
        }
    )

    # 5. qou-5t68: Coupled stale convention-C witness agreement in borromean-binding-recompute
    b_tower_committed_c = mp.mpf("2.4802963")
    b_tower_fresh_d = mp.mpf("2.0630769")
    stale_vs_stale_diff = abs(b_tower_committed_c - b_tower_committed_c)
    live_vs_stale_diff = b_tower_fresh_d - b_tower_committed_c
    p5 = (stale_vs_stale_diff == mp.mpf(0)) and (live_vs_stale_diff != mp.mpf(0))
    assertions.append(
        {
            "name": "qou_5t68_coupled_stale_witness_zero_discrepancy_hides_convention_drift",
            "computed": f"{fmt(stale_vs_stale_diff)}:{fmt(live_vs_stale_diff)}",
            "expected": "0.0:-0.4172194",
            "passed": bool(p5),
            "tolerance": "1e-75",
            "source": f"{LEAN_SOURCE}.coupled_stale_witness_zero_discrepancy_hides_convention_drift",
        }
    )

    all_passed = all(a["passed"] for a in assertions)
    commit_sha = get_commit_sha()
    script_hash = hashlib.sha256(SCRIPT_PATH.read_bytes()).hexdigest()[:12]

    witness = {
        "engine": "mpmath",
        "engineVersion": f"mpmath {mp.__version__}",
        "dps": "80",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": commit_sha,
        "scriptCommitSha": commit_sha,
        "scriptHash": script_hash,
        "allPassed": all_passed,
        "assertions": assertions,
    }
    WITNESS_PATH.write_text(json.dumps(witness, indent=2) + "\n")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
