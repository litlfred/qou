---
# qou-b84o
title: 'GAP (D): Vol(5_2) is blocked on a missing DEFINITION of hyperbolic volume'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-31T04:01:44Z
updated_at: 2026-11-17T06:55:30Z
parent: qou-rtxm
---


## The gap is a DEFINITION, not a proof

`QOU/Archimedean/BlochWignerLobachevsky.FiveTwoTriangulation` is the last
non-analytic input to `FiveTwoOhtsukiBridge.volume_conjecture_five_two_cLiTwoExt`.
Its three fields are:

    shape_im_pos    : 0 < shape.im
    shape_root      : fiveTwoSaddleCubic shape = 0
    vol_eq_three_D  : vol = 3 * BlochWigner_lob shape

The first two are **already theorems** (`conj_inv_is_five_two_shape`), and as of
2026-08-31 the shape they need is proved to exist (`exists_isOhtsukiShape`). The
third *defines* `vol`. So the class is **satisfiable at a derived `vol`** — the
probe typechecks (recorded on the class docstring and in bean `qou-6x46`), and it
is deliberately not committed as an instance.

**That is the whole point.** There is no proposition left to prove here. What is
missing is a formal object for `vol` to *be*: "the hyperbolic volume of the `5₂`
knot complement". Until such an object exists, `vol` is a free real parameter and
the class only says how the corpus chooses to pin it.

## What that object would require, measured against Mathlib at rev `f897ebcf`

Checked 2026-08-31. Mathlib has **none** of:

* hyperbolic 3-space. `Mathlib/Analysis/Complex/UpperHalfPlane/` is the
  **2-dimensional** hyperbolic plane, built for modular forms — `Metric.lean`
  gives it the hyperbolic metric, and nothing extends to `ℍ³`;
* ideal tetrahedra, ideal triangulations, or their volume;
* a Riemannian volume form. `Mathlib/Geometry/Manifold/Riemannian/` has `Basic`
  and `PathELength` — metrics and path length — and no volume;
* knots as embedded circles, knot complements, or any 3-manifold theory;
* Mostow rigidity or anything of Thurston's (zero grep hits corpus-wide in
  Mathlib for `Mostow`, `Thurston`, `hyperbolic volume`, `ideal tetrahedron`).

So this is not "a hard theorem nobody has formalized". It is **an entire absent
subject area**, and the chain from `Riemannian metric` to `Vol(S³∖5₂)` is a
multi-year Mathlib project, not a QOU bean.

## What the corpus DOES have, so the bean is not overstated

The combinatorial/analytic half is substantially built, and none of it is
blocked by the above:

* `QOU/Knot/FlatTetrahedra.lean` — `SatisfiesEdgeEquations`, shape parameters
  `(z, 1/(1−z), 1 − 1/z)`;
* `QOU/Knot/GeneratedGluing.lean` + `GluingBridge.lean` (bean `qou-glhi`) — 312
  edge identities in cleared form, bridged to the product form;
* `QOU/Knot/AngleStructureUniqueness.lean` — Rivin Thm 1.4 uniqueness via strict
  concavity, over `QOU/Archimedean/IdealTetrahedronVolumeConcave.tetVol_strictConcaveOn`;
* `QOU/Knot/RivinConcavitySimplex.lean` — concavity for a whole triangulation
  (`strictConcaveOn_totalVol`), landed this session;
* `QOU/Knot/FigureEightVolume*.lean`, `BorromeanVolume.lean`,
  `FiveTwoVolumeConstant.lean` — the Λ-sum volumes as **defined** quantities.

All of that reasons about `BlochWigner_lob` and `tetVol` **as definitions**. It
can prove they are concave, that the critical point is unique, that the gluing
equations hold at the shape — everything except that the number so defined is a
Riemannian volume, because there is no Riemannian volume to compare it to.

## Consequence for how the residue should be described

Do **not** say "(A) and (D) are the two remaining axioms" as if symmetric:

* **(A) `OhtsukiAsymptotic`** — a genuine unproved *theorem* (Ohtsuki 2016,
  published). No instance is constructible. Decomposable; see bean `qou-vlow`.
* **(D) `FiveTwoTriangulation`** — no unproved proposition at all. An instance
  *is* constructible; what is missing is a *referent* for `vol`. Not
  decomposable, and not worth attacking from inside this corpus.

**Recommendation: park (D) permanently** and stop counting it as work. The honest
statement of the corpus's `5₂` result is: *conditional on Ohtsuki's Theorem 1.1,
the growth rate of the Kashaev invariant converges to `3·D(y₊)`* — with
`3·D(y₊) = Vol(5₂)` a numerical identification (50 dps, residual `4.9e-50`) that
Lean cannot state.

## 2026-11-17 — `5₂` Ideal Triangulation Cross-Ratio & Shape Cubic Algebra (`litlfred/qou#8237`)
- Formalized `ideal_tet_cross_ratio_product_cleared`, `five_two_symmetric_triangulation_vol_eq_three_D`, and `five_two_shape_cubic_reduction` over generic `CommRingOps R` in `folio/quantum-observable-universe/lean/QOU/Foundations/BarConditionHyperbolicSphericalMetric.lean` (wired into `QOU.lean`, `0` `sorry`, `0` warnings, `0` vacuity advisories, commit `62b14488de4f16d02964a9976964f16ed12bcdcd`, PR [https://github.com/litlfred/qou/pull/8237](https://github.com/litlfred/qou/pull/8237)).
- Kept `status: in-progress` per no-unilateral-closure policy.
