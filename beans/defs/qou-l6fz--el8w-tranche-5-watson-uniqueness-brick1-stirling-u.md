---
# qou-l6fz
title: 'el8w tranche 5 (Watson uniqueness): brick1 Stirling UPPER bound n!<=e*sqrt(2pi n)(n/e)^n from factorial_isEquivalent_stirling; brick2 Gevrey1 remainder=>exp(-1/(sigma r)) decay; brick3 sector Phragmen-Lindelof uniqueness. Multi-session; NOT axiomatizable (anti-laundering). Mathlib lacks the upper Stirling bound.'
status: in-progress
pr: 8230
updated_at: 2026-11-21T12:40:00Z
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-13T00:31:38Z
updated_at: 2026-10-04T15:12:27Z
parent: qou-frzo
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (PR #8230)
- **Status**: `in-progress` (awaiting Merge Manager merge of `litlfred/qou#8230` at `1bb9d799f645494190e9e4834f3982913ab5e918`).
- **Lean Formalization**: `QOU.QBeta.PentagonTwoRouteAndC1RamifiedStokesBrick.watson_gevrey1_optimal_truncation_quadratic_completion` (Optimal Gevrey-1 truncation N_star = 1/(sigma*r) exponential decay rate -1/(sigma*r) and quadratic Stirling-Gevrey lower envelope.)
- **80-dps Witness**: `computations/probes/pentagon-two-route-and-c1-ramified-stokes-brick.witness.json` (`scriptHash: ad15e8ab2a08`, `scriptCommitSha: 4eaeef60b72e32fbaaef92149ff8588e4dde4090`).


## 2026-11-21T12:40:00Z — alien-calculus drain (thread "Build the q-native alien calculus")

**Status of the three bricks on main 2ae54ab401 (re-verified lean-direct exit 0, standard axioms):** brick 1 `QOU.Mathlib.Borel.factorial_le_stirling_upper` (n! ≤ e√n(n/e)ⁿ, sharper than the √(2πn) form in the title) DONE; brick 2 `gevrey1_remainder_expDecay` DONE; brick 3 partly: `watson_uniqueness_rhp_open` needs decay exp(−b xˢ) with s > 1 STRICTLY along the real axis, and `watson_uniqueness_sector` transports it to sectors. A Gevrey-1 remainder gives s = 1 in the 1/r variable, so the classical Watson case (opening > π, s = 1) is NOT closed by these. Leaving open for that gap. Batch PR #8230 (W4: NEEDS-REWORK, lean-direct FAIL) does not close it. Superseded-premise check: none.
