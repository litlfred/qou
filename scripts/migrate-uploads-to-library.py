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
    scripts/migrate-uploads-to-library.py --selftest # guard regression cases

## The guard: never create a directory the corpus cannot read

A `library/<doc-id>/` holding only a PDF — no `structure.json`, no
`sections/` — is invisible at EVERY tier of the corpus-grep path-5
checklist, so a "has the corpus got this?" check returns clean while
the paper sits on disk. That is worse than not holding it.

This script used to produce them, and the trigger is worth remembering
because it fires when the upstream step behaves CORRECTLY:
`pdf-structure.py` SKIPS an already-held document and emits nothing, so
a skip and a fresh ingest are indistinguishable here. Two changes:

1. the arXiv-id fallback checks BOTH roots, so a skipped document
   resolves to the `arxiv-<id>/` already in library/ instead of to its
   filename slug;
2. anything still unresolved is REFUSED, loudly, with a non-zero exit —
   the PDF stays in the queue for the next ingest.

Bean `qou-cvx9`.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(REPO, "uploads")
LIB = os.path.join(REPO, "library")
LIBNAME = "library"
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
import bib_ledger  # noqa: E402  -- the source ledger's reader (attestation store, legacy fallback)

TEXT_EXT = {".md", ".ts", ".py", ".json", ".sh", ".tex", ".lean", ".yml", ".yaml", ".txt"}
SKIP_DIRS = {".git", "node_modules", ".lake", "uploads", "library", ".venv", "__pycache__"}


def sh(*args: str) -> str:
    return subprocess.run(args, cwd=REPO, capture_output=True, text=True).stdout


def build_mapping() -> dict[str, str]:
    """basename.pdf -> doc-id, from the generated structure.json files."""
    mapping: dict[str, str] = {}
    # BOTH roots, library/ first so a fresh uploads/ entry wins on conflict.
    # Scanning only one root is what made the residual pass necessary: a
    # citation to an ALREADY-migrated PDF (`library/ki6c/ki6c.pdf`) had no doc-id
    # here, fell through to the blanket rewrite, and became the dangling
    # `library/ki6c/ki6c.pdf` instead of `library/<doc-id>/ki6c.pdf`.
    roots = [r for r in (LIB, SRC) if os.path.isdir(r)]
    if not roots:
        return mapping
    for root in roots:
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
                # BOTH roots. Looking only in uploads/ is what PRODUCED the
                # orphans the guard below exists to stop, and the mechanism is
                # worth stating because it fires when the upstream step
                # behaves *correctly*: `pdf-structure.py` SKIPS an
                # already-held document and emits nothing, so the real
                # `arxiv-<id>/` sits in library/ and never appears in
                # uploads/. This check then failed, the filename slug won,
                # and `library/1808.02836v2/` was created beside the real
                # `library/arxiv-1808.02836v2/` — same paper, one copy
                # greppable, one invisible at every tier of corpus-grep
                # path 5. Bean `qou-cvx9`.
                mapping[name] = cand if any(
                    os.path.isdir(os.path.join(r, cand)) for r in (SRC, LIB)) \
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


def has_structure(doc_id: str) -> bool:
    """Does `<doc_id>` name an INGESTED document in either root?

    Both roots, because the two modes disagree about where the artefacts
    are at the moment this is asked: under `--apply` step 1 has already
    moved them into library/, under a dry run they are still in uploads/.
    Checking one root would make the guard mode-dependent, which is how
    the bug it guards got in.
    """
    return any(os.path.exists(os.path.join(r, doc_id, "structure.json"))
               for r in (LIB, SRC))


def move_files(mapping: dict[str, str], apply: bool
               ) -> tuple[int, int, list[tuple[str, str]]]:
    """Move artefact dirs and PDFs from uploads/ into library/<doc-id>/.

    REFUSES to create a `library/<doc-id>/` that holds no `structure.json`.
    Such a directory is a document the corpus has on disk and cannot read:
    no INDEX row (tier 1), no summary.json (tier 2), no sections/ (tier 3),
    no ocr/ (tier 4) — invisible at EVERY tier of the corpus-grep path-5
    checklist, which is strictly worse than not holding the paper at all,
    because a "has the corpus got this?" check comes back clean.

    The refusal is the whole point: this step cannot tell a fresh ingest
    from a SKIPPED one (`pdf-structure.py` emits nothing either way), so
    it must not guess a directory name. A loud skip leaves the PDF in the
    intake queue where the next ingest run will find it; a silent move
    buries it. Bean `qou-cvx9`.
    """
    moved = missing = 0
    refused: list[tuple[str, str]] = []

    # 1. the generated per-document artefact directories
    if os.path.isdir(SRC):
        for entry in sorted(os.listdir(SRC)):
            sdir = os.path.join(SRC, entry)
            if not os.path.isdir(sdir):
                continue
            if not os.path.exists(os.path.join(sdir, "structure.json")):
                # Not ingested (e.g. `pdf-ocr.py` ran but `pdf-structure.py`
                # has not). Moving it would plant an unreadable directory in
                # library/; leaving it keeps it in the queue for the ingest.
                refused.append((f"uploads/{entry}/", "directory has no structure.json"))
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
        if not has_structure(doc_id):
            # The doc-id came from the filename fallback and names nothing
            # ingested. Do NOT invent the directory.
            refused.append((f"uploads/{name}",
                            f"target {LIBNAME}/{doc_id}/ has no structure.json"))
            continue
        if apply:
            os.makedirs(dstdir, exist_ok=True)
            r = subprocess.run(["git", "mv", "--", f"uploads/{name}", f"{LIBNAME}/{doc_id}/{name}"],
                               cwd=REPO, capture_output=True, text=True)
            if r.returncode != 0:         # untracked file: plain move
                os.replace(src, dst)
        moved += 1

    # 3. Loose non-document files STAY in uploads/, and uploads/ is never
    # removed. This step used to sweep every loose file to the library root
    # and then rmdir the directory -- correct for the one-time 2026-08-15
    # rename, wrong for every run since. uploads/ is a LIVE intake queue that
    # "stays live for the next drop" (AGENTS.md project-structure table,
    # corrected 2026-08-25); the sweep carried off uploads/.gitignore -- the
    # whitespace placeholder that keeps the empty directory tracked -- so a
    # successful ingest deleted the queue it exists to serve.

    return moved, missing, refused


def _rewrite_patterns(mapping: dict[str, str], live: set[str]):
    """The (regex, replacement) list, restricted to names that RESOLVED.

    Split out of `rewrite_refs` so the resolve-required guard can be tested
    without a git worktree — `rewrite_refs` itself walks `tracked_text_files()`
    and cannot run in the selftest's bare temp dir.
    """
    return [(re.compile(r"uploads/" + re.escape(n)), f"{LIBNAME}/{d}/{n}")
            for n, d in sorted(mapping.items(), key=lambda kv: -len(kv[0]))
            if n in live]


def rewrite_refs(mapping: dict[str, str], apply: bool,
                 live: set[str] | None = None) -> tuple[int, int]:
    """uploads/<name> -> library/<doc-id>/<name> across tracked text files.

    Ordered longest-basename-first so `0401068v1 (1).pdf` is rewritten
    before the `0401068v1.pdf` prefix could claim part of it.

    REQUIRES THE PATH TO RESOLVE (owner ruling 2026-09-13).  `live` is the
    set of basenames that ACTUALLY EXISTED in uploads/ when this run started
    -- i.e. the ones genuinely being migrated now.  Only those are rewritten.

    Why: `build_mapping()` reads every `structure.json` under uploads/ AND
    library/, so the mapping also carries documents migrated in PAST runs,
    whose PDFs are long gone from uploads/ ("3 mapped but absent" in the
    2026-09-13 run).  A `uploads/<that name>` string in the tree is then not
    a live reference at all -- it is PROSE describing the earlier migration,
    and rewriting it corrupts the record.  Measured that day, three files:

      beans/defs/qou-4lbh          "uploads/roth_lemma.pdf ->
                                library/roth-lemma/roth_lemma.pdf"
                                became "library/... -> library/...",
                                an arrow from a thing to itself;
      beans/defs/qou-cvx9          "the first draft wrote `uploads/1808.02836v2.pdf`
                                as a literal" became a claim about a path the
                                draft never wrote -- a FALSIFIED record, which
                                is worse than a dangling link because it is
                                confidently wrong rather than visibly broken;
      scripts/library-orphan-audit.py
                                a docstring quoting git's own output,
                                "R100 uploads/X -> library/Y", became
                                "R100 library/Y -> library/Y", which is not a
                                rename.

    All three are files DESCRIBING THIS MIGRATION -- which is exactly the
    population that legitimately contains `uploads/` paths as history.  So
    the rewriter's blast radius was biased toward its own documentation.

    This is the same lesson as the removed residual pass below, one level in:
    that pass could not tell a citation from a sentence; this one could not
    tell a live reference from a historical one.  `live` is the discriminator
    the file system already knows.
    """
    if live is None:                      # standalone call: rewrite nothing
        live = {n for n in mapping        # we cannot know what was live, so
                if os.path.exists(os.path.join(SRC, n))}   # ask the disk now
    pats = _rewrite_patterns(mapping, live)
    # NO residual `uploads/` -> `library/` pass. It was blanket, and a
    # blanket rewrite cannot tell a citation from a sentence: it turned the
    # AGENTS.md row defining the two stages into "`library/` and `library/`
    # are two stages of one pipeline, not the same directory renamed", ate
    # this file's own docstring, retitled a bean about "un-ingested PDFs in
    # uploads/", and pointed every citation of an already-migrated PDF at a
    # path that does not exist. Measured on the 2026-08-29 ingest: 91 of 219
    # rewritten mentions were prose or dangling, none were repairs the
    # per-basename patterns above had missed. A mention this loop does not
    # match is a mention with no known target -- leave it alone.
    files_changed = subs = 0
    # An `id: null` source-ledger row is FILED BY ITS SOURCE PATH in the
    # attestation store (test/attestations/bib-verification/source/<file>...).
    # Rewriting `source.file` inside it in place would leave the row under a
    # path that no longer names it, and the ledger reader refuses such a file
    # as corrupt. So those files are not rewritten here; they are reported,
    # and the row is re-filed by the platform's ledger writer.
    orphan_prefix = os.path.relpath(
        os.path.join(bib_ledger.attestations_root(REPO), "bib-verification", "source"), REPO) + os.sep
    held_back: list[str] = []
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
        if n and rel.startswith(orphan_prefix):
            held_back.append(rel)
            continue
        if n:
            files_changed += 1
            subs += n
            if apply:
                open(path, "w", encoding="utf-8", errors="surrogateescape").write(new)
    if held_back:
        print(f"source-ledger rows with no reference id naming a moved file: {len(held_back)} "
              "(NOT rewritten: such a row is filed by its path; re-file it with the platform "
              "ledger writer, writeSourceLedger in folio-assistant/cat-harness/schemas/bib-attestations.ts)")
        for rel in held_back[:5]:
            print(f"    {rel}")
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

    # Dangling `library/<file>` citations -- the check the old residual pass
    # made unfalsifiable. "stale flat references remaining: 0" above was
    # guaranteed by construction once every `uploads/` had been renamed, so
    # it reported clean while pointing 128 citations at files that are one
    # directory deeper. This asks the question the other way round: does the
    # path a citation names actually exist? Same failure mode this file's
    # ledger comment already records -- a checker passing because its own
    # action removed the evidence.
    # Split repairable from absent. A gate that is permanently red gets
    # ignored, which is the same end state as one that is unfalsifiable:
    # 45 of these name PDFs that were never committed to the repo at all
    # (the ledger row below counts the same 45), so nothing in this tree
    # can fix them and they are reported, not counted.
    by_basename: dict[str, str] = {}
    if os.path.isdir(LIB):
        for d in os.listdir(LIB):
            dp = os.path.join(LIB, d)
            if os.path.isdir(dp):
                for f in os.listdir(dp):
                    by_basename.setdefault(f, d)

    repairable, absent = [], []
    pat = re.compile(r"\b" + LIBNAME + r"/([A-Za-z0-9][\w.\- ]*\.(?:pdf|tgz|zip))")
    for rel in tracked_text_files():
        try:
            text = open(os.path.join(REPO, rel), encoding="utf-8", errors="surrogateescape").read()
        except Exception:
            continue
        for m in pat.finditer(text):
            n = m.group(1)
            if os.path.exists(os.path.join(LIB, n)):
                continue
            (repairable if n in by_basename else absent).append((rel, n))
    print(f"dangling library/<file>, repairable : {len(repairable)}")
    for rel, n in repairable[:5]:
        print(f"    {rel}: {LIBNAME}/{n} -> {LIBNAME}/{by_basename[n]}/{n}")
    print(f"dangling library/<file>, file absent: {len(absent)}"
          + ("  (pre-existing: never committed)" if absent else ""))
    problems += len(repairable)

    led, note = bib_ledger.read_source_ledger(REPO)
    print(note)
    if led.get("entries"):
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

    # Directories the corpus holds and cannot read. Asked here because the
    # cheapest place to see the orphan class is the same command that must
    # never create one. REPORTED, NOT COUNTED, deliberately: 22 such dirs
    # pre-date the guard (bean `qou-cvx9`), and a gate that is permanently
    # red gets ignored — the same end state as one that is unfalsifiable,
    # which this file's own ledger comment already records the cost of.
    # Once the standing 22 are drained this line reads 0 and the guard above
    # is what keeps it there.
    orphans = sorted(d for d in os.listdir(LIB)
                     if os.path.isdir(os.path.join(LIB, d))
                     and not os.path.exists(os.path.join(LIB, d, "structure.json"))) \
        if os.path.isdir(LIB) else []
    print(f"library/ dirs with no structure.json: {len(orphans)}"
          + ("  (invisible at every tier of corpus-grep path 5)" if orphans else ""))
    for d in orphans[:5]:
        print(f"    {LIBNAME}/{d}/")
    if len(orphans) > 5:
        print(f"    ... and {len(orphans) - 5} more")

    leftover = [f for f in os.listdir(SRC) if f.lower().endswith(".pdf")] if os.path.isdir(SRC) else []
    print(f"PDFs still flat in uploads/     : {len(leftover)}")
    for f in leftover[:5]:
        print(f"    {f}")

    print("\nVERIFY:", "clean" if problems == 0 else f"{problems} problem(s)")
    return 0 if problems == 0 else 1


# --------------------------------------------------------------- selftest

def _mk(path: str, body: str = "") -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(body)


def _selftest() -> int:
    """Six cases from `qou-cvx9`, covering BOTH halves of the fix separately.

    The two halves catch different things and the distinction is easy to
    lose, so each has a case no other case can pass for it:

    * `1808.02836v2.pdf` — the orphan the bean actually measured. Nothing
      for it is ingested **in this working tree** (the sectioned copy was
      on the other branch, which is why `git merge-tree` reported it as
      `rename/rename` rather than as a duplicate). Nothing can recover a
      doc-id here, so the only correct move is to REFUSE — this is the
      case the guard, not the fallback, has to carry.
    * `2108.09349v2.pdf` — held locally as `library/arxiv-2108.09349v2/`,
      but ingested under a DIFFERENT filename, so `build_mapping`'s
      `source.file` loop does not claim it and the arXiv-id fallback runs.
      Measured on main: 226 of 633 `structure.json` carry a `doc_id` that
      is neither the stem nor `arxiv-<stem>`, so this is a third of the
      corpus, not a corner. Only the both-roots fallback recovers it; with
      the uploads-only check it becomes `library/2108.09349v2/`.
    * `0406242v4.pdf` — the bean's negative control. Its OLD-STYLE arXiv id
      yields no `arxiv-` prefix, so both scripts already agreed and it
      landed correctly. A guard that refuses this is over-matching.
    * `fulltext.pdf` — never ingested, and its name carries no arXiv id, so
      no recovery is even conceivable. `fulltext`, `m4-24` and `amc_2730`
      are three of the 22 such directories standing on main.
    * `arxiv-2209.06973v1/` — an ordinary fresh ingest; must still move.
    * `pending-ocr/` — in the queue with OCR text but no `structure.json`.
      Moving it plants an unreadable directory; it belongs in the queue.
    * the resolve-required rewrite — a mapping entry whose PDF is no longer
      in uploads/ must contribute NO rewrite pattern, and the both-live case
      must still produce two, so a guard that refuses everything fails.
    """
    global REPO, SRC, LIB
    keep = (REPO, SRC, LIB)
    tmp = tempfile.mkdtemp(prefix="_migrate_selftest_")
    ok = True
    try:
        REPO, SRC, LIB = tmp, os.path.join(tmp, "uploads"), os.path.join(tmp, "library")

        def sj(root, doc_id, srcfile):
            _mk(os.path.join(root, doc_id, "structure.json"),
                json.dumps({"doc_id": doc_id, "source": {"file": srcfile}}))

        # the measured orphan: nothing ingested for it in this tree
        _mk(os.path.join(SRC, "1808.02836v2.pdf"), "%PDF")
        # held locally under the stamp id, ingested under another filename
        sj(LIB, "arxiv-2108.09349v2", "2108.09349v2-final.pdf")
        _mk(os.path.join(SRC, "2108.09349v2.pdf"), "%PDF")
        # negative control: old-style id, both scripts already agree
        sj(LIB, "0406242v4", "0406242v4.pdf")
        _mk(os.path.join(SRC, "0406242v4.pdf"), "%PDF")
        # fresh ingest, artefacts still in the queue
        sj(SRC, "arxiv-2209.06973v1", "2209.06973v1.pdf")
        _mk(os.path.join(SRC, "2209.06973v1.pdf"), "%PDF")
        # never ingested, no arXiv id to recover from
        _mk(os.path.join(SRC, "fulltext.pdf"), "%PDF")
        # OCR ran, ingest did not
        _mk(os.path.join(SRC, "pending-ocr", "ocr", "page-001.txt"), "text")

        mapping = build_mapping()

        want_map = {
            "2108.09349v2.pdf": "arxiv-2108.09349v2",   # the fallback half
            "0406242v4.pdf": "0406242v4",
            "2209.06973v1.pdf": "arxiv-2209.06973v1",
            "1808.02836v2.pdf": "1808.02836v2",         # unrecoverable, by design
            "fulltext.pdf": "fulltext",
        }
        for name, doc in want_map.items():
            if mapping.get(name) != doc:
                print(f"  FAIL  mapping[{name}]: want {doc}, got {mapping.get(name)}")
                ok = False

        # dry run must refuse exactly what --apply refuses: mode-independence
        # is the property the both-roots check in has_structure() buys, and a
        # guard that fires in only one mode is the bug wearing a hat.
        _, _, dry = move_files(mapping, apply=False)
        moved, _, refused = move_files(mapping, apply=True)

        # Assembled, never written as one literal. `rewrite_refs` scans every
        # tracked .py including this one, so a contiguous "uploads/<name>.pdf"
        # here is indistinguishable from a real citation: `--verify` reports
        # it as a stale reference and `--apply` REWRITES it, silently breaking
        # the test that guards the rewriter. Caught by running --verify on the
        # real tree, which is the only reason it is not still in here.
        up = "uploads/"
        want_refused = {up + n for n in ("1808.02836v2.pdf", "fulltext.pdf",
                                         "pending-ocr/")}
        got = {w for w, _ in refused}
        if got != want_refused:
            print(f"  FAIL  refused: want {sorted(want_refused)}, got {sorted(got)}")
            ok = False
        if {w for w, _ in dry} != want_refused:
            print(f"  FAIL  dry run refused a different set: {sorted(w for w, _ in dry)}")
            ok = False

        # no orphan may exist; the recoverable one must have joined the real dir
        for d in ("2108.09349v2", "1808.02836v2", "fulltext", "pending-ocr"):
            if os.path.exists(os.path.join(LIB, d)):
                print(f"  FAIL  {LIBNAME}/{d}/ created — an unreadable directory")
                ok = False
        for doc, pdf in (("arxiv-2108.09349v2", "2108.09349v2.pdf"),
                         ("0406242v4", "0406242v4.pdf"),
                         ("arxiv-2209.06973v1", "2209.06973v1.pdf")):
            if not os.path.exists(os.path.join(LIB, doc, pdf)):
                print(f"  FAIL  {LIBNAME}/{doc}/{pdf} did not land")
                ok = False
        for f in ("1808.02836v2.pdf", "fulltext.pdf"):
            if not os.path.exists(os.path.join(SRC, f)):
                print(f"  FAIL  uploads/{f} left the queue despite the refusal")
                ok = False
        if moved != 3:
            print(f"  FAIL  moved {moved} PDFs, want 3")
            ok = False

        # CASE 7 -- the resolve-required rewrite (owner ruling 2026-09-13).
        # A mapping entry whose PDF is NOT in uploads/ was migrated in an
        # earlier run, so a `uploads/<it>` string in the tree is PROSE about
        # that migration, not a live reference. Rewriting it corrupted three
        # files on 2026-09-13, one of which it made confidently FALSE rather
        # than visibly broken. Guard: such a name contributes no pattern.
        fake = {"live-now.pdf": "arxiv-live-now", "migrated-earlier.pdf": "arxiv-earlier"}
        pats = _rewrite_patterns(fake, {"live-now.pdf"})
        repls = [r for _, r in pats]
        if len(pats) != 1 or repls != [f"{LIBNAME}/arxiv-live-now/live-now.pdf"]:
            print(f"  FAIL  resolve-required rewrite: want only the live name, got {repls}")
            ok = False
        if _rewrite_patterns(fake, set()):
            print("  FAIL  empty live set still produced rewrite patterns")
            ok = False
        # and it must still rewrite BOTH when both are genuinely live --
        # a guard that refuses everything would also pass the two checks above.
        if len(_rewrite_patterns(fake, set(fake))) != 2:
            print("  FAIL  both-live case did not produce two patterns")
            ok = False
    finally:
        REPO, SRC, LIB = keep
        shutil.rmtree(tmp, ignore_errors=True)

    print("  selftest PASS" if ok else "  selftest FAIL")
    return 0 if ok else 1

def main() -> int:
    ap = argparse.ArgumentParser(description="Migrate uploads/ to the per-document layout")
    ap.add_argument("--apply", action="store_true", help="perform the migration (default: dry run)")
    ap.add_argument("--verify", action="store_true", help="post-migration checks only")
    ap.add_argument("--selftest", action="store_true",
                    help="run the guard against the cases qou-cvx9 measured")
    args = ap.parse_args()

    if args.selftest:
        return _selftest()

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

    # Capture what is genuinely being migrated BEFORE move_files empties
    # uploads/. After the move every source path is gone, so this cannot be
    # recomputed downstream -- see rewrite_refs' docstring.
    live = {n for n in mapping if os.path.exists(os.path.join(SRC, n))}
    historical = len(mapping) - len(live)
    if historical:
        print(f"  {historical} mapping entr(ies) already migrated in an earlier "
              f"run — their `uploads/` mentions are history, not references, "
              f"and are left alone")

    moved, missing, refused = move_files(mapping, args.apply)
    files, subs = rewrite_refs(mapping, args.apply, live)
    verb = "moved" if args.apply else "would move"
    verb2 = "rewrote" if args.apply else "would rewrite"
    print(f"\n{verb} {moved} PDFs ({missing} mapped but absent)")
    print(f"{verb2} {subs} references across {files} files")

    if refused:
        # Loud, and non-zero. A silent orphan is the defect; a refusal that
        # scrolls past in a bulk drain is the same defect with extra steps.
        print(f"\nREFUSED {len(refused)} move(s) — target has no structure.json:")
        for what, why in refused:
            print(f"    {what}\n        {why}")
        print("\nThese are NOT ingested. Moving them would create a directory the\n"
              "corpus holds and cannot read — invisible at every tier of\n"
              "corpus-grep path 5. Ingest them first, then re-run:\n"
              "    python3 folio-assistant/cat-harness-tools/scripts/pdf-structure.py --outdir library <pdf>\n"
              "    python3 scripts/summarize-library.py --apply")

    if not args.apply:
        print("\ndry run — re-run with --apply")
    else:
        print("\nnow run: scripts/migrate-uploads-to-library.py --verify")
    return 1 if refused else 0


if __name__ == "__main__":
    sys.exit(main())
