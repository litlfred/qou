---
# qou-sd8y
title: 'BUILD: re-base Archimedean.HyperbolicMetric.dH on Mathlib Geometry/Manifold/Riemannian PathELength'
status: todo
type: task
priority: normal
created_at: 2026-09-04T09:08:08Z
updated_at: 2026-09-04T09:08:08Z
parent: qou-8lxd
---

**BUILD — a method proposal for an already-open gap, not a new gap.**

`QOU/Archimedean/HyperbolicMetric.lean:131` defines

    noncomputable def dH (x y : E) : ℝ≥0∞

as an infimum of path lengths, hand-rolled. The existing bean *"GAP: hyperbolic dH
metric axioms — symmetry, triangle, separation"* records what is unproved about it.
This bean records that **upstream API now exists to prove it against**.

**Mathlib status, measured 2026-09-04 at `f897ebcf72c`:**
`Mathlib/Geometry/Manifold/Riemannian/{Basic,PathELength}.lean` package exactly the
construction — `class IsRiemannianManifold I M : Prop` is literally *"the distance is
the infimum of lengths of paths"*, with `ContMDiffRiemannianMetric`,
`riemannianMetricVectorSpace`, and `EmetricSpace.ofRiemannianMetric`. `PathELength.lean`
carries the measurability/integrability plumbing the symmetry and triangle proofs need
(`MeasureTheory/Function/JacobianOneDim`, `MeasurePreserving` on `Icc`,
`Measure.Subtype.measureSpace`). Also `Geometry/Manifold/VectorBundle/Riemannian.lean`
and `Topology/VectorBundle/Riemannian.lean`.

**What Mathlib still does NOT give**, so the gap does not close by import:
* no Riemannian **volume measure** — this is why `Archimedean/HyperbolicVolumeMeasure.lean`
  builds `μ_hyp` by hand and must;
* no curvature (`grep -rln 'curvature' Mathlib/` → 1 hit, `Measure/Doubling.lean`,
  unrelated);
* no geodesics as a named object.

**Size: medium.** The value is not the lines saved, it is that the three open metric
axioms become theorems against an upstream interface instead of hand proofs.

**Do NOT read this as "the hyperbolic gap is closed."** `qou-5gai`'s ℍ³ verdict stands.
What is corrected there is one sentence about ℍ² — see the false-claim bean filed
alongside this one.

Source: `docs/audits/2026-09-04-mathlib-infrastructure-inventory.md` §B5, §H3.
