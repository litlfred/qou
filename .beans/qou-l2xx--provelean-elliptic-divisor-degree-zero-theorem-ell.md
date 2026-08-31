---
# qou-l2xx
title: 'PROVE(lean): elliptic_divisor_degree_zero — theorem elliptic_divisor_degree_zero {f : ℂ → ℂ} {ω₁ ω₂ : ℂ} (hf : IsElliptic f ω₁ ω₂) (hi [cited manuscript]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-qou
    - infra-blocked
created_at: 2026-08-01T23:31:06Z
updated_at: 2026-08-31T02:53:38Z
parent: qou-k1mq
---

**File:** `QOU/Mathlib/EllipticDivisorDegree.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/Mathlib/EllipticDivisorDegree.lean

### `elliptic_divisor_degree_zero`  —  line 240  ·  tier **B** (infra-blocked / open-conjecture)
- **Proposition:** `theorem elliptic_divisor_degree_zero {f : ℂ → ℂ} {ω₁ ω₂ : ℂ} (hf : IsElliptic f ω₁ ω₂) (hindep : LinearIndependent ℝ ![ω₁, ω₂]) (hnc : ¬ ∃ c, ∀ z, f z = c) (S : Finset ℂ) (hS : (S : Set ℂ) = {z | z ∈ fundamentalParallelogram ω₁ ω₂ ∧ (MeromorphicOn.divisor f Set.univ) z ≠ 0}) : ∑ z ∈ S, (MeromorphicO`
- **Cited:** `[manuscript]`
  - [manuscript] Liouville's
- **Tractability:** Σ of divisor orders of an elliptic function over a fundamental parallelogram = 0 (argument principle); Mathlib's contour/argument-principle infra is incomplete. Overlaps PR #4140.
- **Next step:** Infra-blocked: needs Mathlib theory that does not exist. Track upstream; do not launder via axiom/class.

## Verdict CONFIRMED 2026-08-31 (audit: docs/audits/2026-08-31-individuating-the-fourteen-infra-blocked-verdicts.md)

Individuated with the other thirteen. For THIS item the boilerplate verdict is right: the named
theory is genuinely absent from Mathlib and is genuinely required. Kept as-is.

Recorded because the same verdict was WRONG on several siblings; "confirmed" here means checked,
not merely un-revisited.
