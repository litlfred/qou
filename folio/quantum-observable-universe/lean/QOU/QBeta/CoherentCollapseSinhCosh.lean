/-
Copyright (c) 2026 litlfred. All rights reserved.

# Coherent Markov-trace collapse and the sinh/cosh (bar) grading via `q = exp η`

The Q_β `c_k` precision-ladder bar-parity (cheat sheet §4: `Φ_q`/`Li_2^q`; §9.2:
the "observe last" lever) becomes elementary hyperbolic algebra once the substrate
is written `q = exp η`, `η = log q₀`:

* `h = q - q⁻¹ = 2 sinh η`      — the **bar-ODD** Hecke generator (the `c_3` sector);
* `[2]_q = q + q⁻¹ = 2 cosh η`  — the **bar-EVEN** generator (the `c_2` sector);
* the two Hecke eigenvalues are `q = exp(+η) = cosh η + sinh η` and
  `-q⁻¹ = -(cosh η - sinh η)`, so the standard-rep character of one crossing
  `χ^(2,1)(σ_1) = q + (-q⁻¹) = q - q⁻¹ = 2 sinh η` is **pure bar-odd**.

Since `c_3` is the first bar-antisymmetric coefficient (PR #1887, Lean-proved:
`cosh` bar-even, `sinh` bar-odd), it lives in the `sinh` sector. The final lemma
records the **coherent-collapse vs observe-last** gap: a coherent sum of
opposite-chirality blocks nulls the bar-odd content that the per-block
(incoherent) sum retains — the algebraic core of the owner-confirmed mechanism.

This complements PR #1887's `QBetaReebSinhParity` (the parity wall) at the
**generator** level; there is no overlap (this file is built only on Mathlib's
`Real.sinh`/`cosh`/`exp` lemmas).

Cross-refs: cheat sheet §4, §9.2; PR #1895 scope
`docs/scope/2026-06-05-qbeta-perblock-collapse-order-scope.md` +
`computations/qbeta/qbeta_coherent_collapse_sinh_cosh.py` witness.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.Ring

namespace QOU.QBeta

open Real

/-- The **bar-ODD** Hecke generator `h = q - q⁻¹` equals `2 sinh η` at `q = exp η`
(the `c_3` sector generator). -/
theorem hecke_h_eq_two_sinh (η : ℝ) :
    exp η - (exp η)⁻¹ = 2 * sinh η := by
  rw [sinh_eq, exp_neg]; ring

/-- The **bar-EVEN** generator `[2]_q = q + q⁻¹` equals `2 cosh η`
(the `c_2` sector generator). -/
theorem bracket_two_eq_two_cosh (η : ℝ) :
    exp η + (exp η)⁻¹ = 2 * cosh η := by
  rw [cosh_eq, exp_neg]; ring

/-- The positive Hecke eigenvalue: `q = exp η = cosh η + sinh η`. -/
theorem eigenvalue_pos (η : ℝ) : exp η = cosh η + sinh η := by
  rw [cosh_eq, sinh_eq]; ring

/-- The inverse eigenvalue: `q⁻¹ = exp(-η) = cosh η - sinh η`. -/
theorem eigenvalue_neg (η : ℝ) : (exp η)⁻¹ = cosh η - sinh η := by
  rw [cosh_eq, sinh_eq, exp_neg]; ring

/-- The standard-rep `(2,1)` character of one crossing `σ_1` is the sum of its two
Hecke eigenvalues `q + (-q⁻¹) = q - q⁻¹ = 2 sinh η` — **pure bar-odd**. -/
theorem std_char_sigma1_eq_two_sinh (η : ℝ) :
    exp η + (-(exp η)⁻¹) = 2 * sinh η := by
  rw [← hecke_h_eq_two_sinh]; ring

/-- `h` is **bar-ODD**: under the Lusztig bar `η ↦ -η`, `h(-η) = -h(η)`. -/
theorem hecke_h_bar_odd (η : ℝ) :
    exp (-η) - (exp (-η))⁻¹ = -(exp η - (exp η)⁻¹) := by
  simp only [hecke_h_eq_two_sinh, sinh_neg]; ring

/-- `[2]_q` is **bar-EVEN**: `[2]_q(-η) = [2]_q(η)`. -/
theorem bracket_two_bar_even (η : ℝ) :
    exp (-η) + (exp (-η))⁻¹ = exp η + (exp η)⁻¹ := by
  simp only [bracket_two_eq_two_cosh, cosh_neg]

/-- **Coherent collapse vs observe-last.** For two blocks whose bar-odd parts have
opposite chirality (`+s`, `-s` — the rotation/growth split, PR #1742), the
**coherent** sum (extract *after* summing) is `(y - y')·s`, which **nulls** at
equal weights; the **observe-last** sum (`|·|` per block, *then* sum) is
`(y + y')·s`, which **survives**. This is the algebraic core of the
owner-confirmed coherent-collapse cancellation (the `c_3`-carrying `sinh` is
exactly what the coherent sum can null while the incoherent sum keeps). -/
theorem coherent_vs_observe_last (y y' s : ℝ) (hs : 0 ≤ s) :
    (y * s + y' * (-s) = (y - y') * s) ∧
    (y * |s| + y' * |(-s)| = (y + y') * s) := by
  refine ⟨by ring, ?_⟩
  rw [abs_neg, abs_of_nonneg hs]; ring

end QOU.QBeta
