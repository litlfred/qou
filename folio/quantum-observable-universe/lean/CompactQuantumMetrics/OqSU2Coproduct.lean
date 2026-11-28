import CompactQuantumMetrics.OqSU2ModularNakayama
import Mathlib.RingTheory.TensorProduct.Basic
import Mathlib.Tactic.Group

/-!
# The coproduct of `O_q(SU(2))` and its left-invariant Cartan field

Bean `qou-q3dc`. The corpus presents `O_q(SU(2))` as an algebra
(`OqSU2ModularNakayama.lean`) but had no coproduct, so left-invariant vector
fields could not be written down. This file adds it, over a generic
commutative ring `R` (§7c).

## Results (sorry-free)

* `coprodQuad`, `coprod`: the matrix coproduct
  `Δα = α⊗α + β⊗γ`, `Δβ = α⊗β + β⊗δ`, `Δγ = γ⊗α + δ⊗γ`, `Δδ = γ⊗β + δ⊗δ`
  respects all seven defining relations, so it is an algebra map
  `O_q(SU(2)) → O_q(SU(2)) ⊗ O_q(SU(2))`.
* `rightTrans_diagChar`, `leftTrans_diagChar`: translation by the diagonal
  character `χ_u = (u, 0, 0, u⁻¹)` is a torus scaling. Right translation gives
  `(uα, u⁻¹β, uγ, u⁻¹δ)`; left translation gives `(uα, uβ, u⁻¹γ, u⁻¹δ)`.
  `rightTrans_counit`: right translation by the counit is the identity.
* `hk_sigma_eq_two_sided`: the Hadfield–Krähmer automorphism of the 3D calculus,
  `(q⁻²α, q⁴β, q⁻⁴γ, q²δ)`, is left translation at `q` followed by right
  translation at `q⁻³`. A right translation alone scales `β` by the inverse of
  the `α` scale, and `q⁴ = (q⁻²)⁻¹` only when `q² = 1`, so `σ` is a two-sided
  translation, not the Leibniz twist of a single left-invariant field.
* `leftInvOp_leibniz`: if `φ` satisfies `φ(xy) = φ(x)χ(y) + ε(x)φ(y)` for a
  character `χ`, the left-invariant operator `X_φ = (id ⊗ φ)Δ` satisfies
  `X_φ(fg) = X_φ f · R_χ g + f · X_φ g`. The left factor is untwisted.
* `cartanField`: for `φ = (ε − χ_u)/c` this operator is the one-sided difference
  `f ↦ c⁻¹(f − R_u f)` with `R_u = (uα, u⁻¹β, uγ, u⁻¹δ)`. So a Cartan field of
  this form is exactly the one-sided `qDiff` of `q_ns_twisted_transport.lean`,
  and its energy budget is `−c·φ(Du·Du)` for an `R_u`-invariant functional.

## Not established

* That Woronowicz's Cartan functional for the 3D calculus is `(ε − χ_u)/c`, or
  which `u` it uses. Woronowicz (1987) is not in `library/`, so the parameter
  is left free here. Narrowed in `OqSU2TwistedDerivations.lean`: when `q² − 1`
  is a unit every twist is some `χ_u` (`char_eq_diagChar`), and a twisted
  derivation non-zero on `β` or `γ` forces `u = q⁻¹`
  (`twistedDerivation_offDiag_forces`). For a diagonal field `u` stays free.
* The off-diagonal vector fields of the 3D calculus: now in `OqSU2OffDiagonal.lean`.
* The left counit law. Coassociativity is in `OqSU2Coassoc.lean`; the Haar state is in
  `OqSU2HaarState.lean`, and its coproduct invariance is in
  `QOU/FluidDynamics/q_ns_haar_coproduct_invariance.lean`.
* Anything about Part A of `conj:regularity-breakdown` (bean `qou-pa7n`).

No empirical value enters any proof.

## References

- [woronowicz1987-twisted-su2] Woronowicz, *Twisted SU(2) group. An example of a
  non-commutative differential calculus* (1987): the coproduct and the 3D calculus.
- [hadfield-krahmer-2005] Hadfield, Krähmer, *Twisted homology of quantum SL(2)*,
  arXiv:math/0405249, "three dimensional left-covariant calculus" (library
  `arxiv-math-0405249v5`): the automorphism `σ`.
-/

namespace QOU.AlgebraicSubstrate.OqSU2

open TensorProduct

variable {R : Type*} [CommRing R]

theorem det_left' (q : Rˣ) : α (R := R) q * δ q = 1 + (q : R) • (β q * γ q) := by
  rw [← rel_det_left q]; abel

theorem det_right' (q : Rˣ) :
    δ (R := R) q * α q = 1 + (((q⁻¹ : Rˣ) : R)) • (β q * γ q) := by
  rw [← rel_det_right q]; abel

macro "coprod_norm" : tactic => `(tactic| (
  simp only [add_mul, mul_add, sub_eq_add_neg, neg_add, neg_mul, mul_neg, smul_add, smul_neg,
    Algebra.TensorProduct.tmul_mul_tmul, smul_mul_assoc, mul_smul_comm,
    rel_ab, rel_ag, rel_bd, rel_gd, det_left', det_right', ← rel_bg,
    tmul_add, add_tmul, tmul_smul, smul_tmul', smul_smul, tmul_neg, neg_tmul,
    Units.mul_inv, Units.inv_mul, one_smul, Algebra.TensorProduct.one_def] <;>
  abel))

variable (q : Rˣ)

local notation "a" => α (R := R) q
local notation "b" => β (R := R) q
local notation "g" => γ (R := R) q
local notation "d" => δ (R := R) q

theorem coprodQuad : IsOqSU2Quadruple (R := R) q
    (a ⊗ₜ[R] a + b ⊗ₜ g) (a ⊗ₜ[R] b + b ⊗ₜ d) (g ⊗ₜ[R] a + d ⊗ₜ g) (g ⊗ₜ[R] b + d ⊗ₜ d) where
  ab := by coprod_norm
  ag := by coprod_norm
  bd := by coprod_norm
  gd := by coprod_norm
  bg := by coprod_norm
  det_left := by coprod_norm
  det_right := by coprod_norm

/-- The coproduct `Δ : O_q(SU(2)) → O_q(SU(2)) ⊗ O_q(SU(2))`, the matrix coproduct
`Δ uᵢⱼ = ∑ₖ uᵢₖ ⊗ uₖⱼ` on `u = ((α, β), (γ, δ))`. -/
noncomputable def coprod : OqSU2 R q →ₐ[R] OqSU2 R q ⊗[R] OqSU2 R q :=
  liftQuadruple q _ _ _ _ (coprodQuad q)

@[simp] theorem coprod_alpha : coprod q (α q) = a ⊗ₜ[R] a + b ⊗ₜ g := liftQuadruple_alpha ..
@[simp] theorem coprod_beta : coprod q (β q) = a ⊗ₜ[R] b + b ⊗ₜ d := liftQuadruple_beta ..
@[simp] theorem coprod_gamma : coprod q (γ q) = g ⊗ₜ[R] a + d ⊗ₜ g := liftQuadruple_gamma ..
@[simp] theorem coprod_delta : coprod q (δ q) = g ⊗ₜ[R] b + d ⊗ₜ d := liftQuadruple_delta ..

/-- Right translation by a character `χ`: `f ↦ (id ⊗ χ) Δ f`. -/
noncomputable def rightTrans (χ : OqSU2 R q →ₐ[R] R) : OqSU2 R q →ₐ[R] OqSU2 R q :=
  ((Algebra.TensorProduct.rid R R (OqSU2 R q)).toAlgHom.comp
    (Algebra.TensorProduct.map (AlgHom.id R (OqSU2 R q)) χ)).comp (coprod q)

/-- Left translation by a character `χ`: `f ↦ (χ ⊗ id) Δ f`. -/
noncomputable def leftTrans (χ : OqSU2 R q →ₐ[R] R) : OqSU2 R q →ₐ[R] OqSU2 R q :=
  ((Algebra.TensorProduct.lid R (OqSU2 R q)).toAlgHom.comp
    (Algebra.TensorProduct.map χ (AlgHom.id R (OqSU2 R q)))).comp (coprod q)

/-- Right translation by the diagonal character `(u, 0, 0, u⁻¹)` is the torus scaling
`(α, β, γ, δ) ↦ (uα, u⁻¹β, uγ, u⁻¹δ)`. -/
theorem rightTrans_diagChar (u : Rˣ) :
    rightTrans q (diagCharAlgHom q u) = torusScaleAlgHom q u u⁻¹ := by
  apply algHom_ext <;> simp [rightTrans, torusScaleAlgHom, diagCharAlgHom]

/-- Left translation by the diagonal character `(u, 0, 0, u⁻¹)` is the torus scaling
`(α, β, γ, δ) ↦ (uα, uβ, u⁻¹γ, u⁻¹δ)`. -/
theorem leftTrans_diagChar (u : Rˣ) :
    leftTrans q (diagCharAlgHom q u) = torusScaleAlgHom q u u := by
  apply algHom_ext <;> simp [leftTrans, torusScaleAlgHom, diagCharAlgHom]

/-- The counit `ε : (α, β, γ, δ) ↦ (1, 0, 0, 1)`. -/
noncomputable abbrev counit : OqSU2 R q →ₐ[R] R := diagCharAlgHom q 1

theorem rightTrans_counit : rightTrans q (counit q) = AlgHom.id R (OqSU2 R q) := by
  apply algHom_ext <;> simp [rightTrans, counit, diagCharAlgHom]

/-- The two-sided translation behind the Hadfield–Krähmer automorphism
`(α, β, γ, δ) ↦ (q⁻²α, q⁴β, q⁻⁴γ, q²δ)`: it is left translation by the diagonal
character at `q` composed with right translation by the diagonal character at `q⁻³`. -/
theorem hk_sigma_eq_two_sided :
    torusScaleAlgHom (R := R) q (q⁻¹ ^ 2) (q ^ 4) =
      (rightTrans q (diagCharAlgHom q (q⁻¹ ^ 3))).comp (leftTrans q (diagCharAlgHom q q)) := by
  rw [rightTrans_diagChar, leftTrans_diagChar, torusScaleAlgHom_comp]
  congr 1 <;> group

/-- Convolution `x ⊗ y ↦ φ(y) x` of `A ⊗ A` with a linear functional on the right leg. -/
noncomputable def conv (φ : OqSU2 R q →ₗ[R] R) :
    OqSU2 R q ⊗[R] OqSU2 R q →ₗ[R] OqSU2 R q :=
  (TensorProduct.rid R (OqSU2 R q)).toLinearMap ∘ₗ LinearMap.lTensor (OqSU2 R q) φ

@[simp] theorem conv_tmul (φ : OqSU2 R q →ₗ[R] R) (x y : OqSU2 R q) :
    conv q φ (x ⊗ₜ y) = φ y • x := by
  simp [conv]

theorem rightTrans_apply (χ : OqSU2 R q →ₐ[R] R) (f : OqSU2 R q) :
    rightTrans q χ f = conv q χ.toLinearMap (coprod q f) := by
  simp only [rightTrans, conv, AlgHom.comp_apply, AlgEquiv.toAlgHom_eq_coe,
    AlgHom.coe_coe, LinearMap.comp_apply, LinearEquiv.coe_coe]
  induction coprod q f using TensorProduct.induction_on with
  | zero => simp
  | tmul x y => simp
  | add x y hx hy => simp only [map_add, hx, hy]

/-- The left-invariant operator `X_φ f = (id ⊗ φ) Δ f`. -/
noncomputable def leftInvOp (φ : OqSU2 R q →ₗ[R] R) : OqSU2 R q →ₗ[R] OqSU2 R q :=
  conv q φ ∘ₗ (coprod q).toLinearMap

theorem conv_mul (φ : OqSU2 R q →ₗ[R] R) (χ : OqSU2 R q →ₐ[R] R)
    (hφ : ∀ x y, φ (x * y) = φ x * χ y + counit q x * φ y)
    (S T : OqSU2 R q ⊗[R] OqSU2 R q) :
    conv q φ (S * T) = conv q φ S * conv q χ.toLinearMap T +
      conv q (counit q).toLinearMap S * conv q φ T := by
  induction S using TensorProduct.induction_on with
  | zero => simp
  | add S₁ S₂ h₁ h₂ => simp only [add_mul, map_add, h₁, h₂]; abel
  | tmul x y =>
    induction T using TensorProduct.induction_on with
    | zero => simp
    | add T₁ T₂ h₁ h₂ => simp only [mul_add, map_add, h₁, h₂]; abel
    | tmul x' y' =>
      simp only [Algebra.TensorProduct.tmul_mul_tmul, conv_tmul, hφ, AlgHom.toLinearMap_apply,
        add_smul, smul_mul_smul_comm, mul_comm (φ y)]

/-- **Left-invariant fields are one-sided twisted derivations.** If `φ` is an
`(ε, χ)`-twisted derivation of the counit, then `X_φ = (id ⊗ φ)Δ` satisfies
`X_φ(fg) = X_φ f · R_χ g + f · X_φ g`, where `R_χ` is right translation by `χ`.
The left factor is untwisted. -/
theorem leftInvOp_leibniz (φ : OqSU2 R q →ₗ[R] R) (χ : OqSU2 R q →ₐ[R] R)
    (hφ : ∀ x y, φ (x * y) = φ x * χ y + counit q x * φ y) (f₁ f₂ : OqSU2 R q) :
    leftInvOp q φ (f₁ * f₂) = leftInvOp q φ f₁ * rightTrans q χ f₂ + f₁ * leftInvOp q φ f₂ := by
  have h := conv_mul q φ χ hφ (coprod q f₁) (coprod q f₂)
  have hε : conv q (counit q).toLinearMap (coprod q f₁) = f₁ := by
    rw [← rightTrans_apply, rightTrans_counit]; rfl
  simp only [leftInvOp, LinearMap.comp_apply, AlgHom.toLinearMap_apply, map_mul] at h ⊢
  rw [h, hε, rightTrans_apply]

/-- The one-sided difference functional `(ε − χ)/c` is an `(ε, χ)`-twisted derivation. -/
theorem oneSided_twisted (χ : OqSU2 R q →ₐ[R] R) (cinv : R) (x y : OqSU2 R q) :
    (cinv • ((counit q).toLinearMap - χ.toLinearMap)) (x * y) =
      (cinv • ((counit q).toLinearMap - χ.toLinearMap)) x * χ y +
        counit q x * (cinv • ((counit q).toLinearMap - χ.toLinearMap)) y := by
  simp only [LinearMap.smul_apply, LinearMap.sub_apply, AlgHom.toLinearMap_apply, map_mul,
    smul_eq_mul]
  ring

theorem leftInvOp_sub_smul (χ₁ χ₂ : OqSU2 R q →ₐ[R] R) (cinv : R) (f : OqSU2 R q) :
    leftInvOp q (cinv • (χ₁.toLinearMap - χ₂.toLinearMap)) f =
      cinv • (rightTrans q χ₁ f - rightTrans q χ₂ f) := by
  simp only [rightTrans_apply, leftInvOp, LinearMap.comp_apply, AlgHom.toLinearMap_apply]
  induction coprod q f using TensorProduct.induction_on with
  | zero => simp
  | tmul x y => simp only [conv_tmul, LinearMap.smul_apply, LinearMap.sub_apply, AlgHom.toLinearMap_apply, smul_eq_mul, smul_sub, smul_smul]; exact sub_smul (cinv * χ₁ y) (cinv * χ₂ y) x
  | add S T hS hT => rw [map_add, map_add, map_add, hS, hT, ← smul_add]; congr 1; abel

/-- **The Cartan field built from the counit is a one-sided `q`-difference.** For the
diagonal character `χ_u`, the left-invariant field of `(ε − χ_u)/c` is
`f ↦ c⁻¹(f − R_u f)`, with `R_u = (α, β, γ, δ) ↦ (uα, u⁻¹β, uγ, u⁻¹δ)`, and it obeys
the one-sided Leibniz rule `X(f₁f₂) = Xf₁ · R_u f₂ + f₁ · Xf₂`. -/
theorem cartanField (u : Rˣ) (cinv : R) (f₁ f₂ : OqSU2 R q) :
    (∀ f, leftInvOp q (cinv • ((counit q).toLinearMap - (diagCharAlgHom q u).toLinearMap)) f =
        cinv • (f - torusScaleAlgHom q u u⁻¹ f)) ∧
    leftInvOp q (cinv • ((counit q).toLinearMap - (diagCharAlgHom q u).toLinearMap)) (f₁ * f₂) =
      leftInvOp q (cinv • ((counit q).toLinearMap - (diagCharAlgHom q u).toLinearMap)) f₁ *
          torusScaleAlgHom q u u⁻¹ f₂ +
        f₁ * leftInvOp q (cinv • ((counit q).toLinearMap -
          (diagCharAlgHom q u).toLinearMap)) f₂ := by
  refine ⟨fun f => ?_, ?_⟩
  · rw [leftInvOp_sub_smul, rightTrans_counit, rightTrans_diagChar]; rfl
  · rw [leftInvOp_leibniz q _ (diagCharAlgHom q u) (oneSided_twisted q _ cinv),
      rightTrans_diagChar]

end QOU.AlgebraicSubstrate.OqSU2
