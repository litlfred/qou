import QOU.SchurWeyl.OcneanuWeight
import Mathlib.Algebra.Order.Archimedean.Basic
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith
import Mathlib.Data.Real.Archimedean
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# QOU.SchurWeyl.OcneanuWeightPositiveWindow — every Ocneanu weight is positive iff `0 ≤ z ≤ q − q⁻¹`

For real `q > 1` the closed-form weight `ocneanuWeight q z μ` (`OcneanuWeight`) is positive on
**every** Young diagram exactly when the Markov parameter lies in the closed window

  `0 ≤ z ≤ h`,   `h = q − q⁻¹`.

## Why

The weight is a product of one affine factor per cell over a product of `q^{2·hook} − 1`.
For `q > 1` the denominator is positive, so the sign is the sign of the numerator

  `F(i,j) = q^{2i}(q² − 1) + q z (q^{2j} − q^{2i})`.

* **Inside the window every factor is positive.**  If `j ≥ i` the `z`-term is `≥ 0`; if `j < i`
  it is smallest at `z = h`, where `q h = q² − 1` gives `F = (q² − 1) q^{2j} > 0`.
* **Above the window a column flips sign.**  On the column cell `(i,0)` the factor is
  `F = q^{2i}(q² − 1 − q z) + q z`, which is negative once `q^{2i}` is large, because
  `q² − 1 − q z < 0` when `z > h`.  So for some `n` the column of height `n + 1` has a
  numerator of the opposite sign to the column of height `n`, and one of the two is not positive.
* **Below the window a row flips sign**, by the same argument on the row cell `(0,j)`.

The zeros of the column factors are `z_i = h q^{2i}/(q^{2i} − 1)` (the rank-`i` parameters of
`QOU.Eightfold.OcneanuRankFamily.markovParam`), decreasing to `h`; the row zeros are their mirror
images `h − z_i`, increasing to `0`.  The window is what survives all of them.

## What this does and does not say

It is a theorem about the **closed form** `ocneanuWeight` at every `n`.  That this closed form
*is* the Markov trace's weight system at general `n` is **not** proved in the corpus — it is proved
at `n = 3` (`OcneanuWeightMarkov3`) and checked in exact arithmetic through `n = 6`.  So read the
Markov-trace statement "the faithful positive Markov traces on the whole tower are exactly
`0 ≤ z ≤ h`" as conditional on that identification.

Two corollaries that are immediate from the `iff`:

* the self-dual point `z = h/2` is inside;
* convention D, `z = q³/(q²+1)`, is **outside** (it exceeds `h`), consistent with
  `ocneanuWeight_conventionD_eq_zero_of_three_rows`.

## Base ring (§7c)

`ℝ`, genuinely: the statement is an inequality and the proof uses the ordering throughout.

`Ref: [wenzl1988]`, `[jones1987]` for the trace; the inequality argument is elementary.
-/

namespace QOU.SchurWeyl.PositiveWindow

open QOU.SchurWeyl

/-- The cell numerator factor of `ocneanuWeight`. -/
noncomputable def cellFactor (q z : ℝ) (c : ℕ × ℕ) : ℝ :=
  q ^ (2 * c.1) * (q ^ 2 - 1 - q * z) + q ^ (2 * c.2 + 1) * z

/-- A cell's hook length is positive (its own arm contains it).  Same statement as
`QOU.SchurWeyl.hookLength_pos` in `OcneanuWeightTwoRowNonzero`, restated to keep this file's
import cone small. -/
private theorem hookLength_pos' {mu : YoungDiagram} {c : ℕ × ℕ} (hc : c ∈ mu.cells) :
    0 < hookLength mu c := by
  classical
  have hmem : c ∈ mu.cells.filter (fun d => d.1 = c.1 ∧ c.2 ≤ d.2) := by
    simp [Finset.mem_filter, hc]
  have h1 : 0 < (mu.cells.filter (fun d => d.1 = c.1 ∧ c.2 ≤ d.2)).card :=
    Finset.card_pos.mpr ⟨c, hmem⟩
  simp only [hookLength]
  omega

/-- The hook denominator of `ocneanuWeight` is positive for `q > 1`. -/
theorem den_pos {q : ℝ} (hq : 1 < q) (mu : YoungDiagram) :
    0 < ∏ c ∈ mu.cells, (q ^ (2 * hookLength mu c) - 1) := by
  refine Finset.prod_pos fun c hc => ?_
  have hk : 2 * hookLength mu c ≠ 0 := by
    have := hookLength_pos' hc
    omega
  have : 1 < q ^ (2 * hookLength mu c) := one_lt_pow₀ hq hk
  linarith

/-- For `q > 1`, the weight is positive iff its numerator is. -/
theorem weight_pos_iff {q : ℝ} (hq : 1 < q) (z : ℝ) (mu : YoungDiagram) :
    0 < ocneanuWeight q z mu ↔ 0 < ∏ c ∈ mu.cells, cellFactor q z c := by
  unfold ocneanuWeight
  exact div_pos_iff_of_pos_right (den_pos hq mu)

/-- **Inside the window every cell factor is positive.** -/
theorem cellFactor_pos {q z : ℝ} (hq : 1 < q) (hz0 : 0 ≤ z) (hzh : z ≤ q - q⁻¹)
    (c : ℕ × ℕ) : 0 < cellFactor q z c := by
  have hq0 : 0 < q := by linarith
  have hqh : q * (q - q⁻¹) = q ^ 2 - 1 := by field_simp
  set a := q ^ (2 * c.1) with ha
  set b := q ^ (2 * c.2) with hb
  have ha0 : 0 < a := by positivity
  have hb0 : 0 < b := by positivity
  have hq21 : 0 < q ^ 2 - 1 := by nlinarith
  have hF : cellFactor q z c = a * (q ^ 2 - 1) + q * z * (b - a) := by
    simp only [cellFactor, ha, hb, pow_succ]
    ring
  rw [hF]
  rcases le_total c.1 c.2 with hij | hij
  · have hab : a ≤ b := pow_le_pow_right₀ hq.le (by omega)
    have : 0 ≤ q * z * (b - a) := by
      have := mul_nonneg (mul_nonneg hq0.le hz0) (sub_nonneg.mpr hab)
      linarith
    nlinarith
  · have hba : b ≤ a := pow_le_pow_right₀ hq.le (by omega)
    -- `q z (b − a) ≥ q h (b − a)` since `z ≤ h` and `b − a ≤ 0`
    have hstep : q * (q - q⁻¹) * (b - a) ≤ q * z * (b - a) := by
      have h1 : 0 ≤ q * ((q - q⁻¹) - z) * (a - b) :=
        mul_nonneg (mul_nonneg hq0.le (sub_nonneg.mpr hzh)) (sub_nonneg.mpr hba)
      nlinarith
    rw [hqh] at hstep
    nlinarith

/-- **Inside the window every Ocneanu weight is positive.** -/
theorem ocneanuWeight_pos_of_mem_window {q z : ℝ} (hq : 1 < q) (hz0 : 0 ≤ z)
    (hzh : z ≤ q - q⁻¹) (mu : YoungDiagram) : 0 < ocneanuWeight q z mu :=
  (weight_pos_iff hq z mu).mpr (Finset.prod_pos fun c _ => cellFactor_pos hq hz0 hzh c)

/-! ### Columns and rows -/

/-- The column of height `n`. -/
def colDiagram (n : ℕ) : YoungDiagram where
  cells := Finset.range n ×ˢ {0}
  isLowerSet := by
    intro c d hdc hc
    simp only [Finset.coe_product, Set.mem_prod, Finset.coe_range, Set.mem_Iio,
      Finset.coe_singleton, Set.mem_singleton_iff] at hc ⊢
    exact ⟨lt_of_le_of_lt hdc.1 hc.1, Nat.le_zero.mp (hc.2 ▸ hdc.2)⟩

/-- The row of length `n`. -/
def rowDiagram (n : ℕ) : YoungDiagram where
  cells := {0} ×ˢ Finset.range n
  isLowerSet := by
    intro c d hdc hc
    simp only [Finset.coe_product, Set.mem_prod, Finset.coe_range, Set.mem_Iio,
      Finset.coe_singleton, Set.mem_singleton_iff] at hc ⊢
    exact ⟨Nat.le_zero.mp (hc.1 ▸ hdc.1), lt_of_le_of_lt hdc.2 hc.2⟩

theorem prod_col (q z : ℝ) (n : ℕ) :
    ∏ c ∈ (colDiagram n).cells, cellFactor q z c
      = ∏ i ∈ Finset.range n, cellFactor q z (i, 0) := by
  show ∏ c ∈ Finset.range n ×ˢ {0}, cellFactor q z c = _
  rw [Finset.prod_product]
  simp

theorem prod_row (q z : ℝ) (n : ℕ) :
    ∏ c ∈ (rowDiagram n).cells, cellFactor q z c
      = ∏ j ∈ Finset.range n, cellFactor q z (0, j) := by
  show ∏ c ∈ {0} ×ˢ Finset.range n, cellFactor q z c = _
  rw [Finset.prod_product]
  simp

/-- If one factor of a growing product is negative, the two products around it are not both
positive. -/
theorem not_both_pos_of_neg {f : ℕ → ℝ} {n : ℕ} (hf : f n < 0) :
    ¬ (0 < ∏ i ∈ Finset.range n, f i ∧ 0 < ∏ i ∈ Finset.range (n + 1), f i) := by
  rintro ⟨h1, h2⟩
  rw [Finset.prod_range_succ] at h2
  nlinarith

/-- **Above the window some column factor is negative.** -/
theorem exists_col_neg {q z : ℝ} (hq : 1 < q) (hz : q - q⁻¹ < z) :
    ∃ n, cellFactor q z (n, 0) < 0 := by
  have hq0 : 0 < q := by linarith
  have hqh : q * (q - q⁻¹) = q ^ 2 - 1 := by field_simp
  have hd : 0 < q * z - (q ^ 2 - 1) := by nlinarith
  have hq2 : 1 < q ^ 2 := by nlinarith
  obtain ⟨n, hn⟩ := pow_unbounded_of_one_lt (q * z / (q * z - (q ^ 2 - 1))) hq2
  refine ⟨n, ?_⟩
  have hpow : q ^ (2 * n) = (q ^ 2) ^ n := pow_mul q 2 n
  have : q * z < (q ^ 2) ^ n * (q * z - (q ^ 2 - 1)) := (div_lt_iff₀ hd).mp hn
  simp only [cellFactor, mul_zero, zero_add, pow_one, hpow]
  nlinarith

/-- **Below the window some row factor is negative.** -/
theorem exists_row_neg {q z : ℝ} (hq : 1 < q) (hz : z < 0) :
    ∃ n, cellFactor q z (0, n) < 0 := by
  have hq0 : 0 < q := by linarith
  have hd : 0 < -(q * z) := by nlinarith
  have hq2 : 1 < q ^ 2 := by nlinarith
  obtain ⟨n, hn⟩ := pow_unbounded_of_one_lt ((q ^ 2 - 1 - q * z) / (-(q * z))) hq2
  refine ⟨n, ?_⟩
  have hpow : q ^ (2 * n + 1) = (q ^ 2) ^ n * q := by rw [pow_succ, pow_mul]
  have : q ^ 2 - 1 - q * z < (q ^ 2) ^ n * (-(q * z)) := (div_lt_iff₀ hd).mp hn
  simp only [cellFactor, mul_zero, pow_zero, one_mul, hpow]
  nlinarith

/-- **Outside the window some Ocneanu weight is not positive.** -/
theorem exists_not_pos_of_not_mem_window {q z : ℝ} (hq : 1 < q)
    (hz : ¬ (0 ≤ z ∧ z ≤ q - q⁻¹)) : ∃ mu, ¬ 0 < ocneanuWeight q z mu := by
  by_contra hall
  push_neg at hall
  rcases not_and_or.mp hz with h0 | hh
  · obtain ⟨n, hn⟩ := exists_row_neg hq (not_le.mp h0)
    refine not_both_pos_of_neg (f := fun j => cellFactor q z (0, j)) hn ⟨?_, ?_⟩
    · rw [← prod_row]; exact (weight_pos_iff hq z _).mp (hall _)
    · rw [← prod_row]; exact (weight_pos_iff hq z _).mp (hall _)
  · obtain ⟨n, hn⟩ := exists_col_neg hq (not_le.mp hh)
    refine not_both_pos_of_neg (f := fun i => cellFactor q z (i, 0)) hn ⟨?_, ?_⟩
    · rw [← prod_col]; exact (weight_pos_iff hq z _).mp (hall _)
    · rw [← prod_col]; exact (weight_pos_iff hq z _).mp (hall _)

/-- **The positive window.** For real `q > 1`, every Ocneanu weight is positive iff
`0 ≤ z ≤ q − q⁻¹`. -/
theorem forall_pos_iff {q : ℝ} (hq : 1 < q) (z : ℝ) :
    (∀ mu, 0 < ocneanuWeight q z mu) ↔ 0 ≤ z ∧ z ≤ q - q⁻¹ := by
  constructor
  · intro h
    by_contra hz
    obtain ⟨mu, hmu⟩ := exists_not_pos_of_not_mem_window hq hz
    exact hmu (h mu)
  · rintro ⟨h0, hh⟩ mu
    exact ocneanuWeight_pos_of_mem_window hq h0 hh mu

/-- The self-dual point `z = h/2` is inside the window. -/
theorem half_h_pos {q : ℝ} (hq : 1 < q) (mu : YoungDiagram) :
    0 < ocneanuWeight q ((q - q⁻¹) / 2) mu := by
  have hh : 0 ≤ q - q⁻¹ := by
    have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
    linarith
  exact ocneanuWeight_pos_of_mem_window hq (by linarith) (by linarith) mu

/-- Convention D, `z = q³/(q²+1)`, lies strictly above the window. -/
theorem conventionD_gt_h {q : ℝ} (hq : 1 < q) : q - q⁻¹ < q ^ 3 / (q ^ 2 + 1) := by
  have hq0 : 0 < q := by linarith
  rw [lt_div_iff₀ (by positivity)]
  have : (q - q⁻¹) * (q ^ 2 + 1) = q ^ 3 - q⁻¹ := by field_simp; ring
  rw [this]
  have : 0 < q⁻¹ := inv_pos.mpr hq0
  linarith

/-- Hence at convention D some weight is not positive. -/
theorem conventionD_not_all_pos {q : ℝ} (hq : 1 < q) :
    ¬ ∀ mu, 0 < ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) mu := by
  rw [forall_pos_iff hq]
  intro h
  exact absurd h.2 (not_le.mpr (conventionD_gt_h hq))

end QOU.SchurWeyl.PositiveWindow
