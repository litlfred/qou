import Mathlib.Analysis.SpecialFunctions.Log.NegMulLog

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

-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit
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

end QOU.Archimedean

