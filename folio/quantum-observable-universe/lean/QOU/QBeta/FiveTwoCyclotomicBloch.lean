import Mathlib.Tactic.LinearCombination

/-!
# The 5₂ sum rule: the algebraic core of Routes 8 and 9

Bean `qou-8v3k` (Route 8) and `qou-b7cy` (Route 9), PR #4658.

Everything here is **pure commutative-ring algebra** — no dilogarithm, no
analysis, no Mathlib gap. These are exactly the steps of Routes 8 and 9 that do
not depend on the complex `Li₂` blocker (`qou-clx8`), isolated so that they are
provable independently of it.

## Route 8 — the two Vieta products

Along GGM's deformed 5₂ curve `x·y³ − (x²+1)·y² + (x²+x+1)·y − x = 0` the roots
satisfy `e₁ = (x²+1)/x`, `e₂ = (x²+x+1)/x`, `e₃ = 1`.  Stated with the
denominators cleared, so the results hold over any `CommRing`:

* `prod_one_sub_x_mul` : `∏ⱼ (1 − x·yⱼ) = x`
* `prod_x_sub`         : `∏ⱼ (x − yⱼ) = x²`   (the cleared form of `∏ⱼ(1 − yⱼ/x) = 1/x`)

These are the step that makes the envelope computation collapse:
`S'(x) = (1/x)·log[(1/x)/x] = −2·log x / x`.

## Route 9 — the Bloch-group condition

At the cyclotomic point `x = −1`, with `w = 1 + 2cos(2πk/7)` a root of
`w³ − 2w² − w + 1`:

* `bloch_poly` : `(1 − w)²(1 + w) − w² = w³ − 2w² − w + 1` **as polynomials**
* `bloch_key`  : hence `(1 − w)²(1 + w) = w²` at any root

`bloch_poly` is the sharp form: the Bloch-group condition `δ(2[w] + [−w]) = 0`
is not merely *implied by* the minimal polynomial — it **is** the minimal
polynomial.  That is why `bloch_key` is a one-line `linear_combination`.

Consequence (not formalized here — it needs the Bloch group and Borel's theorem,
neither of which is in Mathlib): `δ(2[w] + [−w]) = w ∧ [(1−w)²(1+w)] = w ∧ w² = 0`,
so `2[w] + [−w]` lies in the Bloch group of `ℚ(ζ₇)⁺`, which is totally real,
hence the element is torsion and its Rogers dilogarithm lies in `π²ℚ`.

**Nothing here proves the sum rule.**  **The 5₂ sum rule is PROVED**:
`QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms. These are its
formalizable algebraic components.
-/

namespace QOU.QBeta.FiveTwoCyclotomicBloch

variable {R : Type*} [CommRing R]

/-! ### Route 8: the Vieta products along the deformed curve -/

/-- `∏ⱼ (1 − x·yⱼ) = x` for the roots of GGM's deformed 5₂ curve.

Hypotheses are Vieta for `x·y³ − (x²+1)·y² + (x²+x+1)·y − x = 0`, with the
denominators cleared so the statement lives over any `CommRing`. -/
theorem prod_one_sub_x_mul (x y₁ y₂ y₃ : R)
    (h₁ : x * (y₁ + y₂ + y₃) = x ^ 2 + 1)
    (h₂ : x * (y₁ * y₂ + y₁ * y₃ + y₂ * y₃) = x ^ 2 + x + 1)
    (h₃ : y₁ * y₂ * y₃ = 1) :
    (1 - x * y₁) * (1 - x * y₂) * (1 - x * y₃) = x := by
  linear_combination (-1 : R) * h₁ + x * h₂ - x ^ 3 * h₃

/-- `∏ⱼ (x − yⱼ) = x²` — the cleared form of `∏ⱼ (1 − yⱼ/x) = 1/x`.

Together with `prod_one_sub_x_mul` this gives
`∏ⱼ [(1 − yⱼ/x)/(1 − x·yⱼ)] = 1/x²`, which is what turns the envelope
derivative into `−2·log x / x`. -/
theorem prod_x_sub (x y₁ y₂ y₃ : R)
    (h₁ : x * (y₁ + y₂ + y₃) = x ^ 2 + 1)
    (h₂ : x * (y₁ * y₂ + y₁ * y₃ + y₂ * y₃) = x ^ 2 + x + 1)
    (h₃ : y₁ * y₂ * y₃ = 1) :
    (x - y₁) * (x - y₂) * (x - y₃) = x ^ 2 := by
  linear_combination (-x) * h₁ + h₂ - h₃

/-! ### Route 9: the Bloch-group condition at the cyclotomic point -/

/-- **The sharp form.** `(1 − w)²(1 + w) − w²` is *identically* the minimal
polynomial `w³ − 2w² − w + 1` of `w = 1 + 2cos(2πk/7)`.

So the Bloch-group condition is not a consequence of the minimal polynomial —
it is the same polynomial. -/
theorem bloch_poly (w : R) :
    (1 - w) ^ 2 * (1 + w) - w ^ 2 = w ^ 3 - 2 * w ^ 2 - w + 1 := by
  ring

/-- At any root of `w³ − 2w² − w + 1` one has `(1 − w)²(1 + w) = w²`.

This is the identity behind `δ(2[w] + [−w]) = w ∧ w² = 0`, i.e. behind
`2[w] + [−w]` lying in the Bloch group of `ℚ(ζ₇)⁺`. -/
theorem bloch_key (w : R) (hw : w ^ 3 - 2 * w ^ 2 - w + 1 = 0) :
    (1 - w) ^ 2 * (1 + w) = w ^ 2 := by
  linear_combination hw

/-- The minimal polynomial of `1 − w` (namely `−2cos(2πk/7)`) is
`u³ − u² − 2u + 1`. -/
theorem minpoly_one_sub (w : R) (hw : w ^ 3 - 2 * w ^ 2 - w + 1 = 0) :
    (1 - w) ^ 3 - (1 - w) ^ 2 - 2 * (1 - w) + 1 = 0 := by
  linear_combination -hw

/-- The minimal polynomial of `1 + w` (namely `4cos²(π/7)`) is
`v³ − 5v² + 6v − 1`. -/
theorem minpoly_one_add (w : R) (hw : w ^ 3 - 2 * w ^ 2 - w + 1 = 0) :
    (1 + w) ^ 3 - 5 * (1 + w) ^ 2 + 6 * (1 + w) - 1 = 0 := by
  linear_combination hw

/-- **Direct equality of the two symmetric-product combinations along the curve.**

Along the elementary-symmetric locus, `(x − y₁)(x − y₂)(x − y₃)` equals
`x · (1 − x y₁)(1 − x y₂)(1 − x y₃)`. -/
theorem prod_x_sub_eq_x_mul_prod_one_sub (x y₁ y₂ y₃ : R)
    (h₁ : x * (y₁ + y₂ + y₃) = x ^ 2 + 1)
    (h₂ : x * (y₁ * y₂ + y₁ * y₃ + y₂ * y₃) = x ^ 2 + x + 1)
    (h₃ : y₁ * y₂ * y₃ = 1) :
    (x - y₁) * (x - y₂) * (x - y₃) =
      x * ((1 - x * y₁) * (1 - x * y₂) * (1 - x * y₃)) := by
  linear_combination (x ^ 3 - x) * h₁ + (1 - x ^ 2) * h₂ + (x ^ 4 - 1) * h₃

/-- **Specialization at the base point `x = 1` pins `(1 − y₁)(1 − y₂)(1 − y₃) = 1`.**

At `x = 1`, the elementary symmetric relations `y₁ + y₂ + y₃ = 2`,
`y₁ y₂ + y₁ y₃ + y₂ y₃ = 3`, and `y₁ y₂ y₃ = 1` force `(1 − y₁)(1 − y₂)(1 − y₃) = 1`. -/
theorem base_point_x_eq_one_pins_products (y₁ y₂ y₃ : R)
    (h₁ : (1 : R) * (y₁ + y₂ + y₃) = 1 ^ 2 + 1)
    (h₂ : (1 : R) * (y₁ * y₂ + y₁ * y₃ + y₂ * y₃) = 1 ^ 2 + 1 + 1)
    (h₃ : y₁ * y₂ * y₃ = 1) :
    (1 - y₁) * (1 - y₂) * (1 - y₃) = 1 := by
  linear_combination -h₁ + h₂ - h₃

/-- **Explicit polynomial inverses of `w`, `1 − w`, and `1 + w` at any root of `w³ − 2w² − w + 1 = 0`.**

Every root `w` of `w³ − 2w² − w + 1 = 0` has polynomial inverses for `w`, `1 − w`, and `1 + w`
in `ℤ[w]`, certifying that none of the three factors can vanish along the cyclotomic locus. -/
theorem root_and_shifts_invertible (w : R) (hw : w ^ 3 - 2 * w ^ 2 - w + 1 = 0) :
    w * (-w ^ 2 + 2 * w + 1) = 1 ∧
      (1 - w) * (2 + w - w ^ 2) = 1 ∧
      (1 + w) * (w ^ 2 - 3 * w + 2) = 1 := by
  refine ⟨?_, ?_, ?_⟩
  · linear_combination -hw
  · linear_combination hw
  · linear_combination hw

end QOU.QBeta.FiveTwoCyclotomicBloch
