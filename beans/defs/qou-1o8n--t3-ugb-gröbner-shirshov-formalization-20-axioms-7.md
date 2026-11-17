---
# qou-1o8n
title: 'T3: UGB Gröbner-Shirshov formalization (20 axioms + 7 sorries)'
status: in-progress
type: epic
priority: normal
created_at: 2026-08-03T15:06:36Z
updated_at: 2026-11-17T08:19:19Z
parent: qou-rtxm
---


## Reorganisation 2026-10-04

Now the epic for P3.GS under Lean / Mathlib foundations.


## Round 58 Progress (lane-e667)
- **PR:** https://github.com/litlfred/qou/pull/8276 (`1909a7bd3bec6ebbdc594cc42f836c8a59fb6451`)
- **Module:** `QOU.Foundations.IsotypicBlockSpolyLaurentHolonomy` (`folio/quantum-observable-universe/lean/QOU/Foundations/IsotypicBlockSpolyLaurentHolonomy.lean`), wired into `QOU.lean`.
- **Theorem:** `overlap_spolynomial_assoc_and_joinable` — proves overlap S-polynomial `f · w - u · g` vanishing under associative reduction rules `u · v = f`, `v · w = g` and normal-form joinability over generic `CommRingCarrier R`, verified at 80 dps in `isotypic-block-spoly-laurent-holonomy.witness.json`.
- **Status:** Kept at `in-progress` pending Merge Manager merge and full dependency verification.
