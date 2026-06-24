import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# QOU.Mass.BindingRecurrenceSpectral — the depth-2 binding kernel is extensive

The fibre q-difference kernel for the binding generating function is depth-2,
`R(q,x) = x² − τ·x + 1` with `det = 1` (constant term `1`), and `τ` is fixed
**without fit** by the selection-rule anchors `a_D^(n) = lw(n−1)`
(`binding_selection_rule_tau_closure.py`, PR #2612); `τ(q₀) = 2.6424`.

The body-order recurrence `a_{n+2} = τ·a_{n+1} − a_n`
(`QOU.Mass.BindingQDifferenceRecurrence`, depth `2`, kernel `[−1, τ]`) has
characteristic roots `λ_± = (τ ± √(τ²−4))/2`. This file proves the three
structural facts that make the kernel **extensive** (its solutions grow), which
is exactly the property the saturating `|χ|` joint trace lacks
(`productModel_3body_nonpos`; PR #2703: `B_joint` is A-independent, λ_eff ≈ 1):

* `lambdaPlus_isRoot`     — `λ₊` solves `x² − τx + 1 = 0`;
* `lambda_product_eq_one` — `λ₊ · λ₋ = 1` (the `det = 1` / reciprocal-roots fact);
* `lambdaPlus_gt_one`     — for `τ > 2`, the dominant root `λ₊ > 1` (extensive
  growth), whence `λ₋ = 1/λ₊ < 1`.

So `τ > 2 ⇒ λ₊ > 1`: the kernel encodes the extensive (A-scaling) binding the
saturating multiplicative trace (sitting at the degenerate `τ = 2`, `λ = 1`
no-growth boundary) cannot source. `τ(q₀) = 2.6424 > 2` satisfies the hypothesis.

LaTeX label: `prop:binding-recurrence-extensive` (interprets
`prop:binding-genfun-qdifference`).

## References
- [manuscript] §mass-theory/binding-genfun-qdifference
-/

namespace QOU.Mass

open Real

/-- Dominant root of the depth-2 binding kernel `x² − τx + 1`. -/
noncomputable def lambdaPlus (τ : ℝ) : ℝ := (τ + Real.sqrt (τ ^ 2 - 4)) / 2

/-- Sub-dominant root of the depth-2 binding kernel `x² − τx + 1`. -/
noncomputable def lambdaMinus (τ : ℝ) : ℝ := (τ - Real.sqrt (τ ^ 2 - 4)) / 2

/-- `λ₊` is a root of the characteristic polynomial `x² − τx + 1`. -/
theorem lambdaPlus_isRoot {τ : ℝ} (hτ : 2 < τ) :
    (lambdaPlus τ) ^ 2 - τ * lambdaPlus τ + 1 = 0 := by
  unfold lambdaPlus
  have hs : Real.sqrt (τ ^ 2 - 4) ^ 2 = τ ^ 2 - 4 := Real.sq_sqrt (by nlinarith)
  have expand :
      ((τ + Real.sqrt (τ ^ 2 - 4)) / 2) ^ 2 - τ * ((τ + Real.sqrt (τ ^ 2 - 4)) / 2) + 1
        = (Real.sqrt (τ ^ 2 - 4) ^ 2 - (τ ^ 2 - 4)) / 4 := by ring
  rw [expand, hs]; ring

/-- **det = 1**: the two roots are reciprocal, `λ₊ · λ₋ = 1` (the constant term). -/
theorem lambda_product_eq_one {τ : ℝ} (hτ : 2 < τ) :
    lambdaPlus τ * lambdaMinus τ = 1 := by
  unfold lambdaPlus lambdaMinus
  have hs : Real.sqrt (τ ^ 2 - 4) ^ 2 = τ ^ 2 - 4 := Real.sq_sqrt (by nlinarith)
  have expand :
      (τ + Real.sqrt (τ ^ 2 - 4)) / 2 * ((τ - Real.sqrt (τ ^ 2 - 4)) / 2)
        = (τ ^ 2 - Real.sqrt (τ ^ 2 - 4) ^ 2) / 4 := by ring
  rw [expand, hs]; ring

/-- **Extensive growth.** For `τ > 2` the dominant root exceeds `1`; with
`λ₊ · λ₋ = 1` this forces `λ₋ < 1`. The depth-2 binding kernel therefore has a
growing (extensive) general solution — the property a saturating multiplicative
trace (`τ = 2`, `λ = 1`) lacks. -/
theorem lambdaPlus_gt_one {τ : ℝ} (hτ : 2 < τ) : 1 < lambdaPlus τ := by
  unfold lambdaPlus
  have hpos : (0 : ℝ) < τ ^ 2 - 4 := by nlinarith
  have hs : 0 < Real.sqrt (τ ^ 2 - 4) := Real.sqrt_pos.mpr hpos
  linarith

end QOU.Mass
