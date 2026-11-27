import CompactQuantumMetrics.OqSU2PBW

/-!
# Coassociativity of `Δ` on `O_q(SU(2))`, commuting convolutions, and the transpose

Bean `qou-q3dc`. `OqSU2Coproduct` builds the coproduct `Δ` and lists coassociativity as not
established. This file proves it and draws the two consequences that the Haar invariance
proof (`OqSU2HaarInvariance`) needs. Everything is over a commutative ring `R`, any unit `q`.

## Results (sorry-free)

* `coprod_coassoc` — `(Δ ⊗ id) Δ = (id ⊗ Δ) Δ` up to the associator, as algebra maps; and
  its linear form `coprod_coassoc_apply`.
* `leftConv f = (f ⊗ id) Δ` (`f` a linear functional), the left-leg convolution operator.
  `leftConv_leftInvOp`: `(f ⊗ id) Δ` commutes with every left-invariant operator
  `X_φ = (id ⊗ φ) Δ`. In Sweedler notation both sides are `f(x₁) x₂ φ(x₃)`.
* `pair_leftInvOp`: `f((id ⊗ φ) Δ x) = φ((f ⊗ id) Δ x)`, both being `(f ⊗ φ) Δ x`.
* `transpose : (α, β, γ, δ) ↦ (α, γ, β, δ)` is an algebra endomorphism (`transposeQuad`), an
  involution (`transpose_transpose`), and a coalgebra anti-map:
  `Δ ∘ T = flip ∘ (T ⊗ T) ∘ Δ` (`coprod_transpose`). It sends the PBW monomial
  `(a, b, c)` to `(a, c, b)` (`transpose_pbwMono`).

No empirical value enters any proof.

-- Ref: [woronowicz1987]
-/

namespace QOU.AlgebraicSubstrate.OqSU2

open TensorProduct

variable {R : Type*} [CommRing R] (q : Rˣ)

local notation "A" => OqSU2 R q

/-! ## Coassociativity -/

/-- **Coassociativity** of the matrix coproduct, as algebra maps `A → A ⊗ (A ⊗ A)`. -/
theorem coprod_coassoc :
    (Algebra.TensorProduct.assoc R R A A A).toAlgHom.comp
        ((Algebra.TensorProduct.map (coprod q) (AlgHom.id R A)).comp (coprod q)) =
      (Algebra.TensorProduct.map (AlgHom.id R A) (coprod q)).comp (coprod q) := by
  refine algHom_ext (B := A ⊗[R] (A ⊗[R] A)) (q := q) ?_ ?_ ?_ ?_ <;>
    simp only [AlgHom.comp_apply, coprod_alpha, coprod_beta, coprod_gamma, coprod_delta,
      map_add, Algebra.TensorProduct.map_tmul, AlgHom.id_apply, AlgEquiv.toAlgHom_eq_coe,
      AlgHom.coe_coe, add_tmul, tmul_add, Algebra.TensorProduct.assoc_tmul] <;>
    abel

/-- Coassociativity in linear form. -/
theorem coprod_coassoc_apply (x : A) :
    TensorProduct.assoc R A A A ((coprod q).toLinearMap.rTensor A (coprod q x)) =
      (coprod q).toLinearMap.lTensor A (coprod q x) := by
  have h := AlgHom.congr_fun (coprod_coassoc q) x
  simp only [AlgHom.comp_apply, AlgEquiv.toAlgHom_eq_coe, AlgHom.coe_coe] at h
  have e1 : ∀ t : A ⊗[R] A, (Algebra.TensorProduct.assoc R R A A A)
      (Algebra.TensorProduct.map (coprod q) (AlgHom.id R A) t) =
      TensorProduct.assoc R A A A ((coprod q).toLinearMap.rTensor A t) := by
    intro t
    induction t using TensorProduct.induction_on with
    | zero => simp
    | tmul y z =>
      simp only [Algebra.TensorProduct.map_tmul, AlgHom.id_apply, LinearMap.rTensor_tmul,
        AlgHom.toLinearMap_apply]
      induction coprod q y using TensorProduct.induction_on with
      | zero => simp
      | tmul u v => simp
      | add s₁ s₂ h₁ h₂ => simp only [add_tmul, map_add, h₁, h₂]
    | add s₁ s₂ h₁ h₂ => simp only [map_add, h₁, h₂]
  have e2 : ∀ t : A ⊗[R] A, Algebra.TensorProduct.map (AlgHom.id R A) (coprod q) t =
      (coprod q).toLinearMap.lTensor A t := by
    intro t
    induction t using TensorProduct.induction_on with
    | zero => simp
    | tmul y z => simp
    | add s₁ s₂ h₁ h₂ => simp only [map_add, h₁, h₂]
  rw [← e1, ← e2, h]

/-! ## The left-leg convolution and its commutation with left-invariant operators -/

/-- `x ⊗ y ↦ f(x) y`. -/
noncomputable def convL (f : A →ₗ[R] R) : A ⊗[R] A →ₗ[R] A :=
  (TensorProduct.lid R A).toLinearMap ∘ₗ LinearMap.rTensor A f

@[simp] theorem convL_tmul (f : A →ₗ[R] R) (x y : A) : convL q f (x ⊗ₜ y) = f x • y := by
  simp [convL]

/-- The left-leg convolution operator `(f ⊗ id) Δ`. -/
noncomputable def leftConv (f : A →ₗ[R] R) : A →ₗ[R] A := convL q f ∘ₗ (coprod q).toLinearMap

theorem leftConv_apply (f : A →ₗ[R] R) (x : A) : leftConv q f x = convL q f (coprod q x) := rfl

theorem leftInvOp_apply' (φ : A →ₗ[R] R) (x : A) : leftInvOp q φ x = conv q φ (coprod q x) :=
  rfl

/-- `(f ⊗ id ⊗ φ)` on the left-bracketed triple tensor. -/
noncomputable def triL (f φ : A →ₗ[R] R) : (A ⊗[R] A) ⊗[R] A →ₗ[R] A :=
  conv q φ ∘ₗ LinearMap.rTensor A (convL q f)

/-- `(f ⊗ id ⊗ φ)` on the right-bracketed triple tensor. -/
noncomputable def triR (f φ : A →ₗ[R] R) : A ⊗[R] (A ⊗[R] A) →ₗ[R] A :=
  convL q f ∘ₗ LinearMap.lTensor A (conv q φ)

theorem triR_assoc (f φ : A →ₗ[R] R) (s : (A ⊗[R] A) ⊗[R] A) :
    triR q f φ (TensorProduct.assoc R A A A s) = triL q f φ s := by
  induction s using TensorProduct.induction_on with
  | zero => simp
  | add s₁ s₂ h₁ h₂ => simp only [map_add, h₁, h₂]
  | tmul s z =>
    induction s using TensorProduct.induction_on with
    | zero => simp
    | add s₁ s₂ h₁ h₂ => simp only [add_tmul, map_add, h₁, h₂]
    | tmul x y => simp [triR, triL, smul_smul, mul_comm]

theorem leftConv_leftInvOp_eq_triL (f φ : A →ₗ[R] R) (t : A ⊗[R] A) :
    leftConv q f (conv q φ t) = triL q f φ ((coprod q).toLinearMap.rTensor A t) := by
  induction t using TensorProduct.induction_on with
  | zero => simp
  | add s₁ s₂ h₁ h₂ => simp only [map_add, h₁, h₂]
  | tmul x y =>
    simp only [conv_tmul, map_smul, LinearMap.rTensor_tmul, AlgHom.toLinearMap_apply, triL,
      LinearMap.comp_apply, leftConv_apply]

theorem leftInvOp_leftConv_eq_triR (f φ : A →ₗ[R] R) (t : A ⊗[R] A) :
    leftInvOp q φ (convL q f t) = triR q f φ ((coprod q).toLinearMap.lTensor A t) := by
  induction t using TensorProduct.induction_on with
  | zero => simp
  | add s₁ s₂ h₁ h₂ => simp only [map_add, h₁, h₂]
  | tmul x y =>
    simp only [convL_tmul, map_smul, LinearMap.lTensor_tmul, AlgHom.toLinearMap_apply, triR,
      LinearMap.comp_apply, leftInvOp_apply']

/-- **Left and right convolutions commute**: `(f ⊗ id)Δ ∘ (id ⊗ φ)Δ = (id ⊗ φ)Δ ∘ (f ⊗ id)Δ`.
This is coassociativity. -/
theorem leftConv_leftInvOp (f φ : A →ₗ[R] R) (x : A) :
    leftConv q f (leftInvOp q φ x) = leftInvOp q φ (leftConv q f x) := by
  rw [leftInvOp_apply', leftConv_leftInvOp_eq_triL, leftConv_apply,
    leftInvOp_leftConv_eq_triR, ← coprod_coassoc_apply, triR_assoc]

/-- `f((id ⊗ φ) Δ x) = φ((f ⊗ id) Δ x)`: both are `(f ⊗ φ) Δ x`. -/
theorem pair_leftInvOp (f φ : A →ₗ[R] R) (x : A) :
    f (leftInvOp q φ x) = φ (leftConv q f x) := by
  rw [leftInvOp_apply', leftConv_apply]
  induction coprod q x using TensorProduct.induction_on with
  | zero => simp
  | add s₁ s₂ h₁ h₂ => simp only [map_add, h₁, h₂]
  | tmul u v => simp [mul_comm]

/-- `(f ⊗ id) Δ 1 = f(1) · 1`. -/
theorem leftConv_one (f : A →ₗ[R] R) : leftConv q f 1 = f 1 • (1 : A) := by
  rw [leftConv_apply, map_one, Algebra.TensorProduct.one_def, convL_tmul]

/-! ## The transpose `(α, β, γ, δ) ↦ (α, γ, β, δ)` -/

theorem transposeQuad : IsOqSU2Quadruple (R := R) q (α q) (γ q) (β q) (δ q) where
  ab := rel_ag q
  ag := rel_ab q
  bd := rel_gd q
  gd := rel_bd q
  bg := (rel_bg q).symm
  det_left := by rw [← rel_bg]; exact rel_det_left q
  det_right := by rw [← rel_bg]; exact rel_det_right q

/-- The transpose `T : (α, β, γ, δ) ↦ (α, γ, β, δ)`, an algebra endomorphism. -/
noncomputable def transpose : A →ₐ[R] A := liftQuadruple q _ _ _ _ (transposeQuad q)

@[simp] theorem transpose_alpha : transpose q (α q) = α (R := R) q := liftQuadruple_alpha ..
@[simp] theorem transpose_beta : transpose q (β q) = γ (R := R) q := liftQuadruple_beta ..
@[simp] theorem transpose_gamma : transpose q (γ q) = β (R := R) q := liftQuadruple_gamma ..
@[simp] theorem transpose_delta : transpose q (δ q) = δ (R := R) q := liftQuadruple_delta ..

theorem transpose_transpose (x : A) : transpose q (transpose q x) = x := by
  have h : (transpose q).comp (transpose q) = AlgHom.id R A := algHom_ext (by simp) (by simp)
    (by simp) (by simp)
  exact AlgHom.congr_fun h x

/-- `Δ ∘ T = flip ∘ (T ⊗ T) ∘ Δ`: the transpose reverses the coproduct. -/
theorem coprod_transpose :
    (coprod q).comp (transpose q) =
      (Algebra.TensorProduct.comm R A A).toAlgHom.comp
        ((Algebra.TensorProduct.map (transpose q) (transpose q)).comp (coprod q)) := by
  refine algHom_ext (B := A ⊗[R] A) (q := q) ?_ ?_ ?_ ?_ <;>
    simp only [AlgHom.comp_apply, transpose_alpha, transpose_beta, transpose_gamma,
      transpose_delta, coprod_alpha, coprod_beta, coprod_gamma, coprod_delta, map_add,
      Algebra.TensorProduct.map_tmul, AlgEquiv.toAlgHom_eq_coe, AlgHom.coe_coe,
      Algebra.TensorProduct.comm_tmul]

/-- Linear form of `coprod_transpose`. -/
theorem coprod_transpose_apply (x : A) :
    coprod q (transpose q x) =
      TensorProduct.comm R A A
        (TensorProduct.map (transpose q).toLinearMap (transpose q).toLinearMap (coprod q x)) := by
  have h := AlgHom.congr_fun (coprod_transpose q) x
  simp only [AlgHom.comp_apply, AlgEquiv.toAlgHom_eq_coe, AlgHom.coe_coe] at h
  rw [h]
  induction coprod q x using TensorProduct.induction_on with
  | zero => simp
  | tmul u v => simp
  | add s₁ s₂ h₁ h₂ => simp only [map_add, h₁, h₂]

/-- `T(β^b γ^c) = β^c γ^b`. -/
theorem transpose_monoY (b c : ℕ) : transpose q (monoY q b c) = monoY (R := R) q c b := by
  have hc : Commute (γ (R := R) q ^ b) (β q ^ c) :=
    ((Commute.symm (show Commute (β (R := R) q) (γ q) from rel_bg q))).pow_pow b c
  rw [monoY, map_mul, map_pow, map_pow, transpose_beta, transpose_gamma, hc.eq, monoY]

/-- `T` sends the PBW monomial `(a, b, c)` to `(a, c, b)`. -/
theorem transpose_pbwMono (i : MonoIdx) :
    transpose q (pbwMono q i) = pbwMono (R := R) q (i.1, i.2.2, i.2.1) := by
  obtain ⟨a, b, c⟩ := i
  simp only [pbwMono]
  split_ifs <;> simp [monoA, monoD, transpose_monoY]

end QOU.AlgebraicSubstrate.OqSU2
