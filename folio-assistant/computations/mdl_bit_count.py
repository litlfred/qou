#!/usr/bin/env python3
# EXPLORATORY (v1-partial) — honest-compression accounting, not a physics
# derivation.  Production-vs-exploratory discipline: this script reads
# existing witnesses + the pre-committed accounting file and emits an
# audit number; it introduces no predictions and wires into no derivation.
#
# Ref: docs/workplans (MDL discussion, 2026-06-10/11 session) and the
#      pre-commitment artifact mdl-accounting.json (same directory).
"""MDL bit-count v1 — "count the bits honestly".

Computes, from per-observable-100x-status.witness.json and the
pre-committed mdl-accounting.json:

  I        = Σ credited bits over non-anchor observables,
             bits_i = log2(prior_rel / max(err_rel, sigma_exp_rel))
  L_cal    = Σ log2(prior_rel / rel_precision_used) over calibrations
  L_choice = Σ log2(alternatives_considered) over counted choices
  C_upper  = I / (L_cal + L_choice)   [UPPER bound: L_framework_core
             is not yet counted — see accounting file]

The Koide calibration of the scale: one relation matched to ~1e-5 against
a comparably-sized formula space gives C ≈ 1, which is why a lone elegant
match stays "intriguing" for decades.  Evidence of real structure
requires C >> 1 under a pre-committed accounting.

Outputs `mdl-bit-count.witness.json`.
"""
from __future__ import annotations

import _path_bridge as _pb  # noqa: F401, E402 — substrate module bridge
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def main() -> int:
    accounting = json.loads((HERE / "mdl-accounting.json").read_text())
    dash = json.loads(
        (HERE / "per-observable-100x-status.witness.json").read_text()
    )

    prior_rel = 1e4  # uniform 4-decade convention (see accounting file)

    rows_out = []
    I_total = 0.0
    for row in dash["data"]["rows"]:
        role = row.get("role", "")
        err_rel = float(row["err_ppb"]) * 1e-9
        sig_rel = float(row["sigma_exp_ppb"]) * 1e-9
        floor = max(err_rel, sig_rel)
        is_anchor = ("anchor" in role.lower()) or ("cal" in role.lower())
        bits = 0.0 if is_anchor else math.log2(prior_rel / floor)
        if not is_anchor:
            I_total += bits
        rows_out.append({
            "obs": row["obs"],
            "role": role,
            "err_ppb": row["err_ppb"],
            "sigma_exp_ppb": row["sigma_exp_ppb"],
            "credited": not is_anchor,
            "bits": round(bits, 2),
        })

    L_cal = 0.0
    cal_out = []
    for c in accounting["L_calibrations"]:
        if c.get("bits_rule") == "0":
            bits = 0.0
        else:
            bits = math.log2(prior_rel / float(c["rel_precision_used"]))
        L_cal += bits
        cal_out.append({"name": c["name"], "bits": round(bits, 2)})

    L_choice = 0.0
    choice_out = []
    for ch in accounting["L_structural_choices"]:
        bits = math.log2(float(ch["alternatives_considered"]))
        counted = ch.get("status") != "pending"
        if counted:
            L_choice += bits
        choice_out.append({
            "name": ch["name"],
            "bits": round(bits, 2),
            "counted": counted,
            "status": ch.get("status", "counted"),
        })

    L_known = L_cal + L_choice
    C_upper = I_total / L_known if L_known > 0 else float("inf")
    band = 3.32 * sum(1 for r in rows_out if r["credited"])  # ±1 decade

    print("=" * 74)
    print(" MDL bit-count v1 — honest-compression accounting (UPPER bound)")
    print("=" * 74)
    print(f"\n {'obs':>10} {'role':<24} {'bits':>8}  credited")
    for r in rows_out:
        print(f" {r['obs']:>10} {r['role'][:24]:<24} {r['bits']:>8}  {r['credited']}")
    print(f"\n  I (credited information)            = {I_total:8.1f} bits")
    print(f"  L_calibrations                      = {L_cal:8.1f} bits")
    print(f"  L_structural_choices (counted only) = {L_choice:8.1f} bits")
    print(f"  C_upper = I / L_known               = {C_upper:8.2f}")
    print(f"  prior sensitivity (±1 decade)       = ±{band:.0f} bits on I")
    print("\n  CAVEAT: L_framework_core is NOT yet counted (v1) — C is an")
    print("  upper bound. Koide-scale reference: C ≈ 1.")

    from witness_base import WitnessBuilder
    builder = WitnessBuilder.wrap_legacy(
        "mdl-bit-count",
        {
            "description": (
                "EXPLORATORY v1-partial MDL accounting: information credit "
                "over the non-anchor rows of the 100x dashboard against the "
                "pre-committed 4-decade prior (mdl-accounting.json), charged "
                "against calibration precisions + counted structural "
                "choices.  C is an UPPER bound until L_framework_core is "
                "counted.  MDL credit is distinct from the L2 100x targets: "
                "a 210-ppb match still compresses."
            ),
            "exploratory": True,
            "accounting_file": "mdl-accounting.json",
            "data": {
                "prior_rel": prior_rel,
                "observables": rows_out,
                "L_calibrations": cal_out,
                "L_structural_choices": choice_out,
                "I_total_bits": round(I_total, 2),
                "L_cal_bits": round(L_cal, 2),
                "L_choice_bits_counted": round(L_choice, 2),
                "C_upper_bound": round(C_upper, 3),
                "prior_sensitivity_bits_per_decade": round(band, 1),
                "koide_reference": "C ≈ 1 for a lone elegant relation",
            },
        },
        script_path=__file__,
        engine="python",
    )
    out_path = builder.save()
    print(f"\n  Wrote {Path(out_path).name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
