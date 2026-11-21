import QOU.Archimedean.DilogPartBBorelCantelli
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic

/-!
# Dilog Part-B W-P1 — the resonance-window measure estimate (a.e. Borel–Cantelli brick)

The deterministic bricks (`DilogPartBBorelCantelli`) reduce a.e. convergence to bounding the
Lebesgue measure of the **resonance window**
`W(q,ε) := {x ∈ (0,1) : s − ⌊s⌋ < ε}`, `s := log(1/x)/log q`.

This file lands the **geometric structure** of that window — the single hard step of the
measure estimate that avoids any change-of-variables: **`W` is contained in a union of
explicit `x`-intervals** `(q^{−(n+ε)}, q^{−n}]`, `n ∈ ℕ` (`window_subset_iUnion`). Each such
interval has length `q^{−n}(1 − q^{−ε})`, so `volume(W) ≤ (1−q^{−ε})·Σ_n q^{−n} =
(1−q^{−ε})·q/(q−1) ≤ ε·log q·q/(q−1)` — the bound that, with Mathlib's `measure_limsup_eq_zero`
(first Borel–Cantelli) and the deterministic `branch_gap_lower_of_fract`, closes a.e.
convergence. The remaining ENNReal geometric-sum arithmetic is bean `qou-a0li`.

## Base ring (§7c)

Archimedean throughout (`ℝ`): `Real.rpow`, `Real.log`, Lebesgue `volume`.

-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit; docs/coordination/dilog-part-b-cusp-attack.md; bean qou-a0li, qou-zuuz
-/

namespace QOU.Archimedean

open Filter Topology Set MeasureTheory

variable {x q ε : ℝ}

/-- **Each window point lands in the explicit interval** `(q^{−(⌊s⌋+ε)}, q^{−⌊s⌋}]`.
    From `⌊s⌋ ≤ s < ⌊s⌋+ε` (the resonance condition) and `s·log q = log(1/x) = −log x`:
    `x ≤ q^{−⌊s⌋}` and `x > q^{−(⌊s⌋+ε)}`. -/
theorem window_mem_Ioc (hx0 : 0 < x) (hx1 : x < 1) (hq1 : 1 < q)
    (hε : brS x q - (Nat.floor (brS x q) : ℝ) < ε) :
    x ∈ Set.Ioc (q ^ (-((Nat.floor (brS x q) : ℝ) + ε))) (q ^ (-(Nat.floor (brS x q) : ℝ))) := by
  have hqpos : (0 : ℝ) < q := by linarith
  have hlogq : 0 < Real.log q := Real.log_pos hq1
  have hs0 : 0 ≤ brS x q := brS_nonneg hx0 hx1 hq1
  have hns : ((Nat.floor (brS x q) : ℝ)) ≤ brS x q := Nat.floor_le hs0
  have hsn : brS x q < (Nat.floor (brS x q) : ℝ) + ε := by linarith
  have hslogq : brS x q * Real.log q = - Real.log x := by
    unfold brS
    rw [div_mul_cancel₀ _ (ne_of_gt hlogq), one_div, Real.log_inv]
  have hlogx : Real.log x = - (brS x q * Real.log q) := by rw [hslogq]; ring
  refine ⟨?_, ?_⟩
  · -- q^{−(⌊s⌋+ε)} < x
    rw [← Real.log_lt_log_iff (Real.rpow_pos_of_pos hqpos _) hx0, Real.log_rpow hqpos, hlogx]
    nlinarith [hsn, hlogq]
  · -- x ≤ q^{−⌊s⌋}
    rw [← Real.log_le_log_iff hx0 (Real.rpow_pos_of_pos hqpos _), Real.log_rpow hqpos, hlogx]
    nlinarith [hns, hlogq]

/-- **The resonance window is contained in a countable union of explicit intervals.**
    `W(q,ε) := {x ∈ (0,1) : s − ⌊s⌋ < ε} ⊆ ⋃ n, (q^{−(n+ε)}, q^{−n}]`.  This is the geometric
    heart of the measure estimate: each interval has length `q^{−n}(1−q^{−ε})`, summing to
    `(1−q^{−ε})·q/(q−1) ≤ ε·log q·q/(q−1)`. -/
theorem window_subset_iUnion (hq1 : 1 < q) (ε : ℝ) :
    {x : ℝ | x ∈ Set.Ioo (0:ℝ) 1 ∧ brS x q - (Nat.floor (brS x q) : ℝ) < ε}
      ⊆ ⋃ n : ℕ, Set.Ioc (q ^ (-((n : ℝ) + ε))) (q ^ (-(n : ℝ))) := by
  intro x hx
  obtain ⟨⟨hx0, hx1⟩, hε⟩ := hx
  exact Set.mem_iUnion.mpr ⟨Nat.floor (brS x q), window_mem_Ioc hx0 hx1 hq1 hε⟩

/-- **Measure reduction.**  `volume(W) ≤ Σ' n, (q^{−n} − q^{−(n+ε)})` — the window measure is
    bounded by the total length of the covering intervals (monotonicity + countable
    subadditivity + `volume(Ioc a b) = b − a`).  The remaining geometric evaluation
    `Σ' n, q^{−n}(1−q^{−ε}) = (1−q^{−ε})·q/(q−1)` is bean `qou-a0li`. -/
theorem volume_window_le (hq1 : 1 < q) (ε : ℝ) :
    volume {x : ℝ | x ∈ Set.Ioo (0:ℝ) 1 ∧ brS x q - (Nat.floor (brS x q) : ℝ) < ε}
      ≤ ∑' n : ℕ, ENNReal.ofReal (q ^ (-(n : ℝ)) - q ^ (-((n : ℝ) + ε))) := by
  apply le_trans (measure_mono (window_subset_iUnion hq1 ε))
  apply le_trans (measure_iUnion_le _)
  apply le_of_eq
  apply tsum_congr
  intro n
  rw [Real.volume_Ioc]

/-- **Resonance-window measure bound (complete).**  For `1 < q` and `0 ≤ ε`,
    `volume(W(q,ε)) ≤ (1 − q^{−ε})·q/(q−1)` — the exact geometric bound.  Evaluates
    `volume_window_le`'s tsum: each term is `q^{−n}(1−q^{−ε}) = (q⁻¹)ⁿ(1−q^{−ε})`, a geometric
    series summing to `(1−q^{−ε})·(1−q⁻¹)⁻¹ = (1−q^{−ε})·q/(q−1)`.  With
    `1 − q^{−ε} ≤ ε·log q`, this is `≤ ε·log q·q/(q−1)`, the summable resonance-window bound
    Borel–Cantelli consumes. -/
theorem volume_window_le_geom (hq1 : 1 < q) (hε0 : 0 ≤ ε) :
    volume {x : ℝ | x ∈ Set.Ioo (0:ℝ) 1 ∧ brS x q - (Nat.floor (brS x q) : ℝ) < ε}
      ≤ ENNReal.ofReal ((1 - q ^ (-ε)) * (q / (q - 1))) := by
  have hqpos : (0 : ℝ) < q := by linarith
  have hqinv_lt : q⁻¹ < 1 := by
    have h1 : q⁻¹ * q = 1 := inv_mul_cancel₀ (ne_of_gt hqpos)
    nlinarith [mul_lt_mul_of_pos_left hq1 (inv_pos.mpr hqpos), h1]
  have hqinv_nn : (0 : ℝ) ≤ q⁻¹ := by positivity
  have hc_nn : 0 ≤ 1 - q ^ (-ε) := by
    have hle : q ^ (-ε) ≤ q ^ (0 : ℝ) :=
      Real.rpow_le_rpow_of_exponent_le (le_of_lt hq1) (by linarith)
    rw [Real.rpow_zero] at hle; linarith
  have hterm : ∀ n : ℕ, q ^ (-(n : ℝ)) - q ^ (-((n : ℝ) + ε)) = (q⁻¹) ^ n * (1 - q ^ (-ε)) := by
    intro n
    rw [show -((n : ℝ) + ε) = -(n : ℝ) + -ε by ring, Real.rpow_add hqpos,
        Real.rpow_neg hqpos.le, Real.rpow_natCast, ← inv_pow]
    ring
  have hsummable : Summable (fun n : ℕ => (q⁻¹) ^ n * (1 - q ^ (-ε))) :=
    (summable_geometric_of_lt_one hqinv_nn hqinv_lt).mul_right _
  have hinv : (1 - q⁻¹)⁻¹ = q / (q - 1) := by
    rw [show (1 : ℝ) - q⁻¹ = (q - 1) / q by field_simp, inv_div]
  have hgeom : ∑' n : ℕ, (q⁻¹) ^ n * (1 - q ^ (-ε)) = (1 - q ^ (-ε)) * (q / (q - 1)) := by
    rw [tsum_mul_right, tsum_geometric_of_lt_one hqinv_nn hqinv_lt, hinv]
    ring
  refine le_trans (volume_window_le hq1 ε) (le_of_eq ?_)
  rw [funext (fun n : ℕ => congrArg ENNReal.ofReal (hterm n)),
      ← ENNReal.ofReal_tsum_of_nonneg (fun n => mul_nonneg (by positivity) hc_nn) hsummable,
      hgeom]

end QOU.Archimedean
