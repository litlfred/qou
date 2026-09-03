#!/usr/bin/env python3
"""Check that every `pdf:` path in references.ts resolves on disk.

Why this exists: `content/schema/references.ts` carries 370 `pdf:` fields
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
import pathlib
import re
import sys

REFS = pathlib.Path("content/schema/references.ts")
LIBRARY = pathlib.Path("library")


def dangling_pdf_fields() -> list[str]:
    src = REFS.read_text(encoding="utf-8")
    return [p for p in re.findall(r'pdf:\s*"([^"]+)"', src)
            if not pathlib.Path(p).exists()]


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
    if not REFS.exists():
        print(f"cannot find {REFS} -- run from the repo root", file=sys.stderr)
        return 2

    total = len(re.findall(r'pdf:\s*"[^"]+"', REFS.read_text(encoding="utf-8")))
    dangling = dangling_pdf_fields()
    print(f"references.ts  pdf: fields {total}, dangling {len(dangling)}")
    for p in dangling:
        print(f"  DANGLING  {p}")

    dups = duplicate_pdfs_in_doc_dirs()
    if dups:
        print(f"\nlibrary/  doc-id dirs with byte-identical PDF copies: {len(dups)}")
        print("  (not an error -- but repoint references.ts, the section")
        print("   front-matter and candidates.json together before removing one)")
        for doc, names in dups:
            print(f"  {doc}")
            for n in names:
                print(f"      {n}")

    return 1 if dangling else 0


if __name__ == "__main__":
    sys.exit(main())
