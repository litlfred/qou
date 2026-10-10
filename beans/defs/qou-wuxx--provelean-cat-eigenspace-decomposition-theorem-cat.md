---
# qou-wuxx
title: 'cat_eigenspace_decomposition: norm additivity (Pythagoras for the Frobenius pairing) — needs a pairing construction'
status: todo
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:09Z
updated_at: 2026-10-10T06:49:34Z
parent: qou-thkm
---

**File:** `QOU/TopologicalMass/cat_eigenspace_decomposition.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/TopologicalMass/cat_eigenspace_decomposition.lean

### `cat_eigenspace_decomposition`  —  line 63  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem cat_eigenspace_decomposition [ctx : CatEigenspaceDecompositionContext] : ctx.m_rho = ctx.nrm (ctx.tr (ctx.tau_hat ctx.α)) + ctx.nrm (ctx.tr (ctx.α - ctx.tau_hat ctx.α)) `
- **Cited:** `[manuscript]`
  - [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-cat-eigenspace.md
- **Tractability:** m_rho = nrm(tr(τ̂ α)) + nrm(tr(α−τ̂ α)) eigenspace split; repo categorical-trace infra.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.



## 2026-10-10 — consolidated (owner-approved, session_01ST9RpvTF7JHNdUNafrjf9J)
Re-homed under thread qou-thkm. Previous parent: qou-l2vh.


## 2026-10-10 re-scope (session_01ST9RpvTF7JHNdUNafrjf9J)
File reworked 2026-09-03: split_eq tautology labelled, transient_antiInvariant proved, old statement refuted at free data (not_cat_eigenspace_decomposition_of_free_data). Remaining gap: norm additivity. Kept OPEN (13a). Blocked by qou-e524.
