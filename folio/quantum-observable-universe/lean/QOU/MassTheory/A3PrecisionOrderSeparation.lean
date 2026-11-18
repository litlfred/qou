/-
# Improving A=3 binding precision is not a higher-cluster-order problem — an order-separation prune

The corpus model predicts the physical ratio `ρ_strong(3) = B(³H)/B(²H) = 3.8128` as
`ρ_grad_G(3) + c₃ = 3.3420 + 0.297 = 3.6390`, a **4.56% miss** (`Δ = 0.17377`). The dominant term
`ρ_grad_G(3) = [3]_q` (graded coinvariant dimension) is EXACT (87.6% of the ratio); the derived
leading (h⁴) Borromean cluster `c₃ = 0.297` is 7.8%. So all the error is in the subleading many-body
cluster. The precision question: can the miss be closed by HIGHER cluster ORDERS (h⁶, h⁸, …), or does
it need a NEW leading-order channel?

Writing the 3-body cluster as `c₃·(1 + a₁h² + a₂h⁴ + …)` with `h = q−q⁻¹` (`h² ≈ 0.0437` at `q₀`),
this file machine-checks the **order-separation** that prunes the higher-order route:

- a single higher-order term with a **bounded** coefficient `|a| ≤ B` contributes at most `B·c·h²`
  (`bounded_order_term_le`);
- the **entire** bounded (`|aₖ| ≤ 2`) geometric tail `c₃·2·h²/(1−h²)` closes ≤ 0.7% of the ratio —
  ≪ the 4.56% miss (`bounded_tail_lt_miss`);
- a higher-order closure would need an **anomalous** h⁶ coefficient `a₁ = Δ/(c₃·h²) > 13`
  (`required_coeff_gt_thirteen`) — 13× the O(1) natural size, a fit red-flag (cf. the Q_β `c₃` `1/u³`
  hypersensitivity).

**Consequence.** A=3 precision is NOT a "compute more cluster orders" problem — that route is
order-separated out. It is the Δ_λ closure: the missing leading-order (h⁴) 3-body channel is a
per-partition magnitude the Δ_λ gate must supply. A=3 ratio precision is Δ_λ-gated, not q₀-limited (the
overall scale cancels in the ratio). scope-(a); no fit; nothing wired. Companion probe
`computations/deltalambda/a3_precision_order_decomposition_probe.py`.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.AbsoluteValue.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Data.Real.Basic

namespace QOU.MassTheory.A3PrecisionOrderSeparation

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **Bounded coefficient ⇒ bounded higher-order contribution.** A higher-order cluster term
`a · c · h²` with a coefficient bounded by `|a| ≤ B` contributes at most `B · c · h²` in magnitude
(for `0 ≤ c`, `0 ≤ h²`). This is the structural fact behind the tail bound: routine (bounded-
coefficient) higher orders cannot exceed `B·c·h²` per order. -/
theorem bounded_order_term_le {a c h2 B : R} (hc : 0 ≤ c) (hh : 0 ≤ h2) (ha : |a| ≤ B) :
    |a * c * h2| ≤ B * c * h2 := by
  rw [abs_mul, abs_mul, abs_of_nonneg hc, abs_of_nonneg hh]
  exact mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_right ha hc) hh

/-- **The full bounded (`|aₖ| ≤ 2`) higher-order tail closes ≤ 0.7% of the ratio — ≪ the 4.56% miss.**
The geometric tail `c₃·2·h²/(1−h²)` at the corpus values (`c₃ = 0.297`, `h² = 0.0437062`) is
`< 0.0272`, far below the miss `Δ = 0.17376892`. So even summing every bounded higher order cannot
close the A=3 miss. -/
theorem bounded_tail_lt_miss :
    (0.297 : ℝ) * 2 * 0.0437062 / (1 - 0.0437062) < 0.17376892 := by norm_num

/-- **A higher-order closure would need an anomalous h⁶ coefficient `a₁ > 13`** — 13× the O(1)
natural size (`h² ≈ 0.0437`), a fit red-flag (cf. the Q_β `c₃` `1/u³` hypersensitivity). Here
`a₁ = Δ/(c₃·h²) = 0.17376892/(0.297·0.0437062)`. -/
theorem required_coeff_gt_thirteen :
    (0.17376892 : ℝ) / (0.297 * 0.0437062) > 13 := by norm_num

/-- **The graded baseline dominates** (`ρ_grad_G(3)/ρ_strong(3) > 87%`): the exact, derived term is
almost the whole ratio, so all the precision error lives in the small subleading cluster. -/
theorem graded_baseline_dominates : (3.3420311 : ℝ) / 3.8128 > 0.87 := by norm_num

/-- **Capstone — A=3 precision is Δ_λ-gated, not a higher-order refinement.** The bounded higher-order
tail is below the miss (`bounded_tail_lt_miss`) while the graded baseline dominates
(`graded_baseline_dominates`); closing the miss by higher orders needs an anomalous coefficient
(`required_coeff_gt_thirteen`). So the routine higher-cluster-order route is order-separated out —
precision improvement requires a new leading-order (h⁴) channel (the Δ_λ closure). scope-(a); no fit. -/
theorem a3_precision_needs_leading_channel :
    ((0.297 : ℝ) * 2 * 0.0437062 / (1 - 0.0437062) < 0.17376892) ∧
    ((0.17376892 : ℝ) / (0.297 * 0.0437062) > 13) ∧
    ((3.3420311 : ℝ) / 3.8128 > 0.87) :=
  ⟨bounded_tail_lt_miss, required_coeff_gt_thirteen, graded_baseline_dominates⟩

/-- **Two-term bounded higher-order sum inequality (`qou-ijoi`).**
If two higher-order cluster coefficients satisfy `|a₁| ≤ B₁` and `|a₂| ≤ B₂` with
`0 ≤ c` and `0 ≤ h2`, then `|a₁ * c * h2 + a₂ * c * h2| ≤ (B₁ + B₂) * c * h2`. -/
theorem bounded_two_order_sum_le {a₁ a₂ c h2 B₁ B₂ : R}
    (hc : 0 ≤ c) (hh : 0 ≤ h2) (ha₁ : |a₁| ≤ B₁) (ha₂ : |a₂| ≤ B₂) :
    |a₁ * c * h2 + a₂ * c * h2| ≤ (B₁ + B₂) * c * h2 := by
  have h1 := bounded_order_term_le hc hh ha₁
  have h2' := bounded_order_term_le hc hh ha₂
  have htri := abs_add_le (a₁ * c * h2) (a₂ * c * h2)
  linarith

end QOU.MassTheory.A3PrecisionOrderSeparation
