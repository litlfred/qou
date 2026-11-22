/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.FormalGroups.SplayPoisson
import Mathlib.RingTheory.TensorProduct.Basic
import Mathlib.LinearAlgebra.TensorProduct.Associator

/-!
# The coproduct descends to `U = T / J` (Prop. 1.13 of arXiv:math/0602138)

Def. 1.11 of F. Leitner, arXiv:math/0602138, calls `π` *strongly multiplicative* when

  `Δ ∘ π = (· ⊗ π + π ⊗ · + π ⊗ π) ∘ (1 ⊗ τ ⊗ 1) ∘ (Δ ⊗ Δ)`,

where `·` is the *ordered* product (the product of `S = ⊗ Aᵢ` read in `T`), not the
product of `T`. Prop. 1.13 says that then `Δ` descends to an algebra map
`U → U ⊗ U`, where `U = T / J` and `J = (yx − xy − π(y, x))`.

This file proves that statement for the quotient `IntegrationQuotient π` of
`SplayPoisson.lean`, whose relation is `fg ~ gf + π(f, g)`.

* The ordered product is a parameter `μ`. The one property of it the proof uses is
  that in `U` it is the *reversed* product of the relation's two letters:
  `mk (μ f g) = mk g * mk f`. For a cross pair `f = y ∈ Aⱼ`, `g = x ∈ Aᵢ`, `j > i`,
  the ordered product puts `x` first, so `μ(y, x) = x y` and the property holds
  (`opMul` is the choice that makes it hold for every pair).
* The proof is the paper's: modulo `J ⊗ T + T ⊗ J`, the commutator of two pure tensors
  `(a ⊗ b)(c ⊗ d) − (c ⊗ d)(a ⊗ b)` equals
  `ca ⊗ [b, d] + [a, c] ⊗ db + [a, c] ⊗ [b, d]` (`tmul_commutator`), and in `U` each
  commutator is the image of a bracket (`integrationMk_commutator`). That is the
  right-hand side of Def. 1.11, so `Δ(fg − gf − π(f, g))` maps to zero.

The counit descends under the weaker hypothesis `ε ∘ π = 0` (`counitDescends`).

-- Ref: [leitner2006] F. Leitner, arXiv:math/0602138, Def. 1.11 and Prop. 1.13.
-/

namespace QOU.FormalGroups

open TensorProduct

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- The operator `(· ⊗ π + π ⊗ · + π ⊗ π)` of Def. 1.11 on `(A ⊗ A) ⊗ (A ⊗ A)`. -/
noncomputable def smOp (μ π : A →ₗ[R] A →ₗ[R] A) :
    (A ⊗[R] A) ⊗[R] (A ⊗[R] A) →ₗ[R] A ⊗[R] A :=
  TensorProduct.map (TensorProduct.lift μ) (TensorProduct.lift π) +
    TensorProduct.map (TensorProduct.lift π) (TensorProduct.lift μ) +
    TensorProduct.map (TensorProduct.lift π) (TensorProduct.lift π)

/-- **Strong multiplicativity** (Def. 1.11 of arXiv:math/0602138), pointwise:
`Δ(π(x, y)) = (· ⊗ π + π ⊗ · + π ⊗ π)((1 ⊗ τ ⊗ 1)(Δx ⊗ Δy))`. -/
def IsStronglyMultiplicative (μ : A →ₗ[R] A →ₗ[R] A) (Δ : A →ₗ[R] A ⊗[R] A)
    (π : A →ₗ[R] A →ₗ[R] A) : Prop :=
  ∀ x y, Δ (π x y) = smOp μ π (tensorTensorTensorComm R A A A A (Δ x ⊗ₜ Δ y))

variable (R A) in
/-- The reversed product `μ(f, g) = g f`. -/
noncomputable def opMul : A →ₗ[R] A →ₗ[R] A := (LinearMap.mul R A).flip

@[simp] theorem opMul_apply (f g : A) : opMul R A f g = g * f := rfl

/-- **The commutator of two pure tensors.** In any algebra `B`,
`(a ⊗ b)(c ⊗ d) − (c ⊗ d)(a ⊗ b) = ca ⊗ [b,d] + [a,c] ⊗ db + [a,c] ⊗ [b,d]`. -/
theorem tmul_commutator {B : Type*} [Ring B] [Algebra R B] (a b c d : B) :
    (a ⊗ₜ[R] b) * (c ⊗ₜ[R] d) - (c ⊗ₜ[R] d) * (a ⊗ₜ[R] b) =
      (c * a) ⊗ₜ[R] (b * d - d * b) + (a * c - c * a) ⊗ₜ[R] (d * b) +
        (a * c - c * a) ⊗ₜ[R] (b * d - d * b) := by
  simp only [Algebra.TensorProduct.tmul_mul_tmul, sub_tmul, tmul_sub]
  abel

section Descent

variable (π : PoissonStructure R A) (μ : A →ₗ[R] A →ₗ[R] A)
  (hμ : ∀ f g, integrationMk π (μ f g) = integrationMk π g * integrationMk π f)

/-- `mk ⊗ mk : A ⊗ A → U ⊗ U`. -/
noncomputable def mk2 : A ⊗[R] A →ₐ[R] IntegrationQuotient π ⊗[R] IntegrationQuotient π :=
  Algebra.TensorProduct.map (integrationMk π) (integrationMk π)

include hμ in
/-- **The key identity.** For all `X, Y ∈ A ⊗ A`, the commutator of their images in
`U ⊗ U` is the image of `(· ⊗ π + π ⊗ · + π ⊗ π)((1 ⊗ τ ⊗ 1)(X ⊗ Y))`. -/
theorem mk2_commutator (X Y : A ⊗[R] A) :
    mk2 π X * mk2 π Y - mk2 π Y * mk2 π X =
      mk2 π (smOp μ π.bracket (tensorTensorTensorComm R A A A A (X ⊗ₜ Y))) := by
  induction X using TensorProduct.induction_on with
  | zero => simp
  | add X₁ X₂ h₁ h₂ =>
    simp only [map_add, add_mul, mul_add, add_tmul] at h₁ h₂ ⊢
    rw [← h₁, ← h₂]; abel
  | tmul x₁ x₂ =>
    induction Y using TensorProduct.induction_on with
    | zero => simp
    | add Y₁ Y₂ h₁ h₂ =>
      simp only [map_add, add_mul, mul_add, tmul_add] at h₁ h₂ ⊢
      rw [← h₁, ← h₂]; abel
    | tmul y₁ y₂ =>
      simp only [mk2, Algebra.TensorProduct.map_tmul, tensorTensorTensorComm_tmul, smOp,
        LinearMap.add_apply, map_add, TensorProduct.map_tmul, TensorProduct.lift.tmul, hμ,
        ← integrationMk_commutator]
      rw [tmul_commutator]

variable (Δ : A →ₐ[R] A ⊗[R] A)

include hμ in
/-- `(mk ⊗ mk) ∘ Δ` kills the relation `fg ~ gf + π(f, g)`. -/
theorem mk2_comp_respects (hΔ : IsStronglyMultiplicative μ Δ.toLinearMap π.bracket)
    ⦃f g : A⦄ (h : IntegrationRel π f g) : (mk2 π).comp Δ f = (mk2 π).comp Δ g := by
  obtain ⟨f, g⟩ := h
  have hk := mk2_commutator π μ hμ (Δ f) (Δ g)
  have hd := hΔ f g
  simp only [AlgHom.toLinearMap_apply] at hd
  rw [← hd] at hk
  simp only [AlgHom.comp_apply, map_mul, map_add]
  rw [← hk]; abel

/-- **Prop. 1.13 of arXiv:math/0602138.** If `Δ : T → T ⊗ T` is an algebra map and `π`
is strongly multiplicative for it, `Δ` descends to an algebra map `U → U ⊗ U` on
`U = T / J`. -/
noncomputable def descendedComul (hΔ : IsStronglyMultiplicative μ Δ.toLinearMap π.bracket) :
    IntegrationQuotient π →ₐ[R] IntegrationQuotient π ⊗[R] IntegrationQuotient π :=
  RingQuot.liftAlgHom R ⟨(mk2 π).comp Δ, mk2_comp_respects π μ hμ Δ hΔ⟩

/-- The descended coproduct is `(mk ⊗ mk) ∘ Δ` on representatives. -/
theorem descendedComul_mk (hΔ : IsStronglyMultiplicative μ Δ.toLinearMap π.bracket) (f : A) :
    descendedComul π μ hμ Δ hΔ (integrationMk π f) =
      Algebra.TensorProduct.map (integrationMk π) (integrationMk π) (Δ f) := by
  simp [descendedComul, integrationMk, mk2]

/-- With `μ` the reversed product, the hypothesis on `μ` holds for every pair. -/
theorem opMul_integrationMk (f g : A) :
    integrationMk π (opMul R A f g) = integrationMk π g * integrationMk π f := by
  simp

/-- The counit descends when `ε ∘ π = 0`: `ε(fg) = ε(gf)` because `R` is commutative. -/
noncomputable def counitDescends (ε : A →ₐ[R] R) (hε : ∀ f g, ε (π.bracket f g) = 0) :
    IntegrationQuotient π →ₐ[R] R :=
  RingQuot.liftAlgHom R ⟨ε, by
    rintro _ _ ⟨f, g⟩
    simp [hε, mul_comm]⟩

end Descent

end QOU.FormalGroups
