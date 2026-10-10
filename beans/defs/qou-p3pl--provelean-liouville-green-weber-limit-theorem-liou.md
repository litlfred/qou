---
# qou-p3pl
title: 'PROVE(lean): liouville_green_weber_limit — theorem liouville_green_weber_limit (n m : ℝ) (A B C : ℝ) (hA : A = 2) (hC : C = -22) : ∃  [cited manuscript]'
status: completed
type: task
priority: normal
tags:
    - cited-sorry
    - paper-qou
    - repo-infra
    - reorg-2026-10-04
    - lean
created_at: 2026-08-01T23:31:08Z
updated_at: 2026-10-04T15:22:38Z
parent: qou-k1mq
---

**File:** `QOU/QBeta/ToroidalHarmonicsBasis.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/QBeta/ToroidalHarmonicsBasis.lean

### `liouville_green_weber_limit`  —  line 114  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem liouville_green_weber_limit (n m : ℝ) (A B C : ℝ) (hA : A = 2) (hC : C = -22) : ∃ (T : ℝ → ℝ), ∀ (F : ℝ → ℝ), ∀ η, ToroidalHarmonicODE n m F η ↔ WeberODE A B C (F ∘ T) η `
- **Cited:** `[manuscript]`
  - [manuscript] quantum-observable-universe/qbeta
- **Tractability:** ODE change-of-variables reducing the toroidal-harmonic ODE to the Weber ODE; concrete calculus, repo-internal.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] k1mq child: no real sorry left in target file. liouville_green_weber_limit theorem uncond, 0 sorry
