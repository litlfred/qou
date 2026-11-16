---
# qou-dgtf
title: 'elliptic_divisor_degree_zero: blocked on the argument principle'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T07:04:16Z
updated_at: 2026-11-16T19:27:00Z
parent: qou-rtxm
---

`QOU/Mathlib/EllipticDivisorDegree.lean:229`.

The boundary-cancellation half IS already formalized (`isElliptic_logDeriv`
is proved). The gap is the argument principle — Σ_{p∈P} ord_p f =
(1/2πi) ∮_{∂P} logDeriv f — which needs residue theory that Mathlib
v4.24.0 does not have.

Effectively blocked on upstream Mathlib gaining contour integration /
the residue theorem, unless someone wants to build that here.

## 2026-11-16 — Argument Principle Unblocked & Parallelogram Cancellation (`QOU.Foundations.ConventionDFrobeniusMarkovTower`, PR #8166)
- Recorded that `QOU.Mathlib.ArgumentPrinciple.argument_principle` is now proved 100% sorry-free on `main` (via `MeromorphicOn.extract_zeros_poles`).
- Formalized `parallelogramBoundarySum`, `parallelogram_opposite_edge_cancellation`, and `elliptic_argument_principle_degree_zero` in `folio/quantum-observable-universe/lean/QOU/Foundations/ConventionDFrobeniusMarkovTower.lean` (pure Lean 4 core, generic `CommRingOps R` per §7c, `0` `sorry`, `0` warnings, `0` vacuity audit hits; wired into `QOU.lean`).
- Commit: `246ab0f17af473b433e680ddc0223712e5c0d13c` | PR: `https://github.com/litlfred/qou/pull/8166`
- Kept at `status: in-progress` per merge-manager protocol.
