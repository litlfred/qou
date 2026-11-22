import Mathlib.Analysis.Complex.JensenFormula
import Mathlib.Analysis.Complex.ValueDistribution.CountingFunction
import Mathlib.Analysis.SpecialFunctions.Integrability.LogMeromorphic

/-!
# Jensen's formula and the zero-counting bound for entire functions (PI-5 bridge)

Bean `qou-bp5n`. Mathlib v4.24.0 already has Jensen's formula
(`MeromorphicOn.circleAverage_log_norm`) and the Nevanlinna logarithmic counting
function (`ValueDistribution.logCounting`). Nothing here rebuilds them. This file
specialises them to the form the Hadamard factorization (`QOU.Mathlib.HadamardFactorization`,
PI-4/PI-5) consumes.

* `jensen_entire` — the classical Jensen formula for an entire `f` with `f 0 ≠ 0`:
  `∑ᶠ u, ord_u f · log (R/‖u‖) = (1/2π)∮ log‖f‖ − log‖f 0‖`,
  summing over the zeros in `closedBall 0 R`.
* `logCounting_zero_eq` — Mathlib's `logCounting f 0 R` is that classical sum
  `N(R)` when `f 0 ≠ 0`. This answers step 1 of the bean: it needs one unfolding
  lemma, not a rebuild.
* `jensen_entire_le` — `N(R) ≤ log M − log‖f 0‖` when `‖f‖ ≤ M` (with `1 ≤ M`)
  on the circle `‖z‖ = R`.
* `zero_count_le` — the zero-counting bound: the number of zeros of `f` in
  `‖z‖ ≤ r`, counted with multiplicity, satisfies
  `n(r) · log 2 ≤ log M − log‖f 0‖` when `‖f‖ ≤ M` on `‖z‖ = 2r`.
  This is the estimate that turns a growth bound `M(2r) ≤ exp(C (2r)^ρ)` into
  `n(r) = O(r^ρ)`, the input to "exponent of convergence ≤ order" (bean `qou-c3if`).

§7c: archimedean throughout (norms, `Real.log`, circle averages), so `ℝ`/`ℂ` are genuine.

-- Ref: [leitner2026] standard complex analysis: Ahlfors, *Complex Analysis*, 3rd ed.,
   §5.3.1 (Jensen's formula) and §5.3.2 (the zero-counting estimate in Hadamard's theorem).
-/

open Real Metric Set Function

namespace QOU.Mathlib.JensenZeroCounting

/-- The divisor of an analytic function vanishes at a point where the function is nonzero. -/
lemma divisor_eq_zero_of_ne_zero {f : ℂ → ℂ} {U : Set ℂ} (hf : AnalyticOnNhd ℂ f U)
    {z : ℂ} (hz : z ∈ U) (hfz : f z ≠ 0) :
    MeromorphicOn.divisor f U z = 0 := by
  rw [MeromorphicOn.divisor_apply hf.meromorphicOn hz, (hf z hz).meromorphicOrderAt_eq,
    ((hf z hz).analyticOrderAt_eq_zero).mpr hfz]
  simp

/-- **Jensen's formula, classical form, for entire functions.** For `f` entire with
`f 0 ≠ 0` and `R ≠ 0`, summing over the zeros `u` of `f` in `closedBall 0 |R|`
weighted by their order:
`∑ᶠ u, ord_u f · log (R · ‖u‖⁻¹) = circleAverage (log ‖f‖) 0 R − log ‖f 0‖`. -/
theorem jensen_entire {f : ℂ → ℂ} (hf : Differentiable ℂ f) (hf0 : f 0 ≠ 0) {R : ℝ}
    (hR : R ≠ 0) :
    ∑ᶠ u, (MeromorphicOn.divisor f (closedBall 0 |R|) u : ℝ) * log (R * ‖u‖⁻¹)
      = circleAverage (log ‖f ·‖) 0 R - log ‖f 0‖ := by
  have han : AnalyticOnNhd ℂ f (closedBall 0 |R|) := fun z _ => hf.analyticAt z
  have hmero : MeromorphicOn f (closedBall 0 |R|) := han.meromorphicOn
  have h0mem : (0 : ℂ) ∈ closedBall (0 : ℂ) |R| := by simp
  have hd0 := divisor_eq_zero_of_ne_zero han h0mem hf0
  have htc : meromorphicTrailingCoeffAt f 0 = f 0 :=
    (hf.analyticAt 0).meromorphicTrailingCoeffAt_of_ne_zero hf0
  rw [MeromorphicOn.circleAverage_log_norm hR hmero, hd0, htc]
  simp

/-- Mathlib's logarithmic counting function of the zeros, `logCounting f 0 R`, is the
classical `N(R) = ∑ ord_u f · log (R/‖u‖)` over the zeros in `‖u‖ ≤ R`, once `f 0 ≠ 0`
(the `log R`-correction term of the Mathlib definition then vanishes). -/
theorem logCounting_zero_eq {f : ℂ → ℂ} (hf : Differentiable ℂ f) (hf0 : f 0 ≠ 0)
    {R : ℝ} :
    ValueDistribution.logCounting f 0 R
      = ∑ᶠ u, (MeromorphicOn.divisor f (closedBall 0 |R|) u : ℝ) * log (R * ‖u‖⁻¹) := by
  have han : AnalyticOnNhd ℂ f univ := fun z _ => hf.analyticAt z
  have hd0 : MeromorphicOn.divisor f univ 0 = 0 :=
    divisor_eq_zero_of_ne_zero han (mem_univ 0) hf0
  have hpos : (MeromorphicOn.divisor f univ)⁺ = MeromorphicOn.divisor f univ :=
    posPart_eq_self.mpr (MeromorphicOn.AnalyticOnNhd.divisor_nonneg han)
  rw [ValueDistribution.logCounting_zero, hpos]
  simp only [Function.locallyFinsuppWithin.logCounting, AddMonoidHom.coe_mk, ZeroHom.coe_mk,
    hd0, Int.cast_zero, zero_mul, add_zero]
  refine finsum_congr fun u => ?_
  rw [Function.locallyFinsuppWithin.toClosedBall,
    Function.locallyFinsuppWithin.restrictMonoidHom_apply,
    MeromorphicOn.divisor_restrict han.meromorphicOn (subset_univ _)]

/-- **Jensen's inequality.** If `‖f z‖ ≤ M` on `‖z‖ = |R|` with `1 ≤ M`, then
`N(R) ≤ log M − log ‖f 0‖`. (`1 ≤ M` absorbs Mathlib's convention `log 0 = 0` at
zeros of `f` on the circle.) -/
theorem jensen_entire_le {f : ℂ → ℂ} (hf : Differentiable ℂ f) (hf0 : f 0 ≠ 0) {R M : ℝ}
    (hR : R ≠ 0) (hM : 1 ≤ M) (hbound : ∀ z ∈ sphere (0 : ℂ) |R|, ‖f z‖ ≤ M) :
    ∑ᶠ u, (MeromorphicOn.divisor f (closedBall 0 |R|) u : ℝ) * log (R * ‖u‖⁻¹)
      ≤ log M - log ‖f 0‖ := by
  rw [jensen_entire hf hf0 hR]
  have hint : CircleIntegrable (log ‖f ·‖) 0 R :=
    circleIntegrable_log_norm_meromorphicOn (fun z _ => (hf.analyticAt z).meromorphicAt)
  have hle : circleAverage (log ‖f ·‖) 0 R ≤ log M := by
    refine circleAverage_mono_on_of_le_circle hint fun z hz => ?_
    by_cases hz0 : f z = 0
    · simp [hz0, log_nonneg hM]
    · exact log_le_log (norm_pos_iff.mpr hz0) (hbound z hz)
  linarith

open Classical in
/-- **The zero-counting bound.** Let `f` be entire with `f 0 ≠ 0`, `r > 0`, and
`‖f z‖ ≤ M` (with `1 ≤ M`) on `‖z‖ = 2r`. Then the number of zeros of `f` in `‖z‖ ≤ r`,
counted with multiplicity, `n(r) = ∑ᶠ u, ord_u f`, satisfies
`n(r) · log 2 ≤ log M − log ‖f 0‖`. -/
theorem zero_count_le {f : ℂ → ℂ} (hf : Differentiable ℂ f) (hf0 : f 0 ≠ 0) {r M : ℝ}
    (hr : 0 < r) (hM : 1 ≤ M) (hbound : ∀ z ∈ sphere (0 : ℂ) (2 * r), ‖f z‖ ≤ M) :
    (∑ᶠ u, (MeromorphicOn.divisor f (closedBall 0 r) u : ℝ)) * log 2
      ≤ log M - log ‖f 0‖ := by
  have hR : (2 * r) ≠ 0 := by positivity
  have habs : |2 * r| = 2 * r := abs_of_pos (by positivity)
  have hJ := jensen_entire_le hf hf0 hR hM (by rwa [habs])
  rw [habs] at hJ
  refine le_trans ?_ hJ
  set Dr := MeromorphicOn.divisor f (closedBall (0 : ℂ) r)
  set D := MeromorphicOn.divisor f (closedBall (0 : ℂ) (2 * r))
  have hanD : AnalyticOnNhd ℂ f (closedBall 0 (2 * r)) := fun z _ => hf.analyticAt z
  have hsub : closedBall (0 : ℂ) r ⊆ closedBall 0 (2 * r) :=
    closedBall_subset_closedBall (by linarith)
  -- `Dr` is the restriction of `D`.
  have hDr : ∀ u, (Dr u : ℝ) = if u ∈ closedBall (0 : ℂ) r then (D u : ℝ) else 0 := by
    intro u
    simp only [Dr]
    rw [← MeromorphicOn.divisor_restrict hanD.meromorphicOn hsub,
      Function.locallyFinsuppWithin.restrict_apply]
    split_ifs <;> simp [D]
  have hDnn : ∀ u, (0 : ℝ) ≤ D u := fun u => by
    exact_mod_cast MeromorphicOn.AnalyticOnNhd.divisor_nonneg hanD u
  have hfin : D.support.Finite := D.finiteSupport (isCompact_closedBall 0 _)
  have hsubD : (fun u => (D u : ℝ) * log (2 * r * ‖u‖⁻¹)).support ⊆ hfin.toFinset := by
    intro u hu; simp only [Set.Finite.coe_toFinset, mem_support]; intro h; simp_all
  have hsubDr : (fun u => (Dr u : ℝ)).support ⊆ hfin.toFinset := by
    intro u hu
    simp only [Set.Finite.coe_toFinset, mem_support]
    intro h; rw [mem_support, hDr] at hu; split_ifs at hu <;> simp_all [D]
  rw [finsum_eq_sum_of_support_subset _ hsubD, finsum_eq_sum_of_support_subset _ hsubDr,
    Finset.sum_mul]
  refine Finset.sum_le_sum fun u hu => ?_
  rw [hDr u]
  have hu' : u ∈ D.support := by simpa using hu
  have huball : u ∈ closedBall (0 : ℂ) (2 * r) := D.supportWithinDomain hu'
  rw [mem_closedBall, dist_zero_right] at huball
  by_cases hur : u ∈ closedBall (0 : ℂ) r
  · rw [if_pos hur]
    rw [mem_closedBall, dist_zero_right] at hur
    refine mul_le_mul_of_nonneg_left ?_ (hDnn u)
    by_cases hu0 : u = 0
    · -- `u = 0` is not in the support since `f 0 ≠ 0`.
      exfalso
      exact hu' (by rw [hu0]; exact divisor_eq_zero_of_ne_zero hanD (by simp; positivity) hf0)
    · have hn : 0 < ‖u‖ := norm_pos_iff.mpr hu0
      apply log_le_log (by norm_num)
      rw [le_mul_inv_iff₀ hn]
      linarith
  · rw [if_neg hur, zero_mul]
    refine mul_nonneg (hDnn u) (log_nonneg ?_)
    by_cases hu0 : u = 0
    · exact absurd (hu0 ▸ mem_closedBall_self hr.le) hur
    · rw [le_mul_inv_iff₀ (norm_pos_iff.mpr hu0)]
      linarith

end QOU.Mathlib.JensenZeroCounting
