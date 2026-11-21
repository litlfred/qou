import Mathlib.LinearAlgebra.TensorProduct.Associator
import Mathlib.Algebra.Algebra.Bilinear
import Mathlib.RingTheory.TensorProduct.Basic

/-!
# QOU.frobenius_relation — the Frobenius relation

**Proposition** ([`prop:frobenius-relation`](../../../quantum-observable-universe/quantum-universes/frobenius-relation.md)).

For an algebra `A` with Frobenius form `ε` and copairing `γ ∈ A ⊗ A`
(snake identity `∑ ε(a γ'ᵢ) γ''ᵢ = a`), the comultiplication
`Δ_μ = (μ ⊗ id) ∘ (id ⊗ γ)` satisfies

    (μ ⊗ id) ∘ (id ⊗ Δ_μ) = Δ_μ ∘ μ        as maps `A ⊗ A → A ⊗ A`.

-- Ref: [leitner2026] quantum-observable-universe/quantum-universes/frobenius-relation.md
-- Ref: [kock2004] Frobenius algebras and 2D TQFTs, §2.3
-/

open TensorProduct

namespace QOU

/-- Frobenius data on an `R`-algebra `A`: a form `ε : A → R` and a copairing
`γ ∈ A ⊗ A` satisfying the snake identity `∑ ε(a γ'ᵢ) γ''ᵢ = a`, i.e. `γ` is
the copairing of the non-degenerate pairing `⟨a, b⟩ = ε(a b)`. -/
class FrobeniusCopairingData (R : Type*) [CommRing R] (A : Type*) [Ring A]
    [Algebra R A] where
  /-- The Frobenius form `∫_A`. -/
  ε : A →ₗ[R] R
  /-- The copairing `γ = ∑ γ'ᵢ ⊗ γ''ᵢ`. -/
  γ : A ⊗[R] A
  /-- Snake identity: `∑ ⟨a, γ'ᵢ⟩ γ''ᵢ = a`. -/
  snake : ∀ a : A,
    TensorProduct.lid R A (LinearMap.rTensor A (ε ∘ₗ LinearMap.mulLeft R a) γ) = a

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- The comultiplication `Δ_μ = (μ ⊗ id) ∘ (id ⊗ γ)`, i.e.
`Δ_μ(b) = ∑ μ(b ⊗ γ'ᵢ) ⊗ γ''ᵢ`. -/
noncomputable def frobeniusComul [F : FrobeniusCopairingData R A] :
    A →ₗ[R] A ⊗[R] A :=
  LinearMap.rTensor A (LinearMap.mul' R A) ∘ₗ
    (TensorProduct.assoc R A A A).symm.toLinearMap ∘ₗ
    (TensorProduct.mk R A (A ⊗[R] A)).flip F.γ

/-- **Frobenius relation** ([`prop:frobenius-relation`]).

`(μ ⊗ id) ∘ (id ⊗ Δ_μ) = Δ_μ ∘ μ` as `R`-linear maps `A ⊗ A → A ⊗ A`.

The proof is associativity of `μ`, checked on pure tensors and on the
summands of `γ`. It uses only the copairing form of `Δ_μ`. The snake identity
is what makes this `Δ_μ` the transpose of `μ` under the pairing
`⟨a, b⟩ = ε(a b)`; that equivalence of the two descriptions of the
comultiplication is standard [kock2004, §2.3] and is cited, not formalised.

Until 2026-11-21 this theorem was stated over a context of bare types and
functions with no axioms, first proved by projecting a field that was the
conclusion, then left as a `sorry` (round-trip audit pass 2, C09; QA on
#8888). -/
theorem frobenius_relation [F : FrobeniusCopairingData R A] :
    LinearMap.rTensor A (LinearMap.mul' R A) ∘ₗ
        (TensorProduct.assoc R A A A).symm.toLinearMap ∘ₗ
        LinearMap.lTensor A (frobeniusComul (R := R) (A := A))
      = frobeniusComul (R := R) (A := A) ∘ₗ LinearMap.mul' R A := by
  apply TensorProduct.ext'
  intro a b
  simp only [LinearMap.comp_apply, LinearMap.lTensor_tmul, frobeniusComul,
    LinearEquiv.coe_coe, LinearMap.mul'_apply, LinearMap.flip_apply,
    TensorProduct.mk_apply]
  induction F.γ using TensorProduct.induction_on with
  | zero => simp
  | tmul x y => simp [mul_assoc]
  | add x y hx hy => simp_all [TensorProduct.tmul_add]

end QOU
