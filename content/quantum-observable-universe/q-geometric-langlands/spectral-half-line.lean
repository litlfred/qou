import Mathlib.Analysis.SpecialFunctions.Complex.Analytic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Complex.LogDeriv

/-!
# QOU.AlgebraicSubstrate.spectral_half_line

Corollary: the spectral coordinate mapping translates the Hasse–Weil
bound into Re(ρᵢ) = 1/2 for all fundamental Reeb modes.

## Proof strategy for `abs_cpow_ofReal_eq_rpow_re`

For real q > 0 and complex ρ:

  (↑q)^ρ  = exp(ρ · log(↑q))          [cpow definition, ↑q ≠ 0]
  |exp(z)| = exp(Re(z))                [Complex.abs_exp]
  (log ↑q).re = Real.log |↑q| = log q  [log_re + abs_ofReal + abs_of_pos]
  (log ↑q).im = arg(↑q) = 0            [log_im + arg_ofReal_of_nonneg]

  Hence: |(↑q)^ρ| = exp(Re(ρ)·log q - Im(ρ)·0)
                   = exp(Re(ρ)·log q)
                   = q^{Re(ρ)}           [rpow_def_of_pos]

LaTeX label: `cor:spectral-half-line`

**Ground ring**: `ℝ` (geometric/analytic realisation).
Uses ℝ-specific analysis (trig, norms, real powers).
NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

set_option autoImplicit false


open Complex Real

namespace QOU.AlgebraicSubstrate

/-- For real q > 0 and complex ρ, |q^ρ| = q^{Re(ρ)}.

    The proof uses the chain:
    `|(↑q)^ρ| = |exp(ρ · log(↑q))| = exp(Re(ρ · log(↑q)))`.
    For positive real q, `log(↑q) = log(q) + 0·i`, so
    `Re(ρ · log(↑q)) = Re(ρ) · log(q)` and
    `exp(Re(ρ) · log(q)) = q^{Re(ρ)}` by definition of `rpow`. -/
theorem abs_cpow_ofReal_eq_rpow_re (q : ℝ) (hq : 0 < q) (ρ : ℂ) :
    Complex.abs ((q : ℂ) ^ ρ) = Real.rpow q ρ.re := by
  have hq_ne : (q : ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr (ne_of_gt hq)
  -- Step 1: unfold cpow to exp(ρ * log(↑q))
  rw [Complex.cpow_def_of_ne_zero hq_ne]
  -- Step 2: |exp(z)| = exp(Re(z))
  rw [Complex.abs_exp]
  -- Step 3: Re(ρ * log(↑q)) = Re(ρ) * log(q)
  -- because (log ↑q).re = log|↑q| = log q, and (log ↑q).im = arg(↑q) = 0
  rw [Complex.mul_re, Complex.log_re, Complex.log_im,
      Complex.abs_ofReal, abs_of_pos hq,
      Complex.arg_ofReal_of_nonneg (le_of_lt hq),
      mul_zero, sub_zero]
  -- Step 4: exp(Re(ρ) * log q) = q^{Re(ρ)}
  rw [Real.rpow_def_of_pos hq]

/-- Backward-compatible alias for q > 1. -/
theorem abs_rpow_eq_rpow_re (q : ℝ) (hq : q > 1) (ρ : ℂ) :
    Complex.abs ((q : ℂ) ^ ρ) = Real.rpow q ρ.re :=
  abs_cpow_ofReal_eq_rpow_re q (by linarith) ρ

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
  rw [spectral_coord i, abs_rpow_eq_rpow_re Z.q hq (ρ i)] at h1
  -- h1 : Real.rpow Z.q (ρ i).re = Real.rpow Z.q (1 / 2)
  -- Since q > 1 (hence q ≠ 1), rpow q is injective in the exponent
  exact Real.rpow_left_injective (ne_of_gt (by linarith : (1 : ℝ) < Z.q)) h1

end QOU.AlgebraicSubstrate
