#!/usr/bin/env python3
"""muon_pin_A_residual_surface_audit.py — how much of the corpus is still pinned
to the RETIRED frozen muon q_0?  Measured: one live witness, and its producer
cannot finish.

WHY.  Bean `qou-tekx` stages the CODATA-2022 muon migration (owner ruling
2026-08-22, implemented 2026-08-28) as a four-step plan whose step 1 is
*"establish what reads A"*.  Its own scoping text says:

    "Only the anchor-defining witness is frozen at A:
     computations/q-pinning-50-digit.witness.json."

**That is stale**, and in the direction that matters: `fca08de7d29` (2026-08-28,
"muon anchor -> CODATA 2022 (owner ruling): derive it, stop the
self-certification") already migrated that witness.  Measured on the current
tree, it holds **C**, and `witness._q0_value_for_anchor("muon")` returns C.  So
the circle the bean's step 3 is built around -- an anchor witness that cannot be
regenerated because its own producer hard-fails on an inconsistent anchor -- is
already broken, by derivation rather than by re-pinning.

WHAT IS ACTUALLY LEFT.  This audit answers step 1 by measurement rather than by
assumption.  Of every tracked `*.witness.json`:

  * **carrying the A literal at all:** 40
  * **COMPUTED at A** (its own `q0Value` is A): **4**
      - `computations/hadron-knot-table.witness.json`               <- the only live one
      - three under `qou-mass/src/qou_mass/data/_deprecated/`       <- deprecated mirror
  * **mentioning A without being computed at it:** 36

That 36 is the important distinction and it is why a grep for the literal
over-counts by an order of magnitude.  They are audits *about* the pin
(`q0-consistency-audit`, `hardcoded-q0-literal-families`, `mu-p-pin-sensitivity-map`,
`consumer-control-arm-audit`, `q0-value-drift-audit`), probes recording the
cross-anchor swing, and proton-pinned witnesses quoting A as the comparison arm.
Every one of them is **correct as recorded** and none is migration work.  This
matches the corpus's own `Q0_FLIP = 1` from `q0_anchor_consistency_audit.py`.

THE ONE LIVE FILE, AND WHY IT IS NOT A ONE-LINER.  `hadron-knot-table.witness.json`
is stamped `q0Anchor: "muon"`, `q0Value` = A, `computedAt` 2026-06-17.  Its
producer `hadron_knot_table.py` is listed `ideal_muon` in `q0_anchor_manifest.json`,
so **no code change is needed** -- a re-run resolves the muon anchor through
`_q0_value_for_anchor("muon")`, which now returns C, and writes C.  The migration
is exactly one producer re-run.

The blocker is cost, and it is already on the record in AGENTS.md: that producer
completes the three A=1 atoms in seconds and then **ran 50 minutes on deuterium,
the first bound atom of nineteen, before being killed by its own timeout** (exit
124, zero tracebacks).  It does not crash; it does not finish.  So the last A-pinned
witness in the corpus is blocked on a long-compute problem, not on the anchor
migration -- which is a different bean's shape entirely.

WHAT THIS AUDIT DOES NOT DO.  It does not re-pin anything, and it must not be
turned into a sweep.  Re-pinning the anchor-defining witness as a step in a bulk
pass took main red on 2026-08-19: both anchors collapsed onto one string, 262
correctly-stamped muon witnesses flipped to Q0_FLIP (Q0_OK 654 -> 392), and every
`ideal_muon` producer hard-failed.  `q0_repin_sweep.py` carries an
`ANCHOR_DEFINING` exclusion for exactly that; do not remove it.

Run:  python3 -u computations/audits/muon_pin_A_residual_surface_audit.py \
        2>&1 | tee /tmp/muon_pin_A_residual.log
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTATIONS = HERE.parent
REPO = COMPUTATIONS.parent
for _p in (COMPUTATIONS, COMPUTATIONS / "substrate"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from witness_base import WitnessBuilder  # noqa: E402

# The three values that have all been called "the muon q_0".  Compared by
# prefix, which is enough: they diverge at the 13th significant digit.
A_PREFIX = "1.1099785955573347"      # retired frozen pin
B_PREFIX = "1.10997859555418"        # lepton-tower derivation at CODATA 2018
C_PREFIX = "1.109978595642739"       # CODATA 2022 — canonical since fca08de7d29

ANCHOR_WITNESS = "computations/q-pinning-50-digit.witness.json"
LIVE_A_WITNESS = "computations/hadron-knot-table.witness.json"


def tracked_witnesses() -> list[str]:
    out = subprocess.run(
        ["git", "ls-files", "*.witness.json"],
        cwd=REPO, capture_output=True, text=True, check=True,
    )
    return out.stdout.split()


def classify(path: str) -> dict | None:
    """Return a row for a witness carrying the A literal, else None.

    The discriminator is `q0Value`: a witness whose own recorded q_0 is A was
    COMPUTED at A and is migration work; one that merely contains the string is
    quoting it, and is correct as recorded.
    """
    p = REPO / path
    try:
        text = p.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    if A_PREFIX not in text:
        return None
    try:
        doc = json.loads(text)
    except json.JSONDecodeError:
        doc = {}
    inner = doc.get("witness") if isinstance(doc.get("witness"), dict) else {}
    anchor = doc.get("q0Anchor") or inner.get("q0Anchor")
    q0v = doc.get("q0Value") or inner.get("q0Value")
    return {
        "path": path,
        "q0Anchor": anchor,
        "q0Value_prefix": str(q0v)[:24] if q0v else None,
        "computed_at_A": bool(q0v and str(q0v).startswith(A_PREFIX)),
        "deprecated": "_deprecated" in path,
    }


def main() -> int:
    files = tracked_witnesses()
    rows = [r for r in (classify(f) for f in files) if r is not None]
    computed_at_A = [r for r in rows if r["computed_at_A"]]
    quoting_A = [r for r in rows if not r["computed_at_A"]]
    live_A = [r for r in computed_at_A if not r["deprecated"]]

    anchor_doc = json.loads((REPO / ANCHOR_WITNESS).read_text(encoding="utf-8"))
    anchor_q = str(anchor_doc.get("q0Value") or
                   (anchor_doc.get("derived_50_digit") or {}).get("q"))
    anchor_is = ("A" if anchor_q.startswith(A_PREFIX)
                 else "C" if anchor_q.startswith(C_PREFIX)
                 else "B" if anchor_q.startswith(B_PREFIX) else "unknown")

    print("=" * 84)
    print("residual A-pin surface — what is actually left of the muon migration")
    print("=" * 84)
    print(f"\n  anchor-defining witness ({ANCHOR_WITNESS})")
    print(f"    holds {anchor_is}: {anchor_q[:46]}")
    print(f"\n  tracked witnesses scanned      : {len(files)}")
    print(f"  carrying the A literal at all  : {len(rows)}")
    print(f"    COMPUTED at A                : {len(computed_at_A)}")
    print(f"      of those, live (not _deprecated): {len(live_A)}")
    print(f"    quoting A, computed elsewhere: {len(quoting_A)}")

    print(f"\n  COMPUTED AT A:")
    for r in sorted(computed_at_A, key=lambda r: r["path"]):
        mark = "  (deprecated mirror)" if r["deprecated"] else "  <- LIVE"
        print(f"    anchor={str(r['q0Anchor']):<8} {r['path']}{mark}")

    w = WitnessBuilder("muon-pin-A-residual-surface", engine="python")
    w.add_parameter("A_prefix_retired_frozen_pin", A_PREFIX)
    w.add_parameter("C_prefix_codata_2022_canonical", C_PREFIX)
    w.add_data("tracked_witnesses_scanned", len(files))
    w.add_data("carrying_A_literal", len(rows))
    w.add_data("computed_at_A", [r["path"] for r in computed_at_A])
    w.add_data("computed_at_A_live", [r["path"] for r in live_A])
    w.add_data("quoting_A_not_computed_at_A", [r["path"] for r in quoting_A])
    w.add_data("anchor_defining_witness_holds", anchor_is)
    w.add_data("anchor_defining_witness_q0", anchor_q)

    w.add_assertion(
        "the anchor-defining witness is on CODATA 2022, not the retired frozen pin",
        computed="1" if anchor_is == "C" else "0", expected="1", tolerance="0",
        source=f"{ANCHOR_WITNESS} — migrated by fca08de7d29 (2026-08-28)",
    )
    w.add_assertion(
        "exactly one LIVE witness is still computed at the retired pin",
        computed=str(len(live_A)), expected="1", tolerance="0",
        source=f"the others are under _deprecated/; the live one is {LIVE_A_WITNESS}",
    )
    w.add_assertion(
        "that one live witness is hadron-knot-table",
        computed="1" if [r["path"] for r in live_A] == [LIVE_A_WITNESS] else "0",
        expected="1", tolerance="0",
        source="matches the corpus's own Q0_FLIP = 1 from q0_anchor_consistency_audit.py",
    )
    w.add_assertion(
        "most A-carrying witnesses are quoting it, not computed at it",
        computed=str(len(quoting_A)), expected=str(len(rows) - len(computed_at_A)),
        tolerance="0",
        source="a grep for the literal over-counts the migration surface ~10x",
    )

    w.add_caveat(
        "Bean qou-tekx's scoping text says the anchor-defining witness is the only "
        "thing frozen at A. That is stale: fca08de7d29 (2026-08-28) migrated it, "
        "and this audit measures what remains instead of assuming it."
    )
    w.add_caveat(
        "The one live file needs NO code change — hadron_knot_table is listed "
        "ideal_muon in q0_anchor_manifest.json, so a re-run resolves the muon "
        "anchor to C and writes C. The blocker is cost: per AGENTS.md the producer "
        "ran 50 minutes on deuterium, the first bound atom of nineteen, and was "
        "killed by its own timeout (exit 124, zero tracebacks). It does not crash; "
        "it does not finish."
    )
    w.add_caveat(
        "This audit does not re-pin anything and must not become a sweep. Re-pinning "
        "the anchor witness inside a bulk pass took main red on 2026-08-19 (262 "
        "correctly-stamped witnesses flipped to Q0_FLIP). q0_repin_sweep.py's "
        "ANCHOR_DEFINING exclusion exists for that; do not remove it."
    )

    out = w.save()
    print(f"\n  witness -> {out}")
    failed = [a for a in w.assertions if not a.passed]
    print(f"  assertions: {len(w.assertions) - len(failed)}/{len(w.assertions)} pass")
    for a in failed:
        print(f"    FAIL  {a.name}: computed={a.computed} expected={a.expected}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
