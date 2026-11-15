#!/usr/bin/env python3
"""Check that every `library.pdf` path in the bibliography resolves on disk.

The entries are `folio/references/<id>.json` since the per-entry split (bean
qou-l7pj); before it they were `pdf:` fields inline in `references.ts`.

Why this exists: `folio/schema/references.ts` carries 370 `pdf:` fields
pointing into `library/`, and nothing validated them. A bibliography entry
whose PDF has been renamed or tidied away fails silently -- the entry still
renders, the citation still resolves, and only someone opening the file finds
out. The failure mode is invisible precisely because the bibliography is
correct in every other respect.

It bit during the 2026-08-25 duplicate-PDF tidy: seven `library/` PDFs existed
in byte-identical pairs, and in six of the seven the bibliography pointed at
the *odd* name (a browser ` (1).pdf` re-download, or a long descriptive
download name) while the section index pointed at the clean arXiv-id name.
Deleting "the redundant copy" on filename appearance alone would have broken
six live bibliography entries.

Also checks the reverse direction: a `library/<doc-id>/` holding more than one
PDF is either a genuine multi-file document or an untidied duplicate, and the
second is worth surfacing.

Exit 0 clean, 1 on any dangling path.
"""
from __future__ import annotations

import hashlib
import os
import pathlib
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
import references_dir  # noqa: E402  -- folio/references/<id>.json (bean qou-l7pj)

REPO = "."
LIBRARY = pathlib.Path("library")


def pdf_fields() -> list[str]:
    """Every entry's `library.pdf`, in bibliography order."""
    return [e["library"]["pdf"] for e in references_dir.entries(REPO)
            if isinstance(e.get("library"), dict) and isinstance(e["library"].get("pdf"), str)]


def dangling_pdf_fields() -> list[str]:
    return [p for p in pdf_fields() if not pathlib.Path(p).exists()]


def duplicate_pdfs_in_doc_dirs() -> list[tuple[str, list[str]]]:
    """doc-id dirs holding two or more byte-identical PDFs."""
    out = []
    for d in sorted(p for p in LIBRARY.iterdir() if p.is_dir()):
        by_hash: dict[str, list[str]] = {}
        for pdf in sorted(d.glob("*.pdf")):
            h = hashlib.sha256(pdf.read_bytes()).hexdigest()
            by_hash.setdefault(h, []).append(pdf.name)
        for names in by_hash.values():
            if len(names) > 1:
                out.append((d.name, names))
    return out


def main() -> int:
    if not os.path.isdir(references_dir.references_dir(REPO)):
        print("cannot find folio/references/ -- run from the repo root", file=sys.stderr)
        return 2

    total = len(pdf_fields())
    dangling = dangling_pdf_fields()
    print(f"folio/references  library.pdf fields {total}, dangling {len(dangling)}")
    for p in dangling:
        print(f"  DANGLING  {p}")

    dups = duplicate_pdfs_in_doc_dirs()
    if dups:
        print(f"\nlibrary/  doc-id dirs with byte-identical PDF copies: {len(dups)}")
        print("  (not an error -- but repoint the entry's library.pdf, the section")
        print("   front-matter and candidates.json together before removing one)")
        for doc, names in dups:
            print(f"  {doc}")
            for n in names:
                print(f"      {n}")

    return 1 if dangling else 0


if __name__ == "__main__":
    sys.exit(main())
