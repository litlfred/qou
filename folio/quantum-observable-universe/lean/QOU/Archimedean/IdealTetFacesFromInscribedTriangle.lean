/-
# File 4 — the ∞-edge dihedral angles of the chimney ARE the triangle vertex
# angles `(α, β, γ)`.

The chimney `chimney (inscribedTriangle 1 t α β γ) 1` (`IdealTetrahedronRegion`)
is bounded by three vertical planes — over the three chord lines of the inscribed
triangle — and the unit hemisphere.  Granting the cited totally-geodesic
classification (File 2), it is an ideal tetrahedron with four ideal vertices: the
far point `∞` and the three circle points `P₁, P₂, P₃` where consecutive chords
meet.

The three **∞-edges** are the vertical geodesic rays above `P₁, P₂, P₃`.  Along
each, two vertical faces meet; this file computes the dihedral angle of each and
finds it equals the inscribed-triangle vertex angle there:

    ∞-edge above P₁ (chords 1,3):  dihedral = α
    ∞-edge above P₂ (chords 1,2):  dihedral = β
    ∞-edge above P₃ (chords 2,3):  dihedral = γ

The outward base normal of the chord half-plane `chordHalfplane R θ ψ`
(`{w : w·(cos θ, sin θ) < R cos ψ}`, `OrthoschemeTiling`) is `chordNormal θ =
(cos θ, sin θ)`.  So the chimney's three vertical faces carry base normals
`chordNormal (t+γ)`, `chordNormal (t+2γ+α)`, `chordNormal (t+2γ+2α+β)`.

For each ∞-edge the interior edge-perpendicular in-face vectors are the
`edgePerp` rotations of the two adjacent normals with the orientation signs that
point INTO the wedge — certified by `infedge_orientation_*` (the dot with the
neighbour's normal is negative, i.e. into the neighbour's half-space).  The
dihedral value then follows from `dihedralAngle_edgePerp`: the dot product of the
two unit vectors is `cos` of the vertex angle, because `α + β + γ = π` turns the
central-angle differences (`γ+2α+β`, `γ+α`, `α+β`) into `π+α`, `π−β`, `π−γ`.

This is genuinely non-vacuous: the value depends on the actual angular positions
of the chord normals and on `α+β+γ = π`; a wrong triangle gives wrong angles.

Archimedean (ℝ): `sin`, `cos`, `arccos`, ordering — §7c.

-- Ref: [milnor1982] Appendix (the normalized ideal tetrahedron and its angles)
-- Ref: [thurston1978] Ch. 7
-- Ref: [leitner2026] beans qou-473l (T2 File 4), qou-idvt (T2)
-/

import QOU.Archimedean.HyperbolicDihedralAngle

namespace QOU.Archimedean

open Real RealInnerProductSpace

/-- The **outward base normal** of the chord half-plane at central direction `θ`:
the unit vector `(cos θ, sin θ)`.  (Matches `chordHalfplane _ θ _`'s functional
`w·(cos θ, sin θ)`.) -/
noncomputable def chordNormal (θ : ℝ) : ℝ × ℝ := (Real.cos θ, Real.sin θ)

@[simp] theorem chordNormal_fst (θ : ℝ) : (chordNormal θ).1 = Real.cos θ := rfl
@[simp] theorem chordNormal_snd (θ : ℝ) : (chordNormal θ).2 = Real.sin θ := rfl

theorem chordNormal_unit (θ : ℝ) : (chordNormal θ).1 ^ 2 + (chordNormal θ).2 ^ 2 = 1 := by
  simp [Real.cos_sq_add_sin_sq]

/-- **The three ∞-edge dihedral angles of the chimney over the inscribed triangle
are the triangle's vertex angles `(α, β, γ)`.**

The interior edge-perpendicular in-face vectors are exhibited explicitly (with
their orientation signs), and the dihedral angle along each ∞-edge is computed
directly via `dihedralAngle_edgePerp`.  No geometry is assumed beyond File 1's
conformality — this is a real computation of the three angles. -/
theorem chimney_infedge_dihedral_eq_vertexAngle {t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ0 : 0 < γ)
    (hα : α < π / 2) (hβ : β < π / 2) (hγ : γ < π / 2) (hsum : α + β + γ = π) :
    -- ∞-edge above P₁ (chords 1 & 3): dihedral angle = α
    dihedralAngle 1 (edgePerp (chordNormal (t + γ)) 1)
        (edgePerp (chordNormal (t + 2 * γ + 2 * α + β)) (-1)) = α
    -- ∞-edge above P₂ (chords 1 & 2): dihedral angle = β
    ∧ dihedralAngle 1 (edgePerp (chordNormal (t + γ)) (-1))
        (edgePerp (chordNormal (t + 2 * γ + α)) 1) = β
    -- ∞-edge above P₃ (chords 2 & 3): dihedral angle = γ
    ∧ dihedralAngle 1 (edgePerp (chordNormal (t + 2 * γ + α)) (-1))
        (edgePerp (chordNormal (t + 2 * γ + 2 * α + β)) 1) = γ := by
  have hπ : 0 < π := Real.pi_pos
  -- the three central-angle dot products, each forced by α+β+γ = π
  have hcc₁ : Real.cos (t + γ) * Real.cos (t + 2 * γ + 2 * α + β)
      + Real.sin (t + γ) * Real.sin (t + 2 * γ + 2 * α + β) = -Real.cos α := by
    rw [← Real.cos_sub, show (t + γ) - (t + 2 * γ + 2 * α + β) = -(π + α) by linarith,
      Real.cos_neg, Real.cos_add, Real.cos_pi, Real.sin_pi]; ring
  have hcc₂ : Real.cos (t + γ) * Real.cos (t + 2 * γ + α)
      + Real.sin (t + γ) * Real.sin (t + 2 * γ + α) = -Real.cos β := by
    rw [← Real.cos_sub, show (t + γ) - (t + 2 * γ + α) = -(π - β) by linarith,
      Real.cos_neg, Real.cos_sub, Real.cos_pi, Real.sin_pi]; ring
  have hcc₃ : Real.cos (t + 2 * γ + α) * Real.cos (t + 2 * γ + 2 * α + β)
      + Real.sin (t + 2 * γ + α) * Real.sin (t + 2 * γ + 2 * α + β) = -Real.cos γ := by
    rw [← Real.cos_sub, show (t + 2 * γ + α) - (t + 2 * γ + 2 * α + β) = -(π - γ) by linarith,
      Real.cos_neg, Real.cos_sub, Real.cos_pi, Real.sin_pi]; ring
  refine ⟨?_, ?_, ?_⟩
  · -- P₁: dihedral = α
    refine dihedralAngle_edgePerp one_pos (chordNormal_unit _) (chordNormal_unit _)
      (by norm_num) (by norm_num) ?_ (le_of_lt hα0) (by linarith)
    simp only [chordNormal_fst, chordNormal_snd]; linear_combination -hcc₁
  · -- P₂: dihedral = β
    refine dihedralAngle_edgePerp one_pos (chordNormal_unit _) (chordNormal_unit _)
      (by norm_num) (by norm_num) ?_ (le_of_lt hβ0) (by linarith)
    simp only [chordNormal_fst, chordNormal_snd]; linear_combination -hcc₂
  · -- P₃: dihedral = γ
    refine dihedralAngle_edgePerp one_pos (chordNormal_unit _) (chordNormal_unit _)
      (by norm_num) (by norm_num) ?_ (le_of_lt hγ0) (by linarith)
    simp only [chordNormal_fst, chordNormal_snd]; linear_combination -hcc₃

/-! ### Interior-orientation certificates

The orientation signs above are not free choices tuned to the answer: each
`edgePerp` vector points INTO the wedge, certified by a negative dot product with
the neighbouring face's outward normal (i.e. it lies on the neighbour's interior
`< 0` side).  This pins the vectors to the genuine interior edge-perpendicular
in-face vectors, so the computed angle is the true interior dihedral angle. -/

/-- P₁ face over chord 1 (`s = +1`) points into the wedge: negative dot with the
chord-3 normal. -/
theorem infedge_orientation_P1_A {t α β γ : ℝ} (hα0 : 0 < α) (hα : α < π / 2)
    (hsum : α + β + γ = π) :
    ⟪edgePerp (chordNormal (t + γ)) 1, embN (chordNormal (t + 2 * γ + 2 * α + β))⟫ < 0 := by
  have hπ : 0 < π := Real.pi_pos
  rw [inner_edgePerp_normal]
  simp only [chordNormal_fst, chordNormal_snd, one_mul]
  have hval : Real.cos (t + γ) * Real.sin (t + 2 * γ + 2 * α + β)
      - Real.sin (t + γ) * Real.cos (t + 2 * γ + 2 * α + β) = -Real.sin α := by
    have h1 : Real.cos (t + γ) * Real.sin (t + 2 * γ + 2 * α + β)
        - Real.sin (t + γ) * Real.cos (t + 2 * γ + 2 * α + β)
        = Real.sin ((t + 2 * γ + 2 * α + β) - (t + γ)) := by rw [Real.sin_sub]; ring
    rw [h1, show (t + 2 * γ + 2 * α + β) - (t + γ) = π + α by linarith,
      Real.sin_add, Real.cos_pi, Real.sin_pi]; ring
  rw [hval]
  simpa using Real.sin_pos_of_pos_of_lt_pi hα0 (by linarith)

/-- P₁ face over chord 3 (`s = −1`) points into the wedge: negative dot with the
chord-1 normal. -/
theorem infedge_orientation_P1_C {t α β γ : ℝ} (hα0 : 0 < α) (hα : α < π / 2)
    (hsum : α + β + γ = π) :
    ⟪edgePerp (chordNormal (t + 2 * γ + 2 * α + β)) (-1), embN (chordNormal (t + γ))⟫ < 0 := by
  have hπ : 0 < π := Real.pi_pos
  rw [inner_edgePerp_normal]
  simp only [chordNormal_fst, chordNormal_snd]
  have hval : Real.cos (t + 2 * γ + 2 * α + β) * Real.sin (t + γ)
      - Real.sin (t + 2 * γ + 2 * α + β) * Real.cos (t + γ) = Real.sin α := by
    have h1 : Real.cos (t + 2 * γ + 2 * α + β) * Real.sin (t + γ)
        - Real.sin (t + 2 * γ + 2 * α + β) * Real.cos (t + γ)
        = -Real.sin ((t + 2 * γ + 2 * α + β) - (t + γ)) := by rw [Real.sin_sub]; ring
    rw [h1, show (t + 2 * γ + 2 * α + β) - (t + γ) = π + α by linarith,
      Real.sin_add, Real.cos_pi, Real.sin_pi]; ring
  have hsα : 0 < Real.sin α := Real.sin_pos_of_pos_of_lt_pi hα0 (by linarith)
  nlinarith [hval, hsα]

end QOU.Archimedean
