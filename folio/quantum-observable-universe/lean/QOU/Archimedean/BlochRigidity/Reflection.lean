import QOU.Archimedean.BlochRigidity.Instance

/-!
# Reflection oddness of the Bloch–Wigner function

`D(1 − z) = −D(z)`. The argument is the one used for `blochD_conj`: the sum
`D(1 − w) + D(w)` has zero derivative on the connected set `ℂ ∖ {0,1}`, because the
derivative kernel `cD` is invariant under `w ↦ 1 − w`, and the sum vanishes at `w = 2`
(both arguments are real).
-/

open Complex

namespace QOU.Archimedean.FiveTermProof

/-- The derivative kernel is symmetric under `z ↦ 1 − z`. -/
theorem cD_one_sub (z : ℂ) : cD (1 - z) = cD z := by
  unfold cD
  rw [show (1 : ℂ) - (1 - z) = z by ring]
  ring

/-- **Reflection.** `D(1 − z) = −D(z)` on all of `ℂ`. -/
theorem blochD_one_sub (z : ℂ) : blochD (1 - z) = -blochD z := by
  set ψ : ℂ → ℝ := fun w => blochD (1 - w) + blochD w with hψ
  have hmem : ∀ {w : ℂ}, w ∈ ({0, 1}ᶜ : Set ℂ) ↔ w ≠ 0 ∧ w ≠ 1 := by simp
  have hd : ∀ w ∈ ({0, 1}ᶜ : Set ℂ), HasFDerivAt ψ (0 : ℂ →L[ℝ] ℝ) w := by
    intro w hw
    obtain ⟨h0, h1⟩ := hmem.1 hw
    have c0 : (1 : ℂ) - w ≠ 0 := sub_ne_zero.2 (Ne.symm h1)
    have c1 : (1 : ℂ) - w ≠ 1 := by
      intro h; apply h0; linear_combination -h
    have hg : HasDerivAt (fun w : ℂ => 1 - w) (-1) w := by
      simpa using (hasDerivAt_id w).const_sub (1 : ℂ)
    have hc := hasFDerivAt_comp_of_hasDerivAt (hasFDerivAt_blochD c0 c1) hg
    have h := hc.add (hasFDerivAt_blochD h0 h1)
    convert h using 1
    ext v
    simp only [ContinuousLinearMap.zero_apply, ContinuousLinearMap.add_apply,
      ContinuousLinearMap.coe_comp', Function.comp_apply, DLin_apply,
      ContinuousLinearMap.mul_apply', Complex.imCLM_apply, cD_one_sub]
    rw [show cD w * -1 * v = -(cD w * v) by ring, Complex.neg_im]
    ring
  have hrank : 1 < Module.rank ℝ ℂ := by rw [Complex.rank_real_complex]; norm_num
  have hpc : IsPathConnected ({0, 1}ᶜ : Set ℂ) :=
    (Set.toFinite _).countable.isPathConnected_compl_of_one_lt_rank hrank
  have hopen : IsOpen ({0, 1}ᶜ : Set ℂ) := (Set.toFinite _).isClosed.isOpen_compl
  have h2 : (2 : ℂ) ∈ ({0, 1}ᶜ : Set ℂ) := hmem.2 ⟨by norm_num, by norm_num⟩
  have hreal : ∀ r : ℝ, ψ r = 0 := fun r => by
    simp only [hψ]
    rw [show (1 : ℂ) - (r : ℂ) = ((1 - r : ℝ) : ℂ) by push_cast; ring,
      blochD_ofReal, blochD_ofReal]; ring
  have hz : ψ z = 0 := by
    by_cases hU : z ∈ ({0, 1}ᶜ : Set ℂ)
    · rw [hopen.is_const_of_fderiv_eq_zero (𝕜 := ℝ) hpc.isConnected.isPreconnected
        (fun w hw => (hd w hw).differentiableAt.differentiableWithinAt)
        (fun w hw => (hd w hw).fderiv) hU h2]
      simpa using hreal 2
    · have : z = 0 ∨ z = 1 := by
        by_contra hc; push_neg at hc; exact hU (hmem.2 hc)
      rcases this with rfl | rfl
      · simpa using hreal 0
      · simpa using hreal 1
  simp only [hψ] at hz
  linarith

end QOU.Archimedean.FiveTermProof
