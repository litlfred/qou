import Mathlib.Analysis.SpecialFunctions.Sqrt
import QOU.MassTheory.BindingRecurrenceSpectral
import QOU.MassTheory.BindingTauAnchorClosure

/-!
# The real roots of the depth-2 binding kernel (transcendental boundary)

The ℝ instance of `QOU.MassTheory.BindingRecurrenceSpectral`, moved behind the
boundary under the owner ruling of 2026-11-27 (bean `qou-dk7p`). The algebraic
file carries a root `λ` of `x² − τx + 1` as a parameter; here the roots are
written with `Real.sqrt`,

  `lambdaPlus τ = (τ + √(τ²−4))/2`, `lambdaMinus τ = (τ − √(τ²−4))/2`,

and shown to be the dominant root and its partner, so every algebraic theorem
applies to them.

LaTeX label: `prop:binding-recurrence-extensive`.

## References
- [leitner2026] §mass-theory/binding-genfun-qdifference
-/

namespace QOU.Mass

/-- Dominant root of the depth-2 binding kernel `x² − τx + 1`. -/
noncomputable def lambdaPlus (τ : ℝ) : ℝ := (τ + Real.sqrt (τ ^ 2 - 4)) / 2

/-- Sub-dominant root of the depth-2 binding kernel `x² − τx + 1`. -/
noncomputable def lambdaMinus (τ : ℝ) : ℝ := (τ - Real.sqrt (τ ^ 2 - 4)) / 2

/-- `λ₊` is a root of the characteristic polynomial `x² − τx + 1`. -/
theorem lambdaPlus_isRoot {τ : ℝ} (hτ : 2 < τ) :
    (lambdaPlus τ) ^ 2 - τ * lambdaPlus τ + 1 = 0 := by
  unfold lambdaPlus
  have hs : Real.sqrt (τ ^ 2 - 4) ^ 2 = τ ^ 2 - 4 := Real.sq_sqrt (by nlinarith)
  linear_combination hs / 4

/-- `λ₊` is the dominant root: `τ ≤ 2λ₊`. -/
theorem lambdaPlus_dominant (τ : ℝ) : τ ≤ 2 * lambdaPlus τ := by
  unfold lambdaPlus; linarith [Real.sqrt_nonneg (τ ^ 2 - 4)]

/-- `λ₋ = τ − λ₊`, the partner root. -/
theorem lambdaMinus_eq_partner (τ : ℝ) : lambdaMinus τ = τ - lambdaPlus τ := by
  unfold lambdaMinus lambdaPlus; ring

/-- **det = 1**: `λ₊ · λ₋ = 1`, from `root_mul_partner_eq_one`. -/
theorem lambda_product_eq_one {τ : ℝ} (hτ : 2 < τ) :
    lambdaPlus τ * lambdaMinus τ = 1 := by
  rw [lambdaMinus_eq_partner]; exact root_mul_partner_eq_one (lambdaPlus_isRoot hτ)

/-- **Extensive growth**, from `dominantRoot_gt_one`. -/
theorem lambdaPlus_gt_one {τ : ℝ} (hτ : 2 < τ) : 1 < lambdaPlus τ :=
  dominantRoot_gt_one hτ (lambdaPlus_dominant τ)

/-- **Trace identity**: `λ₊ + λ₋ = τ`. -/
theorem lambda_sum_eq_tau (τ : ℝ) : lambdaPlus τ + lambdaMinus τ = τ := by
  rw [lambdaMinus_eq_partner]; ring

/-- `binding_extensive_at_substrate` at the explicit real root. -/
theorem binding_extensive_at_substrate_lambdaPlus {q : ℝ} (hq : 0 < q) :
    1 < lambdaPlus (tauAnchor q) :=
  binding_extensive_at_substrate hq (lambdaPlus_dominant _)

end QOU.Mass
