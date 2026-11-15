---
# qou-oh6k
title: 'PROVE(lean): burnside — theorem burnside (n : ℕ) (partitions : List (Partition n)) (hcomplete : ∀ μ : Partition n, [cited sagan2001]'
status: completed
type: task
priority: normal
tags:
    - cited-sorry
    - paper-qou
    - repo-infra
    - cite-sagan2001
    - reorg-2026-10-04
    - lean
created_at: 2026-08-01T23:31:01Z
updated_at: 2026-10-04T15:22:23Z
parent: qou-k1mq
---

**File:** `QOU/BraidKnot/DeltaLambdaSignRule.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/BraidKnot/DeltaLambdaSignRule.lean

### `burnside`  —  line 315  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem burnside (n : ℕ) (partitions : List (Partition n)) (hcomplete : ∀ μ : Partition n, μ.parts ∈ partitions.map Partition.parts) (hnodup : (partitions.map Partition.parts).Nodup) : (partitions.map fun Λ => Λ.dimIrrep ^ 2).sum = Nat.factorial n `
- **Cited:** `[sagan2001]`
  - [sagan2001] Sagan (2001), *The Symmetric Group: Representations, Combinatorial Algorithms, and Symmetric Functions* — (no DOI/URL)
- **Tractability:** Burnside identity Σ_λ (dim V_λ)² = n! for S_n; Mathlib has general character theory but the partition-indexed dimIrrep must be tied to actual irreps (repo Specht dimension).
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] burnside: target decl/file sorry-free on main 2026-10-03; [B] sp00 completed epic lists bricks axiom-clean (#print axioms). Conditional-in-form only on SnIsotypicSpechtSplit, which is inhabited (S
