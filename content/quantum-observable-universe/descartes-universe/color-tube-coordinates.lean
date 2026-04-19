/-!
# QOU.ColorTubeCoordinates

Color tube coordinates: shifted spectral coordinates r = w₂ − z,
g = w₃ − z, b = w₄ − z, and space-like shift σ = w₁ − z on Bring's
surface, with color vector c⃗ = (r, g, b).

LaTeX label: `def:color-tube-coordinates`
-/

import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

namespace QOU.Brings

/-- **Color tube coordinates**: shifted spectral coordinates on Bring's surface.

    Given the spacetime ratio z = x₀/x₁ and Lagrange resolvents w₁, …, w₄,
    the color tube coordinates are the shifts r = w₂ − z, g = w₃ − z,
    b = w₄ − z, together with the space-like shift σ = w₁ − z.

    Ref: [manuscript] Chapter 5, §Color tube coordinates -/
structure ColorTubeCoordinates (R : Type*) [Ring R] where
  /-- Spacetime ratio z = x₀/x₁. -/
  z : R
  /-- Lagrange resolvent w₁. -/
  w₁ : R
  /-- Lagrange resolvent w₂. -/
  w₂ : R
  /-- Lagrange resolvent w₃. -/
  w₃ : R
  /-- Lagrange resolvent w₄. -/
  w₄ : R
  /-- Red color tube coordinate r = w₂ − z. -/
  r : R
  /-- Green color tube coordinate g = w₃ − z. -/
  g : R
  /-- Blue color tube coordinate b = w₄ − z. -/
  b : R
  /-- Space-like shift σ = w₁ − z. -/
  σ : R
  /-- r is the shift of w₂ by z. -/
  r_eq : r = w₂ - z
  /-- g is the shift of w₃ by z. -/
  g_eq : g = w₃ - z
  /-- b is the shift of w₄ by z. -/
  b_eq : b = w₄ - z
  /-- σ is the shift of w₁ by z. -/
  σ_eq : σ = w₁ - z

/-- The color vector is the triple (r, g, b). -/
-- Ref: [manuscript] Chapter 5, §Color tube coordinates
def ColorTubeCoordinates.colorVector {R : Type*} [Ring R]
    (c : ColorTubeCoordinates R) : R × R × R :=
  (c.r, c.g, c.b)

/-- The color tube coordinates recover the resolvents from z:
    wₖ = cₖ + z for each color coordinate. -/
-- Ref: [manuscript] Chapter 5, §Color tube coordinates
theorem color_recovers_resolvent {R : Type*} [Ring R]
    (c : ColorTubeCoordinates R) :
    c.r + c.z = c.w₂ ∧ c.g + c.z = c.w₃ ∧ c.b + c.z = c.w₄ := by
  refine ⟨?_, ?_, ?_⟩ <;> simp [c.r_eq, c.g_eq, c.b_eq] <;> ring

/-- The sum of all four shifted coordinates equals (w₁ + w₂ + w₃ + w₄) − 4z. -/
-- Ref: [manuscript] Chapter 5, §Color tube coordinates
theorem shifted_sum {R : Type*} [Ring R] (c : ColorTubeCoordinates R) :
    c.σ + c.r + c.g + c.b = (c.w₁ + c.w₂ + c.w₃ + c.w₄) - 4 * c.z := by
  rw [c.σ_eq, c.r_eq, c.g_eq, c.b_eq]
  ring


/-- **def:color-tube-coordinates** — placeholder stub; full definition TBD. -/
structure ColorTubeCoordinates where
  witness : ℝ
  witness_pos : 0 < witness
end QOU.Brings
