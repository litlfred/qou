import QOU.Nuclear.FiveTwoDeformedSaddle
import Mathlib.Analysis.SpecialFunctions.Complex.Log

/-!
# The deformed 5₂ branch data (complex logarithms)

The complex-logarithm half of `QOU.Nuclear.FiveTwoDeformedSaddle` (bean `qou-trns`). The
algebra it rests on, the curve identity `deformed_saddle_iff_curve` and the Vieta product
`prod_one_sub`, stays outside the transcendental boundary over any commutative ring. Here:

* `branchTerm x y = 2 log(−y) − log(1−y) − log(1−xy) − log(1−y/x)`;
* `branch_data_of_curve`: on the curve, `branchTerm x y ∈ 2πi·ℤ`;
* `exp_branchSum_eq_one`: `exp (Σⱼ branchTerm x yⱼ) = 1` from Vieta alone.

Declaration names and the namespace are unchanged from before the split.
-/

namespace QOU.QBeta.FiveTwoDeformedSaddle

/-! ### The branch data, deformed -/

open Complex

/-- The exponentiated `y·∂V/∂y`: the combination of logarithms that the saddle
condition sets to an integer multiple of `2πi`. -/
noncomputable def branchTerm (x y : ℂ) : ℂ :=
  2 * Complex.log (-y) - Complex.log (1 - y) - Complex.log (1 - x * y)
    - Complex.log (1 - y / x)

/-- `x − y ≠ 0` is the same condition as `1 − y/x ≠ 0`, off `x = 0`. -/
theorem sub_ne_zero_of_one_sub_div {x y : ℂ} (hx : x ≠ 0) (h3 : (1 : ℂ) - y / x ≠ 0) :
    x - y ≠ 0 := by
  intro h
  rw [sub_eq_zero] at h
  exact h3 (by rw [← h, div_self hx, sub_self])

/-- **The exponential of `branchTerm`, evaluated.**

`exp` collapses the four logarithms; clearing the `1/x` inside `1 − y/x` puts the
result over the cleared denominator `(1−y)(1−xy)(x−y)`, which is the shape the
Vieta products come in. -/
theorem exp_branchTerm {x y : ℂ} (hx : x ≠ 0) (hy : y ≠ 0)
    (h1 : (1 : ℂ) - y ≠ 0) (h2 : (1 : ℂ) - x * y ≠ 0) (h3 : (1 : ℂ) - y / x ≠ 0) :
    Complex.exp (branchTerm x y) = y ^ 2 * x / ((1 - y) * (1 - x * y) * (x - y)) := by
  have hny : -y ≠ 0 := neg_ne_zero.mpr hy
  have hxy : x - y ≠ 0 := sub_ne_zero_of_one_sub_div hx h3
  have e0 : Complex.exp (2 * Complex.log (-y)) = (-y) * (-y) := by
    rw [show (2 : ℂ) * Complex.log (-y) = Complex.log (-y) + Complex.log (-y) by ring,
      Complex.exp_add, Complex.exp_log hny]
  have hrw : (1 : ℂ) - y / x = (x - y) / x := by field_simp
  unfold branchTerm
  rw [Complex.exp_sub, Complex.exp_sub, Complex.exp_sub, e0,
    Complex.exp_log h1, Complex.exp_log h2, Complex.exp_log h3, hrw]
  field_simp

/-- **`exp (branchTerm x y) = 1` on the curve.**

The exponential collapses the four logarithms to `y²/[(1−y)(1−xy)(1−y/x)]`,
which the saddle condition makes `1`. No branch is chosen — that is the point,
exactly as in `exp_branch_eq_one` at `x = 1`. -/
theorem exp_branchTerm_eq_one {x y : ℂ} (hx : x ≠ 0) (hy : y ≠ 0)
    (h1 : (1 : ℂ) - y ≠ 0) (h2 : (1 : ℂ) - x * y ≠ 0) (h3 : (1 : ℂ) - y / x ≠ 0)
    (hsad : x * y ^ 2 = (1 - y) * (1 - x * y) * (x - y)) :
    Complex.exp (branchTerm x y) = 1 := by
  have hxy : x - y ≠ 0 := by
    intro h
    rw [sub_eq_zero] at h
    exact h3 (by rw [← h, div_self hx, sub_self])
  rw [exp_branchTerm hx hy h1 h2 h3]
  rw [div_eq_one_iff_eq (by exact mul_ne_zero (mul_ne_zero h1 h2) hxy)]
  linear_combination hsad

/-- **The branch data of the deformed curve, derived.**

Every point of GGM's deformed 5₂ curve satisfies
`2 log(−y) − log(1−y) − log(1−xy) − log(1−y/x) = k·(2πi)` for some integer `k`.

This is `branch_data_of_cubic` carried along the whole deformation. It comes
from the curve alone: no dilogarithm, no analytic input. -/
theorem branch_data_of_curve {x y : ℂ} (hx : x ≠ 0) (hy : y ≠ 0)
    (h1 : (1 : ℂ) - y ≠ 0) (h2 : (1 : ℂ) - x * y ≠ 0) (h3 : (1 : ℂ) - y / x ≠ 0)
    (hcur : curve x y = 0) :
    ∃ k : ℤ, branchTerm x y = k * (2 * (Real.pi : ℂ) * I) := by
  have hsad := (deformed_saddle_iff_curve x y).mpr hcur
  have hexp := exp_branchTerm_eq_one hx hy h1 h2 h3 hsad
  rwa [Complex.exp_eq_one_iff] at hexp

/-! ### The sum over the three roots — what the pinning lemma consumes -/

/-- **`exp (Σⱼ branchTerm x yⱼ) = 1` from Vieta alone.**

Strictly weaker hypotheses than three copies of `exp_branchTerm_eq_one`: the
saddle condition is not used. The three products contribute

    (∏ⱼ(−yⱼ))² / [ ∏ⱼ(1−yⱼ) · ∏ⱼ(1−x·yⱼ) · ∏ⱼ(1−yⱼ/x) ]
      = 1 / ( 1 · x · (1/x) ) = 1

with `∏ⱼ(1−yⱼ) = 1` supplied by `prod_one_sub` above.

This is exactly the `hexp` hypothesis of
`QOU.Archimedean.eq_zero_of_continuousOn_of_exp_eq_one`, so along the arc the
sum of the deformed branch integers is pinned by its base-point value — given
continuity, which is that lemma's remaining open input. -/
theorem exp_branchSum_eq_one {x y₁ y₂ y₃ : ℂ} (hx : x ≠ 0)
    (hy₁ : y₁ ≠ 0) (hy₂ : y₂ ≠ 0) (hy₃ : y₃ ≠ 0)
    (ha₁ : (1 : ℂ) - y₁ ≠ 0) (ha₂ : (1 : ℂ) - y₂ ≠ 0) (ha₃ : (1 : ℂ) - y₃ ≠ 0)
    (hb₁ : (1 : ℂ) - x * y₁ ≠ 0) (hb₂ : (1 : ℂ) - x * y₂ ≠ 0) (hb₃ : (1 : ℂ) - x * y₃ ≠ 0)
    (hc₁ : (1 : ℂ) - y₁ / x ≠ 0) (hc₂ : (1 : ℂ) - y₂ / x ≠ 0) (hc₃ : (1 : ℂ) - y₃ / x ≠ 0)
    (h₁ : x * (y₁ + y₂ + y₃) = x ^ 2 + 1)
    (h₂ : x * (y₁ * y₂ + y₁ * y₃ + y₂ * y₃) = x ^ 2 + x + 1)
    (h₃ : y₁ * y₂ * y₃ = 1) :
    Complex.exp (branchTerm x y₁ + branchTerm x y₂ + branchTerm x y₃) = 1 := by
  have hd₁ : x - y₁ ≠ 0 := sub_ne_zero_of_one_sub_div hx hc₁
  have hd₂ : x - y₂ ≠ 0 := sub_ne_zero_of_one_sub_div hx hc₂
  have hd₃ : x - y₃ ≠ 0 := sub_ne_zero_of_one_sub_div hx hc₃
  -- the three Vieta products
  have pA : (1 - y₁) * (1 - y₂) * (1 - y₃) = 1 := prod_one_sub' x y₁ y₂ y₃ hx h₁ h₂ h₃
  have pB : (1 - x * y₁) * (1 - x * y₂) * (1 - x * y₃) = x := by
    linear_combination (-1 : ℂ) * h₁ + x * h₂ - x ^ 3 * h₃
  have pC : (x - y₁) * (x - y₂) * (x - y₃) = x ^ 2 := by
    linear_combination (-x) * h₁ + h₂ - h₃
  rw [Complex.exp_add, Complex.exp_add,
    exp_branchTerm hx hy₁ ha₁ hb₁ hc₁, exp_branchTerm hx hy₂ ha₂ hb₂ hc₂,
    exp_branchTerm hx hy₃ ha₃ hb₃ hc₃, div_mul_div_comm, div_mul_div_comm,
    div_eq_one_iff_eq (by
      exact mul_ne_zero (mul_ne_zero (mul_ne_zero (mul_ne_zero ha₁ hb₁) hd₁)
        (mul_ne_zero (mul_ne_zero ha₂ hb₂) hd₂)) (mul_ne_zero (mul_ne_zero ha₃ hb₃) hd₃))]
  -- `(∏y)²·x³ = ∏(1−y) · ∏(1−x·y) · ∏(x−y) = 1 · x · x²`
  linear_combination ((y₁ * y₂ * y₃ + 1) * x ^ 3) * h₃
    - (((1 - x * y₁) * (1 - x * y₂) * (1 - x * y₃))
        * ((x - y₁) * (x - y₂) * (x - y₃))) * pA
    - ((x - y₁) * (x - y₂) * (x - y₃)) * pB
    - x * pC

end QOU.QBeta.FiveTwoDeformedSaddle
