/-!
# QOU.HyperellipticQuintic.z5_automorphism

The ℤ₅ automorphism of the hyperelliptic quintic 𝒳₅ : y² = x⁵ - 1
sending (x, y) ↦ (ζ₅ · x, y), with ζ₅ = exp(2π i / 5).

LaTeX label: `prop:x5-z5-automorphism`

**Ground ring**: `ℂ`.

Self-contained: re-defines `zeta5` and `HyperellipticQuintic`
locally, matching the block-level convention where each content
block's `.lean` file is standalone.
-/

import Mathlib.Data.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Circle

namespace QOU.X5Z5

open Complex

/-- Primitive fifth root of unity (local copy). -/
-- Ref: [bolza1887] https://doi.org/10.2307/2369402
noncomputable def zeta5 : ℂ :=
  Complex.exp (2 * Real.pi * Complex.I / 5)

/-- Defining predicate for 𝒳₅ : y² = x⁵ - 1 (local copy). -/
-- Ref: [bolza1887] https://doi.org/10.2307/2369402
def HyperellipticQuintic : ℂ × ℂ → Prop :=
  fun p => p.2 ^ 2 = p.1 ^ 5 - 1

/-- ζ₅ raised to the fifth power is 1 (sorry pending Mathlib
    lemma-name confirmation in a Lean environment). -/
-- Ref: [bolza1887] https://doi.org/10.2307/2369402
theorem zeta5_pow_five : zeta5 ^ 5 = 1 := by
  sorry

/-- **ℤ₅ automorphism of 𝒳₅**: the map (x, y) ↦ (ζ₅·x, y) preserves
    the defining equation y² = x⁵ - 1.

    LaTeX: `\label{prop:x5-z5-automorphism}`
    Ref: [bolza1887] https://doi.org/10.2307/2369402 -/
theorem z5_automorphism (p : ℂ × ℂ)
    (hp : HyperellipticQuintic p) :
    HyperellipticQuintic (zeta5 * p.1, p.2) := by
  unfold HyperellipticQuintic at hp ⊢
  simp only [mul_pow]
  rw [zeta5_pow_five, one_mul]
  exact hp

end QOU.X5Z5
