/-!
# QOU.HyperellipticQuintic.z5_automorphism

The ℤ₅ automorphism of the hyperelliptic quintic 𝒳₅ : y² = x⁵ - 1
sending (x, y) ↦ (ζ₅ · x, y), with ζ₅ = exp(2π i / 5).

LaTeX label: `prop:x5-z5-automorphism`

**Ground ring**: `ℂ`.
-/

import Mathlib.Data.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Circle

namespace QOU

open Complex

/-- Primitive fifth root of unity ζ₅ = exp(2π i / 5). -/
-- Ref: [manuscript] Chapter 3, §Varying Euler + mirror bundle
noncomputable def zeta5 : ℂ :=
  Complex.exp (2 * Real.pi * I / 5)

/-- Fifth power of ζ₅ equals 1. -/
-- Ref: [manuscript] Chapter 3, §Varying Euler + mirror bundle
theorem zeta5_pow_five : zeta5 ^ 5 = 1 := by
  sorry

/-- **ℤ₅ automorphism of 𝒳₅**: the map (x, y) ↦ (ζ₅·x, y) preserves
    the defining equation y² = x⁵ - 1.

    LaTeX: `\label{prop:x5-z5-automorphism}`
    Ref: [bolza1887] https://doi.org/10.2307/2369402 -/
theorem z5_automorphism (p : ℂ × ℂ)
    (hp : HyperellipticQuintic p) :
    HyperellipticQuintic (zeta5 * p.1, p.2) := by
  -- Expand: need p.2² = (ζ₅·p.1)⁵ - 1
  -- RHS = ζ₅⁵ · p.1⁵ - 1 = p.1⁵ - 1 = LHS
  unfold HyperellipticQuintic at hp ⊢
  simp only [mul_pow]
  rw [zeta5_pow_five, one_mul]
  exact hp

end QOU
