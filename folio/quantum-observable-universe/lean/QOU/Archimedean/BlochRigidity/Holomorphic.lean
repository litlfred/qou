import QOU.Archimedean.BlochRigidity.Derivative
import QOU.Archimedean.BlochRigidity.Growth
import QOU.Archimedean.BlochRigidity.Vanishing
import Mathlib.Analysis.NormedSpace.Connected
import Mathlib.LinearAlgebra.Complex.FiniteDimensional

open Complex

namespace QOU.Archimedean.BlochRigidity

/-- Differentiating `φ ∘ f = c • φ` (near `z`, `f` holomorphic) gives `ω(f z)·f' = c·ω(z)`. -/
theorem omega_comp_of_eventuallyEq {φ : ℂ → ℝ} {f : ℂ → ℂ} {f' z : ℂ} {c : ℝ}
    (hφf : DifferentiableAt ℝ φ (f z)) (hφz : DifferentiableAt ℝ φ z) (hf : HasDerivAt f f' z)
    (hev : (fun w => φ (f w)) =ᶠ[nhds z] fun w => c * φ w) :
    omega φ (f z) * f' = c * omega φ z := by
  have h1 := hasFDerivAt_comp_holo hφf hf
  have h2 := (hφz.hasFDerivAt.const_mul c).congr_of_eventuallyEq hev
  have h0 := h1.unique h2
  have key : ∀ v : ℂ, ((omega φ (f z) * f' - c * omega φ z) * v).re = 0 := by
    intro v
    have := congrArg (fun L => L v) h0
    simp only [ContinuousLinearMap.comp_apply, ContinuousLinearMap.coe_restrictScalars',
      ContinuousLinearMap.smulRight_apply, ContinuousLinearMap.one_apply, smul_eq_mul,
      ContinuousLinearMap.smul_apply, fderiv_eq_re] at this
    have e : (omega φ (f z) * f' - c * omega φ z) * v
        = omega φ (f z) * (v * f') - (c : ℂ) * (omega φ z * v) := by ring
    rw [e, sub_re, this, re_ofReal_mul, sub_self]
  apply sub_eq_zero.1
  apply Complex.ext
  · simpa using key 1
  · have := key I
    simp at this ⊢
    linarith

variable {φ : ℂ → ℝ}

/-- Inversion: `ω(z⁻¹) = z² ω(z)`. -/
theorem omega_inv (hφ : ContDiffOn ℝ (⊤ : ℕ∞) φ {0, 1}ᶜ)
    (hinv : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ z⁻¹ = -φ z) {z : ℂ} (hz0 : z ≠ 0) (hz1 : z ≠ 1) :
    omega φ z⁻¹ = z ^ 2 * omega φ z := by
  have hi0 : z⁻¹ ≠ 0 := inv_ne_zero hz0
  have hi1 : z⁻¹ ≠ 1 := by rwa [ne_eq, inv_eq_one]
  have hev : (fun w : ℂ => φ w⁻¹) =ᶠ[nhds z] fun w => (-1 : ℝ) * φ w := by
    filter_upwards [isOpen_U.mem_nhds (mem_U'.2 ⟨hz0, hz1⟩)] with w hw
    obtain ⟨h0, h1⟩ := mem_U'.1 hw
    rw [hinv w h0 h1]; ring
  have := omega_comp_of_eventuallyEq (f := fun w => w⁻¹) (differentiableAt_of_U hφ hi0 hi1)
    (differentiableAt_of_U hφ hz0 hz1) (hasDerivAt_inv hz0) hev
  have hz2 : z ^ 2 ≠ 0 := pow_ne_zero 2 hz0
  push_cast at this
  calc omega φ z⁻¹ = (omega φ z⁻¹ * -(z ^ 2)⁻¹) * (-z ^ 2) := by field_simp
    _ = z ^ 2 * omega φ z := by rw [this]; ring

/-- Reflection: `ω(1 - z) = ω(z)`. -/
theorem omega_one_sub (hφ : ContDiffOn ℝ (⊤ : ℕ∞) φ {0, 1}ᶜ)
    (hone : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ (1 - z) = -φ z) {z : ℂ} (hz0 : z ≠ 0) (hz1 : z ≠ 1) :
    omega φ (1 - z) = omega φ z := by
  have h0 : 1 - z ≠ 0 := sub_ne_zero.2 (Ne.symm hz1)
  have h1 : 1 - z ≠ 1 := by intro h; apply hz0; linear_combination -h
  have hev : (fun w : ℂ => φ (1 - w)) =ᶠ[nhds z] fun w => (-1 : ℝ) * φ w := by
    filter_upwards [isOpen_U.mem_nhds (mem_U'.2 ⟨hz0, hz1⟩)] with w hw
    obtain ⟨h0, h1⟩ := mem_U'.1 hw
    rw [hone w h0 h1]; ring
  have hd : HasDerivAt (fun w : ℂ => 1 - w) (-1) z := by
    simpa using (hasDerivAt_const z (1 : ℂ)).sub (hasDerivAt_id z)
  have := omega_comp_of_eventuallyEq (f := fun w => 1 - w) (differentiableAt_of_U hφ h0 h1)
    (differentiableAt_of_U hφ hz0 hz1) hd hev
  push_cast at this
  linear_combination -this

/-- **Proposition D2.** If `γ` vanishes on `{0,1}ᶜ`, then `ω` is holomorphic there. -/
theorem omega_holo (hφ : ContDiffOn ℝ (⊤ : ℕ∞) φ {0, 1}ᶜ)
    (hγ : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → gamma φ z = 0) :
    DifferentiableOn ℂ (omega φ) {0, 1}ᶜ := by
  intro z hz
  obtain ⟨hz0, hz1⟩ := mem_U'.1 hz
  have hd := differentiableAt_omega hφ hz0 hz1
  refine DifferentiableAt.differentiableWithinAt ?_
  refine (differentiableAt_iff_restrictScalars ℝ hd).2 ⟨((fderiv ℝ (omega φ) z 1
    - I * fderiv ℝ (omega φ) z I) / 2) • ContinuousLinearMap.id ℂ ℂ, ?_⟩
  ext w
  have hg := hγ z hz0 hz1
  simp only [gamma] at hg
  have := rlinear_eq_add_conj (fderiv ℝ (omega φ) z).toLinearMap w
  simp only [ContinuousLinearMap.coe_coe] at this
  simp only [ContinuousLinearMap.coe_restrictScalars', ContinuousLinearMap.coe_smul',
    ContinuousLinearMap.coe_id', Pi.smul_apply, id_eq, smul_eq_mul]
  rw [this, hg, zero_mul, add_zero]

/-- The holomorphic function `F(z) = z (1 - z) ω(z)`. -/
noncomputable def bigF (φ : ℂ → ℝ) (z : ℂ) : ℂ := z * (1 - z) * omega φ z

theorem bigF_one_sub (hφ : ContDiffOn ℝ (⊤ : ℕ∞) φ {0, 1}ᶜ)
    (hone : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ (1 - z) = -φ z) {z : ℂ} (hz0 : z ≠ 0) (hz1 : z ≠ 1) :
    bigF φ (1 - z) = bigF φ z := by
  simp only [bigF, omega_one_sub hφ hone hz0 hz1]; ring

theorem bigF_inv (hφ : ContDiffOn ℝ (⊤ : ℕ∞) φ {0, 1}ᶜ)
    (hinv : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ z⁻¹ = -φ z) {z : ℂ} (hz0 : z ≠ 0) (hz1 : z ≠ 1) :
    bigF φ z⁻¹ * z = -bigF φ z := by
  simp only [bigF, omega_inv hφ hinv hz0 hz1]
  field_simp
  ring

theorem continuousAt_omega (hφ : ContDiffOn ℝ (⊤ : ℕ∞) φ {0, 1}ᶜ) {z : ℂ} (h0 : z ≠ 0)
    (h1 : z ≠ 1) : ContinuousAt (omega φ) z :=
  (differentiableAt_omega hφ h0 h1).continuousAt

/-- **Proposition D3a (growth at `0`).** The five-term relation at `x = 1/10` is a dilation
relation for `Ω(y) = y ω(y)`, so `|y ω(y)| ≤ C/√|y|` near `0`. -/
theorem omega_growth (hφ : ContDiffOn ℝ (⊤ : ℕ∞) φ {0, 1}ᶜ)
    (h5 : ∀ x y : ℂ, x ≠ 0 → x ≠ 1 → y ≠ 0 → y ≠ 1 → x ≠ y →
      φ x - φ y + φ (y / x) - φ ((1 - x⁻¹) / (1 - y⁻¹)) + φ ((1 - x) / (1 - y)) = 0) :
    ∃ r : ℝ, 0 < r ∧ ∃ C : ℝ, ∀ y : ℂ, y ≠ 0 → ‖y‖ ≤ r →
      ‖y * omega φ y‖ * Real.sqrt ‖y‖ ≤ C := by
  set R : ℂ → ℂ := fun y => (1 - 1 / 10) / (1 - y) ^ 2 * omega φ ((1 - 1 / 10) / (1 - y))
    with hRdef
  have hRc : ContinuousAt R 0 := by
    have hc : ContinuousAt (fun y : ℂ => (1 - 1 / 10) / (1 - y)) 0 :=
      continuousAt_const.div (continuousAt_const.sub continuousAt_id) (by norm_num)
    have hω : ContinuousAt (omega φ) ((1 - 1 / 10) / (1 - 0)) :=
      continuousAt_omega hφ (by norm_num) (by norm_num)
    have hcomp : ContinuousAt (fun y : ℂ => omega φ ((1 - 1 / 10) / (1 - y))) 0 :=
      ContinuousAt.comp (f := fun y : ℂ => (1 - 1 / 10) / (1 - y)) hω hc
    show ContinuousAt (fun y : ℂ => (1 - 1 / 10) / (1 - y) ^ 2
      * omega φ ((1 - 1 / 10) / (1 - y))) 0
    exact (continuousAt_const.div ((continuousAt_const.sub continuousAt_id).pow 2)
      (by norm_num)).mul hcomp
  obtain ⟨δ, hδ, hδR⟩ := Metric.continuousAt_iff.1 hRc 1 one_pos
  set r : ℝ := min (1 / 100) (δ / 2) with hr
  have hr0 : 0 < r := lt_min (by norm_num) (by linarith)
  have hr1 : r ≤ 1 / 100 := min_le_left _ _
  have hrδ : r < δ := lt_of_le_of_lt (min_le_right _ _) (by linarith)
  -- `R` bounded
  have hRb : ∀ y : ℂ, y ≠ 0 → ‖y‖ ≤ r → ‖R y‖ ≤ ‖R 0‖ + 1 := by
    intro y _ hy
    have := hδR (x := y) (by rw [dist_zero_right]; linarith)
    rw [dist_eq_norm] at this
    have := norm_sub_norm_le (R y) (R 0)
    linarith
  -- `Ω` bounded on an annulus
  set A : Set ℂ := Metric.closedBall 0 (11 * r) ∩ {w | r ≤ ‖w‖} with hA
  have hAc : IsCompact A :=
    (isCompact_closedBall 0 (11 * r)).inter_right (isClosed_le continuous_const continuous_norm)
  have hAU : ∀ w ∈ A, w ≠ 0 ∧ w ≠ 1 := by
    intro w hw
    obtain ⟨h1, h2⟩ := hw
    simp only [Metric.mem_closedBall, dist_zero_right] at h1
    simp only [Set.mem_setOf_eq] at h2
    refine ⟨fun h => by rw [h, norm_zero] at h2; linarith, fun h => ?_⟩
    rw [h, norm_one] at h1; linarith
  have hΩc : ContinuousOn (fun w => w * omega φ w) A := by
    intro w hw
    obtain ⟨h0, h1⟩ := hAU w hw
    exact (continuousAt_id.mul (continuousAt_omega hφ h0 h1)).continuousWithinAt
  obtain ⟨B, hB⟩ := hAc.exists_bound_of_continuousOn hΩc
  have hrel : ∀ y : ℂ, y ≠ 0 → ‖y‖ ≤ r →
      y * omega φ y = 10 * y * omega φ (10 * y)
        - 9 * y / (1 - y) * omega φ (9 * y / (1 - y)) / (1 - y) + y * R y := by
    intro y hy0 hyr
    have hy1 : y ≠ 1 := by intro h; rw [h, norm_one] at hyr; linarith
    have hyx : (1 / 10 : ℂ) ≠ y := by
      intro h; rw [← h] at hyr; norm_num at hyr; linarith
    have h1y : 1 - y ≠ 0 := sub_ne_zero.2 (Ne.symm hy1)
    have hf := first_identity hφ h5 (x := 1 / 10) (by norm_num) (by norm_num) hy0 hy1 hyx
    have e1 : y / (1 / 10) = 10 * y := by ring
    have e2 : 10 * y * ((1 - 1 / 10) / (1 - y)) = 9 * y / (1 - y) := by ring
    rw [e1] at hf
    rw [e2] at hf
    simp only [hRdef]
    generalize omega φ y = W0 at hf ⊢
    generalize omega φ (10 * y) = W1 at hf ⊢
    generalize omega φ (9 * y / (1 - y)) = W2 at hf ⊢
    generalize omega φ ((1 - 1 / 10) / (1 - y)) = W3 at hf ⊢
    have e3 : ((1 : ℂ) - 1 / 10) / (1 / 10 * (1 - y) ^ 2) = 9 / (1 - y) ^ 2 := by
      field_simp; ring
    rw [e3] at hf
    generalize 1 - y = t at hf ⊢
    linear_combination (-y) * hf
  obtain ⟨C, hC⟩ := growth_sqrt (Ω := fun w => w * omega φ w) hr0 hr1
    (by positivity : (0 : ℝ) ≤ ‖R 0‖ + 1) hrel hRb
    (fun w h1 h2 => hB w ⟨by simpa using h2, h1⟩)
  exact ⟨r, hr0, C, hC⟩

/-- **Proposition D3c.** If the antiholomorphic part `γ` vanishes, then `ω ≡ 0` on `{0,1}ᶜ`. -/
theorem omega_eq_zero (hφ : ContDiffOn ℝ (⊤ : ℕ∞) φ {0, 1}ᶜ)
    (h5 : ∀ x y : ℂ, x ≠ 0 → x ≠ 1 → y ≠ 0 → y ≠ 1 → x ≠ y →
      φ x - φ y + φ (y / x) - φ ((1 - x⁻¹) / (1 - y⁻¹)) + φ ((1 - x) / (1 - y)) = 0)
    (hinv : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ z⁻¹ = -φ z)
    (hone : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ (1 - z) = -φ z)
    (hγ : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → gamma φ z = 0) :
    ∀ z : ℂ, z ≠ 0 → z ≠ 1 → omega φ z = 0 := by
  obtain ⟨r, hr, C, hC⟩ := omega_growth hφ h5
  have hd : DifferentiableOn ℂ (bigF φ) {0, 1}ᶜ := by
    have hp : DifferentiableOn ℂ (fun z : ℂ => z * (1 - z)) {0, 1}ᶜ :=
      (differentiable_id.mul ((differentiable_const (1 : ℂ)).sub differentiable_id)).differentiableOn
    exact hp.mul (omega_holo hφ hγ)
  have hz := eq_zero_of_symm_growth hd (fun z h0 h1 => bigF_one_sub hφ hone h0 h1)
    (fun z h0 h1 => bigF_inv hφ hinv h0 h1) (r := min r 1) (C := 2 * max C 0)
    (lt_min hr one_pos) ?_
  · intro z h0 h1
    have h := hz z h0 h1
    simp only [bigF] at h
    have h1' : (1 - z) ≠ 0 := sub_ne_zero.2 (Ne.symm h1)
    rcases mul_eq_zero.1 h with h | h
    · exact absurd h (mul_ne_zero h0 h1')
    · exact h
  intro z h0 hz
  have hzr : ‖z‖ ≤ r := hz.trans (min_le_left _ _)
  have hz1 : ‖z‖ ≤ 1 := hz.trans (min_le_right _ _)
  have h1z : ‖1 - z‖ ≤ 2 := by
    calc ‖1 - z‖ ≤ ‖(1 : ℂ)‖ + ‖z‖ := norm_sub_le _ _
      _ ≤ 2 := by rw [norm_one]; linarith
  calc ‖bigF φ z‖ * Real.sqrt ‖z‖ = ‖1 - z‖ * (‖z * omega φ z‖ * Real.sqrt ‖z‖) := by
        simp only [bigF, norm_mul]; ring
    _ ≤ 2 * max C 0 := mul_le_mul h1z ((hC z h0 hzr).trans (le_max_left _ _))
        (by positivity) (by norm_num)

/-- **Proposition D3 (closing).** If `γ` vanishes, then `φ ≡ 0` on `{0,1}ᶜ`: `dφ = Re(ω dz) = 0`
on a connected open set, so `φ` is constant, and inversion-oddness makes the constant `0`. -/
theorem eq_zero_of_gamma_eq_zero (hφ : ContDiffOn ℝ (⊤ : ℕ∞) φ {0, 1}ᶜ)
    (h5 : ∀ x y : ℂ, x ≠ 0 → x ≠ 1 → y ≠ 0 → y ≠ 1 → x ≠ y →
      φ x - φ y + φ (y / x) - φ ((1 - x⁻¹) / (1 - y⁻¹)) + φ ((1 - x) / (1 - y)) = 0)
    (hinv : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ z⁻¹ = -φ z)
    (hone : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ (1 - z) = -φ z)
    (hγ : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → gamma φ z = 0) :
    ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ z = 0 := by
  have hω := omega_eq_zero hφ h5 hinv hone hγ
  have hrank : 1 < Module.rank ℝ ℂ := by rw [Complex.rank_real_complex]; norm_num
  have hpc : IsPathConnected ({0, 1}ᶜ : Set ℂ) :=
    (Set.toFinite _).countable.isPathConnected_compl_of_one_lt_rank hrank
  have hfd : ∀ z ∈ ({0, 1}ᶜ : Set ℂ), fderiv ℝ φ z = 0 := by
    intro z hz
    obtain ⟨h0, h1⟩ := mem_U'.1 hz
    refine ContinuousLinearMap.ext fun w => ?_
    rw [fderiv_eq_re, hω z h0 h1]
    simp
  have h2 : (2 : ℂ) ∈ ({0, 1}ᶜ : Set ℂ) := mem_U'.2 ⟨by norm_num, by norm_num⟩
  have hc : ∀ z ∈ ({0, 1}ᶜ : Set ℂ), φ z = φ 2 := fun z hz =>
    isOpen_U.is_const_of_fderiv_eq_zero (𝕜 := ℝ) hpc.isConnected.isPreconnected
      (fun w hw => (differentiableAt_of_U hφ (mem_U'.1 hw).1
        (mem_U'.1 hw).2).differentiableWithinAt) hfd hz h2
  have hi : (2 : ℂ)⁻¹ ∈ ({0, 1}ᶜ : Set ℂ) := mem_U'.2 ⟨by norm_num, by norm_num⟩
  have h22 : φ 2 = 0 := by
    have e1 := hinv 2 (by norm_num) (by norm_num)
    rw [hc _ hi] at e1
    linarith
  intro z h0 h1
  rw [hc z (mem_U'.2 ⟨h0, h1⟩), h22]

end QOU.Archimedean.BlochRigidity
