/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.Algebra.Equiv
import Mathlib.LinearAlgebra.Dual.Defs
import Mathlib.RingTheory.TensorProduct.Basic

/-!
# Nakayama-twisted Frobenius pairings, ambidextrous adjunction, and the bar involution

Let `τ : A →ₗ[R] R` be a nondegenerate form on an `R`-algebra `A` with Nakayama
automorphism `ν`, i.e. `τ (a * b) = τ (b * ν a)`. This file proves, over any commutative
ring `R`:

* `tau_nu`: `τ ∘ ν = τ`;
* `frobMap` / `frobLinearMap`: `a ↦ (x ↦ τ (x * a))`, injective (`frobMap_injective`), with
  `frobMap_mul_left`: `φ (b * a) x = φ a (x * b)` and
  `frobMap_mul_nu`: `φ (a * ν b) x = φ a (b * x)`.
  Given dual bases `e, f` for `τ`, `frobDualEquiv` upgrades `frobLinearMap` to an explicit
  `R`-linear isomorphism `A ≃ₗ[R] Module.Dual R A`, identifying the twisted bimodule `₁A_ν`
  with the dual `A^∨`.
* **Twisted ambidextrous adjunction (`F3`):**
  - `twistedAmbidextrousEquiv`: for any left `A`-module `M` over `R` and any `R`-module `N`,
    an explicit `R`-linear isomorphism between `ν⁻¹`-twisted left-`A`-equivariant maps
    `M → ₍ν⁻¹₎A ⊗[R] N` (the left-module realisation of `₁A_ν ⊗[R] N`) and underlying
    `R`-linear maps `M →ₗ[R] N`, via `(τ ⊗ id_N)` and `g ↦ (m ↦ ∑ᵢ fᵢ ⊗ g(eᵢ • m))`;
  - `ambidextrousEquiv_of_refl`: the untwisted specialisation when `ν = AlgEquiv.refl`
    (`τ` symmetric), giving `Res ⊣ Ind` alongside the standard tensor-hom `Ind ⊣ Res`;
  - `twistedCenterTraceEquiv`: on `(A, A)`-bimodules, the `R`-linear isomorphism between
    `ν`-twisted bimodule invariants `{ z : A ⊗[R] N | ∀ b, b · z = z · ν b }`
    (`≃ Hom_{A-A}(A, ₁A_ν ⊗[R] N)`) and symmetric `R`-linear traces
    `{ g : A →ₗ[R] N | ∀ a b, g (a * b) = g (b * a) }` (where the twist `ν` cannot be
    dropped when `A` is non-symmetric, e.g. on Sweedler's `H₄` where `dim Z(H₄) = 1`
    while `dim Z_ν(H₄) = dim (H₄/[H₄, H₄])^∨ = 2`).
* `nu_dag`: if a semilinear anti-involution `‡` satisfies `τ (a‡) = σ (τ a)` for a ring
  automorphism `σ` of `R` (for example `q ↦ q⁻¹`), then `ν (a‡) = (ν⁻¹ a)‡`. This is a
  theorem, not an extra axiom: it follows from nondegeneracy.

A worked example of a nontrivial `ν` is Sweedler's algebra
(`QOU.LiftingDescent.Sweedler.frob_mul_eq_frob_mul_nakayama`).

No `sorry`.

## References
- [lorenz2011] Nakayama automorphism of a Frobenius algebra.
- [leitner2026] §1 Categorical foundations.
-/

namespace QOU.QuantumObservableUniverse.Nakayama

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]
variable (τ : A →ₗ[R] R) (ν : A ≃ₐ[R] A)
variable (hν : ∀ a b : A, τ (a * b) = τ (b * ν a))

include hν in
/-- The form is `ν`-invariant. -/
theorem tau_nu (a : A) : τ (ν a) = τ a := by
  have h := hν a 1
  rw [one_mul, mul_one] at h
  exact h.symm

/-- The Frobenius map `a ↦ (x ↦ τ (x * a))`. -/
def frobMap (a : A) : A → R := fun x => τ (x * a)

include hν in
/-- Right multiplication becomes the twisted left dual action. -/
theorem frobMap_mul_nu (a b x : A) : frobMap τ (a * ν b) x = frobMap τ a (b * x) := by
  simp only [frobMap]
  rw [← mul_assoc, ← hν b (x * a), mul_assoc]

/-- Left multiplication becomes the right dual action. -/
theorem frobMap_mul_left (a b x : A) : frobMap τ (b * a) x = frobMap τ a (x * b) := by
  simp only [frobMap, mul_assoc]

/-- Nondegeneracy (right radical zero) makes the Frobenius map injective. -/
theorem frobMap_injective (hnd : ∀ y : A, (∀ x, τ (x * y) = 0) → y = 0) :
    Function.Injective (frobMap τ) := by
  intro a b h
  rw [← sub_eq_zero]
  apply hnd
  intro x
  have hx := congrFun h x
  simp only [frobMap] at hx
  rw [mul_sub, map_sub, hx, sub_self]

include hν in
/-- **Bar compatibility.** If `‡` is an anti-multiplicative surjection with
`τ (a‡) = σ (τ a)`, and `τ` is nondegenerate, then `ν (a‡) = (ν⁻¹ a)‡`. -/
theorem nu_dag (σ : R →+* R) (dag : A → A) (hsurj : Function.Surjective dag)
    (hdag_mul : ∀ a b, dag (a * b) = dag b * dag a)
    (htr : ∀ a, τ (dag a) = σ (τ a))
    (hnd : ∀ y : A, (∀ x, τ (x * y) = 0) → y = 0) (a : A) :
    ν (dag a) = dag (ν.symm a) := by
  rw [← sub_eq_zero]
  apply hnd
  intro x
  obtain ⟨y, rfl⟩ := hsurj x
  rw [mul_sub, map_sub, sub_eq_zero, ← hν (dag a) (dag y), ← hdag_mul, htr, ← hdag_mul,
    htr, hν (ν.symm a) y, AlgEquiv.apply_symm_apply]

/-! ### Dual basis, Frobenius dual equivalence, and twisted ambidextrous adjunction -/

section DualBasisAndAmbidexterity

open TensorProduct

/-- `frobMap τ` packaged as an `R`-linear map `A →ₗ[R] Module.Dual R A`. -/
def frobLinearMap : A →ₗ[R] Module.Dual R A where
  toFun a :=
    { toFun := fun x => τ (x * a)
      map_add' := fun x y => by rw [add_mul, map_add]
      map_smul' := fun r x => by rw [Algebra.smul_mul_assoc, map_smul]; rfl }
  map_add' a b := by
    ext x
    change τ (x * (a + b)) = τ (x * a) + τ (x * b)
    rw [mul_add, map_add]
  map_smul' r a := by
    ext x
    change τ (x * (r • a)) = r • τ (x * a)
    rw [Algebra.mul_smul_comm, map_smul]

/-- Given finite dual bases `e, f` for `τ`, `frobLinearMap τ` upgrades to an `R`-linear
isomorphism `A ≃ₗ[R] Module.Dual R A` identifying `₁A_ν` with `A^∨`. -/
def frobDualEquiv {ι : Type*} (s : Finset ι) (e f : ι → A)
    (hdual_left : ∀ a : A, ∑ i ∈ s, τ (a * e i) • f i = a)
    (hdual_right : ∀ a : A, ∑ i ∈ s, τ (f i * a) • e i = a) :
    A ≃ₗ[R] Module.Dual R A where
  toLinearMap := frobLinearMap τ
  invFun φ := ∑ i ∈ s, φ (f i) • e i
  left_inv a := hdual_right a
  right_inv φ := by
    ext x
    change τ (x * ∑ i ∈ s, φ (f i) • e i) = φ x
    rw [Finset.mul_sum]
    simp only [Algebra.mul_smul_comm, map_sum, map_smul, smul_eq_mul]
    have hx := congrArg φ (hdual_left x)
    simp only [map_sum, map_smul, smul_eq_mul] at hx
    refine (Finset.sum_congr rfl fun i _ => mul_comm _ _).trans hx

/-- Evaluation `(τ ⊗ id_N) : A ⊗[R] N →ₗ[R] N`, `a ⊗ n ↦ τ a • n`. -/
noncomputable def tauEval {N : Type*} [AddCommGroup N] [Module R N] :
    A ⊗[R] N →ₗ[R] N :=
  TensorProduct.lift (LinearMap.mk₂ R (fun a n => τ a • n)
    (fun a₁ a₂ n => by simp [map_add, add_smul])
    (fun r a n => by simp [map_smul, mul_smul])
    (fun a n₁ n₂ => by simp [smul_add])
    (fun r a n => by dsimp only; exact smul_comm (τ a) r n))

@[simp]
theorem tauEval_tmul {N : Type*} [AddCommGroup N] [Module R N] (a : A) (n : N) :
    tauEval τ (a ⊗ₜ[R] n) = τ a • n :=
  rfl

/-- Left multiplication on the `A` factor of `A ⊗[R] N`: `y ⊗ n ↦ (b * y) ⊗ n`. -/
noncomputable def tmulLeft {N : Type*} [AddCommGroup N] [Module R N] (b : A) :
    A ⊗[R] N →ₗ[R] A ⊗[R] N :=
  TensorProduct.lift (LinearMap.mk₂ R (fun y n => (b * y) ⊗ₜ[R] n)
    (fun y₁ y₂ n => by simp [mul_add, TensorProduct.add_tmul])
    (fun r y n => by simp [Algebra.mul_smul_comm, TensorProduct.smul_tmul'])
    (fun y n₁ n₂ => by simp [TensorProduct.tmul_add])
    (fun r y n => by simp [TensorProduct.tmul_smul]))

@[simp]
theorem tmulLeft_tmul {N : Type*} [AddCommGroup N] [Module R N] (b y : A) (n : N) :
    tmulLeft b (y ⊗ₜ[R] n) = (b * y) ⊗ₜ[R] n :=
  rfl

/-- Right multiplication on the `A` factor of `A ⊗[R] N`: `y ⊗ n ↦ (y * b) ⊗ n`. -/
noncomputable def tmulRight {N : Type*} [AddCommGroup N] [Module R N] (b : A) :
    A ⊗[R] N →ₗ[R] A ⊗[R] N :=
  TensorProduct.lift (LinearMap.mk₂ R (fun y n => (y * b) ⊗ₜ[R] n)
    (fun y₁ y₂ n => by simp [add_mul, TensorProduct.add_tmul])
    (fun r y n => by simp [Algebra.smul_mul_assoc, TensorProduct.smul_tmul'])
    (fun y n₁ n₂ => by simp [TensorProduct.tmul_add])
    (fun r y n => by simp [TensorProduct.tmul_smul]))

@[simp]
theorem tmulRight_tmul {N : Type*} [AddCommGroup N] [Module R N] (b y : A) (n : N) :
    tmulRight b (y ⊗ₜ[R] n) = (y * b) ⊗ₜ[R] n :=
  rfl

/-- The `R`-submodule of maps `Φ : M →ₗ[R] A ⊗[R] N` intertwining the left `A`-action on `M`
with the `ν⁻¹`-twisted left action `y ⊗ n ↦ (ν⁻¹ a * y) ⊗ n` on `A ⊗[R] N` (the left-module
realisation of the twisted coinduced module `₁A_ν ⊗[R] N ≃ ₍ν⁻¹₎A₁ ⊗[R] N`). -/
noncomputable def TwistedIndHomSubmodule (M N : Type*)
    [AddCommGroup M] [Module R M] [Module A M] [IsScalarTower R A M]
    [AddCommGroup N] [Module R N] :
    Submodule R (M →ₗ[R] A ⊗[R] N) where
  carrier := { Φ | ∀ (a : A) (m : M), Φ (a • m) = tmulLeft (R := R) (ν.symm a) (Φ m) }
  zero_mem' a m := by simp
  add_mem' {Φ₁ Φ₂} h₁ h₂ a m := by simp [h₁ a m, h₂ a m]
  smul_mem' r {Φ} h a m := by simp [h a m]

/-- Coevaluation lift `g ↦ (m ↦ ∑ᵢ fᵢ ⊗ g(eᵢ • m))` from `M →ₗ[R] N` to `M →ₗ[R] A ⊗[R] N`. -/
noncomputable def twistedCoindLift {ι : Type*} (s : Finset ι) (e f : ι → A)
    {M N : Type*} [AddCommGroup M] [Module R M] [Module A M] [IsScalarTower R A M]
    [AddCommGroup N] [Module R N] (g : M →ₗ[R] N) :
    M →ₗ[R] A ⊗[R] N where
  toFun m := ∑ i ∈ s, f i ⊗ₜ[R] g (e i • m)
  map_add' m₁ m₂ := by
    simp only [smul_add, map_add, TensorProduct.tmul_add, Finset.sum_add_distrib]
  map_smul' r m := by
    simp only [RingHom.id_apply, Finset.smul_sum]
    refine Finset.sum_congr rfl fun i _ => ?_
    have hcomm : e i • (r • m) = r • (e i • m) := by
      rw [← IsScalarTower.algebraMap_smul A r m, ← IsScalarTower.algebraMap_smul A r (e i • m),
        ← mul_smul, ← mul_smul, Algebra.commutes]
    rw [hcomm, map_smul, TensorProduct.tmul_smul]

private theorem finset_sum_smul {ι M' : Type*} [AddCommGroup M'] [Module A M'] [DecidableEq ι]
    (s : Finset ι) (c : ι → A) (m : M') :
    (∑ i ∈ s, c i) • m = ∑ i ∈ s, c i • m := by
  induction s using Finset.induction_on with
  | empty => simp
  | insert i t hi ih => rw [Finset.sum_insert hi, Finset.sum_insert hi, add_smul, ih]

include hν in
theorem twistedCoindLift_mem {ι : Type*} (s : Finset ι) (e f : ι → A)
    (hdual_left : ∀ a : A, ∑ i ∈ s, τ (a * e i) • f i = a)
    (hdual_right : ∀ a : A, ∑ i ∈ s, τ (f i * a) • e i = a)
    {M N : Type*} [AddCommGroup M] [Module R M] [Module A M] [IsScalarTower R A M]
    [AddCommGroup N] [Module R N] (g : M →ₗ[R] N) :
    twistedCoindLift s e f g ∈ TwistedIndHomSubmodule ν M N := by
  classical
  intro a m
  change ∑ i ∈ s, f i ⊗ₜ[R] g (e i • (a • m)) =
    tmulLeft (R := R) (ν.symm a) (∑ j ∈ s, f j ⊗ₜ[R] g (e j • m))
  rw [map_sum]
  simp only [tmulLeft_tmul, ← mul_smul]
  have step1 : ∀ i ∈ s,
      f i ⊗ₜ[R] g ((e i * a) • m) =
        ∑ j ∈ s, (τ ((ν.symm a * f j) * e i) • f i) ⊗ₜ[R] g (e j • m) := by
    intro i _
    conv_lhs => rw [← hdual_right (e i * a)]
    rw [finset_sum_smul]
    simp only [IsScalarTower.smul_assoc, map_sum, map_smul, TensorProduct.tmul_sum]
    refine Finset.sum_congr rfl fun j _ => ?_
    have hτ : τ (f j * (e i * a)) = τ ((ν.symm a * f j) * e i) := by
      calc τ (f j * (e i * a))
          = τ ((f j * e i) * ν (ν.symm a)) := by rw [← mul_assoc, AlgEquiv.apply_symm_apply]
        _ = τ (ν.symm a * (f j * e i)) := (hν (ν.symm a) (f j * e i)).symm
        _ = τ ((ν.symm a * f j) * e i) := by rw [mul_assoc]
    rw [hτ, TensorProduct.smul_tmul]
  rw [Finset.sum_congr rfl step1, Finset.sum_comm]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [← TensorProduct.sum_tmul, hdual_left (ν.symm a * f j)]

include hν in
theorem sum_tmul_tauEval_tmulLeft {ι : Type*} (s : Finset ι) (e f : ι → A)
    (hdual_left : ∀ a : A, ∑ i ∈ s, τ (a * e i) • f i = a)
    {N : Type*} [AddCommGroup N] [Module R N] (z : A ⊗[R] N) :
    ∑ i ∈ s, f i ⊗ₜ[R] tauEval τ (tmulLeft (R := R) (ν.symm (e i)) z) = z := by
  induction z using TensorProduct.induction_on with
  | zero => simp
  | tmul y n =>
    simp only [tmulLeft_tmul, tauEval_tmul]
    have hτ : ∀ i, τ (ν.symm (e i) * y) = τ (y * e i) := fun i => by
      rw [hν (ν.symm (e i)) y, AlgEquiv.apply_symm_apply]
    simp only [hτ, ← TensorProduct.smul_tmul, ← TensorProduct.sum_tmul, hdual_left y]
  | add z₁ z₂ ih₁ ih₂ =>
    simp only [map_add, TensorProduct.tmul_add, Finset.sum_add_distrib, ih₁, ih₂]

/-- **Twisted ambidextrous Hom-equivalence (`F3`).** Over any commutative ring `R`, given a
form `τ : A →ₗ[R] R` with Nakayama automorphism `ν` and finite dual bases `e, f`, left
`A`-equivariant maps `M → ₍ν⁻¹₎A ⊗[R] N` are `R`-linearly isomorphic to underlying `R`-linear
maps `M →ₗ[R] N`. -/
noncomputable def twistedAmbidextrousEquiv {ι : Type*} (s : Finset ι) (e f : ι → A)
    (hdual_left : ∀ a : A, ∑ i ∈ s, τ (a * e i) • f i = a)
    (hdual_right : ∀ a : A, ∑ i ∈ s, τ (f i * a) • e i = a)
    (M N : Type*) [AddCommGroup M] [Module R M] [Module A M] [IsScalarTower R A M]
    [AddCommGroup N] [Module R N] :
    TwistedIndHomSubmodule ν M N ≃ₗ[R] (M →ₗ[R] N) where
  toFun Φ := (tauEval τ).comp Φ.1
  map_add' Φ₁ Φ₂ := by ext m; simp
  map_smul' r Φ := by ext m; simp
  invFun g := ⟨twistedCoindLift s e f g, twistedCoindLift_mem τ ν hν s e f hdual_left hdual_right g⟩
  left_inv Φ := by
    ext m
    change ∑ i ∈ s, f i ⊗ₜ[R] tauEval τ (Φ.1 (e i • m)) = Φ.1 m
    have hstep : ∀ i ∈ s,
        f i ⊗ₜ[R] tauEval τ (Φ.1 (e i • m)) =
          f i ⊗ₜ[R] tauEval τ (tmulLeft (R := R) (ν.symm (e i)) (Φ.1 m)) :=
      fun i _ => by rw [Φ.2 (e i) m]
    rw [Finset.sum_congr rfl hstep]
    exact sum_tmul_tauEval_tmulLeft τ ν hν s e f hdual_left (Φ.1 m)
  right_inv g := by
    classical
    ext m
    change tauEval τ (∑ i ∈ s, f i ⊗ₜ[R] g (e i • m)) = g m
    rw [map_sum]
    simp only [tauEval_tmul]
    have hrhs : ∑ i ∈ s, τ (f i) • g (e i • m) =
        g ((∑ i ∈ s, τ (f i * 1) • e i) • m) := by
      rw [finset_sum_smul, map_sum]
      refine Finset.sum_congr rfl fun i _ => ?_
      rw [mul_one, IsScalarTower.smul_assoc, g.map_smul]
    rw [hrhs, hdual_right 1, one_smul]

/-- **Untwisted specialisation (`ν = AlgEquiv.refl`).** When `τ` is symmetric
(`τ (a * b) = τ (b * a)`), left `A`-module maps `M → A ⊗[R] N` (with untwisted left
multiplication on `A`) are `R`-linearly isomorphic to `M →ₗ[R] N`, giving `Res ⊣ Ind`
alongside `Ind ⊣ Res`. -/
noncomputable def ambidextrousEquiv_of_refl {ι : Type*} (s : Finset ι) (e f : ι → A)
    (hsymm : ∀ a b : A, τ (a * b) = τ (b * a))
    (hdual_left : ∀ a : A, ∑ i ∈ s, τ (a * e i) • f i = a)
    (hdual_right : ∀ a : A, ∑ i ∈ s, τ (f i * a) • e i = a)
    (M N : Type*) [AddCommGroup M] [Module R M] [Module A M] [IsScalarTower R A M]
    [AddCommGroup N] [Module R N] :
    TwistedIndHomSubmodule (AlgEquiv.refl : A ≃ₐ[R] A) M N ≃ₗ[R] (M →ₗ[R] N) :=
  twistedAmbidextrousEquiv τ AlgEquiv.refl hsymm s e f hdual_left hdual_right M N

/-- The `R`-submodule of `ν`-twisted bimodule invariants in `A ⊗[R] N`:
`{ z | ∀ b, (b * ·) z = (· * ν b) z }`, isomorphic to `Hom_{A-A}(A, ₁A_ν ⊗[R] N)`. -/
noncomputable def TwistedCenterSubmodule (N : Type*) [AddCommGroup N] [Module R N] :
    Submodule R (A ⊗[R] N) where
  carrier := { z | ∀ b : A, tmulLeft (R := R) b z = tmulRight (R := R) (ν b) z }
  zero_mem' b := by simp
  add_mem' {z₁ z₂} h₁ h₂ b := by simp [h₁ b, h₂ b]
  smul_mem' r {z} h b := by simp [h b]

/-- The `R`-submodule of symmetric (`[A, A]`-vanishing) `R`-linear traces `A →ₗ[R] N`. -/
def SymmetricTraceSubmodule (N : Type*) [AddCommGroup N] [Module R N] :
    Submodule R (A →ₗ[R] N) where
  carrier := { g | ∀ a b : A, g (a * b) = g (b * a) }
  zero_mem' a b := by simp
  add_mem' {g₁ g₂} h₁ h₂ a b := by simp [h₁ a b, h₂ a b]
  smul_mem' r {g} h a b := by simp [h a b]

include hν in
theorem tauEval_tmulLeft_tmulRight_nu {N : Type*} [AddCommGroup N] [Module R N]
    (a b : A) (z : A ⊗[R] N) :
    tauEval τ (tmulLeft (R := R) a (tmulRight (R := R) (ν b) z)) =
      tauEval τ (tmulLeft (R := R) (b * a) z) := by
  induction z using TensorProduct.induction_on with
  | zero => simp
  | tmul y n =>
    simp only [tmulRight_tmul, tmulLeft_tmul, tauEval_tmul, ← mul_assoc, ← hν b (a * y)]
  | add z₁ z₂ ih₁ ih₂ =>
    simp only [map_add, ih₁, ih₂]

/-- **Twisted bimodule-trace equivalence.** `ν`-twisted bimodule invariants in `A ⊗[R] N`
(`≃ Hom_{A-A}(A, ₁A_ν ⊗[R] N)`) are `R`-linearly isomorphic to symmetric traces
`{ g : A →ₗ[R] N | ∀ a b, g (a * b) = g (b * a) }`. -/
noncomputable def twistedCenterTraceEquiv {ι : Type*} (s : Finset ι) (e f : ι → A)
    (hdual_left : ∀ a : A, ∑ i ∈ s, τ (a * e i) • f i = a)
    (hdual_right : ∀ a : A, ∑ i ∈ s, τ (f i * a) • e i = a)
    (N : Type*) [AddCommGroup N] [Module R N] :
    TwistedCenterSubmodule ν N ≃ₗ[R] SymmetricTraceSubmodule (R := R) (A := A) N where
  toFun z :=
    ⟨{ toFun := fun a => tauEval τ (tmulLeft (R := R) a z.1)
       map_add' := fun a₁ a₂ => by
         have h : ∀ w : A ⊗[R] N,
             tmulLeft (R := R) (a₁ + a₂) w =
               tmulLeft (R := R) a₁ w + tmulLeft (R := R) a₂ w := fun w => by
           induction w using TensorProduct.induction_on with
           | zero => simp
           | tmul y n => simp [add_mul, TensorProduct.add_tmul]
           | add w₁ w₂ ih₁ ih₂ => simp [ih₁, ih₂, add_add_add_comm]
         rw [h, map_add]
       map_smul' := fun r a => by
         have h : ∀ w : A ⊗[R] N,
             tmulLeft (R := R) (r • a) w = r • tmulLeft (R := R) a w := fun w => by
           induction w using TensorProduct.induction_on with
           | zero => simp
           | tmul y n => simp [Algebra.smul_mul_assoc, TensorProduct.smul_tmul']
           | add w₁ w₂ ih₁ ih₂ => simp [ih₁, ih₂, smul_add]
         rw [h, map_smul]; rfl },
     fun a b => by
       have hmul : ∀ w : A ⊗[R] N,
           tmulLeft (R := R) (a * b) w = tmulLeft (R := R) a (tmulLeft (R := R) b w) := fun w => by
         induction w using TensorProduct.induction_on with
         | zero => simp
         | tmul y n => simp [mul_assoc]
         | add w₁ w₂ ih₁ ih₂ => simp [ih₁, ih₂]
       change tauEval τ (tmulLeft (R := R) (a * b) z.1) =
         tauEval τ (tmulLeft (R := R) (b * a) z.1)
       rw [hmul, z.2 b, tauEval_tmulLeft_tmulRight_nu τ ν hν a b z.1]⟩
  map_add' z₁ z₂ := by ext a; simp
  map_smul' r z := by ext a; simp
  invFun g :=
    ⟨∑ i ∈ s, e i ⊗ₜ[R] g.1 (f i), fun b => by
      rw [map_sum, map_sum]
      simp only [tmulLeft_tmul, tmulRight_tmul]
      have lhs_eq : ∑ i ∈ s, (b * e i) ⊗ₜ[R] g.1 (f i) =
          ∑ j ∈ s, e j ⊗ₜ[R] g.1 (f j * b) := by
        have step : ∀ i ∈ s, (b * e i) ⊗ₜ[R] g.1 (f i) =
            ∑ j ∈ s, e j ⊗ₜ[R] (τ ((f j * b) * e i) • g.1 (f i)) := by
          intro i _
          conv_lhs => rw [← hdual_right (b * e i)]
          rw [TensorProduct.sum_tmul]
          refine Finset.sum_congr rfl fun j _ => ?_
          rw [← mul_assoc, TensorProduct.smul_tmul]
        rw [Finset.sum_congr rfl step, Finset.sum_comm]
        refine Finset.sum_congr rfl fun j _ => ?_
        rw [← TensorProduct.tmul_sum]
        simp only [← map_smul, ← map_sum, hdual_left (f j * b)]
      have rhs_eq : ∑ j ∈ s, (e j * ν b) ⊗ₜ[R] g.1 (f j) =
          ∑ i ∈ s, e i ⊗ₜ[R] g.1 (b * f i) := by
        have step : ∀ j ∈ s, (e j * ν b) ⊗ₜ[R] g.1 (f j) =
            ∑ i ∈ s, e i ⊗ₜ[R] (τ ((b * f i) * e j) • g.1 (f j)) := by
          intro j _
          conv_lhs => rw [← hdual_right (e j * ν b)]
          rw [TensorProduct.sum_tmul]
          refine Finset.sum_congr rfl fun i _ => ?_
          have hτ : τ (f i * (e j * ν b)) = τ ((b * f i) * e j) := by
            calc τ (f i * (e j * ν b))
                = τ ((f i * e j) * ν b) := by rw [← mul_assoc]
              _ = τ (b * (f i * e j)) := (hν b (f i * e j)).symm
              _ = τ ((b * f i) * e j) := by rw [mul_assoc]
          rw [hτ, TensorProduct.smul_tmul]
        rw [Finset.sum_congr rfl step, Finset.sum_comm]
        refine Finset.sum_congr rfl fun i _ => ?_
        rw [← TensorProduct.tmul_sum]
        simp only [← map_smul, ← map_sum, hdual_left (b * f i)]
      rw [lhs_eq, rhs_eq]
      refine Finset.sum_congr rfl fun i _ => ?_
      rw [g.2 (f i) b]⟩
  left_inv z := by
    ext : 1
    change ∑ i ∈ s, e i ⊗ₜ[R] tauEval τ (tmulLeft (R := R) (f i) z.1) = z.1
    generalize z.1 = w
    induction w using TensorProduct.induction_on with
    | zero => simp
    | tmul y n =>
      simp only [tmulLeft_tmul, tauEval_tmul, ← TensorProduct.smul_tmul, ← TensorProduct.sum_tmul,
        hdual_right y]
    | add w₁ w₂ ih₁ ih₂ =>
      simp only [map_add, TensorProduct.tmul_add, Finset.sum_add_distrib, ih₁, ih₂]
  right_inv g := by
    ext a
    change tauEval τ (tmulLeft (R := R) a (∑ i ∈ s, e i ⊗ₜ[R] g.1 (f i))) = g.1 a
    rw [map_sum, map_sum]
    simp only [tmulLeft_tmul, tauEval_tmul, ← map_smul, ← map_sum, hdual_left a]

end DualBasisAndAmbidexterity

end QOU.QuantumObservableUniverse.Nakayama
