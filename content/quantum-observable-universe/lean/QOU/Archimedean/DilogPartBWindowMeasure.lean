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

-- Ref: [manuscript] conj:dilogarithm-archimedean-limit; docs/coordination/dilog-part-b-cusp-attack.md; bean qou-a0li, qou-zuuz
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
  refine le_trans (measure_mono (window_subset_iUnion hq1 ε)) ?_
  refine le_trans (measure_iUnion_le _) (le_of_eq (tsum_congr (fun n => ?_)))
  rw [Real.volume_Ioc]

end QOU.Archimedean
