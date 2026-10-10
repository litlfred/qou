/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.OcneanuWeightTwoRowNonzero
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.Field.Power
import Mathlib.Algebra.Order.BigOperators.Ring.Finset

/-!
# The Ocneanu weight is POSITIVE on the at-most-two-row shapes, for every `q > 0`, `q ≠ 1`

`ocneanuWeight_conventionD_eq_zero_of_three_rows` kills every shape with a third row at
convention `D` (`z = q³/(q²+1)`), and `ocneanuWeight_conventionD_ne_zero_of_two_rows` shows the
remaining weights are nonzero.  This file upgrades "nonzero" to **strictly positive** over an
ordered field, for every `q > 0` with `q ≠ 1`.

## The computation

By `ocneanuNumFactor_conventionD` the numerator factor of a cell `(i, j)` is
`q^{2i}·((q²)^{j+2−i} − 1)/(q²+1)`, and the denominator factor is `(q²)^{h} − 1` with `h ≥ 1` the
hook length.  On a shape with at most two rows `i ≤ 1`, so the exponent `j + 2 − i` is at least `1`.
Both `(q²)^m − 1` and `(q²)^h − 1` then have the sign of `q² − 1`: positive for `q > 1`, negative for
`0 < q < 1`.  Each cell therefore contributes a positive ratio, and so does their product.

## Scope

* **`q = 1` is excluded, and it must be.**  There every denominator factor is `0`, so the closed
  form `ocneanuWeight` is `x / 0`, which Lean evaluates to `0`.  The classical weight at `q = 1` is
  the limit of this formula, not its value, and nothing here says anything about it.
* **This is positivity of the weights, not of a state.**  That the Markov trace on `H_n(q)` is a
  positive functional for the `*`-structure `σᵢ* = σᵢ` is Jones's Temperley–Lieb positivity for loop
  value `[2]_q = q + q⁻¹ ≥ 2` (Jones 1983/1985, `[jones1985]`), which is cited, not proved, here.
  The weights being positive is the per-block shadow of that statement: on each surviving
  Wedderburn block the trace is a positive multiple of the matrix trace.
* **The general-`n` Markov property of `ocneanuWeight` is still open** (see `OcneanuWeight`).  This
  file proves a sign, not that the weights are the Markov trace at general `n`.

## Base ring (§7c)

The statement needs an ordering, so it is over `[Field R] [LinearOrder R] [IsStrictOrderedRing R]`,
not `ℝ`; it mentions no archimedean construct.

LaTeX label: `def:ocneanu-weight`
-/

namespace QOU.SchurWeyl

open YoungDiagram

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **`xᵐ − 1` and `xᵏ − 1` have the same sign** for `x > 0`, `x ≠ 1`, `m, k ≥ 1`, so their ratio
is positive. -/
theorem pow_sub_one_div_pow_sub_one_pos {x : R} (hx : 0 < x) (hx1 : x ≠ 1) {m k : ℕ}
    (hm : m ≠ 0) (hk : k ≠ 0) : 0 < (x ^ m - 1) / (x ^ k - 1) := by
  rcases lt_or_gt_of_ne hx1 with h | h
  · apply div_pos_of_neg_of_neg
    · have := pow_lt_one₀ hx.le h hm; linarith
    · have := pow_lt_one₀ hx.le h hk; linarith
  · apply div_pos
    · have := one_lt_pow₀ h hm; linarith
    · have := one_lt_pow₀ h hk; linarith

/-- **The Ocneanu weight is strictly positive on the at-most-two-row shapes** at convention `D`,
for every `q > 0` with `q ≠ 1`.

Together with `ocneanuWeight_conventionD_eq_zero_of_three_rows`, the convention-`D` weights are
nonnegative everywhere on `q > 0, q ≠ 1`, with support exactly the shapes of at most two rows. -/
theorem ocneanuWeight_conventionD_pos_of_two_rows (q : R) (hq : 0 < q) (hq1 : q ≠ 1)
    (mu : YoungDiagram) (h : mu.rowLen 2 = 0) :
    0 < ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) mu := by
  have hq21 : (0 : R) < q ^ 2 + 1 := by positivity
  have hx : (0 : R) < q ^ 2 := by positivity
  have hx1 : q ^ 2 ≠ (1 : R) := by
    intro h2
    have : (q - 1) * (q + 1) = 0 := by linear_combination h2
    rcases mul_eq_zero.mp this with h3 | h3
    · exact hq1 (by linarith)
    · linarith
  rw [ocneanuWeight, ← Finset.prod_div_distrib]
  refine Finset.prod_pos fun c hc => ?_
  have hi : c.1 ≤ 1 := row_le_one_of_rowLen_two_eq_zero h hc
  rw [ocneanuNumFactor_conventionD q hq21.ne' c.1 c.2]
  have hsplit : q ^ (2 * c.2 + 4) - q ^ (2 * c.1)
      = q ^ (2 * c.1) * ((q ^ 2) ^ (c.2 + 2 - c.1) - 1) := by
    rw [mul_sub, mul_one, ← pow_mul, ← pow_add]
    congr 2
    omega
  have hden : q ^ (2 * hookLength mu c) - 1 = (q ^ 2) ^ hookLength mu c - 1 := by
    rw [pow_mul]
  have key : q ^ (2 * c.1) * ((q ^ 2) ^ (c.2 + 2 - c.1) - 1) / (q ^ 2 + 1)
        / ((q ^ 2) ^ hookLength mu c - 1)
      = q ^ (2 * c.1) / (q ^ 2 + 1)
        * (((q ^ 2) ^ (c.2 + 2 - c.1) - 1) / ((q ^ 2) ^ hookLength mu c - 1)) := by
    ring
  rw [hsplit, hden, key]
  exact mul_pos (div_pos (pow_pos hq _) hq21)
    (pow_sub_one_div_pow_sub_one_pos hx hx1 (by omega) (hookLength_pos hc).ne')

end QOU.SchurWeyl
