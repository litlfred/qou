#!/usr/bin/env python3
"""split-pdf-by-chapter.py — Post-process main.pdf into per-chapter PDFs.

Reads top-level outline (bookmarks) from a compiled main.pdf and slices
the document into smaller per-chapter PDFs, plus a bundled front-matter
PDF (front matter + notation + glossary + index).

Per-appendix PDFs are produced upstream by direct `pdflatex` of
`standalone-*.tex` files and are NOT touched by this script.

Usage:
    python3 scripts/split-pdf-by-chapter.py [--pdf main.pdf]
                                            [--paper <dir>]
                                            [--out-dir <dir>]
                                            [--front-matter-name front-matter]
                                            [--manifest <chapters>.json]

Chapter list is taken from the paper manifest
(`content/<paper>/<paper>.ts`). The order of bookmarks in the PDF is
assumed to match the chapter order in the manifest, **after excluding**
any chapters marked as appendices (their PDFs are produced standalone).

Front matter chapters (introduction, notation, glossary,
index-of-definitions) are merged into a single front-matter PDF per
the user's request "one for the front matter, glossary, notation,
index".

Outputs (in --out-dir, default = current directory):
    <slug>.pdf                   — one per main chapter
    front-matter.pdf             — bundled front matter + notation + glossary + index
    pdf-split-manifest.json      — machine-readable list of outputs

Exit codes:
    0  success
    1  manifest / PDF inconsistency (chapter count mismatch, etc.)
    2  pypdf import or file-not-found errors
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    print("ERROR: pypdf not installed. Install with: pip install pypdf", file=sys.stderr)
    sys.exit(2)


# Chapter slugs bundled into front-matter.pdf rather than as standalone PDFs.
# Membership-only set: the actual page order in front-matter.pdf is determined
# by the PDF bookmark traversal in `ranges` (whatever order the chapters
# appear in main.pdf), not by this constant.
FRONT_MATTER_GROUP: frozenset[str] = frozenset({
    "introduction",
    "notation",
    "glossary",
    "index-of-definitions",
})


def parse_chapter_list(manifest_path: Path) -> list[str]:
    """Extract ordered list of chapter directories from the paper manifest."""
    src = manifest_path.read_text()
    # Match chapterRef({ dir: "..." }) in source order.
    return [m.group(1) for m in re.finditer(r'chapterRef\(\s*\{\s*dir:\s*["\']([^"\']+)["\']', src)]


def parse_appendix_dirs(manifest_path: Path) -> set[str]:
    """Heuristic: any chapter dir starting with 'appendix-' is an appendix."""
    return {dir for dir in parse_chapter_list(manifest_path) if dir.startswith("appendix-")}


def collect_top_level_bookmarks(reader: PdfReader) -> list[tuple[str, int]]:
    """Return [(title, start_page_0idx), ...] for top-level outline entries."""
    out = []

    def walk(items, depth=0):
        # pypdf outline: list where nested lists are children of the prior entry.
        for item in items:
            if isinstance(item, list):
                # children of previous entry — skip; we only want top-level chapters
                continue
            # item has .title and is a Destination
            title = getattr(item, "title", None) or "(untitled)"
            try:
                page = reader.get_destination_page_number(item)
            except Exception:
                page = None
            if page is not None and depth == 0:
                out.append((title, page))

    walk(reader.outline, depth=0)
    return out


def slice_pdf(reader: PdfReader, start_page: int, end_page: int, dest: Path) -> None:
    """Write pages [start_page, end_page) of reader to dest (0-indexed, exclusive end)."""
    writer = PdfWriter()
    for i in range(start_page, end_page):
        writer.add_page(reader.pages[i])
    # Preserve PDF metadata
    if reader.metadata:
        writer.add_metadata({k: v for k, v in reader.metadata.items() if v is not None})
    with open(dest, "wb") as f:
        writer.write(f)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--pdf", default="main.pdf", help="path to compiled main.pdf")
    ap.add_argument("--paper", default="quantum-observable-universe",
                    help="paper directory under content/")
    ap.add_argument("--out-dir", default=".", help="output directory")
    ap.add_argument("--front-matter-name", default="front-matter",
                    help="basename for the bundled front-matter PDF (no .pdf suffix)")
    ap.add_argument("--manifest", default=None,
                    help="override path to paper manifest (.ts)")
    args = ap.parse_args()

    pdf_path = Path(args.pdf)
    if not pdf_path.exists():
        print(f"ERROR: PDF not found: {pdf_path}", file=sys.stderr)
        return 2

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    repo_root = Path(__file__).resolve().parent.parent
    manifest_path = Path(args.manifest) if args.manifest else \
        repo_root / "content" / args.paper / f"{args.paper}.ts"
    if not manifest_path.exists():
        print(f"ERROR: paper manifest not found: {manifest_path}", file=sys.stderr)
        return 2

    all_chapters = parse_chapter_list(manifest_path)
    appendix_dirs = parse_appendix_dirs(manifest_path)
    # The main.pdf has every chapter EXCEPT appendices (those are standalone).
    main_chapters_in_order = [c for c in all_chapters if c not in appendix_dirs]

    if not main_chapters_in_order:
        print("ERROR: no chapters found in manifest", file=sys.stderr)
        return 1

    print(f"Loading {pdf_path}...")
    reader = PdfReader(str(pdf_path))
    total_pages = len(reader.pages)
    print(f"  {total_pages} pages total")

    bookmarks = collect_top_level_bookmarks(reader)
    print(f"  {len(bookmarks)} top-level bookmarks")

    # Hard fail: no bookmarks means the PDF has no outline (hyperref missing
    # or compile produced unbookmarked output). Silently emitting zero
    # outputs would let CI publish a broken paper without chapter PDFs.
    if not bookmarks:
        print("ERROR: main.pdf has no top-level bookmarks — cannot split. "
              "Ensure hyperref is loaded and \\chapter{...} commands produce "
              "outline entries.", file=sys.stderr)
        return 1

    # Hard fail: count mismatch of more than 2 indicates structural drift
    # (manifest changed, chapters added/removed, or main.pdf was built from
    # a different source). Publishing a misaligned split is worse than
    # publishing nothing.
    drift = abs(len(bookmarks) - len(main_chapters_in_order))
    if drift > 2:
        print(f"ERROR: bookmark count ({len(bookmarks)}) differs from manifest "
              f"main-chapter count ({len(main_chapters_in_order)}) by {drift} "
              "— split would be misaligned. Refusing to publish.", file=sys.stderr)
        return 1

    # Pair bookmarks with chapter slugs by position.
    # If counts mismatch, we use the shorter of the two and warn.
    pairs = list(zip(main_chapters_in_order, bookmarks))
    if len(pairs) < len(bookmarks):
        # extra bookmarks — fall back to slugifying the bookmark title for trailing ones
        for title, page in bookmarks[len(pairs):]:
            slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-") or "untitled"
            pairs.append((slug, (title, page)))

    # Determine page ranges: chapter i spans [start_i, start_{i+1}); last spans to end.
    ranges = []
    for i, (slug, (title, page)) in enumerate(pairs):
        next_page = pairs[i + 1][1][1] if i + 1 < len(pairs) else total_pages
        ranges.append((slug, title, page, next_page))

    # Split: write per-chapter PDFs; collect front-matter chapters for bundling.
    outputs = []
    front_matter_ranges: list[tuple[str, int, int]] = []
    for slug, title, start, end in ranges:
        if slug in FRONT_MATTER_GROUP:
            front_matter_ranges.append((slug, start, end))
            print(f"  [front-matter] {slug}: pages {start + 1}–{end} ({title})")
        else:
            dest = out_dir / f"{slug}.pdf"
            slice_pdf(reader, start, end, dest)
            outputs.append({"slug": slug, "title": title,
                            "pages": [start + 1, end],
                            "path": str(dest.name)})
            print(f"  [chapter]     {slug}: pages {start + 1}–{end} → {dest.name}")

    # Build front-matter bundle.
    # If the front-matter chapters are contiguous (typical: intro+notation at start,
    # glossary+index at end), we may emit two segments. To keep "one PDF" we merge.
    if front_matter_ranges:
        fm_writer = PdfWriter()
        for slug, start, end in front_matter_ranges:
            for i in range(start, end):
                fm_writer.add_page(reader.pages[i])
        # Also include the "front matter" pages before the first bookmark
        # (title page, TOC, abstract, etc.) — pages [0, bookmarks[0].start).
        if ranges:
            first_start = ranges[0][2]
            if first_start > 0:
                # Prepend by building a fresh writer; pypdf does not support insert-at
                # ergonomically, so we rebuild.
                head_writer = PdfWriter()
                for i in range(0, first_start):
                    head_writer.add_page(reader.pages[i])
                for slug, start, end in front_matter_ranges:
                    for i in range(start, end):
                        head_writer.add_page(reader.pages[i])
                fm_writer = head_writer

        fm_dest = out_dir / f"{args.front_matter_name}.pdf"
        if reader.metadata:
            fm_writer.add_metadata({k: v for k, v in reader.metadata.items() if v is not None})
        with open(fm_dest, "wb") as f:
            fm_writer.write(f)
        outputs.append({"slug": args.front_matter_name,
                        "title": "Front matter (introduction, notation, glossary, index)",
                        "pages": None,
                        "path": fm_dest.name,
                        "bundled": [s for s, _, _ in front_matter_ranges]})
        print(f"  [front-matter bundle] → {fm_dest.name} "
              f"(bundles: {', '.join(s for s, _, _ in front_matter_ranges)})")

    # Emit machine-readable manifest.
    manifest_out = out_dir / "pdf-split-manifest.json"
    manifest_out.write_text(json.dumps({
        "pdf": str(pdf_path.name),
        "total_pages": total_pages,
        "outputs": outputs,
    }, indent=2))
    print(f"\nWrote: {manifest_out.name}")
    print(f"Total outputs: {len(outputs)} PDF(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
