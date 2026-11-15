/-
# Bridge: the complex dilogarithm agrees with QOU's real one

`QOU.MathlibExt.cLiTwo` is deliberately Mathlib-only so it stays upstreamable,
so it cannot mention `QOU.QPochhammer.LiTwo`. This file is the bridge, and it
is where the leverage is: QOU already carries ~20 sorry-free files of *real*
dilogarithm theory (`DilogReflection`, `DilogPartA*`, `DilogPartB*`), and a
single cast lemma makes all of it available to the complex side.

## Why this is the high-leverage brick

The remaining obstacle to the 5₂ saddle sum rule (bean `qou-0yqu`) is the
complex Euler reflection identity, needed at `y₁` with `|y₁| = 1.52 > 1`. The
standard route is analytic continuation from the real segment via the identity
theorem (`AnalyticOnNhd.eqOn_of_preconnected_of_frequently_eq`), which needs
the identity to hold on a set with an accumulation point.

`cLiTwo_reflection_ofReal` supplies exactly that set — the real interval
`(0,1)` — by transporting the already-proved `LiTwo_reflection'`, and
`cLiTwo_reflection` runs the continuation:

    Li₂ z + Li₂ (1 − z) = π²/6 − log z · log (1 − z)   for z ∈ ball(½, ½)

sorry-free, on axioms `[propext, Classical.choice, Quot.sound]` only.

## What is NOT here

**The identity at the 5₂ saddle root `y₁`.** `ball(½,½)` sits inside the unit
disc, and `|y₁| = 1.52`; reaching it needs the *inversion* formula
`Li₂ z + Li₂ (1/z) = −π²/6 − ½ log(−z)²` on top of this. So this file does not
yet discharge `hrefl` in `QOU.QBeta.FiveTwo.sum_reflection_of_branch`, and the
5₂ saddle sum rule (`qou-0yqu`) remains unproved.

`ball(½,½)` rather than the unit ball is forced, not a convenience: for `z` in
the unit ball `|1−z|` reaches 2, so `cLiTwo (1−z)` is outside the region where
the series converges, and `Complex.log`'s branch cut runs through it. The
analyticity hypotheses live in `QOU.MathlibExt.ComplexDilogarithm` (the
`…_ball_half` block).

Nothing is stubbed: no `sorry`, no axiom. Tracked in `qou-gkco`.

-- Ref: [leitner2026] beans qou-gkco, qou-ph1k
-/
import QOU.MathlibExt.ComplexDilogarithm
import QOU.Archimedean.DilogReflection

namespace QOU.Archimedean

-- `LiTwo` and its theory live in `QOU.QPochhammer` (in
-- `QOU/Archimedean/DilogarithmArchimedeanLimit.lean` — the namespace does not
-- follow the directory), so it must be opened explicitly.
open Complex QOU.MathlibExt QOU.QPochhammer

/-- **The bridge.** `cLiTwo` at a real argument is the real `LiTwo`.

Unconditional: both series are the same termwise after casting, and where
neither converges both `tsum`s are `0` by Mathlib's junk-value convention, so
no disc hypothesis is needed. -/
theorem cLiTwo_ofReal (x : ℝ) : cLiTwo (x : ℂ) = ((LiTwo x : ℝ) : ℂ) := by
  unfold cLiTwo LiTwo
  rw [Complex.ofReal_tsum]
  refine tsum_congr fun k => ?_
  push_cast
  ring

-- NOTE (2026-08-06): a `cLiTwo_one : cLiTwo 1 = π²/6` corollary follows in one
-- line from `QOU.QPochhammer.LiTwo_one` + `cLiTwo_ofReal`, but is NOT included
-- here because it could not be VERIFIED in this environment: the restored
-- `lake-cache/qou-v4-24-0` olean for `DilogarithmArchimedeanLimit` is stale —
-- it exports `LiTwo` but not `LiTwo_one` (unknown identifier even fully
-- qualified). Rather than ship an unverified lemma, it is left out; add it
-- once the cache branch is reseeded against current `main`.

/-- **The Euler reflection identity on the real segment, stated in ℂ.**

Transported from the sorry-free real `LiTwo_reflection'`. This is the set on
which the complex reflection identity is already known — the input to an
identity-theorem continuation, which is the remaining work (`qou-gkco`). -/
theorem cLiTwo_reflection_ofReal {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    cLiTwo (x : ℂ) + cLiTwo (1 - (x : ℂ))
      = (Real.pi : ℂ) ^ 2 / 6
        - Complex.log (x : ℂ) * Complex.log (1 - (x : ℂ)) := by
  have hx1' : (0 : ℝ) ≤ 1 - x := by linarith
  have hsub : (1 : ℂ) - (x : ℂ) = ((1 - x : ℝ) : ℂ) := by push_cast; ring
  rw [hsub, cLiTwo_ofReal, cLiTwo_ofReal, ← Complex.ofReal_log hx0.le,
    ← Complex.ofReal_log hx1']
  have hr := LiTwo_reflection' x hx0 hx1
  have : ((LiTwo x + LiTwo (1 - x) : ℝ) : ℂ)
      = ((Real.pi ^ 2 / 6 - Real.log x * Real.log (1 - x) : ℝ) : ℂ) := by
    exact_mod_cast congrArg (fun r : ℝ => (r : ℂ)) hr
  push_cast at this ⊢
  linear_combination this

/-! ### The continuation: the reflection identity on all of `ball(½, ½)`

The identity theorem, applied on the ball whose analyticity hypotheses are
assembled in `QOU.MathlibExt`. The accumulation set is the real segment
`(0,1)`, transported by `cLiTwo_reflection_ofReal` above.

Why `ball(½,½)` and not the unit ball: for `z` in the unit ball `|1−z|` reaches
2, so `cLiTwo (1−z)` is not given by its series, and `Complex.log` has its
branch cut running through it. See the `…_ball_half` block in
`QOU.MathlibExt.ComplexDilogarithm`. -/

open Filter Topology

/-- `ℝ → ℂ` carries the punctured neighbourhood of `½` in ℝ into the punctured
neighbourhood of `½` in ℂ. This is what makes the real segment an accumulation
set for the identity theorem. -/
theorem tendsto_ofReal_nhdsNE_half :
    Filter.Tendsto (fun x : ℝ => (x : ℂ)) (𝓝[≠] (1 / 2 : ℝ)) (𝓝[≠] (1 / 2 : ℂ)) := by
  have hcast : ((1 / 2 : ℝ) : ℂ) = (1 / 2 : ℂ) := by push_cast; ring
  refine tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within _ ?_ ?_
  · have h := (Complex.continuous_ofReal.tendsto (1 / 2 : ℝ)).mono_left
      (nhdsWithin_le_nhds (s := ({(1 / 2 : ℝ)}ᶜ : Set ℝ)))
    rwa [hcast] at h
  · filter_upwards [self_mem_nhdsWithin] with x hx
    simp only [Set.mem_compl_iff, Set.mem_singleton_iff] at hx ⊢
    rw [← hcast]
    exact fun h => hx (Complex.ofReal_inj.mp h)

/-- **The complex Euler reflection identity, on `ball(½, ½)`.**

    Li₂ z + Li₂ (1 − z) = π²/6 − log z · log (1 − z)

Proved by analytic continuation from the real segment `(0,1)`, where it is
`cLiTwo_reflection_ofReal` — itself a transport of the sorry-free real
`LiTwo_reflection'`. This discharges the continuation step recorded as the
remaining work in bean `qou-gkco`.

**Scope.** `|z| < 1` throughout the ball, so this does *not* by itself reach
the 5₂ saddle root `y₁` (`|y₁| = 1.52`); that still needs the inversion
formula. -/
theorem cLiTwo_reflection {z : ℂ} (hz : z ∈ Metric.ball (1 / 2 : ℂ) (1 / 2)) :
    cLiTwo z + cLiTwo (1 - z)
      = (Real.pi : ℂ) ^ 2 / 6 - Complex.log z * Complex.log (1 - z) := by
  set U : Set ℂ := Metric.ball (1 / 2 : ℂ) (1 / 2) with hUdef
  set f : ℂ → ℂ :=
    fun w => cLiTwo w + cLiTwo (1 - w) + Complex.log w * Complex.log (1 - w) with hfdef
  set g : ℂ → ℂ := fun _ => (Real.pi : ℂ) ^ 2 / 6 with hgdef
  have hf : AnalyticOnNhd ℂ f U :=
    (cLiTwo_analyticOnNhd_ball_half.add cLiTwo_one_sub_analyticOnNhd_ball_half).add
      log_mul_log_one_sub_analyticOnNhd_ball_half
  have hg : AnalyticOnNhd ℂ g U := fun _ _ => analyticAt_const
  have hc : (1 / 2 : ℂ) ∈ U := Metric.mem_ball_self (by norm_num)
  have hfreq : ∃ᶠ w in 𝓝[≠] (1 / 2 : ℂ), f w = g w := by
    refine tendsto_ofReal_nhdsNE_half.frequently (Filter.Eventually.frequently ?_)
    have hIoo : Set.Ioo (0 : ℝ) 1 ∈ 𝓝 (1 / 2 : ℝ) :=
      Ioo_mem_nhds (by norm_num) (by norm_num)
    filter_upwards [nhdsWithin_le_nhds hIoo] with x hx
    have hr := cLiTwo_reflection_ofReal hx.1 hx.2
    simp only [hfdef, hgdef]
    linear_combination hr
  have heq := hf.eqOn_of_preconnected_of_frequently_eq hg
    ((convex_ball (1 / 2 : ℂ) (1 / 2)).isPreconnected) hc hfreq hz
  simp only [hfdef, hgdef] at heq
  linear_combination heq

end QOU.Archimedean
