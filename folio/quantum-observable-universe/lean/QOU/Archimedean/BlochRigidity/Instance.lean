import QOU.Archimedean.BlochRigidity.Rigidity
import QOU.Archimedean.BlochWignerFiveTermInstance
import QOU.Archimedean.BlochWignerPositive

/-!
# The rigidity instance for the Bloch–Wigner function

`FiveTermProof.blochD` is continuous on `ℂ ∖ {0,1}`, has the two Bloch–Wigner symmetries, satisfies
the five-term relation and is positive at `i`. By `eq_mul_of_fiveTerm` it therefore spans the
solution space, which is the content of `BlochSuslinRigidity`.
-/

open Complex

namespace QOU.Archimedean.FiveTermProof

theorem continuousOn_blochD : ContinuousOn blochD {0, 1}ᶜ := fun z hz => by
  have h : z ≠ 0 ∧ z ≠ 1 := by simpa using hz
  exact (hasFDerivAt_blochD h.1 h.2).continuousAt.continuousWithinAt

theorem blochD_of_im_ne_zero {z : ℂ} (h : z.im ≠ 0) : blochD z = DNZ z := by
  have : ¬ (z.im = 0 ∧ 1 < z.re) := fun h' => h h'.1
  simp [blochD, this]

/-- **Inversion.** `D(1/z) = −D(z)`. -/
theorem blochD_inv {z : ℂ} : blochD z⁻¹ = -blochD z := by
  by_cases h : z.im = 0
  · have hz : z = (z.re : ℂ) := Complex.ext (by simp) (by simp [h])
    rw [hz, ← ofReal_inv, blochD_ofReal, blochD_ofReal, neg_zero]
  · have hi : z⁻¹.im ≠ 0 := by
      rw [inv_im]
      have : normSq z ≠ 0 := normSq_eq_zero.not.2 (fun h0 => h (by rw [h0]; simp))
      exact div_ne_zero (neg_ne_zero.2 h) this
    rw [blochD_of_im_ne_zero hi, blochD_of_im_ne_zero h, DNZ_inv h]

theorem cD_conj (z : ℂ) : cD ((starRingEnd ℂ) z) = (starRingEnd ℂ) (cD z) := by
  have h1 : ‖(1 : ℂ) - (starRingEnd ℂ) z‖ = ‖1 - z‖ := by
    rw [show (1 : ℂ) - (starRingEnd ℂ) z = (starRingEnd ℂ) (1 - z) by simp, Complex.norm_conj]
  unfold cD
  rw [Complex.norm_conj, h1]
  simp [map_div₀, map_sub, map_neg, conj_ofReal]

/-- **Conjugation.** `D(z̄) = −D(z)`: the sum `D(z̄) + D(z)` has zero derivative on the connected
set `ℂ ∖ {0,1}` and vanishes on the real axis. -/
theorem blochD_conj (z : ℂ) : blochD ((starRingEnd ℂ) z) = -blochD z := by
  set ψ : ℂ → ℝ := fun w => blochD ((starRingEnd ℂ) w) + blochD w with hψ
  have hmem : ∀ {w : ℂ}, w ∈ ({0, 1}ᶜ : Set ℂ) ↔ w ≠ 0 ∧ w ≠ 1 := by simp
  have hd : ∀ w ∈ ({0, 1}ᶜ : Set ℂ), HasFDerivAt ψ (0 : ℂ →L[ℝ] ℝ) w := by
    intro w hw
    obtain ⟨h0, h1⟩ := hmem.1 hw
    have c0 : (starRingEnd ℂ) w ≠ 0 := (map_ne_zero _).2 h0
    have c1 : (starRingEnd ℂ) w ≠ 1 := by
      intro h; apply h1; rw [← (starRingEnd ℂ).injective.eq_iff, h, map_one]
    have hc := (hasFDerivAt_blochD c0 c1).comp w conjCLE.toContinuousLinearMap.hasFDerivAt
    have h := hc.add (hasFDerivAt_blochD h0 h1)
    convert h using 1
    ext v
    simp only [ContinuousLinearMap.zero_apply, ContinuousLinearMap.add_apply,
      ContinuousLinearMap.coe_comp', Function.comp_apply, DLin_apply]
    rw [show (conjCLE.toContinuousLinearMap : ℂ →L[ℝ] ℂ) v = (starRingEnd ℂ) v from rfl,
      cD_conj, ← map_mul, conj_im]
    ring
  have hrank : 1 < Module.rank ℝ ℂ := by rw [Complex.rank_real_complex]; norm_num
  have hpc : IsPathConnected ({0, 1}ᶜ : Set ℂ) :=
    (Set.toFinite _).countable.isPathConnected_compl_of_one_lt_rank hrank
  have hopen : IsOpen ({0, 1}ᶜ : Set ℂ) := (Set.toFinite _).isClosed.isOpen_compl
  have h2 : (2 : ℂ) ∈ ({0, 1}ᶜ : Set ℂ) := hmem.2 ⟨by norm_num, by norm_num⟩
  have hψ2 : ψ 2 = 0 := by
    simp only [hψ]
    rw [show (2 : ℂ) = ((2 : ℝ) : ℂ) by norm_num, conj_ofReal, blochD_ofReal]; ring
  have hz : ψ z = 0 := by
    by_cases hU : z ∈ ({0, 1}ᶜ : Set ℂ)
    · rw [hopen.is_const_of_fderiv_eq_zero (𝕜 := ℝ) hpc.isConnected.isPreconnected
        (fun w hw => (hd w hw).differentiableAt.differentiableWithinAt)
        (fun w hw => (hd w hw).fderiv) hU h2, hψ2]
    · have : z = 0 ∨ z = 1 := by
        by_contra hc; push_neg at hc; exact hU (hmem.2 hc)
      rcases this with rfl | rfl
      · simp only [hψ, map_zero]
        rw [show (0 : ℂ) = ((0 : ℝ) : ℂ) by norm_num, blochD_ofReal]; ring
      · simp only [hψ, map_one]
        rw [show (1 : ℂ) = ((1 : ℝ) : ℂ) by norm_num, blochD_ofReal]; ring
  simp only [hψ] at hz
  linarith

theorem blochSymmetric_blochD : BlochSymmetric blochD :=
  ⟨fun _ _ _ => blochD_inv, blochD_conj⟩

theorem blochD_I_pos : 0 < blochD I := by
  rw [blochD_eq_lob (by simp)]
  exact QOU.Archimedean.BlochWignerPositive.blochWigner_lob_pos (by simp)

end QOU.Archimedean.FiveTermProof

namespace QOU.Archimedean

/-- **Bloch–Suslin rigidity for `D`, proved.** -/
instance blochSuslinRigidity_blochD : BlochSuslinRigidity FiveTermProof.blochD :=
  ⟨fun _ hφc hφs hφ5 => BlochRigidity.eq_mul_of_fiveTerm FiveTermProof.continuousOn_blochD
    FiveTermProof.blochSymmetric_blochD blochWignerFiveTerm_blochD.five_term I_ne_zero
    (by intro h; have := congrArg Complex.im h; simp at this)
    FiveTermProof.blochD_I_pos.ne' hφc hφs hφ5⟩

end QOU.Archimedean

