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

  THE DERIVATIVE BOUND is here too: `|logSinc′ x| ≤ x` on `(0,1]`, equivalently
  `|x cos x − sin x| ≤ x²·sin x`.  Both halves are monotonicity arguments from
  `f(0) = 0` and `f′ > 0`:

      u = sin x − x cos x                 u(0) = 0,  u′ = x sin x > 0
      v = x² sin x − sin x + x cos x      v(0) = 0,  v′ = x(sin x + x cos x) > 0

  the first giving `x cos x − sin x < 0` (so the absolute value opens as
  `sin x − x cos x`), the second giving `sin x − x cos x < x² sin x`.

  Note that mere BOUNDEDNESS of `logSinc′` would not do: it gives `O(h)` for the
  `(h/12)·logSinc′(h)` term, the same order as the answer being chased.  What is
  needed is `logSinc′(x) → 0` as `x → 0⁺`, and `|logSinc′ x| ≤ x` is the
  cheapest clean way to say it.

  -- Ref: [manuscript] QOU/Knot/KashaevEndpointSplit.lean          (defines logSinc)
  -- Ref: [manuscript] QOU/MathlibExt/CompositeEulerMaclaurin.lean (the rule applied)
-/
import QOU.Knot.KashaevEndpointSplit
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.Calculus.MeanValue

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

/-! ### The derivative bound `|logSinc′ x| ≤ x` on `(0,1]` -/

/-- `sin x − x·cos x > 0` on `(0,1]`.  From `u(0) = 0` and `u′ = x·sin x > 0`. -/
theorem sin_sub_mul_cos_pos {x : ℝ} (hx : 0 < x) (hx1 : x ≤ 1) :
    0 < Real.sin x - x * Real.cos x := by
  have hderiv : ∀ y : ℝ, HasDerivAt (fun z : ℝ => Real.sin z - z * Real.cos z)
      (y * Real.sin y) y := by
    intro y
    have h := (Real.hasDerivAt_sin y).sub
      ((hasDerivAt_id y).mul (Real.hasDerivAt_cos y))
    convert h using 1
    simp only [id_eq]
    ring
  have hmono : StrictMonoOn (fun z : ℝ => Real.sin z - z * Real.cos z)
      (Set.Icc 0 1) := by
    refine strictMonoOn_of_deriv_pos (convex_Icc 0 1)
      (fun y _ => ((hderiv y).continuousAt).continuousWithinAt) ?_
    intro y hy
    rw [interior_Icc, Set.mem_Ioo] at hy
    rw [(hderiv y).deriv]
    have hs : 0 < Real.sin y :=
      Real.sin_pos_of_pos_of_lt_pi hy.1 (by linarith [Real.two_le_pi, hy.2])
    exact mul_pos hy.1 hs
  have h0 : (0 : ℝ) ∈ Set.Icc (0 : ℝ) 1 := ⟨le_rfl, by norm_num⟩
  have hxm : x ∈ Set.Icc (0 : ℝ) 1 := ⟨hx.le, hx1⟩
  simpa using hmono h0 hxm hx

/-- `sin x − x·cos x < x²·sin x` on `(0,1]`.  From `v(0) = 0` and
`v′ = x(sin x + x cos x) > 0`, using `cos > 0` on `(0,1] ⊆ (0, π/2)`. -/
theorem sin_sub_mul_cos_lt {x : ℝ} (hx : 0 < x) (hx1 : x ≤ 1) :
    Real.sin x - x * Real.cos x < x ^ 2 * Real.sin x := by
  have hderiv : ∀ y : ℝ, HasDerivAt
      (fun z : ℝ => z ^ 2 * Real.sin z - Real.sin z + z * Real.cos z)
      (y * Real.sin y + y ^ 2 * Real.cos y) y := by
    intro y
    have hy2 : HasDerivAt (fun z : ℝ => z ^ 2) (2 * y) y := by
      have h := (hasDerivAt_id y).pow 2; norm_num at h; convert h using 1
    have h := ((hy2.mul (Real.hasDerivAt_sin y)).sub (Real.hasDerivAt_sin y)).add
      ((hasDerivAt_id y).mul (Real.hasDerivAt_cos y))
    convert h using 1
    simp only [id_eq]
    ring
  have hmono : StrictMonoOn
      (fun z : ℝ => z ^ 2 * Real.sin z - Real.sin z + z * Real.cos z)
      (Set.Icc 0 1) := by
    refine strictMonoOn_of_deriv_pos (convex_Icc 0 1)
      (fun y _ => ((hderiv y).continuousAt).continuousWithinAt) ?_
    intro y hy
    rw [interior_Icc, Set.mem_Ioo] at hy
    rw [(hderiv y).deriv]
    have hs : 0 < Real.sin y :=
      Real.sin_pos_of_pos_of_lt_pi hy.1 (by linarith [Real.two_le_pi, hy.2])
    have hc : 0 < Real.cos y :=
      Real.cos_pos_of_mem_Ioo ⟨by linarith [Real.pi_pos, hy.1],
        by linarith [Real.two_le_pi, hy.2]⟩
    have p1 : 0 < y * Real.sin y := mul_pos hy.1 hs
    have p2 : 0 < y ^ 2 * Real.cos y := mul_pos (pow_pos hy.1 2) hc
    linarith
  have h0 : (0 : ℝ) ∈ Set.Icc (0 : ℝ) 1 := ⟨le_rfl, by norm_num⟩
  have hxm : x ∈ Set.Icc (0 : ℝ) 1 := ⟨hx.le, hx1⟩
  have := hmono h0 hxm hx
  simp only at this
  norm_num at this
  linarith

/-- `logSinc′ x = cos x/sin x − 1/x` on `(0, π)`. -/
theorem hasDerivAt_logSinc {x : ℝ} (hx : 0 < x) (hxpi : x < π) :
    HasDerivAt logSinc (Real.cos x / Real.sin x - 1 / x) x := by
  have hsin : 0 < Real.sin x := Real.sin_pos_of_pos_of_lt_pi hx hxpi
  have h1 : HasDerivAt (fun y : ℝ => Real.log (Real.sin y))
      (Real.cos x / Real.sin x) x := (Real.hasDerivAt_sin x).log (ne_of_gt hsin)
  have h2 : HasDerivAt (fun y : ℝ => Real.log y) (1 / x) x := by
    have h := Real.hasDerivAt_log (ne_of_gt hx)
    rwa [← one_div] at h
  exact h1.sub h2

/-- **`|logSinc′ x| ≤ x` on `(0,1]`.**

`logSinc′ x = cos x/sin x − 1/x = (x cos x − sin x)/(x sin x)`, and the two
monotonicity bounds above pin the numerator between `−x² sin x` and `0`. -/
theorem abs_logSinc_deriv_le {x : ℝ} (hx : 0 < x) (hx1 : x ≤ 1) :
    |Real.cos x / Real.sin x - 1 / x| ≤ x := by
  have hxpi : x < π := lt_of_le_of_lt hx1 (by linarith [Real.two_le_pi])
  have hsin : 0 < Real.sin x := Real.sin_pos_of_pos_of_lt_pi hx hxpi
  have hden : 0 < x * Real.sin x := by positivity
  have hrw : Real.cos x / Real.sin x - 1 / x
      = (x * Real.cos x - Real.sin x) / (x * Real.sin x) := by
    field_simp
  rw [hrw, abs_div, abs_of_pos hden]
  rw [div_le_iff₀ hden]
  have hlo := sin_sub_mul_cos_pos hx hx1
  have hhi := sin_sub_mul_cos_lt hx hx1
  rw [abs_of_nonpos (by linarith)]
  nlinarith

end QOU.Knot.FigureEightVolume
