/-
# The six mixed-site γγ words fail the `J₄`-projected reading 3 near `q₀`

Archimedean companion of `GammaGammaFourStrandMixedTrace.lean` (bean `qou-a1hh`, PR #7950).
For each of the six m = 6 γγ words that pass reading 3 without being pure braids,
`tr(Jb · w · Jb) < 0` for every real `q` with `1 ≤ q ≤ 113/100`, an interval containing the
proton `q₀ ≈ 1.10998`. Each sign reduces to one polynomial, bounded termwise after `q = 1 + t`,
`0 ≤ t ≤ 13/100`. The interval is chosen, not fitted; no empirical number enters a proof.
No `sorry`, no axiom, no `native_decide`, no class.
-/
import QOU.QuarkState.GammaGammaFourStrandMixedTrace
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

namespace QOU.QuarkState.GammaGammaFourStrand

open Matrix QOU.QuarkState.FlavourDoubletFour

section Real


theorem mixed1_poly_neg {q : ℝ} (h1 : 1 ≤ q) (h2 : q ≤ 113 / 100) :
    2*q^10 - 3*q^8 + 3*q^6 - 4*q^4 + 2*q^2 - 2 < 0 := by
  obtain ⟨t, rfl⟩ : ∃ t, q = 1 + t := ⟨q - 1, by ring⟩
  have ht0 : 0 ≤ t := by linarith
  have htc : t ≤ 13 / 100 := by linarith
  linarith [pow_le_pow_left₀ ht0 htc 1, pow_nonneg ht0 1, pow_le_pow_left₀ ht0 htc 2, pow_nonneg ht0 2, pow_le_pow_left₀ ht0 htc 3, pow_nonneg ht0 3, pow_le_pow_left₀ ht0 htc 4, pow_nonneg ht0 4, pow_le_pow_left₀ ht0 htc 5, pow_nonneg ht0 5, pow_le_pow_left₀ ht0 htc 6, pow_nonneg ht0 6, pow_le_pow_left₀ ht0 htc 7, pow_nonneg ht0 7, pow_le_pow_left₀ ht0 htc 8, pow_nonneg ht0 8, pow_le_pow_left₀ ht0 htc 9, pow_nonneg ht0 9, pow_le_pow_left₀ ht0 htc 10, pow_nonneg ht0 10]

theorem mixed2_poly_neg {q : ℝ} (h1 : 1 ≤ q) (h2 : q ≤ 113 / 100) :
    q^6 - q^4 - 2 < 0 := by
  obtain ⟨t, rfl⟩ : ∃ t, q = 1 + t := ⟨q - 1, by ring⟩
  have ht0 : 0 ≤ t := by linarith
  have htc : t ≤ 13 / 100 := by linarith
  linarith [pow_le_pow_left₀ ht0 htc 1, pow_nonneg ht0 1, pow_le_pow_left₀ ht0 htc 2, pow_nonneg ht0 2, pow_le_pow_left₀ ht0 htc 3, pow_nonneg ht0 3, pow_le_pow_left₀ ht0 htc 4, pow_nonneg ht0 4, pow_le_pow_left₀ ht0 htc 5, pow_nonneg ht0 5, pow_le_pow_left₀ ht0 htc 6, pow_nonneg ht0 6]

theorem mixed3_poly_neg {q : ℝ} (h1 : 1 ≤ q) (h2 : q ≤ 113 / 100) :
    q^14 - 2*q^12 + 4*q^10 - 5*q^8 + 3*q^6 - 5*q^4 + q^2 - 1 < 0 := by
  obtain ⟨t, rfl⟩ : ∃ t, q = 1 + t := ⟨q - 1, by ring⟩
  have ht0 : 0 ≤ t := by linarith
  have htc : t ≤ 13 / 100 := by linarith
  linarith [pow_le_pow_left₀ ht0 htc 1, pow_nonneg ht0 1, pow_le_pow_left₀ ht0 htc 2, pow_nonneg ht0 2, pow_le_pow_left₀ ht0 htc 3, pow_nonneg ht0 3, pow_le_pow_left₀ ht0 htc 4, pow_nonneg ht0 4, pow_le_pow_left₀ ht0 htc 5, pow_nonneg ht0 5, pow_le_pow_left₀ ht0 htc 6, pow_nonneg ht0 6, pow_le_pow_left₀ ht0 htc 7, pow_nonneg ht0 7, pow_le_pow_left₀ ht0 htc 8, pow_nonneg ht0 8, pow_le_pow_left₀ ht0 htc 9, pow_nonneg ht0 9, pow_le_pow_left₀ ht0 htc 10, pow_nonneg ht0 10, pow_le_pow_left₀ ht0 htc 11, pow_nonneg ht0 11, pow_le_pow_left₀ ht0 htc 12, pow_nonneg ht0 12, pow_le_pow_left₀ ht0 htc 13, pow_nonneg ht0 13, pow_le_pow_left₀ ht0 htc 14, pow_nonneg ht0 14]

theorem mixed4_poly_neg {q : ℝ} (h1 : 1 ≤ q) (h2 : q ≤ 113 / 100) :
    q^16 - q^14 + 2*q^12 - 4*q^10 + 3*q^8 - 5*q^6 + 2*q^4 - 3*q^2 + 1 < 0 := by
  obtain ⟨t, rfl⟩ : ∃ t, q = 1 + t := ⟨q - 1, by ring⟩
  have ht0 : 0 ≤ t := by linarith
  have htc : t ≤ 13 / 100 := by linarith
  linarith [pow_le_pow_left₀ ht0 htc 1, pow_nonneg ht0 1, pow_le_pow_left₀ ht0 htc 2, pow_nonneg ht0 2, pow_le_pow_left₀ ht0 htc 3, pow_nonneg ht0 3, pow_le_pow_left₀ ht0 htc 4, pow_nonneg ht0 4, pow_le_pow_left₀ ht0 htc 5, pow_nonneg ht0 5, pow_le_pow_left₀ ht0 htc 6, pow_nonneg ht0 6, pow_le_pow_left₀ ht0 htc 7, pow_nonneg ht0 7, pow_le_pow_left₀ ht0 htc 8, pow_nonneg ht0 8, pow_le_pow_left₀ ht0 htc 9, pow_nonneg ht0 9, pow_le_pow_left₀ ht0 htc 10, pow_nonneg ht0 10, pow_le_pow_left₀ ht0 htc 11, pow_nonneg ht0 11, pow_le_pow_left₀ ht0 htc 12, pow_nonneg ht0 12, pow_le_pow_left₀ ht0 htc 13, pow_nonneg ht0 13, pow_le_pow_left₀ ht0 htc 14, pow_nonneg ht0 14, pow_le_pow_left₀ ht0 htc 15, pow_nonneg ht0 15, pow_le_pow_left₀ ht0 htc 16, pow_nonneg ht0 16]

theorem mixed5_poly_neg {q : ℝ} (h1 : 1 ≤ q) (h2 : q ≤ 113 / 100) :
    q^16 - 2*q^12 + 4*q^10 - 5*q^8 + q^6 - 2*q^4 + 2*q^2 - 1 < 0 := by
  obtain ⟨t, rfl⟩ : ∃ t, q = 1 + t := ⟨q - 1, by ring⟩
  have ht0 : 0 ≤ t := by linarith
  have htc : t ≤ 13 / 100 := by linarith
  linarith [pow_le_pow_left₀ ht0 htc 1, pow_nonneg ht0 1, pow_le_pow_left₀ ht0 htc 2, pow_nonneg ht0 2, pow_le_pow_left₀ ht0 htc 3, pow_nonneg ht0 3, pow_le_pow_left₀ ht0 htc 4, pow_nonneg ht0 4, pow_le_pow_left₀ ht0 htc 5, pow_nonneg ht0 5, pow_le_pow_left₀ ht0 htc 6, pow_nonneg ht0 6, pow_le_pow_left₀ ht0 htc 7, pow_nonneg ht0 7, pow_le_pow_left₀ ht0 htc 8, pow_nonneg ht0 8, pow_le_pow_left₀ ht0 htc 9, pow_nonneg ht0 9, pow_le_pow_left₀ ht0 htc 10, pow_nonneg ht0 10, pow_le_pow_left₀ ht0 htc 11, pow_nonneg ht0 11, pow_le_pow_left₀ ht0 htc 12, pow_nonneg ht0 12, pow_le_pow_left₀ ht0 htc 13, pow_nonneg ht0 13, pow_le_pow_left₀ ht0 htc 14, pow_nonneg ht0 14, pow_le_pow_left₀ ht0 htc 15, pow_nonneg ht0 15, pow_le_pow_left₀ ht0 htc 16, pow_nonneg ht0 16]

theorem mixed6_poly_neg {q : ℝ} (h1 : 1 ≤ q) (h2 : q ≤ 113 / 100) :
    q^18 - 5*q^16 + 11*q^14 - 13*q^12 + 13*q^10 - 13*q^8 + 8*q^6 - 4*q^4 + q^2 - 1 < 0 := by
  obtain ⟨t, rfl⟩ : ∃ t, q = 1 + t := ⟨q - 1, by ring⟩
  have ht0 : 0 ≤ t := by linarith
  have htc : t ≤ 13 / 100 := by linarith
  linarith [pow_le_pow_left₀ ht0 htc 1, pow_nonneg ht0 1, pow_le_pow_left₀ ht0 htc 2, pow_nonneg ht0 2, pow_le_pow_left₀ ht0 htc 3, pow_nonneg ht0 3, pow_le_pow_left₀ ht0 htc 4, pow_nonneg ht0 4, pow_le_pow_left₀ ht0 htc 5, pow_nonneg ht0 5, pow_le_pow_left₀ ht0 htc 6, pow_nonneg ht0 6, pow_le_pow_left₀ ht0 htc 7, pow_nonneg ht0 7, pow_le_pow_left₀ ht0 htc 8, pow_nonneg ht0 8, pow_le_pow_left₀ ht0 htc 9, pow_nonneg ht0 9, pow_le_pow_left₀ ht0 htc 10, pow_nonneg ht0 10, pow_le_pow_left₀ ht0 htc 11, pow_nonneg ht0 11, pow_le_pow_left₀ ht0 htc 12, pow_nonneg ht0 12, pow_le_pow_left₀ ht0 htc 13, pow_nonneg ht0 13, pow_le_pow_left₀ ht0 htc 14, pow_nonneg ht0 14, pow_le_pow_left₀ ht0 htc 15, pow_nonneg ht0 15, pow_le_pow_left₀ ht0 htc 16, pow_nonneg ht0 16, pow_le_pow_left₀ ht0 htc 17, pow_nonneg ht0 17, pow_le_pow_left₀ ht0 htc 18, pow_nonneg ht0 18]

/-- **`B0.V1.B0.V1.B1.V0` fails the `J₄`-projected reading 3 on `[1, 113/100]` ∋ `q₀`:** its `Jb` diagonal is negative. -/
theorem mixed1_Jb_trace_neg {q : ℝ} (h1 : 1 ≤ q) (h2 : q ≤ 113 / 100) :
    Matrix.trace (Jb q * mixed1 q * Jb q) < 0 := by
  have hq : q ≠ 0 := ne_of_gt (by linarith)
  have hn : q ^ 2 + 1 ≠ 0 := by positivity
  have hD : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  rw [mixed1_trace hq hn hD]
  apply div_neg_of_neg_of_pos
  · exact mul_neg_of_pos_of_neg (by positivity) (mixed1_poly_neg h1 h2)
  · positivity

/-- **`B0.V1.B1.V0.B0.V1` fails the `J₄`-projected reading 3 on `[1, 113/100]` ∋ `q₀`:** its `Jb` diagonal is negative. -/
theorem mixed2_Jb_trace_neg {q : ℝ} (h1 : 1 ≤ q) (h2 : q ≤ 113 / 100) :
    Matrix.trace (Jb q * mixed2 q * Jb q) < 0 := by
  have hq : q ≠ 0 := ne_of_gt (by linarith)
  have hn : q ^ 2 + 1 ≠ 0 := by positivity
  have hD : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  rw [mixed2_trace hq hn hD]
  apply div_neg_of_neg_of_pos
  · exact mul_neg_of_pos_of_neg (by positivity) (mixed2_poly_neg h1 h2)
  · positivity

/-- **`V1.B0.V1.B1.V0.B0` fails the `J₄`-projected reading 3 on `[1, 113/100]` ∋ `q₀`:** its `Jb` diagonal is negative. -/
theorem mixed3_Jb_trace_neg {q : ℝ} (h1 : 1 ≤ q) (h2 : q ≤ 113 / 100) :
    Matrix.trace (Jb q * mixed3 q * Jb q) < 0 := by
  have hq : q ≠ 0 := ne_of_gt (by linarith)
  have hn : q ^ 2 + 1 ≠ 0 := by positivity
  have hD : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  rw [mixed3_trace hq hn hD]
  apply div_neg_of_neg_of_pos
  · exact mixed3_poly_neg h1 h2
  · positivity

/-- **`V1.B1.V0.B0.V1.B0` fails the `J₄`-projected reading 3 on `[1, 113/100]` ∋ `q₀`:** its `Jb` diagonal is negative. -/
theorem mixed4_Jb_trace_neg {q : ℝ} (h1 : 1 ≤ q) (h2 : q ≤ 113 / 100) :
    Matrix.trace (Jb q * mixed4 q * Jb q) < 0 := by
  have hq : q ≠ 0 := ne_of_gt (by linarith)
  have hn : q ^ 2 + 1 ≠ 0 := by positivity
  have hD : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  rw [mixed4_trace hq hn hD]
  apply div_neg_of_neg_of_pos
  · exact mixed4_poly_neg h1 h2
  · positivity

/-- **`B1.V0.B0.V1.B0.V1` fails the `J₄`-projected reading 3 on `[1, 113/100]` ∋ `q₀`:** its `Jb` diagonal is negative. -/
theorem mixed5_Jb_trace_neg {q : ℝ} (h1 : 1 ≤ q) (h2 : q ≤ 113 / 100) :
    Matrix.trace (Jb q * mixed5 q * Jb q) < 0 := by
  have hq : q ≠ 0 := ne_of_gt (by linarith)
  have hn : q ^ 2 + 1 ≠ 0 := by positivity
  have hD : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  rw [mixed5_trace hq hn hD]
  apply div_neg_of_neg_of_pos
  · exact mul_neg_of_pos_of_neg (by positivity) (mixed5_poly_neg h1 h2)
  · positivity

/-- **`B1.V0.B1.V0.B1.V0` fails the `J₄`-projected reading 3 on `[1, 113/100]` ∋ `q₀`:** its `Jb` diagonal is negative. -/
theorem mixed6_Jb_trace_neg {q : ℝ} (h1 : 1 ≤ q) (h2 : q ≤ 113 / 100) :
    Matrix.trace (Jb q * mixed6 q * Jb q) < 0 := by
  have hq : q ≠ 0 := ne_of_gt (by linarith)
  have hn : q ^ 2 + 1 ≠ 0 := by positivity
  have hD : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  rw [mixed6_trace hq hn hD]
  apply div_neg_of_neg_of_pos
  · exact mul_neg_of_pos_of_neg (by positivity) (mixed6_poly_neg h1 h2)
  · positivity

end Real

end QOU.QuarkState.GammaGammaFourStrand
