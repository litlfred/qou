import QOU.Archimedean.DilogPartBBoundarySeed
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.PSeries

/-!
# Dilog Part-B W-P1 — the a.e. Borel–Cantelli assembly, analytic + schedule bricks

The two hard endpoints of the a.e. positive are proved on `main`: the deterministic
`branch_gap_lower_of_fract` (no-resonance ⇒ gap, `DilogPartBBorelCantelli`) and the
`volume_window_le_geom` measure bound (`DilogPartBWindowMeasure`).  This file provides the
**analytic + schedule inputs** to the Borel–Cantelli assembly, for the canonical Faddeev
schedule

`q_m := 1 + 1/(m+1) → 1⁺`,   `ε_m := 1/(m+1)² = (q_m − 1)²`   (summable).

The key analytic fact is that the **boundary-term majorant vanishes**:

`(q_m − 1)·(−log((ε_m/4)(q_m−1))) → 0`.

Because `ε_m = (q_m−1)²`, the majorant argument is `(q_m−1)³/4`, so with `w := q_m−1 → 0⁺`,
`(q_m−1)·(−log(w³/4)) = w·log 4 − 3·(w·log w) → 0` — reusing the `t·log t → 0` seed
`tendsto_mul_log_nhdsWithin_zero` (#4270).  With `branch_gap_lower_of_fract` (which gives
`δ_m ≥ (ε_m/4)(q_m−1)`) this majorant squeezes the boundary term `(q_m−1)·(−log δ_m) → 0` on
the a.e. no-resonance set; the remaining measure-side plumbing (`ENNReal` summability of
`Σ volume(W_m)`, `measure_limsup_eq_zero`, `ae` threading) is bean `qou-a0li`.

## Base ring (§7c)

Archimedean throughout (`ℝ`): `Real.log`, `atTop` limits.

-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit; docs/coordination/dilog-part-b-cusp-attack.md; bean qou-a0li, qou-zuuz
-/

namespace QOU.Archimedean

open Filter Topology

/-- The canonical Faddeev schedule modulus `q_m := 1 + 1/(m+1) → 1⁺`. -/
noncomputable def qSeqBC (m : ℕ) : ℝ := 1 + 1 / ((m : ℝ) + 1)

/-- The canonical resonance-window widths `ε_m := 1/(m+1)² = (q_m − 1)²` (summable). -/
noncomputable def epsBC (m : ℕ) : ℝ := 1 / ((m : ℝ) + 1) ^ 2

theorem qSeqBC_sub_one (m : ℕ) : qSeqBC m - 1 = 1 / ((m : ℝ) + 1) := by
  unfold qSeqBC; ring

theorem qSeqBC_sub_one_pos (m : ℕ) : 0 < qSeqBC m - 1 := by
  rw [qSeqBC_sub_one]; positivity

theorem one_lt_qSeqBC (m : ℕ) : 1 < qSeqBC m := by
  have := qSeqBC_sub_one_pos m; linarith

theorem qSeqBC_le_two (m : ℕ) : qSeqBC m ≤ 2 := by
  have h : 1 / ((m : ℝ) + 1) ≤ 1 := by
    rw [div_le_one (by positivity)]
    have : (0 : ℝ) ≤ (m : ℝ) := Nat.cast_nonneg m
    linarith
  unfold qSeqBC; linarith

/-- `q_m − 1 = 1/(m+1) → 0`. -/
theorem tendsto_qSeqBC_sub_one : Tendsto (fun m : ℕ => qSeqBC m - 1) atTop (𝓝 0) := by
  have hden : Tendsto (fun m : ℕ => (m : ℝ) + 1) atTop atTop :=
    tendsto_atTop_add_const_right _ 1 (tendsto_natCast_atTop_atTop (R := ℝ))
  have hinv : Tendsto (fun m : ℕ => ((m : ℝ) + 1)⁻¹) atTop (𝓝 0) :=
    Tendsto.inv_tendsto_atTop hden
  refine hinv.congr (fun m => ?_)
  rw [qSeqBC_sub_one, one_div]

theorem tendsto_qSeqBC_one : Tendsto qSeqBC atTop (𝓝 1) := by
  have h : Tendsto (fun m : ℕ => 1 + (qSeqBC m - 1)) atTop (𝓝 (1 + 0)) :=
    tendsto_const_nhds.add tendsto_qSeqBC_sub_one
  simp only [add_zero] at h
  refine h.congr (fun m => ?_)
  ring

/-- `q_m − 1 → 0⁺` (one-sided). -/
theorem tendsto_qSeqBC_sub_one_nhdsGT :
    Tendsto (fun m : ℕ => qSeqBC m - 1) atTop (𝓝[>] (0 : ℝ)) := by
  rw [tendsto_nhdsWithin_iff]
  refine ⟨tendsto_qSeqBC_sub_one, ?_⟩
  filter_upwards with m
  simp only [Set.mem_Ioi]; exact qSeqBC_sub_one_pos m

theorem epsBC_eq_sq (m : ℕ) : epsBC m = (qSeqBC m - 1) ^ 2 := by
  rw [qSeqBC_sub_one]; unfold epsBC; rw [div_pow, one_pow]

/-- `Σ_m ε_m < ∞` — the summable schedule (p-series, p = 2). -/
theorem epsBC_summable : Summable epsBC := by
  have hp : Summable (fun n : ℕ => (1 : ℝ) / (n : ℝ) ^ 2) :=
    Real.summable_one_div_nat_pow.mpr (by norm_num)
  have h := (summable_nat_add_iff 1).mpr hp
  refine h.congr (fun m => ?_)
  unfold epsBC; push_cast; ring

/-- **Boundary-term majorant vanishes.**  `(q_m − 1)·(−log((ε_m/4)(q_m−1))) → 0`.  Since
    `ε_m = (q_m−1)²`, the argument is `(q_m−1)³/4`, so with `w := q_m−1 → 0⁺`,
    `w·(−log(w³/4)) = w·log 4 − 3·(w·log w) → 0` by the `t·log t → 0` seed. -/
theorem tendsto_boundary_majorant :
    Tendsto (fun m : ℕ => (qSeqBC m - 1) * (-Real.log (epsBC m / 4 * (qSeqBC m - 1))))
      atTop (𝓝 0) := by
  have hwlog : Tendsto (fun m : ℕ => (qSeqBC m - 1) * Real.log (qSeqBC m - 1)) atTop (𝓝 0) :=
    tendsto_mul_log_nhdsWithin_zero.comp tendsto_qSeqBC_sub_one_nhdsGT
  have hw4 : Tendsto (fun m : ℕ => (qSeqBC m - 1) * Real.log 4) atTop (𝓝 0) := by
    have := tendsto_qSeqBC_sub_one.mul_const (Real.log 4); simpa using this
  have hcombo : Tendsto (fun m : ℕ =>
      (qSeqBC m - 1) * Real.log 4 - 3 * ((qSeqBC m - 1) * Real.log (qSeqBC m - 1)))
      atTop (𝓝 (0 - 3 * 0)) := hw4.sub (hwlog.const_mul 3)
  rw [mul_zero, sub_zero] at hcombo
  refine hcombo.congr (fun m => ?_)
  have hw : 0 < qSeqBC m - 1 := qSeqBC_sub_one_pos m
  have harg : epsBC m / 4 * (qSeqBC m - 1) = (qSeqBC m - 1) ^ 3 / 4 := by
    rw [epsBC_eq_sq]; ring
  rw [harg, Real.log_div (pow_ne_zero 3 (ne_of_gt hw)) (by norm_num), Real.log_pow]
  push_cast
  ring

end QOU.Archimedean
