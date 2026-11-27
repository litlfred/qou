/-
# The 5₂ sum-rule integrand: the logarithm and the integral

Analytic half of `QOU.Nuclear.FiveTwoSumRuleIntegrand`, split off on the
transcendental boundary (epic `qou-dk7p`, strangler onto `[Coev E]`). The
algebraic and positivity skeleton (Vieta, `recipCubic_eq`, `recipCubic_pos`,
`1/2 ≤ P ≤ 1`, the disc `−23` resolvent) stays in that module; this file holds
what needs `Real.log`, `Complex.log`, interval integrals and `cLiTwoExt`:

* `abs_log_recipCubic_le` — `|log P(z)| ≤ 4z` on `[0,1]`;
* `intervalIntegrable_log_recipCubic_div` — Route 5's integral converges;
* `sum_re_log_one_sub_eq_log_recipCubic` — `Σⱼ Re Log(1 − yⱼz) = log P(z)`;
* `sum_re_cLiTwoExt_eq_integral` — `Σⱼ Re cLiTwoExt(yⱼ) = −∫₀¹ log P(z)/z dz`.

Declaration names and namespace are unchanged by the split.

-- Ref: [leitner2026] bean qou-0yqu Route 5; docs/coordination/1ppq-qbeta.md
-/
import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import QOU.Transcendental.QCalculus.ComplexDilogarithm
import QOU.Nuclear.FiveTwoSumRuleIntegrand

namespace QOU.QBeta.FiveTwo

open Complex

/-- **The integrand's numerator vanishes linearly at `0`**: `|log P(z)| ≤ 4z`
on `[0,1]`.

This is what removes the apparent singularity of `log P(z)/z` at the left
endpoint of Route 5's integral. -/
theorem abs_log_recipCubic_le {z : ℝ} (h0 : 0 ≤ z) (h1 : z ≤ 1) :
    |Real.log (1 - 2 * z + 3 * z ^ 2 - z ^ 3)| ≤ 4 * z := by
  have hpos : 0 < 1 - 2 * z + 3 * z ^ 2 - z ^ 3 := recipCubic_pos h0 h1
  have hle : 1 - 2 * z + 3 * z ^ 2 - z ^ 3 ≤ 1 := recipCubic_le_one h0 h1
  have hhalf : 1 / 2 ≤ 1 - 2 * z + 3 * z ^ 2 - z ^ 3 := recipCubic_ge_half h0 h1
  rw [abs_le]
  constructor
  · -- lower: `log P ≥ 1 − 1/P ≥ −4z`
    refine le_trans ?_ (Real.one_sub_inv_le_log_of_pos hpos)
    have hid : (1 : ℝ) - (1 - 2 * z + 3 * z ^ 2 - z ^ 3)⁻¹
        = ((1 - 2 * z + 3 * z ^ 2 - z ^ 3) - 1) / (1 - 2 * z + 3 * z ^ 2 - z ^ 3) := by
      rw [sub_div, div_self hpos.ne', one_div]
    rw [hid, le_div_iff₀ hpos]
    nlinarith [mul_nonneg h0 (sub_nonneg.2 h1), sq_nonneg z, sq_nonneg (z - 1 / 2),
      mul_nonneg (mul_nonneg h0 h0) (sub_nonneg.2 h1)]
  · -- upper: `log P ≤ P − 1 ≤ 0 ≤ 4z`
    refine le_trans (Real.log_le_sub_one_of_pos hpos) ?_
    nlinarith [mul_nonneg (mul_nonneg h0 (sub_nonneg.2 h1)) (by linarith : (0 : ℝ) ≤ 2 - z)]

/-- **Route 5's integral converges.**

`|log P(z)/z| ≤ 4` on `(0,1]`, immediately from `abs_log_recipCubic_le`, so the
integrand is a bounded measurable function on a set of finite measure. This is
what makes `−∫₀¹ log(1 − 2z + 3z² − z³)/z dz` a well-defined real number, and
hence what makes Route 5 a statement rather than a formal expression.

Contrast the series side: `Σₙ pₙ/n²` **diverges** (`|y₁| = 1.52 > 1`). The
restatement's whole value is that it moves the identity to a place where
convergence is elementary. -/
theorem intervalIntegrable_log_recipCubic_div :
    IntervalIntegrable (fun z : ℝ => Real.log (1 - 2 * z + 3 * z ^ 2 - z ^ 3) / z)
      MeasureTheory.volume 0 1 := by
  rw [intervalIntegrable_iff, Set.uIoc_of_le (by norm_num : (0 : ℝ) ≤ 1)]
  refine MeasureTheory.Measure.integrableOn_of_bounded (M := 4) (by simp) ?_ ?_
  · exact ((Real.measurable_log.comp (by fun_prop)).div measurable_id).aestronglyMeasurable
  · refine (MeasureTheory.ae_restrict_iff' measurableSet_Ioc).2
      (Filter.Eventually.of_forall fun z hz => ?_)
    have h0 : 0 < z := hz.1
    have h1 : z ≤ 1 := hz.2
    rw [Real.norm_eq_abs, abs_div, abs_of_pos h0, div_le_iff₀ h0]
    have hb := abs_log_recipCubic_le h0.le h1
    linarith

/-! ### The integrand identity: `Σⱼ Re Log(1 − yⱼz) = log P(z)` on `[0,1]`

This is the pointwise half of the one link still separating Route 5 from the
sum rule, namely

    Σⱼ Re Li₂(yⱼ) = −∫₀¹ log P(z)/z dz.

The other half is the complex integral representation
`Li₂(y) = −∫₀¹ Log(1 − yz)/z dz`, which for `|y| > 1` *is* the analytic
continuation (the integral converges for any `y ∉ [1,∞)` regardless of `|y|`,
unlike the series). That half is still open — see bean `qou-gkco`.

The pointwise identity below needs no dilogarithm and no continuation. It works
because the **real part** of a complex log is a genuine norm-log, and norms
multiply:

    Σⱼ Re Log(1 − yⱼz) = Σⱼ log‖1 − yⱼz‖ = log ∏ⱼ‖1 − yⱼz‖
                       = log‖∏ⱼ(1 − yⱼz)‖ = log|P(z)| = log P(z)

the last step by `recipCubic_pos`. **No `2πik` correction appears anywhere** —
taking real parts discards exactly the branch ambiguity. (Probe
`qbeta_5two_route5_branch_data_probe` gate G1 saw this numerically: the
correction is identically zero, `3.1e-61` over 40 sample points. It is not a
numerical accident; it is what this proof says.) -/

/-- **`Σⱼ Re Log(1 − yⱼz) = log P(z)` for `z ∈ [0,1]`.**

Real parts, so no branch data enters. `y₁, y₂, y₃` are any three complex
numbers with the 5₂ cubic's elementary symmetric functions. -/
theorem sum_re_log_one_sub_eq_log_recipCubic {y₁ y₂ y₃ : ℂ}
    (e1 : y₁ + y₂ + y₃ = 2) (e2 : y₁ * y₂ + y₁ * y₃ + y₂ * y₃ = 3)
    (e3 : y₁ * y₂ * y₃ = 1) {z : ℝ} (hz0 : 0 ≤ z) (hz1 : z ≤ 1) :
    (Complex.log (1 - y₁ * (z : ℂ))).re + (Complex.log (1 - y₂ * (z : ℂ))).re
        + (Complex.log (1 - y₃ * (z : ℂ))).re
      = Real.log (1 - 2 * z + 3 * z ^ 2 - z ^ 3) := by
  have hP : (0 : ℝ) < 1 - 2 * z + 3 * z ^ 2 - z ^ 3 := recipCubic_pos hz0 hz1
  have hprod : (1 - y₁ * (z : ℂ)) * (1 - y₂ * (z : ℂ)) * (1 - y₃ * (z : ℂ))
      = ((1 - 2 * z + 3 * z ^ 2 - z ^ 3 : ℝ) : ℂ) := by
    rw [prod_one_sub_mul_eq e1 e2 e3 (z : ℂ)]
    push_cast
    ring
  -- each factor is nonzero, since the product is a nonzero real
  have hne : ∀ w : ℂ, w = 1 - y₁ * (z : ℂ) ∨ w = 1 - y₂ * (z : ℂ)
      ∨ w = 1 - y₃ * (z : ℂ) → w ≠ 0 := by
    rintro w (rfl | rfl | rfl) h <;>
      · apply absurd hprod
        rw [h]
        simp only [zero_mul, mul_zero]
        exact fun hc => absurd (Complex.ofReal_eq_zero.mp hc.symm) (ne_of_gt hP)
  have h1 : (1 - y₁ * (z : ℂ)) ≠ 0 := hne _ (Or.inl rfl)
  have h2 : (1 - y₂ * (z : ℂ)) ≠ 0 := hne _ (Or.inr (Or.inl rfl))
  have h3 : (1 - y₃ * (z : ℂ)) ≠ 0 := hne _ (Or.inr (Or.inr rfl))
  -- real part of a complex log is the log of the norm
  rw [Complex.log_re, Complex.log_re, Complex.log_re,
    ← Real.log_mul (norm_ne_zero_iff.mpr h1) (norm_ne_zero_iff.mpr h2),
    ← Real.log_mul (mul_ne_zero (norm_ne_zero_iff.mpr h1) (norm_ne_zero_iff.mpr h2))
      (norm_ne_zero_iff.mpr h3)]
  congr 1
  rw [← norm_mul, ← norm_mul, hprod, Complex.norm_real, Real.norm_eq_abs,
    abs_of_pos hP]

/-! ### The three-root sum collapses to ONE real integral

The assembly step. With the pointwise identity above, plus linearity of the
integral and the fact that `Re` commutes with it, the three separate
dilogarithm-integrals over the roots become a single integral of a real
polynomial's logarithm:

    Σⱼ Re Li₂(yⱼ) = −∫₀¹ log(1 − 2z + 3z² − z³)/z dz

with `Li₂` the integral-defined `QOU.MathlibExt.cLiTwoExt`, which is the object
that makes sense at `‖y₁‖ = 1.52` where the series does not.

One integrability hypothesis per root, and only for the complex-valued
integrand — the real-part versions are derived (`Integrable.re`). For the 5₂
roots the three hypotheses are discharged by
`QOU.MathlibExt.intervalIntegrable_log_one_sub_div`, which needs
`Re(1 − yz) > 0` on `[0,1]` — true for all three.

**This does not prove the sum rule.** It makes Route 5's identity a theorem
about `cLiTwoExt`; what remains is (i) identifying `cLiTwoExt` with the `Li₂` of
the sum rule off the disc — i.e. proving it is the analytic continuation, still
open — and (ii) evaluating the resulting real integral in closed form, which is
untouched. Bean `qou-0yqu`. -/

open MeasureTheory in
/-- **`Σⱼ Re cLiTwoExt(yⱼ) = −∫₀¹ log P(z)/z dz`.** -/
theorem sum_re_cLiTwoExt_eq_integral {y₁ y₂ y₃ : ℂ}
    (e1 : y₁ + y₂ + y₃ = 2) (e2 : y₁ * y₂ + y₁ * y₃ + y₂ * y₃ = 3)
    (e3 : y₁ * y₂ * y₃ = 1)
    (h₁ : IntervalIntegrable (fun z : ℝ => Complex.log (1 - y₁ * (z : ℂ)) / (z : ℂ))
      volume 0 1)
    (h₂ : IntervalIntegrable (fun z : ℝ => Complex.log (1 - y₂ * (z : ℂ)) / (z : ℂ))
      volume 0 1)
    (h₃ : IntervalIntegrable (fun z : ℝ => Complex.log (1 - y₃ * (z : ℂ)) / (z : ℂ))
      volume 0 1) :
    (QOU.MathlibExt.cLiTwoExt y₁).re + (QOU.MathlibExt.cLiTwoExt y₂).re
        + (QOU.MathlibExt.cLiTwoExt y₃).re
      = -∫ z in (0 : ℝ)..1, Real.log (1 - 2 * z + 3 * z ^ 2 - z ^ 3) / z := by
  have hdiv : ∀ (w : ℂ) (r : ℝ), (w / (r : ℂ)).re = w.re / r := by
    intro w r
    rw [div_eq_mul_inv, ← Complex.ofReal_inv, Complex.mul_re, Complex.ofReal_re,
      Complex.ofReal_im, mul_zero, sub_zero, div_eq_mul_inv]
  have hre : ∀ y : ℂ,
      IntervalIntegrable (fun z : ℝ => Complex.log (1 - y * (z : ℂ)) / (z : ℂ)) volume 0 1 →
      IntervalIntegrable (fun z : ℝ => (Complex.log (1 - y * (z : ℂ))).re / z) volume 0 1 := by
    intro y h
    have hb : IntervalIntegrable
        (fun z : ℝ => (Complex.log (1 - y * (z : ℂ)) / (z : ℂ)).re) volume 0 1 :=
      ⟨h.1.re, h.2.re⟩
    have heq : (fun z : ℝ => (Complex.log (1 - y * (z : ℂ)) / (z : ℂ)).re)
        = fun z : ℝ => (Complex.log (1 - y * (z : ℂ))).re / z := by
      funext z
      exact hdiv (Complex.log (1 - y * (z : ℂ))) z
    rwa [heq] at hb
  have r₁ := hre y₁ h₁
  have r₂ := hre y₂ h₂
  have r₃ := hre y₃ h₃
  have key : ∀ (y : ℂ),
      IntervalIntegrable (fun z : ℝ => Complex.log (1 - y * (z : ℂ)) / (z : ℂ)) volume 0 1 →
      (QOU.MathlibExt.cLiTwoExt y).re
        = -∫ z in (0 : ℝ)..1, (Complex.log (1 - y * (z : ℂ))).re / z := by
    intro y h
    rw [QOU.MathlibExt.cLiTwoExt, Complex.neg_re]
    congr 1
    have hcomm := Complex.reCLM.intervalIntegral_comp_comm
      (μ := volume) (a := (0 : ℝ)) (b := 1) h
    rw [show ((∫ z in (0 : ℝ)..1, Complex.log (1 - y * (z : ℂ)) / (z : ℂ)).re)
        = Complex.reCLM (∫ z in (0 : ℝ)..1, Complex.log (1 - y * (z : ℂ)) / (z : ℂ))
      from rfl, ← hcomm]
    refine intervalIntegral.integral_congr fun z _ => ?_
    exact hdiv (Complex.log (1 - y * (z : ℂ))) z
  rw [key y₁ h₁, key y₂ h₂, key y₃ h₃, ← neg_add, ← neg_add,
    ← intervalIntegral.integral_add r₁ r₂,
    ← intervalIntegral.integral_add (r₁.add r₂) r₃]
  congr 1
  refine intervalIntegral.integral_congr fun z hz => ?_
  rw [Set.uIcc_of_le (by norm_num : (0 : ℝ) ≤ 1)] at hz
  rw [← add_div, ← add_div,
    sum_re_log_one_sub_eq_log_recipCubic e1 e2 e3 hz.1 hz.2]

end QOU.QBeta.FiveTwo
