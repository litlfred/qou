import Mathlib.Data.Int.Basic

/-!
# Hopf Cubic Discriminant

This file contains the elementary verification that the Hopf-sector cubic
has a strictly negative discriminant, formally certifying its complex structure
(chirality parity) under the QOU framework.

The cubic is given by `C(y) = y³ - 6y² + 10y - 6`.
Its discriminant is Δ = a²b² - 4b³ - 4a³c - 27c² + 18abc = -76.
Since Δ < 0, the cubic has one real root and a complex-conjugate pair,
mirroring the chiral nature of the Hopf link.
-/

def hopfCubicDisc : ℤ :=
  let a := -6
  let b := 10
  let c := -6
  a^2 * b^2 - 4 * b^3 - 4 * a^3 * c - 27 * c^2 + 18 * a * b * c

theorem hopfCubicDisc_eq : hopfCubicDisc = -76 := by
  rfl

theorem hopfCubicDisc_neg : hopfCubicDisc < 0 := by
  rw [hopfCubicDisc_eq]
  decide
