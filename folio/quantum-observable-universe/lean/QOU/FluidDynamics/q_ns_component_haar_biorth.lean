import QOU.FluidDynamics.q_ns_component_lap_quadrants
import QOU.FluidDynamics.q_ns_haar_field_invariance_full

/-!
# QOU.FluidDynamics.q_ns_component_haar_biorth — Haar biorthogonality of dual components

Thread "Audit the q-Bessel special-function dictionary" (2026-11-27), Peter–Weyl step 3,
bean `qou-kdh5`.
-/

namespace QOU.FluidDynamics.ComponentLap

open QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2 QOU.FluidDynamics.HaarFieldInvariance
  QOU.FluidDynamics.HaarCoproductInvariance QOU.FluidDynamics.HaarFieldInvarianceFull

section Commutator

variable {R : Type*} [CommRing R] (q : Rˣ)

local notation "qi" => (((q⁻¹ : Rˣ) : R))
local notation "tw" => torusScaleAlgHom q q⁻¹ q⁻¹⁻¹

/-- `X₊ ∘ R = q² R ∘ X₊` for the twist `R`. -/
theorem fieldPlus_tw (x : OqSU2 R q) :
    fieldPlus q (tw x) = ((q : R) * q) • tw (fieldPlus q x) := by
  have h := torus_fieldPlus q q⁻¹ q⁻¹⁻¹ x
  simp only [inv_inv] at h ⊢
  rw [h, smul_smul, show (q : R) * q * (qi * qi) = 1 by
    linear_combination ((q : R) * qi + 1) * q_mul_qi q, one_smul]

/-- `X₋ ∘ R = q⁻² R ∘ X₋` for the twist `R`. -/
theorem fieldMinus_tw (x : OqSU2 R q) :
    fieldMinus q (tw x) = (qi * qi) • tw (fieldMinus q x) := by
  have h := torus_fieldMinus q q⁻¹ q⁻¹⁻¹ x
  simp only [inv_inv] at h ⊢
  rw [h, smul_smul, show qi * qi * ((q : R) * q) = 1 by
    linear_combination (qi * (q : R) + 1) * qi_mul_q q, one_smul]

theorem fieldPlus_mul' (f g : OqSU2 R q) :
    fieldPlus q (f * g) = fieldPlus q f * tw g + f * fieldPlus q g := field_leibniz q 0 1 0 f g

theorem fieldMinus_mul' (f g : OqSU2 R q) :
    fieldMinus q (f * g) = fieldMinus q f * tw g + f * fieldMinus q g := field_leibniz q 0 0 1 f g

/-- The `q`-commutator `S = X₊X₋ − q² X₋X₊`. -/
noncomputable def lapS : OqSU2 R q →ₗ[R] OqSU2 R q :=
  lap q - ((q : R) * q) • (fieldMinus q ∘ₗ fieldPlus q)

theorem lapS_apply (x : OqSU2 R q) :
    lapS q x = lap q x - ((q : R) * q) • fieldMinus q (fieldPlus q x) := rfl

/-- **`S` is a twisted derivation with twist `R²`.** `S(fg) = S f · R²g + f · S g`. -/
theorem lapS_mul (f g : OqSU2 R q) :
    lapS q (f * g) = lapS q f * tw (tw g) + f * lapS q g := by
  have hq : (q : R) * q * (qi * qi) = 1 := by
    linear_combination ((q : R) * qi + 1) * q_mul_qi q
  simp only [lapS_apply, lap_apply, fieldPlus_mul', fieldMinus_mul', map_add, fieldPlus_tw, fieldMinus_tw,
    mul_smul_comm, smul_mul_assoc, smul_add, smul_smul, sub_mul, mul_sub]
  linear_combination (norm := module) -hq • (fieldPlus q f * tw (fieldMinus q g))

end Commutator

end QOU.FluidDynamics.ComponentLap
