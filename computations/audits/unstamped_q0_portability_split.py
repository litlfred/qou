#!/usr/bin/env python3
"""Split the resolvable-but-unstamped witnesses by WHAT WOULD FIX EACH ONE.

Bean `1j39`. Pure static inspection + JSON reads; no arithmetic, so the
NO-FLOAT64 discipline is satisfied vacuously.

THE QUESTION
------------
A witness is *resolvable-but-unstamped* when it carries a q₀ pin under a key
`qou_substrate.witness._Q0_FIELDS` recognises, at depth <= 3, but has no
`q0Anchor` provenance stamp. Nothing consults the pin it does carry, so the
`qou-1c4y` proton migration cannot be verified over these files.

The useful split is not "how many" but "what closes each one", and there are
four answers with nothing in common:

  A. producer GONE      -- `scriptFile` names a .py that no longer exists
                           anywhere in the tree. Nothing to port; the witness
                           is a historical record and can only be labelled by
                           hand or left alone.
  B. producer uses      -- `WitnessBuilder.build()` has stamped since the
     WitnessBuilder        stamping landed, so these witnesses are merely
                           STALE. Re-running the producer fixes them, at the
                           cost of regenerating every number in the file.
  C. producer HAND-ROLLS -- a bare `json.dump`, never reaching `build()`.
     json.dump             Re-running will never stamp these. They are the
                           `stamp_q0` CANDIDATES -- see the caveat below,
                           because most of them are not actually stampable.
  D. producer UNNAMED    -- no `scriptFile` at all. Cannot be ported because
                           nothing says what to port.

WHY THIS SCRIPT EXISTS RATHER THAN A NUMBER IN A DOCSTRING
-----------------------------------------------------------
It was a number in a docstring, and the number was wrong within a day.
`_witness_q0_stamp.py` shipped asserting *"every one of the 169 is from a
hand-rolled producer"* and that regeneration therefore could not fix them.
Measured here: of 120 named producers, **62 use WitnessBuilder** (bucket B,
regeneration fixes them) and only **15 hand-roll** (bucket C). The claim was
wrong about ~four fifths of the class it described, and it was wrong because
it was measured once and then written down.

TWO EXTRACTION TRAPS, both of which produced wrong counts before this script
settled — check them before trusting any figure about this class:

  1. **`scriptFile` is TOP-LEVEL, not under a `witness` block.** Reading
     `payload["witness"]["scriptFile"]` finds nothing and reports every
     witness as unattributed (measured: 0 named, against a true 124).
  2. **`scriptFile` USUALLY holds a bare basename, not a repo-relative path** —
     but not always, and treating either shape as the rule is a trap.
     `Path(sf).exists()` is False for essentially all the basename ones, which
     reads as "the producer was deleted" (measured: 121 of 124 "missing",
     against a true 41). Meanwhile `binding-additive-linked-cluster-scan`
     records the full `computations/probes/...py` path, so a resolver that
     assumes basename-only would miss the directory it is told. Take
     `Path(sf).name` and resolve that across the tree, preferring the
     non-`_deprecated` copy — that is correct for both shapes.

BUCKET C IS A CANDIDATE SET, NOT A WORKLIST (measured 2026-08-28, `1j39`)
-------------------------------------------------------------------------
This script decides bucket C from the producer's SOURCE (`json.dump` present,
`WitnessBuilder` absent). That is the right test for "will re-running ever
stamp it", and it says nothing about whether re-running is SAFE. Measured over
15 of the 16 live bucket-C producers, **7 proved stampable and 8 did not**:

  * **3 were stampable as they stood.**
  * **5 STRIPPED provenance on re-run** -- they emitted a witness MISSING
    `scriptFile`, `engine` and `auditOnly`, fields the committed copy has
    because they were added downstream rather than by the producer. Stamping
    one would have added `q0Anchor` while deleting the very `scriptFile` this
    script uses to classify it into bucket C. AGENTS.md's "bare producers"
    hazard. **FIXED for all 5** by having each producer emit those three keys
    itself; 4 of them then stamped cleanly. (The fix also repaired 2 DANGLING
    `auditOnly` pointers: both targets had moved to `docs/audits/_deprecated/`
    and nothing checks that the path resolves.)
  * **4 move numbers** -- `qou-fl9i`'s `mp.dps = 50` -> `set_compute_dps()` fix
    landed in the producers and their witnesses were never regenerated.
  * **1 moves numbers for a DIFFERENT, unidentified reason** (~7e-5, two orders
    above the dps class): `sublemma_2_1_alpha_shift_extract`. Its provenance is
    fixed but it is deliberately NOT stamped, because stamping forces a
    regeneration that would rewrite 92 lines of values under a provenance
    commit message.
  * **1 has content drift**, **1 now fails its own assertions**, **1 writes
    nothing**.

The lesson for the next pass: "not stampable" is usually a fixable producer
defect, not a property of the witness. Five of the eight blockers were the same
downstream-provenance bug, and fixing it converted four of them.

So read `C-handrolled` as an upper bound, and dry-run any producer before
stamping it: run it, diff the witness, and confirm nothing but provenance
moved. This script deliberately does NOT run producers -- it is a static audit,
and adding a run would make it slow, environment-dependent, and capable of
dirtying the tree (producers write SIBLING witnesses).

A SECOND REASON TO DRY-RUN: `scriptFile` MAY NAME A CONSUMER, NOT THE WRITER
----------------------------------------------------------------------------
Every bucket here is assigned by inspecting the file `scriptFile` names, which
assumes that file WROTE the witness. It does not always. Raised by the #5919
author, whose worked example is `free-neutron-decay.witness.json` naming
`derived_masses.py` -- a module that only READS it. Where that happens this
script classifies the wrong file's source as builder-vs-hand-rolled, and a
stamp applied on its verdict would patch a consumer.

Nothing here detects it, and a static audit cannot: deciding which module
writes a given path means resolving delegated writes through shims. **The
dry-run is what closes it** -- running the named producer and requiring the
witness to actually change proves the attribution empirically, which is why
every stamp landed under `1j39` was gated on one. Treat a bucket assignment as
a hypothesis about who writes the file, not a fact.

Exit 0 always -- this reports, it does not gate.
"""
from __future__ import annotations

import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

_REPO = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_REPO / "tools" / "qou-substrate" / "python"))

from qou_substrate.witness import _Q0_FIELDS  # noqa: E402

#: Matches `_witness_q0_stamp._find_pin`. A deeper hit is more likely to be a
#: recorded reference value in a data table than the pin the producer ran at.
_MAX_PIN_DEPTH = 3


def find_pin(node, depth: int = 0):
    """The q₀ the payload itself records, or None."""
    if depth > _MAX_PIN_DEPTH:
        return None
    if isinstance(node, dict):
        for k, v in node.items():
            if k in _Q0_FIELDS and isinstance(v, str) and v.startswith("1.1"):
                return v
        for v in node.values():
            found = find_pin(v, depth + 1)
            if found is not None:
                return found
    return None


def script_of(payload: dict):
    """The producer this witness names, or None.

    Checks the top-level `scriptFile` FIRST -- see trap 1 in the module
    docstring. The two fallbacks cover older shapes; `computation` is also
    sometimes a bare STRING naming a computation rather than a file, which is
    deliberately NOT treated as an attribution (a name is not a producer).
    """
    sf = payload.get("scriptFile")
    if isinstance(sf, str) and sf.strip():
        return sf.strip()
    comp = payload.get("computation")
    if isinstance(comp, dict) and isinstance(comp.get("script"), str):
        return comp["script"].strip() or None
    wit = payload.get("witness")
    if isinstance(wit, dict) and isinstance(wit.get("scriptFile"), str):
        return wit["scriptFile"].strip() or None
    return None


def build_py_index() -> dict:
    """basename -> best path, preferring live over `_deprecated`, then shortest.

    GIT-TRACKED FILES ONLY. A bare `rglob` walks `.lake/`, vendored packages
    and any local venv, so a producer basename could resolve to a third-party
    copy sharing its name, and the builder-vs-hand-rolled verdict would then
    be about the wrong file.

    On this tree the restriction changes NOTHING — both indexes give the same
    18/65/41/56 split. It is a guard against an environment that happens to
    have a colliding basename checked out, not a fix for a defect observed
    here. Stated because the obvious way to write this comment ("measured: N
    against M") would be inventing a measurement that was never taken.
    """
    tracked = subprocess.check_output(
        ["git", "ls-files", "*.py"], cwd=_REPO, text=True).split()
    idx = defaultdict(list)
    for rel in tracked:
        p = _REPO / rel
        idx[p.name].append(p)
    for name in idx:
        idx[name].sort(key=lambda p: (("_deprecated" in str(p) or "fsh-guts" in str(p)), len(str(p))))
    return {k: v[0] for k, v in idx.items()}


def classify_producer(path: Path) -> str:
    """`builder` if it reaches WitnessBuilder, `handrolled` if it json.dumps."""
    try:
        src = path.read_text(errors="replace")
    except Exception:                                   # noqa: BLE001
        return "unreadable"
    if "WitnessBuilder" in src:
        return "builder"
    if "json.dump" in src:
        return "handrolled"
    return "no-write-found"


def main() -> int:
    tracked = subprocess.check_output(
        ["git", "ls-files", "*.witness.json"], cwd=_REPO, text=True).split()

    rows = []          # (witness_rel, scriptFile-or-None)
    stamped = 0
    for rel in tracked:
        try:
            payload = json.loads((_REPO / rel).read_text())
        except Exception:                               # noqa: BLE001
            continue
        if not isinstance(payload, dict):
            continue
        if payload.get("q0Anchor"):
            stamped += 1
            continue
        if find_pin(payload) is None:
            continue
        rows.append((rel, script_of(payload)))

    pyidx = build_py_index()
    buckets = defaultdict(list)
    for rel, sf in rows:
        if not sf:
            buckets["D-unnamed"].append((rel, None))
            continue
        # Trap 2: resolve by basename, not by treating the value as a path.
        hit = pyidx.get(Path(sf).name)
        if hit is None:
            buckets["A-producer-gone"].append((rel, sf))
            continue
        kind = classify_producer(hit)
        key = {"builder": "B-builder-stale",
               "handrolled": "C-handrolled"}.get(kind, "E-" + kind)
        buckets[key].append((rel, str(hit.relative_to(_REPO))))

    print("resolvable-but-unstamped q₀ witnesses — what would fix each")
    print(f"  witnesses tracked          {len(tracked)}")
    print(f"  already carrying q0Anchor  {stamped}")
    print(f"  RESOLVABLE BUT UNSTAMPED   {len(rows)}")
    print()
    order = ["A-producer-gone", "B-builder-stale", "C-handrolled",
             "D-unnamed"] + sorted(k for k in buckets if k.startswith("E-"))
    fix = {
        "A-producer-gone":  "nothing to port — producer deleted/renamed",
        "B-builder-stale":  "RE-RUN the producer; build() stamps",
        "C-handrolled":     ("stamp_q0() CANDIDATES — re-running never stamps "
                             "them; 7 of 15 examined proved stampable, 4 only "
                             "after fixing the producer. DRY-RUN each first "
                             "(see docstring)"),
        "D-unnamed":        "no producer named; classify by the recorded pin",
    }
    for key in order:
        items = buckets.get(key, [])
        prods = {p for _, p in items if p}
        live = sum(1 for w, _ in items if "_deprecated/" not in w)
        print(f"  {key:<18} {len(items):>4} witness(es) over {len(prods):>3} producer(s)"
              f"   [{live} live / {len(items) - live} deprecated]")
        print(f"                     -> {fix.get(key, 'unclassified')}")

    hand = buckets.get("C-handrolled", [])
    live_hand = sorted({p for w, p in hand if "_deprecated/" not in (p or "")})
    print()
    print(f"stamp_q0 targets — live hand-rolled producers ({len(live_hand)}):")
    for p in live_hand:
        print(f"    {p}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
