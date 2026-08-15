#!/usr/bin/env python3
"""
split-bound-volume — cut a bound journal issue into per-paper documents.

`library-relevance-rank.py` flags documents whose section list carries
three or more Introduction/References headings. Two things produce that
and they want opposite handling: a **thesis** is one coherent work whose
chapters each have their own furniture and must be left alone, while a
**bound journal issue** is several unrelated papers in one file whose
combined relevance score is close to meaningless. This splits the latter.

Boundaries are the **journal masthead** — the line a bound issue reprints
on every paper's title page ("ALGEBRA AND NUMBER THEORY 14:7 (2020)").
See `boundaries()` for why the section outline is the wrong input and how
the masthead is auto-detected.

`--dry-run` is the default and prints each span's DOI and first lines.
**Verify those look like real paper title pages before applying.** That
reporting is what caught the previous, outline-based detector: it placed
every cut in the tail of the preceding paper and found 8 papers where
there are 10.

## Not every flagged document should be split

The flag counts furniture, not authorship. A **thesis** trips it too —
its chapters each carry an Introduction and References — and must be left
alone; splitting one would cut a single coherent work into fragments.
This script refuses anything without a repeating well-separated masthead,
which is the mark of a *published issue*, so a thesis fails the detector
rather than being mangled by it. Run the dry run and read the result.

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
import re
import sys

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    sys.exit("split-bound-volume: needs pypdf — pip install pypdf")

MIN_PAPERS = 3      # fewer repeats than this is not a bound issue
MIN_GAP = 4         # a paper is at least this many pages
RE_DOI = re.compile(r"\b(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+?)(?=[\s,;)\]]|$)")


def page_head(text: str) -> str:
    """Normalised top-of-page line, with digits masked so page numbers
    and volume numbers do not make every masthead unique."""
    head = " ".join(x.strip() for x in text.strip().splitlines()[:2])
    return re.sub(r"\d+", "#", re.sub(r"\s+", " ", head)).strip().lower()[:70]


def boundaries(reader) -> tuple[list[int], list[str | None]]:
    """1-based first page of each paper, plus each paper's DOI if printed.

    Detects the **journal masthead** — the line a bound issue reprints on
    every paper's title page ("ALGEBRA AND NUMBER THEORY 14:7 (2020)").
    That is the only mark that reliably sits at a paper start.

    The previous detector used numbered-`1` "Introduction" sections from
    the PDF outline and was wrong twice over on the volume it was written
    for: it placed cuts in the tail of the preceding paper, and it found
    8 papers where the masthead finds 10 (it missed the papers starting on
    pages 45 and 287 entirely). Section outlines describe a paper's
    interior; they say nothing about where one paper stops being another.

    Auto-detected rather than configured: the masthead is the normalised
    head-line that repeats at least MIN_PAPERS times with every occurrence
    at least MIN_GAP pages from the last. Running heads fail that test —
    they repeat on *consecutive* pages.
    """
    texts = [(p.extract_text() or "") for p in reader.pages]
    heads = [page_head(t) for t in texts]

    by_head: dict[str, list[int]] = {}
    for i, h in enumerate(heads, 1):
        if h:
            by_head.setdefault(h, []).append(i)

    best: list[int] = []
    for h, pages in by_head.items():
        if len(pages) < MIN_PAPERS:
            continue
        if any(b - a < MIN_GAP for a, b in zip(pages, pages[1:])):
            continue                      # a running head, not a masthead
        if len(pages) > len(best):
            best = pages

    if not best:
        return [], []

    # Start the first paper at its own masthead, not at page 1. The issue
    # cover and table of contents are not part of any paper, and absorbing
    # them left the first split with no extractable title — the cover page
    # is not a title page.
    cuts = best[:]
    dois = []
    for i, start in enumerate(cuts):
        doi_page = start
        m = RE_DOI.search(" ".join(texts[doi_page - 1].splitlines()[:6]))
        dois.append(m.group(1).rstrip(".") if m else None)
    return cuts, dois


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

    cuts, dois = boundaries(reader)
    if len(cuts) < 2:
        sys.exit(f"{vol_id}: found {len(cuts)} paper boundaries — not a bound volume, or "
                 "no repeating well-separated masthead line was found")

    spans = []
    for i, start in enumerate(cuts):
        end = (cuts[i + 1] - 1) if i + 1 < len(cuts) else total
        spans.append((start, end))

    print(f"{vol_id}: {total} pages -> {len(spans)} papers")
    for i, (a, b) in enumerate(spans, 1):
        first = (reader.pages[a - 1].extract_text() or "").strip().splitlines()
        head = " ".join(l.strip() for l in first[:6])[:70]
        print(f"  p{i:02d}  pages {a:>4}-{b:<4} ({b - a + 1:>3}pp)  {dois[i-1] or '(no doi)'}")
        print(f"        {head}")
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
