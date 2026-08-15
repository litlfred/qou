#!/usr/bin/env python3
"""
split-bound-volume — cut a bound journal issue into per-paper documents.

`library-relevance-rank.py` flags documents whose section list carries
three or more Introduction/References headings. Two things produce that
and they want opposite handling: a **thesis** is one coherent work whose
chapters each have their own furniture and must be left alone, while a
**bound journal issue** is several unrelated papers in one file whose
combined relevance score is close to meaningless. This splits the latter.

Boundaries are the sections numbered `1` whose title begins
"Introduction". Each paper is cut two pages earlier than its Introduction
so it keeps its own title page; the first paper absorbs the issue's front
matter.

## STATUS: the heuristic does not work on the volume it was written for

Dry-run on `ant-v14-n7-s` (Algebra & Number Theory 14:7, 336pp) finds 8
boundaries — the right *count* for that issue — but each cut lands in the
tail of the preceding paper, not on a title page. Every span's first page
carries the previous paper's running head and its References ("Elliptic
curves over totally real cubic fields are modular 1799 References [A…").
So the numbered-`1` "Introduction" sections in this volume's PDF outline
are not positioned where a paper starts, and `LOOKBACK` cannot fix a
boundary that is wrong by a variable amount.

**Do not `--apply` this to a journal issue until the detector is
replaced.** A better signal is the journal's own continuous pagination:
the running head changes at a true paper boundary, and the printed page
numbers (1789, 1799, 1851, 1909, 1979 in this issue) jump at exactly
those points. Detecting the running-head change is the fix; the section
outline is the wrong input.

This file is kept because the dry-run *reporting* is what caught it, and
because the container-marking half is correct and reusable. `--dry-run`
is the default for exactly this reason — **verify the emitted titles**
before trusting any split.

Output, per paper:

    library/<volume-id>-p<NN>/<volume-id>-p<NN>.pdf

Then re-run folio-assistant's `pdf-structure.py` and
`extract-candidates.py` over the new directories.

The volume directory is kept and marked `container: true` in its
`structure.json`, so the ranking skips it instead of double-counting the
same pages under both the volume and its children. It stays the source of
record: the split PDFs are derived, the issue as published is not.

Usage:
    scripts/split-bound-volume.py library/ant-v14-n7-s
    scripts/split-bound-volume.py library/ant-v14-n7-s --apply
"""

from __future__ import annotations

import argparse
import json
import os
import sys

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    sys.exit("split-bound-volume: needs pypdf — pip install pypdf")

LOOKBACK = 2   # pages of title-page headroom before a paper's Introduction


def boundaries(art: dict) -> list[int]:
    """1-based first pages of each paper."""
    starts = [
        s["page_start"]
        for s in art.get("sections", [])
        if s.get("number") == "1" and (s.get("title") or "").lower().startswith("introduction")
    ]
    cut = []
    for i, p in enumerate(sorted(set(starts))):
        cut.append(1 if i == 0 else max(1, p - LOOKBACK))
    return cut


def main() -> int:
    ap = argparse.ArgumentParser(description="Split a bound journal issue into per-paper documents")
    ap.add_argument("voldir")
    ap.add_argument("--apply", action="store_true", help="write the split PDFs (default: dry run)")
    args = ap.parse_args()

    voldir = args.voldir.rstrip("/")
    vol_id = os.path.basename(voldir)
    sj = os.path.join(voldir, "structure.json")
    if not os.path.exists(sj):
        sys.exit(f"no structure.json in {voldir}")
    art = json.load(open(sj))

    pdfs = [f for f in os.listdir(voldir) if f.lower().endswith(".pdf")]
    if not pdfs:
        sys.exit(f"no PDF in {voldir}")
    reader = PdfReader(os.path.join(voldir, pdfs[0]))
    total = len(reader.pages)

    cuts = boundaries(art)
    if len(cuts) < 2:
        sys.exit(f"{vol_id}: found {len(cuts)} paper boundaries — not a bound volume, or "
                 "the Introduction headings are not numbered `1`")

    spans = []
    for i, start in enumerate(cuts):
        end = (cuts[i + 1] - 1) if i + 1 < len(cuts) else total
        spans.append((start, end))

    print(f"{vol_id}: {total} pages -> {len(spans)} papers")
    for i, (a, b) in enumerate(spans, 1):
        first = (reader.pages[a - 1].extract_text() or "").strip().splitlines()
        head = " ".join(l.strip() for l in first[:4])[:76]
        print(f"  p{i:02d}  pages {a:>4}-{b:<4} ({b - a + 1:>3}pp)  {head}")
        if args.apply:
            out_id = f"{vol_id}-p{i:02d}"
            out_dir = os.path.join(os.path.dirname(voldir), out_id)
            os.makedirs(out_dir, exist_ok=True)
            w = PdfWriter()
            for p in range(a - 1, b):
                w.add_page(reader.pages[p])
            with open(os.path.join(out_dir, f"{out_id}.pdf"), "wb") as fh:
                w.write(fh)

    if args.apply:
        art["container"] = True
        art["container_children"] = [f"{vol_id}-p{i:02d}" for i in range(1, len(spans) + 1)]
        art["container_note"] = (
            "Bound journal issue. The per-paper documents listed in "
            "`container_children` carry the content; this directory keeps the "
            "issue as published and is skipped by ranking so the same pages are "
            "not counted twice."
        )
        json.dump(art, open(sj, "w"), indent=1)
        # The volume's own derived text now duplicates its children.
        for junk in ("candidates.json",):
            p = os.path.join(voldir, junk)
            if os.path.exists(p):
                os.remove(p)
        print(f"\nwrote {len(spans)} papers; marked {vol_id} as a container")
        print("now re-run pdf-structure.py + extract-candidates.py on the new dirs")
    else:
        print("\ndry run — verify the titles above look like real papers, then --apply")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
