/-
# `E₀` as a count of Hecke reduction words, and what that does and does not give

Bean `qou-y3bm`, owner option (a), 2026-11-20: "define + derive `E₀` at jet level `n`".
A level-`n` definition needs `E₀⁽⁰⁾` itself to come from a structure, and in the
corpus it does not: `E₀ = m_e/(q(q-1))` is stated in `rem:energy-scale-planck` as
"the energy of one Hecke reduction step `σ² → hσ + 1`", and both Lean definitions
(`QBetaEnergyScale.E0`, `hadronicScaleE0`) are bare `def`s.

This file turns that sentence into a counting statement and proves it.

## The counting reading (proved)

Grade words in ONE Hecke generator `σ` (the two-strand algebra `H₂`) by length and
weight a word of length `k` by `t^k`, `t = q⁻¹`. Then, for `q > 1`:

* all non-empty words:            `Σ_{k≥1} tᵏ = 1/(q-1) = c_q`       (`cq_eq_tsum`)
* words that contain a reduction: `Σ_{k≥2} tᵏ = 1/(q(q-1)) = E₀/m_e` (`E0_ratio_eq_tsum`)

The words containing a reduction are exactly those NOT in Gröbner–Shirshov normal
form: the normal forms of `H₂` are `{1, σ}` (leading term `σ²`). So

    E₀ / m_e  =  (Hilbert series of the free monoid on σ) − (Hilbert series of the
                  normal forms {1, σ}),  evaluated at t = q⁻¹      (`E0_ratio_eq_free_sub_nf`)

and `E₀/m_e = c_q − q⁻¹` (`E0_ratio_eq_cq_sub`, over any field). This reads the
remark's own phrase literally: `E₀/m_e` is the `q⁻¹`-weighted number of words in
which a reduction step occurs.

## Scope — what this is NOT

1. **It is a reading, not a derivation of `E₀` from the categorical chain.** The
   premise "an energy scale equals the `q⁻¹`-weighted count of reducible words" is
   not proved. What is proved is that the corpus's `E₀` equals that count, so the
   reading costs no parameter. It is not selected against data: `E₀` was fixed
   before and independently of it.
2. **It is specific to one generator.** For two generators (`H₃`) the free-monoid
   series is `1/(1-2t)`, which diverges for `t ≥ 1/2`, i.e. for `q ≤ 2`; at
   `q₀ ≈ 1.11` it diverges (`free_two_gen_diverges`). So the reading does not
   extend to `H₃` as stated.
3. **It does not produce the tower factor `1/(1-ℏ_q²)`.** The obvious level grading,
   by powers of the leading-term ideal `(σ²)ⁿ = (σ^{2n})`, gives
   `Σ_{n≥1} t^{2n}/(1-t) = E₀/m_e · 1/(1-t²)` (`leadingIdealPowers_sum`). The factor
   is `1/(1 - q⁻²)` (≈ 5.31 at `q₀`), not `1/(1 - ℏ_q²)` (≈ 1.0099). Their equality
   would need `q⁻² = ℏ_q²`, i.e. `q = 2` (`idealPowers_factor_eq_tower_iff`).
   Scope (a): this grading, alone, is not the brane tower. It does not exclude
   another grading.
-/
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace QOU.QBeta.E0Words

section Generic

variable {R : Type*} [Field R]

/-- `E₀/m_e = 1/(q(q-1))` equals `c_q − q⁻¹ = 1/(q-1) − 1/q`, over any field. -/
theorem E0_ratio_eq_cq_sub (q : R) (hq0 : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    1 / (q * (q - 1)) = 1 / (q - 1) - 1 / q := by
  field_simp
  ring

/-- The two-term tower factor is also a rational identity: with `ℏ_q = 1 - 1/q`,
`1 - ℏ_q² = (2q - 1)/q²`. -/
theorem one_sub_hbar_sq (q : R) (hq0 : q ≠ 0) :
    1 - (1 - 1 / q) ^ 2 = (2 * q - 1) / q ^ 2 := by
  field_simp
  ring

/-- **The ideal-powers grading reproduces the tower factor only at `q = 2`.**
`1/(1 - q⁻²) = 1/(1 - ℏ_q²)` iff `q⁻² = ℏ_q² = (1 - q⁻¹)²`, and over any field
that holds iff `q = 2` (the branch `q⁻¹ = -(1 - q⁻¹)` would
force `0 = 1`). -/
theorem idealPowers_factor_eq_tower_iff (q : R) (hq0 : q ≠ 0) :
    (1 / q) ^ 2 = (1 - 1 / q) ^ 2 ↔ q = 2 := by
  rw [sq_eq_sq_iff_eq_or_eq_neg]
  constructor
  · rintro (h | h)
    · field_simp at h
      linear_combination -h
    · exfalso
      have : (1 : R) = 0 := by linear_combination h
      exact one_ne_zero this
  · intro h
    left
    subst h
    field_simp
    ring

end Generic

section Archimedean

/-- Weight of a word of length `k`: `t^k`, `t = q⁻¹`. -/
noncomputable def wt (q : ℝ) (k : ℕ) : ℝ := (1 / q) ^ k

private lemma t_bounds {q : ℝ} (hq : 1 < q) : 0 ≤ 1 / q ∧ 1 / q < 1 := by
  have hq0 : (0:ℝ) < q := lt_trans zero_lt_one hq
  exact ⟨le_of_lt (by positivity), (div_lt_one hq0).mpr hq⟩

/-- **`c_q` counts the non-empty words.** `Σ_{k≥1} q^{-k} = 1/(q-1)`. -/
theorem cq_eq_tsum {q : ℝ} (hq : 1 < q) :
    ∑' k : ℕ, wt q (k + 1) = 1 / (q - 1) := by
  obtain ⟨h0, h1⟩ := t_bounds hq
  have hq0 : q ≠ 0 := ne_of_gt (lt_trans zero_lt_one hq)
  have hq1 : q - 1 ≠ 0 := sub_ne_zero.mpr (ne_of_gt hq)
  have e : ∀ k : ℕ, wt q (k + 1) = (1 / q) * (1 / q) ^ k := by
    intro k; unfold wt; ring
  rw [tsum_congr e, tsum_mul_left, tsum_geometric_of_lt_one h0 h1]
  field_simp

/-- **`E₀/m_e` counts the words that contain a reduction.**
`Σ_{k≥2} q^{-k} = 1/(q(q-1))`. -/
theorem E0_ratio_eq_tsum {q : ℝ} (hq : 1 < q) :
    ∑' k : ℕ, wt q (k + 2) = 1 / (q * (q - 1)) := by
  obtain ⟨h0, h1⟩ := t_bounds hq
  have hq0 : q ≠ 0 := ne_of_gt (lt_trans zero_lt_one hq)
  have hq1 : q - 1 ≠ 0 := sub_ne_zero.mpr (ne_of_gt hq)
  have e : ∀ k : ℕ, wt q (k + 2) = (1 / q) ^ 2 * (1 / q) ^ k := by
    intro k; unfold wt; ring
  rw [tsum_congr e, tsum_mul_left, tsum_geometric_of_lt_one h0 h1]
  field_simp

/-- **Free minus normal forms.** The Hilbert series of all words in one generator,
minus that of the `H₂` normal forms `{1, σ}`, is `E₀/m_e`. -/
theorem E0_ratio_eq_free_sub_nf {q : ℝ} (hq : 1 < q) :
    (∑' k : ℕ, wt q k) - (wt q 0 + wt q 1) = 1 / (q * (q - 1)) := by
  obtain ⟨h0, h1⟩ := t_bounds hq
  have hq0 : q ≠ 0 := ne_of_gt (lt_trans zero_lt_one hq)
  have hq1 : q - 1 ≠ 0 := sub_ne_zero.mpr (ne_of_gt hq)
  unfold wt
  rw [tsum_geometric_of_lt_one h0 h1]
  field_simp
  ring

/-- **The ideal-powers grading.** Summing the Hilbert series of `(σ^{2n})`,
`t^{2n}/(1-t)`, over `n ≥ 1` gives `E₀/m_e · 1/(1 - q⁻²)`. -/
theorem leadingIdealPowers_sum {q : ℝ} (hq : 1 < q) :
    ∑' n : ℕ, (1 / q) ^ (2 * (n + 1)) / (1 - 1 / q)
      = 1 / (q * (q - 1)) * (1 - (1 / q) ^ 2)⁻¹ := by
  obtain ⟨h0, h1⟩ := t_bounds hq
  have hq0 : q ≠ 0 := ne_of_gt (lt_trans zero_lt_one hq)
  have hq1 : q - 1 ≠ 0 := sub_ne_zero.mpr (ne_of_gt hq)
  have ht2 : 0 ≤ (1 / q) ^ 2 := sq_nonneg _
  have ht2' : (1 / q) ^ 2 < 1 := by nlinarith
  have hne : 1 - 1 / q ≠ 0 := by linarith
  have e : ∀ n : ℕ, (1 / q) ^ (2 * (n + 1)) / (1 - 1 / q)
      = ((1 / q) ^ 2 / (1 - 1 / q)) * ((1 / q) ^ 2) ^ n := by
    intro n
    rw [← pow_mul, show 2 * (n + 1) = 2 + 2 * n by ring, pow_add]
    ring
  rw [tsum_congr e, tsum_mul_left, tsum_geometric_of_lt_one ht2 ht2']
  field_simp

/-- **The two-generator free series diverges at the substrate.** For `1 < q ≤ 2`
the ratio `2t = 2/q ≥ 1`, so `Σ (2t)^k` is not summable: the counting reading does
not extend to `H₃` as stated. -/
theorem free_two_gen_diverges {q : ℝ} (hq : 1 < q) (hq2 : q ≤ 2) :
    ¬ Summable (fun k : ℕ => (2 / q) ^ k) := by
  have hq0 : (0:ℝ) < q := lt_trans zero_lt_one hq
  have h1 : 1 ≤ 2 / q := by rw [le_div_iff₀ hq0]; linarith
  rw [summable_geometric_iff_norm_lt_one]
  rw [Real.norm_eq_abs, abs_of_nonneg (by linarith)]
  linarith

end Archimedean

end QOU.QBeta.E0Words
