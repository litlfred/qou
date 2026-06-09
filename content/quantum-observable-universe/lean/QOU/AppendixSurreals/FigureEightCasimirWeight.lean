/-!
# QOU.AppendixSurreals.FigureEightCasimirWeight — the 3/4 is exact algebra

Supporting lemmas for the **first Casimir q-correction** discussion of
[`conj:casimir-epsilon-vacuum`](../../../quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md)
(audit `docs/audits/2026-06-01-casimir-first-qcorrection-figure8.md`).

The leading `1/d⁴` Casimir term is q-free (disjoint unknots, the n-stable
bare count). The **first** q-correction is carried by the first hyperbolic
braided mode — the figure-eight knot `4_1` — whose substrate weight is its
Jones polynomial

  `J_{4_1}(q) = q⁻² − q⁻¹ + 1 − q + q²`   (Lickorish; normalised `J_{4_1}(1) = 1`).

The audit claims `J_{4_1}(q) = 1 + (3/4) h² + O(h⁴)` with `h = q − q⁻¹`.
This file proves the `3/4` is **exact algebra, not a fit**:

  `(4·(J−1) − 3·h²) · (h² + 8 + 4·(q+q⁻¹)) = h⁴`   (exact field identity),

with the remainder denominator `h² + 8 + 4(q+q⁻¹) > 0` for `q > 0`. Hence
`4(J−1) − 3h² = h⁴ / (positive)`, i.e. the `h²` coefficient of `J−1` is
**exactly** `3/4` with an explicit, sign-definite `O(h⁴)` remainder — no
fitting, no free parameter.

The *identification* of `J_{4_1}` as the first-correction weight is the
structural (physical) input documented in the audit; the `3/4` that follows
from that weight is the elementary algebra proved here.

Ref: [lickorish1997] An Introduction to Knot Theory, Springer GTM 175
(Jones polynomial of the figure-eight knot).
-/

import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace QOU.AppendixSurreals

/-- Jones polynomial of the figure-eight knot `4_1`, in the skein
variable `q`, normalised so `jones41 1 = 1`. -/
noncomputable def jones41 (q : ℝ) : ℝ := (q⁻¹) ^ 2 - q⁻¹ + 1 - q + q ^ 2

@[simp] theorem jones41_one : jones41 1 = 1 := by
  unfold jones41; norm_num

/-- `s`-form: `J_{4_1} = (q+q⁻¹)² − (q+q⁻¹) − 1`. -/
theorem jones41_eq_sform (q : ℝ) (hq : q ≠ 0) :
    jones41 q = (q + q⁻¹) ^ 2 - (q + q⁻¹) - 1 := by
  unfold jones41; field_simp; ring

/-- `s² − h² = 4`, with `s = q+q⁻¹`, `h = q−q⁻¹`. -/
theorem sSq_sub_hSq (q : ℝ) (hq : q ≠ 0) :
    (q + q⁻¹) ^ 2 - (q - q⁻¹) ^ 2 = 4 := by
  field_simp; ring

/-- **The 3/4 is exact.** Cleared form of
`J_{4_1} = 1 + (3/4) h² + O(h⁴)`: the residual `4(J−1) − 3h²`, times the
explicit remainder denominator, equals exactly `h⁴`. Proof is `ring` after
clearing `q⁻¹` (needs only `q ≠ 0`) — there is no fitted constant. -/
theorem jones41_three_quarters_cleared (q : ℝ) (hq : q ≠ 0) :
    (4 * (jones41 q - 1) - 3 * (q - q⁻¹) ^ 2) *
        ((q - q⁻¹) ^ 2 + 8 + 4 * (q + q⁻¹))
      = (q - q⁻¹) ^ 4 := by
  unfold jones41; field_simp; ring

/-- The remainder denominator is strictly positive for `q > 0`, so the
`O(h⁴)` remainder `h⁴ / (·)` is genuinely small and sign-definite: the
leading `h²` coefficient of `J_{4_1} − 1` is exactly `3/4`. -/
theorem jones41_remainder_denom_pos (q : ℝ) (hq : 0 < q) :
    0 < (q - q⁻¹) ^ 2 + 8 + 4 * (q + q⁻¹) := by
  have h2 : (0 : ℝ) < q⁻¹ := by positivity
  nlinarith [sq_nonneg (q - q⁻¹), h2, hq]

/-- Division form on `q > 0`: `4(J−1) − 3h² = h⁴ / (positive)`. -/
theorem jones41_three_quarters (q : ℝ) (hq : 0 < q) :
    4 * (jones41 q - 1) - 3 * (q - q⁻¹) ^ 2
      = (q - q⁻¹) ^ 4 / ((q - q⁻¹) ^ 2 + 8 + 4 * (q + q⁻¹)) := by
  have hpos := jones41_remainder_denom_pos q hq
  rw [eq_div_iff (ne_of_gt hpos)]
  exact jones41_three_quarters_cleared q (ne_of_gt hq)

/-- **The result, as a theorem.**  With `h = q − q⁻¹`, the figure-eight Jones
weight expands as
  `J_{4_1}(q) = 1 + (3/4)·h² + R(q)`,
where the remainder `R(q) = h⁴ / (4·(h² + 8 + 4(q+q⁻¹)))` is *exact*, and for
`q > 0` is positive and of order `h⁴` (its denominator `→ 64` as `q → 1`).
The leading coefficient `3/4` is forced by `ring`; it is not a fitted constant.
This is the precise sense in which "`J_{4_1} = 1 + (3/4)h² + O(h⁴)`" holds. -/
theorem jones41_taylor (q : ℝ) (hq : 0 < q) :
    jones41 q
      = 1 + (3 / 4) * (q - q⁻¹) ^ 2
          + (q - q⁻¹) ^ 4 / (4 * ((q - q⁻¹) ^ 2 + 8 + 4 * (q + q⁻¹))) := by
  have hpos := jones41_remainder_denom_pos q hq
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hden : (q - q⁻¹) ^ 2 + 8 + 4 * (q + q⁻¹) ≠ 0 := ne_of_gt hpos
  field_simp
  ring

/-- The remainder in `jones41_taylor` is nonnegative for `q > 0`: the weight
is bounded *below* by its second-order Taylor polynomial `1 + (3/4)h²`. -/
theorem jones41_taylor_remainder_nonneg (q : ℝ) (hq : 0 < q) :
    0 ≤ (q - q⁻¹) ^ 4 / (4 * ((q - q⁻¹) ^ 2 + 8 + 4 * (q + q⁻¹))) := by
  have hpos := jones41_remainder_denom_pos q hq
  have hden : (0 : ℝ) ≤ 4 * ((q - q⁻¹) ^ 2 + 8 + 4 * (q + q⁻¹)) := by linarith
  exact div_nonneg (by positivity) hden

end QOU.AppendixSurreals
