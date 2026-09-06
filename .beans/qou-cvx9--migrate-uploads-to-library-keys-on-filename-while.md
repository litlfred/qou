---
# qou-cvx9
title: migrate-uploads-to-library keys on filename while pdf-structure keys on the arXiv stamp — divergence silently creates orphan doc dirs
status: todo
type: task
priority: high
created_at: 2026-09-06T13:48:45Z
updated_at: 2026-09-06T13:49:24Z
---

Found pre-merge on #6955 while probing its merge ordering against #6942. **A defect
in the branch, not a merge artifact** — it lands orphan documents on `main` whether
or not #6942 exists.

## The two scripts disagree on what a document's identity is

| script | derives doc-id from |
|---|---|
| `scripts/pdf-structure.py` | the **page-1 arXiv stamp** — `arxiv-1808.02836v2` |
| `scripts/migrate-uploads-to-library.py` | the **filename** — `1808.02836v2` |

For every PDF whose filename lacks the `arxiv-` prefix these disagree. `migrate`
does not detect that: it creates `library/<basename>/` and moves the PDF in,
producing a directory holding **one file** — no `structure.json`, no `sections/`,
no `INDEX.md` row.

## Measured

`git ls-tree -r --name-only` on `origin/claude/uploads-library-ingest-2026-09-06`:

| orphan created | files | the real doc dir | files | sections |
|---|---|---|---|---|
| `library/1808.02836v2/` | **1** | `library/arxiv-1808.02836v2/` | 24 | 22 |
| `library/2108.09349v2/` | **1** | `library/arxiv-2108.09349v2/` | 22 | 20 |

`git merge-tree` surfaces them as `CONFLICT (rename/rename)`, which is how they
were caught — a merge probe, not a check anything runs on purpose.

A third skipped doc, `0406242v4`, does **not** trigger it: its old-style arXiv id
produces no `arxiv-` prefix, so both scripts agree on the path and the PDF lands
correctly beside the full ingest.

## Why it is worse than a cosmetic duplicate

The orphan is **invisible to corpus-grep path 5** at every tier — no `INDEX.md`
row (tier 1), no `summary.json` (tier 2), no `sections/` (tier 3), no `ocr/`
(tier 4). So the corpus holds the document twice and a `has the corpus got this?`
check finds it once at best. That is the precise failure mode the `uploads/` →
`library/` pipeline exists to close, reintroduced by the last step of the pipeline
itself.

## The trigger is the SKIP path, which is the part worth remembering

`pdf-structure.py` correctly **skips** an already-held doc and emits nothing.
`migrate` then moves that PDF anyway, and having no ingest output to consult,
falls back to the filename. So the orphan is produced exactly when the upstream
step did the right thing — a skip is indistinguishable from a fresh ingest at the
`migrate` boundary.

## Proposed guard (NOT written — flagged, per anti-speculation)

`migrate-uploads-to-library.py` should **refuse** to move a PDF into a target dir
that has no `structure.json`, and report it rather than inventing the dir. That
turns a silent orphan into a loud skip. It should probably also consult the
page-1 stamp itself, but the refusal alone closes the invisibility.

Not implemented here: the immediate case is fixed by deleting the two dirs on
#6955, and widening that PR to change an ingest script is the author's call.

## Blast radius

`scripts/migrate-uploads-to-library.py` is the only consumer. Nothing in
`content/`, no producer, no witness, no number. The cost of leaving it is future
orphans on every bulk ingest whose filenames lack the `arxiv-` prefix.

## Default if nothing is done

The two dirs are deleted on #6955 and the script is unchanged, so the next bulk
`uploads/` drain reproduces it. `migrate --verify` reports such dirs as
"pre-existing problems", which reads as pre-existing rather than as just-created.

## Related, separate

`library/` also holds **642 dirs against 589 `INDEX.md` rows**; 23 of the gap are
duplicates whose row is correctly omitted, leaving **8 sectioned documents with no
row** — five pre-existing (`ant-v14-n7-s`, `arxiv-1111.2828v2`, `arxiv-1307.6697v2`,
`arxiv-1401.5542v1`, `arxiv-2104.07437v4`) and three from #6942. Different defect
(staleness, not identity), fixed in-flight on #6955 by re-running
`summarize-library.py --apply`, so it carries no bean of its own.
