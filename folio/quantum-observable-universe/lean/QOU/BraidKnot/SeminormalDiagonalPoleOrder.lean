import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# Pole order at `q = 0` of a seminormal diagonal entry

In Hoefsmit's seminormal form the generator `σ_i` acts on the basis vector of
a standard tableau with diagonal entry `h / (1 - q^{2ρ})`, where
`h = q - q⁻¹` and `ρ` is a signed axial distance (the corpus convention is
`hoefsmitA q = h / (1 - q⁴)` at `ρ = 2`, `Mass/GammaGammaSelectorH3.lean`).

This file proves the elementary fact that `prop:crystal-r-matrix-sub-lemma`
needs about that entry, without any crystal hypothesis:

* for `ρ = m + 1 ≥ 1`, the entry is `q⁻¹ · u(q)` with
  `u = (q² - 1)/(1 - q^{2(m+1)})`, and `u` has value `-1` at `q = 0`:
  a simple pole;
* for `ρ = -(m + 1) ≤ -1`, the entry is `q^{2m+1} · v(q)` with
  `v = (q² - 1)/(q^{2(m+1)} - 1)`, and `v` has value `1` at `q = 0`:
  no pole (a zero of order `2m + 1`).

So the pole order is the indicator of one sign of `ρ`. Which sign the block
writes as `ρ ≤ -1` depends on its orientation of the axial distance; that
identification is not made here.

The statements are over a generic field (AGENTS.md §7c). The "value at
`q = 0`" of the unit factors is stated for the numerator and denominator
polynomials separately, by `Polynomial.eval 0`.

-- Ref: [hoefsmit1974] seminormal form of the Hecke algebra representations
-/

namespace QOU.BraidKnot.SeminormalDiagonalPoleOrder

open Polynomial

variable {K : Type*} [Field K]

/-- Positive axial distance `ρ = m + 1`: the diagonal entry has a factor `q⁻¹`. -/
theorem diag_pos_axial {q : K} (hq : q ≠ 0) (m : ℕ) (hd : 1 - q ^ (2 * (m + 1)) ≠ 0) :
    (q - q⁻¹) / (1 - q ^ (2 * (m + 1))) =
      q⁻¹ * ((q ^ 2 - 1) / (1 - q ^ (2 * (m + 1)))) := by
  field_simp

/-- Negative axial distance `ρ = -(m + 1)`: the diagonal entry has a factor
`q^{2m+1}`. -/
theorem diag_neg_axial {q : K} (hq : q ≠ 0) (m : ℕ) (hd : q ^ (2 * (m + 1)) - 1 ≠ 0) :
    (q - q⁻¹) / (1 - (q ^ (2 * (m + 1)))⁻¹) =
      q ^ (2 * m + 1) * ((q ^ 2 - 1) / (q ^ (2 * (m + 1)) - 1)) := by
  have hq2 : q ^ (2 * (m + 1)) ≠ 0 := pow_ne_zero _ hq
  have h1 : 1 - (q ^ (2 * (m + 1)))⁻¹ = (q ^ (2 * (m + 1)) - 1) / q ^ (2 * (m + 1)) := by
    field_simp
  rw [h1, div_div_eq_mul_div]
  field_simp
  ring

/-- The unit factors' numerator and denominators are nonzero at `q = 0`. -/
theorem unit_factors_at_zero (m : ℕ) :
    ((X : K[X]) ^ 2 - 1).eval 0 = -1 ∧
      ((1 : K[X]) - X ^ (2 * (m + 1))).eval 0 = 1 ∧
      ((X : K[X]) ^ (2 * (m + 1)) - 1).eval 0 = -1 := by
  refine ⟨?_, ?_, ?_⟩ <;> simp

end QOU.BraidKnot.SeminormalDiagonalPoleOrder
