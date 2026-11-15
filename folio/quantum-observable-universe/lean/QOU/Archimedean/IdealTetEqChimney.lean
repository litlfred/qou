/-
# File A3 — THE THEOREM: the vertex-defined ideal tetrahedron IS the chimney.

`idealTetrahedron ∞ P₁ P₂ P₃` (File A2) was built purely from its four ideal
vertices, with **no** reference to `chordHalfplane` or `inscribedTriangle`.  This
file DERIVES the chords from the faces and proves the region identity

    idealTetrahedron (circlePoint 1 t) (circlePoint 1 (t+2γ)) (circlePoint 1 (t+2γ+2α))
      = chimney (inscribedTriangle 1 t α β γ) 1

(for an acute admissible triple `α + β + γ = π`).  This is what upgrades the T2
development from `region_eq_chimney := rfl` (an adopted convention) to
`region_eq_chimney` **proved** as a genuine set-equality.

## The derivation (chords FROM the faces — the design rule)

The engine is `sarea_circlePoint_unit` (File A2): the signed area of the chord of
the unit circle between the vertices at angles `u` and `u + 2ψ`, tested against a
point `w`, is `2 sin ψ · (cos ψ − w·n)` with `n = (cos(u+ψ), sin(u+ψ))`.  That is
`2 sin ψ` times exactly the functional `cos ψ − w·n` a `chordHalfplane` compares to
`0`.  Orienting each vertical face by the opposite (interior) vertex — whose sign is
fixed by `inscribedTriangle_vertex_incidence` — turns the vertex-defined half-space
`{0 < sarea ·i · sarea ·w}` into the chord half-plane.  The hemisphere face is the
`∞`-side of the unit hemisphere, which is definitionally the chimney's floor.

Three vertical faces ⟶ the three chord half-planes; the hemisphere face ⟶ the floor;
their conjunction is the chimney.  Sorry-free, no new axiom; the ONLY cited input is
the totally-geodesic classification adopted (as a definition) in File A1.

Archimedean (ℝ): `sin`, `cos`, `Real.sqrt`, ordering — §7c.

  -- Ref: [milnor1982] Appendix ; [thurston1978] Ch. 7 ; [ratcliffe] §4.6–4.7
  -- Ref: [leitner2026] beans qou-idvt (T2), qou-473l (T2 vertex-independence)
-/

import QOU.Archimedean.IdealTetFromVertices
import QOU.Archimedean.IdealTetrahedronRegion

namespace QOU.Archimedean

open Real
open QOU.Archimedean.HyperbolicVolume

/-! ### The three vertical-face reductions (chord half-planes, DERIVED) -/

/-- **Face opposite `P₃`** (through `∞, P₁, P₂`), oriented toward `P₃`, projects to
chord 1 of the inscribed triangle. -/
theorem face1 {t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ0 : 0 < γ) (hsum : α + β + γ = π)
    (w : ℝ × ℝ) :
    (0 < sarea (circlePoint 1 t) (circlePoint 1 (t + 2 * γ))
        (circlePoint 1 (t + 2 * γ + 2 * α)) *
      sarea (circlePoint 1 t) (circlePoint 1 (t + 2 * γ)) w)
      ↔ w ∈ chordHalfplane 1 (t + γ) γ := by
  have hπ : 0 < π := Real.pi_pos
  have hsinγ : 0 < Real.sin γ := Real.sin_pos_of_pos_of_lt_pi hγ0 (by linarith)
  have hw := sarea_circlePoint_unit t γ w
  have hP3 := sarea_circlePoint_unit t γ (circlePoint 1 (t + 2 * γ + 2 * α))
  have hinc := (inscribedTriangle_vertex_incidence (R := 1) (t := t)
      one_pos hα0 hβ0 hγ0 hsum).2.2.2.2
  simp only [chordHalfplane, Set.mem_setOf_eq, one_mul] at hinc ⊢
  have hpos : 0 < sarea (circlePoint 1 t) (circlePoint 1 (t + 2 * γ))
      (circlePoint 1 (t + 2 * γ + 2 * α)) := by
    rw [hP3]
    have : 0 < Real.cos γ - ((circlePoint 1 (t + 2 * γ + 2 * α)).1 * Real.cos (t + γ)
        + (circlePoint 1 (t + 2 * γ + 2 * α)).2 * Real.sin (t + γ)) := by linarith [hinc]
    positivity
  rw [hw, mul_pos_iff_of_pos_left hpos]
  constructor
  · intro h; nlinarith [hsinγ]
  · intro h; nlinarith [hsinγ]

/-- **Face opposite `P₁`** (through `∞, P₂, P₃`), oriented toward `P₁`, projects to
chord 2 of the inscribed triangle. -/
theorem face2 {t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ0 : 0 < γ) (hsum : α + β + γ = π)
    (w : ℝ × ℝ) :
    (0 < sarea (circlePoint 1 (t + 2 * γ)) (circlePoint 1 (t + 2 * γ + 2 * α))
        (circlePoint 1 t) *
      sarea (circlePoint 1 (t + 2 * γ)) (circlePoint 1 (t + 2 * γ + 2 * α)) w)
      ↔ w ∈ chordHalfplane 1 (t + 2 * γ + α) α := by
  have hπ : 0 < π := Real.pi_pos
  have hsinα : 0 < Real.sin α := Real.sin_pos_of_pos_of_lt_pi hα0 (by linarith)
  have hw := sarea_circlePoint_unit (t + 2 * γ) α w
  have hP1 := sarea_circlePoint_unit (t + 2 * γ) α (circlePoint 1 t)
  have hinc := (inscribedTriangle_vertex_incidence (R := 1) (t := t)
      one_pos hα0 hβ0 hγ0 hsum).1.2.2
  simp only [chordHalfplane, Set.mem_setOf_eq, one_mul] at hinc ⊢
  have hpos : 0 < sarea (circlePoint 1 (t + 2 * γ)) (circlePoint 1 (t + 2 * γ + 2 * α))
      (circlePoint 1 t) := by
    rw [hP1]
    have : 0 < Real.cos α - ((circlePoint 1 t).1 * Real.cos (t + 2 * γ + α)
        + (circlePoint 1 t).2 * Real.sin (t + 2 * γ + α)) := by linarith [hinc]
    positivity
  rw [hw, mul_pos_iff_of_pos_left hpos]
  constructor
  · intro h; nlinarith [hsinα]
  · intro h; nlinarith [hsinα]

/-- **The chord `P₁P₃` in chord-3 form.**  Its subtended half-angle `γ + α = π − β`
exceeds `π/2`, so `sarea_circlePoint_unit` produces the perpendicular-bisector
direction `t + γ + α`, which is `θ₃ − π` for the chord-3 direction `θ₃ = t+2γ+2α+β`.
Rewriting with `α + β + γ = π` gives `sarea P₁P₃ w = 2 sin β · (w·nθ₃ − cos β)` —
the same functional chord 3 tests, up to the sign carried by the `− π` shift. -/
theorem sareaP1P3 {t α β γ : ℝ} (hsum : α + β + γ = π) (w : ℝ × ℝ) :
    sarea (circlePoint 1 t) (circlePoint 1 (t + 2 * γ + 2 * α)) w
      = 2 * Real.sin β * ((w.1 * Real.cos (t + 2 * γ + 2 * α + β)
          + w.2 * Real.sin (t + 2 * γ + 2 * α + β)) - Real.cos β) := by
  have h := sarea_circlePoint_unit t (γ + α) w
  rw [show t + 2 * (γ + α) = t + 2 * γ + 2 * α by ring] at h
  rw [h]
  have hgα : γ + α = π - β := by linarith
  have hsg : Real.sin (γ + α) = Real.sin β := by rw [hgα, Real.sin_pi_sub]
  have hcg : Real.cos (γ + α) = - Real.cos β := by rw [hgα, Real.cos_pi_sub]
  have hdir : t + (γ + α) = (t + 2 * γ + 2 * α + β) - π := by linarith
  have hcd : Real.cos (t + (γ + α)) = - Real.cos (t + 2 * γ + 2 * α + β) := by
    rw [hdir, Real.cos_sub, Real.cos_pi, Real.sin_pi]; ring
  have hsd : Real.sin (t + (γ + α)) = - Real.sin (t + 2 * γ + 2 * α + β) := by
    rw [hdir, Real.sin_sub, Real.cos_pi, Real.sin_pi]; ring
  rw [hsg, hcg, hcd, hsd]; ring

/-- **Face opposite `P₂`** (through `∞, P₁, P₃`), oriented toward `P₂`, projects to
chord 3 of the inscribed triangle.  Here the half-angle `γ + α = π − β` exceeds
`π/2`, so the signed area appears with the OPPOSITE sign; the orientation vertex
`P₂` (negative side) still pins the half-space to chord 3. -/
theorem face3 {t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ0 : 0 < γ) (hsum : α + β + γ = π)
    (w : ℝ × ℝ) :
    (0 < sarea (circlePoint 1 t) (circlePoint 1 (t + 2 * γ + 2 * α))
        (circlePoint 1 (t + 2 * γ)) *
      sarea (circlePoint 1 t) (circlePoint 1 (t + 2 * γ + 2 * α)) w)
      ↔ w ∈ chordHalfplane 1 (t + 2 * γ + 2 * α + β) β := by
  have hπ : 0 < π := Real.pi_pos
  have hsinβ : 0 < Real.sin β := Real.sin_pos_of_pos_of_lt_pi hβ0 (by linarith)
  have hw := sareaP1P3 (t := t) (α := α) (β := β) (γ := γ) hsum w
  have hP2 := sareaP1P3 (t := t) (α := α) (β := β) (γ := γ) hsum (circlePoint 1 (t + 2 * γ))
  have hinc := (inscribedTriangle_vertex_incidence (R := 1) (t := t)
      one_pos hα0 hβ0 hγ0 hsum).2.1.2.2
  simp only [chordHalfplane, Set.mem_setOf_eq, one_mul] at hinc ⊢
  have hneg : sarea (circlePoint 1 t) (circlePoint 1 (t + 2 * γ + 2 * α))
      (circlePoint 1 (t + 2 * γ)) < 0 := by
    rw [hP2]
    have : (circlePoint 1 (t + 2 * γ)).1 * Real.cos (t + 2 * γ + 2 * α + β)
        + (circlePoint 1 (t + 2 * γ)).2 * Real.sin (t + 2 * γ + 2 * α + β) - Real.cos β < 0 := by
      linarith [hinc]
    nlinarith [hsinβ, this]
  rw [hw, mul_pos_iff]
  constructor
  · rintro (⟨ha, _⟩ | ⟨_, hb⟩)
    · exact absurd ha (not_lt.2 hneg.le)
    · nlinarith [hsinβ]
  · intro hX
    exact Or.inr ⟨hneg, by nlinarith [hsinβ]⟩

/-! ### The region identity -/

/-- **THE THEOREM.**  The Milnor-normalized ideal tetrahedron with far vertex `∞` and
three finite vertices on the unit circle at angles `t`, `t + 2γ`, `t + 2γ + 2α`
(defined from those vertices in File A2, independently of any chord data) EQUALS the
chimney over the inscribed triangle of angles `(α, β, γ)`.

This replaces `region_eq_chimney := rfl` with a genuine set-equality: the region is
now an independent object, and its coincidence with the chimney is a proved theorem,
not an adopted convention.  Sorry-free; the only cited input is the totally-geodesic
classification adopted as a definition in File A1. -/
theorem idealTet_eq_chimney {t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ0 : 0 < γ) (hsum : α + β + γ = π) :
    idealTetrahedron (circlePoint 1 t) (circlePoint 1 (t + 2 * γ))
        (circlePoint 1 (t + 2 * γ + 2 * α))
      = chimney (inscribedTriangle 1 t α β γ) 1 := by
  ext p
  have hf1 := face1 (t := t) hα0 hβ0 hγ0 hsum (p 0, p 1)
  have hf2 := face2 (t := t) hα0 hβ0 hγ0 hsum (p 0, p 1)
  have hf3 := face3 (t := t) hα0 hβ0 hγ0 hsum (p 0, p 1)
  -- membership in the four half-spaces (LHS) and in the chimney (RHS), unfolded
  have hL : p ∈ idealTetrahedron (circlePoint 1 t) (circlePoint 1 (t + 2 * γ))
        (circlePoint 1 (t + 2 * γ + 2 * α)) ↔
      (Real.sqrt ((1 : ℝ) ^ 2 - (p 0) ^ 2 - (p 1) ^ 2) < p 2)
        ∧ (p 0, p 1) ∈ chordHalfplane 1 (t + 2 * γ + α) α
        ∧ (p 0, p 1) ∈ chordHalfplane 1 (t + 2 * γ + 2 * α + β) β
        ∧ (p 0, p 1) ∈ chordHalfplane 1 (t + γ) γ := by
    rw [mem_idealTetrahedron]
    refine and_congr Iff.rfl (and_congr ?_ (and_congr ?_ ?_))
    · exact hf2
    · exact hf3
    · exact hf1
  rw [hL]
  simp only [chimney, inscribedTriangle, Set.mem_setOf_eq, Set.mem_inter_iff]
  constructor
  · rintro ⟨hfl, h2, h3, h1⟩; exact ⟨⟨⟨h1, h2⟩, h3⟩, hfl⟩
  · rintro ⟨⟨⟨h1, h2⟩, h3⟩, hfl⟩; exact ⟨hfl, h2, h3, h1⟩

end QOU.Archimedean
