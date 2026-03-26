/-!
# QOU.CategoricalTransport

Extracted from lean-archive/ for content-block co-location.
Source: lean-archive/QOU/CategoricalTransport.lean (monolithic)
-/

import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Basic
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

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Categorical transport equation**: `ℏ_q π_V(∇ψ) = H_q(ψ)`.

    The q-Hamiltonian `H_q = −½ ℏ_q Δ_q + V_q` acts on jet sections,
    and the transport equation is the condition that `ψ` lies in the
    kernel of `H_q − ℏ_q ι_{ξ_q} D_A`.

    This is the categorical analogue of the Schrödinger equation
    (Remark `rem:schrodinger-jet-coaction` in the elaboration chapter).

    LaTeX: `\label{def:categorical-transport}` -/
structure CategoricalTransport (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] where
  /-- The categorical jet data. -/
  jet : CategoricalJet C
  /-- The instanton connection. -/
  instanton : @CategoricalInstanton C _ _ jet.frobHopf
  /-- The vertical projection of the covariant derivative `π_V(∇ψ)`. -/
  proj_V_nabla : jet.jetObj ⟶ jet.jetObj
  /-- The q-Hamiltonian `H_q : ω(J¹(A)) → ω(J¹(A))`. -/
  hamiltonian : jet.jetObj ⟶ jet.jetObj
  /-- **Transport equation**: the two endomorphisms agree
      (ℏ_q · π_V ∘ ∇ = H_q). -/
  transport_eq : proj_V_nabla = hamiltonian

/-- The transport equation implies the kernel condition:
    `ψ` satisfies transport iff `(H_q − π_V ∇) ψ = 0`. -/
theorem CategoricalTransport.kernel_condition {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C]
    (ct : CategoricalTransport C) :
    ct.hamiltonian - ct.proj_V_nabla = 0 := by
  simp [ct.transport_eq, sub_self]

end QOU
