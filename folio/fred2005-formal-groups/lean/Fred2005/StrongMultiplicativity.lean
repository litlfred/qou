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

The `·` of Def. 1.11 is **not** the product of `T`. It is the product of
`S = ⊗ A_i`, transported to `T` through the ordered inclusion `ι≪ : S → T`
(Def. 1.11, the line after the displayed formula). The two differ on letters
from different `A_i`: in `T`, `y'x' = x'·y' + π(y', x')` (Remark 1.12.1).
So the ordered product is a parameter `μ : A →ₗ A →ₗ A` here, and nothing
ties it to the multiplication of `A`. `(1 ⊗ τ ⊗ 1)` is
`TensorProduct.tensorTensorTensorComm`.

-- Ref: [leitner2006] F. Leitner, arXiv:math/0602138, Def. 1.11, Remark 1.12.
-/

namespace Fred2005.StrongMult

open TensorProduct

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- The operator `(· ⊗ π + π ⊗ · + π ⊗ π)` on `(A ⊗ A) ⊗ (A ⊗ A)`, where each
factor `A ⊗ A` is fed to the ordered product `μ` (the `·` of Def. 1.11) or to
the bracket `π`. -/
noncomputable def smOp (μ π : A →ₗ[R] A →ₗ[R] A) :
    (A ⊗[R] A) ⊗[R] (A ⊗[R] A) →ₗ[R] A ⊗[R] A :=
  TensorProduct.map (TensorProduct.lift μ) (TensorProduct.lift π) +
    TensorProduct.map (TensorProduct.lift π) (TensorProduct.lift μ) +
    TensorProduct.map (TensorProduct.lift π) (TensorProduct.lift π)

/-- Only the `π ⊗ π` part of `smOp`. -/
noncomputable def ppOp (π : A →ₗ[R] A →ₗ[R] A) :
    (A ⊗[R] A) ⊗[R] (A ⊗[R] A) →ₗ[R] A ⊗[R] A :=
  TensorProduct.map (TensorProduct.lift π) (TensorProduct.lift π)

/-- The right-hand side of strong multiplicativity at `(x, y)`, given the
coproducts `Δx`, `Δy`. -/
noncomputable def smRHS (μ π : A →ₗ[R] A →ₗ[R] A) (Δx Δy : A ⊗[R] A) : A ⊗[R] A :=
  smOp μ π (tensorTensorTensorComm R A A A A (Δx ⊗ₜ Δy))

/-- **Strong multiplicativity** (Def. 1.11 of arXiv:math/0602138):
`Δ ∘ π = (· ⊗ π + π ⊗ · + π ⊗ π) ∘ (1 ⊗ τ ⊗ 1) ∘ (Δ ⊗ Δ)` as linear maps
`A ⊗ A → A ⊗ A`, with `π` read through `TensorProduct.lift` and `·` the ordered
product `μ` of `S = ⊗ A_i` transported to `T`. -/
def IsStronglyMultiplicative (μ : A →ₗ[R] A →ₗ[R] A) (Δ : A →ₗ[R] A ⊗[R] A)
    (π : A →ₗ[R] A →ₗ[R] A) : Prop :=
  Δ ∘ₗ TensorProduct.lift π =
    smOp μ π ∘ₗ (tensorTensorTensorComm R A A A A).toLinearMap ∘ₗ TensorProduct.map Δ Δ

/-- Def. 1.11 is equivalent to its pointwise form on pure tensors `x ⊗ y`. -/
theorem isStronglyMultiplicative_iff (μ : A →ₗ[R] A →ₗ[R] A) (Δ : A →ₗ[R] A ⊗[R] A)
    (π : A →ₗ[R] A →ₗ[R] A) :
    IsStronglyMultiplicative μ Δ π ↔ ∀ x y, Δ (π x y) = smRHS μ π (Δ x) (Δ y) := by
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
variable (μ π : A →ₗ[R] A →ₗ[R] A) (hl : ∀ a, π a 1 = 0) (hr : ∀ a, π 1 a = 0)
  (hμl : ∀ a, μ a 1 = a) (hμr : ∀ a, μ 1 a = a)
include hl hr

/-- **The `π ⊗ π` term vanishes on primitive elements** (Remark 1.12). -/
theorem ppOp_prim (x y : A) :
    ppOp π (tensorTensorTensorComm R A A A A (prim x ⊗ₜ prim y)) = 0 := by
  simp [ppOp, prim, add_tmul, tmul_add, tensorTensorTensorComm_tmul, hl, hr]

include hμl hμr

/-- **The right-hand side on primitive elements** is `π(x,y) ⊗ 1 + 1 ⊗ π(x,y)`. -/
theorem smRHS_prim (x y : A) :
    smRHS μ π (prim x) (prim y) = prim (π x y) := by
  simp [smRHS, smOp, prim, add_tmul, tmul_add, tensorTensorTensorComm_tmul, hl, hr, hμl, hμr]
  abel

/-- **Strong multiplicativity at a pair of primitives is primitivity of the
bracket.** If `Δx` and `Δy` are primitive, the condition
`Δ(π(x,y)) = (· ⊗ π + π ⊗ · + π ⊗ π)(1 ⊗ τ ⊗ 1)(Δx ⊗ Δy)` holds exactly when
`π(x, y)` is primitive. -/
theorem strongMult_prim_iff (Δ : A →ₗ[R] A ⊗[R] A) {x y : A}
    (hx : Δ x = prim x) (hy : Δ y = prim y) :
    Δ (π x y) = smRHS μ π (Δ x) (Δ y) ↔ Δ (π x y) = prim (π x y) := by
  rw [hx, hy, smRHS_prim μ π hl hr hμl hμr]

/-- A strongly multiplicative `Δ` sends the bracket of two primitives to a
primitive (Remark 1.12). -/
theorem prim_of_isStronglyMultiplicative (Δ : A →ₗ[R] A ⊗[R] A)
    (h : IsStronglyMultiplicative μ Δ π) {x y : A}
    (hx : Δ x = prim x) (hy : Δ y = prim y) : Δ (π x y) = prim (π x y) :=
  (strongMult_prim_iff μ π hl hr hμl hμr Δ hx hy).1
    ((isStronglyMultiplicative_iff μ Δ π).1 h x y)

end

end Fred2005.StrongMult
