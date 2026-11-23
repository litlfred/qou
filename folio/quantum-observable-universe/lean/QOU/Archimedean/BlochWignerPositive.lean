/-
  `0 < D(z)` on the upper half plane — STRICT, which is the half that was needed.

  Bean `qou-0ag0`; closes the last part of `qou-f8lit` item 3.

  ═══ THE STATED OBSTACLE WAS WRONG, AND IT WAS MINE ═══

  `Archimedean/BlochWignerNonneg.lean` landed the non-strict `0 ≤ D(z)` an hour before
  this file, and its header says of strictness:

      "Ruling that out needs the angles bounded away from the corners, or a strict form
       of the subadditivity — neither of which is here."

  **Neither is what this file uses.**  The angles are not bounded away from anything, and
  the subadditivity is used only in its existing non-strict form.  That paragraph is
  corrected in place; it is recorded here too, because it is the second time in one
  session that a stated obstacle to this result described the route being attempted rather
  than the problem.

  ═══ THE ARGUMENT ═══

  Strict concavity of the `Λ`-sum along a line (Rivin,
  `Knot.RivinConcavity.strictConcaveOn_tetVolLine`) applied to the horizontal chord

      t ↦ Λ(α + t) + Λ(β) + Λ(γ − t),      t ∈ (−α, γ)

  with the two endpoints at `t = ∓ε`, `ε = min(α, γ)/2`.  The target sits at `t = 0`, the
  midpoint, so strict concavity gives

      Λα + Λβ + Λγ  >  ½·f(−ε) + ½·f(ε)

  and both `f(∓ε)` are `≥ 0` by `LobMonotonicity.lob_sum_nonneg` — their angle triples are
  positive and still sum to `π`.  Hence `> 0`.

  **What makes it cheap is that the chord never reaches the boundary.**  The obvious route
  runs the chord out to the two degenerate faces, where the `Λ`-sum vanishes *exactly*
  (`LobachevskyMaximum.volChart_eq_zero_of_not_mem`); that needs the exit points
  constructed and shown to lie in `closedSimplex ∖ angleSimplex`, which is fiddly.  Keeping
  both endpoints strictly interior and bounding them below by the *non-strict* lemma
  avoids the boundary entirely — the strictness comes from concavity, not from the
  endpoint values.

  -- Ref: [rivin1994] (concavity of the volume of an ideal hyperbolic polyhedron)
  -- Ref: [milnor1982] §2
-/
import QOU.Archimedean.BlochWignerNonneg
import QOU.Knot.RivinConcavity

namespace QOU.Archimedean.BlochWignerPositive

open Real QOU.Archimedean QOU.MathlibExt QOU.Knot.Rivin

/-- **The ideal-tetrahedron `Λ`-sum is strictly positive.**

Three positive angles summing to `π`.  The strict counterpart of
`LobMonotonicity.lob_sum_nonneg`, and it consumes that lemma rather than strengthening
it — see the module header. -/
theorem lob_sum_pos {α β γ : ℝ} (ha : 0 < α) (hb : 0 < β) (hc : 0 < γ)
    (hsum : α + β + γ = π) : 0 < Lob α + Lob β + Lob γ := by
  set ε : ℝ := min α γ / 2 with hε
  have hεpos : 0 < ε := by
    have : 0 < min α γ := lt_min ha hc
    simpa [hε] using half_pos this
  have hεα : ε < α := by
    have h1 : min α γ ≤ α := min_le_left _ _
    simp only [hε]; linarith
  have hεγ : ε < γ := by
    have h1 : min α γ ≤ γ := min_le_right _ _
    simp only [hε]; linarith
  have hconc := strictConcaveOn_tetVolLine (α := α) (β := β) (γ := γ)
    (u := 1) (v := 0) (w := -1) hsum (by ring) (by norm_num)
  have hmem0 : (-ε) ∈ tetLineDomain α β γ 1 0 (-1) := by
    refine ⟨by simp; linarith, by simpa using hb, by simp; linarith⟩
  have hmem1 : (ε : ℝ) ∈ tetLineDomain α β γ 1 0 (-1) := by
    refine ⟨by simp; linarith, by simpa using hb, by simp; linarith⟩
  have hne : (-ε : ℝ) ≠ ε := by intro h; linarith
  have hchord := hconc.2 hmem0 hmem1 hne (by norm_num : (0:ℝ) < 1/2)
    (by norm_num : (0:ℝ) < 1/2) (by norm_num)
  have hmid : (1/2 : ℝ) • (-ε) + (1/2 : ℝ) • ε = (0:ℝ) := by
    simp only [smul_eq_mul]; ring
  rw [hmid] at hchord
  have h0 : tetVolLine α β γ 1 0 (-1) 0 = Lob α + Lob β + Lob γ := by
    unfold tetVolLine; norm_num
  have hL : 0 ≤ tetVolLine α β γ 1 0 (-1) (-ε) := by
    unfold tetVolLine
    exact LobMonotonicity.lob_sum_nonneg (by simpa using hmem0.1) (by simpa using hmem0.2.1)
      (by simpa using hmem0.2.2) (by ring_nf; linarith)
  have hR : 0 ≤ tetVolLine α β γ 1 0 (-1) ε := by
    unfold tetVolLine
    exact LobMonotonicity.lob_sum_nonneg (by simpa using hmem1.1) (by simpa using hmem1.2.1)
      (by simpa using hmem1.2.2) (by ring_nf; linarith)
  rw [h0] at hchord
  simp only [smul_eq_mul] at hchord
  linarith

/-- **An ideal tetrahedron has strictly positive volume.**

So a nondegenerate ideal tetrahedron is genuinely nondegenerate in volume, not merely
nonnegative — the statement `MathlibExt/ManifoldVolumeBridge.lean` names as the one it
declines to assume. -/
theorem volume_pos (T : IdealTetrahedron) : 0 < T.volume := by
  rw [T.volume_eq_lob_sum]
  exact lob_sum_pos T.angle₁_mem.1 T.angle₂_mem.1 T.angle₃_mem.1 T.angle_sum

/-- **`0 < D(z)` for every `z` in the upper half plane.**

The strict general positivity.  Every such `z` is an `IdealTetrahedron` shape by
construction, so this is `volume_pos` read through Milnor's formula. -/
theorem blochWigner_lob_pos {z : ℂ} (hz : 0 < z.im) : 0 < BlochWigner_lob z :=
  volume_pos (.ofIm z hz)

end QOU.Archimedean.BlochWignerPositive
