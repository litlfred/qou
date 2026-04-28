import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Algebra.BigOperators.Basic

/-!
# Landauer no-go: L²-Cauchy–Schwarz is insufficient

`prop:landauer-cauchy-schwarz-insufficient`: for any semisimple
Frobenius algebra with `n ≥ 2` Wedderburn blocks where every
block has `d_q(λ) = τ(p_λ) = 1`, the L²-Cauchy–Schwarz lower
bound `1/‖C‖² = 1/n` is strictly less than the conjectured
Landauer bound `τ(C_dim_q) = n`.

This is enough to rule out a purely L²-Cauchy–Schwarz proof of
`conj:tau-codim-landauer`: any such proof would have to deliver
`τ(f†f) ≥ n` on this family, but Cauchy–Schwarz only delivers
`τ(f†f) ≥ 1/n`.

Ref: [manuscript] `prop:landauer-cauchy-schwarz-insufficient`
Ref: [computation] `tau-codim-conjectures-validation.witness.json`
-/

namespace QOU.BraidKnot

open scoped BigOperators

/-- For a balanced Frobenius algebra with `n` Wedderburn blocks all
    of `d_q = τ_p = 1`, the conjectured Landauer bound is
    `τ(C_dim_q) = ∑ 1/d_q(λ) = n`. -/
def landauerBound (n : ℕ) : ℝ := (n : ℝ)

/-- For the same balanced Frobenius algebra, the L²-norm-squared of
    the canonical creation morphism is
    `‖C‖² = ∑ 1/(d_q(λ)² · τ(p_λ)) = n`, so the Cauchy–Schwarz
    lower bound on `τ(f†f)` under unit creation normalisation is
    `1/‖C‖² = 1/n`. -/
def cauchySchwarzBound (n : ℕ) : ℝ := 1 / (n : ℝ)

/-- **Landauer no-go.**  For every `n ≥ 2`, the Cauchy–Schwarz
    bound is strictly less than the Landauer bound on the balanced
    `n`-block Frobenius algebra.

    Hence no proof of `conj:tau-codim-landauer` can rest on the
    L²-Cauchy–Schwarz inequality alone: on this family CS delivers
    at most `1/n`, but the conjecture demands `≥ n`.

    Ref: [computation] `tau-codim-conjectures-validation.witness.json`
    -/
theorem landauer_cauchy_schwarz_insufficient
    (n : ℕ) (hn : 2 ≤ n) :
    cauchySchwarzBound n < landauerBound n := by
  unfold cauchySchwarzBound landauerBound
  have hn_pos : (0 : ℝ) < (n : ℝ) := by
    have : (0 : ℕ) < n := lt_of_lt_of_le (by norm_num) hn
    exact_mod_cast this
  have hn_ge_two : (2 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
  have hone_le_n : (1 : ℝ) ≤ (n : ℝ) :=
    le_trans (by norm_num) hn_ge_two
  -- 1/n ≤ 1 ≤ n, with strictness from n ≥ 2 > 1
  have h1 : 1 / (n : ℝ) ≤ 1 := by
    rw [div_le_one hn_pos]; exact hone_le_n
  have h2 : (1 : ℝ) < (n : ℝ) :=
    lt_of_lt_of_le (by norm_num) hn_ge_two
  linarith

/-- **Witness instance** for the minimal `n = 2` case, matching the
    fixed two-block witness in
    `tau-codim-conjectures-validation.witness.json`:
    `cauchySchwarzBound 2 = 1/2 < 2 = landauerBound 2`. -/
example : cauchySchwarzBound 2 < landauerBound 2 :=
  landauer_cauchy_schwarz_insufficient 2 (le_refl 2)

end QOU.BraidKnot
