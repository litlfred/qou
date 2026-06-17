import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination


/-!
# QOU.ColorTubeCoordinates

Color tube coordinates: shifted spectral coordinates r = w₂ − z,
g = w₃ − z, b = w₄ − z, and space-like shift σ = w₁ − z on Bring's
surface, with color vector c⃗ = (r, g, b).

LaTeX label: `def:color-tube-coordinates`
-/

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

/-! ## Color-tube invariants and the Bring constraint variety

The C₅-equivariant invariants of `aggregate-color-quantities.md` and the
shifted quadric / cubic constraints of `color-tube-constraints.md`. These are
polynomial identities over a commutative ring — the resolvent coordinates
commute, so `[CommRing R]` and the formal variable for the C₅ character
`χ_ζ` suffice (no archimedean input; §7c). Formalising them lets the color
quadric `h₂` and cubic `h₃` be consumed in compute against a machine-checked
constraint contract. -/

/-- First power sum `p₁(c) = σ + r + g + b`. -/
def ColorTubeCoordinates.p1 {R : Type*} [CommRing R]
    (c : ColorTubeCoordinates R) : R :=
  c.σ + c.r + c.g + c.b

/-- Hermitian quadric `h₂(c) = σ·b + r·g`
    ([`aggregate-color-quantities`](aggregate-color-quantities.md)). -/
def ColorTubeCoordinates.h2 {R : Type*} [CommRing R]
    (c : ColorTubeCoordinates R) : R :=
  c.σ * c.b + c.r * c.g

/-- Hermitian cubic `h₃(c) = σ²·g + b²·r + r²·σ + g²·b`. -/
def ColorTubeCoordinates.h3 {R : Type*} [CommRing R]
    (c : ColorTubeCoordinates R) : R :=
  c.σ ^ 2 * c.g + c.b ^ 2 * c.r + c.r ^ 2 * c.σ + c.g ^ 2 * c.b

/-- **Spacetime recovery** (`eq:spacetime-recovery`). The Lagrange `z = S/D`
    relation `z·(χ_ζ − z) = p₁(c) + 4z` rearranges to the quadratic
    `z² − (χ_ζ − 4)·z + p₁(c) = 0` determining the spacetime coordinate. -/
-- Ref: [manuscript] Chapter 5, §Color tube constraints
theorem spacetime_recovery {R : Type*} [CommRing R]
    (c : ColorTubeCoordinates R) (χ : R)
    (h : c.z * (χ - c.z) = c.p1 + 4 * c.z) :
    c.z ^ 2 - (χ - 4) * c.z + c.p1 = 0 := by
  linear_combination -h

/-- **Shifted quadric — equivalent forms** (`eq:shifted-quadric`).
    `h₂(c) + z·p₁(c) + 2z² = 0` iff `σ·b + r·g = −z(σ+r+g+b) − 2z²`. -/
-- Ref: [manuscript] Chapter 5, §Color tube constraints
theorem shifted_quadric_iff {R : Type*} [CommRing R]
    (c : ColorTubeCoordinates R) :
    c.h2 + c.z * c.p1 + 2 * c.z ^ 2 = 0 ↔
      c.σ * c.b + c.r * c.g
        = -c.z * (c.σ + c.r + c.g + c.b) - 2 * c.z ^ 2 := by
  unfold ColorTubeCoordinates.h2 ColorTubeCoordinates.p1
  constructor <;> intro h <;> linear_combination h

/-- **Reduced cubic** (`eq:reduced-cubic`). Eliminating `h₂` via the shifted
    quadric turns the shifted cubic
    `h₃ + z(p₁² − 2h₂) + 3z²p₁ + 4z³ = 0` into
    `h₃ + z·p₁² + 5z²p₁ + 8z³ = 0`. The elimination is the ring combination
    `reduced = shifted_cubic + 2z·shifted_quadric`. -/
-- Ref: [manuscript] Chapter 5, §Color tube constraints
theorem reduced_cubic_of_shifted {R : Type*} [CommRing R]
    (c : ColorTubeCoordinates R)
    (hquad : c.h2 + c.z * c.p1 + 2 * c.z ^ 2 = 0)
    (hcubic : c.h3 + c.z * (c.p1 ^ 2 - 2 * c.h2)
                + 3 * c.z ^ 2 * c.p1 + 4 * c.z ^ 3 = 0) :
    c.h3 + c.z * c.p1 ^ 2 + 5 * c.z ^ 2 * c.p1 + 8 * c.z ^ 3 = 0 := by
  linear_combination hcubic + 2 * c.z * hquad

end QOU.Brings
