#!/usr/bin/env python3
"""
library-orphan-audit — detect library/ documents invisible to corpus-grep path 5.

A `library/<doc-id>/` holding a PDF and nothing else — no `sections/`, no `ocr/` — is
**invisible at every tier** of the corpus-grep path-5 checklist: no INDEX row (tier 1),
no `summary.json` (tier 2), no `sections/` (tier 3), no `ocr/` (tier 4). That is strictly
worse than not holding the paper at all, because a "has the corpus got this?" check comes
back clean while the document sits on disk.

## Why this exists when a guard already does

`scripts/migrate-uploads-to-library.py` REFUSES to create such a directory (bean `qou-cvx9`,
landed in #6978), and that refusal was verified working against the exact shape below —
a bare PDF whose canonical directory has no `structure.json` — where it prints
`REFUSED 1 move(s) — target has no structure.json`.

**It still happened.** `library/arxiv-0705.2975v1/` was created on `main` at 2026-09-07 11:38
(`588ed02d5fc`, `R100 uploads/0705.2975v1.pdf -> library/arxiv-0705.2975v1/0705.2975v1.pdf`,
no `structure.json` in the commit) — two hours AFTER the guard landed at 09:21 (`08d1fa9d4fd`,
confirmed an ancestor). So the PDF was moved by some other route: a hand `git mv`, or a tool
that is not that script.

That is the failure class AGENTS.md's detector-blindness taxonomy calls **a guard installed on
one of an API's several write paths** (row 33, bean `qou-3ral`). The repair for it is not a
second entry-point guard — there is always another entry point — but a check on the **invariant**,
which no write path can bypass. This is that check.

## What it checks

  1. **No orphans.** No `library/<doc-id>/` lacks both `sections/` and `ocr/`.
  2. **The index arithmetic closes.** `dirs - INDEX rows` must equal exactly
     `duplicates + containers + orphans`, with **zero residual**. A non-zero residual means a
     document is unaccounted for in a way none of the named populations explains.

Exit 0 when both hold, 1 otherwise.

Usage:
    library-orphan-audit.py              # audit the repo
    library-orphan-audit.py --json       # machine-readable
    library-orphan-audit.py --selftest   # prove the detector actually fires

`--selftest` builds a synthetic orphan in a temp tree and asserts it is FOUND, then removes it
and asserts the tree is clean. Per the corpus's calibration discipline: a detector is not
trusted because it passes, but because reverting the thing it detects makes it fail.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def audit(lib: str, index_md: str | None = None) -> dict:
    """Classify every library/ directory. Pure measurement; no writes."""
    if not os.path.isdir(lib):
        return {"error": f"no such directory: {lib}"}
    dirs = sorted(d for d in os.listdir(lib) if os.path.isdir(os.path.join(lib, d)))

    orphans, duplicates, containers, ingested = [], [], [], []
    for d in dirs:
        p = os.path.join(lib, d)
        has_sec = os.path.isdir(os.path.join(p, "sections"))
        has_ocr = os.path.isdir(os.path.join(p, "ocr"))
        if not has_sec and not has_ocr:
            orphans.append(d)
            continue
        # a duplicate copy carries `duplicate_of` in its first section's front-matter
        is_dup = False
        if has_sec:
            files = sorted(os.listdir(os.path.join(p, "sections")))
            if files:
                try:
                    head = open(os.path.join(p, "sections", files[0]),
                                encoding="utf-8", errors="replace").read(2000)
                    is_dup = "duplicate_of" in head
                except OSError:
                    pass
        if is_dup:
            duplicates.append(d)
        elif os.path.isfile(os.path.join(p, "container_note.md")) or d == "ant-v14-n7-s":
            containers.append(d)
        else:
            ingested.append(d)

    rows = 0
    idx = index_md or os.path.join(lib, "INDEX.md")
    if os.path.isfile(idx):
        with open(idx, encoding="utf-8", errors="replace") as fh:
            rows = sum(1 for line in fh if line.startswith("| ["))

    gap = len(dirs) - rows
    accounted = len(duplicates) + len(containers) + len(orphans)
    return {
        "dirs": len(dirs),
        "index_rows": rows,
        "gap": gap,
        "orphans": orphans,
        "duplicates": len(duplicates),
        "containers": len(containers),
        "ingested": len(ingested),
        "accounted": accounted,
        "residual": gap - accounted,
    }


def report(r: dict) -> int:
    if "error" in r:
        print(r["error"])
        return 1
    print(f"library dirs        {r['dirs']}")
    print(f"INDEX.md rows       {r['index_rows']}")
    print(f"gap                 {r['gap']}")
    print(f"  duplicates        {r['duplicates']}")
    print(f"  containers        {r['containers']}")
    print(f"  ORPHANS           {len(r['orphans'])}")
    print(f"  residual          {r['residual']}")
    ok = True
    if r["orphans"]:
        ok = False
        print()
        print(f"FAIL: {len(r['orphans'])} document(s) hold neither sections/ nor ocr/ —")
        print("      invisible at EVERY tier of corpus-grep path 5:")
        for d in r["orphans"]:
            print(f"        library/{d}/")
        print()
        print("      Ingest them, then regenerate the index:")
        print("        python3 folio-assistant/scripts/pdf-structure.py <pdf> -o library/")
        print("        python3 folio-assistant/scripts/pdf-ocr.py <pdf> -o library/<doc-id>"
              "   # scanned PDFs only")
        print("        python3 scripts/summarize-library.py --apply")
    if r["residual"] != 0:
        ok = False
        print()
        print(f"FAIL: residual {r['residual']} — dirs - rows is not explained by")
        print("      duplicates + containers + orphans. A document is unaccounted for.")
    if ok:
        print()
        print("OK: no orphans; index arithmetic closes with zero residual.")
    return 0 if ok else 1


def selftest() -> int:
    """Prove the detector fires. Build an orphan, assert FOUND; remove it, assert clean."""
    tmp = tempfile.mkdtemp(prefix="liborphan-")
    try:
        lib = os.path.join(tmp, "library")
        os.makedirs(os.path.join(lib, "arxiv-good", "sections"))
        with open(os.path.join(lib, "arxiv-good", "sections", "sec-000-x.md"), "w") as fh:
            fh.write("---\ndoc_id: arxiv-good\n---\nbody\n")
        with open(os.path.join(lib, "INDEX.md"), "w") as fh:
            fh.write("| [arxiv-good](arxiv-good/) | x |\n")

        clean = audit(lib)
        if clean["orphans"] or clean["residual"] != 0:
            print(f"SELFTEST FAIL: clean tree reported dirty: {clean}")
            return 1

        # now plant the exact observed shape: a directory holding only a PDF
        bare = os.path.join(lib, "arxiv-0705.2975v1")
        os.makedirs(bare)
        with open(os.path.join(bare, "0705.2975v1.pdf"), "wb") as fh:
            fh.write(b"%PDF-1.4\n")
        dirty = audit(lib)
        if "arxiv-0705.2975v1" not in dirty["orphans"]:
            print(f"SELFTEST FAIL: planted orphan NOT detected: {dirty}")
            return 1
        if report(dirty) == 0:
            print("SELFTEST FAIL: report() returned OK on a tree with an orphan")
            return 1

        # and removing it must restore clean
        shutil.rmtree(bare)
        again = audit(lib)
        if again["orphans"] or again["residual"] != 0:
            print(f"SELFTEST FAIL: removing the orphan did not restore clean: {again}")
            return 1

        print()
        print("SELFTEST PASS: orphan planted -> DETECTED; orphan removed -> clean.")
        print("  (calibrated by reverting the condition, not by observing a pass)")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="prove the detector fires on a synthetic orphan")
    ap.add_argument("--library", default=os.path.join(REPO, "library"))
    args = ap.parse_args()

    if args.selftest:
        return selftest()
    r = audit(args.library)
    if args.json:
        print(json.dumps(r, indent=2, sort_keys=True))
        return 0 if (not r.get("orphans") and r.get("residual") == 0) else 1
    return report(r)


if __name__ == "__main__":
    raise SystemExit(main())
