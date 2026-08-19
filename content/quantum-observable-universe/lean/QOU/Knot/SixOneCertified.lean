/-
  `6₁`, certified: the generated identities assembled into `SatisfiesEdgeEquations`.

  Bean `qou-glhi`.

  ═══ WHAT THIS DEMONSTRATES ═══

  `QOU/Knot/GeneratedGluing.lean` proves 312 edge identities across 19 manifolds, but as
  **standalone equations**.  `QOU/Knot/GluingBridge.lean` supplies the generic machinery to
  turn them into `SatisfiesEdgeEquations`.  This module runs the whole path end to end on
  one manifold, so the pattern is validated in-repo rather than asserted:

  1. build a `Shape` per tetrahedron from the generated `zⱼ_ne_zero` and
     `one_sub_zⱼ_ne_zero` — those lemmas exist for exactly this purpose;
  2. record the exponent matrix as `GluingData`;
  3. reduce the `∏` form to the generated flattened identity by `Fin.prod_univ_four`
     followed by `linear_combination edge_k ht`;
  4. close with `satisfiesEdgeEquations_of_cleared`.

  Step 3 is the one worth noting: `linear_combination` absorbs the difference in
  association, ordering, and omitted `^0` factors between the two forms, so no
  hand-matching is needed.  **The remaining 18 manifolds are mechanical from here** and
  should be emitted by `scripts/gen-gluing-lean.py` rather than written out.

  ⚠ **A generator improvement this exposes.**  The generated theorems are emitted in
  *flattened* form, and step 3 exists only to bridge that to the `∏` form.  Emitting the
  cleared identity directly as a `Finset` product would make step 3 disappear entirely.
  Worth doing before generating the other 18.

  ═══ SCOPE ═══

  `6₁` is stated for an **arbitrary root** of `x⁴ − 3x³ + 6x² − 5x + 2`, not the geometric
  one — the identities hold at every root, which is what made them provable without
  exhibiting a root in the upper half plane.  Consequently this certifies a
  `ShapedTriangulation` (flat shapes permitted) and says nothing about hyperbolicity; that
  needs `Im z > 0`, which is a separate condition and not established here.

  Nothing here says this is a triangulation *of* `S³ ∖ 6₁`.

  -- Ref: [thurston1978] Ch. 4
  -- Ref: [neumann-zagier1985]
-/
import QOU.Knot.GluingBridge
import QOU.Knot.GeneratedGluing

namespace QOU.Knot.SixOneCertified

open QOU.Knot.FlatTet QOU.MathlibExt QOU.Knot.GeneratedGluing.K61

/-- The four `6₁` shapes as `Shape`s, at an arbitrary root of the minimal polynomial.

`Shape.ne_one` is derived from the generated `one_sub_zⱼ_ne_zero`: `1 - z ≠ 0` and
`z = 1` are contradictory. -/
noncomputable def triangulation {t : ℂ} (ht : minpoly t = 0) : ShapedTriangulation 4 :=
  ⟨![⟨z0 t, z0_ne_zero ht, fun h => one_sub_z0_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z1 t, z1_ne_zero ht, fun h => one_sub_z1_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z2 t, z2_ne_zero ht, fun h => one_sub_z2_ne_zero ht (by rw [h]; ring)⟩,
     ⟨z3 t, z3_ne_zero ht, fun h => one_sub_z3_ne_zero ht (by rw [h]; ring)⟩]⟩

/-- `6₁`'s four edge equations as exponent data, from SnapPy's integer matrix. -/
def gluing : GluingData 4 4 where
  exp := ![![![1,0,1], ![1,2,0], ![0,0,1], ![0,1,1]],
           ![![0,1,1], ![0,0,2], ![0,1,1], ![1,0,0]],
           ![![0,1,0], ![1,0,0], ![1,0,0], ![0,0,1]],
           ![![1,0,0], ![0,0,0], ![1,1,0], ![1,1,0]]]

/-! ### The four cleared identities, at literal edge indices

Proved one per index rather than under `fin_cases`.  `fin_cases` leaves the index as
`⟨0, ⋯⟩`, on which `Matrix.cons_val_zero` and friends do not fire, so the exponent matrix
never reduces and `linear_combination` sees an unreduced goal.  At a literal index the
matrix application reduces and the generated identity closes it. -/

private theorem cleared_0 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 0 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 0 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 0 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 0 i 2)) := by
  simp only [Fin.prod_univ_four, triangulation, gluing, Matrix.cons_val_zero,
    Matrix.cons_val_one, Matrix.head_cons, Matrix.cons_val_two, Matrix.cons_val_three,
    Matrix.tail_cons]
  linear_combination edge_0 ht

private theorem cleared_1 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 1 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 1 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 1 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 1 i 2)) := by
  simp only [Fin.prod_univ_four, triangulation, gluing, Matrix.cons_val_zero,
    Matrix.cons_val_one, Matrix.head_cons, Matrix.cons_val_two, Matrix.cons_val_three,
    Matrix.tail_cons]
  linear_combination edge_1 ht

private theorem cleared_2 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 2 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 2 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 2 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 2 i 2)) := by
  simp only [Fin.prod_univ_four, triangulation, gluing, Matrix.cons_val_zero,
    Matrix.cons_val_one, Matrix.head_cons, Matrix.cons_val_two, Matrix.cons_val_three,
    Matrix.tail_cons]
  linear_combination edge_2 ht

private theorem cleared_3 {t : ℂ} (ht : minpoly t = 0) :
    (∏ i, (((triangulation ht).tet i).z ^ gluing.exp 3 i 0
            * (((triangulation ht).tet i).z - 1) ^ gluing.exp 3 i 2))
      = (∏ i, ((1 - ((triangulation ht).tet i).z) ^ gluing.exp 3 i 1
            * ((triangulation ht).tet i).z ^ gluing.exp 3 i 2)) := by
  simp only [Fin.prod_univ_four, triangulation, gluing, Matrix.cons_val_zero,
    Matrix.cons_val_one, Matrix.head_cons, Matrix.cons_val_two, Matrix.cons_val_three,
    Matrix.tail_cons]
  linear_combination edge_3 ht

/-- **`6₁` satisfies its edge gluing equations**, at every root of the shape field's
minimal polynomial.

The generated identities now *certify a structure* rather than standing alone. -/
theorem satisfiesEdgeEquations {t : ℂ} (ht : minpoly t = 0) :
    (triangulation ht).SatisfiesEdgeEquations gluing := by
  refine satisfiesEdgeEquations_of_cleared _ _ ?_
  intro k
  fin_cases k
  exacts [cleared_0 ht, cleared_1 ht, cleared_2 ht, cleared_3 ht]

end QOU.Knot.SixOneCertified
