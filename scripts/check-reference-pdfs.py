#!/usr/bin/env python3
"""Check that every `library.pdf` path in the bibliography resolves to a held PDF or processed `library/<doc-id>/` entry.

The entries are `folio/references/<id>.json` since the per-entry split (bean
qou-l7pj); before it they were `pdf:` fields inline in `references.ts`.

Public-release policy (owner ruling 2026-11-24): third-party copyrighted `.pdf`
binaries are removed from `library/`, keeping only works authored/co-authored by
Frederick Leitner (Leitner, Leitner–Pawloski, Foth–Leitner) while preserving
100% of extracted `structure.json`, `summary.json`, `sections/*.md`, `ocr/`, and
`candidates.json` in `library/<doc-id>/`. Accordingly, a `library.pdf` path
`library/<doc-id>/<file>.pdf` resolves cleanly when EITHER:
  1. the `.pdf` binary exists on disk (or in `HEAD` inside a sparse checkout), OR
  2. `library/<doc-id>/` holds processed text/metadata (`sections/`, `ocr/`, or
     `summary.json`) and, if `structure.json` records `source.file`, it matches
     `<file>.pdf`.

Exit 0 clean, 1 on any dangling path or mis-stamped arXiv directory.
"""
from __future__ import annotations

import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
import references_dir  # noqa: E402  -- folio/references/<id>.json (bean qou-l7pj)

REPO = "."
LIBRARY = pathlib.Path("library")


def pdf_fields() -> list[str]:
    """Every entry's `library.pdf`, in bibliography order."""
    return [e["library"]["pdf"] for e in references_dir.entries(REPO)
            if isinstance(e.get("library"), dict) and isinstance(e["library"].get("pdf"), str)]


def _git_tracked_library_paths() -> set[str]:
    """Fallback for sparse checkouts that exclude `library/` on disk."""
    try:
        out = subprocess.check_output(
            ["git", "ls-files", "library/"], cwd=REPO, text=True, stderr=subprocess.DEVNULL
        )
        return set(out.splitlines())
    except Exception:
        return set()


def classify_pdf_fields() -> tuple[list[str], list[str], list[str]]:
    """Classify `library.pdf` fields into `(on_disk_or_tracked_pdf, retired_processed, dangling)`."""
    fields = pdf_fields()
    has_local_lib = LIBRARY.is_dir() and any(p.is_dir() for p in LIBRARY.iterdir())
    tracked = set() if has_local_lib else _git_tracked_library_paths()
    tracked_dirs = {p.split("/")[1] for p in tracked if p.startswith("library/") and p.count("/") >= 2}

    present: list[str] = []
    retired: list[str] = []
    dangling: list[str] = []

    for p in fields:
        if pathlib.Path(p).is_file() or p in tracked:
            present.append(p)
            continue
        m = re.match(r"^library/([^/]+)/([^/]+\.pdf)$", p, re.I)
        if not m:
            dangling.append(p)
            continue
        doc_id, pdf_name = m.group(1), m.group(2)
        if has_local_lib:
            doc_dir = LIBRARY / doc_id
            if not doc_dir.is_dir():
                dangling.append(p)
                continue
            has_derived = (
                (doc_dir / "sections").is_dir()
                or (doc_dir / "ocr").is_dir()
                or (doc_dir / "summary.json").is_file()
            )
            if not has_derived:
                dangling.append(p)
                continue
            sj = doc_dir / "structure.json"
            if sj.is_file():
                try:
                    rec_file = ((json.loads(sj.read_text(encoding="utf-8")).get("source") or {}).get("file"))
                except Exception:
                    rec_file = None
                if rec_file and rec_file != pdf_name:
                    dangling.append(p)
                    continue
            retired.append(p)
        else:
            if doc_id not in tracked_dirs:
                dangling.append(p)
                continue
            has_derived = (
                f"library/{doc_id}/summary.json" in tracked
                or any(tp.startswith(f"library/{doc_id}/sections/") or tp.startswith(f"library/{doc_id}/ocr/")
                       for tp in tracked)
            )
            if has_derived:
                retired.append(p)
            else:
                dangling.append(p)

    return present, retired, dangling


def dangling_pdf_fields() -> list[str]:
    return classify_pdf_fields()[2]


def duplicate_pdfs_in_doc_dirs() -> list[tuple[str, list[str]]]:
    """doc-id dirs holding two or more byte-identical PDFs."""
    out = []
    if not LIBRARY.is_dir():
        return out
    for d in sorted(p for p in LIBRARY.iterdir() if p.is_dir()):
        by_hash: dict[str, list[str]] = {}
        for pdf in sorted(d.glob("*.pdf")):
            h = hashlib.sha256(pdf.read_bytes()).hexdigest()
            by_hash.setdefault(h, []).append(pdf.name)
        for names in by_hash.values():
            if len(names) > 1:
                out.append((d.name, names))
    return out


def mismatched_arxiv_doc_dirs() -> list[tuple[str, str]]:
    """`library/arxiv-<X>/` holding `<YYYY.NNNNN>[vN].pdf` (or `structure.json` `source.file`) where `<YYYY.NNNNN> != <X>` (bean qou-7t9z)."""
    out = []
    if not LIBRARY.is_dir():
        return out
    for d in sorted(p for p in LIBRARY.iterdir() if p.is_dir() and p.name.startswith("arxiv-")):
        dir_base = re.sub(r"v\d+$", "", d.name[len("arxiv-"):])
        candidates = [pdf.name for pdf in sorted(d.glob("*.pdf"))]
        sj = d / "structure.json"
        if sj.is_file():
            try:
                sf = ((json.loads(sj.read_text(encoding="utf-8")).get("source") or {}).get("file"))
                if isinstance(sf, str) and sf not in candidates:
                    candidates.append(sf)
            except Exception:
                pass
        for pdf_name in candidates:
            m = re.match(r"^(\d{4}\.\d{4,5})(?:v\d+)?\.pdf$", pdf_name)
            if m and m.group(1) != dir_base:
                out.append((d.name, pdf_name))
    return out


def main() -> int:
    if not os.path.isdir(references_dir.references_dir(REPO)):
        print("cannot find folio/references/ -- run from the repo root", file=sys.stderr)
        return 2

    present, retired, dangling = classify_pdf_fields()
    total = len(present) + len(retired) + len(dangling)
    print(
        f"folio/references  library.pdf fields {total} "
        f"(PDF present: {len(present)}, PDF-retired processed dir: {len(retired)}, dangling: {len(dangling)})"
    )
    for p in dangling:
        print(f"  DANGLING  {p}")

    misstamped = mismatched_arxiv_doc_dirs()
    if misstamped:
        print(f"\nlibrary/  arxiv-<X>/ dirs with mismatched arXiv PDF stem: {len(misstamped)}")
        for doc, pdf_name in misstamped:
            print(f"  MISSTAMPED  library/{doc}/{pdf_name}")

    dups = duplicate_pdfs_in_doc_dirs()
    if dups:
        print(f"\nlibrary/  doc-id dirs with byte-identical PDF copies: {len(dups)}")
        print("  (not an error -- but repoint the entry's library.pdf, the section")
        print("   front-matter and candidates.json together before removing one)")
        for doc, names in dups:
            print(f"  {doc}")
            for n in names:
                print(f"      {n}")

    return 1 if (dangling or misstamped) else 0


if __name__ == "__main__":
    sys.exit(main())
