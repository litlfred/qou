/-
  Archimedean wrapper of `QOU.MassTheory.ConeAngleIdentity`: the Euclidean
  vertex star, whose flat relation uses the straight angle `π` as a real
  angle measure (the `exp` label of the half-turn root of unity, owner ruling
  2026-11-27).  Same namespace; original names kept.
-/
import QOU.MassTheory.ConeAngleIdentity
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

namespace QOU.Archimedean

open Finset

open scoped BigOperators

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
