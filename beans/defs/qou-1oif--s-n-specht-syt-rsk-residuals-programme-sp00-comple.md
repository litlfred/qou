---
# qou-1oif
title: S_n / Specht / SYT / RSK residuals (programme sp00 completed)
status: in-progress
type: epic
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:10:06Z
updated_at: 2026-11-17T08:19:19Z
parent: qou-rtxm
---

Sub-epic P3.SN of Lean / Mathlib foundations (work-plan reorganisation 2026-10-04).


## Round 58 Progress (lane-e667)
- **PR:** https://github.com/litlfred/qou/pull/8276 (`1909a7bd3bec6ebbdc594cc42f836c8a59fb6451`)
- **Module:** `QOU.Foundations.IsotypicBlockSpolyLaurentHolonomy` (`folio/quantum-observable-universe/lean/QOU/Foundations/IsotypicBlockSpolyLaurentHolonomy.lean`), wired into `QOU.lean`.
- **Theorem:** `hook_three_content_sum_and_cubic_factor` — proves three-box hook diagram content sum vanishing `0 + (1 + (-1)) = 0` and cubic spectral factorization `x · ((x + 1) · (x - 1)) = x³ - x` over generic `CommRingCarrier R`, with `S_4` Burnside dimension sum `1² + 3² + 2² + 3² + 1² = 24 = 4!` verified in `isotypic-block-spoly-laurent-holonomy.witness.json`.
- **Status:** Kept at `in-progress` pending Merge Manager merge and full dependency verification.
