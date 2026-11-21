---
# qou-zlr6
title: Cite 0903.2472v1.pdf at qou:QOU.QBeta.StateIntegralRecursionLattice
status: in-progress
pr: 8289
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:28Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-19m0
---

Once registered, the state-integral definition used in QOU/QBeta should point at its actual origin rather than only at the later GGM/DGG papers.

Source: `library/arxiv-0903.2472v1/0903.2472v1.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-0903.2472v1/  ->  [dimofte-gukov-lenells-zagier-2009]
  Exact results for perturbative Chern-Simons theory with complex gauge group

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [dimofte-gukov-lenells-zagier-2009] as the citation key when you do it.

## Round 57 Implementation Progress (PR #8289)
- **Status:** `in-progress` (per no-unilateral-closure policy)
- **PR:** https://github.com/litlfred/qou/pull/8289 (head `b1d29c3ac9e8ff1013e87a6f368591fb977a1ff3`, Commit 1 `85cf34f4dd33fa831b7480e3f2c9e1ff2e2f5c6d`)
- **Lean 4 Module & Theorems:** `QOU/QBeta/CyclicDilogPentagonAndDGLZStateIntegralLattice.lean` (`dglz_2009_state_integral_trivalent_and_symplectic_invariance` citing `[dimofte-gukov-lenells-zagier-2009]`)
- **80-dps Witness:** `computations/probes/round57-fivetwo-discriminant-habiro-dilog-dglz-pentagon.witness.json` (`scriptHash: 3ee733fedb99`, `allPassed: true`, `0` raw `float64`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8289, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — expo-cite-xcheck drain

`Ref: [dimofte-gukov-lenells-zagier-2009] §3` added to StateIntegralRecursionLattice.lean. Completes on merge. Superseded-premise check against docs/coordination/owner-rulings.md (2026-11-21): none.

Evidence: branch `claude/expo-cite-xcheck-2026-11-21` (issue #8802); findings in docs/audits/2026-11-21-expo-cite-xcheck-findings.md.
