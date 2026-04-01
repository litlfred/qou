/-!
# QOU.AlgebraicSubstrate.spectral_half_line

Corollary: the spectral coordinate mapping translates the Hasse–Weil
bound into Re(ρᵢ) = 1/2 for all fundamental Reeb modes.

LaTeX label: `cor:spectral-half-line`
-/

set_option autoImplicit false

import Mathlib.Analysis.SpecialFunctions.Complex.Analytic
import Mathlib.Analysis.SpecialFunctions.Pow.Real

open Complex Real

namespace QOU.AlgebraicSubstrate

/-- Auxiliary: for real q > 1 and complex ρ, |q^ρ| = q^{Re(ρ)}.

    This is the key identity: the absolute value of a real base
    raised to a complex power equals the base raised to the real
    part of the exponent. -/
-- Ref: [manuscript] Chapter 8, Section 4
theorem abs_rpow_eq_rpow_re (q : ℝ) (hq : q > 1) (ρ : ℂ) :
    Complex.abs ((q : ℂ) ^ ρ) = Real.rpow q ρ.re := by
  -- |q^ρ| = |q^{a+bi}| = |e^{(a+bi)·ln q}| = e^{a·ln q} = q^a
  -- where a = Re(ρ). This uses q > 0 and properties of cpow.
  -- Ref: [weil1948] https://doi.org/10.24033/bsmf.1532
  sorry

/-- **Spectral half-line**: all fundamental Reeb modes lie on the
    critical line Re(ρ) = 1/2.

    Given the spectral coordinate mapping αᵢ = q^{ρᵢ}, the
    Hasse–Weil bound |αᵢ| = q^{1/2} forces Re(ρᵢ) = 1/2.

    **Proof**: By `abs_rpow_eq_rpow_re`, |q^{ρᵢ}| = q^{Re(ρᵢ)}.
    Combined with |αᵢ| = q^{1/2}, we get q^{Re(ρᵢ)} = q^{1/2}.
    Since q > 1, the function q^(·) is strictly monotone, giving
    Re(ρᵢ) = 1/2. -/
theorem spectral_half_line
    (Z : LocalQZetaFunction)
    (hq : Z.q > 1)
    (ρ : Fin 8 → ℂ)
    (spectral_coord : ∀ i, Z.eigenvalues i = (Z.q : ℂ) ^ (ρ i))
    (hw : ∀ i, Complex.abs (Z.eigenvalues i) = Real.rpow Z.q (1 / 2)) :
    ∀ i, (ρ i).re = 1 / 2 := by
  intro i
  have h1 := hw i
  rw [spectral_coord i] at h1
  -- Now: Complex.abs ((Z.q : ℂ) ^ (ρ i)) = Real.rpow Z.q (1 / 2)
  -- By abs_rpow_eq_rpow_re: Real.rpow Z.q (ρ i).re = Real.rpow Z.q (1 / 2)
  have h2 := abs_rpow_eq_rpow_re Z.q hq (ρ i)
  rw [h2] at h1
  -- Now: Real.rpow Z.q (ρ i).re = Real.rpow Z.q (1 / 2)
  -- Since q > 1, rpow q is injective on ℝ
  exact Real.rpow_left_injective (ne_of_gt (by linarith : Z.q ≠ 1)) h1

end QOU.AlgebraicSubstrate
