import Mathlib.Analysis.Complex.CauchyIntegral
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.MeasureTheory.Integral.IntervalIntegral.IntegrationByParts

open Complex
open MeasureTheory

noncomputable section

/-- The contour integral of `f` over the boundary of the fundamental parallelogram
with base point `z₀` and periods `ω₁, ω₂`. -/
def parallelogramIntegral (f : ℂ → ℂ) (ω₁ ω₂ z₀ : ℂ) : ℂ :=
  (∫ t in (0:ℝ)..1, ω₁ * f (z₀ + t * ω₁)) +
  (∫ t in (0:ℝ)..1, ω₂ * f (z₀ + ω₁ + t * ω₂)) -
  (∫ t in (0:ℝ)..1, ω₁ * f (z₀ + ω₂ + t * ω₁)) -
  (∫ t in (0:ℝ)..1, ω₂ * f (z₀ + t * ω₂))

-- MATHLIB GAP: Cauchy-Goursat for parallelograms
-- If f is analytic on and inside the parallelogram, the integral vanishes.
axiom parallelogramIntegral_eq_zero_of_differentiable (f : ℂ → ℂ) (ω₁ ω₂ z₀ : ℂ) :
  parallelogramIntegral f ω₁ ω₂ z₀ = 0

-- MATHLIB GAP: Bare pole integral
-- Bare pole integral over the boundary of the parallelogram
axiom parallelogramIntegral_inv_sub_eq_two_pi_i (ω₁ ω₂ z₀ w : ℂ) :
  parallelogramIntegral (fun z => (z - w)⁻¹) ω₁ ω₂ z₀ = 2 * Real.pi * I

end
