---
# qou-1o8n
title: 'T3: UGB Gröbner-Shirshov formalization (20 axioms + 7 sorries)'
status: in-progress
type: epic
priority: normal
created_at: 2026-08-03T15:06:36Z
updated_at: 2026-11-18T10:37:00Z
parent: qou-rtxm
---


## Reorganisation 2026-10-04

Now the epic for P3.GS under Lean / Mathlib foundations.


## Round 58 Progress (lane-e667)
- **PR:** https://github.com/litlfred/qou/pull/8276 (`1909a7bd3bec6ebbdc594cc42f836c8a59fb6451`)
- **Module:** `QOU.Foundations.IsotypicBlockSpolyLaurentHolonomy` (`folio/quantum-observable-universe/lean/QOU/Foundations/IsotypicBlockSpolyLaurentHolonomy.lean`), wired into `QOU.lean`.
- **Theorem:** `overlap_spolynomial_assoc_and_joinable` — proves overlap S-polynomial `f · w - u · g` vanishing under associative reduction rules `u · v = f`, `v · w = g` and normal-form joinability over generic `CommRingCarrier R`, verified at 80 dps in `isotypic-block-spoly-laurent-holonomy.witness.json`.
- **Status:** Kept at `in-progress` pending Merge Manager merge and full dependency verification.

- Round 78 (`lane-e667`): Formalized `qou-pan0`, `qou-tgci`, `qou-ykt7`, `qou-bq5e`, `qou-ch3j` in `QOU.Foundations.FilteredDifferentialSquareIdempotentBlockDecompositionIsometryTransportFinitePresentationDiamondConfluence` with 80-dps `mpmath` 2-commit witness stamp (`0869f3f0f137dac72b436e92a747c174449acb33` -> `8147a3388c97af1335cf6c164bd3eb4c9b4bd78a`, `scriptHash=f8a29b2aeceb36b8f640091b101ca03046313573b1d604a9e680784ae71f9af4`) in PR `litlfred/qou#8422` (`status: in-progress`).

- Round 79 (`lane-e667`): Formalized `qou-ix9e`, `qou-lncp`, `qou-ulfe`, `qou-znz5`, `qou-pso0` in `QOU.Foundations.MonicRewritingRuleOrientationOverlapCriticalPairResolutionFormalGroupLawDistributionConfluenceSpecializationFlatness` with 80-dps `mpmath` 2-commit witness stamp (`0e73e1d84b41af22cbe0a7adb5792bfd6ad829c7` -> `f1e0c5f0a53084f645586bcab55a711f50415015`, `scriptHash=6f730a2d7a28822fd4184de185390b3fa00ae1e8c3c649430e85284ae55ef0da`) in PR `litlfred/qou#8430` (`status: in-progress`).
