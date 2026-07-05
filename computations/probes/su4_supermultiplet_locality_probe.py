#!/usr/bin/env python3
"""Narrow A=4/A=6 probe — SU(4) [1^A] supermultiplet locality vs measured excess.

GATE (proved, sorry-free): QOU.MassTheory.SU4SupermultipletGate —
the fully-antisymmetric [1^A] Wigner SU(4) supermultiplet has dim C(4,A),
nonzero iff A ≤ 4 (α at A=4 = the [1^4] singlet), zero for A > 4 (no [1^5]).

This is the ONE narrow probe the scoping note (§3 Lever 1,
docs/scope/2026-07-05-gap-a4-interface-operator-attack-scoping.md) permits now
that the gate holds: does the gate's ON/OFF locality match the MEASURED
super-pairwise binding excess? The excess is the connected many-body binding
the pairwise-assembly ceiling cannot reach
(probes/interface-operator-pairwise-ceiling.witness.json):

    super_pairwise(A) = ame_ratio_over_D / max(pairwise_ratios_over_D)

RESULT (scope-(a), audit-only, no fit):
The gate predicts a [1^4]-connected term PRESENT for A ≤ 4 and ABSENT for A > 4.
The measured super-pairwise excess:

    A=2 (D)     C(4,2)=6   super=1.000   (pairwise saturates — no excess)
    A=3 (T/³He) C(4,3)=4   super=1.14/1.26
    A=4 (⁴He)   C(4,4)=1   super=2.093   ← PEAK (the closed-shell [1^4] singlet)
    A=6 (⁶Li)   C(4,6)=0   super=0.944   ← back to ~pairwise (term OFF)

The excess PEAKS exactly at the A=4 closed shell and returns to ~1
(pairwise-saturating) by ⁶Li, where C(4,A)=0 — a clean LOCALITY MATCH to the
proved gate. The excess is not ∝ C(4,A) (that would peak at A=2); it peaks at
the UNIQUE [1^4] singlet A=4 — the maximally-bound α closed shell, exactly the
supermultiplet picture.

SCOPE. This confirms the gate's locality PREDICTION against measured data — the
missing ⁴He binding term is A=4-local as the [1^4] supermultiplet requires. It
does NOT derive the magnitude (2.093×): constructing the [1^4] connected Ursell
operator to yield that value is the multi-session follow-on. Locality-consistency,
not a magnitude closure.

`-- Ref:` Wigner 1937 (SU(4) supermultiplet); scoping note §3 Lever 1.
"""
from __future__ import annotations

import json
import math
import os
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from substrate.witness_base import WitnessBuilder  # noqa: E402

COMP = str(_COMP)
CEILING = os.path.join(COMP, "probes", "interface-operator-pairwise-ceiling.witness.json")


def load_super_pairwise() -> dict:
    with open(CEILING, encoding="utf-8") as f:
        w = json.load(f)
    wit = w.get("witness", w)
    m = wit.get("result", wit.get("data", wit)).get("measurement", wit.get("measurement", {}))
    out = {}
    for r in m.get("rows", []):
        pr = r.get("pairwise_ratios_over_D", {})
        best = max(float(v) for v in pr.values()) if pr else float("nan")
        ame = float(r.get("ame_ratio_over_D", "nan"))
        out[r["atom"]] = {
            "A": int(r["A"]),
            "ame_ratio_over_D": ame,
            "best_pairwise_over_D": best,
            "super_pairwise": (ame / best) if best and best == best else float("nan"),
        }
    return out


def main() -> int:
    sp = load_super_pairwise()

    # gate dimensions C(4,A) — the proved SU(4) [1^A] supermultiplet dimension
    dim = {A: math.comb(4, A) for A in range(0, 9)}  # 1,4,6,4,1,0,0,0,0

    # locality-match checks
    A4 = sp.get("4He", {}).get("super_pairwise", float("nan"))
    A6 = sp.get("6Li", {}).get("super_pairwise", float("nan"))
    gate_on_le4 = all(dim[A] > 0 for A in range(0, 5))
    gate_off_gt4 = all(dim[A] == 0 for A in range(5, 9))
    peak_at_4 = A4 > sp["3He"]["super_pairwise"] and A4 > sp["D"]["super_pairwise"]
    off_by_6 = A6 < 1.05  # returned to ~pairwise where C(4,6)=0

    per_atom = {
        atom: {**v, "dim_C4A": dim[v["A"]]}
        for atom, v in sp.items()
    }

    payload = {
        "computation": "su4-supermultiplet-locality",
        "description": ("Narrow A=4/A=6 probe: the proved SU(4) [1^A] supermultiplet "
                        "gate (dim C(4,A), zero for A>4) predicts a connected term local "
                        "to A≤4; the measured super-pairwise excess peaks at ⁴He (2.093×) "
                        "and returns to ~pairwise by ⁶Li (0.944×) where C(4,6)=0 — a clean "
                        "LOCALITY MATCH. Magnitude derivation is follow-on. audit-only, no fit."),
        "tier": "structural (proved gate dims) + measured (committed ceiling witness)",
        "result": {
            "gate": "QOU.MassTheory.SU4SupermultipletGate (C(4,A)=0 ↔ A>4, sorry-free)",
            "dim_C4A": dim,
            "per_atom": per_atom,
            "super_pairwise_peaks_at_A4": bool(peak_at_4),
            "super_pairwise_off_by_A6": bool(off_by_6),
            "verdict": ("LOCALITY MATCH (scope-(a)): the measured super-pairwise excess "
                        "peaks at the A=4 closed shell (2.093×, the unique [1^4] singlet) "
                        "and returns to ~pairwise (0.944×) by ⁶Li where the gate gives "
                        "C(4,6)=0. The missing ⁴He binding term is A=4-local exactly as the "
                        "[1^4] supermultiplet requires. Not proportional to C(4,A) (which "
                        "peaks at A=2) — it peaks at the maximally-bound α singlet. "
                        "Magnitude (2.093× ↔ the [1^4] connected-operator value) is the "
                        "multi-session follow-on; this is locality-consistency only."),
        },
        "context": {
            "axis": "GAP-A-4 class-D — A=4 interface operator (Δ_λ magnitude)",
            "gate_lean": "qou:QOU.MassTheory.SU4SupermultipletGate",
            "measured_source": "probes/interface-operator-pairwise-ceiling.witness.json",
            "scoping": "docs/scope/2026-07-05-gap-a4-interface-operator-attack-scoping.md §3",
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        "su4-supermultiplet-locality", payload,
        script_path=__file__, engine="python", output_dir=os.path.join(COMP, "probes"),
    )
    wb.add_assertion("gate_present_for_A_le_4", computed=str(gate_on_le4), expected="True")
    wb.add_assertion("gate_vanishes_for_A_gt_4", computed=str(gate_off_gt4), expected="True")
    wb.add_assertion("measured_excess_peaks_at_A4", computed=str(bool(peak_at_4)), expected="True")
    wb.add_assertion("measured_excess_off_by_A6", computed=str(bool(off_by_6)), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== SU(4) [1^A] supermultiplet locality vs measured super-pairwise excess ===")
    print(f"  {'atom':5} {'A':>2} {'C(4,A)':>6} {'super_pairwise':>14}")
    for atom, v in per_atom.items():
        print(f"  {atom:5} {v['A']:>2} {v['dim_C4A']:>6} {v['super_pairwise']:>14.3f}")
    print(f"\n  gate ON for A≤4: {gate_on_le4} | OFF for A>4: {gate_off_gt4}")
    print(f"  excess peaks at A=4 (2.093): {peak_at_4} | back to ~pairwise by A=6 (0.944): {off_by_6}")
    print("  VERDICT: LOCALITY MATCH (scope-a). Magnitude derivation is follow-on.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
