import Mathlib.LinearAlgebra.TensorProduct.Associator
import Mathlib.Algebra.Algebra.Bilinear

/-!
# Strong multiplicativity on primitive elements

Def. 1.11 of arXiv:math/0602138 calls a Poisson structure `π` on a bialgebra `T`
*strongly multiplicative* when

  `Δ ∘ π = (· ⊗ π + π ⊗ · + π ⊗ π) ∘ (1 ⊗ τ ⊗ 1) ∘ (Δ ⊗ Δ)`.

This file builds the right-hand operator from Mathlib's tensor-product maps and
proves the computation of Remark 1.12: when `π` vanishes against the unit (as a
biderivation does) and `x, y` are primitive, the `π ⊗ π` term contributes
nothing, and the condition at `(x, y)` says exactly that `π(x, y)` is primitive.

The ring `A` is not assumed commutative: `·` is the product of `A`
(`LinearMap.mul'`), as in the paper, where `T` is a tensor algebra.
`(1 ⊗ τ ⊗ 1)` is `TensorProduct.tensorTensorTensorComm`.

-- Ref: [leitner2006] F. Leitner, arXiv:math/0602138, Def. 1.11, Remark 1.12.
-/

namespace Fred2005.StrongMult

open TensorProduct

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- The operator `(· ⊗ π + π ⊗ · + π ⊗ π)` on `(A ⊗ A) ⊗ (A ⊗ A)`, where each
factor `A ⊗ A` is fed to the product `·` or to the bracket `π`. -/
noncomputable def smOp (π : A →ₗ[R] A →ₗ[R] A) :
    (A ⊗[R] A) ⊗[R] (A ⊗[R] A) →ₗ[R] A ⊗[R] A :=
  TensorProduct.map (LinearMap.mul' R A) (TensorProduct.lift π) +
    TensorProduct.map (TensorProduct.lift π) (LinearMap.mul' R A) +
    TensorProduct.map (TensorProduct.lift π) (TensorProduct.lift π)

/-- Only the `π ⊗ π` part of `smOp`. -/
noncomputable def ppOp (π : A →ₗ[R] A →ₗ[R] A) :
    (A ⊗[R] A) ⊗[R] (A ⊗[R] A) →ₗ[R] A ⊗[R] A :=
  TensorProduct.map (TensorProduct.lift π) (TensorProduct.lift π)

/-- The right-hand side of strong multiplicativity at `(x, y)`, given the
coproducts `Δx`, `Δy`. -/
noncomputable def smRHS (π : A →ₗ[R] A →ₗ[R] A) (Δx Δy : A ⊗[R] A) : A ⊗[R] A :=
  smOp π (tensorTensorTensorComm R A A A A (Δx ⊗ₜ Δy))

/-- **Strong multiplicativity** (Def. 1.11 of arXiv:math/0602138):
`Δ ∘ π = (· ⊗ π + π ⊗ · + π ⊗ π) ∘ (1 ⊗ τ ⊗ 1) ∘ (Δ ⊗ Δ)` as linear maps
`A ⊗ A → A ⊗ A`, with `π` read through `TensorProduct.lift`. -/
def IsStronglyMultiplicative (Δ : A →ₗ[R] A ⊗[R] A) (π : A →ₗ[R] A →ₗ[R] A) : Prop :=
  Δ ∘ₗ TensorProduct.lift π =
    smOp π ∘ₗ (tensorTensorTensorComm R A A A A).toLinearMap ∘ₗ TensorProduct.map Δ Δ

/-- Def. 1.11 is equivalent to its pointwise form on pure tensors `x ⊗ y`. -/
theorem isStronglyMultiplicative_iff (Δ : A →ₗ[R] A ⊗[R] A) (π : A →ₗ[R] A →ₗ[R] A) :
    IsStronglyMultiplicative Δ π ↔ ∀ x y, Δ (π x y) = smRHS π (Δ x) (Δ y) := by
  constructor
  · intro h x y
    have := LinearMap.congr_fun h (x ⊗ₜ y)
    simpa [smRHS] using this
  · intro h
    apply TensorProduct.ext'
    intro x y
    simpa [smRHS] using h x y

/-- The primitive coproduct `x ⊗ 1 + 1 ⊗ x`. -/
def prim (x : A) : A ⊗[R] A := x ⊗ₜ 1 + 1 ⊗ₜ x

section
variable (π : A →ₗ[R] A →ₗ[R] A) (hl : ∀ a, π a 1 = 0) (hr : ∀ a, π 1 a = 0)
include hl hr

/-- **The `π ⊗ π` term vanishes on primitive elements** (Remark 1.12). -/
theorem ppOp_prim (x y : A) :
    ppOp π (tensorTensorTensorComm R A A A A (prim x ⊗ₜ prim y)) = 0 := by
  simp [ppOp, prim, add_tmul, tmul_add, tensorTensorTensorComm_tmul, hl, hr]

/-- **The right-hand side on primitive elements** is `π(x,y) ⊗ 1 + 1 ⊗ π(x,y)`. -/
theorem smRHS_prim (x y : A) :
    smRHS π (prim x) (prim y) = prim (π x y) := by
  simp [smRHS, smOp, prim, add_tmul, tmul_add, tensorTensorTensorComm_tmul, hl, hr]
  abel

/-- **Strong multiplicativity at a pair of primitives is primitivity of the
bracket.** If `Δx` and `Δy` are primitive, the condition
`Δ(π(x,y)) = (· ⊗ π + π ⊗ · + π ⊗ π)(1 ⊗ τ ⊗ 1)(Δx ⊗ Δy)` holds exactly when
`π(x, y)` is primitive. -/
theorem strongMult_prim_iff (Δ : A →ₗ[R] A ⊗[R] A) {x y : A}
    (hx : Δ x = prim x) (hy : Δ y = prim y) :
    Δ (π x y) = smRHS π (Δ x) (Δ y) ↔ Δ (π x y) = prim (π x y) := by
  rw [hx, hy, smRHS_prim π hl hr]

/-- A strongly multiplicative `Δ` sends the bracket of two primitives to a
primitive (Remark 1.12). -/
theorem prim_of_isStronglyMultiplicative (Δ : A →ₗ[R] A ⊗[R] A)
    (h : IsStronglyMultiplicative Δ π) {x y : A}
    (hx : Δ x = prim x) (hy : Δ y = prim y) : Δ (π x y) = prim (π x y) :=
  (strongMult_prim_iff π hl hr Δ hx hy).1 ((isStronglyMultiplicative_iff Δ π).1 h x y)

end

end Fred2005.StrongMult
