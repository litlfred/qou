#!/usr/bin/env python3
"""Seed the source-ledger join by matching upload titles to references.ts.

The source-ledger indexer
(``folio-assistant/content/pipeline/source-ledger-index.ts``) resolves an
upload to a reference when the *filename* carries an arXiv id.  Most of the
corpus does not: books, journal PDFs, and pre-arXiv scans arrive under
opaque names.  This helper reads the first page of each document and reports
which ``references.ts`` titles appear verbatim in it, so the indexer can seed
those joins instead of leaving them for an agent to rediscover.

It is an **accelerator, not an authority**.  A match is only seeded when it is
unambiguous (exactly one candidate), and the relevance triage confirms the
identification when it reads the document.  Nothing here writes bibliographic
metadata: the output is a ``{filename: [refId, ...]}`` map of pointers.

Usage::

    python3 scripts/extract-upload-titles.py                 # report
    python3 scripts/extract-upload-titles.py -o matches.json

    bun run folio-assistant/content/pipeline/source-ledger-index.ts \\
        --write --matches matches.json

Requires ``pypdf``.  Documents with no text layer (scans) are reported so
they can be routed to a vision pass rather than silently skipped.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
import warnings

# pypdf is noisy about malformed xref tables in older arXiv PDFs; the text
# extraction succeeds regardless.
warnings.filterwarnings("ignore")

REFERENCES = "content/schema/references.ts"
UPLOADS_GLOB = "library/*"
SOURCE_EXT = (".pdf",)

# A title shorter than this matches too loosely to be evidence of identity
# ("Knots", "Introduction").
MIN_TITLE_CHARS = 18


def normalise(text: str) -> str:
    """Fold text to a comparable form: lower-case, alphanumerics, single spaces.

    PDF extraction inserts hyphenation, ligatures, and line breaks at
    unpredictable points; collapsing to alphanumeric tokens makes a title
    match survive them.
    """
    text = text.replace('\\"', '"')
    text = re.sub(r"[^a-z0-9]+", " ", text.lower())
    return re.sub(r"\s+", " ", text).strip()


def parse_references(path: str) -> list[tuple[str, str]]:
    """Return ``(id, title)`` for every ``ref()`` entry."""
    src = open(path, encoding="utf-8").read()
    out: list[tuple[str, str]] = []
    for m in re.finditer(r"ref\(\{(.*?)\n\s*\}\)", src, re.S):
        body = m.group(1)
        rid = re.search(r'\bid:\s*"([^"]+)"', body)
        title = re.search(r'\n\s*title:\s*"((?:[^"\\]|\\.)*)"', body)
        if rid:
            out.append((rid.group(1), title.group(1) if title else ""))
    return out


def first_page_text(path: str) -> tuple[str, str | None]:
    """Return ``(text, error)`` for the document's front matter.

    Title-bearing front matter is on page 1 for papers; a couple of pages of
    slack covers books with a half-title.
    """
    from pypdf import PdfReader

    try:
        reader = PdfReader(path)
        meta_title = ""
        try:
            raw = (reader.metadata or {}).get("/Title")
            if raw:
                meta_title = str(raw)
        except Exception:
            pass
        pages = [(p.extract_text() or "") for p in reader.pages[:2]]
        return f"{meta_title} {' '.join(pages)}", None
    except Exception as exc:  # a corrupt upload must not stop the sweep
        return "", str(exc)[:200]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("-o", "--out", help="write the match map as JSON")
    ap.add_argument("--repo-root", default=".", help="qou checkout root")
    args = ap.parse_args()

    os.chdir(args.repo_root)
    refs = [(rid, normalise(t)) for rid, t in parse_references(REFERENCES)]
    refs = [(rid, t) for rid, t in refs if len(t) >= MIN_TITLE_CHARS]
    print(f"references with a usable title: {len(refs)}", file=sys.stderr)

    docs = sorted(
        p for p in glob.glob(UPLOADS_GLOB) if p.lower().endswith(SOURCE_EXT)
    )
    matches: dict[str, list[str]] = {}
    scanned: list[str] = []
    failed: list[str] = []

    for i, path in enumerate(docs):
        name = os.path.basename(path)
        text, err = first_page_text(path)
        if err:
            failed.append(f"{name}: {err}")
            continue
        blob = normalise(text)
        if not blob:
            scanned.append(name)
            continue
        hits = [rid for rid, title in refs if title in blob]
        if hits:
            matches[name] = hits
        if i % 50 == 0:
            print(f"  ... {i}/{len(docs)}", file=sys.stderr, flush=True)

    unique = {k: v for k, v in matches.items() if len(v) == 1}
    print(f"\ndocuments               : {len(docs)}")
    print(f"  matched (any)         : {len(matches)}")
    print(f"  matched unambiguously : {len(unique)}  <- seeds the join")
    print(f"  no text layer (scans) : {len(scanned)}  <- route to a vision pass")
    print(f"  unreadable            : {len(failed)}")
    for name in scanned:
        print(f"    scan: {name}")
    for line in failed:
        print(f"    fail: {line}")

    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(matches, fh, indent=1, sort_keys=True)
        print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
