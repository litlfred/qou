/-
  `sin x > x − x³/6`, `cos x < 1 − x²/2 + x⁴/24`, and `x³cos x < sin³x`.

  THE MATHLIB GAP, IN MATHLIB'S OWN WORDS.  `Trigonometric/Bounds.lean` proves
  `Real.sin_gt_sub_cube : 0 < x → x ≤ 1 → x − x³/4 < sin x`, and its own comment
  above that lemma says: *"the tighter inequality is `sin x > x - x ^ 3 / 6` for
  all `x > 0`, but this inequality has [a simpler proof]"*.  The tighter form is
  not there.  This file supplies it — for ALL `x > 0`, with no upper restriction
  — together with the matching cosine bound and the cubed inequality they give.

  THE LADDER.  Three monotonicity steps, each `f(0) = 0` plus `f′ > 0`, and each
  one feeding the next:

    1. `f  = sin x − x + x³/6`          `f′ = cos x − 1 + x²/2 > 0`
       directly from Mathlib's `one_sub_sq_div_two_lt_cos`.
       ⟹  `sin x > x − x³/6`.

    2. `g  = 1 − x²/2 + x⁴/24 − cos x`  `g′ = sin x − x + x³/6 = f > 0`
       — step 1 IS step 2's derivative positivity.
       ⟹  `cos x < 1 − x²/2 + x⁴/24`.

    3. `(1 − x²/6)³ = 1 − x²/2 + x⁴/12 − x⁶/216` exceeds `1 − x²/2 + x⁴/24`
       exactly when `x² ≤ 9`, so on `(0, π/2)` step 2 gives
       `cos x < (1 − x²/6)³`, hence
       `x³cos x < (x − x³/6)³ < sin³x` by step 1.
       For `x ≥ π/2` it is trivial: `cos x ≤ 0 < sin³x`.

  WHY THIS CORPUS WANTS IT — `qou-mlgp` (A).  `x³cos x < sin³x` on `(0, π)` is
  exactly `logSinc‴ < 0`, i.e. `logSinc″` is MONOTONE.  With
  `QOU/MathlibExt/CorrectedTrapezoid.lean`'s reduction of the order-2 remainder
  from `g⁗` to `g″` (kernel double roots, zero mean), monotone `g″` makes the
  per-cell oscillations TELESCOPE, and the composite error on the sum drops to
  `O(h²·TV(g″)) = O(1/N²)` — below the `O(1/N)` term (A) is extracting.  It
  replaces what would otherwise be an eighth-order cancellation bound on
  `logSinc⁗`.

  -- Ref: [leitner2026] QOU/MathlibExt/CorrectedTrapezoid.lean   (the reduction)
  -- Ref: [leitner2026] QOU/Knot/LogSincNearZero.lean            (|logSinc″| ≤ 1)
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds
import Mathlib.Analysis.Calculus.MeanValue

namespace QOU.MathlibExt

open Real

/-- **`sin x > x − x³/6` for every `x > 0`** — the tighter form of
`Real.sin_gt_sub_cube`, which Mathlib states only as `x − x³/4` on `(0,1]`.

`f = sin x − x + x³/6` has `f(0) = 0` and `f′ = cos x − 1 + x²/2 > 0`, the
latter being exactly `Real.one_sub_sq_div_two_lt_cos`. -/
theorem sub_cube_div_six_lt_sin {x : ℝ} (hx : 0 < x) :
    x - x ^ 3 / 6 < Real.sin x := by
  have hderiv : ∀ y : ℝ, HasDerivAt (fun z : ℝ => Real.sin z - z + z ^ 3 / 6)
      (Real.cos y - 1 + y ^ 2 / 2) y := by
    intro y
    have h3 : HasDerivAt (fun z : ℝ => z ^ 3) (3 * y ^ 2) y := by
      have h := (hasDerivAt_id y).pow 3; norm_num at h; convert h using 1
    have h := ((Real.hasDerivAt_sin y).sub (hasDerivAt_id y)).add (h3.div_const 6)
    convert h using 1
    ring
  have hmono : StrictMonoOn (fun z : ℝ => Real.sin z - z + z ^ 3 / 6)
      (Set.Ici 0) := by
    refine strictMonoOn_of_deriv_pos (convex_Ici 0)
      (fun y _ => ((hderiv y).continuousAt).continuousWithinAt) ?_
    intro y hy
    rw [interior_Ici, Set.mem_Ioi] at hy
    rw [(hderiv y).deriv]
    linarith [Real.one_sub_sq_div_two_lt_cos (ne_of_gt hy)]
  have := hmono (Set.mem_Ici.mpr le_rfl) (Set.mem_Ici.mpr hx.le) hx
  simp only at this
  norm_num at this
  linarith

/-- **`cos x < 1 − x²/2 + x⁴/24` for every `x > 0`.**

`g = 1 − x²/2 + x⁴/24 − cos x` has `g(0) = 0` and `g′ = sin x − x + x³/6`, which
is positive by the previous theorem — the two bounds bootstrap. -/
theorem cos_lt_one_sub_sq_div_two_add_pow_four_div_24 {x : ℝ} (hx : 0 < x) :
    Real.cos x < 1 - x ^ 2 / 2 + x ^ 4 / 24 := by
  have hderiv : ∀ y : ℝ, HasDerivAt
      (fun z : ℝ => 1 - z ^ 2 / 2 + z ^ 4 / 24 - Real.cos z)
      (-y + y ^ 3 / 6 + Real.sin y) y := by
    intro y
    have h2 : HasDerivAt (fun z : ℝ => z ^ 2) (2 * y) y := by
      have h := (hasDerivAt_id y).pow 2; norm_num at h; convert h using 1
    have h4 : HasDerivAt (fun z : ℝ => z ^ 4) (4 * y ^ 3) y := by
      have h := (hasDerivAt_id y).pow 4; norm_num at h; convert h using 1
    have h := (((hasDerivAt_const y (1 : ℝ)).sub (h2.div_const 2)).add
      (h4.div_const 24)).sub (Real.hasDerivAt_cos y)
    convert h using 1
    ring
  have hmono : StrictMonoOn
      (fun z : ℝ => 1 - z ^ 2 / 2 + z ^ 4 / 24 - Real.cos z) (Set.Ici 0) := by
    refine strictMonoOn_of_deriv_pos (convex_Ici 0)
      (fun y _ => ((hderiv y).continuousAt).continuousWithinAt) ?_
    intro y hy
    rw [interior_Ici, Set.mem_Ioi] at hy
    rw [(hderiv y).deriv]
    linarith [sub_cube_div_six_lt_sin hy]
  have := hmono (Set.mem_Ici.mpr le_rfl) (Set.mem_Ici.mpr hx.le) hx
  simp only at this
  norm_num at this
  linarith

/-- **`x³·cos x < sin³x` on `(0, π)`.**

For `x ≥ π/2` this is `cos x ≤ 0 < sin³x`.  For `x < π/2` it is the ladder:
`cos x < 1 − x²/2 + x⁴/24 ≤ (1 − x²/6)³` (the last step needing only `x² ≤ 9`),
so `x³cos x < (x − x³/6)³ < sin³x`.

This is `logSinc‴ < 0`, i.e. `logSinc″` is monotone — see the file header. -/
theorem mul_cube_cos_lt_sin_cube {x : ℝ} (hx : 0 < x) (hxpi : x < π) :
    x ^ 3 * Real.cos x < Real.sin x ^ 3 := by
  have hsin : 0 < Real.sin x := Real.sin_pos_of_pos_of_lt_pi hx hxpi
  have hsin3 : 0 < Real.sin x ^ 3 := pow_pos hsin 3
  rcases le_or_gt (π / 2) x with h | h
  · have hcos : Real.cos x ≤ 0 :=
      Real.cos_nonpos_of_pi_div_two_le_of_le h (by linarith [Real.pi_pos])
    nlinarith [pow_pos hx 3]
  · have hx2 : x ≤ 2 := by linarith [Real.pi_le_four]
    have h1 := sub_cube_div_six_lt_sin hx
    have h2 := cos_lt_one_sub_sq_div_two_add_pow_four_div_24 hx
    have hpos : 0 < x - x ^ 3 / 6 := by nlinarith
    have hcube : Real.cos x < (1 - x ^ 2 / 6) ^ 3 := by nlinarith [pow_pos hx 4, pow_pos hx 6]
    have hx3 : (0 : ℝ) < x ^ 3 := pow_pos hx 3
    have hstep : x ^ 3 * Real.cos x < (x - x ^ 3 / 6) ^ 3 := by nlinarith [hcube, hx3]
    have hfin : (x - x ^ 3 / 6) ^ 3 < Real.sin x ^ 3 :=
      pow_lt_pow_left₀ h1 hpos.le (by norm_num)
    linarith

end QOU.MathlibExt
