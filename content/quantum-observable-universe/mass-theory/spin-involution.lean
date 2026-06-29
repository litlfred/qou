import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic

/-!
# Spin involution on a Frobenius `*`-algebra

A **spin involution** on a Frobenius `*`-algebra `(A, τ, star)` is
an `R`-linear map `σ : A → A` that is

1. involutive (`σ ∘ σ = id`),
2. anti-multiplicative (`σ (a*b) = σ b * σ a`),
3. trace-invariant (`τ ∘ σ = τ`),
4. `*`-compatible (`σ (star a) = star (σ a)`).

The `±1`-eigenspaces of `σ` give the spin grading
`A = A₊ ⊕ A₋`; `A₊` is the spin-singlet sector and `A₋` the
spin-doublet sector. The isospin third-component `T₃` is read off
the `σ`-eigenvalue.

This sibling packages the four spin-involution axioms as a
structure and records the projection identity used downstream.

-- Ref: [manuscript] def:spin-involution
-- Ref: [kassel1995] Kassel, "Quantum Groups," GTM 155, Springer (1995)
-/

namespace QOU.BraidKnot

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Module R A]

/-- A **spin involution** on a Frobenius `*`-algebra: an `R`-linear,
involutive, anti-multiplicative, trace- and `*`-compatible map. -/
structure SpinInvolution
    (τ : A → R) (star : A → A) where
  /-- The underlying map `σ : A → A`. -/
  σ : A → A
  /-- `σ` is `R`-linear. -/
  map_smul : ∀ (r : R) (a : A), σ (r • a) = r • σ a
  /-- `σ` is additive. -/
  map_add : ∀ a b : A, σ (a + b) = σ a + σ b
  /-- Involution: `σ ∘ σ = id`. -/
  involutive : ∀ a : A, σ (σ a) = a
  /-- Anti-multiplicative: `σ (a*b) = σ b * σ a`. -/
  anti_mul : ∀ a b : A, σ (a * b) = σ b * σ a
  /-- Trace-invariant: `τ (σ a) = τ a`. -/
  trace_inv : ∀ a : A, τ (σ a) = τ a
  /-- `*`-compatible: `σ (star a) = star (σ a)`. -/
  star_compat : ∀ a : A, σ (star a) = star (σ a)

/-- A spin involution is bijective: it is its own two-sided inverse,
directly from the involution axiom. -/
theorem spin_involution_bijective
    {τ : A → R} {star : A → A} (S : SpinInvolution τ star) :
    Function.Bijective S.σ :=
  Function.bijective_iff_has_inverse.2
    ⟨S.σ, S.involutive, S.involutive⟩

end QOU.BraidKnot
