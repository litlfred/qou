/-!
# QOU.HyperellipticQuintic

The genus-2 hyperelliptic curve 𝒳₅ : y² = x⁵ - 1, obtained as the
double cover of ℙ¹ branched at the five fifth-roots of unity and ∞.

LaTeX label: `def:hyperelliptic-quintic`

**Ground ring**: `ℂ` (algebraic geometry).  Uses complex analysis
for the affine model.
-/

import Mathlib.Data.Complex.Basic
import Mathlib.Data.Polynomial.Basic

namespace QOU

open Complex Polynomial

/-- **The hyperelliptic quintic 𝒳₅**: the affine plane curve
    y² = x⁵ - 1 in ℂ².  Represented as a predicate on pairs
    (x, y) ∈ ℂ × ℂ; the smooth projective completion adds one
    point at infinity.

    Its six branch points under x ↦ x are the five fifth-roots of
    unity ζ₅^k (k = 0, ..., 4) together with ∞.  By Riemann-Hurwitz
    the genus is (6 - 2)/2 = 2.

    LaTeX: `\label{def:hyperelliptic-quintic}`
    Ref: [bolza1887] https://doi.org/10.2307/2369402 -/
def HyperellipticQuintic : ℂ × ℂ → Prop :=
  fun p => p.2 ^ 2 = p.1 ^ 5 - 1

/-- The defining polynomial P(x) = x⁵ - 1 of the double cover. -/
-- Ref: [bolza1887] https://doi.org/10.2307/2369402
noncomputable def quinticDefining : ℂ[X] :=
  X ^ 5 - C 1

/-- The five fifth-roots of unity as complex numbers. -/
-- Ref: [bolza1887] https://doi.org/10.2307/2369402
noncomputable def fifthRoot (k : Fin 5) : ℂ :=
  Complex.exp (2 * Real.pi * I * k.val / 5)

/-- Each fifth-root is a root of the defining polynomial: x⁵ = 1. -/
-- Ref: [bolza1887] https://doi.org/10.2307/2369402
theorem fifthRoot_is_root (k : Fin 5) : (fifthRoot k) ^ 5 = 1 := by
  sorry

end QOU
