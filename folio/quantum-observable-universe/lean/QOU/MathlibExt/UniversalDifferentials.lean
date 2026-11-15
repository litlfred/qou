/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import Mathlib.RingTheory.Kaehler.Basic

/-!
# The universal first-order differential calculus `Ω¹(A) = ker(μ : A ⊗ A → A)`

The paper defines (`\label{def:kahler-differentials}`) the Kähler differentials of an
algebra `A` as `Ω¹(A) = ker(μ : A ⊗ A → A)` with `d a = 1 ⊗ a − a ⊗ 1`. That is the
**universal** first-order calculus, and it makes sense for a **noncommutative** `A`
(Hecke-type algebras included). Mathlib's `KaehlerDifferential R S` does not: it needs `S`
commutative and it is the quotient `I / I²` of the same kernel `I`.

This file supplies the noncommutative object and ties it to Mathlib's in the commutative
case. Everything is algebraic; no analysis is used.

## Main results

* `Ω1 R A` — the `R`-submodule `ker (LinearMap.mul' R A)` of `A ⊗[R] A`.
* `d R A : A →ₗ[R] Ω1 R A` — `a ↦ 1 ⊗ a − a ⊗ 1`.
* `lsmul`, `rsmul` — the left and right `A`-actions on `Ω1 R A`; `rsmul_lsmul_comm`.
* `d_mul` — the Leibniz rule `d (a b) = a · d b + (d a) · b`.
* `sum_smul_d` — every element of `Ω1 R A` is `Σ xᵢ · d yᵢ`; precisely, the map
  `x ⊗ y ↦ x · d y` sends `z` to `z − μ(z) ⊗ 1`, so it is the identity on `Ω1 R A`.
* `lift`, `lift_d`, `lift_unique` — the universal property: a Leibniz map `D : A → M` into an
  `A`-bimodule factors as `lift D ∘ d` through a unique left-`A`-linear map; `lift_lsmul`,
  `lift_rsmul` show that map is a map of `A`-bimodules.
* `Ω1_eq_kaehler_ideal` — for commutative `A`, `Ω1 R A` is exactly Mathlib's
  `KaehlerDifferential.ideal R A`, and `D_eq_toCotangent_d` identifies Mathlib's `D` with the
  class of our `d` in `I / I²`.

## Note on the old stub

`QOU.Glossary.KahlerDifferentials` was a three-field structure with no axioms, generated
by a script that no longer exists, and had no consumers. This file is its replacement.
-/

open TensorProduct

namespace QOU.MathlibExt.UniversalDifferentials

variable (R : Type*) [CommRing R] (A : Type*) [Ring A] [Algebra R A]

/-- `Ω¹(A) = ker(μ : A ⊗[R] A → A)`, the universal first-order differential calculus. -/
abbrev Ω1 : Submodule R (A ⊗[R] A) := LinearMap.ker (LinearMap.mul' R A)

theorem mem_Ω1 {z : A ⊗[R] A} : z ∈ Ω1 R A ↔ LinearMap.mul' R A z = 0 := LinearMap.mem_ker

/-- The universal derivation `d a = 1 ⊗ a − a ⊗ 1`. -/
def d : A →ₗ[R] Ω1 R A where
  toFun a := ⟨1 ⊗ₜ a - a ⊗ₜ 1, by simp⟩
  map_add' a b := by ext; simp [tmul_add, add_tmul]; abel
  map_smul' r a := by ext; simp [smul_sub, smul_tmul']

@[simp] theorem d_coe (a : A) : (d R A a : A ⊗[R] A) = 1 ⊗ₜ a - a ⊗ₜ 1 := rfl

@[simp] theorem d_one : d R A 1 = 0 := by ext; simp

variable {R A}

/-- Left multiplication on the first factor, `x ⊗ y ↦ a x ⊗ y`. -/
def lmulT (a : A) : A ⊗[R] A →ₗ[R] A ⊗[R] A := TensorProduct.map (LinearMap.mulLeft R a) LinearMap.id

/-- Right multiplication on the second factor, `x ⊗ y ↦ x ⊗ y b`. -/
def rmulT (b : A) : A ⊗[R] A →ₗ[R] A ⊗[R] A := TensorProduct.map LinearMap.id (LinearMap.mulRight R b)

@[simp] theorem lmulT_tmul (a x y : A) : lmulT (R := R) a (x ⊗ₜ y) = (a * x) ⊗ₜ y := rfl
@[simp] theorem rmulT_tmul (b x y : A) : rmulT (R := R) b (x ⊗ₜ y) = x ⊗ₜ (y * b) := rfl

theorem mul'_lmulT (a : A) (z : A ⊗[R] A) :
    LinearMap.mul' R A (lmulT a z) = a * LinearMap.mul' R A z := by
  induction z using TensorProduct.induction_on with
  | zero => simp
  | tmul x y => simp [mul_assoc]
  | add x y hx hy => simp_all [mul_add]

theorem mul'_rmulT (b : A) (z : A ⊗[R] A) :
    LinearMap.mul' R A (rmulT b z) = LinearMap.mul' R A z * b := by
  induction z using TensorProduct.induction_on with
  | zero => simp
  | tmul x y => simp [mul_assoc]
  | add x y hx hy => simp_all [add_mul]

/-- The left `A`-action on `Ω¹(A)`. -/
def lsmul (a : A) : Ω1 R A →ₗ[R] Ω1 R A :=
  (lmulT a).restrict fun z hz => by
    rw [mem_Ω1] at hz ⊢; rw [mul'_lmulT, hz, mul_zero]

/-- The right `A`-action on `Ω¹(A)`. -/
def rsmul (b : A) : Ω1 R A →ₗ[R] Ω1 R A :=
  (rmulT b).restrict fun z hz => by
    rw [mem_Ω1] at hz ⊢; rw [mul'_rmulT, hz, zero_mul]

@[simp] theorem lsmul_coe (a : A) (ω : Ω1 R A) :
    (lsmul a ω : A ⊗[R] A) = lmulT a ω := rfl

@[simp] theorem rsmul_coe (b : A) (ω : Ω1 R A) :
    (rsmul b ω : A ⊗[R] A) = rmulT b ω := rfl

/-- The two actions commute, so `Ω¹(A)` is an `A`-bimodule. -/
theorem rsmul_lsmul_comm (a b : A) (ω : Ω1 R A) :
    rsmul b (lsmul a ω) = lsmul a (rsmul b ω) := by
  ext1
  simp only [rsmul_coe, lsmul_coe]
  induction (ω : A ⊗[R] A) using TensorProduct.induction_on with
  | zero => simp
  | tmul x y => simp
  | add x y hx hy => simp_all

theorem lsmul_mul (a a' : A) (ω : Ω1 R A) : lsmul (a * a') ω = lsmul a (lsmul a' ω) := by
  ext1
  simp only [lsmul_coe]
  induction (ω : A ⊗[R] A) using TensorProduct.induction_on with
  | zero => simp
  | tmul x y => simp [mul_assoc]
  | add x y hx hy => simp_all

theorem rsmul_mul (b b' : A) (ω : Ω1 R A) : rsmul (b * b') ω = rsmul b' (rsmul b ω) := by
  ext1
  simp only [rsmul_coe]
  induction (ω : A ⊗[R] A) using TensorProduct.induction_on with
  | zero => simp
  | tmul x y => simp [mul_assoc]
  | add x y hx hy => simp_all

/-- **Leibniz rule** for the universal derivation: `d (a b) = a · d b + (d a) · b`. -/
theorem d_mul (a b : A) : d R A (a * b) = lsmul a (d R A b) + rsmul b (d R A a) := by
  ext1
  simp

/-- The `R`-linear map `A ⊗ A → Ω¹(A)`, `x ⊗ y ↦ x · d y`. -/
def gen : A ⊗[R] A →ₗ[R] Ω1 R A :=
  TensorProduct.lift
    { toFun := fun x => lsmul x ∘ₗ d R A
      map_add' := fun x y => by ext; simp [lmulT, add_mul, add_tmul]; abel
      map_smul' := fun r x => by ext; simp [lmulT, smul_tmul', smul_sub] }

@[simp] theorem gen_tmul (x y : A) : gen (R := R) (x ⊗ₜ y) = lsmul x (d R A y) := rfl

/-- **Generation by `d`.** `gen z = z − μ(z) ⊗ 1` in `A ⊗ A`. -/
theorem gen_coe (z : A ⊗[R] A) :
    (gen z : A ⊗[R] A) = z - (LinearMap.mul' R A z) ⊗ₜ 1 := by
  induction z using TensorProduct.induction_on with
  | zero => simp
  | tmul x y => simp
  | add x y hx hy => simp only [map_add, Submodule.coe_add, hx, hy, add_tmul]; abel

/-- Every element of `Ω¹(A)` is `Σ xᵢ · d yᵢ`: `gen` is a retraction onto `Ω¹(A)`. -/
theorem gen_of_mem (ω : Ω1 R A) : gen (ω : A ⊗[R] A) = ω := by
  ext1
  rw [gen_coe, (mem_Ω1 R A).1 ω.2, zero_tmul, sub_zero]

variable (R A) in
/-- The **unit section** `A → A ⊗ A`, `a ↦ a ⊗ 1`.  It is a right inverse
    of `μ`, and its range is the complement of `Ω¹(A)` below. -/
def unitSection : A →ₗ[R] A ⊗[R] A := (TensorProduct.mk R A A).flip 1

@[simp] theorem unitSection_apply (a : A) : unitSection R A a = a ⊗ₜ 1 := rfl

theorem mul'_unitSection (a : A) : LinearMap.mul' R A (unitSection R A a) = a := by
  simp

/-- `a ⊗ 1` is a one-form only when `a = 0`. -/
theorem tmul_one_mem_Ω1_iff (a : A) : a ⊗ₜ[R] (1 : A) ∈ Ω1 R A ↔ a = 0 := by
  rw [mem_Ω1]; simp

variable (R A) in
/-- **`A ⊗ A = Ω¹(A) ⊕ (A ⊗ 1)`.**  The kernel of `μ` and the range of the
    unit section are complementary submodules: every `z` splits uniquely as
    `(z − μ(z) ⊗ 1) + μ(z) ⊗ 1`.  Equivalently `μ` restricts to an
    isomorphism `A ⊗ 1 ≅ A`, so the part of `A ⊗ A` that `μ` sees is
    exactly the part `Ω¹(A)` misses. -/
theorem isCompl_Ω1_range_unitSection :
    IsCompl (Ω1 R A) (LinearMap.range (unitSection R A)) := by
  constructor
  · rw [Submodule.disjoint_def]
    rintro z hz ⟨a, rfl⟩
    rw [unitSection_apply, tmul_one_mem_Ω1_iff] at hz
    simp [hz]
  · rw [codisjoint_iff, eq_top_iff]
    intro z _
    have h : z = (gen z : A ⊗[R] A) + unitSection R A (LinearMap.mul' R A z) := by
      rw [gen_coe, unitSection_apply, sub_add_cancel]
    rw [h]
    exact Submodule.add_mem_sup (gen z).2 ⟨_, rfl⟩

/-! ## Universal property -/

section Universal

variable {M : Type*} [AddCommGroup M] [Module R M] [Module A M] [Module Aᵐᵒᵖ M]
  [IsScalarTower R A M]

omit [IsScalarTower R A M] in
/-- A Leibniz map vanishes on `1`. -/
theorem map_one_of_leibniz (D : A →ₗ[R] M)
    (hD : ∀ a b, D (a * b) = a • D b + MulOpposite.op b • D a) : D 1 = 0 := by
  have h := hD 1 1
  rw [mul_one, one_smul, MulOpposite.op_one, one_smul] at h
  simpa using h

/-- The induced map `Ω¹(A) → M`, `Σ xᵢ ⊗ yᵢ ↦ Σ xᵢ • D yᵢ`. -/
def liftT (D : A →ₗ[R] M) : A ⊗[R] A →ₗ[R] M :=
  TensorProduct.lift
    { toFun := fun x => DistribMulAction.toLinearMap R M x ∘ₗ D
      map_add' := fun x y => by ext; simp [add_smul]
      map_smul' := fun r x => by ext; simp [smul_assoc] }

omit [Module Aᵐᵒᵖ M] in
@[simp] theorem liftT_tmul (D : A →ₗ[R] M) (x y : A) : liftT D (x ⊗ₜ y) = x • D y := rfl

/-- The induced map on `Ω¹(A)`. -/
def lift (D : A →ₗ[R] M) : Ω1 R A →ₗ[R] M := liftT D ∘ₗ (Ω1 R A).subtype

/-- `lift D ∘ d = D`. -/
theorem lift_d (D : A →ₗ[R] M)
    (hD : ∀ a b, D (a * b) = a • D b + MulOpposite.op b • D a) (a : A) :
    lift D (d R A a) = D a := by
  simp [lift, map_one_of_leibniz D hD]

omit [Module Aᵐᵒᵖ M] in
theorem liftT_lmulT (D : A →ₗ[R] M) (a : A) (z : A ⊗[R] A) :
    liftT D (lmulT a z) = a • liftT D z := by
  induction z using TensorProduct.induction_on with
  | zero => simp
  | tmul x y => simp [mul_smul]
  | add x y hx hy => simp_all [smul_add]

omit [Module Aᵐᵒᵖ M] in
/-- `lift D` is left `A`-linear. -/
theorem lift_lsmul (D : A →ₗ[R] M) (a : A) (ω : Ω1 R A) :
    lift D (lsmul a ω) = a • lift D ω := liftT_lmulT D a ω

/-- How `liftT D` sees the right action, on all of `A ⊗ A`:
`liftT D (z · b) = μ(z) • D b + b • liftT D z`. -/
theorem liftT_rmulT [SMulCommClass A Aᵐᵒᵖ M] (D : A →ₗ[R] M)
    (hD : ∀ a b, D (a * b) = a • D b + MulOpposite.op b • D a) (b : A) (z : A ⊗[R] A) :
    liftT D (rmulT b z) = LinearMap.mul' R A z • D b + MulOpposite.op b • liftT D z := by
  induction z using TensorProduct.induction_on with
  | zero => simp
  | tmul x y => simp [hD, smul_add, mul_smul, smul_comm x (MulOpposite.op b)]
  | add x y hx hy => simp only [map_add, hx, hy, add_smul, smul_add]; abel

/-- `lift D` is right `A`-linear too, so it is a map of `A`-bimodules. -/
theorem lift_rsmul [SMulCommClass A Aᵐᵒᵖ M] (D : A →ₗ[R] M)
    (hD : ∀ a b, D (a * b) = a • D b + MulOpposite.op b • D a) (b : A) (ω : Ω1 R A) :
    lift D (rsmul b ω) = MulOpposite.op b • lift D ω := by
  simp only [lift, LinearMap.comp_apply, Submodule.subtype_apply, rsmul_coe]
  rw [liftT_rmulT D hD, (mem_Ω1 R A).1 ω.2, zero_smul, zero_add]

omit [Module Aᵐᵒᵖ M] in
/-- **Uniqueness.** A left-`A`-linear `φ : Ω¹(A) → M` with `φ ∘ d = D` is `lift D`. -/
theorem lift_unique (D : A →ₗ[R] M) (φ : Ω1 R A →ₗ[R] M)
    (hφ : ∀ a ω, φ (lsmul a ω) = a • φ ω) (hφd : ∀ a, φ (d R A a) = D a) :
    φ = lift D := by
  have key : ∀ z : A ⊗[R] A, φ (gen z) = liftT D z := by
    intro z
    induction z using TensorProduct.induction_on with
    | zero => simp
    | tmul x y => simp [hφ, hφd]
    | add x y hx hy => simp_all
  ext ω
  rw [← gen_of_mem ω, key]
  simp [lift, gen_of_mem]

end Universal

/-! ## Comparison with Mathlib in the commutative case -/

section Commutative

variable (R) (S : Type*) [CommRing S] [Algebra R S]

/-- For commutative `S`, `Ω¹(S) = ker μ` is exactly Mathlib's `KaehlerDifferential.ideal R S`. -/
theorem mem_Ω1_iff_mem_kaehler_ideal (z : S ⊗[R] S) :
    z ∈ Ω1 R S ↔ z ∈ KaehlerDifferential.ideal R S := by
  rw [mem_Ω1, KaehlerDifferential.ideal, RingHom.mem_ker]
  rfl

/-- Mathlib's universal derivation `D` is the class of our `d` in `I / I²`. -/
theorem D_eq_toCotangent_d (a : S) :
    KaehlerDifferential.D R S a =
      (KaehlerDifferential.ideal R S).toCotangent
        ⟨(d R S a : S ⊗[R] S), (mem_Ω1_iff_mem_kaehler_ideal R S _).1 (d R S a).2⟩ := by
  rfl

end Commutative

end QOU.MathlibExt.UniversalDifferentials
