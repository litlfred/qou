---
# qou-0otg
title: Cite [habiro2000] at prop:habiro-precision-ladder-equivalence
status: in-progress
pr: 8289
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:29Z
updated_at: 2026-10-04T15:17:36Z
parent: qou-1qhv
---

Four Lean sites cite locators (Theorem 1.1, Corollary 1.2) that do not exist in this document, and one attributes a different Habiro title to the key. Either re-point them at the real results here (Props. 5.1-8.2) or register the intended paper - 'On the quantum sl_2 invariants of knots and integral homology spheres' - under its own key and cite that.

**From the source**
- Props. 5.1, 6.1, 6.2, 8.2 and eqs. (1)-(2) in Sec. 3 — Explicit colored-Jones formulas for the trefoil (both chiralities) and figure-eight knot, and skein-basis propositions in the solid torus.
  Use here: Correct locators to replace 'Theorem 1.1' / 'Corollary 1.2' wherever those were cited, or evidence that the claim belongs to a different Habiro paper and needs its own key.

Source: `library/1172-3/1172-3.pdf` (`habiro2000`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## Round 57 Implementation Progress (PR #8289)
- **Status:** `in-progress` (per no-unilateral-closure policy)
- **PR:** https://github.com/litlfred/qou/pull/8289 (head `b1d29c3ac9e8ff1013e87a6f368591fb977a1ff3`, Commit 1 `85cf34f4dd33fa831b7480e3f2c9e1ff2e2f5c6d`)
- **Lean 4 Module & Theorems:** `QOU/AlphaEM/FiveTwoDiscriminantGluingAndHabiroDilogLadder.lean` (`habiro_props_51_61_82_cyclotomic_degree_step` citing `[habiro2000]` Props. 5.1, 6.1, 6.2, 8.2)
- **80-dps Witness:** `computations/probes/round57-fivetwo-discriminant-habiro-dilog-dglz-pentagon.witness.json` (`scriptHash: 3ee733fedb99`, `allPassed: true`, `0` raw `float64`)
