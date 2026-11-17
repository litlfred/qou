---
# qou-1wcu
title: 'W8: library Lean — formal Laurent residue-of-exact-form (QOU/Mathlib)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-12T21:32:19Z
updated_at: 2026-11-17T08:19:19Z
parent: qou-c8p8
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-17 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Round 58 Progress (lane-e667)
- **PR:** https://github.com/litlfred/qou/pull/8276 (`1909a7bd3bec6ebbdc594cc42f836c8a59fb6451`)
- **Module:** `QOU.Foundations.IsotypicBlockSpolyLaurentHolonomy` (`folio/quantum-observable-universe/lean/QOU/Foundations/IsotypicBlockSpolyLaurentHolonomy.lean`), wired into `QOU.lean`.
- **Theorem:** `laurent_residue_exact_zero_and_linear` — proves formal Laurent residue vanishing on exact differentials `laurentRes (laurentDeriv f) = 0`, `R`-linearity, and invariance of `laurentRes` under adding exact differentials `ω + d(f)` over generic `CommRingCarrier R`, verified at 80 dps in `isotypic-block-spoly-laurent-holonomy.witness.json`.
- **Status:** Kept at `in-progress` pending Merge Manager merge and full dependency verification.
