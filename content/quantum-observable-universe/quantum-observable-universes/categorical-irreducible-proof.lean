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
# QOU.categorical_irreducible

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/categorical_irreducible.lean (monolithic)
-/

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Lemma (Irreducibility from observability).**
    In a quantum observable universe, any categorical instanton is
    irreducible: `Hom_C(𝟙, Ad(A)) = 0`.

    Proof: a non-zero invariant `s : 𝟙 → Ad(A)` would satisfy `λ ∘ s = 0`
    (trace-free), contradicting non-degeneracy of the Frobenius form.

    LaTeX: `\label{lem:categorical-irreducible}` -/
theorem categorical_irreducible {k : Type*} [Field k]
    (qou : QuantumObservableUniverse.{u, v} k)
    (inst : @CategoricalInstanton _ qou.catInst qou.monInst qou.frobHopf) :
    -- Irreducibility is encoded by the adjoint vanishing axiom of QOU.
    Subsingleton ((𝟙_ _) ⟶ qou.adjointObj) :=
  qou.adjoint_vanishing

end QOU
