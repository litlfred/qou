import QOU.MathlibExt.ComplexDilogarithmDeriv
import QOU.MathlibExt.AlternatingZetaTwo

/-!
# Boundary values: `cLiTwoExt = cLiTwo` on the **closed** disc

`cLiTwoExt_eq_cLiTwo` gives agreement on the **open** unit disc. Every base point
worth using for a dilogarithm identity sits on the *boundary* — `z = −1` for
Landen, `z = 1` for reflection — so the open-disc statement is exactly one point
short wherever it is needed.

This file closes that gap on the part of the boundary that is off the cut:

    ‖y‖ ≤ 1  and  y ∉ [1,∞)   ⟹   cLiTwoExt y = cLiTwo y

## How

Two continuity facts and a limit, with no new estimates:

* `cLiTwo` is continuous on the **closed** disc. Its series is dominated there by
  `1/(k+1)²`, which is summable (`summable_one_div_succ_sq`), so
  `continuousOn_tsum` applies — the Weierstrass M-test, and the only place the
  boundary is touched.
* `cLiTwoExt` is continuous at `y` because it is **analytic** on `ℂ ∖ [1,∞)`
  (`analyticOnNhd_cLiTwoExt`), which is the theorem `ComplexDilogarithm.lean`
  flags as its own missing piece and `ComplexDilogarithmDeriv.lean` supplies.
* The two agree on the open disc, and `y` is in its closure, so the punctured
  neighbourhood filter is `NeBot` and the limits must agree.

## Why it is infrastructure and not a one-off

Stated for **every** boundary point off the cut, not for `−1`. The Landen base
point is the immediate consumer (`cLiTwoExt_neg_one` below, giving `−π²/12`),
but reflection at `z = 1` and any other boundary evaluation get it for free.

⚠ It does **not** reach `[1,∞)`, which is where the *inversion* leg needs values
— that boundary is on the cut, `cLiTwoExt` is not defined there, and no
continuity argument in this file applies to it. Route 33 G5 records that as the
sharper obstacle, and it stays open.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.MathlibExt

open Complex Metric Filter Topology

/-- **`cLiTwo` is continuous on the closed unit disc.** Weierstrass M-test with
`1/(k+1)²`; this is the only place the boundary is touched. -/
theorem continuousOn_cLiTwo_closedBall :
    ContinuousOn cLiTwo (closedBall (0 : ℂ) 1) := by
  refine continuousOn_tsum (u := fun k : ℕ => (1 : ℝ) / ((k : ℝ) + 1) ^ 2)
    (fun k => ?_) summable_one_div_succ_sq (fun k z hz => ?_)
  · exact (continuous_pow (k + 1)).continuousOn.div_const _
  · have hz1 : ‖z‖ ≤ 1 := by simpa using hz
    have hnum : ‖z ^ (k + 1)‖ ≤ 1 := by
      rw [norm_pow]
      exact pow_le_one₀ (norm_nonneg _) hz1
    have hden : ‖((k : ℂ) + 1) ^ 2‖ = ((k : ℝ) + 1) ^ 2 := by
      rw [norm_pow]
      congr 1
      simpa using Complex.norm_natCast (k + 1)
    rw [norm_div, hden]
    have hD : (0 : ℝ) < ((k : ℝ) + 1) ^ 2 := by positivity
    exact (div_le_div_iff_of_pos_right hD).mpr hnum

/-- **Agreement extends to the closed disc, off the cut.**

`cLiTwoExt_eq_cLiTwo` gives the open disc; this reaches every boundary point
that is not on `[1,∞)`. Both sides are continuous there — `cLiTwo` by the
M-test above, `cLiTwoExt` because it is analytic on `ℂ ∖ [1,∞)` — and they agree
on the open disc, whose closure contains the point. -/
theorem cLiTwoExt_eq_cLiTwo_of_norm_le_one {y : ℂ} (hy : ‖y‖ ≤ 1) (hnc : y ∈ notCut) :
    cLiTwoExt y = cLiTwo y := by
  have hmem : y ∈ closedBall (0 : ℂ) 1 := by simpa using hy
  haveI hne : (𝓝[ball (0 : ℂ) 1] y).NeBot := by
    rw [← mem_closure_iff_nhdsWithin_neBot, closure_ball _ one_ne_zero]
    exact hmem
  have hcont2 : ContinuousWithinAt cLiTwo (ball (0 : ℂ) 1) y :=
    (continuousOn_cLiTwo_closedBall y hmem).mono ball_subset_closedBall
  have hcont1 : ContinuousWithinAt cLiTwoExt (ball (0 : ℂ) 1) y :=
    ((analyticOnNhd_cLiTwoExt y hnc).continuousAt).continuousWithinAt
  have heqf : cLiTwo =ᶠ[𝓝[ball (0 : ℂ) 1] y] cLiTwoExt :=
    eventually_mem_nhdsWithin.mono fun z hz => (cLiTwoExt_eq_cLiTwo (by simpa using hz)).symm
  exact tendsto_nhds_unique hcont1 (hcont2.congr' heqf)

end QOU.MathlibExt
