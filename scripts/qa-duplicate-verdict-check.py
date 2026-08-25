#!/usr/bin/env python3
"""Flag QA sidecar criterion slots that carry contradictory agent verdicts.

The `<block>.qa.json` criterion arrays are append-only by design: entries
append, and the script-kind scanner candidates stay in place as provenance.
Nothing in `block-qa/v1` says which of two entries supersedes the other, so
when one agent records twice on the *same* source with *different* verdicts,
the record is ambiguous — a consumer reading the array gets `fail` from the
first element and `pass` from the last.

Agents do sometimes supersede correctly and say so, in `evidence` free text.
That is not machine-readable, which is exactly the problem this reports.

Three shapes, only one of which is a defect:

  CONTRADICTION  same reviewer.id, same NON-EMPTY field_hash.md,
                 differing `result` -> reported, exit 1
  REDUNDANT      same reviewer.id, same field_hash.md, same `result`
                 -> counted, advisory only
  RE-RECORD      same reviewer.id, DIFFERING field_hash.md
                 -> ignored: this is the prescribed fix-then-re-record, where
                    the later entry certifies the edited `.md`
  UNDETERMINED   entries carry no `field_hash.md` at all -> counted separately.
                 Two hash-less entries are NOT demonstrably on the same source,
                 so calling them contradictory would overstate what is known.

Reviewer ids come in two shapes and only one is suspicious on repeat:

  agent:<batch>  one batch, one pass over the block. A second entry from the
                 same batch means it recorded twice -> this is the finding.
  local/<skill>  a skill re-run across sessions. Entries accumulate as
                 legitimate history; a later verdict differing from an earlier
                 one is a re-audit, not an ambiguity. Reported separately and
                 never counted toward the exit code.

Usage:
    python3 scripts/qa-duplicate-verdict-check.py [path ...] [--json] [--all]

`--all` also lists the redundant slots. Bean qou-supr.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

CONTENT = Path("content")


def slots(path: Path):
    """Yield (criterion, reviewer_id, entries) for every agent group in one sidecar."""
    try:
        doc = json.loads(path.read_text(encoding="utf8"))
    except (OSError, json.JSONDecodeError):
        return
    for criterion, entries in (doc.get("criteria") or {}).items():
        if not isinstance(entries, list):
            continue
        by_id = defaultdict(list)
        for entry in entries:
            reviewer = entry.get("reviewer") or {}
            if reviewer.get("kind") != "agent":
                continue
            rid = reviewer.get("id")
            if rid:
                by_id[rid].append(entry)
        for rid, group in by_id.items():
            if len(group) > 1:
                yield criterion, rid, group


def classify(group):
    """CONTRADICTION / REDUNDANT / UNDETERMINED / None."""
    hashes = {(e.get("field_hash") or {}).get("md") for e in group}
    if hashes == {None}:
        return "UNDETERMINED"             # no hash: cannot tell if same source
    if len(hashes) > 1:
        return None                       # fix-then-re-record; the later one wins
    results = {e.get("result") for e in group}
    return "CONTRADICTION" if len(results) > 1 else "REDUNDANT"


def main(argv):
    show_all = "--all" in argv
    as_json = "--json" in argv
    targets = [a for a in argv if not a.startswith("--")]
    paths = (
        [Path(t) for t in targets]
        if targets
        else sorted(CONTENT.glob("**/*.qa.json"))
    )

    contradictions, redundant, undetermined, reaudits = [], [], [], []
    for path in paths:
        for criterion, rid, group in slots(path):
            kind = classify(group)
            if kind is None:
                continue
            row = {
                "file": str(path),
                "criterion": criterion,
                "reviewer": rid,
                "entries": len(group),
                "md_hash": (group[0].get("field_hash") or {}).get("md"),
                "results": [e.get("result") for e in group],
            }
            if kind == "REDUNDANT":
                redundant.append(row)
            elif kind == "UNDETERMINED":
                undetermined.append(row)
            elif rid.startswith("agent:"):
                contradictions.append(row)      # one batch, recorded twice
            else:
                reaudits.append(row)            # skill re-run: legitimate history

    if as_json:
        json.dump(
            {
                "contradictions": contradictions,
                "reaudits": reaudits,
                "undetermined": undetermined,
                "redundant": redundant,
            },
            sys.stdout,
            indent=2,
        )
        print()
        return 1 if contradictions else 0

    for row in contradictions:
        print(f"{row['file']}")
        print(
            f"    {row['criterion']}  [{row['reviewer']}]  "
            f"{row['entries']} entries at md={row['md_hash']}  "
            f"results: {' vs '.join(str(r) for r in row['results'])}"
        )
    if show_all:
        for row in redundant:
            print(f"{row['file']}")
            print(
                f"    {row['criterion']}  [{row['reviewer']}]  "
                f"{row['entries']} identical entries (redundant)"
            )

    print(
        f"\nsidecars scanned: {len(paths)}\n"
        f"  contradictory (one agent batch, same hash, differing verdict): "
        f"{len(contradictions)}\n"
        f"  re-audits (skill re-run across sessions — legitimate history): "
        f"{len(reaudits)}\n"
        f"  undetermined (no field_hash.md — cannot tell): {len(undetermined)}\n"
        f"  redundant (identical verdict recorded twice): {len(redundant)}"
    )
    if contradictions:
        print(
            "Each contradictory slot needs one entry chosen as authoritative — "
            "that is a re-adjudication of the block, not a mechanical edit. "
            "See bean qou-supr."
        )
    return 1 if contradictions else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
