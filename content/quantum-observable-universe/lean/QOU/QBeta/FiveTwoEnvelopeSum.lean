import QOU.QBeta.FiveTwoDeformedSaddle

/-!
# `Σⱼ ∂V/∂x = −2·log x / x` — the envelope's second ingredient

Bean `qou-trns`. `FiveTwoCurveDeriv.lean` supplies the first ingredient (the
roots are differentiable, so the chain rule applies and the `dyⱼ/dx` terms die
against `∂V/∂y = 0`). This file supplies the second: what the surviving
`∂V/∂x` terms sum to.

## The computation

    V(x,y) = Li₂(y) + Li₂(xy) + Li₂(y/x) + log(−y)²
    ∂V/∂x  = [ −log(1 − x·y) + log(1 − y/x) ] / x

so summing over the three roots needs the two log-sums, and **each is pinned by a
Vieta product already proved in `FiveTwoCyclotomicBloch` (#4658)**:

| product | exponentiates to | gives |
|---|---|---|
| `∏ⱼ(1 − x·yⱼ) = x` | `exp(Σⱼ log(1−x·yⱼ)) = x` | `Σⱼ log(1−x·yⱼ) = log x + 2πi·k₁` |
| `∏ⱼ(x − yⱼ) = x²` | `exp(Σⱼ log(1−yⱼ/x)) = x⁻¹` | `Σⱼ log(1−yⱼ/x) = −log x + 2πi·k₂` |

and then

    Σⱼ ∂V/∂x = (1/x)·[ −2·log x + 2πi·(k₂ − k₁) ] .

With the branch integers pinned to `0` — which is what
`QOU/Archimedean/BranchIntegerPinning.lean` does, given continuity and the base
point — this is `−2·log x / x`. On `x = e^{iφ}` that is `−2iφ/x`, and against
`dx/dφ = i·x` it gives `dS/dφ = Re(−2iφ·i) = 2φ`.

## What is proved here, and what is assumed

`exp_sum_log_one_sub_x_mul` and `exp_sum_log_one_sub_div` are proved **from Vieta
alone** — they are the `hexp` inputs the pinning lemma consumes, and they need no
analysis.

`sum_dVdx_of_pinned` then takes the *pinned* sums as hypotheses and does the
algebra. It does **not** prove the pinning: that needs `hcont`, which remains
open (see this bean's earlier entries). Stating it with the pinned sums as
hypotheses is the honest factoring — the algebra is separable from the analysis,
and only the algebra is done here.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.QBeta.FiveTwoDeformedSaddle

open Complex

/-! ### The two `hexp` inputs, from Vieta alone -/

/-- **`exp(Σⱼ log(1 − x·yⱼ)) = x`.**

The exponential of the first log-sum is `∏ⱼ(1 − x·yⱼ)`, which Vieta makes `x`
(`prod_one_sub_x_mul`, #4658). No analysis, no branch choice. -/
theorem exp_sum_log_one_sub_x_mul {x y₁ y₂ y₃ : ℂ}
    (hb₁ : (1 : ℂ) - x * y₁ ≠ 0) (hb₂ : (1 : ℂ) - x * y₂ ≠ 0) (hb₃ : (1 : ℂ) - x * y₃ ≠ 0)
    (h₁ : x * (y₁ + y₂ + y₃) = x ^ 2 + 1)
    (h₂ : x * (y₁ * y₂ + y₁ * y₃ + y₂ * y₃) = x ^ 2 + x + 1)
    (h₃ : y₁ * y₂ * y₃ = 1) :
    Complex.exp (Complex.log (1 - x * y₁) + Complex.log (1 - x * y₂)
      + Complex.log (1 - x * y₃)) = x := by
  rw [Complex.exp_add, Complex.exp_add, Complex.exp_log hb₁, Complex.exp_log hb₂,
    Complex.exp_log hb₃]
  linear_combination (-1 : ℂ) * h₁ + x * h₂ - x ^ 3 * h₃

/-- **`exp(Σⱼ log(1 − yⱼ/x)) = x⁻¹`.**

`∏ⱼ(1 − yⱼ/x) = ∏ⱼ(x − yⱼ)/x³ = x²/x³ = 1/x`, using `prod_x_sub` (#4658). -/
theorem exp_sum_log_one_sub_div {x y₁ y₂ y₃ : ℂ} (hx : x ≠ 0)
    (hc₁ : (1 : ℂ) - y₁ / x ≠ 0) (hc₂ : (1 : ℂ) - y₂ / x ≠ 0) (hc₃ : (1 : ℂ) - y₃ / x ≠ 0)
    (h₁ : x * (y₁ + y₂ + y₃) = x ^ 2 + 1)
    (h₂ : x * (y₁ * y₂ + y₁ * y₃ + y₂ * y₃) = x ^ 2 + x + 1)
    (h₃ : y₁ * y₂ * y₃ = 1) :
    Complex.exp (Complex.log (1 - y₁ / x) + Complex.log (1 - y₂ / x)
      + Complex.log (1 - y₃ / x)) = x⁻¹ := by
  have hp : (x - y₁) * (x - y₂) * (x - y₃) = x ^ 2 := by
    linear_combination (-x) * h₁ + h₂ - h₃
  have hrw : ∀ y : ℂ, (1 : ℂ) - y / x = (x - y) / x := fun y => by field_simp
  rw [Complex.exp_add, Complex.exp_add, Complex.exp_log hc₁, Complex.exp_log hc₂,
    Complex.exp_log hc₃, hrw, hrw, hrw, div_mul_div_comm, div_mul_div_comm, hp]
  field_simp

/-! ### The assembly -/

/-- **`Σⱼ ∂V/∂x = −2·log x / x`, given the pinned log-sums.**

Pure algebra: the two hypotheses are the branch-pinned values of the log-sums,
and everything else cancels. The pinning itself is *not* proved here — it needs
`hcont`, which is open — so it is taken as a hypothesis, which is the honest
factoring of analysis from algebra. -/
theorem sum_div_of_pinned {x a₁ a₂ a₃ b₁ b₂ b₃ L : ℂ} (hx : x ≠ 0)
    (hA : a₁ + a₂ + a₃ = L) (hB : b₁ + b₂ + b₃ = -L) :
    (-a₁ + b₁) / x + (-a₂ + b₂) / x + (-a₃ + b₃) / x = -2 * L / x := by
  field_simp
  linear_combination hB - hA

/-- The same, with the logarithms put back. Stated separately so that no tactic
ever sees a `log` while clearing denominators — an earlier draft let `field_simp`
rewrite `1 - y/x` to `(x-y)/x` *inside* the logarithm, which changes the branch. -/
theorem sum_dVdx_of_pinned {x y₁ y₂ y₃ : ℂ} (hx : x ≠ 0)
    (hA : Complex.log (1 - x * y₁) + Complex.log (1 - x * y₂) + Complex.log (1 - x * y₃)
      = Complex.log x)
    (hB : Complex.log (1 - y₁ / x) + Complex.log (1 - y₂ / x) + Complex.log (1 - y₃ / x)
      = -Complex.log x) :
    (-Complex.log (1 - x * y₁) + Complex.log (1 - y₁ / x)) / x
      + (-Complex.log (1 - x * y₂) + Complex.log (1 - y₂ / x)) / x
      + (-Complex.log (1 - x * y₃) + Complex.log (1 - y₃ / x)) / x
      = -2 * Complex.log x / x :=
  sum_div_of_pinned hx hA hB

/-- **On the unit circle, against `dx/dφ = i·x`, that is `2φ`.**

`Σⱼ ∂V/∂x · (i·x) = −2·log x · i`, and with `log(e^{iφ}) = iφ` this is
`−2·iφ·i = 2φ` — real, which is why `S` is real and its derivative is `2φ`. -/
theorem envelope_value {x : ℂ} (φ : ℝ) (hx : x ≠ 0) (hlog : Complex.log x = φ * I) :
    (-2 * Complex.log x / x) * (I * x) = (2 * φ : ℝ) := by
  have h : (-2 * ((φ : ℂ) * I) / x) * (I * x) = -2 * (φ : ℂ) * I ^ 2 := by
    field_simp
  rw [hlog, h, Complex.I_sq]
  push_cast
  ring

end QOU.QBeta.FiveTwoDeformedSaddle
