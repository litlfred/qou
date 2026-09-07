---
# qou-4n9o
title: 'library: INDEX.md misses 4 fully-sectioned documents and 23 directories were never sectioned'
status: todo
type: task
priority: normal
created_at: 2026-09-07T07:17:06Z
updated_at: 2026-09-07T07:17:56Z
---

Measured 2026-09-07 while ingesting the owner's 8 q-difference uploads (a23d06ce2c).

AGENTS.md prescribes the invariant `directories − index rows = duplicate count` and says a failure means INDEX.md is behind. It is behind, and in TWO different ways that need different fixes.

    dirs = 661   INDEX.md rows = 615   gap = 46
      19  marked `duplicate_of`      — correct, these get no row by design
      23  ZERO sections              — PDF present, NEVER sectioned; not an index
                                       bug at all, an ingestion backlog
       4  fully sectioned, NO row    — the real index defect

**The 4 that are sectioned and invisible to tier 1** — this is the tier every agent is told to read FIRST, so these are documents corpus-grep path 5 cannot find by its documented route:

    ant-v14-n7-s                            170 sections
    s40687-023-00400-3                       13 sections
    gt-v10-n3-p07-p                          12 sections
    neumann-zagier-1985-...(two dirs)         2 sections each

`ant-v14-n7-s` at 170 sections is a whole document. The two `neumann-zagier` dirs are probably the known NZ triplicate AGENTS.md mentions and may be legitimately duplicate-adjacent — check before adding rows.

**The 23 with zero sections** are a separate problem: they hold a PDF and no `sections/`, so they are invisible to a text grep entirely. Several have opaque names (`1.9781611972443.fm`, `fulltext`, `amc_2730`, `m4-24`) which is presumably why they were skipped. Fix is to run folio-assistant `scripts/pdf-structure.py` over them, and route any with no text layer to the OCR tier (AGENTS.md records 25 directories already in that state).

**Note for whoever does this — the platform version matters.** Regenerating sections with the PINNED platform (`428ca5c`) is a REGRESSION on documents whose sections were produced later: it drops `doc_brief` from section front-matter (the field path 5 relies on to make a hit interpretable) and appends the author line to `doc_title`. Measured on `arxiv-0903.0853v3` + `arxiv-1404.2541v1`: 237 files, −786 lines. Reverted rather than committed. Run `scripts/summarize-library.py --apply` afterwards, which restores `doc_brief`, or bump the pin deliberately.

Not fixed here — out of scope for the branch that found it.
