---
# qou-9gpo
title: 'PROVE(lean): confinement_frobenius_reciprocity — theorem confinement_frobenius_reciprocity [ctx : ConfinementFrobeniusReciprocityContext] : [cited bertsimas1997,manuscript]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-qou
    - infra-blocked
    - cite-bertsimas1997
created_at: 2026-08-01T23:31:07Z
updated_at: 2026-08-01T23:31:07Z
parent: qou-k1mq
---

**File:** `QOU/ParticleInteractions/confinement_frobenius_reciprocity.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/ParticleInteractions/confinement_frobenius_reciprocity.lean

### `confinement_frobenius_reciprocity`  —  line 107  ·  tier **B** (infra-blocked / open-conjecture)
- **Proposition:** `theorem confinement_frobenius_reciprocity [ctx : ConfinementFrobeniusReciprocityContext] : (∀ O : ctx.Observable, ctx.physExp O = ∑ i ∈ ctx.A_star, ∑ j ∈ ctx.A_star, ctx.u_star i * ctx.Ginv i j * ctx.pairing O j) ∧ (∃ i : Fin ctx.d, ctx.x_star i ≠ 0) ∧ 0 < ctx.y_0_star ∧ ctx.A_star.Nonempty ∧ (∀ i :`
- **Cited:** `[bertsimas1997]`, `[manuscript]`, `[bertsimas1997]`
  - [bertsimas1997] Bertsimas, Tsitsiklis (1997), *Introduction to Linear Optimization* — (no DOI/URL)
  - [manuscript] quantum-observable-universe/particle-interactions/confinement-frobenius-reciprocity.md
- **Tractability:** physExp = Σ shadow-price·Ginv·pairing + nonempty active set; LP duality (active set = positive duals) Mathlib lacks.
- **Next step:** Infra-blocked: needs Mathlib theory that does not exist. Track upstream; do not launder via axiom/class.
