---
# qou-1wcu
title: 'W8: library Lean — formal Laurent residue-of-exact-form (QOU/Mathlib)'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-12T21:32:19Z
updated_at: 2026-11-20T08:27:17Z
parent: qou-c8p8
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-17 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Round 58 Progress (lane-e667)
- **PR:** https://github.com/litlfred/qou/pull/8276 (`1909a7bd3bec6ebbdc594cc42f836c8a59fb6451`)
- **Module:** `QOU.Foundations.IsotypicBlockSpolyLaurentHolonomy` (`folio/quantum-observable-universe/lean/QOU/Foundations/IsotypicBlockSpolyLaurentHolonomy.lean`), wired into `QOU.lean`.
- **Theorem:** `laurent_residue_exact_zero_and_linear` — proves formal Laurent residue vanishing on exact differentials `laurentRes (laurentDeriv f) = 0`, `R`-linearity, and invariance of `laurentRes` under adding exact differentials `ω + d(f)` over generic `CommRingCarrier R`, verified at 80 dps in `isotypic-block-spoly-laurent-holonomy.witness.json`.
- **Status:** Kept at `in-progress` pending Merge Manager merge and full dependency verification.

## 2026-11-20 — W10 (qou-c8p8 workstream)

Stalled-claim takeover by W10 (session_01VQDpPeWFnvbDUN18UJ6CyC, PR #8530): prior claim's backing branch had no commit for >3 h (lane-e667 branches last pushed 2026-11-17). The lane-e667 'Progress Update' sections above refer to unmerged bundle PRs and are NOT the closure.

Subject proved on main: `fresidue_fderiv` (Mathlib/FormalLaurentResidue.lean:49), plus `fresidue_jet_succ`, `fresidue_sum_jet_succ`. Re-checked 2026-11-20, generic `[CommRing R]`, axioms clean.
