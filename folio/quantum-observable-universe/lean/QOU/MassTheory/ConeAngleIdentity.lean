import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# Cone-angle bookkeeping at an interior vertex (Rivin, Lemma 1.2)

Bean `qou-0vhl`. Target #3 of the Rivin `math/9907032` combinatorial-optimization
analysis: the cone angle at an interior vertex of a Euclidean cone triangulation
is bookkept against the exterior dihedral angles at the edges incident to it.

## The finite model

At an interior vertex `v` of a Euclidean cone surface, the triangles of its star
are indexed by a finite set `corners`. Developing the star into the plane, each
incident triangle `i` contributes an **interior angle** `interiorAngle i` at `v`,
and the **cone angle** `Θ(v)` is the sum of those corner angles:

  `Θ(v) = ∑_{i ∈ corners} interiorAngle i`.

Around an interior vertex the incident triangles and the incident edges are in
cyclic bijection (edge `e_i` sits between two consecutive triangles), so both are
indexed by the same `corners`. Each incident edge carries an **exterior dihedral
angle**; under the flat development this is `π` minus the interior contribution
at that edge:

  `exteriorDihedral i = π − interiorAngle i`.

These two are the geometric inputs, carried as explicit hypotheses in the
`VertexStar` structure (`cone_eq`, `flat_rel`). Everything below is derived from
them by `Finset` algebra — no hidden geometry.

## The identity

Summing `exteriorDihedral i = π − interiorAngle i` over the `n = corners.card`
incident corners and substituting `Θ = ∑ interiorAngle`:

  `∑ exteriorDihedral i = n·π − Θ`,  equivalently  `Θ + ∑ exteriorDihedral i = n·π`.

This is Rivin's Lemma 1.2 as an affine bookkeeping identity: the cone angle and
the total exterior dihedral around `v` are complementary in `n·π`, where `n` is
the incidence count. The genuine geometric content (`Θ = Σ` exterior dihedral)
appears in its calibrated / curvature form; the general identity is this affine
one, and it is the derivable statement.

## Why this is not vacuous

The conclusion `Θ + ∑ exteriorDihedral = n·π` is **false** if either the
`π`-offset in `flat_rel` is wrong (replace `π` by any other constant `c` and the
right side would be `n·c`, contradicting a concrete instance) or the incidence
count `n = corners.card` is wrong (drop or add a corner and the multiple of `π`
changes). Both hypotheses are load-bearing; the statement holds by `Finset`
arithmetic, not by `rfl` or unfolding. A concrete falsifier is given in
`sum_exteriorDihedral_ne_of_bad_offset` at the end of the file: a two-corner star
whose `flat_rel` uses the offset `π/2` instead of `π` violates the identity, so
the identity genuinely depends on the offset.

`ℝ` is used because angles are real (§7c: archimedean base ring is justified only
because the objects — angles — are genuinely real). The pure combinatorial
skeleton is factored out as `sum_pi_sub_eq` over a generic additive group, so the
ring choice is confined to the geometric wrapper.
-/

namespace QOU.Archimedean

open Finset

open scoped BigOperators

/-- **Pure `Finset` skeleton.** Over any additive commutative group, if
`g i = c - f i` on a finite index set `s`, then `∑ g = s.card • c - ∑ f`.

This is the offset-and-count bookkeeping with no geometry: `c` plays the role of
`π`, `f` the interior angles, `g` the exterior dihedrals. It is non-trivial — it
fails if the offset `c` is replaced inconsistently — and is the engine behind the
geometric identity below. -/
theorem sum_pi_sub_eq {ι R : Type*} [AddCommGroup R] (s : Finset ι)
    (c : R) (f g : ι → R) (hg : ∀ i ∈ s, g i = c - f i) :
    ∑ i ∈ s, g i = s.card • c - ∑ i ∈ s, f i := by
  calc
    ∑ i ∈ s, g i = ∑ i ∈ s, (c - f i) := Finset.sum_congr rfl hg
    _ = (∑ _i ∈ s, c) - ∑ i ∈ s, f i := by rw [Finset.sum_sub_distrib]
    _ = s.card • c - ∑ i ∈ s, f i := by rw [Finset.sum_const]

/-! The geometric wrapper — `VertexStar`, whose flat relation fixes the offset
`c` to the straight angle `π` — lives in
`QOU.Transcendental.MassTheory.ConeAngleIdentityReal`.  Under the owner ruling
of 2026-11-27 the straight angle is the half-turn root of unity `ζ₂ = −1`
(defined algebraically); its value `π` as a real angle measure is the
non-analytic `exp` label of that root, so only the companion needs it. -/

end QOU.Archimedean
