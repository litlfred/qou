import QOU.Archimedean.DilogPartBAEAssembly
import QOU.Archimedean.DilogPartBWindowMeasure

/-!
# Dilog Part-B W-P1 — the a.e. Borel–Cantelli assembly (final)

Assembles the a.e.-convergence positive from the proved endpoints:
`branch_gap_lower_of_fract` (#4437), `volume_window_le_geom` (#4440), and the schedule +
majorant bricks (#4444).  For the canonical Faddeev schedule `q_m = 1 + 1/(m+1)`,
`ε_m = 1/(m+1)²`, we prove that for **a.e. `x ∈ (0,1)`** the branch-index boundary term
`(q_m − 1)·(−log(1 − x·q_m^{⌊s_m⌋})) → 0`.

Two pieces:
* `bdry_tendsto_of_eventually_no_resonance` — the analytic squeeze: if `x` is eventually
  no-resonant (`ε_m ≤ frac(s_m)`), the boundary term is squeezed between `0` and the
  vanishing majorant `tendsto_boundary_majorant`, so `→ 0`.
* the measure side (`ENNReal` summability of `Σ volume(W_m)` + `measure_limsup_eq_zero`) gives
  a.e. eventual no-resonance — remaining, bean `qou-a0li`.

## Base ring (§7c)

Archimedean throughout (`ℝ`): `Real.log`, `atTop` limits, Lebesgue `volume`.

-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit; docs/coordination/dilog-part-b-cusp-attack.md; bean qou-a0li
-/

namespace QOU.Archimedean

open Filter Topology MeasureTheory
open scoped ENNReal

theorem epsBC_pos (m : ℕ) : 0 < epsBC m := by unfold epsBC; positivity

/-- **Analytic squeeze — eventual no-resonance ⇒ boundary term vanishes.**  For `x ∈ (0,1)`, if
    `ε_m ≤ frac(s_m)` eventually (the no-resonance condition), the branch-index boundary term
    `(q_m − 1)·(−log(1 − x·q_m^{⌊s_m⌋})) → 0`.  It is squeezed between `0` (from `q_m > 1` and
    `0 < δ_m ≤ 1`) and the vanishing majorant `(q_m−1)·(−log((ε_m/4)(q_m−1)))`
    (`tendsto_boundary_majorant`), using `branch_gap_lower_of_fract` for `δ_m ≥ (ε_m/4)(q_m−1)`. -/
theorem bdry_tendsto_of_eventually_no_resonance {x : ℝ} (hx0 : 0 < x)
    (hev : ∀ᶠ m in atTop,
      epsBC m ≤ brS x (qSeqBC m) - (Nat.floor (brS x (qSeqBC m)) : ℝ)) :
    Tendsto (fun m : ℕ => (qSeqBC m - 1) *
        (-Real.log (1 - x * qSeqBC m ^ Nat.floor (brS x (qSeqBC m))))) atTop (𝓝 0) := by
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' tendsto_const_nhds
    tendsto_boundary_majorant ?_ ?_
  · filter_upwards [hev] with m hm
    have hq1 := one_lt_qSeqBC m
    have hgap := branch_gap_lower_of_fract hx0 hq1 (qSeqBC_le_two m) (epsBC_pos m) hm
    have hlbpos : 0 < epsBC m / 4 * (qSeqBC m - 1) :=
      mul_pos (div_pos (epsBC_pos m) (by norm_num)) (by linarith)
    have hδpos : 0 < 1 - x * qSeqBC m ^ Nat.floor (brS x (qSeqBC m)) := by linarith [hgap]
    have hxqpos : 0 < x * qSeqBC m ^ Nat.floor (brS x (qSeqBC m)) :=
      mul_pos hx0 (pow_pos (by linarith) _)
    have hlog : Real.log (1 - x * qSeqBC m ^ Nat.floor (brS x (qSeqBC m))) ≤ 0 :=
      Real.log_nonpos hδpos.le (by linarith)
    exact mul_nonneg (by linarith) (by linarith)
  · filter_upwards [hev] with m hm
    have hq1 := one_lt_qSeqBC m
    have hgap := branch_gap_lower_of_fract hx0 hq1 (qSeqBC_le_two m) (epsBC_pos m) hm
    have hlbpos : 0 < epsBC m / 4 * (qSeqBC m - 1) :=
      mul_pos (div_pos (epsBC_pos m) (by norm_num)) (by linarith)
    have hlogle : Real.log (epsBC m / 4 * (qSeqBC m - 1))
        ≤ Real.log (1 - x * qSeqBC m ^ Nat.floor (brS x (qSeqBC m))) :=
      Real.log_le_log hlbpos hgap
    exact mul_le_mul_of_nonneg_left (by linarith) (by linarith)

/-- The resonance window at step `m`: `W_m = {x ∈ (0,1) : frac(s_m) < ε_m}`. -/
def resWindow (m : ℕ) : Set ℝ :=
  {x : ℝ | x ∈ Set.Ioo (0 : ℝ) 1 ∧ brS x (qSeqBC m) - (Nat.floor (brS x (qSeqBC m)) : ℝ) < epsBC m}

/-- **Window measure bound** `volume(W_m) ≤ 2·ε_m`.  From `volume_window_le_geom`
    (`≤ (1−q^{−ε})q/(q−1)`) and `(1−q^{−ε})q/(q−1) ≤ ε·log q·q/(q−1) ≤ ε·q ≤ 2ε` (using
    `1−q^{−ε} ≤ ε log q`, `log q ≤ q−1`, `q ≤ 2`). -/
theorem volume_resWindow_le (m : ℕ) :
    volume (resWindow m) ≤ ENNReal.ofReal (2 * epsBC m) := by
  refine le_trans (volume_window_le_geom (one_lt_qSeqBC m) (epsBC_pos m).le) ?_
  apply ENNReal.ofReal_le_ofReal
  have hq1 := one_lt_qSeqBC m
  have hq2 := qSeqBC_le_two m
  have hqpos : (0 : ℝ) < qSeqBC m := by linarith
  have hq1pos : (0 : ℝ) < qSeqBC m - 1 := by linarith
  have h1 : 1 - qSeqBC m ^ (-epsBC m) ≤ epsBC m * Real.log (qSeqBC m) := by
    have hrpow : qSeqBC m ^ (-epsBC m) = Real.exp (-(epsBC m * Real.log (qSeqBC m))) := by
      rw [Real.rpow_def_of_pos hqpos]; congr 1; ring
    have hexp := Real.add_one_le_exp (-(epsBC m * Real.log (qSeqBC m)))
    rw [hrpow]; linarith [hexp]
  have h2 : Real.log (qSeqBC m) ≤ qSeqBC m - 1 := Real.log_le_sub_one_of_pos hqpos
  have hcdiv : (0 : ℝ) ≤ qSeqBC m / (qSeqBC m - 1) := by positivity
  calc (1 - qSeqBC m ^ (-epsBC m)) * (qSeqBC m / (qSeqBC m - 1))
      ≤ epsBC m * Real.log (qSeqBC m) * (qSeqBC m / (qSeqBC m - 1)) :=
        mul_le_mul_of_nonneg_right h1 hcdiv
    _ ≤ epsBC m * (qSeqBC m - 1) * (qSeqBC m / (qSeqBC m - 1)) :=
        mul_le_mul_of_nonneg_right
          (mul_le_mul_of_nonneg_left h2 (epsBC_pos m).le) hcdiv
    _ = epsBC m * qSeqBC m := by field_simp
    _ ≤ 2 * epsBC m := by nlinarith [epsBC_pos m, hq2]

/-- **Summable window measure** `Σ_m volume(W_m) ≠ ∞`.  From `volume_resWindow_le` +
    `epsBC_summable` (the p-series). -/
theorem tsum_volume_resWindow_ne_top : (∑' m : ℕ, volume (resWindow m)) ≠ ∞ := by
  have hbound : (∑' m : ℕ, volume (resWindow m)) ≤ ∑' m : ℕ, ENNReal.ofReal (2 * epsBC m) :=
    ENNReal.tsum_le_tsum (fun m => volume_resWindow_le m)
  have hfin : (∑' m : ℕ, ENNReal.ofReal (2 * epsBC m)) ≠ ∞ := by
    rw [← ENNReal.ofReal_tsum_of_nonneg (fun m => by
          have := (epsBC_pos m).le; positivity) (epsBC_summable.mul_left 2)]
    exact ENNReal.ofReal_ne_top
  exact ne_top_of_le_ne_top hfin hbound

/-- **A.e. Borel–Cantelli assembly — the dilog Part-B W-P1 a.e. positive.**  For a.e.
    `x ∈ (0,1)`, along the Faddeev schedule `q_m = 1 + 1/(m+1)` the branch-index boundary term
    `(q_m − 1)·(−log(1 − x·q_m^{⌊s_m⌋})) → 0`.  Borel–Cantelli (`ae_eventually_notMem` +
    `tsum_volume_resWindow_ne_top`) gives a.e. eventual no-resonance
    (`ε_m ≤ frac(s_m)`), which the squeeze `bdry_tendsto_of_eventually_no_resonance` turns into
    convergence.  This is the measure-theoretic positive complementing the proved-false
    unconditional pointwise limit (`not_tendsto_boundary_zero`, #4434). -/
theorem ae_bdry_tendsto_zero :
    ∀ᵐ x ∂volume, x ∈ Set.Ioo (0 : ℝ) 1 →
      Tendsto (fun m : ℕ => (qSeqBC m - 1) *
        (-Real.log (1 - x * qSeqBC m ^ Nat.floor (brS x (qSeqBC m))))) atTop (𝓝 0) := by
  filter_upwards [ae_eventually_notMem tsum_volume_resWindow_ne_top] with x hx hxmem
  refine bdry_tendsto_of_eventually_no_resonance hxmem.1 ?_
  filter_upwards [hx] with m hm
  by_contra hlt
  push_neg at hlt
  exact hm ⟨hxmem, hlt⟩

end QOU.Archimedean
