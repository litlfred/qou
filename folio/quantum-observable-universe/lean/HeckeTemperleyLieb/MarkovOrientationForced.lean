import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# The Markov orientation of the level-2 quantum-trace weight is forced

Level-2 Jimbo braiding on `V ⊗ V`, `V = span(e₁, e₂)`, with `h = q - q⁻¹`:

  `Ř(eᵢ⊗eᵢ) = q eᵢ⊗eᵢ`, `Ř(e₁⊗e₂) = e₂⊗e₁`, `Ř(e₂⊗e₁) = e₁⊗e₂ + h e₂⊗e₁`,

and `Ř⁻¹ = Ř - h`. Let `K = diag(a, b)`. The partial trace `tr₂((1⊗K)Ř)` is diagonal with
entries `a q` (on `e₁`) and `a h + b q` (on `e₂`). For `Ř⁻¹` the entries are
`a q⁻¹ - b h` and `b q⁻¹`. The partial trace is a scalar (the Markov property) iff the two
entries agree.

This file proves that, for both crossings, the condition is the same: `a = b q²`.
With the normalisation `a b = 1` and `a > 0`, that gives `a = q`, i.e. `K = diag(q, q⁻¹)`.
The crossing sign therefore does not select the orientation of `K`.
No numerical value enters.
-/

namespace QOU.BraidsAndKnots.MarkovOrientationForced

variable {R : Type*} [Field R]

/-- Diagonal entries of `tr₂((1⊗K)Ř)` agree iff `a = b q²`. -/
theorem positive_crossing_markov_iff (q a b : R) (hq : q ≠ 0) :
    a * q = a * (q - q⁻¹) + b * q ↔ a = b * q ^ 2 := by
  constructor
  · intro h
    have h1 : a * q⁻¹ = b * q := by linear_combination h
    have := congrArg (· * q) h1
    simp only [mul_assoc, inv_mul_cancel₀ hq, mul_one] at this
    linear_combination this
  · intro h
    subst h
    field_simp
    ring

/-- Diagonal entries of `tr₂((1⊗K)Ř⁻¹)` agree iff `a = b q²` — the same condition. -/
theorem negative_crossing_markov_iff (q a b : R) (hq : q ≠ 0) :
    a * q⁻¹ - b * (q - q⁻¹) = b * q⁻¹ ↔ a = b * q ^ 2 := by
  constructor
  · intro h
    have h1 : a * q⁻¹ = b * q := by linear_combination h
    have := congrArg (· * q) h1
    simp only [mul_assoc, inv_mul_cancel₀ hq, mul_one] at this
    linear_combination this
  · intro h
    subst h
    field_simp
    ring

/-- Both crossing signs impose the same condition on `K`. -/
theorem same_condition_both_signs (q a b : R) (hq : q ≠ 0) :
    (a * q = a * (q - q⁻¹) + b * q) ↔ (a * q⁻¹ - b * (q - q⁻¹) = b * q⁻¹) := by
  rw [positive_crossing_markov_iff q a b hq, negative_crossing_markov_iff q a b hq]

/-- With `a b = 1`, the Markov condition gives `a² = q²`. -/
theorem markov_normalised (q a b : R) (hab : a * b = 1) (h : a = b * q ^ 2) :
    a ^ 2 = q ^ 2 := by
  calc a ^ 2 = (a * b) * q ^ 2 := by rw [h]; ring
    _ = q ^ 2 := by rw [hab, one_mul]

/-- Level `N`: the `K = q^{2ρ}` weights of adjacent basis vectors `e_i, e_{i+1}` are
`q^{N-1-2i}` and `q^{N-3-2i}`; their ratio is `q²` for every `N` and `i`.
(This is the `K` half of the level-`N` weight-space ratio; the equality of the plain traces
on permuted weight spaces is not formalised here.) -/
theorem adjacent_weight_ratio (q : R) (hq : q ≠ 0) (m : ℤ) :
    q ^ (m + 2) = q ^ (2 : ℤ) * q ^ m := by
  rw [zpow_add₀ hq, mul_comm]

end QOU.BraidsAndKnots.MarkovOrientationForced
