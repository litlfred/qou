#!/usr/bin/env python3
"""Mark agent QA verdicts that carry no ``field_hash`` as expired, in place.

An agent verdict with no ``field_hash`` records no block version, so it cannot be
resolved against any content and adjudicates nothing. The drain queue already
knows this --- ``folio/pipeline/qa-agent-drain-queue.ts`` computes ``fresh`` as
``e.field_hash?.md === curmd``, and a missing hash is ``undefined``, never equal
--- so every affected block is already re-queued for review.

A *reader* does not know it. Opening a sidecar shows ``"result": "pass"`` beside
a confident note, with nothing to say the verdict is inert. This script closes
that gap and only that gap.

WHY MARK RATHER THAN DELETE.  Deleting 68,380 agent verdicts is the operation
this corpus has already regretted once: ``qou-tqr9`` records agent-adjudicated
axes "silently lost by regenerate-rather-than-merge", 7,381 of them, and
``scripts/qa-sidecar-agent-union.py`` exists to undo exactly that. Marking is
reversible, preserves the record, and fixes what is actually broken --- how the
entry reads. Nothing here removes a verdict.

WHAT IS NOT CHANGED.  ``result``, ``reviewer``, ``reviewed_at``, ``evidence`` and
every other field are untouched. Changing ``result`` to ``n/a`` was considered
and rejected: the criterion is not inapplicable, so that would assert something
false. Only ``notes`` gains a prefix, and each file gains one ``$expired``
explanation.

Provenance of the population: origin ``e62336dabc1`` (2026-07-07, "heuristic
agentic redo for proof criteria (full replace)"); the writers were deleted in
``9ddf0ad9c0`` and none survives. Analysis: bean ``qou-pwut``.

Idempotent. ``--dry-run`` is the default; pass ``--apply`` to write.
"""
from __future__ import annotations

import argparse
import collections
import json
import pathlib
import sys

MARK = "[EXPIRED-NO-FIELD-HASH] "

NOTE = (
    "Entries whose notes begin with "
    f"{MARK.strip()} carry no field_hash, so they record no block version and "
    "adjudicate nothing. They are retained as a historical record, not as live "
    "verdicts. The drain queue already treats them as not-fresh and has "
    "re-queued the block. See bean qou-pwut."
)


def dumps_like(original: str, doc: object) -> str:
    """Serialize matching the file's own conventions.

    Files differ in whether non-ASCII was escaped at write time; picking the
    wrong one turns a semantic edit into a whole-file rewrite. Detect by
    round-tripping the untouched original rather than guessing.
    """
    for ensure in (True, False):
        if json.dumps(json.loads(original), indent=2, ensure_ascii=ensure) + "\n" == original:
            return json.dumps(doc, indent=2, ensure_ascii=ensure) + "\n"
    # No exact round-trip (hand-edited whitespace). Default to the repo norm.
    return json.dumps(doc, indent=2) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="content")
    ap.add_argument("--apply", action="store_true", help="write (default: dry-run)")
    args = ap.parse_args()

    files = sorted(pathlib.Path(args.root).rglob("*.qa.json"))
    stats = collections.Counter()
    crit = collections.Counter()

    for path in files:
        original = path.read_text()
        try:
            doc = json.loads(original)
        except json.JSONDecodeError:
            stats["unparseable"] += 1
            continue

        changed = False
        for name, entries in (doc.get("criteria") or {}).items():
            if not isinstance(entries, list):
                continue
            for entry in entries:
                if not isinstance(entry, dict):
                    continue
                if (entry.get("reviewer") or {}).get("kind") != "agent":
                    continue
                # An EMPTY ``field_hash: {}`` records no block version either:
                # the drain's freshness test is ``e.field_hash?.md === curmd``,
                # and ``{}.md`` is ``undefined`` exactly as a missing key is.
                # The first version of this script tested ``"field_hash" in
                # entry``, which skipped 2,040 such entries.
                if entry.get("field_hash"):
                    continue
                notes = entry.get("notes") or ""
                if notes.startswith(MARK):
                    stats["already marked"] += 1
                    continue
                entry["notes"] = MARK + notes
                crit[name] += 1
                stats["marked"] += 1
                changed = True

        if changed:
            stats["files"] += 1
            doc.setdefault("$expired", NOTE)
            if args.apply:
                path.write_text(dumps_like(original, doc))

    print(f"  entries marked  : {stats['marked']}")
    print(f"  already marked  : {stats['already marked']}")
    print(f"  files touched   : {stats['files']} of {len(files)}")
    if stats["unparseable"]:
        print(f"  UNPARSEABLE     : {stats['unparseable']}")
    print(f"  mode            : {'APPLIED' if args.apply else 'dry-run'}")
    print("\n  top criteria:")
    for name, n in crit.most_common(8):
        print(f"    {n:6}  {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
