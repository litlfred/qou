---
# qou-rc4t
title: 'Constructive: real-closed (Tarski) route for finite-N comparisons'
status: todo
type: task
priority: normal
tags:
    - constructive
    - volume-conjecture
created_at: 2026-11-27T17:25:00Z
updated_at: 2026-11-27T17:25:00Z
parent: qou-dk7p
---
Owner standing pick (recommended option) 2026-11-27, alternative raised
alongside the Lawvere cut.

Goal: state every finite-N comparison (per-N certificate values, which are
algebraic over Q(zeta_N)+) inside the real algebraic numbers, a real-closed
field where order is decidable, so finite-N positivity claims need no axiom.
Mechanism: Sturm-sequence / sign-determination checks on the minimal
polynomial; Mathlib real-closed support is thin, so expect finite checks.

Scope: finite N only. The N -> infinity limit stays on [Coev E]
(QOU/Core/LawvereCut.lean, PR #9487). Pairs with qou-pc7n (certificates).

Not adopted, recorded as options: topos-internal Dedekind reals (moves the
axiom, large); order-only MacNeille cut (special case of the Lawvere cut).
