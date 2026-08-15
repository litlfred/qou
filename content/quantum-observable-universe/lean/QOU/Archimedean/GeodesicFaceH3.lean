/-
# File 2 — the geodesic faces of H³: vertical planes and hemispheres.

The totally-geodesic surfaces of the upper half-space model `H³` are exactly the
**vertical planes** (perpendicular to `∂H³`) and the **hemispheres centred on
`∂H³`** (Thurston, Ch. 7).  This is the ONE fact this whole T2 development takes
as cited-not-proved: Mathlib has no hyperbolic Riemannian geometry, so
"totally geodesic" cannot be stated, let alone proved.  Everything ELSE — the
angles, and the volume identity — is proved in Lean.

This file therefore defines the two families as concrete Euclidean subsets of
`ℝ³` together with their Euclidean unit normals, and records the geodesic
classification in a doc comment.  It makes no geodesic-ness *claim* as a theorem.

  -- Ref: [thurston1978] Ch. 7
  --   The complete totally-geodesic surfaces of H³ (upper half-space model) are
  --   the Euclidean vertical planes and the Euclidean hemispheres centred on the
  --   bounding plane z = 0.  This classification is the cited geometric input; it
  --   is NOT proved here (Mathlib has no hyperbolic metric).

The chimney `chimney (inscribedTriangle 1 t α β γ) 1` of `IdealTetrahedronRegion`
is bounded by three vertical planes (over the three chords) and one hemisphere
(radius 1) — four geodesic faces — with four ideal vertices (the far point `∞`
and the three circle points).  Granting the cited classification, it is a genuine
ideal tetrahedron; File 4 proves its ∞-edge dihedral angles are `(α, β, γ)`.

Archimedean (ℝ): coordinates, squares, `Real.sqrt` — §7c.

  -- Ref: [milnor1982] Appendix (Milnor's normalized position: one face on the
  --   unit hemisphere, opposite vertex at ∞)
  -- Ref: [manuscript] beans qou-473l (T2 File 2), qou-5gai (H-tier)
-/

import QOU.Archimedean.HyperbolicConformalAngle
import Mathlib.Analysis.InnerProductSpace.PiL2

namespace QOU.Archimedean

/-! ### Vertical planes

A vertical plane sits over a line `w·n = d` in the base `ℝ²`.  Its (upward-open)
extrusion is the geodesic face; its Euclidean normal is the horizontal vector
`(n.1, n.2, 0)`. -/

/-- The **vertical plane** over the base line `{w : w·n = d}` — the set of points
of `ℝ³` whose horizontal projection lies on that line, at any height. -/
def verticalPlane (n : ℝ × ℝ) (d : ℝ) : Set (Fin 3 → ℝ) :=
  {p | p 0 * n.1 + p 1 * n.2 = d}

/-- The Euclidean unit normal of the vertical plane with base normal `n` — the
horizontal vector `(n.1, n.2, 0)`, as an element of `EuclideanSpace ℝ (Fin 3)`. -/
noncomputable def verticalPlaneNormal (n : ℝ × ℝ) : EuclideanSpace ℝ (Fin 3) :=
  ![n.1, n.2, 0]

/-- A point is on the vertical plane iff its horizontal projection is on the base
line — the defining membership, restated for downstream `rw`. -/
theorem mem_verticalPlane {n : ℝ × ℝ} {d : ℝ} {p : Fin 3 → ℝ} :
    p ∈ verticalPlane n d ↔ p 0 * n.1 + p 1 * n.2 = d := Iff.rfl

/-- **The vertical-plane normal is a Euclidean unit vector** when the base normal
`n` is a unit vector.  The `z`-component `0` contributes nothing, so the norm is
`√(n.1² + n.2²) = 1`. -/
theorem norm_verticalPlaneNormal {n : ℝ × ℝ} (hn : n.1 ^ 2 + n.2 ^ 2 = 1) :
    ‖verticalPlaneNormal n‖ = 1 := by
  rw [EuclideanSpace.norm_eq]
  have : ∑ i, ‖verticalPlaneNormal n i‖ ^ 2 = 1 := by
    simp [verticalPlaneNormal, Fin.sum_univ_three, Real.norm_eq_abs, sq_abs]; linarith
  rw [this, Real.sqrt_one]

/-! ### Hemispheres

The hemisphere of radius `R` centred at the origin of `∂H³`: the part of the
sphere `x² + y² + z² = R²` with `z > 0`.  Its Euclidean normal at a point `p` on
the sphere is the radial direction `p / R`. -/

/-- The **hemisphere** of radius `R`: points of `ℝ³` on the sphere of radius `R`
about the origin, at positive height.  (Milnor's normalized position uses
`R = 1`.) -/
def hemisphere (R : ℝ) : Set (Fin 3 → ℝ) :=
  {p | (p 0) ^ 2 + (p 1) ^ 2 + (p 2) ^ 2 = R ^ 2 ∧ 0 < p 2}

/-- The Euclidean normal of the hemisphere of radius `R` at a point `p`: the
radial vector `p / R`. -/
noncomputable def hemisphereNormal (R : ℝ) (p : Fin 3 → ℝ) : EuclideanSpace ℝ (Fin 3) :=
  ![p 0 / R, p 1 / R, p 2 / R]

/-- **The hemisphere normal is a Euclidean unit vector** at a point on the
hemisphere (radius `R > 0`): `‖p / R‖ = ‖p‖ / R = R / R = 1`. -/
theorem norm_hemisphereNormal {R : ℝ} (hR : 0 < R) {p : Fin 3 → ℝ}
    (hp : (p 0) ^ 2 + (p 1) ^ 2 + (p 2) ^ 2 = R ^ 2) :
    ‖hemisphereNormal R p‖ = 1 := by
  rw [EuclideanSpace.norm_eq]
  have hsum : ∑ i, ‖hemisphereNormal R p i‖ ^ 2 = 1 := by
    have hR2 : R ^ 2 ≠ 0 := pow_ne_zero 2 (ne_of_gt hR)
    simp only [hemisphereNormal, Fin.sum_univ_three, Real.norm_eq_abs, sq_abs,
      Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons, Matrix.cons_val_two,
      Matrix.tail_cons, div_pow]
    field_simp
    linarith [hp]
  rw [hsum, Real.sqrt_one]

end QOU.Archimedean
