#!/usr/bin/env python3
"""Family-4 motivic-substrate probe — atom-knot ID scaffold.

Continues `docs/audits/family-4-motivic-path.md`.

For each family-4 atom (⁶Li, ⁷Li, ⁹Be, ¹¹B, ¹⁴N, ¹⁹F):

  1. Load the parent ground-state braid from `braid-registry/<sym>.json`.
  2. Record a q-MN character placeholder (`pending-convention-pin`)
     until the q-MN convention is pinned to the canonical Markov-trace
     conventions used elsewhere.
  3. Emit a witness row with status `motivic-pending-orbit-table`.

This script does NOT assign knot IDs — it cannot, until the
K_motivic orbit table is generated (blocker #3 in the audit).  The
output is an honest categorical state:

  - parent braid present?         → registry lookup succeeded
  - q-MN character status?        → `pending-convention-pin`
                                    (step 2 not yet implemented)
  - knot id?                      → null until orbit table lands

Output: `family-4-motivic-probe.witness.json`
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

# Family-4 symbols and their braid-registry filenames.
FAMILY_4 = [
    ("6Li",  "li-6.json"),
    ("7Li",  "li-7.json"),
    ("9Be",  "be-9.json"),
    ("11B",  "b-11.json"),
    ("14N",  "n-14.json"),
    ("19F",  "f-19.json"),
]

REGISTRY_DIR = Path(__file__).parent / "braid-registry"
OUT_PATH = Path(__file__).parent / "family-4-motivic-probe.witness.json"


def load_parent_braid(filename: str) -> dict | None:
    """Read the parent-braid block from a registry entry, or None if missing."""
    path = REGISTRY_DIR / filename
    if not path.exists():
        return None
    try:
        d = json.loads(path.read_text())
    except json.JSONDecodeError:
        return None
    parent = d.get("parent")
    if parent is None:
        return None
    return {
        "ordering":          parent.get("ordering"),
        "log_trace":         parent.get("log_trace"),
        "trace_numerical":   parent.get("trace_numerical"),
        "ground_state_method": parent.get("ground_state_method"),
        "n_orderings_searched": parent.get("n_orderings_searched"),
    }


def probe_one(sym: str, filename: str) -> dict:
    """Run the four-step probe for one atom (steps 3 + 4 are pending)."""
    parent = load_parent_braid(filename)
    row = {
        "sym": sym,
        "registry_file": filename,
        "step_1_ground_state_braid": (
            "present" if parent is not None else "missing"
        ),
        "step_2_q_mn_character": "pending-convention-pin",  # GAP 5a
        "step_3_motivic_galois_orbit": "pending-realization",  # GAP 5b
        "step_4_knot_id": "pending-orbit-table",  # GAP 5c
        "bucket": "motivic",
        "status": "motivic-pending-orbit-table",
    }
    if parent is not None:
        row["parent_braid"] = parent
    return row


def main():
    rows = [probe_one(sym, fn) for sym, fn in FAMILY_4]

    witness = {
        "computation": "family-4-motivic-probe",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Honest categorical state of family-4 atom-knot ID under "
            "the motivic-substrate framework (post PR #455). For each "
            "of {⁶Li, ⁷Li, ⁹Be, ¹¹B, ¹⁴N, ¹⁹F}, reports which of the "
            "four steps in `docs/audits/family-4-motivic-path.md` is "
            "currently passable. No fits, no derived knot IDs — those "
            "wait for the K_motivic orbit table (audit blocker #3)."
        ),
        "design_spec": "docs/audits/family-4-motivic-path.md",
        "consumed_by": "mass-table-ppb (eventually, post-blockers)",
        "atoms": rows,
        "summary": {
            "n_atoms": len(rows),
            "with_parent_braid": sum(
                1 for r in rows
                if r["step_1_ground_state_braid"] == "present"
            ),
            "blockers_referenced": ["GAP 5a", "GAP 5b", "GAP 5c"],
        },
    }

    OUT_PATH.write_text(json.dumps(witness, indent=2, ensure_ascii=False))
    print(f"Wrote {OUT_PATH}")

    # Human-readable summary
    print()
    print("Family-4 motivic-substrate probe")
    print("-" * 64)
    print(f"{'sym':<5} {'registry':<14} step1 step2 step3 step4")
    print("-" * 64)
    short = {
        "present": "✓",
        "missing": "✗",
        "pending-convention-pin":  "·",
        "pending-realization":     "·",
        "pending-orbit-table":     "·",
    }
    for r in rows:
        print(
            f"{r['sym']:<5} {r['registry_file']:<14} "
            f"  {short[r['step_1_ground_state_braid']]}  "
            f"  {short[r['step_2_q_mn_character']]}  "
            f"  {short[r['step_3_motivic_galois_orbit']]}  "
            f"  {short[r['step_4_knot_id']]}"
        )
    print()
    print("Legend: ✓ present, ✗ missing, · pending blocker (see audit doc)")


if __name__ == "__main__":
    main()
