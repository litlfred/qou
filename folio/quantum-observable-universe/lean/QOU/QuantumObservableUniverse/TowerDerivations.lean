/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.QuantumObservableUniverse.TwistedFrobeniusTower

/-!
# Deriving the tower maps from the trace, and twist compatibility

`TwistedFrobeniusTower.lean` takes the conditional expectation `E n` as data. Here it is
derived. Call `E` *adjoint to `ι`* when

  `τ n (x * E y) = τ (n+1) (ι n x * y)` for all `x : A n`, `y : A (n+1)`.

Over any commutative ring, assuming `τ n` is nondegenerate (`hnd`):

* `adjoint_unique`: at most one `E` is adjoint to `ι`. So `E` is determined by `τ` and
  `ι`, and is not a choice. Existence needs finite rank and is not proved here; for the
  Hecke tower it is Ocneanu's relative trace.
* `adjoint_iota`: if `τ (n+1) ∘ ι = τ n`, the adjoint satisfies `E (ι a) = a`.
* `adjoint_left_linear`: `E (ι a * y) = a * E y`.
* `adjoint_trace`: `τ n (E y) = τ (n+1) y`.

So three of the four hypotheses of the tower file are consequences of adjointness. The
fourth, right linearity `E (y * ι b) = E y * b`, is kept as a hypothesis; Kadison's
Frobenius extensions have it.

* `nakayama_compat`: if both levels carry Nakayama twists and `τ (n+1)` is nondegenerate,
  then `ν (n+1) (ι a) = ι (ν n a)`. The twists are compatible along the tower; this is
  derived, not assumed.

Two further statements from the charge discussion:

* `commuting_op_same_eigenvalue` (Schur–Weyl blindness): an operator `T` commuting with
  a map `F` takes the same eigenvalue on `v` and on `F v`. A braid operator commutes
  with the quantum-group lowering map, so it gives every state of an isospin multiplet
  the same eigenvalue.
* `normalized_ratio_rescale`: a ratio `τ x / τ y` does not change when `τ` is rescaled
  by a unit, so an overall factor such as `q₀⁻³` cancels from normalized expectations.

No `sorry`.

## References
- [leitner2026] §1 Categorical foundations.
-/

namespace QOU.QuantumObservableUniverse.TowerDerivations

variable {R : Type*} [CommRing R]
variable {A : ℕ → Type*} [∀ n, Ring (A n)] [∀ n, Algebra R (A n)]
variable (τ : ∀ n, A n →ₗ[R] R) (ι : ∀ n, A n →ₐ[R] A (n + 1))

/-- `E` is adjoint to `ι` for the forms `τ`. -/
def IsAdjoint (n : ℕ) (E : A (n + 1) → A n) : Prop :=
  ∀ (x : A n) (y : A (n + 1)), τ n (x * E y) = τ (n + 1) (ι n x * y)

/-- The adjoint of `ι` is unique when `τ n` is nondegenerate. -/
theorem adjoint_unique (n : ℕ) (hnd : ∀ z : A n, (∀ x, τ n (x * z) = 0) → z = 0)
    (E E' : A (n + 1) → A n) (h : IsAdjoint τ ι n E) (h' : IsAdjoint τ ι n E')
    (y : A (n + 1)) : E y = E' y := by
  rw [← sub_eq_zero]
  apply hnd
  intro x
  rw [mul_sub, map_sub, h, h', sub_self]

/-- The adjoint is a left inverse of `ι`, given `τ (n+1) ∘ ι = τ n`. -/
theorem adjoint_iota (n : ℕ) (hnd : ∀ z : A n, (∀ x, τ n (x * z) = 0) → z = 0)
    (hτι : ∀ a, τ (n + 1) (ι n a) = τ n a) (E : A (n + 1) → A n)
    (h : IsAdjoint τ ι n E) (a : A n) : E (ι n a) = a := by
  rw [← sub_eq_zero]
  apply hnd
  intro x
  rw [mul_sub, map_sub, h, ← map_mul, hτι, sub_self]

/-- The adjoint is left `A n`-linear. -/
theorem adjoint_left_linear (n : ℕ) (hnd : ∀ z : A n, (∀ x, τ n (x * z) = 0) → z = 0)
    (E : A (n + 1) → A n) (h : IsAdjoint τ ι n E) (a : A n) (y : A (n + 1)) :
    E (ι n a * y) = a * E y := by
  rw [← sub_eq_zero]
  apply hnd
  intro x
  rw [mul_sub, map_sub, h, ← mul_assoc, ← mul_assoc, h, ← map_mul (ι n) x a, sub_self]

/-- The adjoint preserves the trace. -/
theorem adjoint_trace (n : ℕ) (E : A (n + 1) → A n) (h : IsAdjoint τ ι n E)
    (y : A (n + 1)) : τ n (E y) = τ (n + 1) y := by
  have := h 1 y
  rwa [one_mul, map_one, one_mul] at this

/-- **Twist compatibility.** The Nakayama twists commute with the inclusion. -/
theorem nakayama_compat (n : ℕ) (ν : ∀ n, A n ≃ₐ[R] A n)
    (hν : ∀ n (a b : A n), τ n (a * b) = τ n (b * ν n a))
    (hnd : ∀ z : A n, (∀ x, τ n (x * z) = 0) → z = 0)
    (hnd' : ∀ z : A (n + 1), (∀ x, τ (n + 1) (x * z) = 0) → z = 0)
    (E : A (n + 1) → A n) (h : IsAdjoint τ ι n E)
    (hright : ∀ y b, E (y * ι n b) = E y * b) (a : A n) :
    ν (n + 1) (ι n a) = ι n (ν n a) := by
  rw [← sub_eq_zero]
  apply hnd'
  intro y
  rw [mul_sub, map_sub, sub_eq_zero, ← hν (n + 1) (ι n a) y,
    ← adjoint_trace τ ι n E h, adjoint_left_linear τ ι n hnd E h, hν n a (E y),
    ← hright, adjoint_trace τ ι n E h]

/-- **Schur–Weyl blindness.** An operator commuting with `F` has the same eigenvalue
on `v` and on `F v`. -/
theorem commuting_op_same_eigenvalue {M : Type*} [AddCommGroup M] [Module R M]
    (T F : M →ₗ[R] M) (hTF : ∀ m, T (F m) = F (T m)) (c : R) (v : M) (hv : T v = c • v) :
    T (F v) = c • F v := by
  rw [hTF, hv, map_smul]

/-- A normalized ratio is unchanged by rescaling the form by a unit. -/
theorem normalized_ratio_rescale {K : Type*} [Field K] (c a b : K) (hc : c ≠ 0) :
    (c * a) / (c * b) = a / b := by
  rw [mul_div_mul_left a b hc]

end QOU.QuantumObservableUniverse.TowerDerivations
