/-!
# QOU.FrobeniusHopf — Frobenius–Hopf Algebra Structure

Formalisation stubs for the Frobenius–Hopf algebra structure used in
*Quantum Observable Universe*, Chapter 1.

## Mathlib4 references
- `Mathlib.RingTheory.HopfAlgebra`        (Hopf algebras)
- `Mathlib.LinearAlgebra.TensorProduct`    (monoidal structure on Vect)
- `Mathlib.Algebra.Lie.Basic`              (Lie algebra structure)
- `Mathlib.Algebra.DirectLimit`            (direct limits of algebras)

## Paper references
- Remark 1.14  `rem:frobenius-simplification`
  In a Frobenius category the QOU 5-tuple reduces to a triple `(M, θ, A)`.
- Definition 2.4  `def:direct-limit-algebra`
  The ℂ QOU as a direct limit `𝒜_∞ = lim 𝒜_n`.
-/

universe u

/-- A Frobenius algebra object in a monoidal category (placeholder).
    A Frobenius algebra is simultaneously an algebra and a coalgebra
    satisfying the Frobenius relation: `(μ ⊗ id) ∘ (id ⊗ Δ) = Δ ∘ μ`.

    Mathlib closest: `Mathlib.RingTheory.HopfAlgebra` (Hopf part).
    Full Frobenius formalisation is an open Mathlib project.

    Paper: diagrams `eq:frobenius-relation`, `eq:frobenius-nondegen`,
    `eq:frobenius-vanishing` in Chapter 1. -/
class FrobeniusAlgebra (A : Type u) where
  mul   : A → A → A
  unit  : A
  comul : A → A × A    -- placeholder for `A → A ⊗ A`
  counit : A → Nat      -- placeholder for `A → k`
  frobenius_relation : True  -- `(μ ⊗ id) ∘ (id ⊗ Δ) = Δ ∘ μ`

/-- A Hopf algebra object (placeholder).
    Extends `FrobeniusAlgebra` with an antipode `S : A → A`.

    Mathlib: `Mathlib.RingTheory.HopfAlgebra`. -/
class HopfAlgebra (A : Type u) extends FrobeniusAlgebra A where
  antipode : A → A
  antipode_left  : True  -- `S ⋆ id = η ∘ ε`
  antipode_right : True  -- `id ⋆ S = η ∘ ε`

/-- **Frobenius non-degeneracy** `eq:frobenius-nondegen`
    The Frobenius form `ε ∘ μ : A ⊗ A → k` is non-degenerate.

    Paper: diagram `eq:frobenius-nondegen` in Chapter 1. -/
def FrobeniusAlgebra.nondegenerate (_A : Type u) [FrobeniusAlgebra _A] : Prop :=
  True  -- placeholder

/-- **Definition 2.4** (Direct-limit algebra) `def:direct-limit-algebra`
    `𝒜_∞ = lim_→ 𝒜_n` built from the recursive brane tower.

    Mathlib: `Mathlib.Algebra.DirectLimit`. -/
axiom DirectLimitAlgebra : Type u
