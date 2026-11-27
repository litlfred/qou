/-
# `Real.rpow` and `Real.sqrt` helpers

Moved from `MathlibExt/Core.lean` §4 behind the transcendental boundary (owner ruling 2026-11-27,
bean `qou-dk7p`).  Names and namespace are unchanged.
-/
import MathlibExt.Core
import Mathlib.Analysis.SpecialFunctions.Pow.Real

namespace QOU.MathlibExt

/-! ## §4  `Real.rpow` numerical helpers

The `Real.rpow` function is central to several QOU bounds (skein
mass relation, pair-skein decomposition, q-Planck constant), but
`norm_num` does not yet evaluate it on non-integer exponents. The
lemmas below convert the most common QOU pattern
`q^(1/2 : ℝ) + q^(-(1/2) : ℝ)` to `Real.sqrt q + 1 / Real.sqrt q`,
where Mathlib's existing `Real.sqrt`-based numerics apply. -/

/-- `x^(1/2 : ℝ) = Real.sqrt x` (for any real `x`; both sides
    are zero on the negative reals via the rpow / sqrt
    conventions).  Symmetric form of Mathlib's
    `Real.sqrt_eq_rpow`.

    Upstream status: this is the `.symm` of Mathlib's `Real.sqrt_eq_rpow`
    (present in the pinned v4.24).  A named `Real.rpow_one_div_two` is
    **not** in the pinned Mathlib (probed 2026-06-26 — `unknown constant`),
    so this local convenience wrapper stays until/unless one lands upstream. -/
theorem Real.rpow_half_eq_sqrt (x : ℝ) :
    x ^ (1/2 : ℝ) = Real.sqrt x :=
  (Real.sqrt_eq_rpow x).symm

/-- For `x > 0`, `x^(-(1/2) : ℝ) = 1 / Real.sqrt x`. -/
theorem Real.rpow_neg_half_eq (x : ℝ) (hx : 0 < x) :
    x ^ (-(1/2 : ℝ)) = 1 / Real.sqrt x := by
  rw [Real.rpow_neg hx.le, Real.rpow_half_eq_sqrt x, one_div]

/-- The QOU "denominator" `q^(1/2) + q^(-1/2)` equals
    `sqrt q + 1 / sqrt q`. -/
theorem q_half_denom (q : ℝ) (hq : 0 < q) :
    q ^ (1/2 : ℝ) + q ^ (-(1/2 : ℝ)) = Real.sqrt q + 1 / Real.sqrt q := by
  rw [Real.rpow_half_eq_sqrt q, Real.rpow_neg_half_eq q hq]

/-- For `x > 0`, the function `t ↦ t + 1/t` evaluated at
    `t = Real.sqrt x` is non-negative and admits a clean
    cross-multiplication identity:
    `(Real.sqrt x) · ((Real.sqrt x) + 1 / (Real.sqrt x))
       = x + 1`,
    i.e. multiplying the QOU half-denominator by `sqrt x` clears
    the inverse, yielding a closed-form polynomial in `x`. -/
theorem sqrt_mul_half_denom (x : ℝ) (hx : 0 < x) :
    Real.sqrt x * (Real.sqrt x + 1 / Real.sqrt x) = x + 1 := by
  have hsqrt_pos : 0 < Real.sqrt x := Real.sqrt_pos.mpr hx
  have hsqrt_ne : Real.sqrt x ≠ 0 := ne_of_gt hsqrt_pos
  have hsq : Real.sqrt x * Real.sqrt x = x :=
    Real.mul_self_sqrt hx.le
  field_simp
  linarith [hsq]

/-- **Bracketing helper**: if `a > 0` and `a^2 < x`, then
    `a < Real.sqrt x`. Lifted from `Real.sqrt_lt_sqrt` with the
    `Real.sqrt_sq` simplification baked in. -/
theorem Real.lt_sqrt_of_sq_lt (a x : ℝ) (ha : 0 ≤ a) (hsq : a^2 < x) :
    a < Real.sqrt x := by
  have hax : a = Real.sqrt (a^2) := by
    rw [Real.sqrt_sq ha]
  rw [hax]
  exact Real.sqrt_lt_sqrt (by positivity) hsq

/-- **Bracketing helper**: if `0 ≤ x` and `x < a^2`, then
    `Real.sqrt x < a` (assuming `0 ≤ a`). -/
theorem Real.sqrt_lt_of_lt_sq (a x : ℝ) (ha : 0 ≤ a) (hx : 0 ≤ x)
    (hsq : x < a^2) :
    Real.sqrt x < a := by
  have hax : a = Real.sqrt (a^2) := by
    rw [Real.sqrt_sq ha]
  rw [hax]
  exact Real.sqrt_lt_sqrt hx hsq

/-- **AM-GM for `√x + 1/√x`**: for `x > 0`, `√x + 1/√x ≥ 2`.

    Direct corollary of `add_inv_ge_two` applied to `t := √x`. -/
theorem sqrt_add_inv_ge_two (x : ℝ) (hx : 0 < x) :
    Real.sqrt x + 1 / Real.sqrt x ≥ 2 := by
  exact add_inv_ge_two (Real.sqrt x) (Real.sqrt_pos.mpr hx)

end QOU.MathlibExt
