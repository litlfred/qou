/-!
# QOU.HyperellipticQuintic

The genus-2 hyperelliptic curve 𝒳₅ : y² = x⁵ - 1, obtained as the
double cover of ℙ¹ branched at the five fifth-roots of unity and ∞.

LaTeX label: `def:hyperelliptic-quintic`

**Ground ring**: `ℂ` (algebraic geometry).

Self-contained block file (not part of `lake build` tree);
sibling block files redefine `zeta5` locally rather than importing
from here.
-/

import Mathlib.Data.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Circle

namespace QOU

open Complex

/-- **Primitive fifth root of unity** ζ₅ = exp(2π i / 5). -/
-- Ref: [bolza1887] https://doi.org/10.2307/2369402
noncomputable def zeta5 : ℂ :=
  Complex.exp (2 * Real.pi * Complex.I / 5)

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
noncomputable def quinticDefining : Polynomial ℂ :=
  Polynomial.X ^ 5 - Polynomial.C 1

/-- The `k`-th fifth-root of unity as a complex number.

    The coercion `(k.val : ℂ)` is essential: using `k.val / 5`
    would be integer division on `ℕ`, which evaluates to `0` for
    every `k ∈ Fin 5` and would make every `fifthRoot k = 1`. -/
-- Ref: [bolza1887] https://doi.org/10.2307/2369402
noncomputable def fifthRoot (k : Fin 5) : ℂ :=
  Complex.exp (2 * Real.pi * Complex.I * (k.val : ℂ) / 5)

/-- ζ₅ raised to the fifth power is 1, since
    exp(2π i / 5)^5 = exp(2π i) = 1. -/
-- Ref: [bolza1887] https://doi.org/10.2307/2369402
theorem zeta5_pow_five : zeta5 ^ 5 = 1 := by
  -- Intended proof:
  -- rw [zeta5, ← Complex.exp_nat_mul]; ring_nf;
  --   simpa using Complex.exp_two_pi_mul_I
  -- Left as sorry pending Mathlib lemma name confirmation in a
  -- Lean environment (not available in content pipeline).
  sorry

/-- Each fifth-root of unity is a root of x⁵ = 1. -/
-- Ref: [bolza1887] https://doi.org/10.2307/2369402
theorem fifthRoot_is_root (k : Fin 5) : (fifthRoot k) ^ 5 = 1 := by
  sorry

end QOU
