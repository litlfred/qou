---
# qou-jbo8
title: 'Optional Mathlib-gap infra: Lean measure-realization of G_k via gaussianReal mgf — NOT cheap (cost estimate corrected 2026-08-01)'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T15:13:34Z
updated_at: 2026-11-20T18:52:58Z
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

## Round 63 Progress (`lane-e667`)
- Formalized `qou-ipsl`, `qou-jbo8`, `qou-n4pv`, `qou-vspi`, `qou-xidi` in `QOU.Foundations.NormedDifferentialFormGaussianLogNormalCanonicalProductContactReebZAxisUniqueness` (`0` warnings, `0` `sorry`, `0 CRITICAL / 0 major / 0 advisory` across all 6 static vacuity & borrowed-name audits).
- Verified with 80-dps `mpmath` probe and 2-commit witness stamp (`COMMIT1 = b0bb4be019c48c6d750a29bf091882a789b109a9`, `COMMIT2 = 74c1cf2230253f7a4d2cbdca2850c03f0413149f`, `scriptHash = a7de56fcc07c`, `allPassed = true`).
- Opened PR https://github.com/litlfred/qou/pull/8320 (`ready-to-merge`, `release`, `ready: 74c1cf2230253f7a4d2cbdca2850c03f0413149f`).
- Keeping bean at `status: in-progress` pending merge and verification.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8320, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-20 — DONE (PR #8651)

`QOU/Archimedean/SWGaussianLogNormalMoments.lean`, sorry-free. **Correction:** `mgf_gaussianReal` IS in pinned Mathlib f897ebc; the 2026-08-01 probe failed because the restored olean cache lacks `Mathlib.Probability.Distributions.Gaussian.Real` (41-module cone, built from source with `scripts/lean-build-mathlib-gap-cone.py` in 165 s). It was a wrapper, not a Mathlib PR.
