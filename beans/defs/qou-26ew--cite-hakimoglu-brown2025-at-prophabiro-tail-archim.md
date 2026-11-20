---
# qou-26ew
title: Cite [hakimoglu-brown2025] at prop:habiro-tail-archimedean-action
status: todo
pr: 8289
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:13:25Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-1qhv
---

Add a canonical secondary source (Lewin, Polylogarithms and Associated Functions, 1981; or Zagier, The dilogarithm function, 2007) alongside hakimoglu-brown2025 at prop:habiro-tail-archimedean-action, so the classical golden-ratio Li_2 evaluation and the Lean '-- Ref:' do not rest on a single unrefereed preprint. Not a claim of error in the preprint.

**From the source**
- eq. (4) (Rogers L-function), eq. (6) (Euler reflection), eq. (7) (Landen), and the Q(sqrt 5) ladder section — Beta-integral analytic proofs of two-term Li_2 relations and ladder identities with arguments in Q(sqrt 2), Q(sqrt 3), Q(sqrt 5), Q(sqrt -7), together with single-term dilogarithm evaluations.
  Use here: Backs the reduction of A_0 = -4 int_0^{ln phi} ln(2 sinh s) ds to Li_2(phi^{-2}) = pi^2/15 - ln^2 phi in prop:habiro-tail-archimedean-action, and the '-- Ref:' in RogersDilogInflection.lean.

Source: `library/arxiv-2506.10206v2/2506.10206v2-analytic-dilogarithm-identities-hakimoglu-brown.pdf` (`hakimoglu-brown2025`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## Round 57 Implementation Progress (PR #8289)
- **Status:** `in-progress` (per no-unilateral-closure policy)
- **PR:** https://github.com/litlfred/qou/pull/8289 (head `b1d29c3ac9e8ff1013e87a6f368591fb977a1ff3`, Commit 1 `85cf34f4dd33fa831b7480e3f2c9e1ff2e2f5c6d`)
- **Lean 4 Module & Theorems:** `QOU/AlphaEM/FiveTwoDiscriminantGluingAndHabiroDilogLadder.lean` (`golden_ratio_rogers_landen_rational_denominators` citing `[hakimoglu-brown2025]`, Lewin 1981, Zagier 2007)
- **80-dps Witness:** `computations/probes/round57-fivetwo-discriminant-habiro-dilog-dglz-pentagon.witness.json` (`scriptHash: 3ee733fedb99`, `allPassed: true`, `0` raw `float64`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8289, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
