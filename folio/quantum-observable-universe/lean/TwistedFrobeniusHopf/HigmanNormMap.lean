/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.RingTheory.TensorProduct.Basic

/-!
# The Higman norm map of a Casimir element

Let `C = Σᵢ eᵢ ⊗ fᵢ ∈ A ⊗ A` be a Casimir element of an `R`-algebra `A`, meaning

* `casimir_left`:  `Σ a eᵢ ⊗ fᵢ = Σ eᵢ ⊗ fᵢ a` for all `a`, and
* `casimir_mid`:   `Σ eᵢ ⊗ a fᵢ = Σ eᵢ a ⊗ fᵢ` for all `a`.

For a symmetric Frobenius algebra with dual bases `eᵢ, fᵢ` both hold; this file takes them
as hypotheses and does not derive them from the form. The Higman norm map
`N(x) = Σᵢ eᵢ x fᵢ` [higman1955] then satisfies, over any commutative ring `R`:

* `norm_central_of_casimir`: `N(x)` is central;
* `norm_comm_of_casimir`: `N(x y) = N(y x)`, so `N` kills commutators and factors through
  `A / [A, A]`.

On `H_n(q)` with its symmetrising trace, `N` acts on the block of `λ` through the Schur
element (Geck–Pfeiffer §7.2); that block-level statement is not formalised here.

No `sorry`.

## References
- [higman1955] Higman's trace map.
- [geckpfeiffer2000] §7.2, Schur elements.
-/

namespace QOU.QuantumObservableUniverse.Higman

open TensorProduct

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- The sandwich map `u ⊗ v ↦ u x v`. -/
noncomputable def sandwich (x : A) : A ⊗[R] A →ₗ[R] A :=
  TensorProduct.lift (LinearMap.mk₂ R (fun u v => u * x * v)
    (fun u u' v => by simp [add_mul]) (fun c u v => by simp [smul_mul_assoc])
    (fun u v v' => by simp [mul_add]) (fun c u v => by simp [mul_smul_comm]))

theorem sandwich_tmul (x u v : A) : sandwich (R := R) x (u ⊗ₜ v) = u * x * v := by
  simp [sandwich]

variable {ι : Type*} (s : Finset ι) (e f : ι → A)

/-- The Higman norm map `N(x) = Σ eᵢ x fᵢ`. -/
def norm (x : A) : A := ∑ i ∈ s, e i * x * f i

theorem norm_eq_sandwich (x : A) :
    norm s e f x = sandwich (R := R) x (∑ i ∈ s, e i ⊗ₜ[R] f i) := by
  simp [norm, map_sum, sandwich_tmul]

theorem norm_central_of_casimir
    (hleft : ∀ a : A, ∑ i ∈ s, (a * e i) ⊗ₜ[R] f i = ∑ i ∈ s, e i ⊗ₜ[R] (f i * a))
    (x a : A) : a * norm s e f x = norm s e f x * a := by
  have h := congrArg (sandwich (R := R) x) (hleft a)
  simp only [map_sum, sandwich_tmul] at h
  simp only [norm, Finset.mul_sum, Finset.sum_mul, mul_assoc] at h ⊢
  exact h

theorem norm_comm_of_casimir
    (hmid : ∀ a : A, ∑ i ∈ s, e i ⊗ₜ[R] (a * f i) = ∑ i ∈ s, (e i * a) ⊗ₜ[R] f i)
    (x y : A) : norm s e f (x * y) = norm s e f (y * x) := by
  have h := congrArg (sandwich (R := R) x) (hmid y)
  simp only [map_sum, sandwich_tmul] at h
  simp only [norm, mul_assoc] at h ⊢
  exact h

end QOU.QuantumObservableUniverse.Higman
