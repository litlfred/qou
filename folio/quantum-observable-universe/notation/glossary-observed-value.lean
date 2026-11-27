import Mathlib.Data.Real.Basic


/-!
# QOU.ObservedValue — Glossary: observed spacetime value

The spacetime coordinate z recovered from color tube coordinates
via the Vieta identity z = S/D.

LaTeX label: `rem:glossary-observed-value`

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU

/-- The observed spacetime value: the element of 𝔸¹ recovered
    from color tube coordinates by the Vieta identity z = S/D,
    where S = Σ cᵢ and D = Σ cᵢcⱼ. -/
-- Ref: [leitner2026] Ch. 8 Glossary
structure ObservedValue where
  /-- The spacetime coordinate z. -/
  z : ℝ
  /-- Sum of color coordinates S. -/
  color_sum : ℝ
  /-- Pairwise product sum D. -/
  color_product_sum : ℝ
  /-- D ≠ 0 (non-degeneracy). -/
  denom_ne_zero : color_product_sum ≠ 0
  /-- Vieta relation: z = S/D. -/
  vieta : z = color_sum / color_product_sum

end QOU
