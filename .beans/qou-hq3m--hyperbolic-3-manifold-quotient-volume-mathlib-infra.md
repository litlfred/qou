---
# qou-hq3m
title: 'Mathlib infra: the volume of a hyperbolic 3-manifold as a quotient of H^3'
status: in-progress
type: task
priority: high
parent: qou-8mtd
tags:
    - hyperbolic-volume
    - mathlib-gap
    - lean
created_at: 2026-08-29T18:40:00Z
updated_at: 2026-08-29T18:40:00Z
---

Child of `qou-8mtd`, taking its open half: "hyperbolic 3-manifolds in Mathlib,
Mostow rigidity, Thurston hyperbolisation — add needed Mathlib infra."

## What the corpus ALREADY has (measured, not assumed)

`qou-8mtd`'s framing — and the header I wrote for `ManifoldVolumeBridge` — says
Mathlib has no hyperbolic 3-manifolds. True of Mathlib. **Badly misleading about
this corpus**, which carries a substantial `QOU/Archimedean/` hyperbolic layer:

| module | state |
|---|---|
| `HyperbolicVolumeMeasure` | `upperHalfSpace`, `hypDensity = 1/z³`, `hypVolume`, **0 sorries** |
| `IdealTetrahedronRegion` | chimney regions, **0 sorries** |
| `TotallyGeodesicFaces` | vertical planes + hemispheres totally geodesic, **0 sorries** |
| `HyperbolicMetric` | `dH` path metric, `IsDHIsometry`, 3 sorries |
| `MostowIdealTetVolume` | 7 sorries |
| `IdealTriangulation` | shape triple `param_prod = -1`, `param_im_pos`, `volume_rotate` — all proved |

So the ideal-tetrahedron and volume-density sides are largely DONE. Anyone
starting here from `qou-8mtd`'s wording would rebuild a lot of it.

## The actual gap

There is a measure on H³ and there are individual isometries. There is **no
group acting, no discrete subgroup, and no quotient.** That is the whole
distance between "we have H³" and "we have a hyperbolic 3-manifold":

    H³  --(Γ acts, discrete, free)-->  H³/Γ  =  the manifold

and it is why `MostowRigidity.volume` has to be an *entered literal* and why
`HyperbolicVolumeBridge.vol` has to be an assumed field. Neither has anything to
attach to.

## The target, and why it is provable rather than assumable

Mathlib has `MeasureTheory.IsAddFundamentalDomain.measure_eq`: two fundamental
domains for a countable group acting by measure-preserving maps have equal
measure. Its hypotheses are exactly `[AddGroup G] [AddAction G α]
[MeasurableVAdd G α] [VAddInvariantMeasure G α μ] [Countable G]`.

And the corpus already proves the hard input: `hypVolume_add_left` says
`hypVolume ((v + ·) ⁻¹' s) = hypVolume s` whenever `v 2 = 0` — which IS the
`VAddInvariantMeasure` condition for horizontal translations.

So the volume of the quotient can be **derived** rather than posited:

1. `horizontal : AddSubgroup (Fin 3 → ℝ)` — the zero-height vectors.
2. `VAddInvariantMeasure Γ (Fin 3 → ℝ) hypVolume` for `Γ ≤ horizontal`,
   proved from `hypVolume_add_left`. **This is the content.**
3. The quotient volume, well-defined: any two fundamental domains agree.

That gives "the volume of a hyperbolic 3-manifold" an actual referent in at
least one genuine case, instead of a class field.

## What this will NOT do

Mostow rigidity and Thurston hyperbolisation stay open, and no route here
touches them. A horizontal-translation quotient is a real hyperbolic 3-manifold
but a very special one (a cusp); it is not a knot complement, and nothing here
makes `Vol(4_1)` computable. The point is to replace *assumed* volume with
*derived* volume in one honest case, and to leave the general bridge conditional
exactly as it is.
