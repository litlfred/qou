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
-- Ref: [bolza1887] Bolza, "On binary sextics with linear transformations into themselves," Amer. J. Math. 10 (1887)
noncomputable def zeta5 : ℂ :=
  Complex.exp (2 * Real.pi * Complex.I / 5)

/-- Defining predicate for 𝒳₅ : y² = x⁵ - 1 (local copy). -/
-- Ref: [bolza1887] Bolza, "On binary sextics with linear transformations into themselves," Amer. J. Math. 10 (1887)
def HyperellipticQuintic : ℂ × ℂ → Prop :=
  fun p => p.2 ^ 2 = p.1 ^ 5 - 1

/-- ζ₅ raised to the fifth power is 1.
    `zeta5^5 = (exp(2πi/5))^5 = exp(5 · 2πi/5) = exp(2πi) = 1`. -/
-- Ref: [bolza1887] Bolza, "On binary sextics with linear transformations into themselves," Amer. J. Math. 10 (1887)
theorem zeta5_pow_five : zeta5 ^ 5 = 1 := by
  unfold zeta5
  rw [← Complex.exp_nat_mul]
  have h5 : (5 : ℕ) * (2 * (Real.pi : ℂ) * Complex.I / 5) =
      2 * (Real.pi : ℂ) * Complex.I := by
    push_cast
    ring
  rw [h5]
  exact Complex.exp_two_pi_mul_I

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
