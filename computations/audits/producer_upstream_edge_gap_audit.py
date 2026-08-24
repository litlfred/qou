#!/usr/bin/env python3
"""Which producers READ a witness but never RECORD the edge?

The staleness machinery is only as good as the dependency graph it walks.
`witness_dependency_drift.py` propagates staleness along
`data.upstream_witness_hashes`, and says so in its own summary line:
"additionally stale via upstream propagation (RECORDED EDGES ONLY)". A producer
that consumes a witness without recording the edge is invisible to it — its
output silently keeps yesterday's inputs.

RETRACTION, 2026-08-23, of the case that motivated this audit. I claimed
`borromean-per-lambda-fr-probe` "records no edge" and was therefore invisible to
the drift detector, and generalised that into an uncounted corpus-wide class of
witnesses that are convention-C by inherited input. **The generalisation was
wrong, and the specific claim was wrong about the producer.**

Checked: that producer has called `record_upstream` on
`y-lambda-at-q0.witness.json` since **2026-08-08** (`453b2a8688`, "port 112 more
producers via record_upstream"), at line 105. Its witness carries the edge.

What was actually true is narrower and self-closing: the *previously committed*
witness was generated **2026-07-02**, a month BEFORE its producer learned to
record edges, so that witness had no edge and the drift detector could not walk
to it. The gap was between a witness and the instrumentation of its own
producer — not an unrecorded dependency, and not a class no detector counts.

The practical difference matters. "An uncounted class needs a new detector" and
"witnesses older than the 2026-08-08 port need regenerating" imply different
work, and only the second is real. The edge mechanism was already being adopted;
what lags is witness age.

## What this measures

Producer-side, complementing `witness_dependency_coverage_audit.py`'s
witness-side view — and without its `is_aggregator` name heuristic, which gates
the whole check behind names containing 'dashboard'/'status'/'summary' and so
examined 6 witnesses out of 2640.

For every live producer under `computations/`:

  READS    it mentions a `*.witness.json` path, or calls a known witness-loading
           helper (`record_upstream`, `load_witness`, `_load_upstream`).
  RECORDS  it calls `record_upstream` / `add_upstream` / `add_upstream_records`.

  GAP      READS and not RECORDS.

## What a GAP is and is not

It is **not** a defect in the producer's mathematics. It is a missing edge in
the staleness graph: the producer is correct today and cannot be told when it
stops being correct.

The fix is mechanical and the helper already exists —
`qou_substrate.witness.record_upstream(path, into)` was written precisely
because 290 of 330 consuming producers read their inputs before constructing a
builder, so the `add_upstream` *method* did not fit their shape.

Heuristic, therefore high-recall: a producer may read a witness through a
variable path this cannot see, and a `.witness.json` mention inside a comment
counts as a read. Treat the output as candidates.

## Which lever actually matters — measured, and it is not the obvious one

Having retracted the claim above, the obvious next step looked like
"regenerate witnesses older than the 2026-08-08 edge port, so drift can see
them". Measured over 2722 witnesses, that step is worth far less than it looks:

    no upstream edge                                2489
      generated AFTER the port                      1099   producer records nothing
      generated BEFORE the port                     1390
        ... AND producer NOW records edges            52   <- regen adds an edge
        ... producer still records nothing          1338   <- regen adds NOTHING

So regenerating by age buys **52** edges, not 1390. For the other 1338 the
producer never learned to record, so a fresh run reproduces the same edgeless
witness — at the cost of a value-attribution each.

And 1099 witnesses written AFTER the port still carry no edge, which is the
219-producer gap above showing up on the witness side.

**The lever is instrumenting the 219 gap producers, not regenerating.** One
helper call per producer makes every future run of it edge-bearing; regeneration
only helps the 52 whose producers are already instrumented. Recorded here
because the age-based plan is the intuitive one and it is mostly wasted work.
"""
from __future__ import annotations

import argparse
import ast
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]

# A READ must be an actual LOAD, not a mention. The first version of this
# audit matched any occurrence of ".witness.json" and reported 1868 readers
# against a corpus survey figure of ~330 consumers -- because a producer that
# merely NAMES ITS OWN OUTPUT file matches that string. Requiring a load
# pattern is what makes the denominator mean "consumes a witness".
READ_MARKERS = re.compile(
    r"record_upstream\s*\(|load_witness\s*\(|_load_upstream\s*\(|"
    r"json\.loads?\s*\([^)]*witness|"
    r"open\s*\([^)]*\.witness\.json|"
    r"Path\s*\([^)]*\.witness\.json[^)]*\)\s*\.read_(text|bytes)",
    re.I)
RECORD_MARKERS = re.compile(
    r"record_upstream\s*\(|add_upstream_records\s*\(|\.add_upstream\s*\(")
# A producer that only *writes* its own witness is not a consumer.
WRITE_ONLY = re.compile(r"WitnessBuilder|write_witness")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()

    reads, records, gaps = [], [], []
    for p in sorted((REPO / "computations").rglob("*.py")):
        sp = str(p)
        if "_deprecated" in sp or "__pycache__" in sp:
            continue
        try:
            src = p.read_text()
        except Exception:
            continue
        rel = str(p.relative_to(REPO))
        does_read = bool(READ_MARKERS.search(src))
        does_record = bool(RECORD_MARKERS.search(src))
        if does_read:
            reads.append(rel)
        if does_record:
            records.append(rel)
        if does_read and not does_record:
            gaps.append(rel)

    print("Producer-side upstream-edge coverage")
    print("=" * 62)
    # Coverage is (readers that record) / (readers), NOT records/reads.
    # Those are different sets: `add_upstream(...)` is a RECORD pattern that
    # is not a READ pattern, so some recorders never enter `reads`. Computing
    # records/reads gave 174/347 = 50.1% while 174 + 219 = 393 > 347 -- the
    # arithmetic does not close, which is how the error was caught.
    covered = len(reads) - len(gaps)
    print(f"  producers that READ a witness      : {len(reads)}")
    print(f"  ... of those, RECORD an edge       : {covered}")
    print(f"  ... GAP (read, no edge recorded)   : {len(gaps)}")
    pct = 100.0 * covered / len(reads) if reads else 0.0
    print(f"  edge coverage among readers        : {pct:.1f}%")
    print(f"  (producers recording an edge, any  : {len(records)} — includes")
    print(f"   {len(records) - covered} matched by a record pattern but no read pattern)")
    print()
    print("Every gap is a producer whose output cannot be told when its inputs")
    print("move. The fix is one helper call; see the module docstring.")

    if args.list:
        print()
        for g in gaps:
            print(f"  {g}")

    if args.json:
        pathlib.Path(args.json).write_text(json.dumps({
            "schema": "producer-upstream-edge-gap/v1",
            "reads": len(reads), "records": len(records),
            "gap": len(gaps), "gap_files": gaps,
        }, indent=1))
        print(f"\nwrote {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
