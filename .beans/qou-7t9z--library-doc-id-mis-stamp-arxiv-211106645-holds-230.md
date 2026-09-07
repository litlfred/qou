---
# qou-7t9z
title: 'Library doc-id mis-stamp: arxiv-2111.06645/ holds 2304.09377v2.pdf — two different works whose dirs differ only by a v3 suffix'
status: todo
type: task
priority: normal
created_at: 2026-09-07T09:03:34Z
updated_at: 2026-09-07T09:04:17Z
---

Found 2026-09-07 during the corpus-grep for `qou-17mq`. Verified directly
against the committed tree, not taken on report.

Two **different works** sit in directories whose names differ only by a `v3`
suffix, which reads as a version pair and is not one:

| dir | PDF it holds | actual arXiv | `structure.json` stamp | title | pp |
|---|---|---|---|---|---|
| `library/arxiv-2111.06645/` | `2304.09377v2.pdf` | **2304.09377** | `id: 2111.06645, version: None` ❌ | *Knots and Their Related q-Series* | 39 |
| `library/arxiv-2111.06645v3/` | `2111.06645v3.pdf` | 2111.06645v3 | `id: 2111.06645, version: 3` ✓ | *Knots, Perturbative Series and Quantum Modularity* | 87 |

The defect is confined to the **directory name** of the 39-page paper, its
`structure.json` arXiv stamp, and the `library.arxiv: "2111.06645"` field that
repeats it (`content/schema/references.ts:6704`). Its bibliographic fields are
correct — DOI `10.3842/SIGMA.2023.082`, `URL .../abs/2304.09377`
(`references.ts:6718`) — and each `references.ts` entry points at its own
directory, so **nothing resolves to the wrong paper today**. This is a
provenance defect, not a live mis-citation.

## Why it matters for corpus-grep path 5

A hit in one of these directories is easily read as a hit in the other. This
is the INVERSE of the duplicate trap AGENTS.md already documents — that one
warns that *two hits on one work are not two sources*; here **one doc-id
spelling covers two works**. Neither directory is `duplicate_of`-marked and
neither is in `docs/audits/library-duplicate-ledger.json`, correctly, because
they are not duplicates. So no existing guard sees this.

Both are live sources on the knot side: the 87-page one is where the
"only their product is canonically defined" precedent cited in
`docs/audits/2026-09-07-em-linking-kernel-and-exponent-are-degenerate.md`
comes from.

## Fix

Rename `library/arxiv-2111.06645/` to `library/arxiv-2304.09377v2/`, correct
its `structure.json` metadata.arxiv stamp, and update
`references.ts:6698-6704` (`docId`, `dir`, `pdf`, `library.arxiv`). Mechanical
and low-risk; no content block cites the directory path directly.

## Detection shape worth generalising

The stamp is derived from page-1 text (`pdf-structure.py` prefers the arXiv
margin stamp over DocInfo, deliberately and for good reasons). This document
presumably carries a stale or cited stamp on its first page. A cheap guard:
assert that `metadata.arxiv.id` is consistent with the PDF **filename** where
the filename itself looks like an arXiv id, and flag the mismatch rather than
silently preferring one. Nothing in the corpus checks this.
