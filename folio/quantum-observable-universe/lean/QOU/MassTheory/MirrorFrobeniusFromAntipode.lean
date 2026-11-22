import Mathlib.RingTheory.TensorProduct.Basic

/-!
# The mirror Frobenius relation follows from the antipode laws (symmetric case)

`FrobeniusHopfData` states one Frobenius relation, `Δ(ab) = Δ(a)·(1 ⊗ b)`. The left snake
identity for `λ = ε` (`CounitFrobeniusForm.counit_snake_left_of_mirror`) needs the mirror,
`Δ(ab) = (a ⊗ 1)·Δ(b)`, which is not an axiom.

`mirror_of_antipode` proves the mirror for an algebra `A` over a commutative ring with the
symmetric (flip) braiding on `A ⊗ A`, from:
* the stated relation,
* `S` reverses multiplication (`antipode_anti_mul`),
* `S` reverses comultiplication, `Δ ∘ S = flip ∘ (S ⊗ S) ∘ Δ` (`antipode_anti_comul`),
* `S ∘ S = id` (`antipode_involutive`).

Scope: this is the symmetric, element-level case (`Vect`-like). The braided, non-symmetric case
is not covered.
-/

namespace QOU.MassTheory.MirrorFrobeniusFromAntipode

open TensorProduct

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- `S ⊗ S` reverses products in `A ⊗ A` when `S` reverses products in `A`. -/
theorem map_anti_mul (S : A →ₗ[R] A) (hS : ∀ a b, S (a * b) = S b * S a) (X Y : A ⊗[R] A) :
    TensorProduct.map S S (X * Y) = TensorProduct.map S S Y * TensorProduct.map S S X := by
  induction X using TensorProduct.induction_on with
  | zero => simp
  | add X₁ X₂ h₁ h₂ => rw [add_mul, map_add, h₁, h₂, map_add, mul_add]
  | tmul a b =>
    induction Y using TensorProduct.induction_on with
    | zero => simp
    | add Y₁ Y₂ h₁ h₂ => rw [mul_add, map_add, h₁, h₂, map_add, add_mul]
    | tmul c d =>
      simp only [Algebra.TensorProduct.tmul_mul_tmul, TensorProduct.map_tmul, hS]

/-- **The mirror Frobenius relation from the antipode laws.** -/
theorem mirror_of_antipode (Δ : A →ₗ[R] A ⊗[R] A) (S : A →ₗ[R] A)
    (hFrob : ∀ a b, Δ (a * b) = Δ a * (1 ⊗ₜ b))
    (hS : ∀ a b, S (a * b) = S b * S a)
    (hSΔ : ∀ a, Δ (S a) = Algebra.TensorProduct.comm R A A (TensorProduct.map S S (Δ a)))
    (hSS : ∀ a, S (S a) = a) (a b : A) :
    Δ (a * b) = (a ⊗ₜ 1) * Δ b := by
  have hab : a * b = S (S b * S a) := by rw [hS, hSS, hSS]
  have hS1 : S 1 = 1 := by
    have h := hS 1 (S 1)
    rw [one_mul, hSS, one_mul] at h
    exact h.symm
  rw [hab, hSΔ, hFrob, map_anti_mul S hS, TensorProduct.map_tmul, hS1, hSS, map_mul,
    Algebra.TensorProduct.comm_tmul, ← hSΔ, hSS]

end QOU.MassTheory.MirrorFrobeniusFromAntipode
