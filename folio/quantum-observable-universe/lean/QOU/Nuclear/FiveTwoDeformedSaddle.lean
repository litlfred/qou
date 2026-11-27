import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.LinearCombination

/-!
# The deformed saddle condition **is** the GGM curve

Bean `qou-trns`. `QOU/QBeta/FiveTwoSaddleSumRule.lean` proves this at the base
point `x = 1`:

```lean
theorem cubic_iff_sq_eq_cube (y : R) : y³ - 2y² + 3y - 1 = 0 ↔ y² = (1 - y)³
theorem branch_data_of_cubic … : ∃ k : ℤ, 2 log y - 3 log (1 - y) = k·(2πi)
```

and calls the branch data "the sole source of the `π²` in the sum rule". The
**deformed** statements — the ones the transport travels along — were missing.
This file supplies them.

## The saddle condition

The transport's integrand is
`V(x,y) = Li₂(y) + Li₂(xy) + Li₂(y/x) + log(−y)²`, and

    ∂V/∂y = (1/y)·[ 2 log(−y) − log(1−y) − log(1−xy) − log(1−y/x) ]

using `d/dz Li₂(z) = −log(1−z)/z` three times. Exponentiating kills every
logarithm, and `∂V/∂y = 0` becomes

    y² = (1−y)(1−xy)(1−y/x)

`deformed_saddle_iff_curve` shows this is **identically** GGM's deformed 5₂
curve — over any commutative ring, denominators cleared. At `x = 1` it collapses
to `y² = (1−y)³`, recovering the corpus statement (`saddle_at_one`).

That matters for scope. The envelope argument needs the saddle condition, and
the saddle condition is often the part one worries about; here it is free,
because it *is* the curve the roots were defined by. What the envelope still
needs is the analysis — `dyⱼ/dx` and `d/dz Li₂` along a path — not this.

## The branch data, deformed

`branch_data_of_curve`: every point of the curve satisfies

    2 log(−y) − log(1−y) − log(1−xy) − log(1−y/x) = k·(2πi),  k ∈ ℤ

derived from the curve alone, no dilogarithm and no analysis — exactly as
`branch_data_of_cubic` does at `x = 1`.

## And the sum over the three roots is pinnable

`exp_branchSum_eq_one` proves `exp (Σⱼ branchTerm x yⱼ) = 1` from **Vieta alone**
— the saddle condition is not needed for the sum, only for the individual terms.
It rests on three products, of which one is new here:

| product | source |
|---|---|
| `∏ⱼ (1 − x·yⱼ) = x` | `prod_one_sub_x_mul` (#4658) |
| `∏ⱼ (x − yⱼ) = x²` | `prod_x_sub` (#4658) |
| `∏ⱼ (1 − yⱼ) = 1` | `prod_one_sub`, **new here** |

That is precisely the `hexp` hypothesis of
`QOU/Archimedean/BranchIntegerPinning.lean`. So along the transport arc the
**sum of the deformed branch integers is pinned to its base-point value** by the
same lemma that pins the transport's own branch integer — given continuity,
which remains the open hypothesis there. At `x = 1` the corpus records
`k = (+1, −1, 0)`, whose sum is `0`.

## Where the logarithms live

This file keeps only the algebra (the Vieta product and the curve identity), over any
commutative ring. The complex-logarithm half (`branchTerm`, `exp_branchTerm`,
`branch_data_of_curve`, `exp_branchSum_eq_one`) sits behind the transcendental boundary in
`QOU.Transcendental.Nuclear.FiveTwoDeformedSaddleBranch`, in this namespace and with these names.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.QBeta.FiveTwoDeformedSaddle

variable {R : Type*} [CommRing R]

/-! ### The third Vieta product -/

/-- **`∏ⱼ (1 − yⱼ) = 1`**, in cleared form.

Hypotheses are Vieta for `x·y³ − (x²+1)·y² + (x²+x+1)·y − x = 0`, matching
`prod_one_sub_x_mul` and `prod_x_sub` in `FiveTwoCyclotomicBloch`. The cleared
statement `x·∏ = x` is what survives over a general `CommRing`; divide by `x` in
a field. -/
theorem prod_one_sub (x y₁ y₂ y₃ : R)
    (h₁ : x * (y₁ + y₂ + y₃) = x ^ 2 + 1)
    (h₂ : x * (y₁ * y₂ + y₁ * y₃ + y₂ * y₃) = x ^ 2 + x + 1)
    (h₃ : y₁ * y₂ * y₃ = 1) :
    x * ((1 - y₁) * (1 - y₂) * (1 - y₃)) = x := by
  linear_combination -h₁ + h₂ - x * h₃

/-- The field form of `prod_one_sub`. -/
theorem prod_one_sub' {K : Type*} [Field K] (x y₁ y₂ y₃ : K) (hx : x ≠ 0)
    (h₁ : x * (y₁ + y₂ + y₃) = x ^ 2 + 1)
    (h₂ : x * (y₁ * y₂ + y₁ * y₃ + y₂ * y₃) = x ^ 2 + x + 1)
    (h₃ : y₁ * y₂ * y₃ = 1) :
    (1 - y₁) * (1 - y₂) * (1 - y₃) = 1 :=
  mul_left_cancel₀ hx (by rw [prod_one_sub x y₁ y₂ y₃ h₁ h₂ h₃, mul_one])

/-! ### The saddle condition is the curve -/

/-- GGM's deformed 5₂ curve. -/
def curve (x y : R) : R := x * y ^ 3 - (x ^ 2 + 1) * y ^ 2 + (x ^ 2 + x + 1) * y - x

/-- **The deformed saddle condition is identically the curve.**

`x·y² = (1−y)(1−x·y)(x−y)` is `y² = (1−y)(1−xy)(1−y/x)` with the `1/x` cleared,
i.e. `∂V/∂y = 0` after exponentiating. It holds exactly on the curve — over any
commutative ring, with no positivity, ordering, or analysis. -/
theorem deformed_saddle_iff_curve (x y : R) :
    x * y ^ 2 = (1 - y) * (1 - x * y) * (x - y) ↔ curve x y = 0 := by
  unfold curve
  constructor <;> intro h <;> linear_combination h

/-- At `x = 1` this is the corpus's `y² = (1−y)³`
(`FiveTwoSaddleSumRule.cubic_iff_sq_eq_cube`). -/
theorem saddle_at_one (y : R) :
    (1 : R) * y ^ 2 = (1 - y) * (1 - 1 * y) * (1 - y) ↔ y ^ 2 = (1 - y) ^ 3 := by
  constructor <;> intro h <;> linear_combination h

/-- …and at `x = 1` the curve is the 5₂ cubic. -/
theorem curve_at_one (y : R) : curve 1 y = y ^ 3 - 2 * y ^ 2 + 3 * y - 1 := by
  unfold curve; ring

end QOU.QBeta.FiveTwoDeformedSaddle
