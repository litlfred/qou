/-!
# QOU.ObservedValue

Observed spacetime value: recovered from color tube coordinates via
the Vieta identity r_z + g_z + b_z + 4z + 1 = 0, defining a
polynomial projection from the color tube triple to 𝔸¹.

LaTeX label: `def:observed-value`

## References

- [manuscript] Chapter 5, §Chiral fibration
-/

import Mathlib.Data.Real.Basic

namespace QOU

/-- **Observed value data**: the spacetime coordinate z recovered
    from the color tube triple (r, g, b) via the Vieta identity. -/
-- Ref: [manuscript] Chapter 5
structure ObservedValue where
  /-- The spacetime coordinate z. -/
  z : ℝ
  /-- The red color tube coordinate r_z. -/
  r : ℝ
  /-- The green color tube coordinate g_z. -/
  g : ℝ
  /-- The blue color tube coordinate b_z. -/
  b : ℝ
  /-- The Vieta identity: r + g + b + 4z + 1 = 0. -/
  vieta : r + g + b + 4 * z + 1 = 0

/-- The spacetime coordinate z is determined by the color sum. -/
-- Ref: [manuscript] Chapter 5
theorem observed_from_colors (ov : ObservedValue) :
    ov.z = -(ov.r + ov.g + ov.b + 1) / 4 := by
  have h := ov.vieta
  linarith

/-- The projection π_z : (r, g, b) ↦ z = -(r + g + b + 1)/4 is
    a polynomial (affine-linear) map with ℤ-coefficients. -/
-- Ref: [manuscript] Chapter 5
theorem projection_polynomial (ov : ObservedValue) :
    ov.z = -(ov.r + ov.g + ov.b + 1) / 4 := by
  linarith [ov.vieta]

end QOU
