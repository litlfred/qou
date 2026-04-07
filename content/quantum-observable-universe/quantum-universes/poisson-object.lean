/-!
# QOU.PoissonObject

Internal Poisson object in a monoidal category equipped with
Frobenius–Hopf data and a differential calculus.

The Poisson bivector `π : 𝟙 → Λ²(Ω¹(A)∨)` is pulled back through
the Frobenius self-duality `A ≅ A∨` to define the bracket internally.

LaTeX: `\label{def:poisson-object}`
Ref: [kock2004]
-/

import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Basic
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Internal Poisson object** in a monoidal category.

    Given Frobenius–Hopf data `(A, μ, η, Δ, ε, S, λ)` and a
    differential calculus `(Ω¹, ∇)`, a Poisson object consists of a
    bivector object `Π` (representing `Λ²(Ω¹(A)∨)`) and a global
    section `π : 𝟙 → Π` satisfying the internal Jacobi identity.

    The bracket is defined by the pullback composite:
      `{f, g} := ⟨π, df ∧ dg⟩`
    where the contraction uses the Frobenius isomorphism `A ≅ A∨`
    to identify `Ω¹(A)∨ ≅ Ω¹(A)`.

    LaTeX: `\label{def:poisson-object}`
    Ref: [kock2004] -/
structure PoissonObject (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C)
    (conn : CategoricalConnection C fh) where
  /-- The bivector object `Π = Λ²(Ω¹(A)∨)` in `C`.
      Under Frobenius self-duality this is isomorphic to `Ω²(A)`. -/
  bivectorObj : C
  /-- The Poisson bivector `π : 𝟙 → Π` (a global section). -/
  bivector : (𝟙_ C) ⟶ bivectorObj
  /-- The bracket morphism `{–, –} : A ⊗ A → A` obtained by
      contracting `π` against differentials.  This is the composite
      `A ⊗ A →[d ⊗ d] Ω¹ ⊗ Ω¹ →[∧] Ω² →[⟨π, –⟩] A`. -/
  bracket : (fh.obj ⊗ fh.obj) ⟶ fh.obj
  /-- **Anti-symmetry**: `{f, g} = -{g, f}`, encoded as
      `bracket ∘ σ = -bracket` where `σ` is the braiding.
      In a general monoidal category without additive structure,
      stated as: the bracket factors through `Λ²`. -/
  -- Ref: [kock2004]
  antisym : sorry
  /-- **Jacobi identity**: the Jacobiator vanishes.
      `{f, {g, h}} + {g, {h, f}} + {h, {f, g}} = 0`. -/
  -- Ref: [kock2004]
  jacobi : sorry
  /-- **Leibniz rule**: the bracket is a biderivation w.r.t. `μ`.
      `{f, g·h} = {f,g}·h + g·{f,h}`. -/
  -- Ref: [kock2004]
  leibniz : sorry

end QOU
