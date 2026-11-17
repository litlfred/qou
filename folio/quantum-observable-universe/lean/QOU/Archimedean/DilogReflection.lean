import QOU.Archimedean.DilogarithmArchimedeanLimit
import Mathlib.Analysis.Calculus.SmoothSeries
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Analysis.Complex.AbelLimit
import Mathlib.NumberTheory.ZetaValues
import Mathlib.Analysis.SpecialFunctions.Pow.Asymptotics
import Mathlib.Analysis.SpecialFunctions.Log.NegMulLog
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus

/-!
# Dilogarithm derivative + Euler reflection — the V1 bar-even keystone infra

Discharges the flagship honest `sorry` of `QOU.Archimedean.DilogarithmArchimedeanLimit`
— `LiTwo_reflection`, the Euler reflection `Li₂(x) + Li₂(1-x) = π²/6 − ln x·ln(1-x)`
— by building the missing analytic infra: the **derivative of the dilogarithm**
`d/dx Li₂(x) = −log(1-x)/x`, which Mathlib does not provide (no `Real.dilog`).

The build (bean milestone `qou-a3ps`):

* `dilogDerivSeries_tsum` (Brick C) — the closed form `∑ₖ xᵏ/(k+1) = −log(1-x)/x`
  for `x ≠ 0`, `|x| < 1`; pure algebra from `neg_log_one_sub_hasSum`.
* `hasDerivAt_LiTwo` (Brick A) — `HasDerivAt LiTwo (−log(1-x)/x) x` for `0 < x < 1`,
  via `hasDerivAt_tsum_of_isPreconnected` on a compact subinterval `(−r, r)`,
  `x < r < 1`, with the summable geometric bound `rⁿ`.
* `LiTwo_reflection'` (Brick B) — the reflection FE, from `g' = 0` on `(0,1)`
  plus the boundary value at the `x → 1⁻` limit.

Everything is over `ℝ` (archimedean by construction — the reflection is a
statement about the real dilogarithm's boundary regulator).

-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit; Euler reflection (Lewin 1981)
-/

namespace QOU.Archimedean

open scoped Topology
open QOU.QPochhammer

/-! ## Brick C — the derivative series closed form -/

/-- **Brick C.**  `∑ₖ xᵏ/(k+1) = −log(1-x)/x` for `x ≠ 0`, `|x| < 1`.  Pure
    algebra: `neg_log_one_sub_hasSum` gives `∑ xᵏ⁺¹/(k+1) = −log(1-x)`; divide
    by `x`. -/
theorem dilogDerivSeries_tsum {x : ℝ} (hx0 : x ≠ 0) (hx : |x| < 1) :
    ∑' k : ℕ, x ^ k / ((k : ℝ) + 1) = -Real.log (1 - x) / x := by
  have hlog : ∑' m : ℕ, x ^ (m + 1) / ((m : ℝ) + 1) = -Real.log (1 - x) :=
    (Real.hasSum_pow_div_log_of_abs_lt_one hx).tsum_eq
  have hfac : (fun m : ℕ => x ^ (m + 1) / ((m : ℝ) + 1))
      = fun m : ℕ => x * (x ^ m / ((m : ℝ) + 1)) := by
    funext m; rw [pow_succ]; ring
  rw [hfac, tsum_mul_left] at hlog
  rw [eq_div_iff hx0, mul_comm]
  exact hlog

/-! ## Brick A — the dilogarithm derivative -/

/-- Term derivative: `d/dz [ zᵏ⁺¹/(k+1)² ] = zᵏ/(k+1)`. -/
private theorem hasDerivAt_LiTwo_term (k : ℕ) (z : ℝ) :
    HasDerivAt (fun z : ℝ => z ^ (k + 1) / ((k : ℝ) + 1) ^ 2)
      (z ^ k / ((k : ℝ) + 1)) z := by
  have hp : HasDerivAt (fun z : ℝ => z ^ (k + 1)) (((k : ℝ) + 1) * z ^ k) z := by
    simpa [Nat.cast_succ] using hasDerivAt_pow (k + 1) z
  have hd := hp.div_const (((k : ℝ) + 1) ^ 2)
  have hk1 : ((k : ℝ) + 1) ≠ 0 := by positivity
  have heq : ((k : ℝ) + 1) * z ^ k / ((k : ℝ) + 1) ^ 2 = z ^ k / ((k : ℝ) + 1) := by
    rw [pow_two]; exact mul_div_mul_left _ _ hk1
  rw [← heq]; exact hd

/-- **Brick A.**  `d/dx Li₂(x) = −log(1-x)/x` for `0 < x < 1`.  Differentiates
    the `LiTwo` power series term-by-term on a compact subinterval `(−r, r)`
    with `x < r < 1`, where the derivative series is dominated by the summable
    geometric series `rⁿ`. -/
theorem hasDerivAt_LiTwo {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    HasDerivAt LiTwo (-Real.log (1 - x) / x) x := by
  set r : ℝ := (1 + x) / 2 with hr_def
  have hxr : x < r := by rw [hr_def]; linarith
  have hr1 : r < 1 := by rw [hr_def]; linarith
  have hr0 : 0 < r := by linarith
  set t : Set ℝ := Set.Ioo (-r) r with ht_def
  have ht_open : IsOpen t := isOpen_Ioo
  have ht_conn : IsPreconnected t := isPreconnected_Ioo
  have hxt : x ∈ t := by rw [ht_def]; exact ⟨by linarith, hxr⟩
  -- summable geometric bound
  have hu : Summable (fun k : ℕ => r ^ k) := summable_geometric_of_lt_one hr0.le hr1
  -- term bound on t
  have hbound : ∀ (k : ℕ) (y : ℝ), y ∈ t → ‖y ^ k / ((k : ℝ) + 1)‖ ≤ r ^ k := by
    intro k y hy
    rw [Real.norm_eq_abs, abs_div, abs_pow]
    have hyr : |y| ≤ r := by
      rw [ht_def] at hy; rw [abs_le]; exact ⟨hy.1.le, hy.2.le⟩
    have hden : |((k : ℝ) + 1)| = (k : ℝ) + 1 := abs_of_pos (by positivity)
    rw [hden]
    have h1 : |y| ^ k ≤ r ^ k := pow_le_pow_left₀ (abs_nonneg y) hyr k
    have hrk : (0 : ℝ) ≤ r ^ k := pow_nonneg hr0.le k
    calc |y| ^ k / ((k : ℝ) + 1) ≤ r ^ k / ((k : ℝ) + 1) := by gcongr
      _ ≤ r ^ k := by
          rw [div_le_iff₀ (by positivity)]; nlinarith [hrk]
  -- pointwise convergence at the base point x
  have hxabs : |x| < 1 := by rw [abs_of_pos hx0]; exact hx1
  have hg0 : Summable (fun k : ℕ => x ^ (k + 1) / ((k : ℝ) + 1) ^ 2) := by
    have hgeo : Summable (fun k : ℕ => |x| ^ k) :=
      summable_geometric_of_lt_one (abs_nonneg x) hxabs
    refine Summable.of_norm_bounded hgeo (fun k => ?_)
    rw [Real.norm_eq_abs, abs_div, abs_pow,
      abs_of_pos (show (0 : ℝ) < ((k : ℝ) + 1) ^ 2 by positivity)]
    have hxk : |x| ^ (k + 1) ≤ |x| ^ k := by
      rw [pow_succ]
      nlinarith [pow_nonneg (abs_nonneg x) k, abs_nonneg x, hxabs.le]
    have hb : |x| ^ (k + 1) / ((k : ℝ) + 1) ^ 2 ≤ |x| ^ (k + 1) := by
      rw [div_le_iff₀ (by positivity)]
      have hk0 : (0 : ℝ) ≤ (k : ℝ) := Nat.cast_nonneg k
      have hone : (1 : ℝ) ≤ ((k : ℝ) + 1) ^ 2 := by nlinarith [hk0]
      nlinarith [pow_nonneg (abs_nonneg x) (k + 1), hone]
    exact le_trans hb hxk
  have hkey := hasDerivAt_tsum_of_isPreconnected hu ht_open ht_conn
    (fun k y _ => hasDerivAt_LiTwo_term k y)
    (fun k y hy => hbound k y hy) hxt hg0 hxt
  -- rewrite the derivative value via Brick C
  have hval : ∑' k : ℕ, x ^ k / ((k : ℝ) + 1) = -Real.log (1 - x) / x :=
    dilogDerivSeries_tsum (ne_of_gt hx0) (by rw [abs_of_pos hx0]; exact hx1)
  rw [hval] at hkey
  exact hkey

/-! ## Brick B — the Euler reflection functional equation

The reflection `Li₂(x) + Li₂(1-x) = π²/6 − ln x·ln(1-x)` for `0 < x < 1`.
The proof: the function `g(x) = Li₂ x + Li₂(1-x) + ln x·ln(1-x)` has `g' ≡ 0`
on `(0,1)` (from `hasDerivAt_LiTwo` + chain/product rule), hence is constant;
the constant is pinned to `π²/6` by the `x → 1⁻` boundary limit, which needs
Abel's theorem (`Li₂ x → π²/6`), continuity of `Li₂` at `0` (`Li₂(1-x) → 0`),
and the standard `ln x·ln(1-x) → 0`. -/

open Filter Set

/-- The `LiTwo` power series in Abel-normalized form: `Li₂(x) = ∑ₙ (1/n²)·xⁿ`
    (the `n = 0` term vanishes since `1/0² = 0`). -/
theorem LiTwo_eq_powerSeries {x : ℝ} (hx : |x| < 1) :
    ∑' n : ℕ, (1 / (n : ℝ) ^ 2) * x ^ n = LiTwo x := by
  rw [LiTwo]
  have hsum : Summable (fun n : ℕ => (1 / (n : ℝ) ^ 2) * x ^ n) := by
    refine Summable.of_norm_bounded
      (summable_geometric_of_lt_one (abs_nonneg x) hx) (fun n => ?_)
    rw [Real.norm_eq_abs, abs_mul, abs_pow]
    rcases Nat.eq_zero_or_pos n with hn | hn
    · subst hn; simp
    · have hcoef : |1 / (n : ℝ) ^ 2| ≤ 1 := by
        rw [abs_of_nonneg (by positivity), div_le_one (by positivity)]
        have : (1 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
        nlinarith
      calc |1 / (n : ℝ) ^ 2| * |x| ^ n ≤ 1 * |x| ^ n := by gcongr
        _ = |x| ^ n := one_mul _
  rw [hsum.tsum_eq_zero_add]
  have h0 : (1 / ((0 : ℕ) : ℝ) ^ 2) * x ^ (0 : ℕ) = 0 := by simp
  rw [h0, zero_add]
  refine tsum_congr (fun n => ?_)
  push_cast
  ring

/-- **Abel's limit for the dilogarithm.**  `Li₂(x) → π²/6` as `x → 1⁻`.
    Mathlib's `Real.tendsto_tsum_powerSeries_nhdsWithin_lt` applied to the
    Basel series `∑ 1/n² = π²/6`. -/
theorem tendsto_LiTwo_nhdsWithin_lt_one :
    Tendsto LiTwo (𝓝[<] (1 : ℝ)) (𝓝 (Real.pi ^ 2 / 6)) := by
  have habel := Real.tendsto_tsum_powerSeries_nhdsWithin_lt
    (f := fun n : ℕ => 1 / (n : ℝ) ^ 2) (l := Real.pi ^ 2 / 6)
    hasSum_zeta_two.tendsto_sum_nat
  have hmem : Set.Ioo (-1 : ℝ) 1 ∈ 𝓝[<] (1 : ℝ) := by
    have := inter_mem_nhdsWithin (Set.Iio (1 : ℝ))
      (Ioi_mem_nhds (show (-1 : ℝ) < 1 by norm_num))
    rwa [Set.Iio_inter_Ioi] at this
  refine habel.congr' ?_
  filter_upwards [hmem] with x hx
  exact LiTwo_eq_powerSeries (abs_lt.mpr ⟨hx.1, hx.2⟩)

/-- Derivative of `x ↦ Li₂(1-x)`:  `log x / (1-x)` for `0 < x < 1` (chain rule
    on Brick A). -/
theorem hasDerivAt_LiTwo_one_sub {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    HasDerivAt (fun x => LiTwo (1 - x)) (Real.log x / (1 - x)) x := by
  have h1 : (0 : ℝ) < 1 - x := by linarith
  have h2 : (1 : ℝ) - x < 1 := by linarith
  have hinner : HasDerivAt (fun x : ℝ => 1 - x) (-1) x := by
    simpa using (hasDerivAt_id x).const_sub 1
  have hcomp := (hasDerivAt_LiTwo (x := 1 - x) h1 h2).comp x hinner
  have hval : (-Real.log (1 - (1 - x)) / (1 - x)) * (-1) = Real.log x / (1 - x) := by
    rw [show (1 : ℝ) - (1 - x) = x by ring]; ring
  rw [hval] at hcomp
  exact hcomp

/-- Derivative of `x ↦ log x · log(1-x)`:  `log(1-x)/x − log x/(1-x)` for
    `0 < x < 1` (product + chain rule). -/
theorem hasDerivAt_log_mul_log_one_sub {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    HasDerivAt (fun x => Real.log x * Real.log (1 - x))
      (Real.log (1 - x) / x - Real.log x / (1 - x)) x := by
  have h1x : (0 : ℝ) < 1 - x := by linarith
  have hxne : x ≠ 0 := ne_of_gt hx0
  have h1xne : (1 : ℝ) - x ≠ 0 := ne_of_gt h1x
  have hlogx : HasDerivAt Real.log x⁻¹ x := Real.hasDerivAt_log hxne
  have hlog1x : HasDerivAt (fun x => Real.log (1 - x)) (-(1 - x)⁻¹) x := by
    have hinner : HasDerivAt (fun x : ℝ => 1 - x) (-1) x := by
      simpa using (hasDerivAt_id x).const_sub 1
    have hc := (Real.hasDerivAt_log h1xne).comp x hinner
    simpa [mul_comm] using hc
  have hmul := hlogx.mul hlog1x
  have hval : x⁻¹ * Real.log (1 - x) + Real.log x * -(1 - x)⁻¹
      = Real.log (1 - x) / x - Real.log x / (1 - x) := by
    field_simp
    ring
  rw [hval] at hmul
  exact hmul

/-- The reflection auxiliary `g(x) = Li₂ x + Li₂(1-x) + log x·log(1-x)` has
    zero derivative on `(0,1)`. -/
theorem hasDerivAt_reflectionAux {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    HasDerivAt (fun x => LiTwo x + LiTwo (1 - x) + Real.log x * Real.log (1 - x)) 0 x := by
  have hsum := ((hasDerivAt_LiTwo hx0 hx1).add
    (hasDerivAt_LiTwo_one_sub hx0 hx1)).add (hasDerivAt_log_mul_log_one_sub hx0 hx1)
  have hval : -Real.log (1 - x) / x + Real.log x / (1 - x)
      + (Real.log (1 - x) / x - Real.log x / (1 - x)) = 0 := by ring
  rw [hval] at hsum
  exact hsum

/-- Per-term norm bound `‖xᵏ⁺¹/(k+1)²‖ ≤ |x|ᵏ⁺¹` for the `LiTwo` series. -/
private theorem norm_LiTwo_term_le {x : ℝ} (k : ℕ) :
    ‖x ^ (k + 1) / ((k : ℝ) + 1) ^ 2‖ ≤ |x| ^ (k + 1) := by
  rw [Real.norm_eq_abs, abs_div, abs_pow,
    abs_of_nonneg (show (0 : ℝ) ≤ ((k : ℝ) + 1) ^ 2 by positivity)]
  have hk0 : (0 : ℝ) ≤ (k : ℝ) := Nat.cast_nonneg k
  have hb : (1 : ℝ) ≤ ((k : ℝ) + 1) ^ 2 := by nlinarith [hk0]
  exact div_le_self (pow_nonneg (abs_nonneg x) (k + 1)) hb

set_option maxHeartbeats 800000 in
/-- **Continuity of the dilogarithm at 0**:  `Li₂(x) → 0` as `x → 0`.  Squeeze
    against `|x|/(1-|x|)` using `‖Li₂ x‖ ≤ ∑ₖ |x|ᵏ⁺¹ = |x|/(1-|x|)`. -/
theorem tendsto_LiTwo_nhds_zero : Tendsto LiTwo (𝓝 (0 : ℝ)) (𝓝 0) := by
  have hbound : ∀ᶠ x in 𝓝 (0 : ℝ), ‖LiTwo x‖ ≤ |x| / (1 - |x|) := by
    filter_upwards [Metric.ball_mem_nhds (0 : ℝ) (by norm_num : (0 : ℝ) < 1 / 2)] with x hx
    rw [Metric.mem_ball, dist_zero_right, Real.norm_eq_abs] at hx
    have hx1 : |x| < 1 := by linarith
    have hsummG : Summable (fun k : ℕ => |x| ^ (k + 1)) := by
      simpa [pow_succ] using (summable_geometric_of_lt_one (abs_nonneg x) hx1).mul_right |x|
    have hsummN : Summable (fun k : ℕ => ‖x ^ (k + 1) / ((k : ℝ) + 1) ^ 2‖) :=
      Summable.of_nonneg_of_le (fun k => norm_nonneg _) (fun k => norm_LiTwo_term_le k) hsummG
    rw [LiTwo]
    calc ‖∑' k : ℕ, x ^ (k + 1) / ((k : ℝ) + 1) ^ 2‖
        ≤ ∑' k : ℕ, ‖x ^ (k + 1) / ((k : ℝ) + 1) ^ 2‖ := norm_tsum_le_tsum_norm hsummN
      _ ≤ ∑' k : ℕ, |x| ^ (k + 1) :=
          Summable.tsum_le_tsum (fun k => norm_LiTwo_term_le k) hsummN hsummG
      _ = |x| / (1 - |x|) := by
          have hfactor : ∑' k : ℕ, |x| ^ (k + 1) = |x| * ∑' k : ℕ, |x| ^ k := by
            rw [← tsum_mul_left]; exact tsum_congr (fun k => by rw [pow_succ'])
          rw [hfactor, tsum_geometric_of_lt_one (abs_nonneg x) hx1, div_eq_mul_inv]
  have hg : Tendsto (fun x : ℝ => |x| / (1 - |x|)) (𝓝 (0 : ℝ)) (𝓝 0) := by
    have hcont : Tendsto (fun x : ℝ => |x| / (1 - |x|)) (𝓝 0)
        (𝓝 (|(0 : ℝ)| / (1 - |(0 : ℝ)|))) :=
      (continuous_abs.tendsto 0).div ((continuous_const.sub continuous_abs).tendsto 0)
        (by norm_num)
    simpa using hcont
  exact squeeze_zero_norm' hbound hg

/-- Boundary limit `Li₂(1-x) → 0` as `x → 1⁻` (continuity at 0 ∘ `x ↦ 1-x`). -/
theorem tendsto_LiTwo_one_sub_nhdsWithin_lt_one :
    Tendsto (fun x => LiTwo (1 - x)) (𝓝[<] (1 : ℝ)) (𝓝 0) := by
  have hinner : Tendsto (fun x : ℝ => 1 - x) (𝓝[<] (1 : ℝ)) (𝓝 0) := by
    have h : Tendsto (fun x : ℝ => 1 - x) (𝓝 (1 : ℝ)) (𝓝 0) := by
      have hcont : Continuous (fun x : ℝ => 1 - x) := continuous_const.sub continuous_id
      simpa using hcont.tendsto (1 : ℝ)
    exact h.mono_left nhdsWithin_le_nhds
  exact tendsto_LiTwo_nhds_zero.comp hinner

/-- Boundary limit `log x · log(1-x) → 0` as `x → 1⁻`.  Reduce to `u = 1-x → 0⁺`
    and squeeze `|log(1-u)·log u| ≤ 2·|log u · u| → 0`. -/
theorem tendsto_log_mul_log_one_sub_nhdsWithin_lt_one :
    Tendsto (fun x => Real.log x * Real.log (1 - x)) (𝓝[<] (1 : ℝ)) (𝓝 0) := by
  -- the u → 0⁺ statement
  have hcomp : Tendsto (fun u : ℝ => Real.log (1 - u) * Real.log u)
      (𝓝[>] (0 : ℝ)) (𝓝 0) := by
    have hbaseline : Tendsto (fun u : ℝ => 2 * |Real.log u * u|) (𝓝[>] (0 : ℝ)) (𝓝 0) := by
      have h0 := tendsto_log_mul_rpow_nhdsGT_zero (r := 1) one_pos
      have h1 : Tendsto (fun u : ℝ => Real.log u * u) (𝓝[>] (0 : ℝ)) (𝓝 0) := by
        refine h0.congr' (Filter.Eventually.of_forall (fun u => ?_))
        rw [Real.rpow_one]
      simpa using (h1.abs.const_mul 2)
    have hmem2 : Set.Ioo (0 : ℝ) (1 / 2) ∈ 𝓝[>] (0 : ℝ) := by
      have := inter_mem_nhdsWithin (Set.Ioi (0 : ℝ))
        (Iio_mem_nhds (show (0 : ℝ) < 1 / 2 by norm_num))
      rwa [Set.Ioi_inter_Iio] at this
    refine squeeze_zero_norm' ?_ hbaseline
    filter_upwards [hmem2] with u hu
    obtain ⟨hu0, hu2⟩ := hu
    have h1u : (0 : ℝ) < 1 - u := by linarith
    have hlognonpos : Real.log (1 - u) ≤ 0 := Real.log_nonpos (by linarith) (by linarith)
    have h1une : (1 : ℝ) - u ≠ 0 := ne_of_gt h1u
    have heq : (1 : ℝ) - (1 - u)⁻¹ = -u / (1 - u) := by field_simp; ring
    have hle : -u / (1 - u) ≤ Real.log (1 - u) := heq ▸ Real.one_sub_inv_le_log_of_pos h1u
    have hlogbound : |Real.log (1 - u)| ≤ 2 * u := by
      rw [abs_of_nonpos hlognonpos]
      rw [neg_div] at hle
      have hstep : -Real.log (1 - u) ≤ u / (1 - u) := by linarith
      have hfrac : u / (1 - u) ≤ 2 * u := by
        rw [div_le_iff₀ h1u]; nlinarith
      linarith
    rw [Real.norm_eq_abs, abs_mul]
    calc |Real.log (1 - u)| * |Real.log u|
        ≤ (2 * u) * |Real.log u| :=
          mul_le_mul_of_nonneg_right hlogbound (abs_nonneg _)
      _ = 2 * |Real.log u * u| := by rw [abs_mul, abs_of_pos hu0]; ring
  -- transport back via x ↦ 1-x : 𝓝[<]1 → 𝓝[>]0
  have htend : Tendsto (fun x : ℝ => 1 - x) (𝓝[<] (1 : ℝ)) (𝓝[>] (0 : ℝ)) := by
    apply tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within
    · have h : Tendsto (fun x : ℝ => 1 - x) (𝓝 (1 : ℝ)) (𝓝 0) := by
        have hcont : Continuous (fun x : ℝ => 1 - x) := continuous_const.sub continuous_id
        simpa using hcont.tendsto (1 : ℝ)
      exact h.mono_left nhdsWithin_le_nhds
    · filter_upwards [self_mem_nhdsWithin] with x hx
      simp only [Set.mem_Ioi]
      have : x < 1 := hx
      linarith
  have := hcomp.comp htend
  refine this.congr (fun x => ?_)
  simp only [Function.comp_apply, sub_sub_cancel]

/-- **Brick B — the Euler reflection functional equation.**
    `Li₂(x) + Li₂(1-x) = π²/6 − log x·log(1-x)` for `0 < x < 1`.  The
    auxiliary `g = Li₂ x + Li₂(1-x) + log x·log(1-x)` is constant on `(0,1)`
    (`g' ≡ 0`), and its `x → 1⁻` boundary value is `π²/6`. -/
theorem LiTwo_reflection' (x : ℝ) (hx0 : 0 < x) (hx1 : x < 1) :
    LiTwo x + LiTwo (1 - x) = Real.pi ^ 2 / 6 - Real.log x * Real.log (1 - x) := by
  set g : ℝ → ℝ :=
    fun x => LiTwo x + LiTwo (1 - x) + Real.log x * Real.log (1 - x) with hg
  -- g is constant on Ioo 0 1
  have hconst : ∀ y ∈ Set.Ioo (0 : ℝ) 1, g y = g x := by
    intro y hy
    refine IsOpen.is_const_of_deriv_eq_zero isOpen_Ioo isPreconnected_Ioo ?_ ?_ hy ⟨hx0, hx1⟩
    · intro z hz
      exact (hasDerivAt_reflectionAux hz.1 hz.2).differentiableAt.differentiableWithinAt
    · intro z hz
      exact (hasDerivAt_reflectionAux hz.1 hz.2).deriv
  -- boundary value of g at x → 1⁻ is π²/6
  have hgtend : Tendsto g (𝓝[<] (1 : ℝ)) (𝓝 (Real.pi ^ 2 / 6)) := by
    have := (tendsto_LiTwo_nhdsWithin_lt_one.add
      tendsto_LiTwo_one_sub_nhdsWithin_lt_one).add
      tendsto_log_mul_log_one_sub_nhdsWithin_lt_one
    simpa using this
  -- but g ≡ g x near 1⁻, so g x = π²/6
  have hmem : Set.Ioo (0 : ℝ) 1 ∈ 𝓝[<] (1 : ℝ) := by
    have := inter_mem_nhdsWithin (Set.Iio (1 : ℝ))
      (Ioi_mem_nhds (show (0 : ℝ) < 1 by norm_num))
    rwa [Set.Iio_inter_Ioi] at this
  have hgconst : Tendsto g (𝓝[<] (1 : ℝ)) (𝓝 (g x)) := by
    refine tendsto_const_nhds.congr' ?_
    filter_upwards [hmem] with y hy using (hconst y hy).symm
  have hgx : g x = Real.pi ^ 2 / 6 := tendsto_nhds_unique hgconst hgtend
  simp only [hg] at hgx
  linarith

/-- **Special value** `Li₂(½) = π²/12 − (ln 2)²/2`, the reflection FE at
    `x = ½` (Lewin 1.16).  A clean immediate corollary of `LiTwo_reflection'`. -/
theorem LiTwo_half : LiTwo (1 / 2) = Real.pi ^ 2 / 12 - Real.log 2 ^ 2 / 2 := by
  have h := LiTwo_reflection' (1 / 2) (by norm_num) (by norm_num)
  rw [show (1 : ℝ) - 1 / 2 = 1 / 2 by norm_num,
    show Real.log (1 / 2) = -Real.log 2 by rw [one_div, Real.log_inv]] at h
  nlinarith [h]

/-! ## Integral representation — Part A of `conj:dilogarithm-archimedean-limit`

`Li₂(x) = ∫₀ˣ −log(1-t)/t dt` for `0 < x < 1`, the FTC applied to
`hasDerivAt_LiTwo` (Brick A) + `LiTwo_zero`.  This is the integral-representation
half of the conjecture's **Part A** (the elementary `q → 1⁻` side, per
`docs/audits/2026-06-07-dilog-archimedean-limit-part-A-elementary.md`).  The
integrand is bounded by `1/(1-x)` on `(0,x]` — from
`Real.one_sub_inv_le_log_of_pos` — so interval-integrability needs no
removable-singularity limit. -/

open MeasureTheory in
/-- **Integral representation** `Li₂(x) = ∫₀ˣ −log(1-t)/t dt` for `0 < x < 1`. -/
theorem LiTwo_eq_integral {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    LiTwo x = ∫ t in (0 : ℝ)..x, -Real.log (1 - t) / t := by
  -- the integrand is continuous on the half-open interval (0, x]
  have hcontOn : ContinuousOn (fun t : ℝ => -Real.log (1 - t) / t) (Set.Ioc 0 x) := by
    refine ContinuousOn.div ?_ continuousOn_id (fun t ht => ne_of_gt ht.1)
    refine ContinuousOn.neg (ContinuousOn.log
      ((continuous_const.sub continuous_id).continuousOn) (fun t ht => ?_))
    exact ne_of_gt (by have := ht.2; linarith)
  -- interval-integrability via the uniform bound 1/(1-x) on (0,x]
  have hint : IntervalIntegrable (fun t => -Real.log (1 - t) / t) volume 0 x := by
    rw [intervalIntegrable_iff_integrableOn_Ioc_of_le hx0.le]
    have hmeas : AEStronglyMeasurable (fun t => -Real.log (1 - t) / t)
        (volume.restrict (Set.Ioc 0 x)) := hcontOn.aestronglyMeasurable measurableSet_Ioc
    haveI : IsFiniteMeasure (volume.restrict (Set.Ioc (0 : ℝ) x)) :=
      ⟨by rw [Measure.restrict_apply_univ]; exact measure_Ioc_lt_top⟩
    refine Integrable.mono' (g := fun _ => 1 / (1 - x)) (integrable_const _) hmeas ?_
    refine ae_restrict_of_forall_mem measurableSet_Ioc (fun t ht => ?_)
    obtain ⟨ht0, htx⟩ := ht
    have h1t : (0 : ℝ) < 1 - t := by linarith
    have h1x : (0 : ℝ) < 1 - x := by linarith
    have hnn : (0 : ℝ) ≤ -Real.log (1 - t) := by
      have hlp : Real.log (1 - t) ≤ 0 := Real.log_nonpos (by linarith) (by linarith)
      linarith
    have hlog2 : -Real.log (1 - t) * (1 - t) ≤ t := by
      have hmul : (1 - (1 - t)⁻¹) * (1 - t) ≤ Real.log (1 - t) * (1 - t) :=
        mul_le_mul_of_nonneg_right (Real.one_sub_inv_le_log_of_pos h1t) h1t.le
      have hlhs : (1 - (1 - t)⁻¹) * (1 - t) = -t := by field_simp; ring
      rw [hlhs] at hmul; nlinarith [hmul]
    rw [Real.norm_eq_abs, abs_of_nonneg (div_nonneg hnn ht0.le), div_le_iff₀ ht0,
      one_div, inv_mul_eq_div, le_div_iff₀ h1x]
    have hle : -Real.log (1 - t) * (1 - x) ≤ -Real.log (1 - t) * (1 - t) :=
      mul_le_mul_of_nonneg_left (by linarith) hnn
    linarith [hle, hlog2]
  -- derivative on the open interval + continuity on the closed interval
  have hderiv : ∀ t ∈ Set.Ioo (0 : ℝ) x,
      HasDerivWithinAt LiTwo (-Real.log (1 - t) / t) (Set.Ioi t) t :=
    fun t ht => (hasDerivAt_LiTwo ht.1 (lt_trans ht.2 hx1)).hasDerivWithinAt
  have hcont : ContinuousOn LiTwo (Set.Icc 0 x) := by
    intro t ht
    rcases eq_or_lt_of_le ht.1 with rfl | h0
    · show Tendsto LiTwo (𝓝[Set.Icc 0 x] 0) (𝓝 (LiTwo 0))
      rw [LiTwo_zero]
      exact tendsto_LiTwo_nhds_zero.mono_left nhdsWithin_le_nhds
    · exact ((hasDerivAt_LiTwo h0 (lt_of_le_of_lt ht.2 hx1)).continuousAt).continuousWithinAt
  have hftc := intervalIntegral.integral_eq_sub_of_hasDeriv_right_of_le hx0.le hcont hderiv hint
  rw [LiTwo_zero, sub_zero] at hftc
  exact hftc.symm

/-! ## Rescaled to the unit interval — the shape Route 5 of the 5₂ sum rule needs

`LiTwo_eq_integral` integrates over `[0, x]`, with the argument as the *endpoint*.
Route 5 (bean `qou-0yqu`) needs the argument inside the *integrand* over a fixed
range, because that is what turns a product over roots into a single logarithm:

    Σⱼ Li₂(yⱼ) = −∫₀¹ log ∏ⱼ(1 − yⱼz) / z dz = −∫₀¹ log(1 − 2z + 3z² − z³)/z dz

the factorisation being `QOU.QBeta.FiveTwo.prod_one_sub_mul_eq`, and the
resulting integral convergent by
`QOU.QBeta.FiveTwo.intervalIntegrable_log_recipCubic_div`.

The substitution `t = y·z` is all that separates the two shapes. Note this
lemma is real and needs `0 < y < 1`, so on its own it covers only the real
saddle root `y₃ = 0.4301…`; the conjugate pair `y₁, y₂` has `|y₁| = 1.52` and
is not reached here. -/

open MeasureTheory in
/-- **Unit-interval integral representation**: `Li₂(y) = −∫₀¹ log(1 − yz)/z dz`
for `0 < y < 1`. The substitution `t = y·z` in `LiTwo_eq_integral`. -/
theorem LiTwo_eq_integral_unit {y : ℝ} (hy0 : 0 < y) (hy1 : y < 1) :
    LiTwo y = -∫ z in (0 : ℝ)..1, Real.log (1 - y * z) / z := by
  have hy : y ≠ 0 := ne_of_gt hy0
  -- the substitution `t = y·z`
  have hcomp : (∫ z in (0 : ℝ)..1, -Real.log (1 - y * z) / (y * z))
      = y⁻¹ • ∫ t in (y * 0 : ℝ)..(y * 1), -Real.log (1 - t) / t :=
    intervalIntegral.integral_comp_mul_left (fun t : ℝ => -Real.log (1 - t) / t) hy
  -- pull the constant `y⁻¹` out of the integrand
  have hpt : ∀ z : ℝ, -Real.log (1 - y * z) / (y * z)
      = y⁻¹ * (-Real.log (1 - y * z) / z) := by
    intro z
    rcases eq_or_ne z 0 with rfl | hz
    · simp
    · field_simp
  have hleft : (∫ z in (0 : ℝ)..1, -Real.log (1 - y * z) / (y * z))
      = y⁻¹ * ∫ z in (0 : ℝ)..1, -Real.log (1 - y * z) / z := by
    rw [← intervalIntegral.integral_const_mul]
    exact intervalIntegral.integral_congr fun z _ => hpt z
  rw [hleft, mul_zero, mul_one, ← LiTwo_eq_integral hy0 hy1, smul_eq_mul] at hcomp
  have hcancel : (∫ z in (0 : ℝ)..1, -Real.log (1 - y * z) / z) = LiTwo y :=
    mul_left_cancel₀ (inv_ne_zero hy) hcomp
  rw [← hcancel, ← intervalIntegral.integral_neg]
  exact intervalIntegral.integral_congr fun z _ => by rw [neg_div]

/-- **Two-point reflection difference identity**: for `x, y ∈ (0, 1)`, the difference
between `Li₂(x) + Li₂(1 − x)` and `Li₂(y) + Li₂(1 − y)` eliminates `π²/6` and equals
`log y · log(1 − y) − log x · log(1 − x)`. -/
theorem LiTwo_reflection_diff_symm (x y : ℝ)
    (hx0 : 0 < x) (hx1 : x < 1) (hy0 : 0 < y) (hy1 : y < 1) :
    (LiTwo x + LiTwo (1 - x)) - (LiTwo y + LiTwo (1 - y)) =
      Real.log y * Real.log (1 - y) - Real.log x * Real.log (1 - x) := by
  have hx := LiTwo_reflection' x hx0 hx1
  have hy := LiTwo_reflection' y hy0 hy1
  have hsub : (LiTwo x + LiTwo (1 - x)) - (LiTwo y + LiTwo (1 - y)) =
      (Real.pi ^ 2 / 6 - Real.log x * Real.log (1 - x)) -
        (Real.pi ^ 2 / 6 - Real.log y * Real.log (1 - y)) := by
    rw [hx, hy]
  linarith

/-- **Midpoint comparison for the reflection sum**: for any `x ∈ (0, 1)`,
`(Li₂(x) + Li₂(1 − x)) − 2 Li₂(1/2) = (log 2)² − log x · log(1 − x)`. -/
theorem LiTwo_sum_sub_two_LiTwo_half (x : ℝ) (hx0 : 0 < x) (hx1 : x < 1) :
    (LiTwo x + LiTwo (1 - x)) - 2 * LiTwo (1 / 2) =
      Real.log 2 ^ 2 - Real.log x * Real.log (1 - x) := by
  have hrefl := LiTwo_reflection' x hx0 hx1
  have hhalf := LiTwo_half
  have hrew : (LiTwo x + LiTwo (1 - x)) - 2 * LiTwo (1 / 2) =
      (Real.pi ^ 2 / 6 - Real.log x * Real.log (1 - x)) -
        2 * (Real.pi ^ 2 / 12 - Real.log 2 ^ 2 / 2) := by
    rw [hrefl, hhalf]
  linarith

end QOU.Archimedean
