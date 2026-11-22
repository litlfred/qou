/-
  The van der Veen Step-4 Gaussian: `2^{−n/2}·(2/A)^{1/2}` — bean `qou-mlgp` (D).

  WHAT THIS IS.  The multivariate Gaussian with COMPLEX covariance that produces
  the one-loop constant on the LINK side.  `qou-vdvS` established

      Q_∞ = ψ · ∫_{ℝ^{n+1}} exp(−π[ A u²/2 + 2 Σ_{j=1}^{n} (v_j + u/2)² ]) du dv
          = ψ · 2^{−n/2} · (2/A)^{1/2},        A = n − mi,  n = c+d,  m = 4a−c+d

  and from it `c_σ(W_{a,1,c,d}) = 2^{1/2−n}(n²+m²)^{−1/4}`.  Everything else on
  that arc — `vdv_c_sigma_iff_tau`, `vdv_tau_sq`, `vdv_radical_is_gaussian_norm`
  in `QOU/OneLoopPrefactorInvariance.lean` — is algebra downstream of this one
  integral, and until now the integral itself was a hypothesis.

  WHY IT IS ELEMENTARY FOR EVERY `n`, WHICH IS THE POINT.  As PUBLISHED the
  quadratic form carries absolute values (van der Veen's Lemma 2a states the
  Taylor expansion in distances `n′ = |n − ⌊N/2⌋|`, `k′ = |k − ⌊N/4⌋|`), which
  turns Step 4 into an integral over an ORTHANT and produces `erfc` factors that
  only close in low rank.  Restoring the signs — the expansion
  `f(π/2+x, π/4+y) = f(π/2,π/4) − (x² + 2xy + 2y²) + O(|x|³+|y|³)` is signed,
  and `2xy < 0` when `x, y` have opposite signs — puts the integral back over
  all of `ℝ^{n+1}`, where it factorises completely:

    * each `v_j` integral is a COMPLETE Gaussian `∫ e^{−2π(v+s)²} dv = 2^{−1/2}`,
      independent of the shift `s` and hence of `u`.  That is the whole reason
      the `u`-integral survives as a one-dimensional problem;
    * the `u` integral is `∫ e^{−πAu²/2} du = (2/A)^{1/2}`, a complex-covariance
      Gaussian, legitimate because `Re A = c+d ≥ 1 > 0`.

  See `docs/outreach/2026-08-08-van-der-veen-whitehead-chains-corrections.md`
  §1 for the numerical evidence that the signed form is the correct one.

  WHAT IS PROVED HERE AND WHAT IS NOT.  The statement below is the ITERATED
  integral `∫_ℝ du (∫_{ℝ^n} dv …)`, which is what "do the `v`-integrals first"
  means and is the form the derivation actually uses.  Identifying it with the
  Bochner integral over `ℝ^{n+1}` is Fubini and needs joint integrability on the
  product measure; that is NOT included, and the header of the downstream
  theorem should not claim it.

  MATHLIB SUPPLIES BOTH ANALYTIC INPUTS, so this is assembly, not analysis:
  `integral_gaussian_complex` (the complex-covariance Gaussian, `0 < re b`) and
  `integral_fintype_prod_volume_eq_pow` (`∫_{ι→E} ∏ f(x i) = (∫ f)^{card ι}`).

  -- Ref: [leitner2026] QOU/OneLoopPrefactorInvariance.lean  (what consumes this)
  -- Ref: [leitner2026] QOU/MathlibExt/GaussianThetaSum.lean (the (B) companion)
  -- Ref: [leitner2026] computations/probes/one_loop_vdv_constant_closed_form_probe.py
-/
import Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral
import Mathlib.MeasureTheory.Integral.Pi

namespace QOU.MathlibExt

open Complex Real MeasureTheory

/-- **`∫_ℝ e^{−2π(v+s)²} dv = 2^{−1/2}`**, for every real shift `s`.

The complete Gaussian at covariance `2π` is `2^{−1/2}` and translation does not
move it.  Independence of `s` is the structural fact behind the `v`-integrals in
Step 4: it is why the `n` transverse directions contribute a bare `2^{−n/2}` and
leave the `u`-integral untouched. -/
theorem integral_cexp_two_pi_sq_shift (s : ℝ) :
    ∫ v : ℝ, Complex.exp (-(2 * (π : ℂ)) * ((v : ℂ) + (s : ℂ)) ^ 2)
      = (((Real.sqrt 2)⁻¹ : ℝ) : ℂ) := by
  have hshift : (fun v : ℝ => Complex.exp (-(2 * (π : ℂ)) * ((v : ℂ) + (s : ℂ)) ^ 2))
      = fun v : ℝ =>
        (fun w : ℝ => Complex.exp (-(2 * (π : ℂ)) * (w : ℂ) ^ 2)) (v + s) := by
    funext v; push_cast; ring_nf
  rw [hshift, integral_add_right_eq_self
    (fun w : ℝ => Complex.exp (-(2 * (π : ℂ)) * (w : ℂ) ^ 2)) s]
  have hb : (0 : ℝ) < (2 * (π : ℂ)).re := by
    simp [Complex.mul_re]
    positivity
  rw [integral_gaussian_complex hb]
  have hval : ((π : ℂ)) / (2 * (π : ℂ)) = ((1 / 2 : ℝ) : ℂ) := by
    have hπ : (π : ℂ) ≠ 0 := by simp [Real.pi_ne_zero]
    push_cast
    field_simp
  rw [hval, show ((1 : ℂ) / 2) = (((1 / 2 : ℝ) : ℝ) : ℂ) by norm_num,
    ← Complex.ofReal_cpow (by norm_num : (0:ℝ) ≤ 1 / 2)]
  congr 1
  rw [← Real.sqrt_eq_rpow, show (1 / 2 : ℝ) = (2 : ℝ)⁻¹ by norm_num, Real.sqrt_inv]

/-- **`∫_ℝ e^{−πAu²/2} du = (2/A)^{1/2}`** for any complex `A` with `Re A > 0`.

`Re A = c+d ≥ 1` on the Whitehead chains, so the hypothesis is never binding
there; it is exactly the condition that makes the Gaussian converge. -/
theorem integral_cexp_neg_pi_mul_div_two {A : ℂ} (hA : 0 < A.re) :
    ∫ u : ℝ, Complex.exp (-((π : ℂ) * A / 2) * (u : ℂ) ^ 2)
      = (2 / A) ^ ((1 : ℂ) / 2) := by
  have hb : (0 : ℝ) < ((π : ℂ) * A / 2).re := by
    simp only [Complex.div_re, Complex.mul_re, Complex.ofReal_re, Complex.ofReal_im,
      Complex.normSq_apply]
    norm_num
    positivity
  rw [integral_gaussian_complex hb]
  congr 1
  have hπ : (π : ℂ) ≠ 0 := by simp [Real.pi_ne_zero]
  have hAne : A ≠ 0 := by
    intro h; rw [h] at hA; simp at hA
  field_simp

/-- **The Step-4 Gaussian: `2^{−n/2}·(2/A)^{1/2}`**, for every `n` and every
complex `A` with `Re A > 0`.

Stated as the iterated integral (`v` first, then `u`) — see the file header on
what that does and does not claim.  Note there is no rank restriction and no
`erfc`: with the signs of the Taylor expansion restored, the transverse
integrals are complete Gaussians and the whole thing is elementary. -/
theorem integral_vdv_step4 (n : ℕ) {A : ℂ} (hA : 0 < A.re) :
    (∫ u : ℝ, ∫ v : Fin n → ℝ,
        Complex.exp (-(π : ℂ) *
          (A * (u : ℂ) ^ 2 / 2 + 2 * ∑ j, ((v j : ℂ) + (u : ℂ) / 2) ^ 2)))
      = (((Real.sqrt 2)⁻¹ : ℝ) : ℂ) ^ n * (2 / A) ^ ((1 : ℂ) / 2) := by
  have hinner : ∀ u : ℝ,
      (∫ v : Fin n → ℝ, Complex.exp (-(π : ℂ) *
          (A * (u : ℂ) ^ 2 / 2 + 2 * ∑ j, ((v j : ℂ) + (u : ℂ) / 2) ^ 2)))
        = Complex.exp (-((π : ℂ) * A / 2) * (u : ℂ) ^ 2)
            * (((Real.sqrt 2)⁻¹ : ℝ) : ℂ) ^ n := by
    intro u
    have hfac : ∀ v : Fin n → ℝ,
        Complex.exp (-(π : ℂ) *
            (A * (u : ℂ) ^ 2 / 2 + 2 * ∑ j, ((v j : ℂ) + (u : ℂ) / 2) ^ 2))
          = Complex.exp (-((π : ℂ) * A / 2) * (u : ℂ) ^ 2) *
              ∏ j, Complex.exp (-(2 * (π : ℂ)) * ((v j : ℂ) + ((u / 2 : ℝ) : ℂ)) ^ 2) := by
      intro v
      rw [← Complex.exp_sum, ← Complex.exp_add]
      congr 1
      push_cast
      rw [← Finset.mul_sum]
      ring
    simp_rw [hfac]
    rw [integral_const_mul]
    congr 1
    rw [integral_fintype_prod_volume_eq_pow (fun w : ℝ =>
      Complex.exp (-(2 * (π : ℂ)) * ((w : ℂ) + ((u / 2 : ℝ) : ℂ)) ^ 2))]
    rw [integral_cexp_two_pi_sq_shift (u / 2)]
    simp
  simp_rw [hinner]
  rw [integral_mul_const, integral_cexp_neg_pi_mul_div_two hA, mul_comm]

end QOU.MathlibExt
