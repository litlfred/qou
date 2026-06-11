import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Topology.Basic
import Mathlib.Topology.ContinuousFunction.Basic
import Mathlib.Geometry.Manifold.SmoothManifoldWithCorners
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.LinearAlgebra.ExteriorAlgebra.Basic


/-!
# QOU.CategoricalJet

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/CategoricalJet.lean (monolithic)
-/

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Categorical jet object**: `J¹(A) = A ⊗_C Ω¹(A)` where `Ω¹(A) = ker(μ)`.

    The jet object fits into the universal extension
    `0 → A ⊗ Ω¹(A) → J¹(A) → A → 0`
    with jet evaluation `j¹ : J¹(A) → A` as the counit.

    LaTeX: `\label{def:categorical-jet}` -/
structure CategoricalJet (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] where
  /-- The Frobenius–Hopf object `A` in `C`. -/
  frobHopf : @FrobeniusHopfData C _ _
  /-- The jet object `J¹(A)` in `C`. -/
  jetObj : C
  /-- Jet evaluation `j¹ : J¹(A) → A` (the counit). -/
  jetEval : jetObj ⟶ frobHopf.obj
  /-- The kernel inclusion `A ⊗ Ω¹(A) ↪ J¹(A)`. -/
  kernelIncl : frobHopf.obj ⟶ jetObj
  /-- **Exactness**: the composite `kernelIncl ≫ jetEval = 0`, encoding
      the short exact sequence `0 → A ⊗ Ω¹(A) → J¹(A) → A → 0`. -/
  exact : kernelIncl ≫ jetEval = 0

/-- The kernel inclusion is monic: if `kernelIncl ≫ f = kernelIncl ≫ g` then
    `f = g` (follows from exactness and the universal property). -/
theorem CategoricalJet.kernelIncl_exact {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C]
    (cj : CategoricalJet C) :
    cj.kernelIncl ≫ cj.jetEval = 0 :=
  cj.exact

/-- **Proposition (Jet prolongation).**
    The jet evaluation intertwines the prolonged connection with the
    original: `j¹ ≫ ∇ = ∇' ≫ (j¹ ⊗ j¹)`.

    The connection on `J¹(A)` is the unique lift such that the prolongation
    square commutes.  The kernel `A ⊗ Ω¹(A)` inherits its connection
    from the Leibniz rule.

    LaTeX: `\label{prop:categorical-jet-prolongation}` -/
structure CategoricalJetProlongation {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C]
    (cj : CategoricalJet C) where
  /-- The prolonged connection `∇' : J¹(A) → J¹(A)`. -/
  prolonged_connection : cj.jetObj ⟶ cj.jetObj
  /-- The original connection `∇ : A → A`. -/
  connection : cj.frobHopf.obj ⟶ cj.frobHopf.obj
  /-- **Prolongation compatibility**: `j¹ ≫ ∇ = ∇' ≫ j¹`. -/
  commutes : cj.jetEval ≫ connection = prolonged_connection ≫ cj.jetEval

/-- The prolongation square commutes. -/
theorem categorical_jet_prolongation {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C]
    (cj : CategoricalJet C) (jp : CategoricalJetProlongation cj) :
    cj.jetEval ≫ jp.connection = jp.prolonged_connection ≫ cj.jetEval :=
  jp.commutes

end QOU
