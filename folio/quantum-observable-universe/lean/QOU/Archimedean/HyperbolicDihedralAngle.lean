/-
# File 3 — the hyperbolic dihedral angle along a vertical edge.

The dihedral angle of a wedge along a common edge is the hyperbolic angle
between two tangent vectors, one in each face, each perpendicular to the edge and
pointing into its face (into the wedge).  By File 1 (conformality) this equals
the Euclidean angle between those tangent vectors, at any height.

This file handles the case both of whose faces are **vertical planes** — the
∞-edges of the ideal tetrahedron, where the common edge is a vertical geodesic
ray to `∞`.  There the edge is vertical, so the edge-perpendicular in-face
tangent vectors are **horizontal**: for a vertical plane with base normal `n`, the
in-face horizontal direction is the 90°-rotation `(−n.2, n.1)` of `n` (times an
orientation sign `s = ±1` chosen to point into the wedge).

`dihedralAngle z e₁ e₂` is literally the hyperbolic angle `hypAngle z e₁ e₂`
between the two edge-perpendicular in-face tangent vectors — the DEFINITION of a
dihedral angle.  Its geometric content is entirely in *which* vectors `e₁, e₂`
are the correct edge-perpendicular in-face vectors of a given pair of faces; that
is certified by `norm_edgePerp` (unit), `inner_edgePerp_self_normal`
(perpendicular to its own face's normal ⇒ lies IN the face), and — where a
concrete wedge is analysed (File 4) — `inner_edgePerp_normal` (the interior
orientation).

The workhorse `dihedralAngle_edgePerp` reads the dihedral value off the dot
product of the two (unit) edge-perpendicular vectors: if it is `cos θ` with
`θ ∈ [0, π]`, the dihedral angle is `θ`.  File 4 supplies the dot product for the
three ∞-edges of the chimney and gets `(α, β, γ)`.

Archimedean (ℝ): `arccos`, `cos`, ordering — §7c.

-- Ref: [thurston1978] Ch. 7 (dihedral angles of ideal polyhedra; the conformal
--   model measures them as Euclidean angles between face tangents)
-- Ref: [milnor1982] Appendix
-- Ref: [leitner2026] beans qou-473l (T2 File 3), qou-idvt (T2)
-/

import QOU.Archimedean.GeodesicFaceH3

namespace QOU.Archimedean

open RealInnerProductSpace

/-! ### 2D inner-product helpers -/

/-- An explicit horizontal Euclidean 2-vector. -/
noncomputable def v2 (a b : ℝ) : EuclideanSpace ℝ (Fin 2) := ![a, b]

/-- Embed a base direction `n : ℝ²` as a horizontal Euclidean 2-vector. -/
noncomputable def embN (n : ℝ × ℝ) : EuclideanSpace ℝ (Fin 2) := v2 n.1 n.2

/-- The inner product of two explicit horizontal 2-vectors is the dot product. -/
theorem inner2 (a b c d : ℝ) : ⟪v2 a b, v2 c d⟫ = a * c + b * d := by
  simp [v2, EuclideanSpace.inner_eq_star_dotProduct, dotProduct, Fin.sum_univ_two]; ring

/-- The norm of an explicit horizontal 2-vector. -/
theorem norm2_one (a b : ℝ) (h : a ^ 2 + b ^ 2 = 1) : ‖v2 a b‖ = 1 := by
  rw [EuclideanSpace.norm_eq]
  have : ∑ i, ‖v2 a b i‖ ^ 2 = 1 := by
    simp [v2, Fin.sum_univ_two, Real.norm_eq_abs, sq_abs]; linarith
  rw [this, Real.sqrt_one]

/-! ### The edge-perpendicular in-face tangent vector -/

/-- **The interior edge-perpendicular in-face tangent vector** of a vertical face
with base normal `n`, oriented by `s = ±1`.  It is the 90°-rotation
`s·(−n.2, n.1)` of the normal: horizontal (so ⊥ the vertical edge), in the face
plane (⊥ `n`, see `inner_edgePerp_self_normal`), and unit when `n` is unit and
`s = ±1`.  The sign `s` is chosen (per wedge) so the vector points into the
wedge, certified for a concrete wedge by `inner_edgePerp_normal`. -/
noncomputable def edgePerp (n : ℝ × ℝ) (s : ℝ) : EuclideanSpace ℝ (Fin 2) :=
  v2 (s * (-n.2)) (s * n.1)

/-- **`edgePerp` is a unit vector** when the base normal is unit and `s = ±1`. -/
theorem norm_edgePerp {n : ℝ × ℝ} {s : ℝ} (hn : n.1 ^ 2 + n.2 ^ 2 = 1)
    (hs : s ^ 2 = 1) : ‖edgePerp n s‖ = 1 := by
  rw [edgePerp]
  apply norm2_one
  nlinarith [hn, hs]

/-- **`edgePerp n s` lies in its own face**: it is perpendicular to the face's
base normal `n` (dot product zero) — the "in-face" certificate. -/
theorem inner_edgePerp_self_normal (n : ℝ × ℝ) (s : ℝ) :
    ⟪edgePerp n s, embN n⟫ = 0 := by
  rw [edgePerp, embN, inner2]; ring

/-- **The dot product of two `edgePerp` vectors.** -/
theorem inner_edgePerp (n₁ n₂ : ℝ × ℝ) (s₁ s₂ : ℝ) :
    ⟪edgePerp n₁ s₁, edgePerp n₂ s₂⟫
      = s₁ * s₂ * (n₁.1 * n₂.1 + n₁.2 * n₂.2) := by
  rw [edgePerp, edgePerp, inner2]; ring

/-- **The dot product of an `edgePerp` vector with a neighbour's base normal** —
the quantity whose SIGN certifies the interior orientation (negative = points
into the neighbour's half-space, i.e. into the wedge). -/
theorem inner_edgePerp_normal (n₁ n₂ : ℝ × ℝ) (s₁ : ℝ) :
    ⟪edgePerp n₁ s₁, embN n₂⟫ = s₁ * (n₁.1 * n₂.2 - n₁.2 * n₂.1) := by
  rw [edgePerp, embN, inner2]; ring

/-! ### The dihedral angle -/

/-- **The hyperbolic dihedral angle** along a common edge, between two
edge-perpendicular in-face tangent vectors `e₁, e₂` at height `z`: the hyperbolic
angle between them.  (For a vertical edge these are horizontal vectors; File 1
makes the value height-independent and equal to the Euclidean angle.) -/
noncomputable def dihedralAngle (z : ℝ) (e₁ e₂ : EuclideanSpace ℝ (Fin 2)) : ℝ :=
  hypAngle z e₁ e₂

/-- The hyperbolic dihedral angle equals the Euclidean angle between the two
edge-perpendicular in-face tangent vectors (File 1, `z > 0`) — hence is
height-independent. -/
theorem dihedralAngle_eq_euclidean {z : ℝ} (hz : 0 < z)
    (e₁ e₂ : EuclideanSpace ℝ (Fin 2)) :
    dihedralAngle z e₁ e₂ = InnerProductGeometry.angle e₁ e₂ :=
  hypAngle_eq_angle hz e₁ e₂

/-- **The workhorse.**  If the two interior edge-perpendicular in-face vectors are
unit (base normals unit, signs `±1`) and their dot product is `cos θ` for some
`θ ∈ [0, π]`, then the dihedral angle along that edge is `θ`.

This is genuinely non-vacuous: the dot product is the actual Euclidean dot of the
two rotated normals, and `θ` is recovered as `arccos` of it — the standard
measurement of a dihedral angle in the conformal model. -/
theorem dihedralAngle_edgePerp {z : ℝ} (hz : 0 < z) {n₁ n₂ : ℝ × ℝ} {s₁ s₂ θ : ℝ}
    (hn1 : n₁.1 ^ 2 + n₁.2 ^ 2 = 1) (hn2 : n₂.1 ^ 2 + n₂.2 ^ 2 = 1)
    (hs1 : s₁ ^ 2 = 1) (hs2 : s₂ ^ 2 = 1)
    (hdot : s₁ * s₂ * (n₁.1 * n₂.1 + n₁.2 * n₂.2) = Real.cos θ)
    (hθ0 : 0 ≤ θ) (hθπ : θ ≤ Real.pi) :
    dihedralAngle z (edgePerp n₁ s₁) (edgePerp n₂ s₂) = θ := by
  rw [dihedralAngle, hypAngle_eq_angle hz, InnerProductGeometry.angle,
    inner_edgePerp, norm_edgePerp hn1 hs1, norm_edgePerp hn2 hs2, hdot, mul_one,
    div_one]
  exact Real.arccos_cos hθ0 hθπ

end QOU.Archimedean
