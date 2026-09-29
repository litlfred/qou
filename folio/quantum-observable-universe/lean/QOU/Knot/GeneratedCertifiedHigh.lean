/-
  `SatisfiesEdgeEquations` certifications for the high-degree manifolds.
  Beans `qou-glhi`, `qou-fr7j`.

  Companion to `QOU/Knot/GeneratedCertified.lean` (shape-field degrees 2–6), covering the
  eight manifolds of `QOU/Knot/GeneratedGluingHigh.lean` at degrees 7–14.  Same generator,
  same validated template; read `GeneratedCertified`'s header for both.

  ═══ n = 14, which the old template refused twice over ═══

  `10_100` has **14 tetrahedra** — nearly double the `Fin.prod_univ_eight` ceiling the
  generator used to stop at — and a degree-14 shape field.  It certifies by the same one
  line as every other manifold:

      simp [Fin.prod_univ_succ, triangulation, gluing]

  So neither the tetrahedron count nor the field degree is a barrier to certification.
  The only thing that ever grew was compile time, and that grew mildly (see
  `GeneratedGluingHigh`'s header for the measurements).

  ═══ SCOPE ═══

  Stated for an ARBITRARY root of each shape field's minimal polynomial.  Certifies a
  `ShapedTriangulation` (flat shapes permitted) and says nothing about hyperbolicity,
  which needs `Im z > 0` separately.  Nothing here says any of these is a triangulation
  *of* a knot complement.
-/
import QOU.Knot.GluingBridge
import QOU.Knot.GeneratedGluingHigh

namespace QOU.Knot.GeneratedCertifiedHigh

open QOU.Knot.FlatTet QOU.MathlibExt

/-! ### `9_2` certified -/

namespace Cert92
open QOU.Knot.GeneratedGluingHigh.K92

/-- The 5 `9_2` shapes, at an arbitrary root of the minimal polynomial. -/
noncomputable def triangulation {t : ℂ} (ht : minpoly t = 0) :
    ShapedTriangulation 5 :=
  ⟨![⟨z0 t, z0_ne_zero ht, fun h => one_sub_z0_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z1 t, z1_ne_zero ht, fun h => one_sub_z1_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z2 t, z2_ne_zero ht, fun h => one_sub_z2_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z3 t, z3_ne_zero ht, fun h => one_sub_z3_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z4 t, z4_ne_zero ht, fun h => one_sub_z4_ne_zero ht (by rw [h]; ring)⟩]⟩

/-- `9_2`'s edge exponents, from SnapPy's integer matrix. -/
def gluing : GluingData 5 5 where
  exp := ![![![2,0,0], ![1,1,0], ![1,0,1], ![0,0,0], ![0,0,0]],
           ![![0,2,1], ![1,0,1], ![0,1,1], ![1,0,0], ![0,0,0]],
           ![![0,0,1], ![0,1,0], ![1,0,0], ![0,0,2], ![0,1,0]],
           ![![0,0,0], ![0,0,1], ![0,1,0], ![0,2,0], ![0,1,2]],
           ![![0,0,0], ![0,0,0], ![0,0,0], ![1,0,0], ![2,0,0]]]

private theorem cleared_0 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 0 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 0 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 0 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 0 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_0 ht

private theorem cleared_1 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 1 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 1 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 1 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 1 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_1 ht

private theorem cleared_2 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 2 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 2 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 2 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 2 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_2 ht

private theorem cleared_3 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 3 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 3 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 3 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 3 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_3 ht

private theorem cleared_4 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 4 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 4 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 4 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 4 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_4 ht

/-- **`9_2` satisfies its edge gluing equations**, at every root of the shape
field's minimal polynomial. -/
theorem satisfiesEdgeEquations {t : ℂ} (ht : minpoly t = 0) :
    (triangulation ht).SatisfiesEdgeEquations gluing := by
  refine satisfiesEdgeEquations_of_cleared _ _ ?_
  intro k
  fin_cases k
  exacts [cleared_0 ht, cleared_1 ht, cleared_2 ht, cleared_3 ht, cleared_4 ht]

end Cert92

/-! ### `10_1` certified -/

namespace Cert101
open QOU.Knot.GeneratedGluingHigh.K101

/-- The 6 `10_1` shapes, at an arbitrary root of the minimal polynomial. -/
noncomputable def triangulation {t : ℂ} (ht : minpoly t = 0) :
    ShapedTriangulation 6 :=
  ⟨![⟨z0 t, z0_ne_zero ht, fun h => one_sub_z0_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z1 t, z1_ne_zero ht, fun h => one_sub_z1_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z2 t, z2_ne_zero ht, fun h => one_sub_z2_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z3 t, z3_ne_zero ht, fun h => one_sub_z3_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z4 t, z4_ne_zero ht, fun h => one_sub_z4_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z5 t, z5_ne_zero ht, fun h => one_sub_z5_ne_zero ht (by rw [h]; ring)⟩]⟩

/-- `10_1`'s edge exponents, from SnapPy's integer matrix. -/
def gluing : GluingData 6 6 where
  exp := ![![![2,0,0], ![1,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0]],
           ![![0,1,0], ![0,0,2], ![0,1,0], ![0,0,0], ![0,0,0], ![0,0,0]],
           ![![0,1,2], ![0,2,0], ![0,0,2], ![0,1,0], ![0,1,0], ![0,0,0]],
           ![![0,0,0], ![1,0,0], ![2,0,0], ![1,1,0], ![1,1,0], ![2,0,1]],
           ![![0,0,0], ![0,0,0], ![0,1,0], ![0,0,1], ![0,0,1], ![0,0,1]],
           ![![0,0,0], ![0,0,0], ![0,0,0], ![1,0,1], ![1,0,1], ![0,2,0]]]

private theorem cleared_0 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 0 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 0 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 0 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 0 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_0 ht

private theorem cleared_1 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 1 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 1 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 1 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 1 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_1 ht

private theorem cleared_2 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 2 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 2 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 2 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 2 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_2 ht

private theorem cleared_3 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 3 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 3 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 3 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 3 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_3 ht

private theorem cleared_4 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 4 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 4 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 4 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 4 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_4 ht

private theorem cleared_5 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 5 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 5 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 5 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 5 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_5 ht

/-- **`10_1` satisfies its edge gluing equations**, at every root of the shape
field's minimal polynomial. -/
theorem satisfiesEdgeEquations {t : ℂ} (ht : minpoly t = 0) :
    (triangulation ht).SatisfiesEdgeEquations gluing := by
  refine satisfiesEdgeEquations_of_cleared _ _ ?_
  intro k
  fin_cases k
  exacts [cleared_0 ht, cleared_1 ht, cleared_2 ht, cleared_3 ht, cleared_4 ht, cleared_5 ht]

end Cert101

/-! ### `7_5` certified -/

namespace Cert75
open QOU.Knot.GeneratedGluingHigh.K75

/-- The 7 `7_5` shapes, at an arbitrary root of the minimal polynomial. -/
noncomputable def triangulation {t : ℂ} (ht : minpoly t = 0) :
    ShapedTriangulation 7 :=
  ⟨![⟨z0 t, z0_ne_zero ht, fun h => one_sub_z0_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z1 t, z1_ne_zero ht, fun h => one_sub_z1_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z2 t, z2_ne_zero ht, fun h => one_sub_z2_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z3 t, z3_ne_zero ht, fun h => one_sub_z3_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z4 t, z4_ne_zero ht, fun h => one_sub_z4_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z5 t, z5_ne_zero ht, fun h => one_sub_z5_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z6 t, z6_ne_zero ht, fun h => one_sub_z6_ne_zero ht (by rw [h]; ring)⟩]⟩

/-- `7_5`'s edge exponents, from SnapPy's integer matrix. -/
def gluing : GluingData 7 7 where
  exp := ![![![1,0,1], ![1,0,0], ![1,1,0], ![0,0,0], ![0,0,0], ![0,0,0], ![1,0,0]],
           ![![0,1,0], ![0,1,1], ![0,0,0], ![0,0,0], ![0,1,1], ![0,1,0], ![0,0,0]],
           ![![0,0,1], ![0,1,0], ![0,0,0], ![0,1,0], ![0,1,0], ![0,0,1], ![1,0,0]],
           ![![0,1,0], ![0,0,0], ![1,0,1], ![1,0,1], ![0,0,0], ![0,0,0], ![0,1,0]],
           ![![1,0,0], ![0,0,1], ![0,0,0], ![1,0,0], ![0,0,0], ![0,1,0], ![0,0,0]],
           ![![0,0,0], ![1,0,0], ![0,0,1], ![0,0,0], ![1,0,1], ![1,0,0], ![0,1,1]],
           ![![0,0,0], ![0,0,0], ![0,1,0], ![0,1,1], ![1,0,0], ![1,0,1], ![0,0,1]]]

private theorem cleared_0 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 0 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 0 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 0 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 0 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_0 ht

private theorem cleared_1 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 1 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 1 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 1 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 1 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_1 ht

private theorem cleared_2 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 2 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 2 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 2 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 2 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_2 ht

private theorem cleared_3 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 3 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 3 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 3 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 3 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_3 ht

private theorem cleared_4 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 4 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 4 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 4 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 4 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_4 ht

private theorem cleared_5 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 5 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 5 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 5 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 5 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_5 ht

private theorem cleared_6 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 6 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 6 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 6 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 6 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_6 ht

/-- **`7_5` satisfies its edge gluing equations**, at every root of the shape
field's minimal polynomial. -/
theorem satisfiesEdgeEquations {t : ℂ} (ht : minpoly t = 0) :
    (triangulation ht).SatisfiesEdgeEquations gluing := by
  refine satisfiesEdgeEquations_of_cleared _ _ ?_
  intro k
  fin_cases k
  exacts [cleared_0 ht, cleared_1 ht, cleared_2 ht, cleared_3 ht, cleared_4 ht, cleared_5 ht, cleared_6 ht]

end Cert75

/-! ### `8_2` certified -/

namespace Cert82
open QOU.Knot.GeneratedGluingHigh.K82

/-- The 6 `8_2` shapes, at an arbitrary root of the minimal polynomial. -/
noncomputable def triangulation {t : ℂ} (ht : minpoly t = 0) :
    ShapedTriangulation 6 :=
  ⟨![⟨z0 t, z0_ne_zero ht, fun h => one_sub_z0_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z1 t, z1_ne_zero ht, fun h => one_sub_z1_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z2 t, z2_ne_zero ht, fun h => one_sub_z2_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z3 t, z3_ne_zero ht, fun h => one_sub_z3_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z4 t, z4_ne_zero ht, fun h => one_sub_z4_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z5 t, z5_ne_zero ht, fun h => one_sub_z5_ne_zero ht (by rw [h]; ring)⟩]⟩

/-- `8_2`'s edge exponents, from SnapPy's integer matrix. -/
def gluing : GluingData 6 6 where
  exp := ![![![1,0,2], ![0,1,0], ![0,1,0], ![0,0,1], ![0,0,0], ![0,0,0]],
           ![![0,2,0], ![0,0,1], ![0,0,1], ![0,0,0], ![0,0,0], ![0,0,0]],
           ![![1,0,0], ![1,0,0], ![1,0,0], ![0,0,1], ![1,0,1], ![0,1,1]],
           ![![0,0,0], ![1,0,1], ![0,1,0], ![1,1,0], ![0,1,0], ![1,0,0]],
           ![![0,0,0], ![0,1,0], ![1,0,0], ![1,0,0], ![0,1,1], ![1,1,0]],
           ![![0,0,0], ![0,0,0], ![0,0,1], ![0,1,0], ![1,0,0], ![0,0,1]]]

private theorem cleared_0 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 0 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 0 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 0 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 0 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_0 ht

private theorem cleared_1 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 1 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 1 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 1 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 1 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_1 ht

private theorem cleared_2 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 2 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 2 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 2 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 2 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_2 ht

private theorem cleared_3 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 3 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 3 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 3 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 3 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_3 ht

private theorem cleared_4 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 4 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 4 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 4 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 4 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_4 ht

private theorem cleared_5 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 5 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 5 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 5 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 5 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_5 ht

/-- **`8_2` satisfies its edge gluing equations**, at every root of the shape
field's minimal polynomial. -/
theorem satisfiesEdgeEquations {t : ℂ} (ht : minpoly t = 0) :
    (triangulation ht).SatisfiesEdgeEquations gluing := by
  refine satisfiesEdgeEquations_of_cleared _ _ ?_
  intro k
  fin_cases k
  exacts [cleared_0 ht, cleared_1 ht, cleared_2 ht, cleared_3 ht, cleared_4 ht, cleared_5 ht]

end Cert82

/-! ### `8_3` certified -/

namespace Cert83
open QOU.Knot.GeneratedGluingHigh.K83

/-- The 6 `8_3` shapes, at an arbitrary root of the minimal polynomial. -/
noncomputable def triangulation {t : ℂ} (ht : minpoly t = 0) :
    ShapedTriangulation 6 :=
  ⟨![⟨z0 t, z0_ne_zero ht, fun h => one_sub_z0_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z1 t, z1_ne_zero ht, fun h => one_sub_z1_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z2 t, z2_ne_zero ht, fun h => one_sub_z2_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z3 t, z3_ne_zero ht, fun h => one_sub_z3_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z4 t, z4_ne_zero ht, fun h => one_sub_z4_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z5 t, z5_ne_zero ht, fun h => one_sub_z5_ne_zero ht (by rw [h]; ring)⟩]⟩

/-- `8_3`'s edge exponents, from SnapPy's integer matrix. -/
def gluing : GluingData 6 6 where
  exp := ![![![1,0,0], ![1,0,0], ![1,0,0], ![0,0,1], ![1,0,0], ![0,0,0]],
           ![![0,1,0], ![1,0,1], ![1,0,0], ![1,0,0], ![0,0,1], ![1,1,0]],
           ![![0,1,1], ![0,1,0], ![0,0,1], ![0,1,1], ![0,1,0], ![0,1,0]],
           ![![1,0,1], ![0,0,0], ![0,1,1], ![1,0,0], ![0,0,0], ![0,0,0]],
           ![![0,0,0], ![0,0,1], ![0,1,0], ![0,1,0], ![0,1,0], ![0,0,1]],
           ![![0,0,0], ![0,1,0], ![0,0,0], ![0,0,0], ![1,0,1], ![1,0,1]]]

private theorem cleared_0 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 0 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 0 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 0 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 0 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_0 ht

private theorem cleared_1 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 1 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 1 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 1 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 1 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_1 ht

private theorem cleared_2 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 2 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 2 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 2 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 2 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_2 ht

private theorem cleared_3 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 3 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 3 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 3 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 3 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_3 ht

private theorem cleared_4 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 4 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 4 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 4 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 4 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_4 ht

private theorem cleared_5 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 5 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 5 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 5 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 5 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_5 ht

/-- **`8_3` satisfies its edge gluing equations**, at every root of the shape
field's minimal polynomial. -/
theorem satisfiesEdgeEquations {t : ℂ} (ht : minpoly t = 0) :
    (triangulation ht).SatisfiesEdgeEquations gluing := by
  refine satisfiesEdgeEquations_of_cleared _ _ ?_
  intro k
  fin_cases k
  exacts [cleared_0 ht, cleared_1 ht, cleared_2 ht, cleared_3 ht, cleared_4 ht, cleared_5 ht]

end Cert83

/-! ### `7_6` certified -/

namespace Cert76
open QOU.Knot.GeneratedGluingHigh.K76

/-- The 8 `7_6` shapes, at an arbitrary root of the minimal polynomial. -/
noncomputable def triangulation {t : ℂ} (ht : minpoly t = 0) :
    ShapedTriangulation 8 :=
  ⟨![⟨z0 t, z0_ne_zero ht, fun h => one_sub_z0_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z1 t, z1_ne_zero ht, fun h => one_sub_z1_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z2 t, z2_ne_zero ht, fun h => one_sub_z2_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z3 t, z3_ne_zero ht, fun h => one_sub_z3_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z4 t, z4_ne_zero ht, fun h => one_sub_z4_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z5 t, z5_ne_zero ht, fun h => one_sub_z5_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z6 t, z6_ne_zero ht, fun h => one_sub_z6_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z7 t, z7_ne_zero ht, fun h => one_sub_z7_ne_zero ht (by rw [h]; ring)⟩]⟩

/-- `7_6`'s edge exponents, from SnapPy's integer matrix. -/
def gluing : GluingData 8 8 where
  exp := ![![![1,0,1], ![1,1,0], ![1,0,0], ![0,0,0], ![1,0,0], ![0,0,0], ![0,0,0], ![0,0,0]],
           ![![0,1,0], ![0,0,1], ![0,0,0], ![1,0,1], ![0,0,0], ![0,0,0], ![1,0,0], ![1,1,0]],
           ![![0,0,1], ![0,1,0], ![0,1,0], ![0,1,0], ![0,0,1], ![0,0,1], ![0,0,0], ![0,0,0]],
           ![![0,1,0], ![0,0,0], ![0,1,1], ![0,0,0], ![0,0,0], ![0,0,0], ![0,1,1], ![0,0,1]],
           ![![1,0,0], ![0,0,0], ![0,0,1], ![1,0,0], ![0,0,0], ![0,1,0], ![0,0,0], ![0,0,0]],
           ![![0,0,0], ![0,0,1], ![1,0,0], ![0,0,0], ![0,1,1], ![1,0,0], ![1,0,1], ![0,1,0]],
           ![![0,0,0], ![1,0,0], ![0,0,0], ![0,1,1], ![0,1,0], ![1,0,1], ![0,0,0], ![0,0,1]],
           ![![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![1,0,0], ![0,1,0], ![0,1,0], ![1,0,0]]]

private theorem cleared_0 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 0 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 0 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 0 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 0 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_0 ht

private theorem cleared_1 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 1 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 1 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 1 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 1 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_1 ht

private theorem cleared_2 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 2 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 2 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 2 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 2 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_2 ht

private theorem cleared_3 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 3 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 3 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 3 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 3 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_3 ht

private theorem cleared_4 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 4 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 4 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 4 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 4 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_4 ht

private theorem cleared_5 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 5 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 5 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 5 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 5 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_5 ht

private theorem cleared_6 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 6 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 6 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 6 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 6 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_6 ht

private theorem cleared_7 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 7 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 7 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 7 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 7 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_7 ht

/-- **`7_6` satisfies its edge gluing equations**, at every root of the shape
field's minimal polynomial. -/
theorem satisfiesEdgeEquations {t : ℂ} (ht : minpoly t = 0) :
    (triangulation ht).SatisfiesEdgeEquations gluing := by
  refine satisfiesEdgeEquations_of_cleared _ _ ?_
  intro k
  fin_cases k
  exacts [cleared_0 ht, cleared_1 ht, cleared_2 ht, cleared_3 ht, cleared_4 ht, cleared_5 ht, cleared_6 ht, cleared_7 ht]

end Cert76

/-! ### `t12000` certified -/

namespace Certt12000
open QOU.Knot.GeneratedGluingHigh.Kt12000

/-- The 8 `t12000` shapes, at an arbitrary root of the minimal polynomial. -/
noncomputable def triangulation {t : ℂ} (ht : minpoly t = 0) :
    ShapedTriangulation 8 :=
  ⟨![⟨z0 t, z0_ne_zero ht, fun h => one_sub_z0_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z1 t, z1_ne_zero ht, fun h => one_sub_z1_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z2 t, z2_ne_zero ht, fun h => one_sub_z2_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z3 t, z3_ne_zero ht, fun h => one_sub_z3_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z4 t, z4_ne_zero ht, fun h => one_sub_z4_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z5 t, z5_ne_zero ht, fun h => one_sub_z5_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z6 t, z6_ne_zero ht, fun h => one_sub_z6_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z7 t, z7_ne_zero ht, fun h => one_sub_z7_ne_zero ht (by rw [h]; ring)⟩]⟩

/-- `t12000`'s edge exponents, from SnapPy's integer matrix. -/
def gluing : GluingData 8 8 where
  exp := ![![![1,2,0], ![0,0,1], ![0,0,1], ![0,1,0], ![0,0,0], ![0,1,0], ![0,0,0], ![0,0,0]],
           ![![0,0,2], ![0,1,0], ![0,1,0], ![0,0,0], ![0,0,1], ![0,0,0], ![0,0,0], ![0,0,0]],
           ![![1,0,0], ![1,0,0], ![1,0,0], ![0,0,1], ![0,0,1], ![1,0,0], ![1,0,0], ![0,0,0]],
           ![![0,0,0], ![1,0,1], ![0,0,0], ![1,0,0], ![1,1,0], ![0,1,0], ![0,0,1], ![0,1,0]],
           ![![0,0,0], ![0,1,0], ![0,1,0], ![0,0,1], ![0,0,0], ![0,0,1], ![0,0,1], ![0,1,0]],
           ![![0,0,0], ![0,0,0], ![1,0,0], ![0,1,0], ![1,0,0], ![1,0,0], ![0,0,0], ![0,0,1]],
           ![![0,0,0], ![0,0,0], ![0,0,1], ![0,0,0], ![0,1,0], ![0,0,0], ![0,2,0], ![0,0,1]],
           ![![0,0,0], ![0,0,0], ![0,0,0], ![1,0,0], ![0,0,0], ![0,0,1], ![1,0,0], ![2,0,0]]]

private theorem cleared_0 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 0 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 0 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 0 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 0 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_0 ht

private theorem cleared_1 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 1 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 1 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 1 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 1 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_1 ht

private theorem cleared_2 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 2 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 2 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 2 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 2 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_2 ht

private theorem cleared_3 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 3 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 3 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 3 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 3 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_3 ht

private theorem cleared_4 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 4 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 4 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 4 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 4 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_4 ht

private theorem cleared_5 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 5 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 5 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 5 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 5 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_5 ht

private theorem cleared_6 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 6 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 6 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 6 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 6 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_6 ht

private theorem cleared_7 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 7 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 7 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 7 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 7 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_7 ht

/-- **`t12000` satisfies its edge gluing equations**, at every root of the shape
field's minimal polynomial. -/
theorem satisfiesEdgeEquations {t : ℂ} (ht : minpoly t = 0) :
    (triangulation ht).SatisfiesEdgeEquations gluing := by
  refine satisfiesEdgeEquations_of_cleared _ _ ?_
  intro k
  fin_cases k
  exacts [cleared_0 ht, cleared_1 ht, cleared_2 ht, cleared_3 ht, cleared_4 ht, cleared_5 ht, cleared_6 ht, cleared_7 ht]

end Certt12000

/-! ### `10_100` certified -/

namespace Cert10100
open QOU.Knot.GeneratedGluingHigh.K10100

/-- The 14 `10_100` shapes, at an arbitrary root of the minimal polynomial. -/
noncomputable def triangulation {t : ℂ} (ht : minpoly t = 0) :
    ShapedTriangulation 14 :=
  ⟨![⟨z0 t, z0_ne_zero ht, fun h => one_sub_z0_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z1 t, z1_ne_zero ht, fun h => one_sub_z1_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z2 t, z2_ne_zero ht, fun h => one_sub_z2_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z3 t, z3_ne_zero ht, fun h => one_sub_z3_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z4 t, z4_ne_zero ht, fun h => one_sub_z4_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z5 t, z5_ne_zero ht, fun h => one_sub_z5_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z6 t, z6_ne_zero ht, fun h => one_sub_z6_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z7 t, z7_ne_zero ht, fun h => one_sub_z7_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z8 t, z8_ne_zero ht, fun h => one_sub_z8_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z9 t, z9_ne_zero ht, fun h => one_sub_z9_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z10 t, z10_ne_zero ht, fun h => one_sub_z10_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z11 t, z11_ne_zero ht, fun h => one_sub_z11_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z12 t, z12_ne_zero ht, fun h => one_sub_z12_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z13 t, z13_ne_zero ht, fun h => one_sub_z13_ne_zero ht (by rw [h]; ring)⟩]⟩

/-- `10_100`'s edge exponents, from SnapPy's integer matrix. -/
def gluing : GluingData 14 14 where
  exp := ![![![1,0,0], ![1,0,0], ![1,0,0], ![0,0,0], ![1,0,0], ![0,0,0], ![0,0,0], ![1,0,0], ![0,0,0], ![1,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0]],
           ![![0,1,0], ![0,0,1], ![0,0,0], ![0,0,1], ![0,0,0], ![0,1,0], ![0,1,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,1], ![0,0,0], ![0,0,0]],
           ![![0,0,1], ![0,1,0], ![1,0,1], ![0,1,1], ![0,0,0], ![0,0,0], ![0,0,1], ![0,1,0], ![1,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0]],
           ![![1,0,1], ![0,0,0], ![0,1,0], ![1,1,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0]],
           ![![0,1,0], ![0,0,0], ![0,0,1], ![1,0,0], ![0,0,0], ![0,0,0], ![1,0,0], ![0,0,0], ![0,1,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0]],
           ![![0,0,0], ![0,0,1], ![0,0,0], ![0,0,0], ![0,1,0], ![0,0,0], ![0,1,0], ![0,0,0], ![1,0,0], ![0,0,0], ![0,0,1], ![0,0,0], ![0,1,0], ![0,0,0]],
           ![![0,0,0], ![0,1,0], ![0,0,0], ![0,0,0], ![0,0,1], ![0,0,1], ![0,0,0], ![0,1,0], ![0,0,0], ![0,0,1], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0]],
           ![![0,0,0], ![1,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![1,0,0], ![1,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![1,0,0], ![1,0,0], ![1,0,0], ![0,0,0]],
           ![![0,0,0], ![0,0,0], ![0,1,0], ![0,0,0], ![0,0,0], ![0,1,0], ![0,0,0], ![0,0,1], ![0,0,1], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,1], ![0,0,0]],
           ![![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,1,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![1,0,1], ![0,1,0], ![0,0,0], ![0,0,1], ![1,1,0]],
           ![![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![1,0,1], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,1,0], ![1,1,0], ![0,0,1], ![0,0,0], ![0,1,0]],
           ![![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![1,0,0], ![0,0,0], ![1,0,0], ![0,1,0], ![0,0,0], ![0,0,0], ![1,0,0], ![1,0,0], ![1,0,0]],
           ![![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,1], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,1], ![0,1,0], ![0,1,0], ![0,0,1]],
           ![![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,0], ![0,0,1], ![0,0,1], ![0,0,1], ![0,1,0], ![0,0,0], ![0,1,0], ![0,0,0], ![0,0,1]]]

private theorem cleared_0 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 0 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 0 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 0 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 0 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_0 ht

private theorem cleared_1 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 1 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 1 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 1 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 1 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_1 ht

private theorem cleared_2 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 2 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 2 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 2 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 2 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_2 ht

private theorem cleared_3 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 3 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 3 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 3 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 3 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_3 ht

private theorem cleared_4 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 4 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 4 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 4 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 4 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_4 ht

private theorem cleared_5 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 5 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 5 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 5 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 5 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_5 ht

private theorem cleared_6 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 6 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 6 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 6 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 6 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_6 ht

private theorem cleared_7 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 7 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 7 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 7 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 7 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_7 ht

private theorem cleared_8 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 8 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 8 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 8 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 8 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_8 ht

private theorem cleared_9 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 9 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 9 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 9 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 9 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_9 ht

private theorem cleared_10 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 10 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 10 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 10 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 10 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_10 ht

private theorem cleared_11 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 11 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 11 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 11 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 11 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_11 ht

private theorem cleared_12 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 12 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 12 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 12 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 12 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_12 ht

private theorem cleared_13 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 13 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 13 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 13 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 13 i 2)) := by
  simp [Fin.prod_univ_succ, triangulation, gluing]
  linear_combination edge_13 ht

/-- **`10_100` satisfies its edge gluing equations**, at every root of the shape
field's minimal polynomial. -/
theorem satisfiesEdgeEquations {t : ℂ} (ht : minpoly t = 0) :
    (triangulation ht).SatisfiesEdgeEquations gluing := by
  refine satisfiesEdgeEquations_of_cleared _ _ ?_
  intro k
  fin_cases k
  exacts [cleared_0 ht, cleared_1 ht, cleared_2 ht, cleared_3 ht, cleared_4 ht, cleared_5 ht, cleared_6 ht, cleared_7 ht, cleared_8 ht, cleared_9 ht, cleared_10 ht, cleared_11 ht, cleared_12 ht, cleared_13 ht]

end Cert10100
end QOU.Knot.GeneratedCertifiedHigh
