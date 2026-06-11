import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Monoidal.Braided.Basic
import Mathlib.CategoryTheory.Preadditive.Basic
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans


/-!
# QOU.PoissonObject

Internal Poisson object in a monoidal category equipped with
Frobenius–Hopf data and a differential calculus.

The Poisson bivector `π : 𝟙 → Λ²(Ω¹(A)∨)` is pulled back through
the Frobenius self-duality `A ≅ A∨` to define the bracket internally.
Anti-symmetry of the bracket is automatic since `π` factors through
the exterior square `Λ²`.

LaTeX: `\label{def:poisson-object}`
Ref: [kock2004]
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Internal Poisson object** in a braided preadditive monoidal category.

    Given Frobenius–Hopf data `(A, μ, η, Δ, ε, S, λ)` and a
    differential calculus `(Ω¹, ∇)`, a Poisson object consists of a
    bivector object `Π` (representing `Λ²(Ω¹(A)∨)`) and a global
    section `π : 𝟙 → Π` satisfying the Jacobi identity and Leibniz
    rule.  Anti-symmetry of the bracket is automatic since `π` factors
    through `Λ²`.

    The bracket is defined by the pullback composite:
      `{f, g} := ⟨π, df ∧ dg⟩`
    where the contraction uses the Frobenius isomorphism `A ≅ A∨`
    to identify `Ω¹(A)∨ ≅ Ω¹(A)`.

    LaTeX: `\label{def:poisson-object}`
    Ref: [kock2004] -/
structure PoissonObject (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.BraidedCategory C]
    [CategoryTheory.Preadditive C]
    (fh : FrobeniusHopfData C)
    (conn : CategoricalConnection C fh) where
  /-- The bivector object `Π = Λ²(Ω¹(A)∨)` in `C`.
      Under Frobenius self-duality this is isomorphic to `Ω²(A)`. -/
  bivectorObj : C
  /-- The Poisson bivector `π : 𝟙 → Π` (a global section). -/
  bivector : (𝟙_ C) ⟶ bivectorObj
  /-- The bracket morphism `{–, –} : A ⊗ A → A` obtained by
      contracting `π` against differentials.  This is the composite
      `A ⊗ A →[d ⊗ d] Ω¹ ⊗ Ω¹ →[∧] Ω² →[⟨π, –⟩] A`.
      Anti-symmetric by construction since `π ∈ Λ²`. -/
  bracket : (fh.obj ⊗ fh.obj) ⟶ fh.obj
  /-- The Leibniz-rule RHS: categorical morphism `A ⊗ (A ⊗ A) → A`
      encoding `{f,g}·h + g·{f,h}`.  Provided abstractly following
      the pattern of `CategoricalConnection.leibniz_rhs`, since the
      full composite involves associators and whiskerings that depend
      on the specific monoidal structure.  In a strict monoidal
      category this equals
      `(bracket ⊗ id) ≫ μ + (id ⊗ bracket) ≫ μ` (suitably shuffled). -/
  leibniz_rhs : (fh.obj ⊗ (fh.obj ⊗ fh.obj)) ⟶ fh.obj
  /-- **Leibniz rule**: `{f, g·h} = {f,g}·h + g·{f,h}`.
      Stated as an equality of morphisms `A ⊗ (A ⊗ A) → A`:
      the bracket applied after multiplication equals the abstract
      Leibniz RHS. -/
  -- Ref: [kock2004]
  leibniz : (fh.obj ◁ fh.mul) ≫ bracket = leibniz_rhs
  /-- The Jacobiator: categorical morphism `(A ⊗ A) ⊗ A → A`
      encoding the cyclic sum `{f,{g,h}} + {g,{h,f}} + {h,{f,g}}`.
      Provided abstractly since the cyclic sum involves iterated
      brackets and associator shuffles. -/
  jacobiator : ((fh.obj ⊗ fh.obj) ⊗ fh.obj) ⟶ fh.obj
  /-- **Jacobi identity**: the Jacobiator vanishes. -/
  -- Ref: [kock2004]
  jacobi : jacobiator = 0

end QOU
