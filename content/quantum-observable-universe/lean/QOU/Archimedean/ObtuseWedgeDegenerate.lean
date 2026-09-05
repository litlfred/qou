/-
  `wedgeAt` is acute-ONLY by construction — the obtuse case cannot be obtained
  by substituting an obtuse half-angle (bean `qou-w3eg`, H4-5).

  WHY THIS FILE EXISTS.  The obtuse case of Milnor's identity needs a
  replacement for the wedge subtending the obtuse angle, and the tempting move
  is to reuse `wedgeAt R θ ψ` at `ψ > π/2` and let the geometry supply Milnor's
  minus sign.  **That does not work, and this file proves why** — so that a
  later agent does not spend a session discovering it.

  `wedgeAt R θ ψ` is
  `{w | ⟨w,u_θ⟩ < R cos ψ ∧ |⟨w,v_θ⟩| < ⟨w,u_θ⟩ · tan ψ}`
  (`OrthoschemeRotation.lean`), whose docstring calls it "the open isoceles
  triangle with apex at the circumcentre, apex angle `2ψ`".  For `ψ ∈ (π/2, π)`
  we have `tan ψ < 0`, and since `|⟨w,v_θ⟩| ≥ 0` the second conjunct forces
  `⟨w,u_θ⟩ < 0`: every point of the set lies **strictly on the far side of the
  circumcentre**, so the set opens away from the apex rather than towards it.
  Together with `⟨w,u_θ⟩ < R cos ψ < 0` (unbounded below) it is not a triangle
  at all.

  So the acuteness hypotheses carried throughout the wedge machinery
  (`hypVolume_chimney_wedgeAt`, `disjoint_wedgeAt_adjacent`, the tiling) are
  **structural, not technical** — they are what make `wedgeAt` denote the object
  its name claims.

  WHAT THE OBTUSE CASE ACTUALLY NEEDS instead: the wedge in the OPPOSITE
  direction with the ACUTE half-angle `π − γ = α + β`, SUBTRACTED —

      inscribedTriangle R t α β γ
        =ᵐ (wedgeAt R (t+2γ+α) α ∪ wedgeAt R (t+2γ+2α+β) β)
             \ wedgeAt R (t+γ+π) (π−γ)

  every half-angle on the right being acute when `γ` is obtuse, which is the
  set-level counterpart of `IdealTetObtuseReduction.lob_sum_eq_reflected`.  That
  identity is measured (zero mismatches over ~117k grid points,
  `computations/milnor_obtuse_wedge_decomposition_probe.py`) and is **not**
  proved here.

  Nothing in this file asserts anything about a volume.

  Archimedean (ℝ): `Real.tan`, `Real.pi`, ordering — §7c.

  -- Ref: [milnor1982] https://doi.org/10.1090/S0273-0979-1982-14958-8
  -- Ref: [manuscript] bean qou-w3eg (H4-5 obtuse)
-/
import QOU.Archimedean.OrthoschemeRotation

namespace QOU.Archimedean.HyperbolicVolume

open Real Set
open QOU.Archimedean

/-- **`tan` is negative on `(π/2, π)`** — `sin > 0` and `cos < 0` there.
Mathlib names the `(-π/2, 0)` case (`Real.tan_neg_of_neg_of_pi_div_two_lt`) but
not this one. -/
theorem tan_neg_of_pi_div_two_lt_of_lt_pi {ψ : ℝ} (h1 : π / 2 < ψ) (h2 : ψ < π) :
    Real.tan ψ < 0 := by
  rw [Real.tan_eq_sin_div_cos]
  exact div_neg_of_pos_of_neg
    (Real.sin_pos_of_pos_of_lt_pi (by linarith [Real.pi_pos]) h2)
    (Real.cos_neg_of_pi_div_two_lt_of_lt h1 (by linarith [Real.pi_pos]))

/-- **At an obtuse half-angle the wedge lies strictly on the FAR side of the
apex.**  The defining inequality `|⟨w,v⟩| < ⟨w,u⟩ · tan ψ` has a non-negative
left side, so it forces `⟨w,u⟩ · tan ψ > 0`; with `tan ψ < 0` that gives
`⟨w,u⟩ < 0`.

This is the precise sense in which `wedgeAt` is acute-only: at `ψ > π/2` it does
not degenerate to something smaller, it moves to the other side of the
circumcentre. -/
theorem wedgeAt_inner_neg_of_obtuse {R θ ψ : ℝ} (h1 : π / 2 < ψ) (h2 : ψ < π)
    {w : ℝ × ℝ} (hw : w ∈ wedgeAt R θ ψ) :
    w.1 * Real.cos θ + w.2 * Real.sin θ < 0 := by
  obtain ⟨-, hside⟩ := hw
  have habs : (0 : ℝ) ≤ |(-(w.1 * Real.sin θ) + w.2 * Real.cos θ)| := abs_nonneg _
  have hprod : 0 < (w.1 * Real.cos θ + w.2 * Real.sin θ) * Real.tan ψ :=
    lt_of_le_of_lt habs hside
  have htan : Real.tan ψ < 0 := tan_neg_of_pi_div_two_lt_of_lt_pi h1 h2
  by_contra hcon
  push_neg at hcon
  nlinarith [hprod, htan, hcon]

/-- **The obtuse wedge is disjoint from the closed near half-plane** — the
containment form of the lemma above.  In particular it contains no point of the
ray from the circumcentre in the direction `θ` its name refers to. -/
theorem wedgeAt_subset_far_halfplane_of_obtuse {R θ ψ : ℝ}
    (h1 : π / 2 < ψ) (h2 : ψ < π) :
    wedgeAt R θ ψ ⊆ {w : ℝ × ℝ | w.1 * Real.cos θ + w.2 * Real.sin θ < 0} :=
  fun _ hw => wedgeAt_inner_neg_of_obtuse h1 h2 hw

/-- **The apex itself is not in the obtuse wedge.**  A sanity corollary: the
circumcentre lies in `wedgeAt R θ ψ` for no obtuse `ψ`, whereas for acute `ψ`
the wedge is the isoceles triangle *with apex there*. -/
theorem origin_notMem_wedgeAt_of_obtuse {R θ ψ : ℝ} (h1 : π / 2 < ψ) (h2 : ψ < π) :
    ((0 : ℝ), (0 : ℝ)) ∉ wedgeAt R θ ψ := by
  intro hmem
  have := wedgeAt_inner_neg_of_obtuse h1 h2 hmem
  simp at this

end QOU.Archimedean.HyperbolicVolume
