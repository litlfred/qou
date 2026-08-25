import QOU.MathlibExt.ComplexDilogarithmDeriv
import Mathlib.Analysis.Convex.PathConnected
import Mathlib.Analysis.Analytic.IsolatedZeros

/-!
# `cLiTwoExt` is **the** analytic continuation — uniqueness

Bean `qou-clx8`. `ComplexDilogarithmDeriv.lean` proved `cLiTwoExt` analytic on
`ℂ ∖ [1,∞)`, and `cLiTwoExt_eq_cLiTwo` had already given agreement with the
series on the open disc. Together those are what "analytic continuation" means —
but the bean's own phrasing asks for more:

> `cLiTwoExt(y₁)` is not *identified* with the `Li₂(y₁)` the sum rule refers to

which is **uniqueness**: any analytic `g` on `ℂ ∖ [1,∞)` agreeing with the series
on the disc *is* `cLiTwoExt`. That is the identity theorem, and it needs the
domain to be preconnected. This file supplies that and draws the conclusion.

## The Mathlib gap that was actually missing

Mathlib has all three moving parts —

* `Complex.starConvex_one_slitPlane`  (`ℂ ∖ (−∞,0]` is star-convex about `1`)
* `StarConvex.isPathConnected`
* `AnalyticOnNhd.eqOn_of_preconnected_of_frequently_eq` (the identity theorem)

— but **not the star-convexity of `ℂ ∖ [1,∞)`**, which is the set this
development lives on. `starConvex_zero_notCut` below fills it: `ℂ ∖ [1,∞)` is
star-convex **about `0`**, for the reason the picture suggests — if `t·w` lies on
the cut for some `t ∈ (0,1]`, then `t·w` is real and `≥ 1`, so `w` is real and
`w = (t·w)/t ≥ 1/t ≥ 1`, i.e. `w` was on the cut already.

`notCut_eq_preimage_slitPlane` records the relation to Mathlib's set:
`ℂ ∖ [1,∞) = (1 − ·)⁻¹(ℂ ∖ (−∞,0])`, so the two are exchanged by `w ↦ 1 − w`,
and the star centres `0` and `1` correspond. The direct proof is shorter than
transporting star-convexity across that map, so the transport is recorded as an
equation rather than used.

## What this closes

    eqOn_cLiTwoExt_of_eqOn_ball : any analytic `g` on `ℂ ∖ [1,∞)` agreeing with
                                  `cLiTwo` on the disc equals `cLiTwoExt` there

So `cLiTwoExt` is not merely *an* analytic function extending the series — it is
**the** one, and `cLiTwoExt y₁` at `‖y₁‖ = 1.52` is the value the sum rule's
`Li₂(y₁)` refers to, with no choice left open.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms. `qou-clx8` is explicit
that closing it does not move the sum rule; Route 5 is a restatement, and even
the whole chain leaves an unevaluated real integral.
-/

namespace QOU.MathlibExt

open Complex Set

/-! ### `ℂ ∖ [1,∞)` is star-convex about `0`, hence connected -/

/-- `ℂ ∖ [1,∞)` is the image of Mathlib's slit plane under `w ↦ 1 − w`.

Recorded because it explains why the star centre here is `0` where Mathlib's is
`1`: the two sets are exchanged by that involution, which sends `1 ↦ 0`. -/
theorem notCut_eq_preimage_slitPlane :
    notCut = (fun w : ℂ => 1 - w) ⁻¹' slitPlane := by
  ext w
  simp only [notCut, mem_preimage, mem_setOf_eq, mem_slitPlane_iff,
    Complex.sub_re, Complex.sub_im, Complex.one_re, Complex.one_im]
  constructor
  · rintro (h | h)
    · exact Or.inr (by simpa using neg_ne_zero.mpr h)
    · exact Or.inl (by linarith)
  · rintro (h | h)
    · exact Or.inr (by linarith)
    · refine Or.inl ?_
      simpa using fun hc => h (by simp [hc])

/-- **`0 ∈ ℂ ∖ [1,∞)`.** -/
theorem zero_mem_notCut : (0 : ℂ) ∈ notCut := Or.inr (by norm_num)

/-- **`ℂ ∖ [1,∞)` is star-convex about `0`** — the piece Mathlib does not have.

If `b·w` were on the cut for some `b ∈ (0,1]`, it would be real and `≥ 1`, hence
`w` real with `w = (b·w)/b ≥ 1/b ≥ 1`: `w` was on the cut to begin with. -/
theorem starConvex_zero_notCut : StarConvex ℝ 0 notCut := by
  intro w hw a b _ha hb hab
  have hb1 : b ≤ 1 := by linarith
  simp only [smul_zero, zero_add, Complex.real_smul]
  rcases hw with him | hre
  · -- `w` off the real axis: `b·w` is too, unless `b = 0`, and then it is `0`
    rcases eq_or_lt_of_le hb with rfl | hbpos
    · exact Or.inr (by simp)
    · refine Or.inl ?_
      simp only [Complex.mul_im, Complex.ofReal_re, Complex.ofReal_im, zero_mul, add_zero]
      exact mul_ne_zero (ne_of_gt hbpos) him
  · -- `Re w < 1`: scaling by `b ∈ [0,1]` cannot push the real part up to `1`
    refine Or.inr ?_
    simp only [Complex.mul_re, Complex.ofReal_re, Complex.ofReal_im, zero_mul, sub_zero]
    rcases le_or_gt w.re 0 with h | h
    · nlinarith
    · nlinarith

/-- **`ℂ ∖ [1,∞)` is path-connected.** -/
theorem isPathConnected_notCut : IsPathConnected notCut :=
  starConvex_zero_notCut.isPathConnected zero_mem_notCut

/-- **`ℂ ∖ [1,∞)` is preconnected** — the hypothesis the identity theorem wants. -/
theorem isPreconnected_notCut : IsPreconnected notCut :=
  isPathConnected_notCut.isConnected.isPreconnected

/-! ### Uniqueness of the continuation -/

/-- **`cLiTwoExt` is the unique analytic extension of the series.**

If `g` is analytic on `ℂ ∖ [1,∞)` and agrees with `cLiTwo` on the open unit disc,
then `g = cLiTwoExt` on all of `ℂ ∖ [1,∞)`.

The identity theorem, with `z₀ = 0`: agreement on a whole disc is far more than
the accumulation it needs. -/
theorem eqOn_cLiTwoExt_of_eqOn_ball {g : ℂ → ℂ}
    (hg : AnalyticOnNhd ℂ g notCut)
    (hagree : ∀ z : ℂ, ‖z‖ < 1 → g z = cLiTwo z) :
    Set.EqOn g cLiTwoExt notCut := by
  refine hg.eqOn_of_preconnected_of_frequently_eq analyticOnNhd_cLiTwoExt
    isPreconnected_notCut zero_mem_notCut ?_
  have hev : ∀ᶠ z in nhds (0 : ℂ), g z = cLiTwoExt z := by
    filter_upwards [Metric.ball_mem_nhds (0 : ℂ) one_pos] with z hz
    have hz' : ‖z‖ < 1 := by simpa using hz
    rw [hagree z hz', cLiTwoExt_eq_cLiTwo hz']
  exact (hev.filter_mono nhdsWithin_le_nhds).frequently

/-- **Non-vacuity.** `eqOn_cLiTwoExt_of_eqOn_ball` is universally quantified over
`g`, and a uniqueness theorem whose hypotheses nothing satisfies proves nothing.
They are satisfiable: `cLiTwoExt` itself meets them.

The check with real bite is numerical and lives in Route 23 G1: mpmath's
`polylog(2, ·)` is an **independently implemented** analytic continuation
(functional equations and series acceleration, nothing to do with this integral),
so uniqueness predicts it must agree with `cLiTwoExt` everywhere off the cut. It
does — to 30 dps at `‖y‖ = 40`, far outside the disc where the series diverges. -/
theorem eqOn_cLiTwoExt_hypotheses_satisfiable :
    AnalyticOnNhd ℂ cLiTwoExt notCut ∧ ∀ z : ℂ, ‖z‖ < 1 → cLiTwoExt z = cLiTwo z :=
  ⟨analyticOnNhd_cLiTwoExt, fun _ hz => cLiTwoExt_eq_cLiTwo hz⟩

/-- The same statement phrased against `cLiTwoExt` itself: two analytic functions
on `ℂ ∖ [1,∞)` agreeing near `0` agree everywhere on it. -/
theorem eqOn_of_analyticOnNhd_of_eventuallyEq {f g : ℂ → ℂ}
    (hf : AnalyticOnNhd ℂ f notCut) (hg : AnalyticOnNhd ℂ g notCut)
    (h : ∀ᶠ z in nhds (0 : ℂ), f z = g z) :
    Set.EqOn f g notCut :=
  hf.eqOn_of_preconnected_of_frequently_eq hg isPreconnected_notCut zero_mem_notCut
    (h.filter_mono nhdsWithin_le_nhds).frequently

end QOU.MathlibExt
