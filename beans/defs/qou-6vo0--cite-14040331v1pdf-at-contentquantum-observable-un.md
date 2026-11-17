---
# qou-6vo0
title: Cite 1404.0331v1.pdf at folio/quantum-observable-universe/lean/QOU/BraidKnot/AJTrefoil.lean (cl…
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:13:11Z
updated_at: 2026-10-04T15:17:10Z
parent: qou-19m0
---

StrongAJTrefoil is declared a literature-theorem class; its docstring should carry the strong-AJ source (this paper's §0.3 for torus knots, Thm 1 for cables), not only garoufalidis2004's statement of the ordinary AJ conjecture.

Source: `library/arxiv-1404.0331v1/1404.0331v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-1404.0331v1/  ->  [tran2014]
  THE STRONG AJ CONJECTURE FOR CABLES OF TORUS KNOTS

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [tran2014] as the citation key when you do it.

### Progress (Round 71 — PR litlfred/qou#8300)
- Formalized in PR `litlfred/qou#8300` (`feat/round71-deltalambda-idempotent-ajtrefoil-n5-gbdepth-43c1`, Commit 1 `a2b0ac0a51416e015d2c71b026de5cf8836daab0`, Head `432940fd4ad329afd23f7d920528ba787ac8691a`, `scriptHash: 06c965f4587d`).
