/-
  H4-5c-ii(b): THE TILING — the three wedges ARE the inscribed triangle.

      H4-5b       Vol(chimney (wedge R ψ) R)      =  Λ(ψ)
      H4-5c-i     Vol(chimney (wedgeAt R θ ψ) R)  =  Λ(ψ)          any axis
      H4-5c-ii(a) Vol(chimney (milnorWedges …) R) =  Λ(α)+Λ(β)+Λ(γ)
      HERE        milnorWedges  =ᵐ  inscribedTriangle

  This is the last open step of the H4 tier.  `hypVolume_chimney_milnorWedges`
  gave Milnor's value on Milnor's *pieces*; what was missing is that those
  pieces assemble into the triangle.  With this, the Λ-sum is a statement about
  a triangle inscribed in a circle.

  THREE INGREDIENTS, AND NONE OF THEM IS A CONVEXITY ARGUMENT.

  1. THE WEDGE IS EXACTLY THREE HALF-PLANES.  For `0 < ψ < π/2`,

         wedgeAt R θ ψ = {w·u_θ < R cos ψ} ∩ {w·v_{θ−ψ} > 0} ∩ {w·v_{θ+ψ} < 0}

     with `u_φ = (cos φ, sin φ)`, `v_φ = (−sin φ, cos φ)`.  The two edge
     conditions ARE `|w·v_θ| < (w·u_θ)·tan ψ`, on dividing by `cos ψ > 0`.
     H4-5c-ii(a) proved one direction of this (`wedgeAt_upper`,
     `wedgeAt_lower`, for the disjointness); the tiling needs the converse,
     `mem_wedgeAt_of_halfplanes`, which is what turns a membership test into
     three linear inequalities.

  2. `⊆` IS ONE LINEAR IDENTITY.  For a wedge at `(θ, ψ)` tested against the
     chord half-plane of its neighbour at `(θ+ψ+ψ', ψ')`:

         cos ψ · F  =  sin(ψ+ψ') · G₂  +  cos ψ' · G₃

     where `F = R cos ψ' − w·u_{θ+ψ+ψ'}` is the goal, `G₂ = −(w·v_{θ+ψ})` is
     the slack against the SHARED edge, and `G₃ = R cos ψ − w·u_θ` is the
     wedge's slack against its OWN chord.  Both coefficients are positive
     because `0 < ψ+ψ' < π`.  No convex hull, no barycentric coordinates: the
     containment of a triangle in a half-plane is a two-term positive
     combination.

  3. `⊇` IS A SIGN RELATION.  With `x = w·v_t`, `y = w·v_{t+2γ}`,
     `z = w·v_{t+2γ+2α}`,

         sin(2α)·x + sin(2β)·y + sin(2γ)·z = 0                (`perp_sign_relation`)

     and all three coefficients are positive, so `x, y, z` cannot be
     all-positive or all-negative.  The six surviving sign patterns each land
     in one sector, and `T ⊆ H_i` then gives `T ∩ S_i ⊆ W_i` for free.  So the
     covering needs no geometry beyond this one relation — in particular no
     `arctan`, no branch choice, and no arithmetic mod `2π` except in the two
     places where a wedge wraps past the first vertex.

  WHERE ACUTENESS ENTERS — a third time, and in the same way.  `0 < ψ+ψ' < π`
  in (2) and `2α, 2β, 2γ ∈ (0, π)` in (3) are the same inequality that
  H4-5c-ii(a) needed for the disjointness.  Acuteness continues to be *earned*
  from the separation argument rather than imported.

  SCOPE — the honest question here is the triangle's DEFINITION, not the
  tiling.  `inscribedTriangle` is *defined* as the intersection of the three
  chord half-planes.  That is what makes the tiling provable, and it is also
  where one could quietly assume the geometry.  The anchor against that is
  `inscribedTriangle_vertex_incidence`: each of the three points on the circle
  lies on exactly two of the three chord lines and strictly inside the third
  half-plane — the incidence pattern that pins the half-plane triple to THE
  triangle with those vertices.  A full
  `interior (convexHull ℝ {P₁, P₂, P₃})` identification is NOT attempted and
  is NOT claimed.

  And, unchanged from H4-5c-ii(a): this says nothing about ideal tetrahedra.
  That a chimney over the inscribed triangle IS the ideal tetrahedron of the
  corresponding dihedral angles is Milnor's geometric identification, and
  Mathlib has no ideal tetrahedra.

  Archimedean (ℝ): `sin`, `cos`, `tan`, Lebesgue measure, ordering — §7c.

  -- Ref: [milnor1982] Appendix (the circumcentre subdivision)
  -- Ref: [thurston1978] Ch. 7
  -- Ref: [leitner2026] beans qou-w3eg (H4-5), qou-5gai (H4)
-/

import QOU.Archimedean.OrthoschemeLambdaSum

namespace QOU.Archimedean.HyperbolicVolume

open Real MeasureTheory Set
open QOU.Archimedean QOU.Archimedean.IdealTetrahedronConcavity

/-! ### 1. Frame expansions

Rotating the test direction by `±ψ` re-expresses a perpendicular projection in
the frame at `θ`.  Both are pure `ring` after the addition formulas — no
Pythagorean identity is needed, because nothing here is being *rotated*; the
point is fixed and only the test direction moves. -/

/-- Projection on `v_{θ+ψ}`, in the frame at `θ`. -/
theorem perp_add_expand (θ ψ : ℝ) (w : ℝ × ℝ) :
    -(w.1 * Real.sin (θ + ψ)) + w.2 * Real.cos (θ + ψ)
      = -((w.1 * Real.cos θ + w.2 * Real.sin θ) * Real.sin ψ)
        + (-(w.1 * Real.sin θ) + w.2 * Real.cos θ) * Real.cos ψ := by
  simp only [Real.sin_add, Real.cos_add]; ring

/-- Projection on `v_{θ−ψ}`, in the frame at `θ`. -/
theorem perp_sub_expand (θ ψ : ℝ) (w : ℝ × ℝ) :
    -(w.1 * Real.sin (θ - ψ)) + w.2 * Real.cos (θ - ψ)
      = (w.1 * Real.cos θ + w.2 * Real.sin θ) * Real.sin ψ
        + (-(w.1 * Real.sin θ) + w.2 * Real.cos θ) * Real.cos ψ := by
  simp only [Real.sin_sub, Real.cos_sub]; ring

/-! ### 2. The wedge is exactly three half-planes

`wedgeAt_upper` / `wedgeAt_lower` are the forward direction.  This is the
converse, and it is what lets the covering argument put a point back INTO a
wedge from linear inequalities alone. -/

/-- **The converse of `wedgeAt_upper` / `wedgeAt_lower`.**

Being strictly inside the chord half-plane and strictly on the correct side of
each of the two edge lines puts a point in the wedge.  Together with
`wedgeAt_upper` / `wedgeAt_lower` this says the wedge IS the intersection of
those three half-planes. -/
theorem mem_wedgeAt_of_halfplanes {R θ ψ : ℝ} (hψ0 : 0 < ψ) (hψ : ψ < π / 2)
    {w : ℝ × ℝ}
    (hchord : w.1 * Real.cos θ + w.2 * Real.sin θ < R * Real.cos ψ)
    (hup : -(w.1 * Real.sin (θ + ψ)) + w.2 * Real.cos (θ + ψ) < 0)
    (hlo : 0 < -(w.1 * Real.sin (θ - ψ)) + w.2 * Real.cos (θ - ψ)) :
    w ∈ wedgeAt R θ ψ := by
  have hπ : 0 < π := Real.pi_pos
  have hcos : 0 < Real.cos ψ := Real.cos_pos_of_mem_Ioo ⟨by linarith, hψ⟩
  rw [perp_add_expand] at hup
  rw [perp_sub_expand] at hlo
  set p := w.1 * Real.cos θ + w.2 * Real.sin θ with hp
  set q := -(w.1 * Real.sin θ) + w.2 * Real.cos θ with hq
  -- `hup` : q cos ψ < p sin ψ ;  `hlo` : −q cos ψ < p sin ψ
  refine ⟨hchord, ?_⟩
  rw [Real.tan_eq_sin_div_cos,
    show p * (Real.sin ψ / Real.cos ψ) = p * Real.sin ψ / Real.cos ψ by ring, abs_lt]
  refine ⟨?_, ?_⟩
  · rw [neg_lt, lt_div_iff₀ hcos]; linarith
  · rw [lt_div_iff₀ hcos]; linarith

/-! ### 3. `⊆` — a wedge lies inside its neighbours' chord half-planes -/

/-- **The wedge fits inside the chord half-plane of its NEXT neighbour.**

The identity in the header, item 2.  Note there is no `0 < R` hypothesis: the
wedge's own chord slack `G₃` comes straight from membership, so a degenerate
`R` makes the wedge empty and the statement vacuous rather than false. -/
theorem wedgeAt_lt_chord_next {R θ ψ ψ' : ℝ}
    (hψ0 : 0 < ψ) (hψ : ψ < π / 2) (hψ'0 : 0 < ψ') (hψ' : ψ' < π / 2) :
    ∀ w ∈ wedgeAt R θ ψ,
      w.1 * Real.cos (θ + ψ + ψ') + w.2 * Real.sin (θ + ψ + ψ') < R * Real.cos ψ' := by
  intro w hw
  have hπ : 0 < π := Real.pi_pos
  have hcψ : 0 < Real.cos ψ := Real.cos_pos_of_mem_Ioo ⟨by linarith, hψ⟩
  have hcψ' : 0 < Real.cos ψ' := Real.cos_pos_of_mem_Ioo ⟨by linarith, hψ'⟩
  have hs : 0 < Real.sin (ψ + ψ') :=
    Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
  have hG₂ : 0 < -(-(w.1 * Real.sin (θ + ψ)) + w.2 * Real.cos (θ + ψ)) := by
    have := wedgeAt_upper hψ0 hψ w hw; linarith
  have hG₃ : 0 < R * Real.cos ψ - (w.1 * Real.cos θ + w.2 * Real.sin θ) := by
    have := hw.1; linarith
  have key :
      Real.cos ψ * (R * Real.cos ψ'
          - (w.1 * Real.cos (θ + ψ + ψ') + w.2 * Real.sin (θ + ψ + ψ')))
        = Real.sin (ψ + ψ') * (-(-(w.1 * Real.sin (θ + ψ)) + w.2 * Real.cos (θ + ψ)))
          + Real.cos ψ' * (R * Real.cos ψ - (w.1 * Real.cos θ + w.2 * Real.sin θ)) := by
    simp only [Real.sin_add, Real.cos_add]
    linear_combination
      (-(Real.cos ψ') * (w.1 * Real.cos θ + w.2 * Real.sin θ)) * Real.sin_sq_add_cos_sq ψ
  nlinarith [mul_pos hs hG₂, mul_pos hcψ' hG₃]

/-- **The wedge fits inside the chord half-plane of its PREVIOUS neighbour** —
the mirror of `wedgeAt_lt_chord_next`, with the same certificate. -/
theorem wedgeAt_lt_chord_prev {R θ ψ ψ' : ℝ}
    (hψ0 : 0 < ψ) (hψ : ψ < π / 2) (hψ'0 : 0 < ψ') (hψ' : ψ' < π / 2) :
    ∀ w ∈ wedgeAt R θ ψ,
      w.1 * Real.cos (θ - ψ - ψ') + w.2 * Real.sin (θ - ψ - ψ') < R * Real.cos ψ' := by
  intro w hw
  have hπ : 0 < π := Real.pi_pos
  have hcψ : 0 < Real.cos ψ := Real.cos_pos_of_mem_Ioo ⟨by linarith, hψ⟩
  have hcψ' : 0 < Real.cos ψ' := Real.cos_pos_of_mem_Ioo ⟨by linarith, hψ'⟩
  have hs : 0 < Real.sin (ψ + ψ') :=
    Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
  have hG₂ : 0 < -(w.1 * Real.sin (θ - ψ)) + w.2 * Real.cos (θ - ψ) :=
    wedgeAt_lower hψ0 hψ w hw
  have hG₃ : 0 < R * Real.cos ψ - (w.1 * Real.cos θ + w.2 * Real.sin θ) := by
    have := hw.1; linarith
  have key :
      Real.cos ψ * (R * Real.cos ψ'
          - (w.1 * Real.cos (θ - ψ - ψ') + w.2 * Real.sin (θ - ψ - ψ')))
        = Real.sin (ψ + ψ') * (-(w.1 * Real.sin (θ - ψ)) + w.2 * Real.cos (θ - ψ))
          + Real.cos ψ' * (R * Real.cos ψ - (w.1 * Real.cos θ + w.2 * Real.sin θ)) := by
    simp only [Real.sin_sub, Real.cos_sub, Real.sin_add]
    linear_combination
      (-(Real.cos ψ') * (w.1 * Real.cos θ + w.2 * Real.sin θ)) * Real.sin_sq_add_cos_sq ψ
  nlinarith [mul_pos hs hG₂, mul_pos hcψ' hG₃]

/-! ### 4. The inscribed triangle, and the anchor that pins the definition -/

/-- **The chord half-plane** — the open side, containing the circumcentre, of
the line through the chord whose midpoint direction is `θ` and which subtends
central angle `2ψ`. -/
def chordHalfplane (R θ ψ : ℝ) : Set (ℝ × ℝ) :=
  {w | w.1 * Real.cos θ + w.2 * Real.sin θ < R * Real.cos ψ}

theorem isOpen_chordHalfplane (R θ ψ : ℝ) : IsOpen (chordHalfplane R θ ψ) :=
  isOpen_lt (by fun_prop) continuous_const

theorem measurableSet_chordHalfplane (R θ ψ : ℝ) :
    MeasurableSet (chordHalfplane R θ ψ) :=
  (isOpen_chordHalfplane R θ ψ).measurableSet

/-- `2π`-periodicity of the chord half-plane, needed exactly twice below (the
two wedges whose neighbour lies past the first vertex). -/
theorem chordHalfplane_add_two_pi (R θ ψ : ℝ) :
    chordHalfplane R (θ + 2 * π) ψ = chordHalfplane R θ ψ := by
  simp [chordHalfplane, Real.cos_add_two_pi, Real.sin_add_two_pi]

/-- **The triangle inscribed in the circle of radius `R`** with inscribed
angles `(α, β, γ)` and first vertex at angle `t`, as the intersection of its
three chord half-planes.

See `inscribedTriangle_vertex_incidence` for the anchor that ties this
definition to the triangle with the three named vertices. -/
def inscribedTriangle (R t α β γ : ℝ) : Set (ℝ × ℝ) :=
  chordHalfplane R (t + γ) γ ∩ chordHalfplane R (t + 2 * γ + α) α ∩
    chordHalfplane R (t + 2 * γ + 2 * α + β) β

theorem measurableSet_inscribedTriangle (R t α β γ : ℝ) :
    MeasurableSet (inscribedTriangle R t α β γ) :=
  ((measurableSet_chordHalfplane _ _ _).inter
    (measurableSet_chordHalfplane _ _ _)).inter (measurableSet_chordHalfplane _ _ _)

/-- The point of the circle of radius `R` at angle `a`. -/
noncomputable def circlePoint (R a : ℝ) : ℝ × ℝ := (R * Real.cos a, R * Real.sin a)

/-- Testing a circle point against a chord direction sees only the angle
between them. -/
theorem circlePoint_dot (R a θ : ℝ) :
    (circlePoint R a).1 * Real.cos θ + (circlePoint R a).2 * Real.sin θ
      = R * Real.cos (a - θ) := by
  simp only [circlePoint, Real.cos_sub]; ring

/-- The elementary product-to-sum step behind every strict incidence below. -/
theorem cos_sub_cos_two_mul_add (x y : ℝ) :
    Real.cos x - Real.cos (2 * y + x) = 2 * Real.sin (y + x) * Real.sin y := by
  simp only [Real.cos_add, Real.sin_add, Real.cos_two_mul, Real.sin_two_mul]
  linear_combination (-2 * Real.cos x) * Real.sin_sq_add_cos_sq y

/-! ### 5. `⊆` — the three wedges lie in the triangle -/

/-- **Milnor's three wedges lie inside the inscribed triangle.**

Nine containments; each is one application of `wedgeAt_lt_chord_next` or
`wedgeAt_lt_chord_prev`, except the three that are a wedge's own chord (by
definition).  Two of the nine cross the first vertex and pick up the `2π`
shift — the only place periodicity is used. -/
theorem milnorWedges_subset_inscribedTriangle {R t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ0 : 0 < γ)
    (hα : α < π / 2) (hβ : β < π / 2) (hγ : γ < π / 2) (hsum : α + β + γ = π) :
    milnorWedges R t α β γ ⊆ inscribedTriangle R t α β γ := by
  rintro w ((hw | hw) | hw)
  · -- W₁ = wedgeAt R (t+γ) γ
    refine ⟨⟨hw.1, ?_⟩, ?_⟩
    · have h := wedgeAt_lt_chord_next hγ0 hγ hα0 hα w hw
      rwa [show t + γ + γ + α = t + 2 * γ + α by ring] at h
    · have h := wedgeAt_lt_chord_prev hγ0 hγ hβ0 hβ w hw
      rwa [show t + γ - γ - β = t + 2 * γ + 2 * α + β - 2 * π by linarith,
        Real.cos_sub_two_pi, Real.sin_sub_two_pi] at h
  · -- W₂ = wedgeAt R (t+2γ+α) α
    refine ⟨⟨?_, hw.1⟩, ?_⟩
    · have h := wedgeAt_lt_chord_prev hα0 hα hγ0 hγ w hw
      rwa [show t + 2 * γ + α - α - γ = t + γ by ring] at h
    · have h := wedgeAt_lt_chord_next hα0 hα hβ0 hβ w hw
      rwa [show t + 2 * γ + α + α + β = t + 2 * γ + 2 * α + β by ring] at h
  · -- W₃ = wedgeAt R (t+2γ+2α+β) β
    refine ⟨⟨?_, ?_⟩, hw.1⟩
    · have h := wedgeAt_lt_chord_next hβ0 hβ hγ0 hγ w hw
      rwa [show t + 2 * γ + 2 * α + β + β + γ = t + γ + 2 * π by linarith,
        Real.cos_add_two_pi, Real.sin_add_two_pi] at h
    · have h := wedgeAt_lt_chord_prev hβ0 hβ hα0 hα w hw
      rwa [show t + 2 * γ + 2 * α + β - β - α = t + 2 * γ + α by ring] at h

/-! ### 6. `⊇` — the sign relation, and the covering -/

/-- **The sign relation.**

The three edge functionals `w·v_t`, `w·v_{t+2γ}`, `w·v_{t+2γ+2α}` are three
linear functionals on a two-dimensional space, so they satisfy one relation;
`α+β+γ = π` makes its coefficients `sin 2α, sin 2β, sin 2γ` — all POSITIVE for
acute angles.  That positivity is the whole covering argument: it forbids the
two sign patterns that would leave a point of the triangle in no sector. -/
theorem perp_sign_relation {t α β γ : ℝ} (hsum : α + β + γ = π) (w : ℝ × ℝ) :
    Real.sin (2 * α) * (-(w.1 * Real.sin t) + w.2 * Real.cos t)
      + Real.sin (2 * β) * (-(w.1 * Real.sin (t + 2 * γ)) + w.2 * Real.cos (t + 2 * γ))
      + Real.sin (2 * γ)
          * (-(w.1 * Real.sin (t + (2 * γ + 2 * α)))
              + w.2 * Real.cos (t + (2 * γ + 2 * α))) = 0 := by
  have hb : Real.sin (2 * β)
      = -(Real.sin (2 * α) * Real.cos (2 * γ) + Real.cos (2 * α) * Real.sin (2 * γ)) := by
    rw [show 2 * β = 2 * π - (2 * α + 2 * γ) by linarith]
    simp [Real.sin_sub, Real.sin_add, Real.cos_add]
  rw [perp_add_expand t (2 * γ) w, perp_add_expand t (2 * γ + 2 * α) w, hb]
  simp only [Real.sin_add, Real.cos_add]
  linear_combination
    (-((-(w.1 * Real.sin t) + w.2 * Real.cos t) * Real.sin (2 * α)))
      * Real.sin_sq_add_cos_sq (2 * γ)

/-- **The covering.**

A point of the triangle that is off all three edge lines lies in one of the
three wedges.  The case split is on the signs of the three edge functionals;
`perp_sign_relation` kills the all-positive and all-negative branches, and each
of the six survivors is one application of `mem_wedgeAt_of_halfplanes`. -/
theorem inscribedTriangle_subset_milnorWedges_of_ne {R t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ0 : 0 < γ)
    (hα : α < π / 2) (hβ : β < π / 2) (hγ : γ < π / 2) (hsum : α + β + γ = π)
    {w : ℝ × ℝ} (hw : w ∈ inscribedTriangle R t α β γ)
    (hx : -(w.1 * Real.sin t) + w.2 * Real.cos t ≠ 0)
    (hy : -(w.1 * Real.sin (t + 2 * γ)) + w.2 * Real.cos (t + 2 * γ) ≠ 0)
    (hz : -(w.1 * Real.sin (t + (2 * γ + 2 * α)))
            + w.2 * Real.cos (t + (2 * γ + 2 * α)) ≠ 0) :
    w ∈ milnorWedges R t α β γ := by
  obtain ⟨⟨h₁, h₂⟩, h₃⟩ := hw
  have hπ : 0 < π := Real.pi_pos
  have s2α : 0 < Real.sin (2 * α) :=
    Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
  have s2β : 0 < Real.sin (2 * β) :=
    Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
  have s2γ : 0 < Real.sin (2 * γ) :=
    Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
  have hrel := perp_sign_relation (t := t) (α := α) (β := β) (γ := γ) hsum w
  -- the three sector tests, named
  set x := -(w.1 * Real.sin t) + w.2 * Real.cos t with hxdef
  set y := -(w.1 * Real.sin (t + 2 * γ)) + w.2 * Real.cos (t + 2 * γ) with hydef
  set z := -(w.1 * Real.sin (t + (2 * γ + 2 * α)))
              + w.2 * Real.cos (t + (2 * γ + 2 * α)) with hzdef
  -- membership in each wedge, from three half-planes
  have mem₁ : 0 < x → y < 0 → w ∈ wedgeAt R (t + γ) γ := by
    intro hxp hyn
    refine mem_wedgeAt_of_halfplanes hγ0 hγ h₁ ?_ ?_
    · rw [show t + γ + γ = t + 2 * γ by ring]; exact hyn
    · rw [show t + γ - γ = t by ring]; exact hxp
  have mem₂ : 0 < y → z < 0 → w ∈ wedgeAt R (t + 2 * γ + α) α := by
    intro hyp hzn
    refine mem_wedgeAt_of_halfplanes hα0 hα h₂ ?_ ?_
    · rw [show t + 2 * γ + α + α = t + (2 * γ + 2 * α) by ring]; exact hzn
    · rw [show t + 2 * γ + α - α = t + 2 * γ by ring]; exact hyp
  have mem₃ : 0 < z → x < 0 → w ∈ wedgeAt R (t + 2 * γ + 2 * α + β) β := by
    intro hzp hxn
    refine mem_wedgeAt_of_halfplanes hβ0 hβ h₃ ?_ ?_
    · rw [show t + 2 * γ + 2 * α + β + β = t + 2 * π by linarith,
        Real.sin_add_two_pi, Real.cos_add_two_pi]
      exact hxn
    · rw [show t + 2 * γ + 2 * α + β - β = t + (2 * γ + 2 * α) by ring]; exact hzp
  rcases hx.lt_or_gt with hxs | hxs
  · -- x < 0
    rcases hz.lt_or_gt with hzs | hzs
    · rcases hy.lt_or_gt with hys | hys
      · exact absurd hrel (by nlinarith)
      · exact Or.inl (Or.inr (mem₂ hys hzs))
    · exact Or.inr (mem₃ hzs hxs)
  · -- 0 < x
    rcases hy.lt_or_gt with hys | hys
    · exact Or.inl (Or.inl (mem₁ hxs hys))
    · rcases hz.lt_or_gt with hzs | hzs
      · exact Or.inl (Or.inr (mem₂ hys hzs))
      · exact absurd hrel (by nlinarith)

/-! ### 7. The exceptional set is null

The three edge lines.  Larger than the three spine SEGMENTS that actually get
lost, but null for a much cheaper reason: each is the kernel of a nonzero
linear functional. -/

/-- The functional whose kernel is the edge line in direction `φ`. -/
noncomputable def perpFunctional (φ : ℝ) : (ℝ × ℝ) →ₗ[ℝ] ℝ where
  toFun w := -(w.1 * Real.sin φ) + w.2 * Real.cos φ
  map_add' := by intro a b; simp; ring
  map_smul' := by intro c a; simp; ring

@[simp] theorem perpFunctional_apply (φ : ℝ) (w : ℝ × ℝ) :
    perpFunctional φ w = -(w.1 * Real.sin φ) + w.2 * Real.cos φ := rfl

/-- **An edge line is null.**  A line through the origin in the plane. -/
theorem volume_perpLine (φ : ℝ) :
    (volume : Measure (ℝ × ℝ)) {w | -(w.1 * Real.sin φ) + w.2 * Real.cos φ = 0} = 0 := by
  have hne : LinearMap.ker (perpFunctional φ) ≠ ⊤ := by
    intro htop
    have hmem : (-Real.sin φ, Real.cos φ) ∈ LinearMap.ker (perpFunctional φ) := by
      rw [htop]; trivial
    rw [LinearMap.mem_ker, perpFunctional_apply] at hmem
    nlinarith [Real.sin_sq_add_cos_sq φ]
  have hset : {w : ℝ × ℝ | -(w.1 * Real.sin φ) + w.2 * Real.cos φ = 0}
      = (LinearMap.ker (perpFunctional φ) : Set (ℝ × ℝ)) := by
    ext w; simp [LinearMap.mem_ker]
  rw [hset]
  exact Measure.addHaar_submodule _ _ hne

/-! ### 8. H4-5c-ii(b) — the tiling, and the Λ-sum on a triangle -/

/-- **THE TILING.**  Milnor's three wedges are the inscribed triangle, up to a
null set. -/
theorem milnorWedges_ae_eq_inscribedTriangle {R t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ0 : 0 < γ)
    (hα : α < π / 2) (hβ : β < π / 2) (hγ : γ < π / 2) (hsum : α + β + γ = π) :
    milnorWedges R t α β γ =ᵐ[(volume : Measure (ℝ × ℝ))] inscribedTriangle R t α β γ := by
  have hsub := milnorWedges_subset_inscribedTriangle
    (R := R) (t := t) hα0 hβ0 hγ0 hα hβ hγ hsum
  rw [ae_eq_set]
  constructor
  · simp [Set.diff_eq_empty.mpr hsub]
  · -- the leftover lies in the union of the three edge lines
    refine measure_mono_null ?_
      (measure_union_null (measure_union_null (volume_perpLine t)
        (volume_perpLine (t + 2 * γ))) (volume_perpLine (t + (2 * γ + 2 * α))))
    intro w hw
    by_contra hcon
    simp only [Set.mem_union, Set.mem_setOf_eq, not_or] at hcon
    exact hw.2 (inscribedTriangle_subset_milnorWedges_of_ne hα0 hβ0 hγ0 hα hβ hγ hsum
      hw.1 hcon.1.1 hcon.1.2 hcon.2)

/-- **Milnor's Λ-sum, on the inscribed triangle.**

    Vol(chimney (inscribedTriangle R t α β γ) R)  =  Λ(α) + Λ(β) + Λ(γ)

The H4 tier's target, now stated on a triangle rather than on a union of three
wedges.  The hypotheses are Milnor's: three positive acute angles summing to
`π`.

The base is a.e. inside the open disk rather than pointwise inside it — the
closed inscribed triangle has its three vertices ON the circle, where the fibre
mass is `⊤`.  That is exactly the a.e. form H4-2 was stated in
(`hypVolume_chimney_of_ae_lt`), and here is where it is spent. -/
theorem hypVolume_chimney_inscribedTriangle {R t α β γ : ℝ} (hR : 0 < R)
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ0 : 0 < γ)
    (hα : α < π / 2) (hβ : β < π / 2) (hγ : γ < π / 2) (hsum : α + β + γ = π) :
    hypVolume (chimney (inscribedTriangle R t α β γ) R)
      = ENNReal.ofReal (Lob α + Lob β + Lob γ) := by
  have hae := milnorWedges_ae_eq_inscribedTriangle
    (R := R) (t := t) hα0 hβ0 hγ0 hα hβ hγ hsum
  have hMmeas : MeasurableSet (milnorWedges R t α β γ) :=
    ((measurableSet_wedgeAt _ _ _).union (measurableSet_wedgeAt _ _ _)).union
      (measurableSet_wedgeAt _ _ _)
  have hMsub : ∀ w ∈ milnorWedges R t α β γ, w.1 ^ 2 + w.2 ^ 2 < R ^ 2 := by
    rintro w ((hw | hw) | hw)
    · exact wedgeAt_subset_disk hγ0 hγ w hw
    · exact wedgeAt_subset_disk hα0 hα w hw
    · exact wedgeAt_subset_disk hβ0 hβ w hw
  have hres : (volume : Measure (ℝ × ℝ)).restrict (inscribedTriangle R t α β γ)
      = (volume : Measure (ℝ × ℝ)).restrict (milnorWedges R t α β γ) :=
    Measure.restrict_congr_set hae.symm
  rw [hypVolume_chimney_of_ae_lt (measurableSet_inscribedTriangle R t α β γ)
      (by rw [hres]; exact (ae_restrict_iff' hMmeas).mpr (Filter.Eventually.of_forall hMsub)),
    setLIntegral_congr hae.symm,
    ← hypVolume_chimney_of_subset_disk hMmeas hMsub]
  exact hypVolume_chimney_milnorWedges hR hα0 hβ0 hγ0 hα hβ hγ hsum

/-! ### 9. The anchor: the definition really is the triangle with those vertices

`inscribedTriangle` is DEFINED as an intersection of three half-planes.  This
is what keeps that from quietly assuming the geometry: the three points of the
circle at angles `t`, `t+2γ`, `t+2γ+2α` sit on the boundary in the pattern that
characterises a triangle's vertices — each on exactly two of the three chord
lines, and strictly inside the third half-plane.

That, plus convexity of a half-plane intersection, is what "the triangle with
those vertices" means.  A full `interior (convexHull ℝ {P₁, P₂, P₃})`
identification is not attempted here. -/

/-- **Vertex incidence.**  Each of the three circle points lies ON two chord
lines and STRICTLY INSIDE the third half-plane.

This is what pins `inscribedTriangle` to the triangle whose vertices are the
three named points of the circle.  Strictness in the third slot is where
`0 < R` is spent: the gap is `2R·sin·sin`.

**No acuteness.**  This statement held for every positive triple summing to `π`
all along; the three `< π/2` hypotheses it used to carry were inherited from its
neighbours and were consumed by nothing (dropped 2026-09-08, bean `qou-w3eg`).
Each is spent only inside a `Real.sin_pos_of_pos_of_lt_pi` whose side goal is
`X < π`, and `α + β + γ = π` with the other two positive already gives that.
The gap `cos ψ' − cos(2ψ+ψ') = 2 sin(ψ+ψ') sin ψ` is positive whenever both
sines are, which on the simplex is everywhere.

That matters downstream rather than here: this lemma is the only place the
`idealTet_eq_chimney` chain touched acuteness, so its removal carries the
vertex-defined-region identity to obtuse triangles as well. -/
theorem inscribedTriangle_vertex_incidence {R t α β γ : ℝ} (hR : 0 < R)
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ0 : 0 < γ) (hsum : α + β + γ = π) :
    -- P₁, at angle `t`: on chord lines 1 and 3, strictly inside half-plane 2
    ((circlePoint R t).1 * Real.cos (t + γ) + (circlePoint R t).2 * Real.sin (t + γ)
        = R * Real.cos γ
      ∧ (circlePoint R t).1 * Real.cos (t + 2 * γ + 2 * α + β)
          + (circlePoint R t).2 * Real.sin (t + 2 * γ + 2 * α + β) = R * Real.cos β
      ∧ circlePoint R t ∈ chordHalfplane R (t + 2 * γ + α) α)
    -- P₂, at angle `t+2γ`: on chord lines 1 and 2, strictly inside half-plane 3
    ∧ ((circlePoint R (t + 2 * γ)).1 * Real.cos (t + γ)
          + (circlePoint R (t + 2 * γ)).2 * Real.sin (t + γ) = R * Real.cos γ
      ∧ (circlePoint R (t + 2 * γ)).1 * Real.cos (t + 2 * γ + α)
          + (circlePoint R (t + 2 * γ)).2 * Real.sin (t + 2 * γ + α) = R * Real.cos α
      ∧ circlePoint R (t + 2 * γ) ∈ chordHalfplane R (t + 2 * γ + 2 * α + β) β)
    -- P₃, at angle `t+2γ+2α`: on chord lines 2 and 3, strictly inside half-plane 1
    ∧ ((circlePoint R (t + 2 * γ + 2 * α)).1 * Real.cos (t + 2 * γ + α)
          + (circlePoint R (t + 2 * γ + 2 * α)).2 * Real.sin (t + 2 * γ + α)
            = R * Real.cos α
      ∧ (circlePoint R (t + 2 * γ + 2 * α)).1 * Real.cos (t + 2 * γ + 2 * α + β)
          + (circlePoint R (t + 2 * γ + 2 * α)).2 * Real.sin (t + 2 * γ + 2 * α + β)
            = R * Real.cos β
      ∧ circlePoint R (t + 2 * γ + 2 * α) ∈ chordHalfplane R (t + γ) γ) := by
  have hπ : 0 < π := Real.pi_pos
  have sα : 0 < Real.sin α := Real.sin_pos_of_pos_of_lt_pi hα0 (by linarith)
  have sβ : 0 < Real.sin β := Real.sin_pos_of_pos_of_lt_pi hβ0 (by linarith)
  have sγ : 0 < Real.sin γ := Real.sin_pos_of_pos_of_lt_pi hγ0 (by linarith)
  -- the strict slot, three times: `cos ψ' − cos(2ψ+ψ') = 2 sin(ψ+ψ') sin ψ`
  have strict : ∀ x y : ℝ, 0 < Real.sin (y + x) → 0 < Real.sin y →
      R * Real.cos (2 * y + x) < R * Real.cos x := by
    intro x y hsyx hsy
    nlinarith [cos_sub_cos_two_mul_add x y, mul_pos hsyx hsy]
  refine ⟨⟨?_, ?_, ?_⟩, ⟨?_, ?_, ?_⟩, ⟨?_, ?_, ?_⟩⟩
  · rw [circlePoint_dot, show t - (t + γ) = -γ by ring, Real.cos_neg]
  · rw [circlePoint_dot, show t - (t + 2 * γ + 2 * α + β) = β - 2 * π by linarith,
      Real.cos_sub_two_pi]
  · simp only [chordHalfplane, Set.mem_setOf_eq]
    rw [circlePoint_dot, show t - (t + 2 * γ + α) = -(2 * γ + α) by ring, Real.cos_neg]
    exact strict α γ (by rw [show γ + α = π - β by linarith, Real.sin_pi_sub]; exact sβ) sγ
  · rw [circlePoint_dot, show t + 2 * γ - (t + γ) = γ by ring]
  · rw [circlePoint_dot, show t + 2 * γ - (t + 2 * γ + α) = -α by ring, Real.cos_neg]
  · simp only [chordHalfplane, Set.mem_setOf_eq]
    rw [circlePoint_dot,
      show t + 2 * γ - (t + 2 * γ + 2 * α + β) = -(2 * α + β) by ring, Real.cos_neg]
    exact strict β α (by rw [show α + β = π - γ by linarith, Real.sin_pi_sub]; exact sγ) sα
  · rw [circlePoint_dot, show t + 2 * γ + 2 * α - (t + 2 * γ + α) = α by ring]
  · rw [circlePoint_dot, show t + 2 * γ + 2 * α - (t + 2 * γ + 2 * α + β) = -β by ring,
      Real.cos_neg]
  · simp only [chordHalfplane, Set.mem_setOf_eq]
    rw [circlePoint_dot, show t + 2 * γ + 2 * α - (t + γ) = 2 * α + γ by ring]
    exact strict γ α (by rw [show α + γ = π - β by linarith, Real.sin_pi_sub]; exact sβ) sα

end QOU.Archimedean.HyperbolicVolume
