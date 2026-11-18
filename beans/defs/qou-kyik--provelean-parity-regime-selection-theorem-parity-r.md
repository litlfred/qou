---
# qou-kyik
title: 'PROVE(lean): parity_regime_selection — theorem parity_regime_selection [ctx : ParityRegimeSelectionContext] : ctx.sign_val = (-(1 [cited manuscript]'
status: in-progress
type: task
priority: normal
tags:
    - paper-qou
    - repo-infra
    - reorg-2026-10-04
    - lean
    - cited-sorry
created_at: 2026-08-01T23:31:07Z
updated_at: 2026-11-18T07:45:11Z
parent: qou-l2vh
---

**File:** `QOU/ParticleInteractions/parity_regime_selection.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/folio/quantum-observable-universe/lean/QOU/ParticleInteractions/parity_regime_selection.lean

### `parity_regime_selection`  —  line 77  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem parity_regime_selection [ctx : ParityRegimeSelectionContext] : ctx.sign_val = (-(1 : ℝ)) ^ (ctx.A - 1) ∧ (Odd ctx.A → 3 ≤ ctx.A → ctx.Q_value = |ctx.S_Delta| * ctx.m_e) ∧ (Even ctx.A → ctx.Q_value = (ctx.Sigma_FP + 1) * ctx.m_e) ∧ (ctx.A = 1 → ctx.Q_value = (ctx.S_Delta + 1) * ctx.m_e) `
- **Cited:** `[manuscript]`, `[manuscript]`
  - [manuscript] quantum-observable-universe/particle-interactions/parity-regime-selection.ts
- **Tractability:** sign_val = (−1)^{A−1} + parity-split Q-value regimes; arithmetic/parity over context class.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.

## Round 82 Progress (PR #8389)
- Branch: `feat/round82-confdiff-gevreypos-hyproot-tracesq-normchain-43c1`
- Commit 1 (code + probe): `9fc5597f0f6558c185cf46ffd6acdc86ad1d4b21`
- Commit 2 (witness): `4a084d4105014f8457a64297f35613ebb0f95d6b` (`scriptSha256 = 0b271ed473fcb7e2f06260119e75930af659f57c2419e9542b05b4df69271355`)
