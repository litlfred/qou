import QOU.Core.LieDerivativeComplex

/-!
# Lie derivatives along non-constant vector fields: the tensor (function-linear) forms

Vector fields are the derivations `Der_R(A)` of a commutative `R`-algebra `A` (for a manifold,
`A = C^∞(M)`), acting on `A` by evaluation. A form is an `R`-alternating map
`Der_R(A)^n → A`; it is a *tensor* (`FunLinear`) when it is `A`-linear in every slot.
Because `⁅a • X, Z⁆ = a • ⁅X, Z⁆ - (Z a) • X`, the Koszul differential is only `R`-linear in
its arguments a priori. The results here show the anchor terms cancel:

* `funLinear_ceDAlt`: `d` maps tensors to tensors.
* `funLinear_curryLeft`: so does the interior product `ι_X`.
* `funLinear_lieDerivAlt`: so does the Lie derivative `L_X`.

So the Cartan calculus of `QOU.Core.LieDerivative` and `QOU.Core.LieDerivativeComplex`
(`L_X = d ι_X + ι_X d`, `d ∘ d = 0`, `[L_X, d] = 0`, `[L_X, L_Y] = L_⁅X,Y⁆`) restricts to the
algebraic de Rham complex of `A`, with arbitrary (non-constant) vector fields.

The proof of `funLinear_ceDAlt` uses Cartan's formula: `ι_{aX} dω = L_{aX} ω - d(a ι_X ω)`,
with `L_{aX} ω = a L_X ω + Σᵢ (Yᵢ a) ω(…X at i…)` and `d(a η) = a dη + da ∧ η`; the two
correction sums agree by alternation.

Purely algebraic, generic commutative rings, sorry-free. Bean `qou-pn77`.
-/

namespace QOU.LieDerivative

open Fin

variable {R : Type*} [CommRing R] {A : Type*} [CommRing A] [Algebra R A]

attribute [local instance] derivationLieRingModule

instance derivationLieModule : LieModule R (Derivation R A A) A where
  smul_lie r D a := by change (r • D) a = r • D a; rfl
  lie_smul r D a := by change D (r • a) = r • D a; exact D.map_smul r a

local notation "Der" => Derivation R A A

@[simp] lemma der_lie_apply (D : Der) (a : A) : ⁅D, a⁆ = D a := rfl

/-- The bracket of derivations with a function coefficient:
`⁅a • X, Z⁆ = a • ⁅X, Z⁆ - (Z a) • X`. -/
lemma der_smul_lie (a : A) (X Z : Der) : ⁅a • X, Z⁆ = a • ⁅X, Z⁆ - (Z a) • X := by
  ext b
  simp only [Derivation.commutator_apply, Derivation.smul_apply, Derivation.sub_apply,
    smul_eq_mul, Derivation.leibniz]
  ring

/-- An `R`-alternating form on vector fields is **function-linear** (a tensor) if it is
`A`-linear in every slot. -/
def FunLinear {n : ℕ} (ω : Der [⋀^Fin n]→ₗ[R] A) : Prop :=
  ∀ (v : Fin n → Der) (i : Fin n) (a : A) (X : Der),
    ω (Function.update v i (a • X)) = a * ω (Function.update v i X)

/-- By alternation, `A`-linearity in the first slot gives `A`-linearity in every slot. -/
lemma funLinear_of_head {n : ℕ} (ω : Der [⋀^Fin (n + 1)]→ₗ[R] A)
    (h : ∀ (a : A) (X : Der) (y : Fin n → Der), ω (Fin.cons (a • X) y) = a * ω (Fin.cons X y)) :
    FunLinear ω := by
  intro v i a X
  rw [map_update_eq, map_update_eq, h, mul_smul_comm]

lemma FunLinear.head {n : ℕ} {ω : Der [⋀^Fin (n + 1)]→ₗ[R] A} (h : FunLinear ω)
    (a : A) (X : Der) (y : Fin n → Der) : ω (Fin.cons (a • X) y) = a * ω (Fin.cons X y) := by
  have := h (Fin.cons X y) 0 a X
  simpa [Function.update_eq_self] using this

lemma FunLinear.add {n : ℕ} {ω₁ ω₂ : Der [⋀^Fin n]→ₗ[R] A} (h₁ : FunLinear ω₁)
    (h₂ : FunLinear ω₂) : FunLinear (ω₁ + ω₂) := by
  intro v i a X; simp [h₁ v i a X, h₂ v i a X, mul_add]

lemma FunLinear.sub {n : ℕ} {ω₁ ω₂ : Der [⋀^Fin n]→ₗ[R] A} (h₁ : FunLinear ω₁)
    (h₂ : FunLinear ω₂) : FunLinear (ω₁ - ω₂) := by
  intro v i a X; simp [h₁ v i a X, h₂ v i a X, mul_sub]

/-- **Interior product preserves tensors.** -/
theorem funLinear_curryLeft {n : ℕ} {ω : Der [⋀^Fin (n + 1)]→ₗ[R] A} (h : FunLinear ω)
    (X : Der) : FunLinear (ω.curryLeft X) := by
  intro v i a Y
  simp only [AlternatingMap.curryLeft_apply_apply]
  have e : ∀ Z, (Matrix.vecCons X (Function.update v i Z) : Fin (n + 1) → Der) =
      Function.update (Matrix.vecCons X v) i.succ Z := fun Z => by
    funext k
    refine Fin.cases ?_ (fun k => ?_) k
    · simp [Matrix.vecCons, Function.update_of_ne (Fin.succ_ne_zero i).symm]
    · by_cases hk : k = i
      · subst hk; simp [Matrix.vecCons]
      · simp [Matrix.vecCons, Function.update_of_ne hk,
          Function.update_of_ne (Fin.succ_injective _ |>.ne hk)]
  rw [e, e, h]

/-- Multiplying the values of a form by a function. -/
def mulForm {n : ℕ} (a : A) (η : Der [⋀^Fin n]→ₗ[R] A) : Der [⋀^Fin n]→ₗ[R] A :=
  (LinearMap.mulLeft R a).compAlternatingMap η

@[simp] lemma mulForm_apply {n : ℕ} (a : A) (η : Der [⋀^Fin n]→ₗ[R] A) (v : Fin n → Der) :
    mulForm a η v = a * η v := rfl

/-- `d (a η) = a dη + da ∧ η`. -/
lemma ceD_mulForm {n : ℕ} (a : A) (η : Der [⋀^Fin n]→ₗ[R] A) (y : Fin (n + 1) → Der) :
    ceD (mulForm a η) y =
      a * ceD η y + ∑ i : Fin (n + 1), (-1 : ℤ) ^ (i : ℕ) • (y i a * η (i.removeNth y)) := by
  have hf : firstSum (mulForm a η) y =
      a * firstSum η y + ∑ i : Fin (n + 1), (-1 : ℤ) ^ (i : ℕ) • (y i a * η (i.removeNth y)) := by
    simp only [firstSum, mulForm_apply, der_lie_apply, Derivation.leibniz, smul_eq_mul,
      Finset.mul_sum, ← Finset.sum_add_distrib, mul_smul_comm, smul_add]
    refine Finset.sum_congr rfl fun i _ => ?_
    ring_nf
  cases n with
  | zero => simpa [ceD] using hf
  | succ m =>
    have hb : bracketSum (mulForm a η) y = a * bracketSum η y := by
      simp only [bracketSum, mulForm_apply, Finset.mul_sum]
      refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => ?_
      split_ifs
      · rw [mul_smul_comm]
      · rw [mul_zero]
    simp only [ceD, hf, hb]
    ring

/-- `L_{aX} ω = a L_X ω + Σᵢ (Yᵢ a) ω(…X at i…)` for a tensor `ω`. -/
lemma lieDeriv_smul {n : ℕ} {ω : Der [⋀^Fin n]→ₗ[R] A} (h : FunLinear ω) (a : A) (X : Der)
    (y : Fin n → Der) :
    lieDeriv (a • X) ω y =
      a * lieDeriv X ω y + ∑ i : Fin n, y i a * ω (Function.update y i X) := by
  simp only [lieDeriv, der_lie_apply, Derivation.smul_apply, smul_eq_mul, der_smul_lie]
  have : ∀ i, ω (Function.update y i (a • ⁅X, y i⁆ - y i a • X)) =
      a * ω (Function.update y i ⁅X, y i⁆) - y i a * ω (Function.update y i X) := fun i => by
    rw [AlternatingMap.map_update_sub, h, h]
  simp only [this, Finset.sum_sub_distrib, Finset.mul_sum, mul_sub]
  ring

/-- Head-linearity of `dω` for a tensor `ω` of degree `n + 1`. -/
lemma ceD_head_smul {n : ℕ} {ω : Der [⋀^Fin (n + 1)]→ₗ[R] A} (h : FunLinear ω) (a : A)
    (X : Der) (y : Fin (n + 1) → Der) :
    ceD ω (Fin.cons (a • X) y) = a * ceD ω (Fin.cons X y) := by
  have hc₁ := cartan_formula (a • X) ω y
  have hc₂ := cartan_formula X ω y
  have hι : ω.curryLeft (a • X) = mulForm a (ω.curryLeft X) := by
    ext v; simp [AlternatingMap.curryLeft_apply_apply, Matrix.vecCons, h.head]
  rw [hι, ceD_mulForm, lieDeriv_smul h] at hc₁
  have hs : ∑ i : Fin (n + 1), y i a * ω (Function.update y i X) =
      ∑ i : Fin (n + 1), (-1 : ℤ) ^ (i : ℕ) • (y i a * (ω.curryLeft X) (i.removeNth y)) := by
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [map_update_eq, mul_smul_comm]; rfl
  rw [hs] at hc₁
  have : ceD ω (Fin.cons (a • X) y) = a * lieDeriv X ω y - a * ceD (ω.curryLeft X) y := by
    linear_combination hc₁
  rw [this, ← hc₂]; ring

/-- **`d` preserves tensors.** For a function-linear form `ω` on the vector fields
`Der_R(A)`, its Koszul differential `dω` is again function-linear: `d` restricts to the
algebraic de Rham complex of `A`. -/
theorem funLinear_ceDAlt {n : ℕ} {ω : Der [⋀^Fin n]→ₗ[R] A} (h : FunLinear ω) :
    FunLinear (ceDAlt ω) := by
  apply funLinear_of_head
  intro a X y
  rw [ceDAlt_apply, ceDAlt_apply]
  cases n with
  | zero =>
    simp [ceD, firstSum, Derivation.smul_apply]
  | succ m => exact ceD_head_smul h a X y

/-- **The Lie derivative preserves tensors.** -/
theorem funLinear_lieDerivAlt {n : ℕ} {ω : Der [⋀^Fin n]→ₗ[R] A} (h : FunLinear ω)
    (X : Der) : FunLinear (lieDerivAlt X ω) := by
  cases n with
  | zero => intro _ i; exact i.elim0
  | succ m =>
    have e : lieDerivAlt X ω = (ceDAlt ω).curryLeft X + ceDAlt (ω.curryLeft X) := by
      rw [curryLeft_ceDAlt]; abel
    rw [e]
    exact (funLinear_curryLeft (funLinear_ceDAlt h) X).add
      (funLinear_ceDAlt (funLinear_curryLeft h X))

end QOU.LieDerivative
