#!/usr/bin/env python3
"""
Witness stems that exist at two paths — and the ones whose CONSUMERS DIVERGE.

Bean `qou-kcii`. A witness is normally addressed by bare stem, not path:
`_path_bridge.witness_path("foo.witness.json", HERE)`. That resolver searches
`prefer_dir` first — typically the CALLING SCRIPT'S OWN directory — then the
`computations/` root, then each cluster subdirectory.

So when one stem exists at two paths, WHICH FILE A CONSUMER GETS DEPENDS ON
WHERE THE CONSUMER LIVES. Two scripts can read "the same witness" and receive
different numbers, with nothing in either script indicating it.

WHY THIS AUDIT REPORTS TWO NUMBERS
----------------------------------
Duplicated stems alone over-reports: a stem duplicated in a corner nothing
reads is untidy, not dangerous. The number that matters is how many stems
have consumers resolving to DIFFERENT copies. Measured 2026-08-21: 25 stems
duplicated, 7 of them consumer-splitting.

The 7 are not hypothetical. `habiro-coefficients-extended` is read by three
scripts in `computations/` (including `cross_check_trM_1ppb.py`, the L1
compute-precision gate) and two in `computations/habiro/` — and the two
copies differ: the top-level one holds 4/4 real results, the habiro/ one
holds 4/4 errors (bean `qou-ls7l`). A "cleanup" that unified them the wrong
way would hand the L1 gate a witness full of error stubs.

It already produced one wrong reading: a probe written for bean `qou-3zby`
used `rglob` instead of the resolver, read the other copy, and reported the
wrong `q0Anchor` for its headline input. Caught pre-commit, but only just.

A REFERENCE IS NOT A VERIFIED READ. The consumer scan is textual — it asks
which `.py` files mention the stem — so a stem named in a comment counts as
a consumer. That over-reports rather than under-reports, which is the safe
direction for a detector, but check the call site before acting on a row.

WHAT THIS DOES NOT DO
---------------------
It does not pick a winner or move anything. Which copy is canonical is the
owning arc's call — and for at least one pair the answer is NOT "keep the
one in the tidier directory": `witness_provenance_audit.py` exists twice as
two genuinely DIFFERENT audits (correctness vs completeness, bean `qou-2r42`),
so consolidating by name would silently swap one check for another.

Reported, not gated. A gate red on arrival gets skipped — this file's own
sibling `precision-gates.sh` says so at the top — and this is red at 7.

Usage:
    python3 computations/audits/duplicate_witness_stem_audit.py
    python3 computations/audits/duplicate_witness_stem_audit.py --strict
        exit 1 if any stem's consumers resolve to different copies
"""

from __future__ import annotations

import argparse
import collections
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTATIONS = HERE.parent
SKIP_PARTS = {"_deprecated", "__pycache__"}


def _cluster_dirs() -> list[Path]:
    """Mirror `_path_bridge._WITNESS_DIRS`: root first, then cluster subdirs.

    A cluster is a non-underscore, non-dot directory carrying `__init__.py`
    — the same filter the bridge applies, so an untracked scratch dir does
    not change what this audit predicts.
    """
    dirs = [COMPUTATIONS]
    for child in sorted(COMPUTATIONS.iterdir()):
        if not child.is_dir() or child.name.startswith(("_", ".")):
            continue
        if (child / "__init__.py").is_file():
            dirs.append(child)
    return dirs


def _resolve(stem: str, caller_dir: Path, dirs: list[Path]) -> Path | None:
    """Which copy `witness_path(stem, caller_dir)` would return."""
    for d in [caller_dir] + [x for x in dirs if x != caller_dir]:
        if (d / stem).exists():
            return d
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any stem's consumers resolve to different copies")
    args = ap.parse_args()

    dirs = _cluster_dirs()

    by_stem: dict[str, list[Path]] = collections.defaultdict(list)
    for p in COMPUTATIONS.rglob("*.witness.json"):
        if SKIP_PARTS & set(p.parts):
            continue
        by_stem[p.name].append(p.parent)
    dups = {k: v for k, v in by_stem.items() if len(v) > 1}

    # Self-excluded: this file names several stems in its own docstring, and
    # a docstring mention is not a read.
    self_path = Path(__file__).resolve()
    sources = {}
    for p in COMPUTATIONS.rglob("*.py"):
        if SKIP_PARTS & set(p.parts) or p.resolve() == self_path:
            continue
        try:
            sources[p] = p.read_text(errors="ignore")
        except OSError:
            continue

    split = []
    for stem in sorted(dups):
        key = stem[: -len(".witness.json")]
        got: dict[str, list[str]] = collections.defaultdict(list)
        for path, text in sources.items():
            if key not in text:
                continue
            r = _resolve(stem, path.parent, dirs)
            if r is not None:
                got[str(r.relative_to(COMPUTATIONS.parent))].append(path.name)
        if len(got) > 1:
            split.append({"stem": stem,
                          "resolves_to": {k: sorted(v) for k, v in sorted(got.items())}})

    print("=" * 70)
    print("duplicate-witness-stem audit")
    print("=" * 70)
    print(f"  witness stems duplicated across paths : {len(dups)}")
    print(f"  of those, CONSUMERS DIVERGE on        : {len(split)}")
    if split:
        print("\n  consumer-splitting stems (a 'cleanup' here changes what code reads):")
        for row in split:
            print(f"    {row['stem']}")
            for d, cs in row["resolves_to"].items():
                head = ", ".join(cs[:3]) + (" …" if len(cs) > 3 else "")
                print(f"        -> {d}/   read by {len(cs)}: {head}")
    print("\n  These are REFERENCES, not verified reads: the scan is textual, so a "
          "stem\n  named only in a comment counts. That over-reports rather than "
          "under-reports,\n  which is the right direction for a detector — but check "
          "the call site\n  before acting on a row.\n\n  Reported, not gated. Which "
          "copy is canonical is the owning arc's call;\n  see bean qou-2r42 for a pair "
          "where consolidating by name would swap\n  one audit for a different one.")

    if args.strict and split:
        print(f"\nSTRICT: {len(split)} stem(s) resolve differently per consumer — "
              "exiting 1", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
