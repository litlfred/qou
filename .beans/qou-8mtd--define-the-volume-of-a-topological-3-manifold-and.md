---
# qou-8mtd
title: Define the volume of a topological 3-manifold and connect it to the triangulation volume
status: todo
type: task
priority: high
parent: m015
tags:
    - hyperbolic-volume
    - mathlib-gap
    - open-problem
created_at: 2026-08-10T18:00:39Z
updated_at: 2026-08-10T18:00:39Z
---

**The gap the exposition arc made visible but did not narrow.**

`QOU/MathlibExt/IdealTriangulation.lean` now defines the volume **of a triangulation** —
`IdealTetrahedron.volume = D(z)`, `IdealTriangulation.volume = Σᵢ D(zᵢ)` — with
`volume_rotate` proving it independent of the edge labelling, so it is a property of the
tetrahedron rather than of the bookkeeping. All sorry-free and pinned in the axiom guard.

**What is still undefined: the volume of a topological 3-manifold.** Nothing connects an
`IdealTriangulation` to a knot complement. So the corpus can say "the volume of *this
triangulation* is `3·D(y₁)`" and cannot say "`Vol(5₂) = 3·D(y₁)`", because the left-hand
side has no referent. `VOL_5_2` is *defined* as `3·D(y₁)` (`FiveTwoVolumeConstant.lean`)
— a definition, not a computation of an invariant.

## What closing this requires

1. **A notion of hyperbolic 3-manifold** — Mathlib has none. Minimally a complete
   finite-volume hyperbolic structure, enough to state that a volume exists and is a
   number.
2. **Volume as a topological invariant** — Mostow rigidity. This is what makes "the
   volume of the complement" well-posed independently of any triangulation.
3. **The bridge: a triangulation *of* a manifold.** That an ideal triangulation whose
   shapes satisfy the gluing equations, all positively oriented, realises the complete
   structure — Thurston hyperbolisation. Only then does `Σᵢ D(zᵢ) = Vol(M)` become a
   theorem rather than a definition.

## Discipline (do not shortcut)

- **Do not axiomatise the bridge and call it discharged.** A `class` carrying
  `triangulationVolumeEqManifoldVolume` as a field, consumed downstream, is
  §"Axiomatization is NOT a Proof". The honest intermediate is a *conditional* result in
  the §3b-cond shape, with the hypothesis named and visible in the type.
- **Do not restate `VOL_5_2 := 3·D(y₁)` as evidence.** It is a definition; the numerical
  agreement with the literature (2.828122088330783) is evidence the definition was chosen
  well, not proof that it is the invariant.
- Numerical agreement at more knots is **not** progress on this bean. The gap is
  definitional, not quantitative.

## Realistic scoping

Step 1 alone is a Mathlib-scale project. A defensible smaller win: state the bridge as a
named conditional hypothesis (content-bearing class, no instance — the honest "open"
state per §3b-tax) so downstream statements can be *explicitly* conditional rather than
silently ambiguous about which volume they mean.

Surfaced by PR #4925 (`thm:ideal-tetrahedron-volume-well-defined`); the same caveat is
stated in every block of the gluing/volume arc.
