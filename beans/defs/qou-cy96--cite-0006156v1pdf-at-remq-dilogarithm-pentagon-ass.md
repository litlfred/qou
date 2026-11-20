---
# qou-cy96
title: Cite 0006156v1.pdf at rem:q-dilogarithm-pentagon-associator
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:36:00Z
updated_at: 2026-11-20T16:06:50Z
pr: 8325
parent: qou-ysb7
---

rem:q-dilogarithm-pentagon-associator cites faddeev_kashaev1994 for the operator pentagon; this paper carries a proof at complex b, which is the regime the corpus's fibre-level (non-real q) framing requires.

**From the source**
- Sect. 6.1, eq. (20) + Sect. 6.5 — The operator five-term identity e_b(P) e_b(X) = e_b(X) e_b(P+X) e_b(P) on a Heisenberg pair, with a proof valid for complex b (real b by continuity).
  Use here: Sources the operator pentagon that rem:q-dilogarithm-pentagon-associator states, at the complex-b generality the corpus's fibre-vs-observable split needs (fibre-level q need not be real).

Source: `library/arxiv-hep-th-0006156v1/0006156v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-hep-th-0006156v1/  ->  [faddeev-kashaev-volkov2000]
  Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [faddeev-kashaev-volkov2000] as the citation key when you do it.

### Progress (Round 61)
- Formalized Lean 4 theorems, 80-dps mpmath probe, and 2-commit witness chain in PR #8325 (`5b31e8e9599f35d940975c6c2937ae31bf0eaa65`). Status kept `in-progress` pending PR merge.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8325, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
