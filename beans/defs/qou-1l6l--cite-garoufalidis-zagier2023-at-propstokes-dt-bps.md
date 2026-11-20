---
# qou-1l6l
title: Cite [garoufalidis-zagier2023] at prop:stokes-dt-bps-bridge
status: todo
pr: 8283
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:17Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-1qhv
---

The reference is registered and its companion sources are already load-bearing at the Stokes/DT bridge; if the Habiro-ring holomorphic-block structure is in fact used by the A_ω program, it should carry a citation site there. If it is not used, the honest outcome is to record it as background rather than leave a registered-but-unconsumed entry.

Source: `library/arxiv-2111.06645/2304.09377v2.pdf` (`garoufalidis-zagier2023`)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## Round 56 Implementation Progress (PR #8283)
- **Status:** `in-progress` (per no-unilateral-closure policy)
- **PR:** https://github.com/litlfred/qou/pull/8283 (head `f53a095b5ee34373c44ef4b0b400e85b12af4c1c`, Commit 1 `0e2f86d58bac8f2f07854f3515aabf15d9779cd3`)
- **Lean 4 Module & Theorems:** `QOU/QBeta/StokesDTBpsHolomorphicBlockAndQHolonomicRecurrence.lean` (`stokes_dt_bps_habiro_holomorphic_block_invariance` citing `[garoufalidis-zagier2023]`)
- **80-dps Witness:** `computations/probes/round56-mellor-melvin-bws0-stokes-dt-qholonomic.witness.json` (`scriptHash: d98411981e4d`, `allPassed: true`, `0` raw `float64`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8283, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
