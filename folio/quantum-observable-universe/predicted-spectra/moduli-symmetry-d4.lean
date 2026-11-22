import Mathlib.Data.Real.Basic
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp


/-!
# QOU.Archimedean.moduli_symmetry_d4 — Dihedral D₄-action on ℂ×

The two natural involutions σ : q ↦ iq (complex rotation by π/2)
and τ : q ↦ q⁻¹ (Hecke bar involution) generate a faithful action
of the dihedral group D₄ of order 8 on ℂ×.

This file proves the dihedral relations σ⁴ = id, τ² = id (on ℂ×),
and (στ)² = id, which together yield the D₄ presentation.

LaTeX label: `prop:moduli-symmetry-d4`

## References

- [leitner2026] §6/moduli-symmetry-d4
- [leitner2026] §6/golden-quartet-galois
- [leitner2026] §5/baryon-integration-limit
-/

namespace QOU.Archimedean.ModuliSymmetryD4

open Complex

/-- The complex rotation σ : q ↦ iq. -/
noncomputable def sigma (q : ℂ) : ℂ := I * q

/-- The bar involution τ : q ↦ q⁻¹. -/
noncomputable def tau (q : ℂ) : ℂ := q⁻¹

/-- σ has order dividing 4: σ⁴(q) = q for every q. -/
-- Ref: [leitner2026] §6/moduli-symmetry-d4
theorem sigma_pow_four (q : ℂ) : sigma (sigma (sigma (sigma q))) = q := by
  unfold sigma
  have hII : I * I = -1 := Complex.I_mul_I
  calc I * (I * (I * (I * q)))
      = (I * I) * (I * I) * q := by ring
    _ = (-1) * (-1) * q := by rw [hII]
    _ = q := by ring

/-- τ has order dividing 2: τ²(q) = q for nonzero q. -/
-- Ref: [leitner2026] §6/moduli-symmetry-d4
theorem tau_pow_two (q : ℂ) (_ : q ≠ 0) : tau (tau q) = q := by
  unfold tau
  exact inv_inv q

/-- σ maps nonzero to nonzero. -/
-- Ref: [leitner2026] §6/moduli-symmetry-d4
theorem sigma_ne_zero (q : ℂ) (hq : q ≠ 0) : sigma q ≠ 0 := by
  unfold sigma
  exact mul_ne_zero Complex.I_ne_zero hq

/-- τ maps nonzero to nonzero. -/
-- Ref: [leitner2026] §6/moduli-symmetry-d4
theorem tau_ne_zero (q : ℂ) (hq : q ≠ 0) : tau q ≠ 0 := by
  unfold tau
  exact inv_ne_zero hq

/-- σ⁻¹(q) = -i · q (since I⁻¹ = -I). -/
-- Ref: [leitner2026] §6/moduli-symmetry-d4
theorem I_inv : I⁻¹ = -I := by
  have h : I * (-I) = 1 := by
    have h2 : I * I = -1 := Complex.I_mul_I
    rw [mul_neg, h2, neg_neg]
  exact (eq_inv_of_mul_eq_one_right h).symm

/-- The composition (σ ∘ τ) is its own inverse: (στ)²(q) = q for nonzero q.
    This is the dihedral commutation, equivalent to τστ = σ⁻¹. -/
-- Ref: [leitner2026] §6/moduli-symmetry-d4
theorem sigma_tau_involution (q : ℂ) (hq : q ≠ 0) :
    sigma (tau (sigma (tau q))) = q := by
  unfold sigma tau
  -- Compute step by step. τ(q) = q⁻¹. σ(q⁻¹) = I · q⁻¹.
  -- τ(I · q⁻¹) = (I · q⁻¹)⁻¹ = I⁻¹ · q = (-I) · q.
  -- σ((-I) · q) = I · (-I) · q = -I² · q = -(-1) · q = q. ✓
  have hI : (I : ℂ) ≠ 0 := Complex.I_ne_zero
  have hqi : q⁻¹ ≠ 0 := inv_ne_zero hq
  have h1 : (I * q⁻¹)⁻¹ = I⁻¹ * q := by
    rw [mul_inv, inv_inv]
  have h2 : I⁻¹ = -I := I_inv
  have h3 : I * I = -1 := Complex.I_mul_I
  calc I * (I * q⁻¹)⁻¹
      = I * (I⁻¹ * q) := by rw [h1]
    _ = (I * I⁻¹) * q := by ring
    _ = 1 * q := by rw [mul_inv_cancel₀ hI]
    _ = q := one_mul q

/-- **Dihedral D₄-action on ℂ×** (Proposition):

    σ : q ↦ iq has order dividing 4 (σ⁴ = id), τ : q ↦ q⁻¹ has order
    dividing 2 (τ² = id on ℂ×), and they satisfy the dihedral
    commutation (στ)² = id.

    Together with σ ≠ id (σ has actual order 4 since I⁴ = 1 and
    I, I², I³ are distinct from 1), τ ≠ id (since q ≠ q⁻¹ for, e.g.,
    q = 2), and σ ≠ τ, this presents D₄ of order 8 acting on ℂ×. -/
-- Ref: [leitner2026] §6/moduli-symmetry-d4
theorem moduli_symmetry_d4 :
    (∀ q : ℂ, sigma (sigma (sigma (sigma q))) = q) ∧
    (∀ q : ℂ, q ≠ 0 → tau (tau q) = q) ∧
    (∀ q : ℂ, q ≠ 0 → sigma (tau (sigma (tau q))) = q) :=
  ⟨sigma_pow_four,
   tau_pow_two,
   sigma_tau_involution⟩

end QOU.Archimedean.ModuliSymmetryD4
