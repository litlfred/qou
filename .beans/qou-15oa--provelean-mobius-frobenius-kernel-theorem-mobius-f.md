---
# qou-15oa
title: 'PROVE(lean): mobius_frobenius_kernel — theorem mobius_frobenius_kernel {E : Type*} [NormedAddCommGroup E] [ctx : MobiusFrobeniusK [cited manuscript]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
created_at: 2026-08-01T23:31:04Z
updated_at: 2026-08-01T23:31:04Z
parent: qou-k1mq
---

**File:** `QOU/BraidsKnots/mobius_frobenius_kernel.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/BraidsKnots/mobius_frobenius_kernel.lean

### `mobius_frobenius_kernel`  —  line 82  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem mobius_frobenius_kernel {E : Type*} [NormedAddCommGroup E] [ctx : MobiusFrobeniusKernelContext E] (s t : ℝ) (_hst : ctx.γ s ≠ ctx.γ t) : Filter.Tendsto (fun q => ctx.K_FH q s t) (nhdsWithin 1 {q : ℝ | q ≠ 1}) (nhds (1 / ‖ctx.γ s - ctx.γ t‖ ^ 2)) `
- **Cited:** `[manuscript]`, `[manuscript]`
  - [manuscript] lem:mobius-energy-frobenius-kernel,
- **Tractability:** q→1 limit (Tendsto) of the Möbius–Frobenius kernel over a context; real-analysis over context class, repo-internal.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.
