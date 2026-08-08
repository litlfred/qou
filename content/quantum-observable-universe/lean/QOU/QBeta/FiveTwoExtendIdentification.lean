import QOU.QBeta.FiveTwoRogersExtend
import QOU.QBeta.FiveTwoRogersReflection
import QOU.Archimedean.ComplexDilogBridge
import QOU.MathlibExt.ComplexDilogarithmLanden
import QOU.MathlibExt.ComplexDilogarithmBoundary

/-!
# `extend` **is** `Re` of the analytic Rogers `L` — the `x < 0` regime

Bean `qou-rstq` item 4. Route 33 measured the identification at `1e-50` in all
three regimes and named what Lean was missing *per regime*. This file closes the
`x < 0` one, which is the Landen regime, using
`QOU.MathlibExt.landenCombo_ofReal_eq_zero`.

## The statement

    extend (π²/6) rogersL x = Re (cLiTwoExt x + log x · log(1−x) / 2)   for x < 0

The left side is the corpus's **piecewise** extension, built on the real `LiTwo`
(a `tsum`, hence the junk value `0` outside its disc of convergence). The right
side is `Re` of the **analytic** Rogers `L`, principal branches throughout.
`extended_sum` is stated for the left; the level-7 bridge computes with the
right. Identifying them is what item 4 asks for.

## Why Landen is exactly the input

Write `u = x/(x−1)`. For `x < 0` that lands in `(0,1)`, where the series
converges and `cLiTwo_ofReal` bridges `LiTwo` to `cLiTwo`. Two log identities
then do all the bookkeeping:

    log(1−u) = −log(1−x)          because `1 − u = 1/(1−x)`
    log u    = log(−x) − log(1−x) because `u = (−x)/(1−x)`

so that

    rogersL u = Li₂ u − ½·log(−x)·log(1−x) + ½·log(1−x)²

and Landen — `Li₂ x + Li₂ u + ½·log(1−x)² = 0` — replaces `Li₂ u`, leaving

    rogersL u = −Li₂ x − ½·log(−x)·log(1−x) = −Re L(x)

since `Re log x = log(−x)` for `x < 0` (the `iπ` in `log x` meets a *real*
`log(1−x)`, so it contributes nothing to the real part). Then
`extend x = −rogersL u = Re L(x)`.

The `iπ` not contributing is worth stating rather than passing over: it is the
same `−t`-on-log's-cut phenomenon that produced corrections 5 and 6 in the
transport lane. Here it is harmless, and *because* the partner factor is real —
not because the cut was avoided.

## Scope

This closes one of the two open regimes. The **inversion** regime (`x > 1`)
is untouched and remains the sharper: `x > 1` lies *on* `cLiTwoExt`'s cut, so it
needs a genuine boundary value rather than a constant of integration. Exactly one
of the six arguments `extended_sum` uses lives there — `w₁ = 2.24698` — and it
cannot be avoided.

With this file, the identification is proved for **five of those six
arguments**: the three negative ones here, and the two in `[0,1]` where
`extend` is the identity and `cLiTwo_ofReal` already bridges. Item 4 is **not**
closed; it is reduced to a single argument in a single regime.

**The 5₂ sum rule remains verified to 80 dps, unproved.**
-/

namespace QOU.QBeta.FiveTwoExtendIdentification

open QOU.MathlibExt QOU.Archimedean QOU.QBeta.FiveTwoRogersExtend
open QOU.QBeta.FiveTwoRogersReflection

/-- The **analytic** Rogers `L`, principal branches. -/
noncomputable def cRogersL (z : ℂ) : ℂ :=
  cLiTwoExt z + Complex.log z * Complex.log (1 - z) / 2

/-- For `x < 0` the Landen argument lands strictly inside `(0,1)`. -/
theorem landenArg_mem_Ioo {x : ℝ} (hx : x < 0) : 0 < x / (x - 1) ∧ x / (x - 1) < 1 := by
  have hden : x - 1 < 0 := by linarith
  constructor
  · exact div_pos_of_neg_of_neg hx hden
  · rw [div_lt_one_of_neg hden]; linarith

/-- `1 − x/(x−1) = 1/(1−x)`. -/
theorem one_sub_landenArg {x : ℝ} (hx : x < 0) : 1 - x / (x - 1) = 1 / (1 - x) := by
  have hden : x - 1 ≠ 0 := by intro h; linarith
  have hden' : (1 : ℝ) - x ≠ 0 := by intro h; linarith
  field_simp
  ring

/-- `x/(x−1) = (−x)/(1−x)`. -/
theorem landenArg_eq {x : ℝ} (hx : x < 0) : x / (x - 1) = (-x) / (1 - x) := by
  have hden : x - 1 ≠ 0 := by intro h; linarith
  have hden' : (1 : ℝ) - x ≠ 0 := by intro h; linarith
  field_simp
  ring

/-- **`LiTwo` on `(0,1)` is `Re` of the continuation.** The corpus's `LiTwo` is a
`tsum`; inside the disc it agrees with `cLiTwo`, which agrees with `cLiTwoExt`. -/
theorem liTwo_eq_re_cLiTwoExt {u : ℝ} (h0 : 0 < u) (h1 : u < 1) :
    QOU.QPochhammer.LiTwo u = (cLiTwoExt (u : ℂ)).re := by
  have hnorm : ‖(u : ℂ)‖ < 1 := by
    simpa [Complex.norm_real, Real.norm_eq_abs, abs_of_pos h0] using h1
  rw [cLiTwoExt_eq_cLiTwo hnorm, cLiTwo_ofReal, Complex.ofReal_re]

/-- **The real part of `log x · log(1−x)` for `x < 0`.** The `iπ` in `log x`
meets a *real* `log(1−x)`, so it drops out of the real part — harmlessly, and
because the partner is real, not because the cut was avoided. -/
theorem re_log_mul_log_one_sub {x : ℝ} (hx : x < 0) :
    (Complex.log (x : ℂ) * Complex.log (1 - (x : ℂ))).re
      = Real.log (-x) * Real.log (1 - x) := by
  have h1x : (0 : ℝ) < 1 - x := by linarith
  have hcast : (1 : ℂ) - (x : ℂ) = (((1 - x : ℝ)) : ℂ) := by push_cast; ring
  rw [hcast, ← Complex.ofReal_log h1x.le, mul_comm, Complex.re_ofReal_mul,
    Complex.log_re, Complex.norm_real, Real.norm_eq_abs, abs_of_neg hx]
  ring

/-- `Re` of the analytic Rogers `L` at a negative real, in real terms. -/
theorem re_cRogersL_of_neg {x : ℝ} (hx : x < 0) :
    (cRogersL (x : ℂ)).re
      = (cLiTwoExt (x : ℂ)).re + Real.log (-x) * Real.log (1 - x) / 2 := by
  have hhalf : ∀ w : ℂ, w / 2 = ((((1 : ℝ) / 2) : ℝ) : ℂ) * w := by
    intro w; push_cast; ring
  rw [cRogersL, Complex.add_re, hhalf, Complex.re_ofReal_mul,
    re_log_mul_log_one_sub hx]
  ring

/-- **`extend` IS `Re` of the analytic Rogers `L`, on `x < 0`.**

The corpus's piecewise extension and the analytic function agree on the whole
negative axis. Landen (`landenCombo_ofReal_eq_zero`) is the only analytic input;
everything else is log bookkeeping. -/
theorem extend_eq_re_cRogersL_of_neg {x : ℝ} (hx : x < 0) :
    extend (Real.pi ^ 2 / 6) rogersL x = (cRogersL (x : ℂ)).re := by
  obtain ⟨hu0, hu1⟩ := landenArg_mem_Ioo hx
  set u : ℝ := x / (x - 1) with hu
  have h1x : (0 : ℝ) < 1 - x := by linarith
  have hnegx : (0 : ℝ) < -x := by linarith
  -- the two log identities
  have hlog1u : Real.log (1 - u) = -Real.log (1 - x) := by
    rw [hu, one_sub_landenArg hx, one_div, Real.log_inv]
  have hlogu : Real.log u = Real.log (-x) - Real.log (1 - x) := by
    rw [hu, landenArg_eq hx, Real.log_div (by linarith) (by linarith)]
  -- Landen, with real parts taken
  have hlanden := landenCombo_ofReal_eq_zero hx
  rw [landenCombo] at hlanden
  have hcast : (x : ℂ) / ((x : ℂ) - 1) = (u : ℂ) := by
    rw [hu]; push_cast; ring
  rw [hcast] at hlanden
  have hre := congrArg Complex.re hlanden
  simp only [Complex.add_re, Complex.zero_re] at hre
  -- `log (1 - x)` is real, so its square contributes only its real part
  have hcast1 : (1 : ℂ) - (x : ℂ) = (((1 - x : ℝ)) : ℂ) := by push_cast; ring
  have hsq : (Complex.log (1 - (x : ℂ)) ^ 2 / 2).re = Real.log (1 - x) ^ 2 / 2 := by
    rw [hcast1, ← Complex.ofReal_log h1x.le]
    norm_cast
  rw [hsq, ← liTwo_eq_re_cLiTwoExt hu0 hu1] at hre
  -- assemble: linear in the atoms `LiTwo u`, `(cLiTwoExt x).re`,
  -- `log(1−x)²` and `log(−x)·log(1−x)`, so `linear_combination` closes it
  rw [extend_of_neg _ _ hx, ← hu, rogersL, hlogu, hlog1u, re_cRogersL_of_neg hx]
  linear_combination -hre

end QOU.QBeta.FiveTwoExtendIdentification
