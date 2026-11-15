import QOU.Archimedean.BlochRigidity.Holomorphic
import QOU.Archimedean.BlochRigidity.Regularity
import QOU.Archimedean.BlochSuslinComplex

/-!
# Rigidity of the five-term relation

Every continuous function on `ℂ ∖ {0,1}` with the Bloch–Wigner symmetries that satisfies Suslin's
five-term relation is a real multiple of any one such function that is not identically zero.

The proof is a dimension count. To each solution `φ` the identity of `gamma_normSq_eq_mul_im`
attaches a real number `k(φ)`, linear in `φ`. A solution with `k = 0` has `γ ≡ 0`, hence vanishes
(`eq_zero_of_gamma_eq_zero`). So the solution space injects into `ℝ` by `k`.
-/

open Complex

namespace QOU.Archimedean.BlochRigidity

variable {φ D : ℂ → ℝ}

/-- `ω` is linear in the function, at a point where both are differentiable. -/
theorem omega_sub_mul {w : ℂ} (c : ℝ) (hφ : DifferentiableAt ℝ φ w)
    (hD : DifferentiableAt ℝ D w) :
    omega (fun v => φ v - c * D v) w = omega φ w - c * omega D w := by
  have h : fderiv ℝ (fun v => φ v - c * D v) w = fderiv ℝ φ w - c • fderiv ℝ D w := by
    rw [fderiv_fun_sub hφ (hD.const_mul c), fderiv_const_mul hD c]
  simp only [omega, h, ContinuousLinearMap.sub_apply, ContinuousLinearMap.smul_apply,
    smul_eq_mul]
  push_cast
  ring

/-- `γ` is linear in the function, on `{0,1}ᶜ`, for smooth functions. -/
theorem gamma_sub_mul (c : ℝ) (hφ : ContDiffOn ℝ (⊤ : ℕ∞) φ {0, 1}ᶜ)
    (hD : ContDiffOn ℝ (⊤ : ℕ∞) D {0, 1}ᶜ) {z : ℂ} (h0 : z ≠ 0) (h1 : z ≠ 1) :
    gamma (fun v => φ v - c * D v) z = gamma φ z - c * gamma D z := by
  have hev : omega (fun v => φ v - c * D v) =ᶠ[nhds z]
      fun v => omega φ v - (c : ℂ) * omega D v := by
    filter_upwards [isOpen_U.mem_nhds (mem_U'.2 ⟨h0, h1⟩)] with v hv
    obtain ⟨v0, v1⟩ := mem_U'.1 hv
    exact omega_sub_mul c (differentiableAt_of_U hφ v0 v1) (differentiableAt_of_U hD v0 v1)
  have hfd : fderiv ℝ (omega (fun v => φ v - c * D v)) z
      = fderiv ℝ (omega φ) z - (c : ℂ) • fderiv ℝ (omega D) z := by
    rw [hev.fderiv_eq, fderiv_fun_sub (differentiableAt_omega hφ h0 h1)
      ((differentiableAt_omega hD h0 h1).const_mul _),
      fderiv_const_mul (differentiableAt_omega hD h0 h1)]
  simp only [gamma, hfd, ContinuousLinearMap.sub_apply, ContinuousLinearMap.smul_apply,
    smul_eq_mul]
  ring

/-- A solution with vanishing constant `k` vanishes. -/
theorem eq_zero_of_k_eq_zero (hφ : ContDiffOn ℝ (⊤ : ℕ∞) φ {0, 1}ᶜ) (hs : BlochSymmetric φ)
    (h5 : SuslinFiveTerm φ)
    (hk : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → (gamma φ z).re * normSq z * normSq (1 - z) = 0) :
    ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ z = 0 := by
  refine eq_zero_of_gamma_eq_zero hφ h5 hs.inv
    (fun z h0 h1 => one_sub_odd hs.inv hs.conj h5 h0 h1) ?_
  intro z h0 h1
  have hN : normSq z * normSq (1 - z) ≠ 0 :=
    mul_ne_zero (normSq_eq_zero.not.2 h0) (normSq_eq_zero.not.2 (sub_ne_zero.2 (Ne.symm h1)))
  have hre : (gamma φ z).re = 0 := by
    have := hk z h0 h1
    rw [mul_assoc] at this
    exact (mul_eq_zero.1 this).resolve_right hN
  exact Complex.ext hre (gamma_im hφ h0 h1)

/-- **Rigidity.** Every continuous, Bloch-symmetric solution of the five-term relation on
`ℂ ∖ {0,1}` is a real multiple of a fixed solution `D` that is not identically zero there. -/
theorem eq_mul_of_fiveTerm (hDc : ContinuousOn D {0, 1}ᶜ) (hDs : BlochSymmetric D)
    (hD5 : SuslinFiveTerm D) {z₀ : ℂ} (hz₀0 : z₀ ≠ 0) (hz₀1 : z₀ ≠ 1) (hDz : D z₀ ≠ 0)
    (hφc : ContinuousOn φ {0, 1}ᶜ) (hφs : BlochSymmetric φ) (hφ5 : SuslinFiveTerm φ) :
    ∃ c : ℝ, ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ z = c * D z := by
  have hDd := contDiffOn_of_fiveTerm hDc hDs.inv hD5
  have hφd := contDiffOn_of_fiveTerm hφc hφs.inv hφ5
  obtain ⟨kD, hkD⟩ := gamma_normSq_eq_mul_im hDd hD5
  obtain ⟨kφ, hkφ⟩ := gamma_normSq_eq_mul_im hφd hφ5
  -- `k(D) ≠ 0`, since `D` does not vanish
  have hkD0 : kD ≠ 0 := by
    intro h
    exact hDz (eq_zero_of_k_eq_zero hDd hDs hD5
      (fun z h0 h1 => by rw [hkD z h0 h1, h, zero_mul]) z₀ hz₀0 hz₀1)
  set c : ℝ := kφ / kD with hc
  set ψ : ℂ → ℝ := fun v => φ v - c * D v with hψ
  have hψc : ContinuousOn ψ {0, 1}ᶜ := hφc.sub (continuousOn_const.mul hDc)
  have hψs : BlochSymmetric ψ :=
    ⟨fun z h0 h1 => by simp only [hψ, hφs.inv z h0 h1, hDs.inv z h0 h1]; ring,
     fun z => by simp only [hψ, hφs.conj z, hDs.conj z]; ring⟩
  have hψ5 : SuslinFiveTerm ψ := by
    intro x y hx0 hx1 hy0 hy1 hxy
    have e1 := hφ5 x y hx0 hx1 hy0 hy1 hxy
    have e2 := hD5 x y hx0 hx1 hy0 hy1 hxy
    simp only [hψ]
    linear_combination e1 - c * e2
  have hψd := contDiffOn_of_fiveTerm hψc hψs.inv hψ5
  obtain ⟨kψ, hkψ⟩ := gamma_normSq_eq_mul_im hψd hψ5
  -- evaluate the three identities at `z = I`
  have hI0 : (I : ℂ) ≠ 0 := I_ne_zero
  have hI1 : (I : ℂ) ≠ 1 := by intro h; have := congrArg Complex.im h; simp at this
  have hlin := gamma_sub_mul c hφd hDd hI0 hI1
  have hkψ0 : kψ = 0 := by
    have a := hkψ I hI0 hI1
    have b := hkφ I hI0 hI1
    have d := hkD I hI0 hI1
    rw [show (fun v => φ v - c * D v) = ψ from rfl] at hlin
    rw [hlin] at a
    simp only [sub_re, re_ofReal_mul, I_im, mul_one] at a b d
    have hc' : c * kD = kφ := by rw [hc]; field_simp
    linear_combination -a + b - c * d - hc'
  refine ⟨c, fun z h0 h1 => ?_⟩
  have := eq_zero_of_k_eq_zero hψd hψs hψ5
    (fun z h0 h1 => by rw [hkψ z h0 h1, hkψ0, zero_mul]) z h0 h1
  simp only [hψ] at this
  linarith

end QOU.Archimedean.BlochRigidity
