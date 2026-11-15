/-
  Stirling UPPER bound — Watson-uniqueness brick 1 (bean el8w tranche 5).

  Mathlib carries the Stirling *lower* bound `Stirling.le_factorial_stirling`
  (`√(2πn)·(n/e)ⁿ ≤ n!`) and the asymptotic `factorial_isEquivalent_stirling`,
  but NOT an explicit *upper* bound `n! ≤ C·√n·(n/e)ⁿ`. That upper bound is the
  first brick of the remaining el8w gap (Watson / Nevanlinna–Sokal uniqueness):
  the uniqueness half needs `∀N, |g| ≤ CσᴺN!rᴺ ⇒ |g| ≤ C'e^{−1/(σr)}`, whose
  optimization at `N ≈ 1/(σr)` requires bounding `N!` from ABOVE.

  The bound is immediate from the structure Mathlib already proves:
  `Stirling.stirlingSeq n = n!/(√(2n)(n/e)ⁿ)` decreases to `√π`
  (`log_stirlingSeq'_antitone`), so for `n ≥ 1` it never exceeds its first
  value `stirlingSeq 1 = e/√2` — giving

      n! = stirlingSeq n · √(2n)(n/e)ⁿ ≤ (e/√2)·√(2n)(n/e)ⁿ = e·√n·(n/e)ⁿ.

  Archimedean (ℝ): genuinely archimedean — `Real.exp`, `Real.sqrt`, ordering.

  -- Ref: [leitner2026] bean el8w tranche 5 — Watson uniqueness brick 1
-/

import Mathlib.Analysis.SpecialFunctions.Stirling

namespace QOU.Mathlib.Borel

open Stirling Real
open scoped Nat

/-- `stirlingSeq n ≤ e/√2` for `n ≥ 1`: the sequence `stirlingSeq` decreases
    (to `√π`), so past `n = 1` it never exceeds `stirlingSeq 1 = e/√2`. -/
theorem stirlingSeq_le_succ_zero (m : ℕ) :
    stirlingSeq (m + 1) ≤ Real.exp 1 / Real.sqrt 2 := by
  have hla : Real.log (stirlingSeq (m + 1)) ≤ Real.log (Real.exp 1 / Real.sqrt 2) := by
    have h := log_stirlingSeq'_antitone (Nat.zero_le m)
    simpa [Function.comp, stirlingSeq_one] using h
  have h1 : 0 < stirlingSeq (m + 1) := stirlingSeq'_pos m
  have h2 : 0 < Real.exp 1 / Real.sqrt 2 := by positivity
  calc stirlingSeq (m + 1)
      = Real.exp (Real.log (stirlingSeq (m + 1))) := (Real.exp_log h1).symm
    _ ≤ Real.exp (Real.log (Real.exp 1 / Real.sqrt 2)) := Real.exp_le_exp.mpr hla
    _ = Real.exp 1 / Real.sqrt 2 := Real.exp_log h2

/-- **Stirling upper bound.** For `n ≥ 1`,
    `n! ≤ e · √n · (n/e)ⁿ`. The companion of `Stirling.le_factorial_stirling`
    (which bounds `n!` from below); together they pin `n!` to `Θ(√n (n/e)ⁿ)`.
    Watson-uniqueness brick 1 — the piece Mathlib was missing. -/
theorem factorial_le_stirling_upper {n : ℕ} (hn : 1 ≤ n) :
    (n ! : ℝ) ≤ Real.exp 1 * Real.sqrt n * ((n : ℝ) / Real.exp 1) ^ n := by
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
  have hP : (0 : ℝ) < (((m + 1 : ℕ) : ℝ) / Real.exp 1) ^ (m + 1) := by positivity
  have hs2 : (0 : ℝ) < Real.sqrt (2 * ((m + 1 : ℕ) : ℝ)) := by
    apply Real.sqrt_pos.mpr; positivity
  have hD : (0 : ℝ) < Real.sqrt (2 * ((m + 1 : ℕ) : ℝ))
      * (((m + 1 : ℕ) : ℝ) / Real.exp 1) ^ (m + 1) := by positivity
  -- n! = stirlingSeq n · √(2n)(n/e)ⁿ
  have hfact : ((m + 1)! : ℝ)
      = stirlingSeq (m + 1)
        * (Real.sqrt (2 * ((m + 1 : ℕ) : ℝ)) * (((m + 1 : ℕ) : ℝ) / Real.exp 1) ^ (m + 1)) := by
    rw [stirlingSeq]
    field_simp
  -- multiply stirlingSeq bound by the positive tail
  have hstep := mul_le_mul_of_nonneg_right (stirlingSeq_le_succ_zero m) hD.le
  rw [hfact]
  refine hstep.trans (le_of_eq ?_)
  rw [Real.sqrt_mul (by norm_num : (0 : ℝ) ≤ 2)]
  have h2 : Real.sqrt 2 ≠ 0 := by positivity
  field_simp

end QOU.Mathlib.Borel
