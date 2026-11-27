import Mathlib.RingTheory.TensorProduct.Basic

/-!
# The quasi-Yang–Baxter equation from one hexagon, by pure algebra

Bean `qou-5ufw` (constructive item 1.2, three strands). The two-strand case is
`QOU.HeckeTemperleyLieb.HAdicTwoStrandHecke`. For three strands the KZ braid action is
`σ₁ = s₁₂ R₁₂`, `σ₂ = Φ⁻¹ s₂₃ R₂₃ Φ`, and its braid relation `σ₁σ₂σ₁ = σ₂σ₁σ₂` is equivalent
to the **quasi-Yang–Baxter equation**

  `R₁₂ Φ₃₁₂ R₁₃ Φ₁₃₂⁻¹ R₂₃ Φ = Φ₃₂₁ R₂₃ Φ₂₃₁⁻¹ R₁₃ Φ₂₁₃ R₁₂`.

This file proves that equation from

* a coproduct `Δ : A →ₐ[k] A ⊗ A`,
* quasi-cocommutativity `Δᵒᵖ(a) · R = R · Δ(a)` for all `a`,
* the hexagon `(Δ ⊗ id)(R) = P · R₁₃ · Q · R₂₃ · Φ`,

over **any** commutative ring `k`. No analysis, no limit and no numerical value of anything is
used. The pentagon is not used: it is needed for coherence from four strands on, not for the
three-strand braid relation.

**What is data and what is cited.** `P` and `Q` stand for the leg-permuted associators `Φ₃₁₂`
and `Φ₁₃₂⁻¹`. The theorem holds for arbitrary `P, Q`, so nothing about their identity is
assumed. Applying the leg swap `τ₁₂` gives `τ₁₂ P = Φ₃₂₁`, `τ₁₂ Q = Φ₂₃₁⁻¹`, `τ₁₂ Φ = Φ₂₁₃`;
those are the definitions of the permuted associators. That a **rational** associator satisfying
the pentagon and hexagons exists (so that the h-adic KZ data over `ℚ⟦h⟧` is an instance) is
Drinfeld's theorem and is cited, not proved here.
-/

namespace QOU.HeckeTemperleyLieb.QuasiYangBaxterFromHexagon

open scoped TensorProduct
open Algebra.TensorProduct

variable {k A : Type*} [CommRing k] [Ring A] [Algebra k A]

/-- The leg swap `τ₁₂` on `(A ⊗ A) ⊗ A`. -/
noncomputable def tau12 : (A ⊗[k] A) ⊗[k] A →ₐ[k] (A ⊗[k] A) ⊗[k] A :=
  Algebra.TensorProduct.map (Algebra.TensorProduct.comm k A A).toAlgHom (AlgHom.id k A)

/-- `x ↦ x₁₂ = x ⊗ 1`. -/
def leg12 (x : A ⊗[k] A) : (A ⊗[k] A) ⊗[k] A := x ⊗ₜ[k] (1 : A)

/-- `a ⊗ b ↦ (a ⊗ 1) ⊗ b`, i.e. `x ↦ x₁₃`. -/
noncomputable def leg13 : A ⊗[k] A →ₐ[k] (A ⊗[k] A) ⊗[k] A :=
  Algebra.TensorProduct.map (Algebra.TensorProduct.includeLeft : A →ₐ[k] A ⊗[k] A)
    (AlgHom.id k A)

/-- `a ⊗ b ↦ (1 ⊗ a) ⊗ b`, i.e. `x ↦ x₂₃`. -/
noncomputable def leg23 : A ⊗[k] A →ₐ[k] (A ⊗[k] A) ⊗[k] A :=
  Algebra.TensorProduct.map (Algebra.TensorProduct.includeRight : A →ₐ[k] A ⊗[k] A)
    (AlgHom.id k A)

theorem tau12_leg13 (x : A ⊗[k] A) : tau12 (leg13 x) = leg23 x := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul a b =>
    simp [tau12, leg13, leg23, Algebra.TensorProduct.map_tmul,
      Algebra.TensorProduct.includeLeft_apply, Algebra.TensorProduct.includeRight_apply]
  | add x y hx hy => rw [map_add, map_add, hx, hy, map_add]

theorem tau12_leg23 (x : A ⊗[k] A) : tau12 (leg23 x) = leg13 x := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul a b =>
    simp [tau12, leg13, leg23, Algebra.TensorProduct.map_tmul,
      Algebra.TensorProduct.includeLeft_apply, Algebra.TensorProduct.includeRight_apply]
  | add x y hx hy => rw [map_add, map_add, hx, hy, map_add]

/-- Quasi-cocommutativity, tensored with the identity on the third leg:
`(Δᵒᵖ ⊗ id)(X) · R₁₂ = R₁₂ · (Δ ⊗ id)(X)` for every `X ∈ A ⊗ A`. -/
theorem quasiCocomm_leg12 (Δ : A →ₐ[k] A ⊗[k] A) (R : A ⊗[k] A)
    (hR : ∀ a, Algebra.TensorProduct.comm k A A (Δ a) * R = R * Δ a) (X : A ⊗[k] A) :
    tau12 (Algebra.TensorProduct.map Δ (AlgHom.id k A) X) * leg12 R =
      leg12 R * Algebra.TensorProduct.map Δ (AlgHom.id k A) X := by
  induction X using TensorProduct.induction_on with
  | zero => simp
  | tmul a b =>
    simp only [tau12, leg12, Algebra.TensorProduct.map_tmul, AlgHom.id_apply,
      AlgEquiv.toAlgHom_eq_coe, AlgHom.coe_coe, Algebra.TensorProduct.tmul_mul_tmul,
      mul_one, one_mul]
    rw [hR a]
  | add x y hx hy => rw [map_add, map_add, add_mul, mul_add, hx, hy]

/-- **Quasi-Yang–Baxter from one hexagon.** If `Δᵒᵖ(a) R = R Δ(a)` for all `a` and
`(Δ ⊗ id)(R) = P · R₁₃ · Q · R₂₃ · Φ`, then

  `R₁₂ · P · R₁₃ · Q · R₂₃ · Φ = τ₁₂(P) · R₂₃ · τ₁₂(Q) · R₁₃ · τ₁₂(Φ) · R₁₂`.

With `P = Φ₃₁₂`, `Q = Φ₁₃₂⁻¹` this is the quasi-Yang–Baxter equation. -/
theorem quasiYBE_of_hexagon (Δ : A →ₐ[k] A ⊗[k] A) (R : A ⊗[k] A)
    (hR : ∀ a, Algebra.TensorProduct.comm k A A (Δ a) * R = R * Δ a)
    (P Q Φ : (A ⊗[k] A) ⊗[k] A)
    (hhex : Algebra.TensorProduct.map Δ (AlgHom.id k A) R =
      P * leg13 R * Q * leg23 R * Φ) :
    leg12 R * (P * leg13 R * Q * leg23 R * Φ) =
      tau12 P * leg23 R * tau12 Q * leg13 R * tau12 Φ * leg12 R := by
  have h := quasiCocomm_leg12 Δ R hR R
  rw [hhex] at h
  rw [← h]
  simp only [map_mul, tau12_leg13, tau12_leg23]

end QOU.HeckeTemperleyLieb.QuasiYangBaxterFromHexagon
