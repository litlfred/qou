/-
  `logSinc` near `0` — and why `qou-mlgp` (A) does NOT need it to be `C⁴` there.

  A CORRECTION TO THE PREVIOUS ROUND.  `CompositeEulerMaclaurin.lean`'s header
  says the last thing standing between this corpus and (A) is exhibiting the
  analytic extension of `logSinc` at `0`, because the composite rule was applied
  on `[0, θ]` and `logSinc x = log(sin x) − log x` is not differentiable at `0`
  as literally written.  That framing was wrong — not about the mathematics, but
  about what (A) needs.  The requirement is an artefact of putting the left
  endpoint at `0`, and it disappears if the grid starts at `h` instead.

  APPLY THE COMPOSITE RULE ON `[h, θ]`, NOT `[0, θ]`.  The Kashaev sum is
  `∑_{j=1}^{k} logSinc(jh)` — it starts at `j = 1`, so `[h, θ]` with `k−1` cells
  is the natural interval anyway, and it never touches `0`.  What that costs is
  three boundary terms at the left end:

      (1/h)·∫_0^h logSinc,      ½·logSinc(h),      (h/12)·logSinc′(h)

  and ALL THREE ARE `O(h²) = O(1/N²)` — one order BELOW the `O(1/N)` term (A) is
  chasing.  Measured at `N = 100…800` they are `≈ −0.55/N²`, `−0.82/N²`,
  `−0.27/N²`.  So they do not enter the answer at all.

  (They are also not independently interesting: their leading parts cancel
  exactly.  With `logSinc x = −x²/6 + O(x⁴)` the three contribute
  `−h²/18 + h²/12 − h²/36 = 0`, which is why the `[0,θ]` and `[h,θ]` forms of
  the expansion agree to `O(h⁴)`.)

  WHAT IS ACTUALLY NEEDED, THEN, is not `C⁴` at `0` but two elementary bounds
  near `0`, and this file proves the first of them:

      −x²/3  ≤  logSinc x  ≤  0        for  0 < x ≤ 1

  from `Real.sin_lt`, `Real.sin_gt_sub_cube` and `Real.log_le_sub_one_of_pos`.
  No analytic extension, no power series, no removable-singularity machinery.

  STILL NEEDED for the assembly: `|logSinc′ x| ≤ x` on `(0,1]`, equivalently
  `|x cos x − sin x| ≤ x²·sin x`.  Both halves are one-line monotonicity
  arguments (`u = sin x − x cos x` has `u(0) = 0`, `u′ = x sin x > 0`;
  `v = x² sin x − sin x + x cos x` has `v(0) = 0`, `v′ = x(sin x + x cos x) > 0`
  on `(0,1]`), but they are not formalised here.

  -- Ref: [manuscript] QOU/Knot/KashaevEndpointSplit.lean          (defines logSinc)
  -- Ref: [manuscript] QOU/MathlibExt/CompositeEulerMaclaurin.lean (the rule applied)
-/
import QOU.Knot.KashaevEndpointSplit

namespace QOU.Knot.FigureEightVolume

open Real

/-- `logSinc x ≤ 0` on `(0, π)` — immediate from `sin x < x`. -/
theorem logSinc_nonpos {x : ℝ} (hx : 0 < x) (hxpi : x < π) : logSinc x ≤ 0 := by
  have hsin : 0 < Real.sin x := Real.sin_pos_of_pos_of_lt_pi hx hxpi
  have hlt : Real.sin x < x := Real.sin_lt hx
  have := Real.log_lt_log hsin hlt
  simp only [logSinc]
  linarith

/-- **`−x²/3 ≤ logSinc x` on `(0, 1]`.**

`sin x > x − x³/4` gives `sin x / x > 1 − x²/4 ≥ 3/4`, and
`log t ≥ 1 − 1/t = (t−1)/t` (the `log y ≤ y − 1` bound at `y = 1/t`) turns that
into `logSinc x ≥ −(x²/4)/(3/4) = −x²/3`. -/
theorem neg_sq_div_three_le_logSinc {x : ℝ} (hx : 0 < x) (hx1 : x ≤ 1) :
    -(x ^ 2 / 3) ≤ logSinc x := by
  have hxpi : x < π := lt_of_le_of_lt hx1 (by linarith [Real.two_le_pi])
  have hsin : 0 < Real.sin x := Real.sin_pos_of_pos_of_lt_pi hx hxpi
  set t : ℝ := Real.sin x / x with ht
  have htpos : 0 < t := by rw [ht]; positivity
  -- `t > 1 − x²/4 ≥ 3/4`
  have hcube : x - x ^ 3 / 4 < Real.sin x := Real.sin_gt_sub_cube hx hx1
  have htlb : 1 - x ^ 2 / 4 < t := by
    rw [ht, lt_div_iff₀ hx]
    nlinarith
  have ht34 : (3 : ℝ) / 4 ≤ t := by nlinarith [sq_nonneg x, hx1, hx]
  -- `log t = −log (1/t) ≥ −(1/t − 1)`
  have hinv : Real.log (1 / t) ≤ 1 / t - 1 :=
    Real.log_le_sub_one_of_pos (by positivity)
  have hlogneg : Real.log (1 / t) = -Real.log t := by
    rw [one_div, Real.log_inv]
  have hlow : 1 - 1 / t ≤ Real.log t := by
    rw [hlogneg] at hinv; linarith
  -- `1 − 1/t = (t−1)/t ≥ −(x²/4)/(3/4) = −x²/3`
  have hfrac : -(x ^ 2 / 3) ≤ 1 - 1 / t := by
    have hx2 : x ^ 2 ≤ 1 := by nlinarith
    have hpos : (0 : ℝ) < 1 + x ^ 2 / 3 := by positivity
    have hstep : (1 + x ^ 2 / 3) * (1 - x ^ 2 / 4) ≤ (1 + x ^ 2 / 3) * t :=
      mul_le_mul_of_nonneg_left (le_of_lt htlb) hpos.le
    have hbase : (1 : ℝ) ≤ (1 + x ^ 2 / 3) * (1 - x ^ 2 / 4) := by
      nlinarith [mul_nonneg (sq_nonneg x) (by linarith : (0 : ℝ) ≤ 1 - x ^ 2)]
    have h1t : 1 / t ≤ 1 + x ^ 2 / 3 := by
      rw [div_le_iff₀ htpos]
      linarith
    linarith
  -- and `logSinc x = log t`
  have hsplit : logSinc x = Real.log t := by
    simp only [logSinc, ht]
    rw [Real.log_div (ne_of_gt hsin) (ne_of_gt hx)]
  rw [hsplit]
  linarith

/-- The two-sided statement, packaged: `logSinc` is `O(x²)` near `0`, which is
all `qou-mlgp` (A) needs from the left endpoint. -/
theorem abs_logSinc_le {x : ℝ} (hx : 0 < x) (hx1 : x ≤ 1) :
    |logSinc x| ≤ x ^ 2 / 3 := by
  have hxpi : x < π := lt_of_le_of_lt hx1 (by linarith [Real.two_le_pi])
  rw [abs_le]
  exact ⟨neg_sq_div_three_le_logSinc hx hx1,
    le_trans (logSinc_nonpos hx hxpi) (by positivity)⟩

end QOU.Knot.FigureEightVolume
