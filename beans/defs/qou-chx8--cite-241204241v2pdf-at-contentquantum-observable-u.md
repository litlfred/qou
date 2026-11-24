---
# qou-chx8
title: Cite 2412.04241v2.pdf at folio/quantum-observable-universe/lean/QOU/Machinery/HabiroZetaFamily.…
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:43Z
updated_at: 2026-11-24T09:20:51Z
parent: qou-ysb7
---

Once the ref() key exists, the four Machinery/Habiro* Lean files should carry -- Ref: [<key>] at the docstring lines that currently name only the arXiv id, so the reference becomes machine-checkable.

Source: `library/arxiv-2412.04241v2/2412.04241v2.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-2412.04241v2/  ->  [garoufalidis-scholze-wheeler-zagier2024]
  The Habiro ring of a number field

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [garoufalidis-scholze-wheeler-zagier2024] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8335, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-22 — done in draft PR #9116 (issue #9115)

Citation added on branch `claude/library-cites-2026-11-22`, locator read from the held PDF. Close when #9116 merges.

Closed via post-merge reconciliation: landed on origin/main in PR #9116 (3885f1e31ec).
