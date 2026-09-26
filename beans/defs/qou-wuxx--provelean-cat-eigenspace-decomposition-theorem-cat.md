---
# qou-wuxx
title: 'PROVE(lean): cat_eigenspace_decomposition — theorem cat_eigenspace_decomposition [ctx : CatEigenspaceDecompositionContext] : ctx.m_rho [cited manuscript]'
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

**File:** `QOU/TopologicalMass/cat_eigenspace_decomposition.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/TopologicalMass/cat_eigenspace_decomposition.lean

### `cat_eigenspace_decomposition`  —  line 63  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem cat_eigenspace_decomposition [ctx : CatEigenspaceDecompositionContext] : ctx.m_rho = ctx.nrm (ctx.tr (ctx.tau_hat ctx.α)) + ctx.nrm (ctx.tr (ctx.α - ctx.tau_hat ctx.α)) `
- **Cited:** `[manuscript]`
  - [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-cat-eigenspace.md
- **Tractability:** m_rho = nrm(tr(τ̂ α)) + nrm(tr(α−τ̂ α)) eigenspace split; repo categorical-trace infra.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.
