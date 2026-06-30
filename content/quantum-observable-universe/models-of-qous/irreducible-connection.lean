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
# QOU.irreducible_connection

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/irreducible_connection.lean (monolithic)
-/

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Lemma (Irreducibility of the connection).**
    In a ℂ quantum observable universe, every instanton connection is
    irreducible, provided parallel adjoint sections embed into global ones.

    LaTeX: `\label{lem:irreducible-connection}`
    Proof: A parallel section `D_A s = 0` is in particular a global section
    of `Ad(P)`.  By injectivity of the embedding and the vanishing
    `H⁰(M, Ad(P)) = 0`, all parallel sections are equal — hence the
    connection is irreducible. -/
theorem irreducible_connection (cqou : CQuantumObservableUniverse)
    (inst : InstantonConnection cqou.toCRManifoldData)
    (embed : inst.parallelAdjointSections → cqou.adjointSections)
    (h_inj : Function.Injective embed) :
    inst.IsIrreducible :=
  ⟨fun a b => h_inj (cqou.adjoint_cohomology_vanishes.allEq _ _)⟩

end QOU
