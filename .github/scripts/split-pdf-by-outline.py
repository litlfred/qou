#!/usr/bin/env python3
"""
Split a compiled PDF into smaller PDFs based on top-level outline entries.

Outputs:
- front-matter.pdf (pages before the first structural section)
- notation.pdf / glossary.pdf / index.pdf when matching outline titles
- chapter-XX-<slug>.pdf for non-appendix structural sections
- appendix-<slug>.pdf for appendix sections
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path
from typing import Iterable

from pypdf import PdfReader, PdfWriter


SKIP_TITLE_RE = re.compile(r"^(contents|table of contents|list of figures|list of tables)\b", re.IGNORECASE)
NOTATION_RE = re.compile(r"\bnotation\b", re.IGNORECASE)
GLOSSARY_RE = re.compile(r"\bglossary\b", re.IGNORECASE)
INDEX_RE = re.compile(r"\bindex\b", re.IGNORECASE)
APPENDIX_RE = re.compile(r"\bappendix\b", re.IGNORECASE)


def slugify(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", normalized.strip().lower()).strip("-")
    return slug or "section"


def iter_outline(outline: Iterable, depth: int = 0):
    for item in outline:
        if isinstance(item, list):
            yield from iter_outline(item, depth + 1)
            continue
        yield item, depth


def get_top_level_sections(reader: PdfReader):
    outline = getattr(reader, "outline", [])
    sections: list[tuple[str, int]] = []
    for entry, depth in iter_outline(outline):
        if depth != 0:
            continue
        title = str(getattr(entry, "title", "")).strip()
        if not title:
            continue
        try:
            page_num = reader.get_destination_page_number(entry) + 1  # 1-indexed
        except Exception:
            continue
        sections.append((title, page_num))
    # keep first title for each start page, ordered by page
    ordered: list[tuple[str, int]] = []
    seen_page: set[int] = set()
    for title, page in sorted(sections, key=lambda it: it[1]):
        if page in seen_page:
            continue
        seen_page.add(page)
        ordered.append((title, page))
    return ordered


def write_page_range(reader: PdfReader, start_page: int, end_page: int, out_path: Path):
    writer = PdfWriter()
    for i in range(start_page - 1, end_page):
        writer.add_page(reader.pages[i])
    with out_path.open("wb") as f:
        writer.write(f)


def classify_filename(title: str, chapter_index: int) -> str:
    title_slug = slugify(title)
    if NOTATION_RE.search(title):
        return "notation.pdf"
    if GLOSSARY_RE.search(title):
        return "glossary.pdf"
    if INDEX_RE.search(title):
        return "index.pdf"
    if APPENDIX_RE.search(title):
        return f"appendix-{title_slug}.pdf"
    return f"chapter-{chapter_index:02d}-{title_slug}.pdf"


def main():
    parser = argparse.ArgumentParser(description="Split PDF by top-level outline entries.")
    parser.add_argument("--input", required=True, help="Input PDF path")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    input_pdf = Path(args.input)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    reader = PdfReader(str(input_pdf))
    total_pages = len(reader.pages)
    if total_pages == 0:
        raise SystemExit("Input PDF has no pages.")

    sections = get_top_level_sections(reader)
    structural = [(title, page) for (title, page) in sections if not SKIP_TITLE_RE.search(title)]
    if not structural:
        raise SystemExit("No structural outline entries found to split.")

    first_start = min(page for _, page in structural)
    if first_start > 1:
        write_page_range(reader, 1, first_start - 1, output_dir / "front-matter.pdf")
        print(f"✓ front-matter.pdf (1-{first_start - 1})")

    chapter_idx = 1
    used_names: dict[str, int] = {}
    for i, (title, start_page) in enumerate(structural):
        end_page = structural[i + 1][1] - 1 if i + 1 < len(structural) else total_pages
        if start_page > end_page:
            continue
        filename = classify_filename(title, chapter_idx)
        if filename.startswith("chapter-"):
            chapter_idx += 1
        if filename in used_names:
            used_names[filename] += 1
            stem = filename[:-4]
            filename = f"{stem}-{used_names[filename]}.pdf"
        else:
            used_names[filename] = 1
        write_page_range(reader, start_page, end_page, output_dir / filename)
        print(f"✓ {filename} ({start_page}-{end_page}) [{title}]")


if __name__ == "__main__":
    main()
