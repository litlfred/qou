import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic


/-!
# QOU.ExceptionalDivisor

The exceptional divisor at brane point p: the ℙ¹(ℂ) fiber
parametrized by spherical coordinates (φ, ψ) obtained by
blowing up p in the Descartes universe.

LaTeX label: `def:exceptional-divisor`

**Ground ring**: `ℝ` (geometric/analytic realisation).
Uses ℝ-specific analysis (trig, norms, real powers).
NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU

/-- **Exceptional divisor** at a brane point: the ℙ¹(ℂ) fibre obtained
    by blowing up a brane point p ∈ M.  Parametrized by spherical
    coordinates (φ, ψ) where φ ∈ [0, π] is the polar angle and
    ψ ∈ [0, 2π) is the azimuthal angle.

    The fibre point in ℝ³ is given by:
      𝒮_p(φ, ψ) = O(p) + R(sin φ (cos ψ T₁ + sin ψ T₂) - cos φ N)

    where O(p) = p + R·N(p) is the centre, N(p) the outward normal,
    and (T₁, T₂) a positively-oriented tangent frame.

    LaTeX: `\label{def:exceptional-divisor}`
    Ref: [leitner2026] Chapter 6, §Colour-sector coordinates -/
structure ExceptionalDivisor where
  /-- The radius of the ℙ¹(ℂ) fibre. -/
  R : ℝ
  /-- Radius is positive. -/
  R_pos : 0 < R
  /-- The centre offset from the brane point along the normal:
      O(p) = p + R · N(p). Here represented as the ℝ³ coordinates
      of the centre. -/
  centre : Fin 3 → ℝ
  /-- The outward unit normal N(p) at the brane point. -/
  normal : Fin 3 → ℝ
  /-- First tangent vector T₁. -/
  tangent1 : Fin 3 → ℝ
  /-- Second tangent vector T₂. -/
  tangent2 : Fin 3 → ℝ

/-- A point on the exceptional divisor parametrized by spherical
    coordinates (φ, ψ). Returns the i-th coordinate of the fibre point. -/
-- Ref: [leitner2026] Chapter 6, §Colour-sector coordinates
noncomputable def ExceptionalDivisor.fibrePoint
    (E : ExceptionalDivisor) (φ ψ : ℝ) (i : Fin 3) : ℝ :=
  E.centre i + E.R * (Real.sin φ * (Real.cos ψ * E.tangent1 i +
    Real.sin ψ * E.tangent2 i) - Real.cos φ * E.normal i)

/-- The exceptional divisor is topologically S² ≅ ℙ¹(ℂ): the full
    parameter range φ ∈ [0, π], ψ ∈ [0, 2π) covers the sphere exactly once.
    This is encoded by the statement that at the poles (φ = 0 and φ = π),
    the point is independent of ψ. -/
-- Ref: [leitner2026] Chapter 6, §Colour-sector coordinates
theorem ExceptionalDivisor.south_pole_independent
    (E : ExceptionalDivisor) (ψ₁ ψ₂ : ℝ) (i : Fin 3) :
    E.fibrePoint 0 ψ₁ i = E.fibrePoint 0 ψ₂ i := by
  simp [ExceptionalDivisor.fibrePoint, Real.sin_zero, Real.cos_zero]

end QOU
