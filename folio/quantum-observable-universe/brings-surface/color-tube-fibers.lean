import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Tactic.Ring


/-!
# QOU.ColorTubeFibers

The color tube at z is an affine cubic curve defined by
c³ + (4z+1)c² + (6z²+3z+1)c + (4z³+3z²+2z+1) = 0,
isomorphic to the color elliptic fiber via the shift X = c + z.

LaTeX label: `def:color-tube-fibers`

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.Brings

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **Color tube fibre data** at spacetime ratio z.

    The affine cubic c³ + (4z+1)c² + (6z²+3z+1)c + (4z³+3z²+2z+1) = 0
    defines the color tube R_z (equivalently G_z, B_z) at z. This is
    isomorphic to the color elliptic fibre E_z via the shift X = c + z.

    Ref: [leitner2026] §5, Color fibration -/
structure ColorTubeFibre (R : Type*) [CommRing R] where
  /-- The spacetime ratio z. -/
  z : R
  /-- The color tube coordinate c (standing for r, g, or b). -/
  c : R
  /-- The defining cubic relation for the color tube. -/
  cubic_eq : c ^ 3 + (4 * z + 1) * c ^ 2 + (6 * z ^ 2 + 3 * z + 1) * c +
    (4 * z ^ 3 + 3 * z ^ 2 + 2 * z + 1) = 0

/-- The color tube cubic polynomial. -/
-- Ref: [leitner2026] §5, Color fibration
def colorTubeCubic (R : Type*) [CommRing R] (z c : R) : R :=
  c ^ 3 + (4 * z + 1) * c ^ 2 + (6 * z ^ 2 + 3 * z + 1) * c +
    (4 * z ^ 3 + 3 * z ^ 2 + 2 * z + 1)

/-- The color cubic polynomial (from color-elliptic). -/
-- Ref: [leitner2026] §5, Color fibration
def colorCubicPoly (R : Type*) [CommRing R] (z X : R) : R :=
  X ^ 3 + (z + 1) * X ^ 2 + (z ^ 2 + z + 1) * X + (z ^ 3 + z ^ 2 + z + 1)

/-- **Shift isomorphism**: substituting X = c + z in the color cubic yields
    the color tube cubic. This proves the two fibres are isomorphic. -/
-- Ref: [leitner2026] §5, Color fibration
theorem shift_isomorphism (R : Type*) [CommRing R] (z c : R) :
    colorCubicPoly R z (c + z) = colorTubeCubic R z c := by
  unfold colorCubicPoly colorTubeCubic
  ring

/-- At z = 0, the color tube cubic specialises to c³ + c² + c + 1. -/
-- Ref: [leitner2026] §5, Color fibration
theorem color_tube_at_z_zero (c : R_q) :
    colorTubeCubic R_q 0 c = c ^ 3 + c ^ 2 + c + 1 := by
  unfold colorTubeCubic
  ring

/-- The constant term of the color tube cubic is the `X = z` evaluation
    of the color cubic, written in its shifted-cubic form:
    `4z³+3z²+2z+1 = z³ + (z+1)z² + (z²+z+1)z + (z³+z²+z+1)`. -/
-- Ref: [leitner2026] §5, Color fibration
theorem constant_term_identity (z : R_q) :
    4 * z ^ 3 + 3 * z ^ 2 + 2 * z + 1 =
      z ^ 3 + (z + 1) * z ^ 2 + (z ^ 2 + z + 1) * z + (z ^ 3 + z ^ 2 + z + 1) := by
  ring

end

end QOU.Brings
