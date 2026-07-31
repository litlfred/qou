import Mathlib.Analysis.SpecialFunctions.Log.NegMulLog
import QOU.Archimedean.DilogPartBBranchPointSum

/-!
# Analytic seed for the dilog Part-B W-P1 boundary term

The W-P1 assembly (`wp1_riemann_bound`, `DilogPartBBranchPointSum.lean`) reduces
the positive-factor convergence to the single scalar limit
`(q−1)·log(1−xqⁿ) → 0` — the non-uniform boundary term at the branch point.

This file provides the **analytic seed** for controlling that term: `t·log t → 0`
as `t → 0⁺`.  Once a lower bound `1−xqⁿ ≥ c·(q−1)` is available (the
Diophantine / Faddeev-scaling no-resonance condition on `x`), the boundary term
is dominated by `δ·log δ`-type quantities with `δ = 1−xqⁿ → 0`, and this seed
closes it.  Proved from the continuity of Mathlib's entropy function
`Real.negMulLog = −t·log t` at `0`.

-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
-/

namespace QOU.Archimedean

open Filter Topology

/-- **Analytic seed — `t·log t → 0` as `t → 0⁺`.**  Immediate from the continuity
    of the entropy function `Real.negMulLog t = −t·log t` at `0`
    (`Real.negMulLog_zero : negMulLog 0 = 0`).  This is the ingredient that
    controls the W-P1 boundary term `(q−1)·log(1−xqⁿ)` once the endpoint
    `1−xqⁿ` is bounded below by a multiple of `q−1`. -/
theorem tendsto_mul_log_nhdsWithin_zero :
    Tendsto (fun t : ℝ => t * Real.log t) (𝓝[>] (0 : ℝ)) (𝓝 0) := by
  have hc : Tendsto Real.negMulLog (𝓝 (0 : ℝ)) (𝓝 (Real.negMulLog 0)) :=
    Real.continuous_negMulLog.tendsto 0
  rw [Real.negMulLog_zero] at hc
  have heq : Real.negMulLog = fun t : ℝ => -(t * Real.log t) := by
    funext t; exact neg_mul t (Real.log t)
  rw [heq] at hc
  have h2 := hc.mono_left (nhdsWithin_le_nhds (a := (0 : ℝ)) (s := Set.Ioi (0 : ℝ)))
  simpa using h2.neg

/-- **Conditional boundary-term limit (the "positive direction" of the W-P1
    residual).**  Along any filter `l`, if the endpoint gap `δ` tends to `0⁺` and
    is bounded below by a fixed multiple of the width `w` (`c·w ≤ δ`, `c > 0` —
    the Diophantine / no-resonance condition), then the boundary term
    `w·(−log δ) → 0`.

    Applied with `δ = 1 − xqⁿ`, `w = q − 1`, this closes the W-P1 boundary limit
    `(q−1)·log(1−xqⁿ) → 0` **whenever** `x` satisfies the no-resonance bound
    `1 − xqⁿ ≥ c(q−1)` — the precise hypothesis under which W-P1 converges.
    Proof: squeeze `0 ≤ w(−log δ) ≤ (δ/c)(−log δ) = −(1/c)·(δ log δ) → 0` by the
    seed `tendsto_mul_log_nhdsWithin_zero`. -/
theorem boundary_term_vanishes {ι : Type*} {l : Filter ι} {w δ : ι → ℝ} {c : ℝ}
    (hc : 0 < c) (hw0 : ∀ᶠ i in l, 0 < w i) (hδ1 : ∀ᶠ i in l, δ i < 1)
    (hbound : ∀ᶠ i in l, c * w i ≤ δ i) (hδlim : Tendsto δ l (𝓝[>] (0 : ℝ))) :
    Tendsto (fun i => w i * (-Real.log (δ i))) l (𝓝 0) := by
  have hδ0 : ∀ᶠ i in l, 0 < δ i := hδlim.eventually self_mem_nhdsWithin
  have hseed : Tendsto (fun i => δ i * Real.log (δ i)) l (𝓝 0) :=
    tendsto_mul_log_nhdsWithin_zero.comp hδlim
  have hupper : Tendsto (fun i => -(1 / c) * (δ i * Real.log (δ i))) l (𝓝 0) := by
    simpa using hseed.const_mul (-(1 / c))
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' tendsto_const_nhds hupper ?_ ?_
  · filter_upwards [hw0, hδ0, hδ1] with i hw hδ hδ1'
    have hnlog : 0 ≤ -Real.log (δ i) := by
      have := Real.log_nonpos hδ.le hδ1'.le; linarith
    exact mul_nonneg hw.le hnlog
  · filter_upwards [hw0, hδ0, hδ1, hbound] with i hw hδ hδ1' hb
    have hnlog : 0 ≤ -Real.log (δ i) := by
      have := Real.log_nonpos hδ.le hδ1'.le; linarith
    have hwle : w i ≤ δ i / c := by rw [le_div_iff₀ hc]; linarith [hb]
    calc w i * (-Real.log (δ i)) ≤ (δ i / c) * (-Real.log (δ i)) :=
          mul_le_mul_of_nonneg_right hwle hnlog
      _ = -(1 / c) * (δ i * Real.log (δ i)) := by ring

open QOU.QPochhammer in
/-- **Conditional W-P1 convergence.**  Along any filter `l` with `1 < q i`, the
    endpoint `x·qⁿ → 1⁻`, and the Diophantine no-resonance bound
    `c·(q−1) ≤ 1 − x·qⁿ` (`c > 0`), the positive-factor rescaled log-sum converges:

    `(1−q)·Σ_{k<n} log(1−xqᵏ) → π²/6 − Li₂(x)`,

    i.e. the W-P1 quantity `−(1−q)Σ log(1−xqᵏ) → Li₂(x) − π²/6`.  Assembles
    `wp1_riemann_bound` (the explicit two-sided bound), `boundary_term_vanishes`
    (the boundary term `(q−1)(−log(1−xqⁿ)) → 0` under the bound), and the Abel
    limit `Li₂(xqⁿ) → π²/6` (`tendsto_LiTwo_nhdsWithin_lt_one`), squeezed.  The
    unconditional (all-`x`, Faddeev-scaling) statement remains open. -/
theorem wp1_tendsto_of_dioph {ι : Type*} {l : Filter ι} {q : ι → ℝ} {n : ι → ℕ}
    {x : ℝ} (hx0 : 0 < x) (hq1 : ∀ᶠ i in l, 1 < q i)
    (hendpoint : Tendsto (fun i => x * q i ^ n i) l (𝓝[<] 1))
    {c : ℝ} (hc : 0 < c)
    (hdioph : ∀ᶠ i in l, c * (q i - 1) ≤ 1 - x * q i ^ n i) :
    Tendsto (fun i => (1 - q i) * ∑ k ∈ Finset.range (n i), Real.log (1 - x * q i ^ k))
      l (𝓝 (Real.pi ^ 2 / 6 - LiTwo x)) := by
  have hxqn_lt1 : ∀ᶠ i in l, x * q i ^ n i < 1 := hendpoint.eventually self_mem_nhdsWithin
  have hval : Tendsto (fun i => x * q i ^ n i) l (𝓝 1) := hendpoint.mono_right nhdsWithin_le_nhds
  have hxqn_pos : ∀ᶠ i in l, 0 < x * q i ^ n i := by
    filter_upwards [hq1] with i h; positivity
  have hδval : Tendsto (fun i => 1 - x * q i ^ n i) l (𝓝 0) := by
    simpa using hval.const_sub 1
  have hδlim : Tendsto (fun i => 1 - x * q i ^ n i) l (𝓝[>] (0 : ℝ)) := by
    rw [tendsto_nhdsWithin_iff]
    refine ⟨hδval, ?_⟩
    filter_upwards [hxqn_lt1] with i h; simp only [Set.mem_Ioi]; linarith
  have hbdry : Tendsto (fun i => (q i - 1) * (-Real.log (1 - x * q i ^ n i))) l (𝓝 0) := by
    refine boundary_term_vanishes hc ?_ ?_ hdioph hδlim
    · filter_upwards [hq1] with i h; linarith
    · filter_upwards [hxqn_pos] with i h; linarith
  have hqm1_lim : Tendsto (fun i => q i - 1) l (𝓝 0) := by
    have hg : Tendsto (fun i => c⁻¹ * (1 - x * q i ^ n i)) l (𝓝 0) := by
      simpa using hδval.const_mul c⁻¹
    refine squeeze_zero' ?_ ?_ hg
    · filter_upwards [hq1] with i h; linarith
    · filter_upwards [hdioph] with i h
      have := mul_le_mul_of_nonneg_left h (inv_pos.mpr hc).le
      rwa [← mul_assoc, inv_mul_cancel₀ (ne_of_gt hc), one_mul] at this
  have hqm1qn : Tendsto (fun i => (q i - 1) * q i ^ n i) l (𝓝 0) := by
    have hg : Tendsto (fun i => (q i - 1) * x⁻¹) l (𝓝 0) := by
      simpa using hqm1_lim.mul_const x⁻¹
    refine squeeze_zero' ?_ ?_ hg
    · filter_upwards [hq1] with i h
      have h1 : (0 : ℝ) ≤ q i - 1 := by linarith
      have h2 : (0 : ℝ) ≤ q i ^ n i := (pow_pos (by linarith : (0:ℝ) < q i) _).le
      positivity
    · filter_upwards [hq1, hxqn_lt1] with i hq hlt
      have hqn_le : q i ^ n i ≤ x⁻¹ := by
        rw [inv_eq_one_div, le_div_iff₀ hx0, mul_comm]; exact le_of_lt hlt
      exact mul_le_mul_of_nonneg_left hqn_le (by linarith : (0:ℝ) ≤ q i - 1)
  have hE : Tendsto (fun i => (q i - 1) * (-Real.log (1 - x * q i ^ n i))
      - (q i - 1) * q i ^ n i * (-Real.log (1 - x * 1))) l (𝓝 0) := by
    have hvanish : Tendsto (fun i => (q i - 1) * q i ^ n i * (-Real.log (1 - x * 1)))
        l (𝓝 0) := by simpa using hqm1qn.mul_const (-Real.log (1 - x * 1))
    simpa using hbdry.sub hvanish
  have hA : Tendsto (fun i => LiTwo (x * q i ^ n i) - LiTwo x) l
      (𝓝 (Real.pi ^ 2 / 6 - LiTwo x)) := by
    have hLi : Tendsto (fun i => LiTwo (x * q i ^ n i)) l (𝓝 (Real.pi ^ 2 / 6)) :=
      tendsto_LiTwo_nhdsWithin_lt_one.comp hendpoint
    simpa using hLi.sub_const (LiTwo x)
  have hAE : Tendsto (fun i => (LiTwo (x * q i ^ n i) - LiTwo x)
      - ((q i - 1) * (-Real.log (1 - x * q i ^ n i))
         - (q i - 1) * q i ^ n i * (-Real.log (1 - x * 1))))
      l (𝓝 (Real.pi ^ 2 / 6 - LiTwo x)) := by simpa using hA.sub hE
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' hAE hA ?_ ?_
  · filter_upwards [hq1, hxqn_lt1] with i hq hlt
    obtain ⟨_, hhi⟩ := wp1_riemann_bound hx0 hq (n i) hlt
    linarith [hhi]
  · filter_upwards [hq1, hxqn_lt1] with i hq hlt
    obtain ⟨hlo, _⟩ := wp1_riemann_bound hx0 hq (n i) hlt
    linarith [hlo]

end QOU.Archimedean

