/-
  Toroidal locus of the Hoefsmit mixing ladder.

  Matching the associated-Legendre order-ladder factor (n - μ)(n + μ + 1),
  at degree n = d + α and order μ = β, against the squared Hoefsmit
  channel-mixing numerator d² - 1 IDENTICALLY in the axial distance d
  forces α = -1/2 and β ∈ {1/2, -3/2}: the half-integer degree shift of
  the toroidal harmonic family P^μ_{ν-1/2} is derived, not imposed.

  Generic field of characteristic zero (§7c: no ℝ, no ordering — the
  argument is pure polynomial-coefficient matching).

  -- Ref: [whipple1917] https://doi.org/10.1112/plms/s2-16.1.301
  -- Ref: [wenzl1988c] https://doi.org/10.1007/BF01388470
-/

import Mathlib.Tactic

namespace QOU.BraidsAndKnots

variable {R : Type*} [Field R] [CharZero R]

/-- The toroidal locus is valid: at α = -1/2, β = 1/2 the ladder factor
    reproduces `d² - 1` for every `d`. -/
theorem toroidal_locus_valid (d : R) :
    (d + -(1/2) - 1/2) * (d + -(1/2) + 1/2 + 1) = d ^ 2 - 1 := by
  ring

/-- **Uniqueness (the forcing theorem).** If the ladder factor at constant
    shifts `(α, β)` reproduces `d² - 1` identically in `d`, then
    `α = -1/2` and `β ∈ {1/2, -3/2}` (the Legendre reflection pair
    `μ ↔ -μ - 1`). The half-integer degree shift is forced. -/
theorem toroidal_locus_forced (α β : R)
    (h : ∀ d : R, (d + α - β) * (d + α + β + 1) = d ^ 2 - 1) :
    α = -(1/2) ∧ (β = 1/2 ∨ β = -(3/2)) := by
  have hα : α = -(1/2) := by linear_combination (h 1 - h (-1)) / 4
  subst hα
  have hβ : (β - 1/2) * (β + 3/2) = 0 := by linear_combination -(h 0)
  rcases mul_eq_zero.mp hβ with hb | hb
  · exact ⟨rfl, Or.inl (by linear_combination hb)⟩
  · exact ⟨rfl, Or.inr (by linear_combination hb)⟩

end QOU.BraidsAndKnots
