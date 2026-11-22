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

  -- Ref: [leitner2026] QOU/Knot/KashaevEndpointSplit.lean          (defines logSinc)
  -- Ref: [leitner2026] QOU/MathlibExt/CompositeEulerMaclaurin.lean (the rule applied)
-/
import QOU.Knot.KashaevEndpointSplit
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.Calculus.MeanValue
import QOU.MathlibExt.TrapezoidRule
import QOU.MathlibExt.SinCubeBounds
import QOU.MathlibExt.CompositeEulerMaclaurin

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

/-! ### The second derivative, and an honest note on the higher ones

The composite Euler–Maclaurin rule's error over `k` cells is `k·h⁵·sup|g⁗|/720`,
which on the SUM is `k·h⁴·sup|g⁗|/720 ≈ sup|g⁗|/N³`.  So the assembly needs
`sup|logSinc⁗|` on `[h, θ]` to be `o(N²)`.  It is in fact `O(1)`:

    logSinc″   = 1/x² − 1/sin²x                    →  −1/3   as x → 0
    logSinc‴   = 2cos x/sin³x − 2/x³               →   0
    logSinc⁗   = 6/x⁴ − (4cos²x + 2)/sin⁴x         →  −2/15

(all three verified against numerical differentiation).  But each is a
DIFFERENCE OF TWO TERMS THAT INDIVIDUALLY BLOW UP, and the bound depends on the
cancellation: at `N = 100` the crude `6/h⁴` is `6.2·10⁶` while the true value is
`0.1335` — a factor of `5·10⁷`.  Feeding the crude bound into the composite rule
gives an error of `O(N)`, i.e. no theorem at all.

So proving `sup|logSinc⁗| = O(1)` is NOT bookkeeping; it needs `sin` and `cos`
expansions carried to eighth order with explicit remainders, and an earlier note
in this corpus that called the interior bound "unglamorous work" understated it.
What IS elementary is the second derivative, which is what the trapezoid-remainder
form of the argument needs, and it is proved below from the same two `sin`
bounds used above.
-/

/-- `logSinc″ x = 1/x² − 1/sin²x` on `(0, π)`. -/
theorem hasDerivAt_logSinc_deriv {x : ℝ} (hx : 0 < x) (hxpi : x < π) :
    HasDerivAt (fun y : ℝ => Real.cos y / Real.sin y - 1 / y)
      (1 / x ^ 2 - 1 / Real.sin x ^ 2) x := by
  have hsin : 0 < Real.sin x := Real.sin_pos_of_pos_of_lt_pi hx hxpi
  have h1 := QOU.MathlibExt.hasDerivAt_cos_div_sin (ne_of_gt hsin)
  have h2 : HasDerivAt (fun y : ℝ => 1 / y) (-(1 / x ^ 2)) x := by
    simpa [one_div] using hasDerivAt_inv (ne_of_gt hx)
  have := h1.sub h2
  convert this using 1
  ring

/-- **`|logSinc″ x| ≤ 1` on `(0,1]`.**

`logSinc″ x = (sin²x − x²)/(x²sin²x)`, and `sin x < x`, `sin x > x − x³/4` give
`x² − sin²x ≤ x⁴/2` and `x²sin²x ≥ 9x⁴/16`, so the quotient is at most `8/9`. -/
theorem abs_logSinc_deriv2_le {x : ℝ} (hx : 0 < x) (hx1 : x ≤ 1) :
    |1 / x ^ 2 - 1 / Real.sin x ^ 2| ≤ 1 := by
  have hxpi : x < π := lt_of_le_of_lt hx1 (by linarith [Real.two_le_pi])
  have hsin : 0 < Real.sin x := Real.sin_pos_of_pos_of_lt_pi hx hxpi
  have hlt : Real.sin x < x := Real.sin_lt hx
  have hcube : x - x ^ 3 / 4 < Real.sin x := Real.sin_gt_sub_cube hx hx1
  have hx3 : x ^ 3 ≤ x := by
    nlinarith [mul_nonneg hx.le (by nlinarith : (0 : ℝ) ≤ 1 - x ^ 2)]
  have hlb : 3 * x / 4 ≤ Real.sin x := by linarith
  have hden0 : 0 < x ^ 2 * Real.sin x ^ 2 := by positivity
  have hrw : 1 / x ^ 2 - 1 / Real.sin x ^ 2
      = (Real.sin x ^ 2 - x ^ 2) / (x ^ 2 * Real.sin x ^ 2) := by
    field_simp
  rw [hrw, abs_div, abs_of_pos hden0, div_le_one hden0]
  have hnumneg : Real.sin x ^ 2 - x ^ 2 ≤ 0 := by
    nlinarith [mul_pos (sub_pos.mpr hlt) (by linarith : (0 : ℝ) < x + Real.sin x)]
  rw [abs_of_nonpos hnumneg]
  -- `x² − sin²x ≤ x⁴/2 ≤ (9/16)x⁴ ≤ x²sin²x`
  have hd1 : x - Real.sin x < x ^ 3 / 4 := by linarith
  have hd2 : x + Real.sin x < 2 * x := by linarith
  have hnum : x ^ 2 - Real.sin x ^ 2 ≤ x ^ 4 / 2 := by
    nlinarith [hd1, hd2, hx, hsin, sub_pos.mpr hlt]
  have hsin2 : 9 * x ^ 2 / 16 ≤ Real.sin x ^ 2 := by nlinarith [hlb, hx]
  have hden : 9 * x ^ 4 / 16 ≤ x ^ 2 * Real.sin x ^ 2 := by
    nlinarith [hsin2, sq_nonneg x, hx]
  linarith [pow_nonneg hx.le 4]

/-! ### `logSinc″` is antitone — the last hypothesis the composite rule needs -/

/-- `logSinc‴ x = −2/x³ + 2·cos x/sin³x` on `(0, π)`. -/
theorem hasDerivAt_logSinc_deriv2 {x : ℝ} (hx : 0 < x) (hxpi : x < π) :
    HasDerivAt (fun y : ℝ => 1 / y ^ 2 - 1 / Real.sin y ^ 2)
      (-(2 / x ^ 3) + 2 * Real.cos x / Real.sin x ^ 3) x := by
  have hsin : 0 < Real.sin x := Real.sin_pos_of_pos_of_lt_pi hx hxpi
  have h1 : HasDerivAt (fun y : ℝ => 1 / y ^ 2) (-(2 / x ^ 3)) x := by
    have hx2 : HasDerivAt (fun y : ℝ => y ^ 2) (2 * x) x := by
      have h := (hasDerivAt_id x).pow 2; norm_num at h; convert h using 1
    have h := hx2.inv (by positivity)
    simp only [one_div]
    convert h using 1
    field_simp
  have h2 : HasDerivAt (fun y : ℝ => 1 / Real.sin y ^ 2)
      (-(2 * Real.cos x / Real.sin x ^ 3)) x := by
    have hs2 : HasDerivAt (fun y : ℝ => Real.sin y ^ 2)
        (2 * Real.sin x * Real.cos x) x := by
      have h := (Real.hasDerivAt_sin x).pow 2
      norm_num at h
      convert h using 1
    have h := hs2.inv (by positivity)
    simp only [one_div]
    convert h using 1
    field_simp
  have h := h1.sub h2
  convert h using 1
  ring

/-- **`logSinc″` is antitone on any `[c,d] ⊆ (0, π)`.**

`logSinc‴ ≤ 0` there, because `2cos x/sin³x ≤ 2/x³` is exactly
`x³·cos x ≤ sin³x` — `QOU.MathlibExt.mul_cube_cos_lt_sin_cube`.

This is the final hypothesis of
`QOU.MathlibExt.abs_integral_sub_composite_le_osc`; with it, every input that
composite rule asks for is available for `logSinc` on `[h, θ]`. -/
theorem antitoneOn_logSinc_deriv {c d : ℝ} (hc : 0 < c) (hd : d < π) :
    AntitoneOn (fun y : ℝ => 1 / y ^ 2 - 1 / Real.sin y ^ 2) (Set.Icc c d) := by
  have hmem : ∀ x ∈ Set.Icc c d, 0 < x ∧ x < π := by
    intro x hx
    rw [Set.mem_Icc] at hx
    exact ⟨lt_of_lt_of_le hc hx.1, lt_of_le_of_lt hx.2 hd⟩
  refine antitoneOn_of_deriv_nonpos (convex_Icc c d) ?_ ?_ ?_
  · intro x hx
    obtain ⟨h0, hpi⟩ := hmem x hx
    exact ((hasDerivAt_logSinc_deriv2 h0 hpi).continuousAt).continuousWithinAt
  · intro x hx
    rw [interior_Icc, Set.mem_Ioo] at hx
    have h0 : 0 < x := lt_trans hc hx.1
    have hpi : x < π := lt_trans hx.2 hd
    exact ((hasDerivAt_logSinc_deriv2 h0 hpi).differentiableAt).differentiableWithinAt
  · intro x hx
    rw [interior_Icc, Set.mem_Ioo] at hx
    have h0 : 0 < x := lt_trans hc hx.1
    have hpi : x < π := lt_trans hx.2 hd
    have hsin : 0 < Real.sin x := Real.sin_pos_of_pos_of_lt_pi h0 hpi
    rw [(hasDerivAt_logSinc_deriv2 h0 hpi).deriv]
    have hx3 : (0 : ℝ) < x ^ 3 := pow_pos h0 3
    have hs3 : (0 : ℝ) < Real.sin x ^ 3 := pow_pos hsin 3
    have hkey := QOU.MathlibExt.mul_cube_cos_lt_sin_cube h0 hpi
    have hle : 2 * Real.cos x / Real.sin x ^ 3 ≤ 2 / x ^ 3 := by
      rw [div_le_div_iff₀ hs3 hx3]
      nlinarith [hkey]
    linarith

/-! ### The composite rule, instantiated at `logSinc`

Every hypothesis is now in hand, so this is a direct application.  The grid is
`h, 2h, …, (m+1)h` — it starts at `h`, never touching `0`, which is the whole
reason no regularity at `0` is needed.
-/

/-- **The Euler–Maclaurin expansion of `∑_{j=1}^{m+1} logSinc(jh)`.**

    | ∑_{j=0}^{m} logSinc(h+jh)
        − [ (1/h)∫_h^{h+mh} logSinc + ½(logSinc h + logSinc(h+mh))
            + (h/12)(logSinc′(h+mh) − logSinc′(h)) ] |
      ≤ (h²/12)·(logSinc″(h) − logSinc″(h+mh))

i.e. the `B₂` term appears once and the error is `O(h²)` — an order below the
`O(1/N)` term `qou-mlgp` (A) extracts.

This is `QOU.MathlibExt.abs_integral_sub_composite_le_osc` at `g = logSinc`,
`a = h`, divided through by `h`.  The four hypotheses it needs are
`hasDerivAt_logSinc`, `hasDerivAt_logSinc_deriv`, continuity of `logSinc″` (from
`hasDerivAt_logSinc_deriv2`), and `antitoneOn_logSinc_deriv`. -/
theorem abs_sum_logSinc_sub_euler_maclaurin {h : ℝ} (hh : 0 < h) (m : ℕ)
    (hlt : h + m * h < π) :
    |(∑ j ∈ Finset.range (m + 1), logSinc (h + j * h))
        - ((1 / h) * (∫ x in h..(h + m * h), logSinc x)
           + (logSinc h + logSinc (h + m * h)) / 2
           + (h / 12) * ((Real.cos (h + m * h) / Real.sin (h + m * h)
                            - 1 / (h + m * h))
                         - (Real.cos h / Real.sin h - 1 / h)))|
      ≤ h ^ 2 / 12 * ((1 / h ^ 2 - 1 / Real.sin h ^ 2)
          - (1 / (h + m * h) ^ 2 - 1 / Real.sin (h + m * h) ^ 2)) := by
  have hmR : (0 : ℝ) ≤ (m : ℝ) := Nat.cast_nonneg m
  have hle : h ≤ h + (m : ℝ) * h := by nlinarith
  have hmem : ∀ x ∈ Set.Icc h (h + (m : ℝ) * h), 0 < x ∧ x < π := by
    intro x hx
    rw [Set.mem_Icc] at hx
    exact ⟨lt_of_lt_of_le hh hx.1, lt_of_le_of_lt hx.2 hlt⟩
  have hcomp := QOU.MathlibExt.abs_integral_sub_composite_le_osc
    (g := logSinc) (g₁ := fun x => Real.cos x / Real.sin x - 1 / x)
    (g₂ := fun x => 1 / x ^ 2 - 1 / Real.sin x ^ 2) (a := h) hh m
    (fun x hx => by
      obtain ⟨h0, hpi⟩ := hmem x hx; exact hasDerivAt_logSinc h0 hpi)
    (fun x hx => by
      obtain ⟨h0, hpi⟩ := hmem x hx; exact hasDerivAt_logSinc_deriv h0 hpi)
    (fun x hx => by
      obtain ⟨h0, hpi⟩ := hmem x hx
      exact ((hasDerivAt_logSinc_deriv2 h0 hpi).continuousAt).continuousWithinAt)
    (antitoneOn_logSinc_deriv hh hlt)
  -- divide the composite bound through by `h`
  have hkey : (∑ j ∈ Finset.range (m + 1), logSinc (h + (j : ℝ) * h))
      - ((1 / h) * (∫ x in h..(h + (m : ℝ) * h), logSinc x)
         + (logSinc h + logSinc (h + (m : ℝ) * h)) / 2
         + (h / 12) * ((Real.cos (h + (m : ℝ) * h) / Real.sin (h + (m : ℝ) * h)
                          - 1 / (h + (m : ℝ) * h))
                       - (Real.cos h / Real.sin h - 1 / h)))
      = -(1 / h) * ((∫ x in h..(h + (m : ℝ) * h), logSinc x)
          - (h * (∑ j ∈ Finset.range (m + 1), logSinc (h + (j : ℝ) * h))
             - h / 2 * (logSinc h + logSinc (h + (m : ℝ) * h))
             - h ^ 2 / 12 * ((Real.cos (h + (m : ℝ) * h) / Real.sin (h + (m : ℝ) * h)
                                - 1 / (h + (m : ℝ) * h))
                             - (Real.cos h / Real.sin h - 1 / h)))) := by
    field_simp
    ring
  rw [hkey, abs_mul, abs_neg, abs_of_pos (show (0 : ℝ) < 1 / h from by positivity)]
  have hb : |(∫ x in h..(h + (m : ℝ) * h), logSinc x)
      - (h * (∑ j ∈ Finset.range (m + 1), logSinc (h + (j : ℝ) * h))
         - h / 2 * (logSinc h + logSinc (h + (m : ℝ) * h))
         - h ^ 2 / 12 * ((Real.cos (h + (m : ℝ) * h) / Real.sin (h + (m : ℝ) * h)
                            - 1 / (h + (m : ℝ) * h))
                         - (Real.cos h / Real.sin h - 1 / h)))|
      ≤ h ^ 3 / 12 * ((1 / h ^ 2 - 1 / Real.sin h ^ 2)
          - (1 / (h + (m : ℝ) * h) ^ 2 - 1 / Real.sin (h + (m : ℝ) * h) ^ 2)) := hcomp
  refine le_trans (mul_le_mul_of_nonneg_left hb (by positivity)) (le_of_eq ?_)
  field_simp
  try ring

end QOU.Knot.FigureEightVolume
