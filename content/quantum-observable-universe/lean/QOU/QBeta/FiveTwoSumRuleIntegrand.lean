/-
# The 5₂ sum-rule integrand: Vieta, the reciprocal cubic, and its positivity

The 2026-08-06 restatement (bean `qou-0yqu`, Route 5) rewrites the 5₂ saddle
sum rule with no dilogarithm:

    A = Σⱼ Li₂(yⱼ) = −∫₀¹ log(1 − 2z + 3z² − z³) / z  dz

This file proves the **algebraic and positivity skeleton** of that chain,
sorry-free. It does *not* prove the sum rule; see "Scope" below.

## The crux, and why it matters

The reciprocal cubic factors as

    1 − 2z + 3z² − z³ = (1 − z)³ + z                    `recipCubic_eq`

from which positivity on `[0,1]` is immediate (`recipCubic_pos`): both
summands are non-negative there and they never vanish together.

That positivity is the whole reason the restatement is worth having. The
defining series `Σₙ pₙ/n²` **diverges** — `|y₁| = 1.52 > 1` — which is what
made analytic continuation of `Li₂` to `|z| > 1` look mandatory (bean
`qou-gkco`). But the *integral* is over a region where the integrand is
regular, so it converges anyway. No complex dilogarithm, no branch cut.

## Scope — what is proved here and what is not

**Proved, sorry-free, over a generic `CommRing` where possible (§7c):**

* `prod_one_sub_mul_eq` — Vieta: `∏ⱼ(1 − yⱼz) = 1 − 2z + 3z² − z³`;
* `recipCubic_eq` — `1 − 2z + 3z² − z³ = (1−z)³ + z`;
* `recipCubic_pos` — hence `0 < 1 − 2z + 3z² − z³` on `[0,1]` (over `ℝ`);
* `pow_succ_rec` / `powerSum_rec` — the power sums obey the cubic's recurrence,
  which is why `pₙ ∈ ℤ` and the generating function is the reciprocal cubic.

**NOT proved here** (and not stubbed — no `sorry`, no axiom):

* that the integral equals `A` (needs `∫₀¹ log(1−yz)/z = −Li₂(y)`);
* the closed-form evaluation of the integral, i.e. the sum rule itself. That
  remains **verified to 80 dps, unproved**; routes 1–4 in `qou-0yqu` are dead
  and Route 5 is a restatement, not a solution.

-- Ref: [manuscript] bean qou-0yqu Route 5; docs/coordination/1ppq-qbeta.md
-/
import Mathlib.Analysis.SpecialFunctions.Complex.Log

namespace QOU.QBeta.FiveTwo

open Complex

/-! ### Vieta: the reciprocal cubic is the product over the roots -/

/-- `∏ⱼ (1 − yⱼ z) = 1 − 2z + 3z² − z³` for any three ring elements with the
5₂ cubic's elementary symmetric functions `e₁ = 2`, `e₂ = 3`, `e₃ = 1`.

This is the generating-function step: it is what makes the power sums
`pₙ = Σⱼ yⱼⁿ` integers and identifies `Σₙ pₙzⁿ/n` with `−log` of this cubic. -/
theorem prod_one_sub_mul_eq {R : Type*} [CommRing R] {y₁ y₂ y₃ : R}
    (e1 : y₁ + y₂ + y₃ = 2) (e2 : y₁ * y₂ + y₁ * y₃ + y₂ * y₃ = 3)
    (e3 : y₁ * y₂ * y₃ = 1) (z : R) :
    (1 - y₁ * z) * (1 - y₂ * z) * (1 - y₃ * z) = 1 - 2 * z + 3 * z ^ 2 - z ^ 3 := by
  linear_combination (-z) * e1 + z ^ 2 * e2 + (-z ^ 3) * e3

/-! ### The crux: the reciprocal cubic is `(1−z)³ + z` -/

/-- `1 − 2z + 3z² − z³ = (1 − z)³ + z`, over any commutative ring.

A one-line `ring` identity, but it is the load-bearing one: it exhibits the
integrand as a sum of two pieces that are separately non-negative on `[0,1]`. -/
theorem recipCubic_eq {R : Type*} [CommRing R] (z : R) :
    1 - 2 * z + 3 * z ^ 2 - z ^ 3 = (1 - z) ^ 3 + z := by ring

/-- **The integrand never vanishes on `[0,1]`.**

Immediate from `recipCubic_eq`: on `[0,1]` both `(1−z)³` and `z` are
non-negative, and at `z = 0` the first is `1`.

This is what makes `∫₀¹ log(1 − 2z + 3z² − z³)/z dz` a convergent *real*
integral, even though the series defining `Σⱼ Li₂(yⱼ)` diverges because
`|y₁| = 1.52 > 1`. It is the technical content behind "Route 5 bypasses the
complex-`Li₂` continuation". -/
theorem recipCubic_pos {z : ℝ} (h0 : 0 ≤ z) (h1 : z ≤ 1) :
    0 < 1 - 2 * z + 3 * z ^ 2 - z ^ 3 := by
  rw [recipCubic_eq]
  have hc : (0 : ℝ) ≤ (1 - z) ^ 3 := pow_nonneg (by linarith) 3
  rcases eq_or_lt_of_le h0 with hz | hz
  · rw [← hz]; norm_num
  · linarith

/-! ### The power-sum recurrence

Each root satisfies the cubic, so its powers obey the associated linear
recurrence; summing over the roots gives the recurrence for `pₙ = Σⱼ yⱼⁿ`,
which is why those power sums are integers (`3, 2, −2, −7, −6, 7, 25, …`). -/

/-- A single root's powers obey the cubic's recurrence. -/
theorem pow_succ_rec {R : Type*} [CommRing R] {y : R}
    (hy : y ^ 3 = 2 * y ^ 2 - 3 * y + 1) (n : ℕ) :
    y ^ (n + 3) = 2 * y ^ (n + 2) - 3 * y ^ (n + 1) + y ^ n := by
  have h : y ^ (n + 3) = y ^ n * y ^ 3 := by ring
  rw [h, hy]; ring

/-- The power sums `pₙ = y₁ⁿ + y₂ⁿ + y₃ⁿ` obey `pₙ₊₃ = 2pₙ₊₂ − 3pₙ₊₁ + pₙ`. -/
theorem powerSum_rec {R : Type*} [CommRing R] {y₁ y₂ y₃ : R}
    (h1 : y₁ ^ 3 = 2 * y₁ ^ 2 - 3 * y₁ + 1)
    (h2 : y₂ ^ 3 = 2 * y₂ ^ 2 - 3 * y₂ + 1)
    (h3 : y₃ ^ 3 = 2 * y₃ ^ 2 - 3 * y₃ + 1) (n : ℕ) :
    y₁ ^ (n + 3) + y₂ ^ (n + 3) + y₃ ^ (n + 3)
      = 2 * (y₁ ^ (n + 2) + y₂ ^ (n + 2) + y₃ ^ (n + 2))
        - 3 * (y₁ ^ (n + 1) + y₂ ^ (n + 1) + y₃ ^ (n + 1))
        + (y₁ ^ n + y₂ ^ n + y₃ ^ n) := by
  rw [pow_succ_rec h1, pow_succ_rec h2, pow_succ_rec h3]; ring

/-! ### Eliminating the complex roots

The restatement's final step drops `y₁, y₂` entirely in favour of the real
root. Both ingredients are Vieta consequences, given that the two non-real
roots are a conjugate pair. -/

/-- **`y₃·‖y₁‖² = 1`.** With `y₂ = conj y₁`, the product relation `e₃ = 1`
says the real root is the reciprocal of `‖y₁‖²`.

This is what turns `log r` into `−½·log y₃` in the restatement, removing the
modulus of the complex root as independent data. -/
theorem real_root_mul_normSq {y₁ y₃ : ℂ}
    (e3 : y₁ * (starRingEnd ℂ) y₁ * y₃ = 1) :
    y₃ * (Complex.normSq y₁ : ℂ) = 1 := by
  rw [Complex.mul_conj] at e3
  linear_combination e3

/-- **The angle is determined by the real root.** With `y₂ = conj y₁`, Vieta's
`e₁ = 2` gives `2·Re y₁ = 2 − y₃`.

Together with `real_root_mul_normSq` (`‖y₁‖² = 1/y₃`) this yields
`cos θ = (2 − y₃)·√y₃ / 2`, the closed form used in the restatement — so the
whole sum rule depends on the single real algebraic number `y₃`. -/
theorem two_mul_re_eq {y₁ y₃ : ℂ}
    (e1 : y₁ + (starRingEnd ℂ) y₁ + y₃ = 2) :
    2 * (y₁.re : ℂ) = 2 - y₃ := by
  have h : y₁ + (starRingEnd ℂ) y₁ = 2 * (y₁.re : ℂ) := by
    rw [Complex.add_conj]; push_cast; ring
  linear_combination e1 - h

end QOU.QBeta.FiveTwo
