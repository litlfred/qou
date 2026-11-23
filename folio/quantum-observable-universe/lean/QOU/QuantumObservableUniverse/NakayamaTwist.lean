/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.Algebra.Equiv
import Mathlib.LinearAlgebra.Dual.Defs

/-!
# Nakayama-twisted Frobenius pairings and the bar involution

Let `τ : A →ₗ[R] R` be a nondegenerate form on an `R`-algebra `A` with Nakayama
automorphism `ν`, i.e. `τ (a * b) = τ (b * ν a)`. This file proves, over any commutative
ring `R`:

* `tau_nu`: `τ ∘ ν = τ`;
* `frobMap`: `a ↦ (x ↦ τ (x * a))`, injective (`frobMap_injective`), with
  `frobMap_mul_left`: `φ (b * a) x = φ a (x * b)` and
  `frobMap_mul_nu`: `φ (a * ν b) x = φ a (b * x)`.
  So `φ` identifies the twisted bimodule `₁A_ν` with the dual `A^∨`: the left and right
  dual actions match after twisting one side by `ν`. This is the algebraic content of
  the twisted ambidextrous adjunction `Ind ⊣ Res ⊣ Ind_ν`; when `ν = id` it is untwisted.
* `nu_dag`: if a semilinear anti-involution `‡` satisfies `τ (a‡) = σ (τ a)` for a ring
  automorphism `σ` of `R` (for example `q ↦ q⁻¹`), then `ν (a‡) = (ν⁻¹ a)‡`. This is a
  theorem, not an extra axiom: it follows from nondegeneracy.

A worked example of a nontrivial `ν` is Sweedler's algebra
(`QOU.LiftingDescent.Sweedler.frob_mul_eq_frob_mul_nakayama`).

No `sorry`.

## References
- [lorenz2011] Nakayama automorphism of a Frobenius algebra.
- [leitner2026] §1 Categorical foundations.
-/

namespace QOU.QuantumObservableUniverse.Nakayama

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]
variable (τ : A →ₗ[R] R) (ν : A ≃ₐ[R] A)
variable (hν : ∀ a b : A, τ (a * b) = τ (b * ν a))

include hν in
/-- The form is `ν`-invariant. -/
theorem tau_nu (a : A) : τ (ν a) = τ a := by
  have h := hν a 1
  rw [one_mul, mul_one] at h
  exact h.symm

/-- The Frobenius map `a ↦ (x ↦ τ (x * a))`. -/
def frobMap (a : A) : A → R := fun x => τ (x * a)

include hν in
/-- Right multiplication becomes the twisted left dual action. -/
theorem frobMap_mul_nu (a b x : A) : frobMap τ (a * ν b) x = frobMap τ a (b * x) := by
  simp only [frobMap]
  rw [← mul_assoc, ← hν b (x * a), mul_assoc]

/-- Left multiplication becomes the right dual action. -/
theorem frobMap_mul_left (a b x : A) : frobMap τ (b * a) x = frobMap τ a (x * b) := by
  simp only [frobMap, mul_assoc]

/-- Nondegeneracy (right radical zero) makes the Frobenius map injective. -/
theorem frobMap_injective (hnd : ∀ y : A, (∀ x, τ (x * y) = 0) → y = 0) :
    Function.Injective (frobMap τ) := by
  intro a b h
  rw [← sub_eq_zero]
  apply hnd
  intro x
  have hx := congrFun h x
  simp only [frobMap] at hx
  rw [mul_sub, map_sub, hx, sub_self]

include hν in
/-- **Bar compatibility.** If `‡` is an anti-multiplicative surjection with
`τ (a‡) = σ (τ a)`, and `τ` is nondegenerate, then `ν (a‡) = (ν⁻¹ a)‡`. -/
theorem nu_dag (σ : R →+* R) (dag : A → A) (hsurj : Function.Surjective dag)
    (hdag_mul : ∀ a b, dag (a * b) = dag b * dag a)
    (htr : ∀ a, τ (dag a) = σ (τ a))
    (hnd : ∀ y : A, (∀ x, τ (x * y) = 0) → y = 0) (a : A) :
    ν (dag a) = dag (ν.symm a) := by
  rw [← sub_eq_zero]
  apply hnd
  intro x
  obtain ⟨y, rfl⟩ := hsurj x
  rw [mul_sub, map_sub, sub_eq_zero, ← hν (dag a) (dag y), ← hdag_mul, htr, ← hdag_mul,
    htr, hν (ν.symm a) y, AlgEquiv.apply_symm_apply]

end QOU.QuantumObservableUniverse.Nakayama
