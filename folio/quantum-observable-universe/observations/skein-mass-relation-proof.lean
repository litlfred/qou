import QOU.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Group.Basic


/-!
# QOU.HadronicMass.SkeinMassRelation

Extracted from folio/quantum-observable-universe/lean/ for content-block co-location.
Source: folio/quantum-observable-universe/lean/QOU/HadronicMass.lean (monolithic)

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.HadronicMass

/-- The **Skein mass relation**: at a crossing in the color-exchange
    space, the mass functional satisfies the q-deformed Skein relation.

    - `m_plus`:  mass of the `L₊` resolution (positive crossing)
    - `m_minus`: mass of the `L₋` resolution (negative crossing)
    - `m_zero`:  mass of the `L₀` resolution (smoothing) -/
structure SkeinMassRelation where
  /-- The substrate parameter q > 1. -/
  q : ℝ
  /-- q is greater than 1. -/
  q_gt_one : q > 1
  /-- Mass of the L₊ resolution. -/
  m_plus : ℝ
  /-- Mass of the L₋ resolution. -/
  m_minus : ℝ
  /-- Mass of the L₀ resolution (smoothing). -/
  m_zero : ℝ
  /-- The Skein relation holds. -/
  skein : q * m_plus - q⁻¹ * m_minus =
    (q ^ (1/2 : ℝ) - q ^ (-(1/2 : ℝ))) * m_zero

end QOU.HadronicMass
