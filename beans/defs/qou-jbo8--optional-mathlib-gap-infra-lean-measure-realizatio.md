---
# qou-jbo8
title: 'Optional Mathlib-gap infra: Lean measure-realization of G_k via gaussianReal mgf — NOT cheap (cost estimate corrected 2026-08-01)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T15:13:34Z
updated_at: 2026-10-04T15:21:51Z
parent: qou-c8p8
---

Goal: realize the SW Gaussian factor `G_k = q̃^{k(k−1)/2}` as the moments of
an actual measure, upgrading `SWJacksonMomentFactorization` from a moment-
sequence identity to a measure statement. The target is the log-normal
`LN(−L/2, L)` with `L = ln q̃`: for `X ~ N(μ, σ²)`, `E[e^{kX}] = e^{kμ +
k²σ²/2}`, and at `μ = −L/2`, `σ² = L` this is `e^{L(k²−k)/2} = q̃^{k(k−1)/2}
= G_k` exactly.

**Cost estimate CORRECTED (2026-08-01).** This was originally beaned as
"the cheap leg" on the assumption that Mathlib exposes the moment
generating function of `gaussianReal`. **It does not, in the pinned
toolchain (v4.24.0).** Probed directly against the restored oleans:

- `ProbabilityTheory.gaussianReal : ℝ → NNReal → Measure ℝ` — exists.
- `ProbabilityTheory.mgf` — exists, but only generically.
- `integral_gaussianReal` — does not exist (unknown identifier).
- `exact?` on the goal
  `∫ x, Real.exp (t * x) ∂(gaussianReal m v) = Real.exp (m * t + v * t^2 / 2)`
  fails to close it.

So the mgf identity itself would have to be proved from scratch — a genuine
Gaussian-integral analysis task (complete the square under the integral,
justify integrability, evaluate the shifted Gaussian), not a citation. That
is a Mathlib-contribution-sized piece of work, not a one-liner.

**Recommendation.** Leave this OPTIONAL and unstarted unless a Lean chain
actually needs to consume the SW identification as a *measure* statement.
Nothing in the merged tranche (PR #4446) does: the factorization, the
SW-core Jacobi closed form, and the tropical transport are all moment-level
algebra and are complete without it. If it is picked up, budget it as a
Mathlib PR (`mgf_gaussianReal`), not as repo infra.

Sibling leg: `qou-x1rm` (compact-support ⇒ StieltjesDeterminate via
Stone–Weierstrass) — same optional status, likewise not on any critical path.
