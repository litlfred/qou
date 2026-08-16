#!/usr/bin/env python3
"""
library-refresh-metadata — re-derive each document's title and authors with
the current extractor, without disturbing anything else.

## Why not just re-run the producer

Because `pdf-structure.py` writes a whole `structure.json`, and this
library's `structure.json` files now carry state the producer knows
nothing about: `container` markers from the bound-volume split, and
`duplicate_of` / `duplicate_copies` from the duplicate adjudication. A
straight re-run silently discards all of it.

So the producer is called in `--json` mode, which writes nothing, and only
`metadata` is merged. Section files are left alone: their text is
unchanged by a metadata fix, and rewriting 6,900 files to no effect is not
free for a reviewer.

## What actually changes

`pdf-structure.py` learned to repair two kinds of PDF extraction damage —
ligatures and floating accents (`Reﬁned`, `Gr¨ obner`) and kerning splits
(`STA VROS GAROUF ALIDIS`) — and to skip more publisher front matter that
was being taken as the title. Titles extracted before that landed in
`library/INDEX.md` and in `references.ts`, where a search for
"Garoufalidis" does not match "GAROUF ALIDIS".

The previous title is kept as `metadata.title_prev` whenever it differs,
so a bad repair is visible and reversible rather than silently overwriting
what a reader may have already cited.

Usage:
    scripts/library-refresh-metadata.py                # dry run, shows diffs
    scripts/library-refresh-metadata.py --apply
    scripts/library-refresh-metadata.py --only <doc-id>
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.path.join(REPO, "library")
PRODUCER = os.path.join(os.path.dirname(REPO), "folio-assistant",
                        "scripts", "pdf-structure.py")

# `title_lines` matters as much as `title`: it is what lets a consumer
# split a byline off, and omitting it here silently withheld the fix
# that had just been added to the producer for exactly that purpose.
FIELDS = ("title", "title_lines", "authors_raw", "abstract", "arxiv", "doi")


def extract(pdf: str) -> dict | None:
    r = subprocess.run([sys.executable, PRODUCER, "--json", pdf],
                       capture_output=True, text=True)
    if r.returncode != 0 or not r.stdout.strip():
        return None
    try:
        return json.loads(r.stdout).get("metadata") or {}
    except Exception:
        return None


def main() -> int:
    ap = argparse.ArgumentParser(description="Re-derive library metadata with the current extractor")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--only", help="single doc-id")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    if not os.path.exists(PRODUCER):
        sys.exit(f"producer not found: {PRODUCER}\n"
                 "run scripts/setup-folio-assistant.sh first")

    docs = sorted(os.listdir(LIB))
    if args.only:
        docs = [d for d in docs if d == args.only]

    changed = failed = seen = 0
    for doc in docs:
        d = os.path.join(LIB, doc)
        sj = os.path.join(d, "structure.json")
        if not (os.path.isdir(d) and os.path.exists(sj)):
            continue
        pdfs = sorted(glob.glob(os.path.join(d, "*.pdf")))
        if not pdfs:
            continue
        seen += 1
        if args.limit and changed >= args.limit:
            break
        try:
            art = json.load(open(sj))
        except Exception:
            failed += 1
            continue
        # A container's own metadata describes the bound issue, not a
        # paper; its children carry the papers and are refreshed on their
        # own terms.
        if art.get("container"):
            continue

        fresh = extract(pdfs[0])
        if fresh is None:
            failed += 1
            print(f"  !! {doc}: extraction failed")
            continue

        old = art.get("metadata") or {}
        diffs = {k: (old.get(k), fresh.get(k)) for k in FIELDS
                 if fresh.get(k) and old.get(k) != fresh.get(k)}
        if not diffs:
            continue
        changed += 1
        for k, (a, b) in diffs.items():
            if k in ("abstract", "arxiv", "doi"):
                continue
            print(f"  {doc}")
            print(f"     {k}: {str(a)[:88]}")
            print(f"     {'':>{len(k)}}  -> {str(b)[:88]}")

        if args.apply:
            md = dict(old)
            for k, (a, b) in diffs.items():
                if k == "title" and a:
                    md["title_prev"] = a
                md[k] = b
            art["metadata"] = md
            json.dump(art, open(sj, "w"), indent=1, ensure_ascii=False)

    print(f"\n{seen} documents, {changed} with changed metadata, {failed} failed")
    if not args.apply:
        print("dry run — re-run with --apply")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
