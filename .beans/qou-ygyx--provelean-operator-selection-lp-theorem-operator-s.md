---
# qou-ygyx
title: 'PROVE(lean): operator_selection_lp — theorem operator_selection_lp [ctx : OperatorSelectionLpContext] : OperatorSelectionLpCont [cited bertsimas1997,manuscript]'
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

**File:** `QOU/ParticleInteractions/operator_selection_lp.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/ParticleInteractions/operator_selection_lp.lean

### `operator_selection_lp`  —  line 99  ·  tier **B** (infra-blocked / open-conjecture)
- **Proposition:** `theorem operator_selection_lp [ctx : OperatorSelectionLpContext] : OperatorSelectionLpContext.IsFeasible ctx.x_star ∧ (∀ x : Fin ctx.d → ℝ, OperatorSelectionLpContext.IsFeasible x → OperatorSelectionLpContext.objective ctx.x_star ≤ OperatorSelectionLpContext.objective x) ∧ OperatorSelectionLpContext`
- **Cited:** `[bertsimas1997]`, `[manuscript]`, `[bertsimas1997]`
  - [bertsimas1997] Bertsimas, Tsitsiklis (1997), *Introduction to Linear Optimization* — (no DOI/URL)
  - [manuscript] quantum-observable-universe/mass-theory/operator-selection-lp.md
- **Tractability:** LP optimality of x_star (feasible + objective-minimising); LP optimality certificate, Mathlib lacks the duality library.
- **Next step:** Infra-blocked: needs Mathlib theory that does not exist. Track upstream; do not launder via axiom/class.
