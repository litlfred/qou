/-
# The tower-summed `E₀` as a weighted word count, and why its levels are not counts

Bean `qou-y3bm`, continuing `E0ReductionWordCount.lean` (PR #8608). There, with
`t = q⁻¹`, order-zero `E₀/m_e = Σ_{k≥2} tᵏ` counts the one-generator words that
contain a Hecke reduction. The tower-summed `E₀` (`qbeta_e0.canonical`) multiplies
this by `1/(1 - ℏ_q²)`, `ℏ_q = 1 - t`. This file asks what that product counts.

## Proved here (sorry-free)

* `towerFactor_eq_q_sq_chi` — `1/(1 - ℏ_q²) = q²/(2q - 1) = q²·χ_q`, where
  `χ_q = 1/(2q - 1)` is the corpus's `q`-Lyapunov exponent
  (`information-theory/operational-entropy-properties.md`). Hence
  `E₀^tower = m_e·q·c_q·χ_q`. An identity, not a derivation.
* `towerE0_ratio_eq_tsum` — the tower total is again a POSITIVE word count, with a
  different weight per word:

      E₀^tower / m_e  =  Σ_{k≥1} (1 − 2⁻ᵏ) · tᵏ .

  A word of length `k` counts with weight `1 − 2⁻ᵏ`: the share of the `2ᵏ` binary
  labellings of its letters that are not all one fixed label.
* `levelOne_coeff_neg` — but the level decomposition is NOT a positive count. The
  `n = 1` level, `E₀⁽⁰⁾·ℏ_q²/m_e = t²(1 − t)²/(1 − t) = t²(1 − t)`, has coefficient
  `−1` on `t³`. So "the words of jet level `n`" cannot be a subset of words with
  positive weights: any reading of the levels as word sets needs signs
  (inclusion–exclusion), or the levels are not word sets at all.

## Scope

* Nothing here derives the tower. The `1/2` in `1 − 2⁻ᵏ` is exact and
  `q`-independent; a two-channel label per letter (e.g. the two Hecke eigenchannels
  `q`, `−q⁻¹`, given equal weight) would produce it, but that equal weighting is NOT
  derived and is not claimed. It is the next question, not an answer.
* The order-zero reading (indicator `k ≥ 2`) and the tower reading (`1 − 2⁻ᵏ`, which
  is nonzero already at `k = 1`) are different weight functions. The tower total is
  therefore not "order zero plus positive jet corrections" word by word.
-/
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace QOU.QBeta.E0TowerWords

section Generic

variable {R : Type*} [Field R]

/-- `1/(1 - ℏ_q²) = q²/(2q - 1)`: the tower factor is `q²·χ_q`. -/
theorem towerFactor_eq_q_sq_chi (q : R) (hq0 : q ≠ 0) (h2q : 2 * q - 1 ≠ 0) :
    (1 - (1 - 1 / q) ^ 2)⁻¹ = q ^ 2 * (1 / (2 * q - 1)) := by
  have h : 1 - (1 - 1 / q) ^ 2 = (2 * q - 1) / q ^ 2 := by
    field_simp
    ring
  rw [h]
  field_simp

/-- `E₀^tower/m_e = q·c_q·χ_q`, i.e. `1/(q(q-1)) · q²/(2q-1) = q/((q-1)(2q-1))`. -/
theorem towerE0_ratio_closed (q : R) (hq0 : q ≠ 0) (hq1 : q - 1 ≠ 0)
    (h2q : 2 * q - 1 ≠ 0) :
    1 / (q * (q - 1)) * (1 - (1 - 1 / q) ^ 2)⁻¹
      = q * (1 / (q - 1)) * (1 / (2 * q - 1)) := by
  rw [towerFactor_eq_q_sq_chi q hq0 h2q]
  field_simp

end Generic

section Archimedean

/-- **The tower total as a positive word count.** For `q > 1`, with `t = q⁻¹`,
`Σ_{k≥0} (1 − 2⁻ᵏ)·tᵏ = q/((q-1)(2q-1)) = E₀^tower/m_e` (the `k = 0` term is `0`). -/
theorem towerE0_ratio_eq_tsum {q : ℝ} (hq : 1 < q) :
    ∑' k : ℕ, (1 - (1 / 2 : ℝ) ^ k) * (1 / q) ^ k
      = q / ((q - 1) * (2 * q - 1)) := by
  have hq0 : (0:ℝ) < q := lt_trans zero_lt_one hq
  have ht0 : (0:ℝ) ≤ 1 / q := le_of_lt (by positivity)
  have ht1 : 1 / q < 1 := (div_lt_one hq0).mpr hq
  have hs0 : (0:ℝ) ≤ 1 / (2 * q) := le_of_lt (by positivity)
  have hs1 : 1 / (2 * q) < 1 := by
    rw [div_lt_one (by positivity)]; linarith
  have hA : Summable (fun k : ℕ => (1 / q) ^ k) := summable_geometric_of_lt_one ht0 ht1
  have hB : Summable (fun k : ℕ => (1 / (2 * q)) ^ k) :=
    summable_geometric_of_lt_one hs0 hs1
  have e : ∀ k : ℕ, (1 - (1 / 2 : ℝ) ^ k) * (1 / q) ^ k
      = (1 / q) ^ k - (1 / (2 * q)) ^ k := by
    intro k
    rw [sub_mul, one_mul, ← mul_pow]
    congr 2
    field_simp
  rw [tsum_congr e, hA.tsum_sub hB, tsum_geometric_of_lt_one ht0 ht1,
    tsum_geometric_of_lt_one hs0 hs1]
  have hq1 : q - 1 ≠ 0 := sub_ne_zero.mpr (ne_of_gt hq)
  have h2q : 2 * q - 1 ≠ 0 := by linarith
  have hqne : q ≠ 0 := ne_of_gt hq0
  have h2q' : -1 + q * 2 ≠ 0 := by linarith
  field_simp
  ring_nf
  field_simp
  ring

/-- **The `n = 1` jet level is not a positive count.** Its generating function is
`t²(1 - t) = t² - t³`: the coefficient of `t³` is `-1`. Stated as the polynomial
identity that exhibits the sign. -/
theorem levelOne_coeff_neg (t : ℝ) (ht : t ≠ 1) :
    t ^ 2 * (1 - t) ^ 2 / (1 - t) = t ^ 2 + (-1) * t ^ 3 := by
  have h : (1 - t) ≠ 0 := sub_ne_zero.mpr (Ne.symm ht)
  field_simp
  ring

end Archimedean

end QOU.QBeta.E0TowerWords
