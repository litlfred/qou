/-!
# QOU.ColorTubeFibers

The color tube at z is an affine cubic curve defined by
c³ + (4z+1)c² + (6z²+3z+1)c + (4z³+3z²+2z+1) = 0,
isomorphic to the coral elliptic fiber via the shift X = c + z.

LaTeX label: `def:color-tube-fibers`
-/

import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

namespace QOU.Brings

/-- **Color tube fibre data** at spacetime ratio z.

    The affine cubic c³ + (4z+1)c² + (6z²+3z+1)c + (4z³+3z²+2z+1) = 0
    defines the color tube R_z (equivalently G_z, B_z) at z. This is
    isomorphic to the coral elliptic fibre E_z via the shift X = c + z.

    Ref: [manuscript] §5, Coral fibration -/
structure ColorTubeFibre (R : Type*) [CommRing R] where
  /-- The spacetime ratio z. -/
  z : R
  /-- The color tube coordinate c (standing for r, g, or b). -/
  c : R
  /-- The defining cubic relation for the color tube. -/
  cubic_eq : c ^ 3 + (4 * z + 1) * c ^ 2 + (6 * z ^ 2 + 3 * z + 1) * c +
    (4 * z ^ 3 + 3 * z ^ 2 + 2 * z + 1) = 0

/-- The color tube cubic polynomial. -/
-- Ref: [manuscript] §5, Coral fibration
def colorTubeCubic (R : Type*) [CommRing R] (z c : R) : R :=
  c ^ 3 + (4 * z + 1) * c ^ 2 + (6 * z ^ 2 + 3 * z + 1) * c +
    (4 * z ^ 3 + 3 * z ^ 2 + 2 * z + 1)

/-- The coral cubic polynomial (from coral-elliptic). -/
-- Ref: [manuscript] §5, Coral fibration
def coralCubicPoly (R : Type*) [CommRing R] (z X : R) : R :=
  X ^ 3 + (z + 1) * X ^ 2 + (z ^ 2 + z + 1) * X + (z ^ 3 + z ^ 2 + z + 1)

/-- **Shift isomorphism**: substituting X = c + z in the coral cubic yields
    the color tube cubic. This proves the two fibres are isomorphic. -/
-- Ref: [manuscript] §5, Coral fibration
theorem shift_isomorphism (R : Type*) [CommRing R] (z c : R) :
    coralCubicPoly R z (c + z) = colorTubeCubic R z c := by
  unfold coralCubicPoly colorTubeCubic
  ring

/-- At z = 0, the color tube cubic specialises to c³ + c² + c + 1. -/
-- Ref: [manuscript] §5, Coral fibration
theorem color_tube_at_z_zero (c : ℝ) :
    colorTubeCubic ℝ 0 c = c ^ 3 + c ^ 2 + c + 1 := by
  unfold colorTubeCubic
  ring

/-- The constant term of the color tube cubic factors as
    (4z+1)(z²+1) − z(z+1). More directly: 4z³+3z²+2z+1 = (2z+1)²(z) + 1,
    but the cleanest identity is that it equals (z+1)⁴ − z⁴. -/
-- Ref: [manuscript] §5, Coral fibration
theorem constant_term_identity (z : ℝ) :
    4 * z ^ 3 + 3 * z ^ 2 + 2 * z + 1 = (z + 1) ^ 4 - z ^ 4 := by ring

end QOU.Brings
