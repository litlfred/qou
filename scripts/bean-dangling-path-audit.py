#!/usr/bin/env python3
"""Open beans naming a repo path that no longer resolves.

WHY THIS EXISTS, and why it is not the staleness ranking. Its sibling
`bean-staleness-triage.py` ranks by "the tree moved UNDER the bean" — commits
touching the bean's named paths since its `updated_at`. This asks the opposite
question, "did the tree move OUT FROM UNDER it", and the ranking structurally
cannot answer it: a DELETED path has no commits after any date, so a bean whose
files are gone scores **zero** and sorts to the very bottom of the ranking.

WHAT IT IS NOT. A named path that does not resolve is a TRIAGE SIGNAL, never a
verdict. Four classes of false positive were measured on 2026-09-06, and three
of them are filtered here; read the fourth before acting on any row.

  1. PLACEHOLDERS — `computations/X.witness.json`, `computations/substrate/x.py`.
     Metasyntactic examples in bean prose. Filtered by _PLACEHOLDER.

  2. ELIDED PATHS — `content/.../lean/QOU/Foo.lean`, and also
     `docs/audits/2026-08-08-...-attack-vectors...md`, where the ellipsis sits
     INSIDE a segment rather than being one. A path abbreviated for readability;
     the regex cannot reconstruct it. Filtered on `...` appearing anywhere. The
     whole-segment-only test missed the second form.

  3. SYMLINK-HIDDEN — the path exists under `folio-assistant/`, which is a
     SYMLINK to a sibling checkout. `os.path.exists` resolves it; `find` does
     NOT traverse it without `-L`. This class cost a whole wrong bean
     (`qou-7br7`, retracted the same day): two `find folio-assistant …` runs
     returned nothing and were read as corroboration that the library ingest
     producer had been deleted. It had not — 14 of 100 missing paths were
     platform files reachable through that symlink. Filtered by checking
     `folio-assistant/<path>` explicitly.

  4. MOVED, NOT DELETED — `computations/_deprecated/hecke_core_legacy.py` is now
     `computations/hecke_core_legacy.py`. NOT filtered, because "the bean's
     reference is stale" is a real if minor finding and the basename search that
     would suppress it also suppresses genuine deletions. Reported with a
     `moved?` marker naming where a same-basename file was found.

Usage:  python3 scripts/bean-dangling-path-audit.py [--all]
        --all   also list the filtered classes, for auditing the filter itself
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FA = os.path.join(ROOT, "folio-assistant")

_ROOTS = "computations|content|docs|scripts|tools|schemas|library|qou-mass"
PATH_RE = re.compile(
    rf'(?<![\w/.-])((?:{_ROOTS})/[\w./-]+\.(?:py|lean|ts|md|json|sh|rs|toml))'
)
# `X.witness.json`, `x.py`, `foo/X.py` — a path segment that is a lone letter is
# a stand-in, not a filename anyone shipped.
_PLACEHOLDER = re.compile(r'(?:^|/)[A-Za-z](?:\.[\w.]+)?$')


def classify(rel: str) -> tuple[str, str]:
    """-> (class, detail). class 'ok' means the path resolves."""
    if os.path.exists(os.path.join(ROOT, rel)):
        return "ok", ""
    if _PLACEHOLDER.search(rel):
        return "placeholder", ""
    # `...` ANYWHERE, not only as a whole segment: a bean writes both
    # `content/.../lean/Foo.lean` and `docs/audits/2026-08-08-...-vectors...md`,
    # and the second form has the ellipsis inside a segment.
    if "..." in rel:
        return "elided", ""
    if os.path.exists(os.path.join(FA, rel)):
        return "symlink-hidden", f"folio-assistant/{rel}"
    base = os.path.basename(rel)
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames
                       if d not in (".git", "node_modules", ".lake", ".beans")]
        if base in filenames:
            return "missing", f"moved? {os.path.relpath(os.path.join(dirpath, base), ROOT)}"
    return "missing", ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true",
                    help="also list the filtered classes")
    a = ap.parse_args()

    counts: dict[str, int] = {}
    rows: list[tuple[int, str, list[tuple[str, str]]]] = []
    filtered: dict[str, set[str]] = {}

    for bf in sorted(glob.glob(os.path.join(ROOT, ".beans", "*.md"))):
        txt = open(bf, encoding="utf-8", errors="replace").read()
        m = re.search(r'^status:\s*(\S+)', txt[:400], re.M)
        if not m or m.group(1) not in ("in-progress", "todo"):
            continue
        bid = os.path.basename(bf).split("--")[0]
        hits: list[tuple[str, str]] = []
        for rel in sorted(set(PATH_RE.findall(txt))):
            cls, detail = classify(rel)
            counts[cls] = counts.get(cls, 0) + 1
            if cls == "missing":
                hits.append((rel, detail))
            elif cls != "ok":
                filtered.setdefault(cls, set()).add(rel)
        if hits:
            rows.append((len(hits), bid, hits))

    rows.sort(reverse=True)
    print(f"{len(rows)} open bean(s) name a path that does not resolve, "
          f"after filtering placeholders / elided / symlink-hidden.\n")
    for n, bid, hits in rows:
        print(f"{bid}  ({n})")
        for rel, detail in hits:
            print(f"    {rel}" + (f"   [{detail}]" if detail else ""))

    print("\npath references by class (occurrences, not distinct):")
    for k in ("ok", "missing", "placeholder", "elided", "symlink-hidden"):
        print(f"  {k:<16}{counts.get(k, 0):>6}")

    if a.all:
        for cls, paths in sorted(filtered.items()):
            print(f"\nFILTERED — {cls} ({len(paths)} distinct):")
            for p in sorted(paths):
                print(f"  {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
