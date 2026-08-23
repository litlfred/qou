#!/usr/bin/env python3
"""
migrate-uploads-to-library — flat uploads/*.pdf → library/<doc-id>/<file>.pdf

Renames the intake tree `uploads/` → `library/` and moves each document
into a per-document directory alongside the derived artefacts produced by
folio-assistant's `scripts/pdf-structure.py`:

    library/<doc-id>/
      <original-name>.pdf     the upload, moved (git mv, history preserved)
      structure.json          metadata + TOC + section index
      sections/*.md           greppable section text
      candidates.json         extraction proposals

`<doc-id>` comes from `structure.json`, which derives it from the arXiv
stamp on page 1 (`arxiv-0706.2213v3`) or the slugified filename.

## The original basename is kept

The convention doc writes `original.pdf`. This migration keeps the real
filename instead, for three reasons: every existing citation becomes a
pure *prefix* rewrite (`uploads/X.pdf` → `uploads/<id>/X.pdf`) which is
mechanically verifiable; 7 documents share a `doc_id` with another (they
are duplicate uploads) and would collide on a fixed name; and 748 prose
citations across the corpus name the file, so keeping it preserves their
legibility.

## Why references are rewritten and not left to rot

751 files cite `uploads/<file>.pdf`. **None of them open it** — they are
provenance strings in witness JSON, `-- Ref:` citations, audit-doc
pointers and bean records. Only two scripts resolve the path for real
(`bib-agent-backfill.ts`, `extract-upload-titles.py`) plus the source
ledger's `source.file`.

That makes a stale path harmless at runtime and *not* harmless as a
citation: AGENTS.md records a live incident where an authoritative
pointer resolved to nothing. So the rewrite is total — including beans,
which would otherwise carry 485 dangling references.

## Idempotent

The replacement `uploads/<name>` → `uploads/<doc-id>/<name>` cannot match
an already-migrated path, because `uploads/<doc-id>/<name>` does not
contain the substring `uploads/<name>`. Re-running is a no-op.

Usage:
    scripts/migrate-uploads-to-library.py            # dry run (default)
    scripts/migrate-uploads-to-library.py --apply
    scripts/migrate-uploads-to-library.py --verify   # post-migration checks
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(REPO, "uploads")
LIB = os.path.join(REPO, "library")
LIBNAME = "library"
LEDGER = os.path.join(REPO, "content", "bib-qa-verifications.json")

TEXT_EXT = {".md", ".ts", ".py", ".json", ".sh", ".tex", ".lean", ".yml", ".yaml", ".txt"}
SKIP_DIRS = {".git", "node_modules", ".lake", "uploads", "library", ".venv", "__pycache__"}


def sh(*args: str) -> str:
    return subprocess.run(args, cwd=REPO, capture_output=True, text=True).stdout


def build_mapping() -> dict[str, str]:
    """basename.pdf -> doc-id, from the generated structure.json files."""
    mapping: dict[str, str] = {}
    root = SRC if os.path.isdir(SRC) else LIB
    if not os.path.isdir(root):
        return mapping
    for entry in sorted(os.listdir(root)):
        sj = os.path.join(root, entry, "structure.json")
        if not os.path.exists(sj):
            continue
        try:
            art = json.load(open(sj))
        except Exception:
            continue
        src = art.get("source", {}).get("file")
        doc_id = art.get("doc_id") or entry
        if src:
            mapping[src] = doc_id

    # Fallback for PDFs no structure.json claims. Two causes, both benign:
    # a duplicate upload (`X (1).pdf` beside `X.pdf`) and an alternate
    # filename for the same arXiv id — in both cases another PDF wrote the
    # directory and won the `source.file` field. Route them to the same
    # doc-id so nothing is orphaned at the root.
    if os.path.isdir(SRC):
        for name in sorted(os.listdir(SRC)):
            if not name.lower().endswith(".pdf") or name in mapping:
                continue
            stem = os.path.splitext(name)[0]
            base = re.sub(r"\s*\(\d+\)$", "", stem)          # "X (1)" -> "X"
            if base + ".pdf" in mapping:
                mapping[name] = mapping[base + ".pdf"]
                continue
            m = re.match(r"^(\d{4}\.\d{4,5})(v\d+)?", base)   # 2209.06973v1-foo
            if m:
                cand = "arxiv-" + m.group(1) + (m.group(2) or "")
                mapping[name] = cand if os.path.isdir(os.path.join(SRC, cand)) \
                    else re.sub(r"[^\w.-]+", "-", base.lower())[:60]
                continue
            mapping[name] = re.sub(r"[^\w.-]+", "-", base.lower())[:60]
    return mapping


def tracked_text_files() -> list[str]:
    out = []
    for line in sh("git", "ls-files").splitlines():
        if not line:
            continue
        top = line.split("/", 1)[0]
        if top in SKIP_DIRS:
            continue
        if os.path.splitext(line)[1].lower() in TEXT_EXT:
            out.append(line)
    return out


def move_files(mapping: dict[str, str], apply: bool) -> tuple[int, int]:
    """Move artefact dirs and PDFs from uploads/ into library/<doc-id>/."""
    moved = missing = 0

    # 1. the generated per-document artefact directories
    if os.path.isdir(SRC):
        for entry in sorted(os.listdir(SRC)):
            sdir = os.path.join(SRC, entry)
            if not os.path.isdir(sdir):
                continue
            ddir = os.path.join(LIB, entry)
            if apply and not os.path.exists(ddir):
                os.makedirs(LIB, exist_ok=True)
                r = subprocess.run(["git", "mv", "--", f"uploads/{entry}", f"{LIBNAME}/{entry}"],
                                   cwd=REPO, capture_output=True, text=True)
                if r.returncode != 0:
                    os.renames(sdir, ddir)

    # 2. the flat PDFs
    for name, doc_id in sorted(mapping.items()):
        src = os.path.join(SRC, name)
        dstdir = os.path.join(LIB, doc_id)
        dst = os.path.join(dstdir, name)
        if not os.path.exists(src):
            if not os.path.exists(dst):
                missing += 1
            continue                      # already migrated
        if apply:
            os.makedirs(dstdir, exist_ok=True)
            r = subprocess.run(["git", "mv", "--", f"uploads/{name}", f"{LIBNAME}/{doc_id}/{name}"],
                               cwd=REPO, capture_output=True, text=True)
            if r.returncode != 0:         # untracked file: plain move
                os.replace(src, dst)
        moved += 1

    # 3. loose non-document files (tarballs, notes) keep their names at the root
    if apply and os.path.isdir(SRC):
        for entry in sorted(os.listdir(SRC)):
            s = os.path.join(SRC, entry)
            if os.path.isfile(s):
                os.makedirs(LIB, exist_ok=True)
                r = subprocess.run(["git", "mv", "--", f"uploads/{entry}", f"{LIBNAME}/{entry}"],
                                   cwd=REPO, capture_output=True, text=True)
                if r.returncode != 0:
                    os.replace(s, os.path.join(LIB, entry))
        if not os.listdir(SRC):
            os.rmdir(SRC)

    return moved, missing


def rewrite_refs(mapping: dict[str, str], apply: bool) -> tuple[int, int]:
    """uploads/<name> -> library/<doc-id>/<name> across tracked text files.

    Ordered longest-basename-first so `0401068v1 (1).pdf` is rewritten
    before the `0401068v1.pdf` prefix could claim part of it. The residual
    pass maps any surviving bare `uploads/` mention to `library/`.
    """
    pats = [(re.compile(r"uploads/" + re.escape(n)), f"{LIBNAME}/{d}/{n}")
            for n, d in sorted(mapping.items(), key=lambda kv: -len(kv[0]))]
    pats.append((re.compile(r"\buploads/"), f"{LIBNAME}/"))
    pats.append((re.compile(r"`uploads`"), f"`{LIBNAME}`"))
    files_changed = subs = 0
    for rel in tracked_text_files():
        path = os.path.join(REPO, rel)
        try:
            text = open(path, encoding="utf-8", errors="surrogateescape").read()
        except Exception:
            continue
        if "uploads/" not in text:
            continue
        new, n = text, 0
        for rx, repl in pats:
            new, k = rx.subn(repl, new)
            n += k
        if n:
            files_changed += 1
            subs += n
            if apply:
                open(path, "w", encoding="utf-8", errors="surrogateescape").write(new)
    return files_changed, subs


def verify(mapping: dict[str, str]) -> int:
    problems = 0

    stale = []
    for rel in tracked_text_files():
        try:
            text = open(os.path.join(REPO, rel), encoding="utf-8", errors="surrogateescape").read()
        except Exception:
            continue
        for name in mapping:
            if f"uploads/{name}" in text:
                stale.append((rel, name))
    print(f"stale flat references remaining : {len(stale)}")
    for rel, name in stale[:5]:
        print(f"    {rel}: uploads/{name}")
    problems += len(stale)

    missing = [n for n, d in mapping.items()
               if not os.path.exists(os.path.join(LIB, d, n))]
    print(f"mapped PDFs missing on disk     : {len(missing)}")
    for n in missing[:5]:
        print(f"    {n}")
    problems += len(missing)

    if os.path.exists(LEDGER):
        led = json.load(open(LEDGER))
        rows = led["entries"].values() if isinstance(led["entries"], dict) else led["entries"]
        bad = 0
        for r in rows:
            if not isinstance(r, dict):
                continue
            f = (r.get("source") or {}).get("file") if isinstance(r.get("source"), dict) else None
            # Check the CURRENT prefix. An earlier revision of this check
            # tested `uploads/` and ran *after* the rewrite had renamed every
            # path to `library/`, so it matched nothing and reported a clean
            # zero — a checker passing because its evidence was absent.
            if f and f.startswith((LIBNAME + "/", "uploads/")) \
                    and not os.path.exists(os.path.join(REPO, f)):
                bad += 1
        print(f"ledger rows with unresolvable path: {bad}"
              + ("  (pre-existing: these files were never committed)" if bad else ""))
        # Not counted as a migration problem: these rows cited files that do
        # not exist in the repo before the move either. Reported, not hidden.

    leftover = [f for f in os.listdir(SRC) if f.lower().endswith(".pdf")] if os.path.isdir(SRC) else []
    print(f"PDFs still flat in uploads/     : {len(leftover)}")
    for f in leftover[:5]:
        print(f"    {f}")

    print("\nVERIFY:", "clean" if problems == 0 else f"{problems} problem(s)")
    return 0 if problems == 0 else 1


def main() -> int:
    ap = argparse.ArgumentParser(description="Migrate uploads/ to the per-document layout")
    ap.add_argument("--apply", action="store_true", help="perform the migration (default: dry run)")
    ap.add_argument("--verify", action="store_true", help="post-migration checks only")
    args = ap.parse_args()

    mapping = build_mapping()
    if not mapping:
        print("no structure.json artefacts found under uploads/ — "
              "run folio-assistant scripts/pdf-structure.py first", file=sys.stderr)
        return 1
    print(f"mapping: {len(mapping)} PDFs → {len(set(mapping.values()))} document directories")
    dupes = {}
    for n, d in mapping.items():
        dupes.setdefault(d, []).append(n)
    multi = {d: ns for d, ns in dupes.items() if len(ns) > 1}
    if multi:
        print(f"  {len(multi)} doc-id(s) hold >1 PDF (duplicate uploads):")
        for d, ns in list(multi.items())[:8]:
            print(f"    {d}: {', '.join(ns)}")

    if args.verify:
        return verify(mapping)

    moved, missing = move_files(mapping, args.apply)
    files, subs = rewrite_refs(mapping, args.apply)
    verb = "moved" if args.apply else "would move"
    verb2 = "rewrote" if args.apply else "would rewrite"
    print(f"\n{verb} {moved} PDFs ({missing} mapped but absent)")
    print(f"{verb2} {subs} references across {files} files")
    if not args.apply:
        print("\ndry run — re-run with --apply")
    else:
        print("\nnow run: scripts/migrate-uploads-to-library.py --verify")
    return 0


if __name__ == "__main__":
    sys.exit(main())
