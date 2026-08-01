---
# qou-lhsb
title: 'PROVE(lean): confinement_categorical — theorem confinement_categorical [ctx : ConfinementCategoricalContext] : ctx.E_infinity_00  [cited manuscript]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
created_at: 2026-08-01T23:31:09Z
updated_at: 2026-08-01T23:31:09Z
parent: qou-k1mq
---

**File:** `QOU/WedderburnMass/confinement_categorical.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/WedderburnMass/confinement_categorical.lean

### `confinement_categorical`  —  line 86  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem confinement_categorical [ctx : ConfinementCategoricalContext] : ctx.E_infinity_00 = (Finset.range ctx.n_blocks).sum (fun lam => ctx.e_block lam) ∧ (∀ x : ctx.A, ctx.integral x = ctx.integral (ctx.pi_centre x)) ∧ (∀ x : ctx.A, ctx.observable x → ctx.pi_centre x = x) `
- **Cited:** `[manuscript]`, `[manuscript]`, `[manuscript]`
  - [manuscript] quantum-observable-universe/mass-theory/confinement-categorical.md
  - [manuscript] prop:spectral-sequence-collapse
  - [manuscript] prop:confinement-categorical
- **Tractability:** E∞ = Σ block energies + central-integral invariance; repo Wedderburn/center infra.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.
