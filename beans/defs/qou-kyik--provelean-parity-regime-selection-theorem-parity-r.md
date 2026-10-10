---
# qou-kyik
title: 'PROVE(lean): parity_regime_selection — theorem parity_regime_selection [ctx : ParityRegimeSelectionContext] : ctx.sign_val = (-(1 [cited manuscript]'
status: todo
type: task
priority: normal
tags:
    - paper-qou
    - repo-infra
    - reorg-2026-10-04
    - lean
    - cited-sorry
created_at: 2026-08-01T23:31:07Z
updated_at: 2026-10-04T15:22:42Z
parent: qou-l2vh
---

**File:** `QOU/ParticleInteractions/parity_regime_selection.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/ParticleInteractions/parity_regime_selection.lean

### `parity_regime_selection`  —  line 77  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem parity_regime_selection [ctx : ParityRegimeSelectionContext] : ctx.sign_val = (-(1 : ℝ)) ^ (ctx.A - 1) ∧ (Odd ctx.A → 3 ≤ ctx.A → ctx.Q_value = |ctx.S_Delta| * ctx.m_e) ∧ (Even ctx.A → ctx.Q_value = (ctx.Sigma_FP + 1) * ctx.m_e) ∧ (ctx.A = 1 → ctx.Q_value = (ctx.S_Delta + 1) * ctx.m_e) `
- **Cited:** `[manuscript]`, `[manuscript]`
  - [manuscript] quantum-observable-universe/particle-interactions/parity-regime-selection.ts
- **Tractability:** sign_val = (−1)^{A−1} + parity-split Q-value regimes; arithmetic/parity over context class.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.
