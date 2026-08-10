import QOU.QBeta.FiveTwoEnvelopeSum
import QOU.Archimedean.BranchIntegerPinning
import QOU.Archimedean.ConstantOffOnePoint
import Mathlib.Analysis.Calculus.Deriv.Prod
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.Calculus.FDeriv.RestrictScalars

/-!
# The envelope, assembled: the three remaining joins

Bean `qou-trns`. The pieces existed separately; this file joins them. Each of the
three sections is one of the tasks that bean listed as outstanding.

## 1. The envelope theorem itself

`hasDerivAt_of_partial_y_eq_zero`: if `∂F/∂y = 0` at the point, then along **any**
differentiable path the total derivative collapses to the `x`-part:

    d/dt F(x t, y t) = (∂F/∂x)·x′(t)

with `y′` never appearing. This is why the envelope argument needs only that the
roots are *differentiable*, not what their derivatives are — and
`deformed_saddle_iff_curve` already gives `∂V/∂y = 0` for free, because the
saddle condition **is** the curve.

Stated for a general `F`, since nothing about the dilogarithm enters.

## 2. The branch pinning, reduced to `hcont`

`exp_logSumA_sub_log_eq_one` and `exp_logSumB_add_log_eq_one` discharge the
`exp(·) = 1` hypothesis of the pinning lemma **from the Vieta products alone**;
`branchDiff_eq_zero_of_continuousOn` then pins the branch difference to `0` given
continuity and the base point. So *all* the algebra is done and what remains is
exactly `hcont`.

## 3. The gluing

`envelope_integrate`: from `S′ = 2φ` on `[0,b)` **off one point**, plus continuity
on `[0,b]`, conclude `S φ = S 0 + φ²` on all of `[0,b]` — so `S(π) − S(0) = π²`.
That one exceptional point is `φ₀`, where the discriminant vanishes and no
differentiable root labelling exists (`exists_unit_circle_disc_zero`).

## ⚠ What is still not proved

`hcont` — continuity of the branch-difference along the arc. Every other input to
the envelope step is now a theorem; this is the single remaining analytic
hypothesis, and it is stated as a hypothesis everywhere it is used rather than
assumed silently.

Route 26 G8 also measured that the section-2 identities hold on `[0,π)` and
**fail at the endpoint** `φ = π`, forced by `1 − x·y` and `1 − y/x` coinciding at
`x = −1`. Harmless — `π` is an endpoint and section 3 needs the derivative only
on the half-open interval — but it is why the statements below are on `Ico`.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.QBeta.FiveTwoDeformedSaddle

open Complex Set

/-! ### 1. The envelope theorem -/

/-- **The envelope theorem.** If the `y`-partial vanishes at the point, the total
derivative along any differentiable path is the `x`-part alone — `y′` cancels.

This is the whole reason the envelope argument needs only *existence* of
`dyⱼ/dx`. -/
theorem hasDerivAt_of_partial_y_eq_zero {F : ℂ × ℂ → ℂ} {F' : (ℂ × ℂ) →L[ℂ] ℂ}
    {x y : ℝ → ℂ} {x' y' : ℂ} {t : ℝ}
    (hF : HasFDerivAt F F' (x t, y t))
    (hx : HasDerivAt x x' t) (hy : HasDerivAt y y' t)
    (hzero : F' (0, 1) = 0) :
    HasDerivAt (fun s => F (x s, y s)) (F' (1, 0) * x') t := by
  have hpath : HasDerivAt (fun s => (x s, y s)) ((x', y') : ℂ × ℂ) t := hx.prodMk hy
  have hcomp := (hF.restrictScalars ℝ).comp_hasDerivAt t hpath
  have hlin : (F'.restrictScalars ℝ) ((x', y') : ℂ × ℂ) = F' (1, 0) * x' := by
    show F' ((x', y') : ℂ × ℂ) = F' (1, 0) * x'
    have hv : ((x', y') : ℂ × ℂ) = x' • ((1 : ℂ), (0 : ℂ)) + y' • ((0 : ℂ), (1 : ℂ)) := by
      ext <;> simp
    rw [hv, map_add, F'.map_smul, F'.map_smul, hzero]
    simp [smul_eq_mul, mul_comm]
  rwa [hlin] at hcomp

/-! ### 2. The branch pinning, with the `exp` inputs discharged -/

/-- `exp(Σⱼ log(1 − x·yⱼ) − log x) = 1`, from the Vieta product. This is the
`hexp` hypothesis of `eq_zero_of_continuousOn_of_exp_eq_one`, discharged. -/
theorem exp_logSumA_sub_log_eq_one {x y₁ y₂ y₃ : ℂ} (hx : x ≠ 0)
    (hb₁ : (1 : ℂ) - x * y₁ ≠ 0) (hb₂ : (1 : ℂ) - x * y₂ ≠ 0) (hb₃ : (1 : ℂ) - x * y₃ ≠ 0)
    (h₁ : x * (y₁ + y₂ + y₃) = x ^ 2 + 1)
    (h₂ : x * (y₁ * y₂ + y₁ * y₃ + y₂ * y₃) = x ^ 2 + x + 1)
    (h₃ : y₁ * y₂ * y₃ = 1) :
    Complex.exp ((Complex.log (1 - x * y₁) + Complex.log (1 - x * y₂)
      + Complex.log (1 - x * y₃)) - Complex.log x) = 1 := by
  rw [Complex.exp_sub, exp_sum_log_one_sub_x_mul hb₁ hb₂ hb₃ h₁ h₂ h₃, Complex.exp_log hx]
  exact div_self hx

/-- `exp(Σⱼ log(1 − yⱼ/x) + log x) = 1`, from the other Vieta product. -/
theorem exp_logSumB_add_log_eq_one {x y₁ y₂ y₃ : ℂ} (hx : x ≠ 0)
    (hc₁ : (1 : ℂ) - y₁ / x ≠ 0) (hc₂ : (1 : ℂ) - y₂ / x ≠ 0) (hc₃ : (1 : ℂ) - y₃ / x ≠ 0)
    (h₁ : x * (y₁ + y₂ + y₃) = x ^ 2 + 1)
    (h₂ : x * (y₁ * y₂ + y₁ * y₃ + y₂ * y₃) = x ^ 2 + x + 1)
    (h₃ : y₁ * y₂ * y₃ = 1) :
    Complex.exp ((Complex.log (1 - y₁ / x) + Complex.log (1 - y₂ / x)
      + Complex.log (1 - y₃ / x)) + Complex.log x) = 1 := by
  rw [Complex.exp_add, exp_sum_log_one_sub_div hx hc₁ hc₂ hc₃ h₁ h₂ h₃, Complex.exp_log hx]
  exact inv_mul_cancel₀ hx

/-- **The pinning, reduced to `hcont`.** Given that the branch difference is
continuous on `[a,b]` and vanishes at `a`, and that its exponential is `1`
throughout — which the two lemmas above supply from Vieta — it vanishes
identically.

This is `eq_zero_of_continuousOn_of_exp_eq_one` with its algebraic input
discharged: **only continuity is left**. -/
theorem branchDiff_eq_zero_of_continuousOn {G : ℝ → ℂ} {a b φ : ℝ}
    (hφ : φ ∈ Icc a b) (hcont : ContinuousOn G (Icc a b))
    (hexp : ∀ s ∈ Icc a b, Complex.exp (G s) = 1) (h0 : G a = 0) :
    G φ = 0 :=
  QOU.Archimedean.eq_zero_of_continuousOn_of_exp_eq_one hφ hcont hexp h0

/-! ### 3. The gluing -/

/-- **From `S′ = 2φ` off one point to `S φ = S 0 + φ²`.**

`constant_of_hasDerivWithinAt_zero_off_point` applied to `φ ↦ S φ − φ²`. The one
exceptional point is `φ₀`, where the discriminant vanishes
(`exists_unit_circle_disc_zero`) and no differentiable root labelling exists.

At `b = π` this is `S(π) − S(0) = π²`, which is what the transport wants. -/
theorem envelope_integrate {S : ℝ → ℝ} {b c : ℝ}
    (hcont : ContinuousOn S (Icc 0 b))
    (hderiv : ∀ φ ∈ Ico 0 b, φ ≠ c → HasDerivWithinAt S (2 * φ) (Ici φ) φ) :
    ∀ φ ∈ Icc 0 b, S φ = S 0 + φ ^ 2 := by
  have key := QOU.Archimedean.constant_of_hasDerivWithinAt_zero_off_point
    (f := fun φ => S φ - φ ^ 2) (a := 0) (b := b) (c := c)
    (by
      exact hcont.sub ((continuous_pow 2).continuousOn))
    (by
      intro φ hφ hne
      have hsq : HasDerivWithinAt (fun s : ℝ => s ^ 2) (2 * φ) (Ici φ) φ := by
        simpa using ((hasDerivAt_pow 2 φ).hasDerivWithinAt (s := Ici φ))
      simpa using (hderiv φ hφ hne).sub hsq)
  intro φ hφ
  have := key φ hφ
  linarith [this]

end QOU.QBeta.FiveTwoDeformedSaddle
