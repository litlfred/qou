---
# qou-e524
title: 'Infra: categorical Frobenius descent (mass functor)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-04T01:39:43Z
updated_at: 2026-11-16T19:27:00Z
parent: qou-rtxm
---

Blocks: cat_descended_is_base_mass (2), cat_eigenspace_decomposition (1), mass_categorical_descent (1), confinement_categorical (1 — needs Hochschild vanishing). Need Frobenius trace intertwining formalized.

## 2026-11-16 — Categorical Frobenius Descent (`QOU.Foundations.ConventionDFrobeniusMarkovTower`, PR #8166)
- Formalized `frobeniusTotalTrace`, `frobeniusMassWeightedTrace`, `frobenius_trace_intertwining_descent`, and `cat_eigenspace_projector_orthogonality` in `folio/quantum-observable-universe/lean/QOU/Foundations/ConventionDFrobeniusMarkovTower.lean` (pure Lean 4 core, generic `CommRingOps R` per §7c, `0` `sorry`, `0` warnings, `0` vacuity audit hits; wired into `QOU.lean`).
- Commit: `246ab0f17af473b433e680ddc0223712e5c0d13c` | PR: `https://github.com/litlfred/qou/pull/8166`
- Kept at `status: in-progress` per merge-manager protocol.
