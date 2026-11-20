---
# qou-20d3
title: Remark interpreting 0411647v2.pdf at a remark interpreting QOU.BraidsAndKnots.YoungDiagramKernel,…
status: todo
pr: 8449
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:12:49Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-aqfj
---

The genus-grading obstruction (Prop 3.4 applies to polynomial functions on Young diagrams; f^lambda is outside that algebra) is currently stated only inside a Python docstring. It is the load-bearing reason the kernel stays open and deserves a durable, cited home. NOT proposing aid-proof: Sniady does not close Cov_Planch(f^lambda, R_4) <= 0, and the corpus is right that it does not.

Source: `library/arxiv-math-0411647v2/0411647v2.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-math-0411647v2/  ->  [sniady2006asymptotics]
  Asymptotics of characters of symmetric groups, genus expansion and free probability

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [sniady2006asymptotics] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8449, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
