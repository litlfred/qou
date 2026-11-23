import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.Ring

/-!
# `α_EM` Habiro element: Laurent bar-involution fixed point, Chebyshev expansion, & cyclotomic values

The `α_EM` next-order factor is the **Habiro element**
`H(q) = [2]_q · (1 − h²·α)`, where `[2]_q = q + q⁻¹` and `h = q − q⁻¹`
(`prop:alpha-em-habiro-bar-involution`).

## Mathematical formalisation

1. **Two-variable generic-ring model `alphaEmHabiro q qi α`** (`q · qi = 1`):
   - Bar-involution symmetry `H(qi, q, α) = H(q, qi, α)` (`alphaEmHabiro_bar_invariant`);
   - Exact symmetric Laurent / Chebyshev Fourier expansion
     `H(q, q⁻¹, α) = (1 + α)(q + q⁻¹) − α(q³ + q⁻³)` whenever `q · q⁻¹ = 1`
     (`alphaEmHabiro_fourier_expansion`, matching `alpha_em_q_difference_fourier.py`);
   - Cyclotomic root-of-unity evaluations:
     * `ζ₁ = 1`: `H(1, 1, α) = 2` (`alphaEmHabiro_at_one`),
     * `ζ₂ = −1`: `H(−1, −1, α) = −2` (`alphaEmHabiro_at_neg_one`),
     * `ζ₄` (`ζ² = −1`, `ζ⁻¹ = −ζ`): `H(ζ, −ζ, α) = 0` (`alphaEmHabiro_zeta4_inv_and_zero`),
     * `ζ₃` (`ζ² + ζ + 1 = 0`, `ζ⁻¹ = −1 − ζ`): `H(ζ, ζ⁻¹, α) = −(1 + 3α)`
       (`alphaEmHabiro_at_zeta3`).

2. **Genuine Laurent-polynomial ring-automorphism fixed point**:
   Over `LaurentPolynomial R = R[q, q⁻¹]`, `LaurentPolynomial.invert` (`q^n ↦ q^{-n}`)
   is an involutive ring automorphism (`invert (invert f) = f`), and the
   canonical Habiro Laurent polynomial `habiroLaurentPoly α` is proved to be an
   exact fixed point of `LaurentPolynomial.invert` (`habiroLaurentPoly_invert_fixed`).

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

namespace QOU.BraidKnot

section GenericRing

variable {R : Type*} [CommRing R]

/-- The `α_EM` **Habiro element** `H = [2]_q · (1 − h²·α)` written with `q` and
    `qi` representing `q` and `q⁻¹` over a generic commutative ring `R`. -/
def alphaEmHabiro (q qi α : R) : R :=
  (q + qi) * (1 - (q - qi) ^ 2 * α)

/-- **Bar-involution fixed point, special values, Fourier expansion, & cyclotomic zero**
    (`prop:alpha-em-habiro-bar-involution`):
    `H(qi, q, α) = H(q, qi, α)` for all `q, qi, α : R`. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem alphaEmHabiro_bar_invariant (q qi α : R) :
    alphaEmHabiro qi q α = alphaEmHabiro q qi α := by
  unfold alphaEmHabiro
  ring

/-- **Exact symmetric-Laurent Fourier expansion**: whenever `q · qi = 1`,
    `H(q, qi, α) = (1 + α)(q + qi) − α(q³ + qi³)`, expressing `H` as an explicit
    linear combination of the bar-even Chebyshev modes `q + q⁻¹` and `q³ + q⁻³`. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
theorem alphaEmHabiro_fourier_expansion {q qi : R} (hq : q * qi = 1) (α : R) :
    alphaEmHabiro q qi α = (1 + α) * (q + qi) - α * (q ^ 3 + qi ^ 3) := by
  unfold alphaEmHabiro
  calc (q + qi) * (1 - (q - qi) ^ 2 * α)
      = (1 + α) * (q + qi) - α * (q ^ 3 + qi ^ 3) +
          α * (q + qi) * (q * qi - 1) := by ring
    _ = (1 + α) * (q + qi) - α * (q ^ 3 + qi ^ 3) := by
        rw [hq, sub_self, mul_zero, add_zero]

/-- **Special value `H(ζ₁) = H(1) = 2`** (classical leading term for `α/(4π)`). -/
theorem alphaEmHabiro_at_one (α : R) :
    alphaEmHabiro 1 1 α = 2 := by
  unfold alphaEmHabiro
  ring

/-- **Special value `H(ζ₂) = H(−1) = −2`** (charge-conjugation sign mode). -/
theorem alphaEmHabiro_at_neg_one (α : R) :
    alphaEmHabiro (-1) (-1) α = -2 := by
  unfold alphaEmHabiro
  ring

/-- **Exact modular zero `H(ζ₄) = 0`** at `qi = −ζ`. -/
theorem alphaEmHabiro_at_zeta4 (ζ α : R) :
    alphaEmHabiro ζ (-ζ) α = 0 := by
  unfold alphaEmHabiro
  ring

/-- At any fourth root of unity `ζ` (`ζ² = −1`), `ζ · (−ζ) = 1` and `H(ζ, −ζ, α) = 0`. -/
theorem alphaEmHabiro_zeta4_inv_and_zero (ζ α : R) (hζ : ζ ^ 2 = -1) :
    ζ * (-ζ) = 1 ∧ alphaEmHabiro ζ (-ζ) α = 0 := by
  refine ⟨?_, alphaEmHabiro_at_zeta4 ζ α⟩
  calc ζ * (-ζ) = -(ζ ^ 2) := by ring
    _ = -(-1) := by rw [hζ]
    _ = 1 := by ring

/-- **Primitive cube-root evaluation `H(ζ₃)`**: if `ζ² + ζ + 1 = 0`, then
    `ζ · (−1 − ζ) = 1` (`ζ⁻¹ = −1 − ζ`), `[2]_{ζ₃} = −1`, `h² = −3`, and
    `H(ζ, −1 − ζ, α) = −(1 + 3α)`. -/
theorem alphaEmHabiro_at_zeta3 {ζ : R} (hζ : ζ ^ 2 + ζ + 1 = 0) (α : R) :
    ζ * (-1 - ζ) = 1 ∧ alphaEmHabiro ζ (-1 - ζ) α = -(1 + 3 * α) := by
  have hinv : ζ * (-1 - ζ) = 1 := by
    calc ζ * (-1 - ζ) = 1 - (ζ ^ 2 + ζ + 1) := by ring
      _ = 1 := by rw [hζ, sub_zero]
  refine ⟨hinv, ?_⟩
  unfold alphaEmHabiro
  calc (ζ + (-1 - ζ)) * (1 - (ζ - (-1 - ζ)) ^ 2 * α)
      = -(1 + 3 * α) + 4 * α * (ζ ^ 2 + ζ + 1) := by ring
    _ = -(1 + 3 * α) := by rw [hζ, mul_zero, add_zero]

end GenericRing

section LaurentBarRing

open LaurentPolynomial

/-- Canonical Habiro element `H(q) = (q + q⁻¹)(1 − (q − q⁻¹)² α)` in the Laurent
    polynomial ring `R[q, q⁻¹]`. -/
noncomputable def habiroLaurentPoly {R : Type*} [CommRing R] (α : R) :
    LaurentPolynomial R :=
  alphaEmHabiro (T 1) (T (-1)) (C α)

/-- **Laurent bar-involution fixed-point theorem**:
    under the ring automorphism `LaurentPolynomial.invert : R[q, q⁻¹] ≃+* R[q, q⁻¹]`
    (`q^n ↦ q^{-n}`), `habiroLaurentPoly α` is fixed and `invert` is an involution. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
theorem habiroLaurentPoly_invert_fixed {R : Type*} [CommRing R] (α : R) :
    LaurentPolynomial.invert (habiroLaurentPoly α) = habiroLaurentPoly α ∧
    LaurentPolynomial.invert (LaurentPolynomial.invert (habiroLaurentPoly α)) =
      habiroLaurentPoly α := by
  have hfix : LaurentPolynomial.invert (habiroLaurentPoly α) = habiroLaurentPoly α := by
    unfold habiroLaurentPoly alphaEmHabiro
    simp only [map_mul, map_add, map_sub, map_one, map_pow, invert_T, neg_neg, invert_C]
    ring
  exact ⟨hfix, by rw [hfix, hfix]⟩

end LaurentBarRing

end QOU.BraidKnot
