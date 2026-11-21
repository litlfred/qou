/-
# File 2 — the geodesic faces of H³: vertical planes and hemispheres.

The totally-geodesic surfaces of the upper half-space model `H³` are exactly the
**vertical planes** (perpendicular to `∂H³`) and the **hemispheres centred on
`∂H³`** (Thurston, Ch. 2 §2.3).

**Status update (T2 metric backfill, drained to the corpus faces).**  This
classification is no longer taken wholesale as cited-not-proved.  `HyperbolicMetric`
now DERIVES the hyperbolic distance `dH` (an infimum of path lengths), and
`HyperbolicIsometryReflection` / `HyperbolicIsometryInversion` DERIVE the two
boundary isometries whose fixed sets are these families.
`HyperbolicGeodesic.fixedSet_isTotallyGeodesic` PROVES — sorry-free, conditional on
a single named conjecture — that the *fixed sets* of those isometries are totally
geodesic, and `TotallyGeodesicFaces` then DRAINS this to **the concrete faces
defined below**: `verticalPlane_isTotallyGeodesic` proves `IsTotallyGeodesic` for
`verticalPlane n d` at ANY unit base normal `n` and ANY offset `d` (via a general
Householder vertical-plane reflection, a `dH`-isometry), and
`hemisphere_isTotallyGeodesic` proves it for `hemisphere R` (via the boundary
inversion centred at the origin).  So the vertical-plane / hemisphere
totally-geodesic property now holds for the EXACT faces the ideal tetrahedron
intersects, not merely fixed-set variants.  The residual that genuinely remains
cited/open is now ONLY **geodesic existence + uniqueness in `H³`** (the
`HypMinimizerUnique` conjecture, bean `qou-r111`); the *exhaustiveness* half of the
old citation ("these are the ONLY totally-geodesic surfaces") is not part of any
downstream obligation and is dropped.

This file defines the two families as concrete Euclidean subsets of `ℝ³` together
with their Euclidean unit normals; the geodesic-ness *theorem* for these exact
faces (transported to the `EuclideanSpace ℝ (Fin 3)` carrier by the
coordinate-identity `EuclideanSpace.equiv`) lives in `TotallyGeodesicFaces`.

  -- Ref: [thurston1978] Ch. 2 §2.3 (the upper half-space model), p. 10: "a
  --   hyperbolic two-plane is a Euclidean sphere orthogonal to [the boundary]".
  --   Cf. [ratcliffe] §4.6–4.7.  The vertical-plane / hemisphere totally-geodesic
  --   classification is now PROVED conditional on `HypMinimizerUnique` — for the
  --   concrete `verticalPlane n d` / `hemisphere R` of THIS file in
  --   `QOU.Archimedean.TotallyGeodesicFaces`, via `HyperbolicGeodesic`'s
  --   `fixedSet_isTotallyGeodesic`; only geodesic existence+uniqueness remains open
  --   (Mathlib 4.24.0 still has no hyperbolic Riemannian geometry).

The chimney `chimney (inscribedTriangle 1 t α β γ) 1` of `IdealTetrahedronRegion`
is bounded by three vertical planes (over the three chords) and one hemisphere
(radius 1) — four geodesic faces — with four ideal vertices (the far point `∞`
and the three circle points).  Granting the cited classification, it is a genuine
ideal tetrahedron; File 4 proves its ∞-edge dihedral angles are `(α, β, γ)`.

Archimedean (ℝ): coordinates, squares, `Real.sqrt` — §7c.

  -- Ref: [milnor1982] Appendix (Milnor's normalized position: one face on the
  --   unit hemisphere, opposite vertex at ∞)
  -- Ref: [leitner2026] beans qou-473l (T2 File 2), qou-5gai (H-tier)
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
