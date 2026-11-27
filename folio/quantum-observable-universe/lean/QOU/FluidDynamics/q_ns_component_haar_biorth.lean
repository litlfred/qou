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


/-! ### `S` on generators, products and powers -/

theorem lapS_alpha : lapS q (α q) = α (R := R) q := by
  rw [lapS_apply, lap_apply, (fieldMinus_generators q).1, (fieldPlus_generators q).2.1,
    (fieldPlus_generators q).1, map_zero, smul_zero, sub_zero]

theorem lapS_gamma : lapS q (γ q) = γ (R := R) q := by
  rw [lapS_apply, lap_apply, (fieldMinus_generators q).2.2.1, (fieldPlus_generators q).2.2.2,
    (fieldPlus_generators q).2.2.1, map_zero, smul_zero, sub_zero]

theorem lapS_beta : lapS q (β q) = (-((q : R) * q)) • β (R := R) q := by
  rw [lapS_apply, lap_apply, (fieldMinus_generators q).2.1, map_zero,
    (fieldPlus_generators q).2.1, (fieldMinus_generators q).1, zero_sub]
  module

theorem lapS_delta : lapS q (δ q) = (-((q : R) * q)) • δ (R := R) q := by
  rw [lapS_apply, lap_apply, (fieldMinus_generators q).2.2.2, map_zero,
    (fieldPlus_generators q).2.2.2, (fieldMinus_generators q).2.2.1, zero_sub]
  module

/-- `S(uv) = (s e + t) uv` when `S u = s u`, `S v = t v` and `R² v = e v`. -/
theorem lapS_mul_eigen {u v : OqSU2 R q} {s t e : R} (hu : lapS q u = s • u)
    (hv : lapS q v = t • v) (he : tw (tw v) = e • v) :
    lapS q (u * v) = (s * e + t) • (u * v) := by
  rw [lapS_mul, hu, hv, he, smul_mul_smul_comm, mul_smul_comm]
  module

/-- `S(u^n) = s [n]_e u^n` when `S u = s u` and `R² u = e u`. -/
theorem lapS_pow_eigen {u : OqSU2 R q} {s e : R} (hu : lapS q u = s • u)
    (he : tw (tw u) = e • u) (n : ℕ) :
    lapS q (u ^ n) = (s * jk e n) • u ^ n := by
  induction n with
  | zero =>
    have h := lapS_mul q (1 : OqSU2 R q) 1
    simp only [mul_one, map_one] at h
    rw [pow_zero, jk_zero, mul_zero, zero_smul]
    simpa using h
  | succ n ih =>
    rw [pow_succ, lapS_mul_eigen q ih hu he, jk_succ', ← pow_succ]
    congr 1; ring

theorem tw_tw_pow {u : OqSU2 R q} {e : R} (he : tw (tw u) = e • u) (n : ℕ) :
    tw (tw (u ^ n)) = e ^ n • u ^ n := by
  rw [map_pow, map_pow, he, smul_pow]

theorem tw_tw_alpha : tw (tw (α q)) = (qi * qi) • α (R := R) q := by
  rw [(field_twist_generators q).1, map_smul, (field_twist_generators q).1, smul_smul]

theorem tw_tw_beta : tw (tw (β q)) = ((q : R) * q) • β (R := R) q := by
  rw [(field_twist_generators q).2.1, map_smul, (field_twist_generators q).2.1, smul_smul]

theorem tw_tw_gamma : tw (tw (γ q)) = (qi * qi) • γ (R := R) q := by
  rw [(field_twist_generators q).2.2.1, map_smul, (field_twist_generators q).2.2.1, smul_smul]

theorem tw_tw_delta : tw (tw (δ q)) = ((q : R) * q) • δ (R := R) q := by
  rw [(field_twist_generators q).2.2.2, map_smul, (field_twist_generators q).2.2.2, smul_smul]

/-- `S ζ = 0`. -/
theorem lapS_zeta : lapS q (zetaB (R := R) q) = 0 := by
  rw [zetaB, lapS_mul_eigen q (lapS_beta q) (t := 1) (by rw [lapS_gamma, one_smul]) (tw_tw_gamma q),
    show -((q : R) * q) * (qi * qi) + 1 = 0 by
      linear_combination (-((q : R) * qi) - 1) * q_mul_qi q, zero_smul]

theorem lapS_zeta_pow (k : ℕ) : lapS q (zetaB (R := R) q ^ k) = 0 := by
  rw [lapS_pow_eigen q (s := 0) (e := 1) (by rw [lapS_zeta, zero_smul])
    (by rw [tw_zeta, tw_zeta, one_smul]) k, zero_mul, zero_smul]

end Commutator

end QOU.FluidDynamics.ComponentLap
