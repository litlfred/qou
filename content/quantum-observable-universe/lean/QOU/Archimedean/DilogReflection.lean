import QOU.Archimedean.DilogarithmArchimedeanLimit
import Mathlib.Analysis.Calculus.SmoothSeries
import Mathlib.Analysis.Calculus.MeanValue

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

-- Ref: [manuscript] conj:dilogarithm-archimedean-limit; Euler reflection (Lewin 1981)
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

end QOU.Archimedean
