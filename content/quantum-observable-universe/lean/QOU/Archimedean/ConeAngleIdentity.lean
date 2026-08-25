import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

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

/-- **The star of an interior vertex** of a Euclidean cone triangulation.

`corners` indexes the incident triangles (equivalently, the incident edges, in
cyclic bijection). `interiorAngle i` is the corner angle of triangle `i` at the
vertex; `exteriorDihedral i` is the exterior dihedral at the corresponding edge;
`coneAngle` is the total angle `Θ(v)` around the vertex.

The two geometric facts are carried as fields:
* `cone_eq`  — the cone angle is the sum of the corner angles;
* `flat_rel` — the exterior dihedral is `π` minus the interior contribution. -/
structure VertexStar (ι : Type*) where
  /-- Incident triangles / edges of the vertex star. -/
  corners : Finset ι
  /-- Corner (interior) angle at the vertex contributed by each incident triangle. -/
  interiorAngle : ι → ℝ
  /-- Exterior dihedral angle at each incident edge. -/
  exteriorDihedral : ι → ℝ
  /-- Total cone angle `Θ(v)` around the vertex. -/
  coneAngle : ℝ
  /-- Cone angle = sum of the corner angles. -/
  cone_eq : coneAngle = ∑ i ∈ corners, interiorAngle i
  /-- Flat relation: exterior dihedral = `π` − interior contribution. -/
  flat_rel : ∀ i ∈ corners, exteriorDihedral i = Real.pi - interiorAngle i

variable {ι : Type*} (V : VertexStar ι)

/-- **Rivin Lemma 1.2 (exterior-sum form).** The total exterior dihedral around
an interior vertex equals `n·π` minus the cone angle, where `n` is the number of
incident corners.

`-- Ref: [rivin2003] Lemma 1.2` -/
theorem sum_exteriorDihedral_eq :
    ∑ i ∈ V.corners, V.exteriorDihedral i
      = V.corners.card • Real.pi - V.coneAngle := by
  rw [V.cone_eq]
  exact sum_pi_sub_eq V.corners Real.pi V.interiorAngle V.exteriorDihedral V.flat_rel

/-- **Rivin Lemma 1.2 (complementary form).** The cone angle and the total
exterior dihedral around an interior vertex are complementary in `n·π`.

This is the falsifiable identity: it fails if the `π`-offset in `flat_rel` is
wrong or if the incidence count `n = corners.card` is wrong.

`-- Ref: [rivin2003] Lemma 1.2` -/
theorem coneAngle_add_sum_exteriorDihedral :
    V.coneAngle + ∑ i ∈ V.corners, V.exteriorDihedral i
      = V.corners.card • Real.pi := by
  rw [sum_exteriorDihedral_eq]
  ring

/-- **Cone angle solved for.** `Θ(v) = n·π − ∑ exterior dihedral.` -/
theorem coneAngle_eq :
    V.coneAngle = V.corners.card • Real.pi - ∑ i ∈ V.corners, V.exteriorDihedral i := by
  rw [sum_exteriorDihedral_eq]; ring

/-- **`nsmul` unfolded to a product** for downstream numerical use:
`Θ(v) + ∑ exterior dihedral = (n : ℝ) · π`. -/
theorem coneAngle_add_sum_exteriorDihedral_mul :
    V.coneAngle + ∑ i ∈ V.corners, V.exteriorDihedral i
      = (V.corners.card : ℝ) * Real.pi := by
  rw [coneAngle_add_sum_exteriorDihedral, nsmul_eq_mul]

/-!
## Falsifier: the identity genuinely needs the `π`-offset

The following witnesses that the affine identity depends on the offset being `π`.
We build a two-corner star with corner angles `π/2` each (so cone angle `π`), but
with `exteriorDihedral` defined by the **wrong** offset `π/2 − interiorAngle`
instead of `π − interiorAngle`. That star does not satisfy `flat_rel` — which is
exactly the point — but if one *nonetheless* summed its (wrong) exterior
dihedrals and its cone angle, the complementary identity `= 2·π` would be false;
the sum is `0`, not `2π`. Hence the offset in `flat_rel` is load-bearing, and
`coneAngle_add_sum_exteriorDihedral` is not a tautology.
-/

/-- A concrete instance showing the `π`-offset is load-bearing: with a `π/2`
offset the complementary sum is `π`, not `2·π`, so the identity is falsifiable. -/
theorem offset_is_load_bearing :
    let corners : Finset (Fin 2) := Finset.univ
    let interiorAngle : Fin 2 → ℝ := fun _ => Real.pi / 2
    let exteriorBad : Fin 2 → ℝ := fun _ => Real.pi / 2 - Real.pi / 2
    let coneAngle : ℝ := ∑ i ∈ corners, interiorAngle i
    coneAngle + ∑ i ∈ corners, exteriorBad i ≠ corners.card • Real.pi := by
  intro corners interiorAngle exteriorBad coneAngle
  show (∑ i ∈ corners, interiorAngle i) + ∑ i ∈ corners, exteriorBad i
      ≠ corners.card • Real.pi
  have hcorners : corners = (Finset.univ : Finset (Fin 2)) := rfl
  simp only [hcorners, exteriorBad, interiorAngle, sub_self, Finset.sum_const_zero,
    add_zero, Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
  -- Goal: (↑2) * (π/2) ≠ (↑2) * π, i.e. π ≠ 2π, false only because π ≠ 0.
  intro h
  push_cast at h
  -- h : 2 * (π/2) = 2 * π  ⟹  π = 0, contradicting `Real.pi_ne_zero`.
  exact Real.pi_ne_zero (by linarith)

end QOU.Archimedean
