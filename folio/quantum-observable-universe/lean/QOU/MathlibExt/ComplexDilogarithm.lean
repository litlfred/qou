/-
# The complex dilogarithm `Li₂ : ℂ → ℂ` — the Mathlib gap, filled on the disc

**Mathlib has no polylogarithm at all** (checked 2026-08-06: no `Polylog`, no
`dilog`, no `Real.dilog`). QOU already carries a *real* one —
`QOU.QPochhammer.LiTwo : ℝ → ℝ` with `LiTwo_reflection'` proved sorry-free on
`(0,1)` — but the 5₂ saddle sum rule needs `Li₂` at **complex** arguments, and
that is what this file starts.

## Why the complex case is needed

The three roots of the 5₂ saddle cubic `y³ − 2y² + 3y − 1` are

    y₃ = 0.4301597…          real, in (0,1)   — covered by the real `LiTwo`
    y₁ = 0.78492 + 1.30714i  complex, |y₁| = 1.52 > 1
    y₂ = conj y₁

so exactly one of the three is in reach of the existing real theory. See bean
`qou-ph1k`.

## Scope of THIS file — honest

Defines `cLiTwo` by its defining power series and proves, all sorry-free:

* **convergence** — `cLiTwo_term_norm_le`, `cLiTwo_summable`: the series
  converges on the open unit disc;
* **analyticity** — `cLiTwo_radius_ge_one`, `cLiTwo_hasFPowerSeriesOnBall`,
  `cLiTwo_analyticOnNhd`: it *is* a power series there, so `cLiTwo` is
  analytic on the open unit disc;
* **the reflection identity's domain** — `norm_lt_one_of_mem_ball_half`,
  `one_sub_mem_ball_half`, `re_pos_of_mem_ball_half`,
  `mem_slitPlane_of_mem_ball_half`, and the four `…_ball_half` analyticity
  lemmas: on `Metric.ball (1/2) (1/2)` all four ingredients of the reflection
  identity are simultaneously analytic;
* **the integral representation** — `cLiTwo_eq_intervalIntegral`:
  `Li₂(y) = −∫₀¹ log(1 − yz)/z dz` on the disc, by termwise integration
  (dominated convergence with the geometric bound `‖y‖^(k+1)`). This is the
  form that continues past `‖y‖ = 1`, since the integral converges for every
  `y ∉ [1,∞)` while the series does not.

and finally `cLiTwoExt`, the integral *as a definition*, which is what reaches
past the disc.

It does **not** provide:

* agreement with the real `QOU.QPochhammer.LiTwo` on ℝ (deliberately: that
  import would tie this file to QOU and defeat the upstreaming goal below —
  it lives in `QOU.Archimedean.ComplexDilogBridge` instead, together with the
  complex Euler reflection identity `cLiTwo_reflection`, proved there on
  `ball(½,½)`);
* **analyticity of `cLiTwoExt` on `ℂ ∖ [1,∞)`** — so calling it "the analytic
  continuation" is, in this file, a name backed by agreement on the disc plus
  the standard definition, not a theorem. Needs differentiation under the
  integral sign;
* the inversion formula `Li₂ z + Li₂ (1/z) = −π²/6 − ½·log(−z)²`. Note this is
  **false** for `cLiTwo` at `‖z‖ > 1` (junk-valued `0` there), which is
  precisely why `cLiTwoExt` exists.

**None of those is stubbed** — no `sorry`, no `True`-valued placeholder, no
axiom. The file asserts only what it proves. Remaining work: `qou-ph1k`,
`qou-gkco`.

This still does **not** discharge `hrefl` in
`QOU.QBeta.FiveTwo.sum_reflection_of_branch`, which needs the reflection
identity at `y₁` (`‖y₁‖ = 1.52`) — outside `ball(½,½)`.

## Upstreaming

This is deliberately written in Mathlib style (series definition, `Summable`
lemmas, no QOU-specific dependencies beyond Mathlib itself) so it can be
offered upstream once the continuation and reflection land. Upstreaming is
premature until then and has no bean of its own; it is recorded as a follow-on
inside `qou-gkco`. (An earlier revision of this line cited a bean `qou-mlib`
that was never created — corrected 2026-08-06.)

-- Ref: [leitner2026] bean qou-ph1k; docs/coordination/1ppq-qbeta.md 2026-08-02
-- Ref: [lewin1981] Polylogarithms and Associated Functions, L. Lewin
-/
import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.Analysis.SpecialFunctions.Complex.Analytic
import Mathlib.Analysis.Analytic.OfScalars
import Mathlib.Analysis.Analytic.Basic
import Mathlib.Analysis.Analytic.ChangeOrigin
import Mathlib.MeasureTheory.Integral.DominatedConvergence
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.LogBounds

namespace QOU.MathlibExt

open Complex

/-- The complex dilogarithm as its defining power series,
`Li₂ z = ∑_{k ≥ 0} z^(k+1)/(k+1)²`.

Indexed from `k = 0` with numerator `z^(k+1)` so the `k`-th term is
`z^(k+1)/(k+1)²`, matching `QOU.QPochhammer.LiTwo` term by term. Outside the
closed unit disc the `tsum` is `0` by Mathlib's junk-value convention; the
lemmas below are all guarded by a disc hypothesis. -/
noncomputable def cLiTwo (z : ℂ) : ℂ :=
  ∑' k : ℕ, z ^ (k + 1) / ((k : ℂ) + 1) ^ 2

@[simp] theorem cLiTwo_zero : cLiTwo 0 = 0 := by
  unfold cLiTwo
  simp

/-- Each term is dominated by `‖z‖^(k+1)`, since `1/(k+1)² ≤ 1`. -/
theorem cLiTwo_term_norm_le (z : ℂ) (k : ℕ) :
    ‖z ^ (k + 1) / ((k : ℂ) + 1) ^ 2‖ ≤ ‖z‖ ^ (k + 1) := by
  have hk : (1 : ℝ) ≤ ‖((k : ℂ) + 1) ^ 2‖ := by
    have : ((k : ℂ) + 1) = ((k + 1 : ℕ) : ℂ) := by push_cast; ring
    rw [this, ← Nat.cast_pow, Complex.norm_natCast]
    exact_mod_cast Nat.one_le_iff_ne_zero.mpr (by positivity)
  rw [norm_div, norm_pow]
  calc ‖z‖ ^ (k + 1) / ‖((k : ℂ) + 1) ^ 2‖
      ≤ ‖z‖ ^ (k + 1) / 1 := by gcongr
      _ = ‖z‖ ^ (k + 1) := by ring

/-- The defining series converges on the open unit disc. -/
theorem cLiTwo_summable {z : ℂ} (hz : ‖z‖ < 1) :
    Summable fun k : ℕ => z ^ (k + 1) / ((k : ℂ) + 1) ^ 2 := by
  refine Summable.of_norm_bounded (g := fun k : ℕ => ‖z‖ ^ (k + 1)) ?_ ?_
  · exact (summable_geometric_of_lt_one (norm_nonneg z) hz).mul_left ‖z‖ |>.congr
      fun k => by rw [pow_succ']
  · intro k
    exact cLiTwo_term_norm_le z k

/-! ### Standard power-series indexing

`cLiTwo` is written `∑' k, z^(k+1)/(k+1)²` so that it matches
`QOU.QPochhammer.LiTwo` term by term (which is what makes `cLiTwo_ofReal`
unconditional). Mathlib's power-series machinery — `FormalMultilinearSeries.
ofScalars`, whose sum is `∑' n, cₙ • xⁿ` — wants the other indexing.

Rather than redefine `cLiTwo` and break the bridge, the two indexings are
reconciled here. This is step 1 of the analyticity route recorded in bean
`qou-gkco`; steps 2–3 (radius `= 1`, hence `AnalyticOnNhd` on the disc) are
not done. -/

/-- The coefficients of `Li₂` in standard indexing: `c₀ = 0`, `cₙ = 1/n²`. -/
noncomputable def cLiTwoCoeff (n : ℕ) : ℂ := if n = 0 then 0 else ((n : ℂ) ^ 2)⁻¹

@[simp] theorem cLiTwoCoeff_zero : cLiTwoCoeff 0 = 0 := by simp [cLiTwoCoeff]

theorem cLiTwoCoeff_succ (k : ℕ) :
    cLiTwoCoeff (k + 1) = (((k : ℂ) + 1) ^ 2)⁻¹ := by
  simp only [cLiTwoCoeff, Nat.succ_ne_zero, if_false]
  push_cast
  ring_nf

/-- The standard-indexed series is summable on the open unit disc. -/
theorem cLiTwoCoeff_summable {z : ℂ} (hz : ‖z‖ < 1) :
    Summable fun n : ℕ => cLiTwoCoeff n * z ^ n := by
  refine Summable.of_norm_bounded (g := fun n : ℕ => ‖z‖ ^ n) ?_ ?_
  · exact summable_geometric_of_lt_one (norm_nonneg z) hz
  · intro n
    rcases Nat.eq_zero_or_pos n with rfl | hn
    · simp
    · have hk : (1 : ℝ) ≤ ‖(n : ℂ)‖ ^ 2 := by
        rw [Complex.norm_natCast]
        have h1 : (1 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
        nlinarith
      simp only [cLiTwoCoeff, hn.ne', if_false, norm_mul, norm_inv, norm_pow]
      calc (‖(n : ℂ)‖ ^ 2)⁻¹ * ‖z‖ ^ n
          ≤ 1 * ‖z‖ ^ n := by
            gcongr
            exact inv_le_one_of_one_le₀ hk
        _ = ‖z‖ ^ n := one_mul _

/-- **The two indexings agree.** `cLiTwo z = ∑' n, cₙ zⁿ` with `c` as above. -/
theorem cLiTwo_eq_tsum_coeff {z : ℂ} (hz : ‖z‖ < 1) :
    cLiTwo z = ∑' n : ℕ, cLiTwoCoeff n * z ^ n := by
  rw [(cLiTwoCoeff_summable hz).tsum_eq_zero_add]
  simp only [cLiTwoCoeff_zero, zero_mul, zero_add, cLiTwoCoeff_succ]
  unfold cLiTwo
  refine tsum_congr fun k => ?_
  rw [div_eq_inv_mul]

/-- Every coefficient has norm `≤ 1`: `c₀ = 0` and `‖1/n²‖ = 1/n² ≤ 1`. -/
theorem cLiTwoCoeff_norm_le_one (n : ℕ) : ‖cLiTwoCoeff n‖ ≤ 1 := by
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · simp
  · have h1 : (1 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
    have hk : (1 : ℝ) ≤ ‖(n : ℂ)‖ ^ 2 := by
      rw [Complex.norm_natCast]; nlinarith
    simp only [cLiTwoCoeff, hn.ne', if_false, norm_inv, norm_pow]
    exact inv_le_one_of_one_le₀ hk

/-- **Step 2 of the analyticity route (bean `qou-gkco`): radius `≥ 1`.**

Immediate from `cLiTwoCoeff_norm_le_one` via `le_radius_of_bound` at `r = 1`,
with no ratio test needed. Combined with `cLiTwo_eq_tsum_coeff`, this says the
defining series of `cLiTwo` is a genuine power series on the open unit disc.

Step 3 — upgrading this to `AnalyticOnNhd ℂ cLiTwo (Metric.ball 0 1)`, which
is what the identity theorem needs — is **not** done here. -/
theorem cLiTwo_radius_ge_one :
    1 ≤ (FormalMultilinearSeries.ofScalars ℂ cLiTwoCoeff).radius := by
  have h : ∀ n : ℕ,
      ‖FormalMultilinearSeries.ofScalars ℂ cLiTwoCoeff n‖ * ((1 : NNReal) : ℝ) ^ n ≤ 1 := by
    intro n
    rw [FormalMultilinearSeries.ofScalars_norm]
    simpa using cLiTwoCoeff_norm_le_one n
  simpa using FormalMultilinearSeries.le_radius_of_bound _ 1 h

/-- **Step 3: `cLiTwo` is represented by its power series on the unit ball.** -/
theorem cLiTwo_hasFPowerSeriesOnBall :
    HasFPowerSeriesOnBall cLiTwo
      (FormalMultilinearSeries.ofScalars ℂ cLiTwoCoeff) 0 1 := by
  have hrad : 0 < (FormalMultilinearSeries.ofScalars ℂ cLiTwoCoeff).radius :=
    lt_of_lt_of_le (by norm_num) cLiTwo_radius_ge_one
  refine (((FormalMultilinearSeries.ofScalars ℂ cLiTwoCoeff).hasFPowerSeriesOnBall
    hrad).mono (by norm_num) cLiTwo_radius_ge_one).congr ?_
  intro z hz
  rw [mem_emetric_ball_zero_iff] at hz
  have hz' : ‖z‖ < 1 := by
    rw [show (1 : ENNReal) = ((1 : NNReal) : ENNReal) by simp, enorm_lt_coe] at hz
    exact_mod_cast hz
  have hsum : (FormalMultilinearSeries.ofScalars ℂ cLiTwoCoeff).sum z
      = ∑' n : ℕ, cLiTwoCoeff n * z ^ n := by
    simpa [smul_eq_mul] using
      congrFun (FormalMultilinearSeries.ofScalarsSum_eq_tsum cLiTwoCoeff) z
  rw [hsum, ← cLiTwo_eq_tsum_coeff hz']

/-- **`cLiTwo` is analytic on the open unit disc.**

The hypothesis the identity theorem needs. With
`QOU.Archimedean.cLiTwo_reflection_ofReal` (the reflection identity already
proved on the real segment `(0,1)` — a set with an accumulation point), this is
what would give the complex reflection identity on the disc. That continuation
step is **not** taken here; extending past `|z| = 1` needs the inversion
formula on top. Bean `qou-gkco`. -/
theorem cLiTwo_analyticOnNhd :
    AnalyticOnNhd ℂ cLiTwo (EMetric.ball (0 : ℂ) 1) :=
  cLiTwo_hasFPowerSeriesOnBall.analyticOnNhd

/-! ### The natural domain of the reflection identity: `ball(½, ½)`

The reflection identity `Li₂ z + Li₂(1−z) = π²/6 − log z·log(1−z)` is **not**
well-posed on the unit ball: `cLiTwo (1−z)` is not given by its series there
(`|1−z|` reaches 2), and `Complex.log z` has its branch cut through it.

`Metric.ball (1/2) (1/2)` is the natural domain — the disc on the segment
`[0,1]` as diameter. On it all four ingredients are simultaneously good, and it
contains the real segment `(0,1)` where the identity is already proved
(`QOU.Archimedean.cLiTwo_reflection_ofReal`), so it is also the connected open
set an identity-theorem continuation needs. -/

/-- `ball(½,½) ⊆ ball(0,1)`, so `cLiTwo` is given by its series there. -/
theorem norm_lt_one_of_mem_ball_half {z : ℂ}
    (hz : z ∈ Metric.ball (1 / 2 : ℂ) (1 / 2)) : ‖z‖ < 1 := by
  rw [Metric.mem_ball, Complex.dist_eq] at hz
  have h : ‖z‖ ≤ ‖z - 1 / 2‖ + ‖(1 / 2 : ℂ)‖ := by
    simpa using norm_add_le (z - 1 / 2) (1 / 2 : ℂ)
  have h2 : ‖(1 / 2 : ℂ)‖ = 1 / 2 := by norm_num
  linarith

/-- `z ↦ 1 − z` maps `ball(½,½)` to itself, so `cLiTwo (1−z)` is fine too. -/
theorem one_sub_mem_ball_half {z : ℂ}
    (hz : z ∈ Metric.ball (1 / 2 : ℂ) (1 / 2)) :
    1 - z ∈ Metric.ball (1 / 2 : ℂ) (1 / 2) := by
  rw [Metric.mem_ball, Complex.dist_eq] at hz ⊢
  have : (1 : ℂ) - z - 1 / 2 = -(z - 1 / 2) := by ring
  rw [this, norm_neg]
  exact hz

/-- `Re z > 0` on `ball(½,½)`, so `log z` and `log (1−z)` avoid the branch cut. -/
theorem re_pos_of_mem_ball_half {z : ℂ}
    (hz : z ∈ Metric.ball (1 / 2 : ℂ) (1 / 2)) : 0 < z.re := by
  rw [Metric.mem_ball, Complex.dist_eq] at hz
  have h : |(z - 1 / 2).re| ≤ ‖z - 1 / 2‖ := by
    simpa using RCLike.abs_re_le_norm (z - 1 / 2)
  have hre : (z - 1 / 2).re = z.re - 1 / 2 := by simp
  rw [hre] at h
  have hlt : |z.re - 1 / 2| < 1 / 2 := lt_of_le_of_lt h hz
  have := (abs_lt.mp hlt).1
  linarith

/-- `ball(½,½) ⊆ slitPlane` — immediate from `Re z > 0`. -/
theorem mem_slitPlane_of_mem_ball_half {z : ℂ}
    (hz : z ∈ Metric.ball (1 / 2 : ℂ) (1 / 2)) : z ∈ slitPlane :=
  mem_slitPlane_iff.2 (Or.inl (re_pos_of_mem_ball_half hz))

/-! ### All four ingredients are analytic on `ball(½, ½)`

`cLiTwo z`, `cLiTwo (1−z)`, `log z`, `log (1−z)` — the pointwise form of the
three domain facts above. Together these make the reflection identity's two
sides analytic on the ball, which is the hypothesis the identity theorem
(`AnalyticOnNhd.eqOn_of_preconnected_of_frequently_eq`) consumes. -/

/-- `cLiTwo` is analytic at each point of the open unit disc. -/
theorem cLiTwo_analyticAt {z : ℂ} (hz : ‖z‖ < 1) : AnalyticAt ℂ cLiTwo z := by
  refine cLiTwo_analyticOnNhd z ?_
  rw [mem_emetric_ball_zero_iff,
    show (1 : ENNReal) = ((1 : NNReal) : ENNReal) by simp, enorm_lt_coe]
  exact_mod_cast hz

theorem cLiTwo_analyticOnNhd_ball_half :
    AnalyticOnNhd ℂ cLiTwo (Metric.ball (1 / 2 : ℂ) (1 / 2)) :=
  fun _ hz => cLiTwo_analyticAt (norm_lt_one_of_mem_ball_half hz)

/-- The reflected summand. Uses `one_sub_mem_ball_half` — this is where the
self-mapping of the ball under `z ↦ 1−z` earns its keep. -/
theorem cLiTwo_one_sub_analyticOnNhd_ball_half :
    AnalyticOnNhd ℂ (fun z => cLiTwo (1 - z)) (Metric.ball (1 / 2 : ℂ) (1 / 2)) :=
  fun _ hz =>
    AnalyticAt.comp
      (cLiTwo_analyticAt (norm_lt_one_of_mem_ball_half (one_sub_mem_ball_half hz)))
      (analyticAt_const.sub analyticAt_id)

/-- The `log`-product term. Uses `mem_slitPlane_of_mem_ball_half` on both
factors — this is where `Re z > 0` earns its keep. -/
theorem log_mul_log_one_sub_analyticOnNhd_ball_half :
    AnalyticOnNhd ℂ (fun z => Complex.log z * Complex.log (1 - z))
      (Metric.ball (1 / 2 : ℂ) (1 / 2)) := fun _ hz =>
  (analyticAt_clog (mem_slitPlane_of_mem_ball_half hz)).mul
    (AnalyticAt.clog (analyticAt_const.sub analyticAt_id)
      (mem_slitPlane_of_mem_ball_half (one_sub_mem_ball_half hz)))

/-! ### The integral representation `Li₂(y) = −∫₀¹ log(1 − yz)/z dz`

This is the identity Route 5 of the 5₂ saddle sum rule needs (bean `qou-0yqu`),
and it is also the door out of the unit disc: **the integral converges for every
`y ∉ [1,∞)` regardless of `‖y‖`**, unlike the defining series, so it *is* the
analytic continuation.

Proved here on the disc, by termwise integration. Writing `k = n − 1`, the
`k`-th term is `y^(k+1)·z^k/(k+1)`, whose integral over `[0,1]` is
`y^(k+1)/(k+1)²` — exactly the `k`-th term of `cLiTwo`'s defining series, with
no reindexing needed. The swap is
`intervalIntegral.hasSum_integral_of_dominated_convergence` with the constant
dominating bound `‖y‖^(k+1)` (using `z^k ≤ 1` and `1/(k+1) ≤ 1` on `[0,1]`),
which is geometric and hence summable.

The `y` with `‖y‖ ≥ 1` case — needed for the 5₂ root `y₁`, `‖y₁‖ = 1.52` — is
**not** here: it requires taking the right-hand side as the *definition* past
the disc and is tracked in `qou-gkco`. -/

open MeasureTheory in
/-- **The integral representation on the open unit disc.** -/
theorem cLiTwo_eq_intervalIntegral {y : ℂ} (hy : ‖y‖ < 1) :
    cLiTwo y = -∫ z in (0 : ℝ)..1, Complex.log (1 - y * (z : ℂ)) / (z : ℂ) := by
  set F : ℕ → ℝ → ℂ :=
    fun k z => y ^ (k + 1) * (z : ℂ) ^ k / ((k : ℂ) + 1) with hFdef
  -- (1) each term integrates to the corresponding coefficient of `cLiTwo`
  have hterm : ∀ k : ℕ,
      (∫ z in (0 : ℝ)..1, F k z) = y ^ (k + 1) / ((k : ℂ) + 1) ^ 2 := by
    intro k
    have hfun : (fun z : ℝ => F k z)
        = fun z : ℝ => (y ^ (k + 1) / ((k : ℂ) + 1)) * (((z ^ k : ℝ)) : ℂ) := by
      funext z
      simp only [hFdef]
      push_cast
      ring
    rw [hfun, intervalIntegral.integral_const_mul, intervalIntegral.integral_ofReal,
      integral_pow]
    have hk : ((k : ℂ) + 1) ≠ 0 := by
      have hcast : ((k : ℂ) + 1) = ((k + 1 : ℕ) : ℂ) := by push_cast; ring
      rw [hcast, Ne, Nat.cast_eq_zero]
      exact Nat.succ_ne_zero k
    push_cast
    field_simp
    ring
  -- (2) pointwise, the series sums to the integrand on `(0,1]`
  have hlim : ∀ t : ℝ, t ∈ Set.uIoc (0 : ℝ) 1 →
      HasSum (fun k => F k t) (-(Complex.log (1 - y * (t : ℂ)) / (t : ℂ))) := by
    intro t ht
    rw [Set.uIoc_of_le (by norm_num : (0 : ℝ) ≤ 1)] at ht
    have ht0 : (0 : ℝ) < t := ht.1
    have ht1 : t ≤ 1 := ht.2
    have htne : ((t : ℂ)) ≠ 0 := by
      simpa using ne_of_gt ht0
    have hyt : ‖y * (t : ℂ)‖ < 1 := by
      rw [norm_mul, Complex.norm_real, Real.norm_eq_abs, abs_of_pos ht0]
      calc ‖y‖ * t ≤ ‖y‖ * 1 := by nlinarith [norm_nonneg y]
        _ = ‖y‖ := mul_one _
        _ < 1 := hy
    have hbase := Complex.hasSum_taylorSeries_neg_log hyt
    have hshift := (hasSum_nat_add_iff' 1).mpr hbase
    simp only [Finset.sum_range_one, pow_zero, Nat.cast_zero, div_zero, sub_zero] at hshift
    have hres := hshift.div_const ((t : ℂ))
    rw [neg_div] at hres
    have hfe : (fun k : ℕ => F k t)
        = fun n : ℕ => (y * (t : ℂ)) ^ (n + 1) / (((n + 1 : ℕ)) : ℂ) / (t : ℂ) := by
      funext k
      simp only [hFdef]
      have hcast : (((k + 1 : ℕ)) : ℂ) = (k : ℂ) + 1 := by push_cast; ring
      rw [hcast]
      field_simp
      ring
    rw [hfe]
    exact hres
  -- (3) dominated convergence
  have hmeas : ∀ k : ℕ, AEStronglyMeasurable (F k)
      (MeasureTheory.volume.restrict (Set.uIoc (0 : ℝ) 1)) := by
    intro k
    refine Continuous.aestronglyMeasurable ?_
    simp only [hFdef]
    fun_prop
  have hbound : ∀ k : ℕ, ∀ᵐ t ∂(MeasureTheory.volume : Measure ℝ),
      t ∈ Set.uIoc (0 : ℝ) 1 → ‖F k t‖ ≤ ‖y‖ ^ (k + 1) := by
    intro k
    refine Filter.Eventually.of_forall fun t ht => ?_
    rw [Set.uIoc_of_le (by norm_num : (0 : ℝ) ≤ 1)] at ht
    have ht0 : (0 : ℝ) < t := ht.1
    have ht1 : t ≤ 1 := ht.2
    have hzk : |t| ^ k ≤ 1 := by
      rw [abs_of_pos ht0]
      exact pow_le_one₀ ht0.le ht1
    have hk1 : (1 : ℝ) ≤ ‖((k : ℂ) + 1)‖ := by
      have : ((k : ℂ) + 1) = ((k + 1 : ℕ) : ℂ) := by push_cast; ring
      rw [this, Complex.norm_natCast]
      exact_mod_cast Nat.one_le_iff_ne_zero.mpr (Nat.succ_ne_zero k)
    have hkpos : (0 : ℝ) < ‖((k : ℂ) + 1)‖ := by linarith
    simp only [hFdef, norm_div, norm_mul, norm_pow, Complex.norm_real, Real.norm_eq_abs]
    rw [div_le_iff₀ hkpos]
    nlinarith [pow_nonneg (norm_nonneg y) (k + 1), hzk, hk1,
      pow_nonneg (abs_nonneg t) k]
  have hsummable : Summable fun k : ℕ => ‖y‖ ^ (k + 1) := by
    simpa [pow_succ'] using (summable_geometric_of_lt_one (norm_nonneg y) hy).mul_left ‖y‖
  have hswap := intervalIntegral.hasSum_integral_of_dominated_convergence
    (bound := fun (k : ℕ) (_ : ℝ) => ‖y‖ ^ (k + 1)) (μ := MeasureTheory.volume)
    (a := (0 : ℝ)) (b := 1) hmeas hbound
    (Filter.Eventually.of_forall fun _ _ => hsummable)
    (intervalIntegrable_const)
    (Filter.Eventually.of_forall hlim)
  -- (4) match the two HasSum statements
  simp only [hterm] at hswap
  have hcli : HasSum (fun k : ℕ => y ^ (k + 1) / ((k : ℂ) + 1) ^ 2) (cLiTwo y) :=
    (cLiTwo_summable hy).hasSum
  rw [hcli.unique hswap, intervalIntegral.integral_neg]

/-! ### Past the disc: the integral as the definition

`cLiTwo` is a `tsum`, so outside the closed unit disc it is junk-valued `0` —
the *inversion* formula `Li₂ z + Li₂(1/z) = −π²/6 − ½Log(−z)²` is not merely
unproved for it, it is **false**. Anything that needs `Li₂` at `‖y‖ > 1` (the
5₂ saddle root `y₁`, `‖y₁‖ = 1.52`) has to use a different object.

`cLiTwoExt` below is that object: the standard integral definition, which makes
sense for every `y` such that `1 − yz ≠ 0` on `[0,1]` — in particular for all
`y ∉ [1,∞)` — with no reference to convergence of the series.

**Labelling — updated 2026-08-08.** `cLiTwoExt` agrees with `cLiTwo` on the open
disc (`cLiTwoExt_eq_cLiTwo`), and it is now **proved analytic** on `ℂ ∖ [1,∞)`
in `QOU/MathlibExt/ComplexDilogarithmDeriv.lean`
(`analyticOnNhd_cLiTwoExt`), by differentiation under the integral sign. So
"the analytic continuation" is a theorem, not a name.

This paragraph previously said analyticity was "not proved here … not a theorem
in this file". That is no longer true and the sentence would now be a false
claim in the corpus, which is why it is rewritten rather than left standing.
Uniqueness too: `eqOn_cLiTwoExt_of_eqOn_ball` in
`QOU/MathlibExt/ComplexDilogarithmUnique.lean` shows any analytic function on
`ℂ ∖ [1,∞)` agreeing with the series on the disc *is* `cLiTwoExt`, so it is
**the** continuation and not merely *a* one. Bean `qou-clx8`. -/

/-- The dilogarithm by its integral definition, valid past the unit disc.

    `Li₂(y) = −∫₀¹ log(1 − yz)/z dz`

Junk-valued (`0`) where the integrand fails to be integrable, per Mathlib's
convention; every lemma about it carries the relevant hypothesis. -/
noncomputable def cLiTwoExt (y : ℂ) : ℂ :=
  -∫ z in (0 : ℝ)..1, Complex.log (1 - y * (z : ℂ)) / (z : ℂ)

/-- On the open unit disc the integral definition and the series agree. -/
theorem cLiTwoExt_eq_cLiTwo {y : ℂ} (hy : ‖y‖ < 1) : cLiTwoExt y = cLiTwo y :=
  (cLiTwo_eq_intervalIntegral hy).symm

@[simp] theorem cLiTwoExt_zero : cLiTwoExt 0 = 0 := by
  rw [cLiTwoExt_eq_cLiTwo (by norm_num), cLiTwo_zero]

/-! ### Integrability of the `cLiTwoExt` integrand

`log(1 − yz)/z` looks singular at `z = 0` and is not: `log(1 − yz) ∼ −yz`, so
the quotient extends continuously with value `−y`. Formally that value is the
*slope* of `z ↦ log(1 − yz)` at `0`, whose derivative there is `−y`.

The hypothesis `Re(1 − yz) > 0` on `[0,1]` is not cosmetic: it keeps `1 − yz`
inside `slitPlane`, without which `Complex.log` is discontinuous and the
integral representation is simply wrong. It holds for the 5₂ saddle roots —
`Re(1 − y₁z) = 1 − 0.785z` and `Re(1 − y₃z) = 1 − 0.430z`, both positive on
`[0,1]`. -/

open MeasureTheory in
/-- **The `cLiTwoExt` integrand is interval-integrable on `[0,1]`** when
`1 − yz` stays in the open right half-plane there. -/
theorem intervalIntegrable_log_one_sub_div_of_slitPlane {y : ℂ}
    (hslit : ∀ z : ℝ, 0 ≤ z → z ≤ 1 → (1 - y * (z : ℂ)) ∈ slitPlane) :
    IntervalIntegrable (fun z : ℝ => Complex.log (1 - y * (z : ℂ)) / (z : ℂ))
      MeasureTheory.volume 0 1 := by
  have hbase : Continuous fun w : ℝ => 1 - y * (w : ℂ) :=
    continuous_const.sub (continuous_const.mul Complex.continuous_ofReal)
  -- derivative of `z ↦ log (1 − yz)` at `0` is `−y`: the removable value
  have hg : HasDerivAt (fun w : ℝ => 1 - y * (w : ℂ)) (-y) 0 := by
    simpa using (Complex.ofRealCLM.hasDerivAt (x := (0 : ℝ))).const_mul y |>.const_sub 1
  have hslit0 : (fun w : ℝ => 1 - y * (w : ℂ)) 0 ∈ slitPlane := by
    simp
  have hderiv : HasDerivAt (fun w : ℝ => Complex.log (1 - y * (w : ℂ))) (-y) 0 := by
    simpa using hg.clog_real hslit0
  -- the continuous extension
  set G : ℝ → ℂ :=
    fun z => if z = 0 then -y else Complex.log (1 - y * (z : ℂ)) / (z : ℂ) with hGdef
  have hcont : ContinuousOn G (Set.Icc (0 : ℝ) 1) := by
    intro z hz
    rcases eq_or_ne z 0 with rfl | hz0
    · refine continuousWithinAt_diff_self.mp ?_
      have hslope := hasDerivAt_iff_tendsto_slope.mp hderiv
      have hmono : nhdsWithin (0 : ℝ) (Set.Icc (0 : ℝ) 1 \ {0})
          ≤ nhdsWithin (0 : ℝ) ({(0 : ℝ)}ᶜ) := nhdsWithin_mono _ fun w hw => hw.2
      have htend : Filter.Tendsto G (nhdsWithin (0 : ℝ) (Set.Icc (0 : ℝ) 1 \ {0}))
          (nhds (-y)) := by
        refine (hslope.mono_left hmono).congr' ?_
        refine Filter.eventuallyEq_of_mem self_mem_nhdsWithin fun w hw => ?_
        have hw0 : w ≠ 0 := hw.2
        simp only [hGdef, if_neg hw0, slope]
        rw [div_eq_inv_mul]
        simp [Complex.ofReal_inv]
      have hG0 : G 0 = -y := by simp [hGdef]
      rw [ContinuousWithinAt, hG0]
      exact htend
    · have hslitz : (1 - y * (z : ℂ)) ∈ slitPlane := hslit z hz.1 hz.2
      have hcz : ContinuousWithinAt
          (fun w : ℝ => Complex.log (1 - y * (w : ℂ)) / (w : ℂ)) (Set.Icc (0 : ℝ) 1) z := by
        refine ContinuousWithinAt.div ?_ ?_ (by simpa using hz0)
        · exact ContinuousAt.comp_continuousWithinAt (g := Complex.log)
            (f := fun w : ℝ => 1 - y * (w : ℂ)) (continuousAt_clog hslitz)
            hbase.continuousWithinAt
        · exact Complex.continuous_ofReal.continuousWithinAt
      refine hcz.congr_of_eventuallyEq ?_ (by simp [hGdef, hz0])
      filter_upwards [(eventually_ne_nhds hz0).filter_mono nhdsWithin_le_nhds] with w hw
      simp [hGdef, hw]
  have hGint : IntervalIntegrable G MeasureTheory.volume 0 1 :=
    (hcont.mono (by rw [Set.uIcc_of_le (by norm_num : (0:ℝ) ≤ 1)])).intervalIntegrable
  rw [intervalIntegrable_iff_integrableOn_Ioc_of_le (by norm_num : (0:ℝ) ≤ 1)] at hGint ⊢
  refine hGint.congr_fun (fun w hw => ?_) measurableSet_Ioc
  simp [hGdef, ne_of_gt hw.1]

/-- The original right-half-plane form, now a corollary. `Re(1 − yz) > 0` is
**sufficient but not necessary** — it excludes most of `ℂ ∖ [1,∞)`, e.g.
`y = 1.5 + 0.3i`. See `QOU/MathlibExt/ComplexDilogarithmSlit.lean` for the sharp
hypothesis. Kept because `FiveTwoSumRuleIntegrand` documents this name. -/
theorem intervalIntegrable_log_one_sub_div {y : ℂ}
    (hre : ∀ z : ℝ, 0 ≤ z → z ≤ 1 → 0 < (1 - y * (z : ℂ)).re) :
    IntervalIntegrable (fun z : ℝ => Complex.log (1 - y * (z : ℂ)) / (z : ℂ))
      MeasureTheory.volume 0 1 :=
  intervalIntegrable_log_one_sub_div_of_slitPlane
    (fun z h0 h1 => mem_slitPlane_iff.2 (Or.inl (hre z h0 h1)))

/-! ### Conjugation symmetry — Schwarz reflection, for free

`cLiTwoExt` is an integral over a **real** interval of `log(1 − yz)/z`, and every
piece of that integrand commutes with conjugation: `z̄ = z` on the reals,
`conj(1 − yz) = 1 − ȳz`, and `Complex.log` commutes with `conj` off the cut. So
`Li₂(ȳ) = conj (Li₂ y)` needs no analytic continuation at all — it is the
integral definition read twice.

**The hypothesis `y.im ≠ 0` cannot be dropped**, and this is not a technicality
of the proof: on the cut the statement is *false*. At `y = 5`, `conj y = y`, so
it would assert `Li₂(5) ∈ ℝ`, and `mpmath` gives
`Li₂(5) = 1.78371916127 − 5.05619832211i`. Measured off the axis it holds
exactly — residual `0.0` at 40 dps at the five `5₂` arguments, and still `0.0`
at `1e−7` from the cut on either side of `Re = 5`.

This is what `QOU.Archimedean.FiveTwoOhtsukiBridge.IsKummerAtOhtsukiArgs.of_upper_half_plane`
consumes to reach the three lower-half-plane arguments of Ohtsuki's sum from
`QOU.Knot.KummerRadial.kummer`, which is proved only for `Im z > 0`. -/

/-- Conjugation passes through an interval integral, with **no integrability
hypothesis**: `conj` is a linear isometry, so where `f` fails to be integrable
so does `conj ∘ f`, and both sides are Bochner's junk value `0`. -/
theorem intervalIntegral_conj {a b : ℝ} {f : ℝ → ℂ} :
    (∫ z in a..b, (starRingEnd ℂ) (f z)) = (starRingEnd ℂ) (∫ z in a..b, f z) := by
  simp only [intervalIntegral, _root_.integral_conj, map_sub]

/-- **`Li₂(ȳ) = conj (Li₂ y)` off the real axis.** See the section docstring for
why `y.im ≠ 0` is required rather than merely convenient. -/
theorem cLiTwoExt_conj {y : ℂ} (hy : y.im ≠ 0) :
    cLiTwoExt ((starRingEnd ℂ) y) = (starRingEnd ℂ) (cLiTwoExt y) := by
  have hpt : ∀ z : ℝ,
      Complex.log (1 - (starRingEnd ℂ) y * (z : ℂ)) / (z : ℂ)
        = (starRingEnd ℂ) (Complex.log (1 - y * (z : ℂ)) / (z : ℂ)) := by
    intro z
    -- `Im (1 − yz) = −(Im y · z)`, so `1 − yz` is on the negative real axis only
    -- if `z = 0` — and there it is `1`.
    have him : (1 - y * (z : ℂ)).im = -(y.im * z) := by simp
    have harg : (1 - y * (z : ℂ)).arg ≠ Real.pi := by
      intro hc
      obtain ⟨hre, h0⟩ := Complex.arg_eq_pi_iff.mp hc
      rw [him, neg_eq_zero] at h0
      rcases mul_eq_zero.mp h0 with h | h
      · exact hy h
      · rw [show ((z : ℂ)) = 0 by exact_mod_cast h] at hre
        norm_num at hre
    have hconj : (starRingEnd ℂ) (1 - y * (z : ℂ)) = 1 - (starRingEnd ℂ) y * (z : ℂ) := by
      simp
    rw [map_div₀, ← Complex.log_conj _ harg, hconj, Complex.conj_ofReal]
  unfold cLiTwoExt
  rw [map_neg]
  refine neg_inj.mpr ?_
  rw [intervalIntegral.integral_congr (g := fun z : ℝ =>
    (starRingEnd ℂ) (Complex.log (1 - y * (z : ℂ)) / (z : ℂ))) fun z _ => hpt z]
  exact intervalIntegral_conj

/-- **`Li₂(1)` is real.** `cLiTwoExt_conj` cannot reach `y = 1` — it is on the
axis, where the conjugation identity is exactly what fails in general — so this
is proved the same way but from the *stronger* local fact: on `[0,1]` the
integrand `log(1 − z)/z` is real-valued outright, because `1 − z ≥ 0` there.

Stated as `.im = 0` rather than `= π²/6`: that is all the `5₂` bridge's `hone`
hypothesis needs, and it avoids importing an evaluation this file does not
prove. -/
theorem cLiTwoExt_one_im : (cLiTwoExt 1).im = 0 := by
  have hpt : ∀ z : ℝ, z ∈ Set.uIcc (0 : ℝ) 1 →
      (starRingEnd ℂ) (Complex.log (1 - (1 : ℂ) * (z : ℂ)) / (z : ℂ))
        = Complex.log (1 - (1 : ℂ) * (z : ℂ)) / (z : ℂ) := by
    intro z hz
    rw [Set.uIcc_of_le (by norm_num : (0 : ℝ) ≤ 1)] at hz
    have h1 : (1 : ℂ) - (1 : ℂ) * (z : ℂ) = ((1 - z : ℝ) : ℂ) := by push_cast; ring
    have h2 : (0 : ℝ) ≤ 1 - z := by linarith [hz.2]
    rw [h1, ← Complex.ofReal_log h2, ← Complex.ofReal_div, Complex.conj_ofReal]
  refine Complex.conj_eq_iff_im.mp ?_
  unfold cLiTwoExt
  rw [map_neg]
  refine neg_inj.mpr ?_
  rw [← intervalIntegral_conj]
  exact intervalIntegral.integral_congr hpt

end QOU.MathlibExt
