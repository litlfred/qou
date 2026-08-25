import QOU.MathlibExt.ComplexDilogarithmSlit
import Mathlib.Analysis.Calculus.ParametricIntervalIntegral

/-!
# `cLiTwoExt` is complex-differentiable on `ℂ ∖ [1,∞)`

Bean `qou-clx8`. `ComplexDilogarithmSlit.lean` gave the derivative **along rays**
by moving the parameter into the limit of integration. That is not enough for
analyticity, which needs every direction. This file gets it, by differentiating
under the integral sign after all — which the bean called "not a Mathlib
one-liner", correctly: Mathlib supplies the theorem
(`intervalIntegral.hasDerivAt_integral_of_dominated_loc_of_deriv_le`, with
`𝕜 = ℂ`, so its conclusion is a genuine **complex** derivative) but not the one
hypothesis that is actually work here.

## The missing infrastructure, and why it is the whole job

The dominating function has to bound `∂/∂w [log(1−wz)/z] = −(1−wz)⁻¹` uniformly
for `w` in a ball and `z ∈ [0,1]`. So what is needed is

    ∃ ε > 0, ∃ δ > 0, ∀ w ∈ closedBall w₀ ε, ∀ z ∈ [0,1],  δ ≤ ‖1 − w·z‖

and once that exists the dominating function is a **constant**, which is the
easiest possible case of the theorem.

`exists_uniform_lower_bound` below is that statement. It is proved by compactness
rather than by explicit estimates: `closedBall w₀ ε ×ˢ Icc 0 1` is compact, the
map `(w,z) ↦ ‖1 − w·z‖` is continuous on it, and it never vanishes there —
because `ℂ ∖ [1,∞)` is **open** (`isOpen_notCut`), so a small enough ball stays
inside it, and there `mem_slitPlane_one_sub_mul` puts `1 − wz` in `slitPlane`,
which excludes `0`. A continuous positive function on a compact set has a
positive minimum.

Explicit estimates would work too, but they split into two cases with different
shapes (`m/√(M²+m²)` off the real axis, `1 − max(Re w₀ + ε, 0)` on it) and the
compactness argument handles both at once.

## The result

    hasDerivAt_cLiTwoExt : HasDerivAt cLiTwoExt (∫ z in 0..1, -(1 - w*z)⁻¹) w
    hasDerivAt_cLiTwoExt' : w ≠ 0 → HasDerivAt cLiTwoExt (-(log (1-w)/w)) w
    differentiableOn_cLiTwoExt, analyticOnNhd_cLiTwoExt

so `cLiTwoExt` is analytic on `ℂ ∖ [1,∞)` and **"the analytic continuation" is
now a theorem, not a name** — which is what `qou-clx8` set out to establish.

## ⚠ Why the derivative is stated as an integral first

`-(log (1−w)/w)` is the *wrong* value at `w = 0`: Lean's `x/0 = 0` makes it `0`,
while the true derivative there is `1` (from the series `Σ wᵏ/k²`). The integral
form `∫₀¹ -(1−wz)⁻¹ dz` is correct at every `w` including `0`, where it is `-1`
— note that is the derivative of the *integrand's* integral, and the sign flips
in `cLiTwoExt`'s leading minus. So the closed form is a **corollary with `w ≠ 0`**,
not the primary statement.

This lane has already been bitten once by exactly this: `hinv1`/`hlan1` were
false because Lean's junk values (`tsum` of a non-summable family is `0`) were
read as if they were the mathematical values. Stating the closed form as
primitive would have repeated it.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms. `qou-clx8` is explicit
that closing it does not move the sum rule; Route 5 is a restatement.
-/

namespace QOU.MathlibExt

open Complex MeasureTheory Metric Set Interval

/-! ### `ℂ ∖ [1,∞)` is open -/

/-- The complement of the cut, as a predicate: `w.im ≠ 0 ∨ w.re < 1`. -/
def notCut : Set ℂ := {w : ℂ | w.im ≠ 0 ∨ w.re < 1}

/-- **`ℂ ∖ [1,∞)` is open.** Its complement `{w | w.im = 0 ∧ 1 ≤ w.re}` is the
intersection of two closed preimages. -/
theorem isOpen_notCut : IsOpen notCut := by
  have hc : notCutᶜ
      = (fun w : ℂ => w.im) ⁻¹' {0} ∩ (fun w : ℂ => w.re) ⁻¹' Ici 1 := by
    ext w; simp [notCut, not_or, not_lt]
  rw [← isClosed_compl_iff, hc]
  exact (isClosed_singleton.preimage Complex.continuous_im).inter
    (isClosed_Ici.preimage Complex.continuous_re)

theorem mem_notCut_iff {w : ℂ} : w ∈ notCut ↔ (w.im ≠ 0 ∨ w.re < 1) := Iff.rfl

/-! ### The uniform lower bound — the piece Mathlib does not supply -/

set_option maxHeartbeats 1000000 in
/-- **`‖1 − w·z‖` is bounded below, uniformly for `w` near `w₀` and `z ∈ [0,1]`.**

This is the hypothesis `hasDerivAt_integral_of_dominated_loc_of_deriv_le` needs
and the only real work in this file: with it the dominating function is a
constant.

Compactness, not estimates. `ℂ ∖ [1,∞)` is open, so some closed ball around `w₀`
stays inside it; on that ball `mem_slitPlane_one_sub_mul` puts `1 − wz` in
`slitPlane`, which excludes `0`; and a continuous, nowhere-zero function on the
compact `closedBall ×ˢ Icc 0 1` attains a positive minimum. -/
theorem exists_uniform_lower_bound {w₀ : ℂ} (hw₀ : w₀ ∈ notCut) :
    ∃ ε > (0 : ℝ), ∃ δ > (0 : ℝ),
      (∀ w ∈ closedBall w₀ ε, w ∈ notCut) ∧
      ∀ w ∈ closedBall w₀ ε, ∀ z ∈ Icc (0 : ℝ) 1, δ ≤ ‖1 - w * (z : ℂ)‖ := by
  -- a closed ball inside the open set
  obtain ⟨r, hr0, hr⟩ := Metric.isOpen_iff.mp isOpen_notCut w₀ hw₀
  refine ⟨r / 2, by linarith, ?_⟩
  have hsub : closedBall w₀ (r / 2) ⊆ notCut := fun w hw =>
    hr (mem_ball.2 (lt_of_le_of_lt (mem_closedBall.1 hw) (by linarith)))
  -- the compact product on which the norm is minimised
  set K : Set (ℂ × ℝ) := closedBall w₀ (r / 2) ×ˢ Icc (0 : ℝ) 1 with hK
  have hKcomp : IsCompact K := (isCompact_closedBall _ _).prod isCompact_Icc
  have hKne : K.Nonempty :=
    ⟨(w₀, 0), mem_closedBall_self (by linarith), ⟨le_rfl, by norm_num⟩⟩
  have hcont : ContinuousOn (fun p : ℂ × ℝ => ‖1 - p.1 * (p.2 : ℂ)‖) K :=
    (continuous_const.sub (continuous_fst.mul
      (Complex.continuous_ofReal.comp continuous_snd))).norm.continuousOn
  obtain ⟨p, hpK, hmin⟩ := hKcomp.exists_isMinOn hKne hcont
  -- the minimum is positive, because `1 − wz` lands in `slitPlane`
  have hpos : 0 < ‖1 - p.1 * (p.2 : ℂ)‖ := by
    rw [norm_pos_iff]
    exact Complex.slitPlane_ne_zero
      (mem_slitPlane_one_sub_mul (hsub hpK.1) hpK.2.1 hpK.2.2)
  refine ⟨‖1 - p.1 * (p.2 : ℂ)‖, hpos, hsub, ?_⟩
  intro w hw z hz
  have hmem : (w, z) ∈ K := Set.mem_prod.2 ⟨hw, hz⟩
  simpa using hmin hmem

/-! ### Differentiation under the integral sign -/

/-- The `w`-derivative of the integrand, pointwise in `z`. -/
theorem hasDerivAt_integrand {w : ℂ} {z : ℝ} (hz : z ≠ 0)
    (hslit : 1 - w * (z : ℂ) ∈ slitPlane) :
    HasDerivAt (fun x : ℂ => Complex.log (1 - x * (z : ℂ)) / (z : ℂ))
      (-(1 - w * (z : ℂ))⁻¹) w := by
  have hz' : ((z : ℝ) : ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr hz
  have hne : (1 : ℂ) - w * (z : ℂ) ≠ 0 := Complex.slitPlane_ne_zero hslit
  have hbase : HasDerivAt (fun x : ℂ => 1 - x * (z : ℂ)) (-(z : ℂ)) w := by
    simpa using ((hasDerivAt_id w).mul_const ((z : ℝ) : ℂ)).const_sub 1
  have hlog := hbase.clog hslit
  have h2 := hlog.div_const ((z : ℝ) : ℂ)
  convert h2 using 1
  field_simp

/-- **`cLiTwoExt` is complex-differentiable off the cut**, with derivative given
by the integral of the differentiated integrand.

The value is stated as an integral rather than in closed form on purpose — see
the module docstring: `-(log (1−w)/w)` is Lean-junk `0` at `w = 0`. -/
theorem hasDerivAt_cLiTwoExt {w : ℂ} (hw : w ∈ notCut) :
    HasDerivAt cLiTwoExt (-∫ z in (0 : ℝ)..1, -(1 - w * (z : ℂ))⁻¹) w := by
  obtain ⟨ε, hε, δ, hδ, hball, hbound⟩ := exists_uniform_lower_bound hw
  set F : ℂ → ℝ → ℂ := fun x z => Complex.log (1 - x * (z : ℂ)) / (z : ℂ) with hF
  set F' : ℂ → ℝ → ℂ := fun x z => -(1 - x * (z : ℂ))⁻¹ with hF'
  -- every `x` in the ball is off the cut, hence has an integrable integrand
  have hint : ∀ x ∈ closedBall w ε, IntervalIntegrable (F x) volume 0 1 := fun x hx =>
    intervalIntegrable_log_one_sub_div_of_notCut (mem_notCut_iff.1 (hball x hx))
  have hslit : ∀ x ∈ closedBall w ε, ∀ z ∈ Icc (0 : ℝ) 1,
      1 - x * (z : ℂ) ∈ slitPlane := fun x hx z hz =>
    mem_slitPlane_one_sub_mul (mem_notCut_iff.1 (hball x hx)) hz.1 hz.2
  -- `F'` is continuous in `z` on `[0,1]` for each such `x`
  have hF'cont : ∀ x ∈ closedBall w ε, ContinuousOn (F' x) (Icc (0 : ℝ) 1) := by
    intro x hx z hz
    refine ContinuousWithinAt.neg (ContinuousWithinAt.inv₀ ?_ ?_)
    · exact ((continuous_const.sub
        (continuous_const.mul Complex.continuous_ofReal)).continuousWithinAt)
    · exact Complex.slitPlane_ne_zero (hslit x hx z hz)
  -- Mathlib's hypotheses, one by one
  have hmeasF : ∀ᶠ x in nhds w, AEStronglyMeasurable (F x) (volume.restrict (Ι (0:ℝ) 1)) := by
    filter_upwards [Metric.closedBall_mem_nhds w hε] with x hx
    rw [Set.uIoc_of_le (by norm_num : (0:ℝ) ≤ 1)]
    exact ((hint x hx).1).aestronglyMeasurable
  have hmeasF' : AEStronglyMeasurable (F' w) (volume.restrict (Ι (0:ℝ) 1)) := by
    refine (ContinuousOn.aestronglyMeasurable ?_ measurableSet_Ioc)
    have : Ι (0:ℝ) 1 ⊆ Icc (0:ℝ) 1 := by
      rw [Set.uIoc_of_le (by norm_num : (0:ℝ) ≤ 1)]
      exact Set.Ioc_subset_Icc_self
    exact (hF'cont w (mem_closedBall_self hε.le)).mono this
  have hb : ∀ᵐ z ∂volume, z ∈ Ι (0:ℝ) 1 → ∀ x ∈ ball w ε, ‖F' x z‖ ≤ δ⁻¹ := by
    filter_upwards with z hz x hx
    have hzI : z ∈ Icc (0:ℝ) 1 := by
      rw [Set.uIoc_of_le (by norm_num : (0:ℝ) ≤ 1)] at hz
      exact Set.Ioc_subset_Icc_self hz
    have hxb : x ∈ closedBall w ε := ball_subset_closedBall hx
    have := hbound x hxb z hzI
    simp only [hF', norm_neg, norm_inv]
    exact inv_anti₀ hδ this
  have hbint : IntervalIntegrable (fun _ : ℝ => δ⁻¹) volume 0 1 :=
    intervalIntegrable_const
  have hdiff : ∀ᵐ z ∂volume, z ∈ Ι (0:ℝ) 1 →
      ∀ x ∈ ball w ε, HasDerivAt (fun x => F x z) (F' x z) x := by
    filter_upwards with z hz x hx
    have hzI : z ∈ Icc (0:ℝ) 1 := by
      rw [Set.uIoc_of_le (by norm_num : (0:ℝ) ≤ 1)] at hz
      exact Set.Ioc_subset_Icc_self hz
    have hzne : z ≠ 0 := by
      rw [Set.uIoc_of_le (by norm_num : (0:ℝ) ≤ 1)] at hz
      exact ne_of_gt hz.1
    exact hasDerivAt_integrand hzne (hslit x (ball_subset_closedBall hx) z hzI)
  have key := intervalIntegral.hasDerivAt_integral_of_dominated_loc_of_deriv_le
    (bound := fun _ : ℝ => δ⁻¹) hε hmeasF (hint w (mem_closedBall_self hε.le))
    hmeasF' hb hbint hdiff
  simpa [cLiTwoExt, hF, hF'] using key.2.neg

/-- The closed form, for `w ≠ 0`: `d/dw Li₂(w) = −log(1−w)/w`.

`∫₀¹ (1 − wz)⁻¹ dz = −log(1−w)/w` by the fundamental theorem of calculus, the
antiderivative in `z` being `−log(1 − wz)/w`. -/
theorem hasDerivAt_cLiTwoExt' {w : ℂ} (hw : w ∈ notCut) (hw0 : w ≠ 0) :
    HasDerivAt cLiTwoExt (-(Complex.log (1 - w) / w)) w := by
  have hmain := hasDerivAt_cLiTwoExt hw
  have hval : (-∫ z in (0 : ℝ)..1, -(1 - w * (z : ℂ))⁻¹)
      = -(Complex.log (1 - w) / w) := by
    have hderiv : ∀ z ∈ Set.uIcc (0:ℝ) 1,
        HasDerivAt (fun s : ℝ => Complex.log (1 - w * (s : ℂ)) / w)
          (-(1 - w * (z : ℂ))⁻¹) z := by
      intro z hz
      rw [Set.uIcc_of_le (by norm_num : (0:ℝ) ≤ 1)] at hz
      have hslit := mem_slitPlane_one_sub_mul (mem_notCut_iff.1 hw) hz.1 hz.2
      have hbase : HasDerivAt (fun s : ℝ => 1 - w * (s : ℂ)) (-w) z := by
        simpa using ((Complex.ofRealCLM.hasDerivAt (x := z)).const_mul w).const_sub 1
      have hne : (1 : ℂ) - w * (z : ℂ) ≠ 0 := Complex.slitPlane_ne_zero hslit
      have hlog := hbase.clog_real hslit
      have h2 := hlog.div_const w
      convert h2 using 1
      field_simp
    have hcont : IntervalIntegrable (fun z : ℝ => -(1 - w * (z : ℂ))⁻¹) volume 0 1 := by
      apply ContinuousOn.intervalIntegrable
      rw [Set.uIcc_of_le (by norm_num : (0:ℝ) ≤ 1)]
      intro z hz
      refine ContinuousWithinAt.neg (ContinuousWithinAt.inv₀ ?_ ?_)
      · exact ((continuous_const.sub
          (continuous_const.mul Complex.continuous_ofReal)).continuousWithinAt)
      · exact Complex.slitPlane_ne_zero
          (mem_slitPlane_one_sub_mul (mem_notCut_iff.1 hw) hz.1 hz.2)
    rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hcont]
    simp
  rwa [hval] at hmain

/-- **`cLiTwoExt` is differentiable on `ℂ ∖ [1,∞)`.** -/
theorem differentiableOn_cLiTwoExt : DifferentiableOn ℂ cLiTwoExt notCut :=
  fun _ hw => ((hasDerivAt_cLiTwoExt hw).differentiableAt).differentiableWithinAt

/-- **`cLiTwoExt` is analytic on `ℂ ∖ [1,∞)`.**

This is the statement `qou-clx8` set out to prove: the integral definition really
*is* the analytic continuation, not merely a function agreeing with the series on
the disc. -/
theorem analyticOnNhd_cLiTwoExt : AnalyticOnNhd ℂ cLiTwoExt notCut := by
  refine DifferentiableOn.analyticOnNhd ?_ isOpen_notCut
  exact differentiableOn_cLiTwoExt

end QOU.MathlibExt
