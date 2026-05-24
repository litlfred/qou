/-!
# QOU.BraidKnot.SW3RootRationalIntegrand

The Schur-Weyl 3-root product `λ_{SW}^(1)(z)` is the exact rational
function `-P(z)/D(z)` where `P, D` are the cross-resultant and the
derivative resultant of the color-tube cubic, respectively.

This file contains:
- Definitions of the color-tube cubic `F(z, c)`
- The numerator `P(z) = res_c(F, F_z)`
- The denominator `D(z) = res_c(F, F_c) = -disc_c(F)` (palindromic).
  For a monic cubic, `res_c(F, F_c)` is `(-1)^{n(n-1)/2} = -1` times
  `disc_c(F)`, so `D(0) = +16` while `disc_c(F)|_{z=0} = -16`.
- The proposition `sw_3root_product_degree1 = -P/D`

Proof relies on:
- Implicit function theorem (ratio of partials)
- Vieta-resultant identity `∏_k G(c_k) = Res_c(F, G)` for monic F

LaTeX label: `prop:sw-3root-rational-integrand`

## References

- Lang, "Algebra" §IV.8 — Vieta's formulas + resultants
- `picard_lefschetz_thimble.py` — production implementation
-/

import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Polynomial.Basic
import Mathlib.RingTheory.Polynomial.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

namespace QOU.BraidKnot

/-- The color-tube cubic `F(z, c) = c³ + (4z+1)c² + (6z²+3z+1)c + (4z³+3z²+2z+1)`. -/
noncomputable def colorTubeCubic (z c : ℝ) : ℝ :=
  c^3 + (4*z + 1) * c^2 + (6*z^2 + 3*z + 1) * c + (4*z^3 + 3*z^2 + 2*z + 1)

/-- ∂F/∂z. -/
noncomputable def colorTubeCubic_dz (z c : ℝ) : ℝ :=
  4 * c^2 + (12*z + 3) * c + (12*z^2 + 6*z + 2)

/-- ∂F/∂c. -/
noncomputable def colorTubeCubic_dc (z c : ℝ) : ℝ :=
  3 * c^2 + 2 * (4*z + 1) * c + (6*z^2 + 3*z + 1)

/-- Numerator polynomial `P(z) = ∏_k F_z(z, c_k) = res_c(F, F_z)`. -/
noncomputable def sw3RootProduct_numerator (z : ℝ) : ℝ :=
  64 * z^6 + 96 * z^5 + 120 * z^4 + 160 * z^3 + 105 * z^2 + 66 * z + 39

/-- Denominator polynomial `D(z) = res_c(F, F_c) = ∏_k F_c(z, c_k)`.
    For this monic cubic, `D(z) = -disc_c(F)` (sign `(-1)^{n(n-1)/2} = -1`
    with `n = 3`). Palindromic coefficients: (16, 24, 35, 50, 35, 24, 16). -/
noncomputable def sw3RootProduct_denominator (z : ℝ) : ℝ :=
  16 * z^6 + 24 * z^5 + 35 * z^4 + 50 * z^3 + 35 * z^2 + 24 * z + 16

/-- The Schur-Weyl 3-root product (degree-1 prolongation product).
    Defined as the rational function `-P(z)/D(z)`. -/
noncomputable def sw3RootProductDegree1 (z : ℝ) : ℝ :=
  - sw3RootProduct_numerator z / sw3RootProduct_denominator z

/-- **Palindrome theorem**: D(z) is palindromic.
    The coefficient sequence (16, 24, 35, 50, 35, 24, 16) is symmetric.

    Equivalently: `z^6 · D(1/z) = D(z)` (functional symmetry under z ↔ 1/z). -/
theorem sw3RootProduct_denominator_palindromic (z : ℝ) (hz : z ≠ 0) :
    z^6 * sw3RootProduct_denominator (1/z) = sw3RootProduct_denominator z := by
  unfold sw3RootProduct_denominator
  field_simp
  ring

/-- **Numerator value at q=0**: P(0) = 39. -/
theorem sw3RootProduct_numerator_at_zero :
    sw3RootProduct_numerator 0 = 39 := by
  unfold sw3RootProduct_numerator
  norm_num

/-- **Denominator value at z=0**: D(0) = 16. -/
theorem sw3RootProduct_denominator_at_zero :
    sw3RootProduct_denominator 0 = 16 := by
  unfold sw3RootProduct_denominator
  norm_num

/-- **Value at z=0**: λ_SW^(1)(0) = -39/16. -/
theorem sw3RootProductDegree1_at_zero :
    sw3RootProductDegree1 0 = -39 / 16 := by
  unfold sw3RootProductDegree1
  rw [sw3RootProduct_numerator_at_zero, sw3RootProduct_denominator_at_zero]
  norm_num

/-- **F(0, c) factors as (c+1)(c² + 1)**: the cubic at z=0 has roots
    {-1, +i, -i} (one real, two purely imaginary). -/
theorem colorTubeCubic_at_zero_factored (c : ℝ) :
    colorTubeCubic 0 c = (c + 1) * (c^2 + 1) := by
  unfold colorTubeCubic
  ring

/-- **Vieta identity for the cubic**: sum of roots = -(4z+1).
    (Statement of the Vieta consequence; proof requires
    the cubic to have three real roots, generally only true
    in a neighborhood; here we state the algebraic identity
    that for any factorization F = (c - r₁)(c - r₂)(c - r₃),
    we have r₁ + r₂ + r₃ = -(4z+1).) -/
-- Ref: [lang2002algebra] §IV.8 — Vieta's formulas
-- Proof: extract three point-values of the polynomial identity, then
-- combine them linearly to isolate the c² coefficient (which equals
-- -(r₁+r₂+r₃) in the factored form, and 4z+1 in the expanded form).
-- The combination (1/2)·F(1) + (1/2)·F(-1) − F(0) cancels the c³ and
-- linear-c terms, leaving 2·(c² coeff) on the LHS and -2·s₁ on the
-- RHS — yielding s₁ = -(4z+1).
theorem cubic_roots_sum_vieta (z : ℝ) (r₁ r₂ r₃ : ℝ)
    (h : colorTubeCubic z = fun c => (c - r₁) * (c - r₂) * (c - r₃)) :
    r₁ + r₂ + r₃ = -(4*z + 1) := by
  have h0 := congr_fun h 0
  have h1 := congr_fun h 1
  have hm1 := congr_fun h (-1)
  unfold colorTubeCubic at h0 h1 hm1
  -- h0  : … = (0 - r₁) · (0 - r₂) · (0 - r₃)        — fixes r₁r₂r₃
  -- h1  : … = (1 - r₁) · (1 - r₂) · (1 - r₃)
  -- hm1 : … = (-1 - r₁) · (-1 - r₂) · (-1 - r₃)
  -- (h1 + hm1)/2 - h0   collapses to   4z+1 = -(r₁+r₂+r₃)
  linear_combination ((1:ℝ)/2) * h1 + ((1:ℝ)/2) * hm1 - h0

/-- **Main proposition**: λ_SW^(1)(z) = -P(z)/D(z).
    This is the definition + the rational-function structure; the
    deeper claim that this equals ∏_k dc_k/dz for cubic roots c_k
    requires implicit-function theorem and Vieta-resultant identity. -/
-- Ref: [lang2002algebra] §IV.8 — Vieta-resultant identity ∏G(c_k) = Res(F, G)
-- This is the definition of sw3RootProductDegree1; the equality with
-- the production ∏_k dc_k/dz formula is an algebraic identity proved
-- in `probe_categorical_action_symbolic.py` (sympy resultant computation
-- + machine-precision numerical sanity check at z=0.1).
theorem sw3RootProductDegree1_rational_form (z : ℝ)
    (hD : sw3RootProduct_denominator z ≠ 0) :
    sw3RootProductDegree1 z * sw3RootProduct_denominator z =
        - sw3RootProduct_numerator z := by
  unfold sw3RootProductDegree1
  field_simp

end QOU.BraidKnot
