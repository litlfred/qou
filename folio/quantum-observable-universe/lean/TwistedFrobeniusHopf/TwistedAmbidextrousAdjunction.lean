import Mathlib.LinearAlgebra.TensorProduct.Associator
import Mathlib.RingTheory.TensorProduct.Basic
import Mathlib.LinearAlgebra.TensorProduct.Finiteness
import Mathlib.Algebra.Algebra.Bilinear
import Mathlib.Algebra.DualNumber
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Matrix.Basis
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FinCases

/-!
# Nakayama-Twisted Frobenius Comultiplication and Ambidextrous Adjunction

Over an arbitrary commutative base ring `R` (§7c generic base-ring discipline, no `ℝ`),
this module develops the dual-basis formalism for a (not necessarily symmetric) Frobenius
`R`-algebra `A` with linear trace `τ : A →ₗ[R] R` and Nakayama automorphism
`ν : A ≃ₐ[R] A` satisfying `τ(a * b) = τ(b * ν(a))`.

## Main declarations and results

1. `TwistedFrobeniusDualBasis` — dual basis `(eᵢ, fᵢ)_{i ∈ ι}` satisfying
   `∑ᵢ τ(a * fᵢ) • eᵢ = a` and `∑ᵢ τ(eᵢ * a) • fᵢ = a`, together with concrete
   inhabited instances on `R` (`selfDualBasis`) and on `2 × 2` matrices with twisted
   diagonal trace (`twistedMatrix2DualBasis`), including a proof that `ν ≠ id` when
   the diagonal weights differ (`twistedMatrix2_nu_ne_id`).
2. `deltaFrob` — the Frobenius comultiplication `Δ_Frob(a) = ∑ᵢ (a * eᵢ) ⊗ fᵢ`, with
   exact snake/counit equations `(id ⊗ τ)(Δ_Frob(a)) = a` (`counit_right_deltaFrob`)
   and `(τ ⊗ id)(Δ_Frob(a)) = ν(a)` (`counit_left_deltaFrob`).
3. `twisted_casimir_eq` & `deltaFrob_right_mul_twisted` — the `ν`-twisted Casimir
   identity `∑ᵢ eᵢ ⊗ (fᵢ * ν(a)) = ∑ᵢ (a * eᵢ) ⊗ fᵢ` and the resulting `(A, A_ν)`
   Frobenius bimodule law `Δ_Frob(a * b) = Δ_Frob(a) * (1 ⊗ ν(b))`.
4. `dualNumber_deltaFrob_one_ne_one` & `dualNumber_deltaFrob_not_multiplicative` —
   explicit finite Frobenius separation witness on `DualNumber R = R[ε]/(ε²)` proving
   `Δ_Frob(1) = 1 ⊗ ε + ε ⊗ 1 ≠ 1 ⊗ 1` and `Δ_Frob(1 * 1) ≠ Δ_Frob(1) * Δ_Frob(1)`
   over every nontrivial commutative ring `R`, refuting conflation of `Δ_Frob` with a
   multiplicative Hopf coproduct `Δ_Hopf`.
5. `twistedAmbidextrousEquiv` — explicit `R`-linear Hom-equivalence
   `(N →ₗ[R] M) ≃ₗ[R] NuRightLinearHom F M N act` between `R`-linear maps `N →ₗ[R] M`
   and right-`A`-linear maps `N → M ⊗[R] A_ν` (`Res_A ⊣ Coind_A ≃ Ind_{A_ν}`), built
   from `Δ_Frob(1)` as coevaluation and `τ` as evaluation, together with the regular
   bimodule specialization (`N = A`) and untwisted corollary when `ν = AlgEquiv.refl`.

References: Tadashi Nakayama (1939, 1941), Joachim Kock (2004) §2.2–2.3, Lars Kadison (1999).
-- Ref: [nakayama1939]
-/

namespace QOU.AlgebraicSubstrate

open TensorProduct BigOperators

/-! ## 1. Nakayama-Twisted Frobenius Dual-Basis Structure -/

/-- Dual-basis data for a Frobenius `R`-algebra `A` with trace `τ` and Nakayama
automorphism `ν` satisfying `τ(a * b) = τ(b * ν a)`. The dual pair `(e, f)` satisfies
the reconstruction laws `∑ᵢ τ(a * fᵢ) • eᵢ = a` and `∑ᵢ τ(eᵢ * a) • fᵢ = a`. -/
structure TwistedFrobeniusDualBasis (R : Type*) [CommRing R] (A : Type*) [Ring A]
    [Algebra R A] (ι : Type*) [Fintype ι] where
  /-- The Frobenius trace form `τ : A →ₗ[R] R`. -/
  τ : A →ₗ[R] R
  /-- The Nakayama `R`-algebra automorphism `ν : A ≃ₐ[R] A`. -/
  ν : A ≃ₐ[R] A
  /-- Left dual-basis family `e : ι → A`. -/
  e : ι → A
  /-- Right dual-basis family `f : ι → A`. -/
  f : ι → A
  /-- Twisted cyclicity: `τ(a * b) = τ(b * ν a)`. -/
  hν : ∀ a b : A, τ (a * b) = τ (b * ν a)
  /-- Left reconstruction: `∑ᵢ τ(a * fᵢ) • eᵢ = a`. -/
  dual_left : ∀ a : A, ∑ i, τ (a * f i) • e i = a
  /-- Right reconstruction: `∑ᵢ τ(eᵢ * a) • fᵢ = a`. -/
  dual_right : ∀ a : A, ∑ i, τ (e i * a) • f i = a

section ConcreteInstances

variable (R : Type*) [CommRing R]

/-- Concrete witness on the base ring `A = R` with `τ = id`, `ν = refl`, and 1-element
dual basis `e () = 1, f () = 1`. -/
def selfDualBasis : TwistedFrobeniusDualBasis R R Unit where
  τ := LinearMap.id
  ν := AlgEquiv.refl
  e _ := 1
  f _ := 1
  hν a b := by simp [mul_comm]
  dual_left a := by simp
  dual_right a := by simp

/-- Inner conjugation `X ↦ D X D⁻¹` on `2 × 2` matrices for diagonal units `d : Fin 2 → Rˣ`. -/
def diagConjAlgEquiv (d : Fin 2 → Rˣ) :
    Matrix (Fin 2) (Fin 2) R ≃ₐ[R] Matrix (Fin 2) (Fin 2) R where
  toFun X := Matrix.of fun p q => (d p : R) * X p q * (((d q)⁻¹ : Rˣ) : R)
  invFun X := Matrix.of fun p q => (((d p)⁻¹ : Rˣ) : R) * X p q * (d q : R)
  left_inv X := by
    ext p q
    simp only [Matrix.of_apply]
    calc
      (((d p)⁻¹ : Rˣ) : R) * ((d p : R) * X p q * (((d q)⁻¹ : Rˣ) : R)) * (d q : R)
          = ((((d p)⁻¹ : Rˣ) : R) * (d p : R)) * X p q *
              ((((d q)⁻¹ : Rˣ) : R) * (d q : R)) := by ring
      _ = 1 * X p q * 1 := by rw [Units.inv_mul, Units.inv_mul]
      _ = X p q := by ring
  right_inv X := by
    ext p q
    simp only [Matrix.of_apply]
    calc
      (d p : R) * ((((d p)⁻¹ : Rˣ) : R) * X p q * (d q : R)) * (((d q)⁻¹ : Rˣ) : R)
          = ((d p : R) * (((d p)⁻¹ : Rˣ) : R)) * X p q *
              ((d q : R) * (((d q)⁻¹ : Rˣ) : R)) := by ring
      _ = 1 * X p q * 1 := by rw [Units.mul_inv, Units.mul_inv]
      _ = X p q := by ring
  map_mul' X Y := by
    ext p q
    simp only [Matrix.of_apply, Matrix.mul_apply, Fin.sum_univ_two]
    have h0 : ((d 0 : R) * (((d 0)⁻¹ : Rˣ) : R)) = 1 := Units.mul_inv (d 0)
    have h1 : ((d 1 : R) * (((d 1)⁻¹ : Rˣ) : R)) = 1 := Units.mul_inv (d 1)
    linear_combination
      (d p : R) * X p 0 * Y 0 q * (((d q)⁻¹ : Rˣ) : R) * h0.symm +
      (d p : R) * X p 1 * Y 1 q * (((d q)⁻¹ : Rˣ) : R) * h1.symm
  map_add' X Y := by
    ext p q
    simp only [Matrix.of_apply, Matrix.add_apply]
    ring
  commutes' r := by
    ext p q
    simp only [Matrix.of_apply, Algebra.algebraMap_eq_smul_one, Matrix.smul_apply,
      Matrix.one_apply, smul_eq_mul]
    by_cases hpq : p = q
    · subst hpq
      simp only [↓reduceIte]
      calc
        (d p : R) * (r * 1) * (((d p)⁻¹ : Rˣ) : R)
            = r * ((d p : R) * (((d p)⁻¹ : Rˣ) : R)) := by ring
        _ = r * 1 := by rw [Units.mul_inv]
    · simp [hpq]

/-- Weighted trace `τ_d(X) = d₀ X₀₀ + d₁ X₁₁` on `2 × 2` matrices. -/
def weightedMatrix2Trace (d : Fin 2 → Rˣ) : Matrix (Fin 2) (Fin 2) R →ₗ[R] R where
  toFun X := ∑ p : Fin 2, (d p : R) * X p p
  map_add' X Y := by
    simp only [Matrix.add_apply, Fin.sum_univ_two]
    ring
  map_smul' r X := by
    simp only [Matrix.smul_apply, smul_eq_mul, RingHom.id_apply, Fin.sum_univ_two]
    ring

/-- Concrete non-commutative, Nakayama-twisted Frobenius dual-basis witness on
`Matrix (Fin 2) (Fin 2) R` with `τ(X) = d₀ X₀₀ + d₁ X₁₁`, `ν(X) = D X D⁻¹`,
`e_{(p,q)} = E_{p,q}`, and `f_{(p,q)} = d_p⁻¹ E_{q,p}`. -/
def twistedMatrix2DualBasis (d : Fin 2 → Rˣ) :
    TwistedFrobeniusDualBasis R (Matrix (Fin 2) (Fin 2) R) (Fin 2 × Fin 2) where
  τ := weightedMatrix2Trace R d
  ν := diagConjAlgEquiv R d
  e pq := Matrix.single pq.1 pq.2 1
  f pq := (((d pq.1)⁻¹ : Rˣ) : R) • Matrix.single pq.2 pq.1 1
  hν X Y := by
    simp only [weightedMatrix2Trace, diagConjAlgEquiv, LinearMap.coe_mk, AddHom.coe_mk,
      AlgEquiv.coe_mk, Equiv.coe_fn_mk, Matrix.mul_apply, Matrix.of_apply, Fin.sum_univ_two]
    have h0 : ((d 0 : R) * (((d 0)⁻¹ : Rˣ) : R)) = 1 := Units.mul_inv (d 0)
    have h1 : ((d 1 : R) * (((d 1)⁻¹ : Rˣ) : R)) = 1 := Units.mul_inv (d 1)
    linear_combination
      (X 0 1 * Y 1 0) * (d 0 : R) * h1.symm +
      (X 1 0 * Y 0 1) * (d 1 : R) * h0.symm +
      (X 0 0 * Y 0 0) * (d 0 : R) * h0.symm +
      (X 1 1 * Y 1 1) * (d 1 : R) * h1.symm
  dual_left X := by
    ext r s
    simp only [Fintype.sum_prod_type, weightedMatrix2Trace, LinearMap.coe_mk, AddHom.coe_mk,
      Matrix.sum_apply, Matrix.smul_apply, Matrix.mul_apply, Matrix.single, Matrix.of_apply,
      smul_eq_mul, Fin.sum_univ_two]
    have h0 : ((d 0 : R) * (((d 0)⁻¹ : Rˣ) : R)) = 1 := Units.mul_inv (d 0)
    have h1 : ((d 1 : R) * (((d 1)⁻¹ : Rˣ) : R)) = 1 := Units.mul_inv (d 1)
    fin_cases r <;> fin_cases s <;> simp <;>
      first
      | linear_combination X 0 0 * h0
      | linear_combination X 0 1 * h0
      | linear_combination X 1 0 * h1
      | linear_combination X 1 1 * h1
  dual_right X := by
    ext r s
    simp only [Fintype.sum_prod_type, weightedMatrix2Trace, LinearMap.coe_mk, AddHom.coe_mk,
      Matrix.sum_apply, Matrix.smul_apply, Matrix.mul_apply, Matrix.single, Matrix.of_apply,
      smul_eq_mul, Fin.sum_univ_two]
    have h0 : ((d 0 : R) * (((d 0)⁻¹ : Rˣ) : R)) = 1 := Units.mul_inv (d 0)
    have h1 : ((d 1 : R) * (((d 1)⁻¹ : Rˣ) : R)) = 1 := Units.mul_inv (d 1)
    fin_cases r <;> fin_cases s <;> simp <;>
      first
      | linear_combination X 0 0 * h0
      | linear_combination X 0 1 * h1
      | linear_combination X 1 0 * h0
      | linear_combination X 1 1 * h1

/-- When the diagonal weights `d 0` and `d 1` are distinct, the Nakayama automorphism of
`twistedMatrix2DualBasis` is genuinely non-trivial (`ν(E₀₁) ≠ E₀₁`). -/
theorem twistedMatrix2_nu_ne_id {d : Fin 2 → Rˣ} (hd : (d 0 : R) ≠ (d 1 : R)) :
    (twistedMatrix2DualBasis R d).ν (Matrix.single 0 1 1) ≠ Matrix.single 0 1 1 := by
  intro h
  have h01 := congr_fun (congr_fun h 0) 1
  simp only [twistedMatrix2DualBasis, diagConjAlgEquiv, AlgEquiv.coe_mk, Equiv.coe_fn_mk,
    Matrix.of_apply, Matrix.single, and_self, ↓reduceIte, mul_one] at h01
  apply hd
  calc
    (d 0 : R) = ((d 0 : R) * (((d 1)⁻¹ : Rˣ) : R)) * (d 1 : R) := by
      rw [mul_assoc, Units.inv_mul, mul_one]
    _ = 1 * (d 1 : R) := by rw [h01]
    _ = (d 1 : R) := one_mul _

end ConcreteInstances

/-! ## 2. Frobenius Comultiplication, Snake Laws, and `ν`-Twisted Casimir Identity -/

namespace TwistedFrobeniusDualBasis

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable {ι : Type*} [Fintype ι] (F : TwistedFrobeniusDualBasis R A ι)

/-- Left counit identity on the dual basis: `∑ᵢ τ(fᵢ) • eᵢ = 1`. -/
theorem sum_tau_f_smul_e : ∑ i, F.τ (F.f i) • F.e i = (1 : A) := by
  simpa only [one_mul] using F.dual_left 1

/-- Right counit identity on the dual basis: `∑ᵢ τ(eᵢ) • fᵢ = 1`. -/
theorem sum_tau_e_smul_f : ∑ i, F.τ (F.e i) • F.f i = (1 : A) := by
  simpa only [mul_one] using F.dual_right 1

/-- Inverse Nakayama cyclicity: `τ(ν⁻¹(a) * b) = τ(b * a)`. -/
theorem tau_symm_mul (a b : A) : F.τ (F.ν.symm a * b) = F.τ (b * a) := by
  rw [F.hν, AlgEquiv.apply_symm_apply]

/-- The **Frobenius comultiplication** `Δ_Frob : A →ₗ[R] A ⊗[R] A` defined by
`Δ_Frob(a) = ∑ᵢ (a * eᵢ) ⊗ₜ fᵢ`. -/
noncomputable def deltaFrob : A →ₗ[R] A ⊗[R] A where
  toFun a := ∑ i, (a * F.e i) ⊗ₜ[R] F.f i
  map_add' a b := by
    simp only [add_mul, TensorProduct.add_tmul, Finset.sum_add_distrib]
  map_smul' r a := by
    simp only [Algebra.smul_mul_assoc, TensorProduct.smul_tmul', RingHom.id_apply,
      Finset.smul_sum]

theorem deltaFrob_apply (a : A) : F.deltaFrob a = ∑ i, (a * F.e i) ⊗ₜ[R] F.f i := rfl

theorem deltaFrob_one : F.deltaFrob 1 = ∑ i, F.e i ⊗ₜ[R] F.f i := by
  simp [deltaFrob_apply]

/-- **Right counit / snake equation:** `(id_A ⊗ τ)(Δ_Frob(a)) = a`. -/
theorem counit_right_deltaFrob (a : A) :
    TensorProduct.rid R A ((LinearMap.lTensor A F.τ) (F.deltaFrob a)) = a := by
  rw [deltaFrob_apply, map_sum, map_sum]
  simp only [LinearMap.lTensor_tmul, TensorProduct.rid_tmul]
  calc
    ∑ i, F.τ (F.f i) • (a * F.e i)
        = ∑ i, a * (F.τ (F.f i) • F.e i) := by
          refine Finset.sum_congr rfl fun i _ => ?_
          rw [Algebra.mul_smul_comm]
    _ = a * ∑ i, F.τ (F.f i) • F.e i := by rw [Finset.mul_sum]
    _ = a * 1 := by rw [F.sum_tau_f_smul_e]
    _ = a := mul_one a

/-- **Left counit / Nakayama-twisted snake equation:** `(τ ⊗ id_A)(Δ_Frob(a)) = ν(a)`. -/
theorem counit_left_deltaFrob (a : A) :
    TensorProduct.lid R A ((LinearMap.rTensor A F.τ) (F.deltaFrob a)) = F.ν a := by
  rw [deltaFrob_apply, map_sum, map_sum]
  simp only [LinearMap.rTensor_tmul, TensorProduct.lid_tmul]
  calc
    ∑ i, F.τ (a * F.e i) • F.f i
        = ∑ i, F.τ (F.e i * F.ν a) • F.f i := by
          refine Finset.sum_congr rfl fun i _ => ?_
          rw [F.hν a (F.e i)]
    _ = F.ν a := F.dual_right (F.ν a)

/-- At `a = 1`, both counit contractions of the Casimir element `Δ_Frob(1)` equal `1`. -/
theorem counit_left_deltaFrob_one :
    TensorProduct.lid R A ((LinearMap.rTensor A F.τ) (F.deltaFrob 1)) = 1 := by
  rw [F.counit_left_deltaFrob, map_one]

/-- When `ν = AlgEquiv.refl` (symmetric Frobenius algebra), the left counit is untwisted:
`(τ ⊗ id_A)(Δ_Frob(a)) = a`. -/
theorem counit_left_deltaFrob_of_refl (hrefl : F.ν = AlgEquiv.refl) (a : A) :
    TensorProduct.lid R A ((LinearMap.rTensor A F.τ) (F.deltaFrob a)) = a := by
  rw [F.counit_left_deltaFrob, hrefl]
  rfl

/-- **Left Frobenius `A`-linearity:** `Δ_Frob(a * b) = (a ⊗ 1) * Δ_Frob(b)`. -/
theorem deltaFrob_left_mul (a b : A) :
    F.deltaFrob (a * b) = (a ⊗ₜ[R] (1 : A)) * F.deltaFrob b := by
  rw [deltaFrob_apply, deltaFrob_apply, Finset.mul_sum]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Algebra.TensorProduct.tmul_mul_tmul, mul_assoc, one_mul]

/-- **`ν`-Twisted Casimir Law:** `∑ᵢ eᵢ ⊗ (fᵢ * ν a) = ∑ᵢ (a * eᵢ) ⊗ fᵢ`.

The Frobenius Casimir element `γ = ∑ᵢ eᵢ ⊗ fᵢ` intertwines left multiplication by `a` on
the first tensor factor with right multiplication by `ν(a)` on the second tensor factor. -/
theorem twisted_casimir_eq (a : A) :
    ∑ i, F.e i ⊗ₜ[R] (F.f i * F.ν a) = ∑ i, (a * F.e i) ⊗ₜ[R] F.f i := by
  calc
    ∑ i, F.e i ⊗ₜ[R] (F.f i * F.ν a)
        = ∑ i, F.e i ⊗ₜ[R] (∑ j, F.τ (F.e j * (F.f i * F.ν a)) • F.f j) := by
          refine Finset.sum_congr rfl fun i _ => ?_
          rw [F.dual_right (F.f i * F.ν a)]
    _ = ∑ i, ∑ j, F.τ (F.e j * (F.f i * F.ν a)) • (F.e i ⊗ₜ[R] F.f j) := by
          refine Finset.sum_congr rfl fun i _ => ?_
          rw [TensorProduct.tmul_sum]
          refine Finset.sum_congr rfl fun j _ => ?_
          rw [TensorProduct.tmul_smul]
    _ = ∑ j, ∑ i, F.τ (F.e j * (F.f i * F.ν a)) • (F.e i ⊗ₜ[R] F.f j) := Finset.sum_comm
    _ = ∑ j, (∑ i, F.τ ((a * F.e j) * F.f i) • F.e i) ⊗ₜ[R] F.f j := by
          refine Finset.sum_congr rfl fun j _ => ?_
          rw [TensorProduct.sum_tmul]
          refine Finset.sum_congr rfl fun i _ => ?_
          have hcyc : F.τ (F.e j * (F.f i * F.ν a)) = F.τ ((a * F.e j) * F.f i) := by
            rw [← mul_assoc, ← F.hν a (F.e j * F.f i), mul_assoc]
          rw [hcyc, TensorProduct.smul_tmul']
    _ = ∑ j, (a * F.e j) ⊗ₜ[R] F.f j := by
          refine Finset.sum_congr rfl fun j _ => ?_
          rw [F.dual_left (a * F.e j)]

/-- Alternative form of `deltaFrob` via the `ν`-twisted Casimir identity:
`Δ_Frob(a) = ∑ᵢ eᵢ ⊗ (fᵢ * ν a)`. -/
theorem deltaFrob_eq_sum_tmul_mul_nu (a : A) :
    F.deltaFrob a = ∑ i, F.e i ⊗ₜ[R] (F.f i * F.ν a) :=
  (F.twisted_casimir_eq a).symm

/-- **`ν`-Twisted Right Frobenius Bimodule Law:** `Δ_Frob(a * b) = Δ_Frob(a) * (1 ⊗ ν b)`. -/
theorem deltaFrob_right_mul_twisted (a b : A) :
    F.deltaFrob (a * b) = F.deltaFrob a * ((1 : A) ⊗ₜ[R] F.ν b) := by
  calc
    F.deltaFrob (a * b)
        = (a ⊗ₜ[R] (1 : A)) * F.deltaFrob b := F.deltaFrob_left_mul a b
    _ = (a ⊗ₜ[R] (1 : A)) * ∑ i, F.e i ⊗ₜ[R] (F.f i * F.ν b) := by
          rw [F.deltaFrob_eq_sum_tmul_mul_nu b]
    _ = ∑ i, (a * F.e i) ⊗ₜ[R] (F.f i * F.ν b) := by
          rw [Finset.mul_sum]
          refine Finset.sum_congr rfl fun i _ => ?_
          rw [Algebra.TensorProduct.tmul_mul_tmul, one_mul]
    _ = (∑ i, (a * F.e i) ⊗ₜ[R] F.f i) * ((1 : A) ⊗ₜ[R] F.ν b) := by
          rw [Finset.sum_mul]
          refine Finset.sum_congr rfl fun i _ => ?_
          rw [Algebra.TensorProduct.tmul_mul_tmul, mul_one]

/-! ## 3. Twisted Ambidextrous Hom-Equivalence (`Res_A ⊣ Coind_A ≃ Ind_{A_ν}`) -/

section AmbidextrousAdjunction

variable (M : Type*) [AddCommGroup M] [Module R M]
variable (N : Type*) [AddCommGroup N] [Module R N]

/-- Right `A`-action on `M ⊗[R] A` twisted by `ν`: `(m ⊗ x) ◁_ν a := m ⊗ (x * ν a)`. -/
noncomputable def rMulNu (a : A) : (M ⊗[R] A) →ₗ[R] (M ⊗[R] A) :=
  LinearMap.lTensor M (LinearMap.mulRight R (F.ν a))

@[simp]
theorem rMulNu_tmul (a : A) (m : M) (x : A) :
    F.rMulNu M a (m ⊗ₜ[R] x) = m ⊗ₜ[R] (x * F.ν a) := rfl

/-- The `R`-submodule of `ν`-twisted right-`A`-linear maps `N → M ⊗[R] A_ν` for a right
`A`-action `act : N →ₗ[R] A →ₗ[R] N`. -/
noncomputable def NuRightLinearHom (act : N →ₗ[R] A →ₗ[R] N) :
    Submodule R (N →ₗ[R] M ⊗[R] A) where
  carrier := { g | ∀ (n : N) (a : A), g (act n a) = F.rMulNu M a (g n) }
  add_mem' {g₁ g₂} hg₁ hg₂ n a := by
    simp only [LinearMap.add_apply, map_add, hg₁ n a, hg₂ n a]
  zero_mem' n a := by simp
  smul_mem' r {g} hg n a := by
    simp only [LinearMap.smul_apply, map_smul, hg n a]

/-- Coevaluation-induced lift `Φ(φ)(n) = ((φ ∘ act n) ⊗ id_A)(Δ_Frob 1) = ∑ᵢ φ(n ◁ eᵢ) ⊗ fᵢ`. -/
noncomputable def ambidextrousToTensor (act : N →ₗ[R] A →ₗ[R] N) (φ : N →ₗ[R] M) :
    N →ₗ[R] M ⊗[R] A where
  toFun n := LinearMap.rTensor A (φ.comp (act n)) (F.deltaFrob 1)
  map_add' n₁ n₂ := by
    rw [F.deltaFrob_one]
    simp only [map_add, map_sum, LinearMap.rTensor_tmul, LinearMap.comp_apply,
      LinearMap.add_apply, TensorProduct.add_tmul, Finset.sum_add_distrib]
  map_smul' r n := by
    rw [F.deltaFrob_one]
    simp only [map_smul, map_sum, LinearMap.rTensor_tmul, LinearMap.comp_apply,
      LinearMap.smul_apply, TensorProduct.smul_tmul', RingHom.id_apply, Finset.smul_sum]

theorem ambidextrousToTensor_apply (act : N →ₗ[R] A →ₗ[R] N) (φ : N →ₗ[R] M) (n : N) :
    F.ambidextrousToTensor M N act φ n = ∑ i, φ (act n (F.e i)) ⊗ₜ[R] F.f i := by
  simp [ambidextrousToTensor, F.deltaFrob_one, map_sum]

/-- `ambidextrousToTensor` lands in `NuRightLinearHom` whenever `act` is associative:
this is a direct consequence of the `ν`-twisted Casimir law `twisted_casimir_eq`. -/
theorem ambidextrousToTensor_mem_nuRightLinearHom (act : N →ₗ[R] A →ₗ[R] N)
    (h_mul : ∀ (n : N) (a b : A), act (act n a) b = act n (a * b))
    (φ : N →ₗ[R] M) :
    F.ambidextrousToTensor M N act φ ∈ F.NuRightLinearHom M N act := by
  intro n a
  calc
    F.ambidextrousToTensor M N act φ (act n a)
        = ∑ i, φ (act (act n a) (F.e i)) ⊗ₜ[R] F.f i :=
          F.ambidextrousToTensor_apply M N act φ (act n a)
    _ = ∑ i, φ (act n (a * F.e i)) ⊗ₜ[R] F.f i := by
          refine Finset.sum_congr rfl fun i _ => ?_
          rw [h_mul n a (F.e i)]
    _ = LinearMap.rTensor A (φ.comp (act n)) (∑ i, (a * F.e i) ⊗ₜ[R] F.f i) := by
          simp [map_sum]
    _ = LinearMap.rTensor A (φ.comp (act n)) (∑ i, F.e i ⊗ₜ[R] (F.f i * F.ν a)) := by
          rw [← F.twisted_casimir_eq a]
    _ = ∑ i, φ (act n (F.e i)) ⊗ₜ[R] (F.f i * F.ν a) := by
          simp [map_sum]
    _ = F.rMulNu M a (F.ambidextrousToTensor M N act φ n) := by
          rw [F.ambidextrousToTensor_apply, map_sum]
          rfl

/-- Evaluation contraction `Ψ(g)(n) = (id_M ⊗ τ)(g n)` using the Frobenius form `τ`. -/
noncomputable def ambidextrousFromTensor (g : N →ₗ[R] M ⊗[R] A) : N →ₗ[R] M :=
  (TensorProduct.rid R M).toLinearMap.comp ((LinearMap.lTensor M F.τ).comp g)

theorem ambidextrousFromTensor_apply (g : N →ₗ[R] M ⊗[R] A) (n : N) :
    F.ambidextrousFromTensor M N g n =
      TensorProduct.rid R M (LinearMap.lTensor M F.τ (g n)) := rfl

/-- Left inverse law `Ψ(Φ(φ)) = φ` from unitality `act n 1 = n` and `∑ᵢ τ(fᵢ) • eᵢ = 1`. -/
theorem ambidextrousFrom_to (act : N →ₗ[R] A →ₗ[R] N) (h_one : ∀ n : N, act n 1 = n)
    (φ : N →ₗ[R] M) :
    F.ambidextrousFromTensor M N (F.ambidextrousToTensor M N act φ) = φ := by
  ext n
  rw [F.ambidextrousFromTensor_apply, F.ambidextrousToTensor_apply, map_sum, map_sum]
  simp only [LinearMap.lTensor_tmul, TensorProduct.rid_tmul]
  calc
    ∑ i, F.τ (F.f i) • φ (act n (F.e i))
        = φ (act n (∑ i, F.τ (F.f i) • F.e i)) := by
          rw [map_sum, map_sum]
          refine Finset.sum_congr rfl fun i _ => ?_
          rw [map_smul, map_smul]
    _ = φ (act n 1) := by rw [F.sum_tau_f_smul_e]
    _ = φ n := by rw [h_one n]

/-- Tensor reconstruction helper: for every `t : M ⊗[R] A`,
`∑ᵢ ((id_M ⊗ τ)(t ◁_ν eᵢ)) ⊗ fᵢ = t`, using both `hν` and `dual_right`. -/
theorem sum_contract_rMulNu_tmul_f (t : M ⊗[R] A) :
    ∑ i, (TensorProduct.rid R M (LinearMap.lTensor M F.τ (F.rMulNu M (F.e i) t))) ⊗ₜ[R] F.f i =
      t := by
  induction t using TensorProduct.induction_on with
  | zero => simp
  | tmul m x =>
    simp only [rMulNu_tmul, LinearMap.lTensor_tmul, TensorProduct.rid_tmul]
    calc
      ∑ i, (F.τ (x * F.ν (F.e i)) • m) ⊗ₜ[R] F.f i
          = m ⊗ₜ[R] (∑ i, F.τ (F.e i * x) • F.f i) := by
            rw [TensorProduct.tmul_sum]
            refine Finset.sum_congr rfl fun i _ => ?_
            rw [← F.hν (F.e i) x, TensorProduct.smul_tmul, TensorProduct.tmul_smul]
      _ = m ⊗ₜ[R] x := by rw [F.dual_right x]
  | add t₁ t₂ ht₁ ht₂ =>
    simp only [map_add, TensorProduct.add_tmul, Finset.sum_add_distrib, ht₁, ht₂]

/-- Right inverse law `Φ(Ψ(g)) = g` for every `ν`-twisted right-`A`-linear map `g`. -/
theorem ambidextrousTo_from (act : N →ₗ[R] A →ₗ[R] N)
    {g : N →ₗ[R] M ⊗[R] A} (hg : g ∈ F.NuRightLinearHom M N act) :
    F.ambidextrousToTensor M N act (F.ambidextrousFromTensor M N g) = g := by
  ext n
  rw [F.ambidextrousToTensor_apply]
  calc
    ∑ i, F.ambidextrousFromTensor M N g (act n (F.e i)) ⊗ₜ[R] F.f i
        = ∑ i, (TensorProduct.rid R M
            (LinearMap.lTensor M F.τ (F.rMulNu M (F.e i) (g n)))) ⊗ₜ[R] F.f i := by
          refine Finset.sum_congr rfl fun i _ => ?_
          rw [F.ambidextrousFromTensor_apply, hg n (F.e i)]
    _ = g n := F.sum_contract_rMulNu_tmul_f M (g n)

/-- **Twisted Ambidextrous Hom-Equivalence (`Res_A ⊣ Coind_A ≃ Ind_{A_ν}`).**

For any right `A`-module `(N, act)` and `R`-module `M`, `R`-linear maps `N →ₗ[R] M` are
`R`-linearly isomorphic to `ν`-twisted right-`A`-linear maps `N → M ⊗[R] A_ν`, with
coevaluation `Δ_Frob(1) = ∑ᵢ eᵢ ⊗ fᵢ` and evaluation `τ`. -/
noncomputable def twistedAmbidextrousEquiv (act : N →ₗ[R] A →ₗ[R] N)
    (h_one : ∀ n : N, act n 1 = n)
    (h_mul : ∀ (n : N) (a b : A), act (act n a) b = act n (a * b)) :
    (N →ₗ[R] M) ≃ₗ[R] F.NuRightLinearHom M N act where
  toFun φ := ⟨F.ambidextrousToTensor M N act φ,
    F.ambidextrousToTensor_mem_nuRightLinearHom M N act h_mul φ⟩
  map_add' φ₁ φ₂ := by
    ext n
    simp [ambidextrousToTensor_apply, TensorProduct.add_tmul, Finset.sum_add_distrib]
  map_smul' r φ := by
    ext n
    simp [ambidextrousToTensor_apply, TensorProduct.smul_tmul', Finset.smul_sum]
  invFun g := F.ambidextrousFromTensor M N g.1
  left_inv φ := F.ambidextrousFrom_to M N act h_one φ
  right_inv g := Subtype.ext (F.ambidextrousTo_from M N act g.2)

/-- Regular bimodule specialization (`N = A` with right multiplication `LinearMap.mul R A`):
`(A →ₗ[R] M) ≃ₗ[R] NuRightLinearHom F M A (LinearMap.mul R A)`. -/
noncomputable def regularTwistedAmbidextrousEquiv :
    (A →ₗ[R] M) ≃ₗ[R] F.NuRightLinearHom M A (LinearMap.mul R A) :=
  F.twistedAmbidextrousEquiv M A (LinearMap.mul R A)
    (fun a => mul_one a)
    (fun a b c => mul_assoc a b c)

/-- Untwisted corollary when `ν = AlgEquiv.refl` (symmetric Frobenius algebra):
every `g ∈ NuRightLinearHom` satisfies ordinary untwisted right `A`-linearity
`g (act n a) = (id_M ⊗ (· * a))(g n)`. -/
theorem untwisted_right_linear_of_refl (hrefl : F.ν = AlgEquiv.refl)
    (act : N →ₗ[R] A →ₗ[R] N) {g : N →ₗ[R] M ⊗[R] A}
    (hg : g ∈ F.NuRightLinearHom M N act) (n : N) (a : A) :
    g (act n a) = LinearMap.lTensor M (LinearMap.mulRight R a) (g n) := by
  rw [hg n a, rMulNu, hrefl]
  rfl

end AmbidextrousAdjunction

end TwistedFrobeniusDualBasis

/-! ## 4. Non-Bialgebra Separation Witness (`R[ε]/(ε²)`: `Δ_Frob` is NOT Multiplicative) -/

section DualNumberSeparation

variable (R : Type*) [CommRing R]

/-- The square-zero generator `ε = inr 1` of `DualNumber R = R[ε]/(ε²)`. -/
def dualEps : DualNumber R :=
  TrivSqZeroExt.inr 1

theorem dualEps_mul_dualEps : dualEps R * dualEps R = 0 := by
  simp [dualEps]

/-- Frobenius dual-basis structure on the truncated polynomial algebra
`DualNumber R = R[ε]/(ε²)` with trace `τ(a + b ε) = b`, `ν = refl`, and dual basis
`(e₀, e₁) = (1, ε)`, `(f₀, f₁) = (ε, 1)`. -/
def dualNumberFrobenius : TwistedFrobeniusDualBasis R (DualNumber R) (Fin 2) where
  τ := TrivSqZeroExt.sndHom R R
  ν := AlgEquiv.refl
  e i := if i = 0 then 1 else dualEps R
  f i := if i = 0 then dualEps R else 1
  hν x y := by
    change (x * y).snd = (y * x).snd
    simp only [TrivSqZeroExt.snd_mul, smul_eq_mul]
    change x.fst * y.snd + x.snd * y.fst = y.fst * x.snd + y.snd * x.fst
    ring
  dual_left x := by
    ext <;> simp [Fin.sum_univ_two, dualEps, TrivSqZeroExt.snd_mul, smul_eq_mul, mul_comm]
  dual_right x := by
    ext <;> simp [Fin.sum_univ_two, dualEps, TrivSqZeroExt.snd_mul, smul_eq_mul]

/-- In `DualNumber R`, the Frobenius Casimir / comultiplication of `1` is
`Δ_Frob(1) = 1 ⊗ ε + ε ⊗ 1`. -/
theorem dualNumber_deltaFrob_one_eq :
    (dualNumberFrobenius R).deltaFrob 1 =
      (1 : DualNumber R) ⊗ₜ[R] dualEps R + dualEps R ⊗ₜ[R] (1 : DualNumber R) := by
  rw [TwistedFrobeniusDualBasis.deltaFrob_one, Fin.sum_univ_two]
  simp [dualNumberFrobenius]

/-- Augmentation product functional `(a₁ + b₁ ε) ⊗ (a₂ + b₂ ε) ↦ a₁ * a₂` on
`DualNumber R ⊗[R] DualNumber R`. -/
noncomputable def dualNumberFstMulFst :
    (DualNumber R ⊗[R] DualNumber R) →ₗ[R] R :=
  TensorProduct.lift
    (LinearMap.mk₂ R (fun u v : DualNumber R => u.fst * v.fst)
      (fun u₁ u₂ v => by simp [add_mul])
      (fun r u v => by simp [smul_eq_mul, mul_assoc])
      (fun u v₁ v₂ => by simp [mul_add])
      (fun r u v => by simp [smul_eq_mul, mul_left_comm]))

/-- Mixed functional `(a₁ + b₁ ε) ⊗ (a₂ + b₂ ε) ↦ a₁ * b₂` on
`DualNumber R ⊗[R] DualNumber R`. -/
noncomputable def dualNumberFstMulSnd :
    (DualNumber R ⊗[R] DualNumber R) →ₗ[R] R :=
  TensorProduct.lift
    (LinearMap.mk₂ R (fun u v : DualNumber R => u.fst * v.snd)
      (fun u₁ u₂ v => by simp [add_mul])
      (fun r u v => by simp [smul_eq_mul, mul_assoc])
      (fun u v₁ v₂ => by simp [mul_add])
      (fun r u v => by simp [smul_eq_mul, mul_left_comm]))

/-- **Non-unitality of `Δ_Frob`:** over any nontrivial commutative ring `R`,
`Δ_Frob(1) ≠ 1` in `DualNumber R ⊗[R] DualNumber R` (whereas any bialgebra coproduct
satisfies `Δ_Hopf(1) = 1 ⊗ 1`). -/
theorem dualNumber_deltaFrob_one_ne_one [Nontrivial R] :
    (dualNumberFrobenius R).deltaFrob 1 ≠ (1 : DualNumber R ⊗[R] DualNumber R) := by
  intro h
  have hval := congr_arg (dualNumberFstMulFst R) h
  rw [dualNumber_deltaFrob_one_eq, Algebra.TensorProduct.one_def] at hval
  simp [dualNumberFstMulFst, dualEps] at hval

/-- **Non-multiplicativity of `Δ_Frob` (`Δ_Frob ≠ Δ_Hopf`):** over any nontrivial
commutative ring `R` (regardless of characteristic),
`Δ_Frob(1 * 1) ≠ Δ_Frob(1) * Δ_Frob(1)`. -/
theorem dualNumber_deltaFrob_not_multiplicative [Nontrivial R] :
    (dualNumberFrobenius R).deltaFrob (1 * 1) ≠
      (dualNumberFrobenius R).deltaFrob 1 * (dualNumberFrobenius R).deltaFrob 1 := by
  intro h
  have hval := congr_arg (dualNumberFstMulSnd R) h
  have hsq : dualEps R * dualEps R = 0 := dualEps_mul_dualEps R
  rw [mul_one, dualNumber_deltaFrob_one_eq] at hval
  simp only [add_mul, mul_add, Algebra.TensorProduct.tmul_mul_tmul, mul_one, one_mul, hsq,
    TensorProduct.tmul_zero, TensorProduct.zero_tmul, zero_add, add_zero] at hval
  simp [dualNumberFstMulSnd, dualEps] at hval

end DualNumberSeparation

end QOU.AlgebraicSubstrate
