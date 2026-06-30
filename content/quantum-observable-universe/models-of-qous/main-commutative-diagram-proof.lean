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
# QOU.main_commutative_diagram

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/main_commutative_diagram.lean (monolithic)
-/

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

-- Ref: [kock2004] Kock, "Frobenius Algebras and 2D Topological Quantum Field Theories," CUP LMS Student Texts 59, 2004
theorem main_commutative_diagram (cqou : CQuantumObservableUniverse)
    (sp : SubstrateParameter cqou.M)
    (inst : InstantonConnection cqou.toCRManifoldData)
    (diag : MainCommutativeDiagram cqou sp inst) :
    ∀ (x : diag.JetBundle),
      diag.substrate_coupling (diag.euler_lagrange x) =
      diag.parallel_transport (diag.jet_eval x) :=
  diag.commutes

-- Ref: [kock2004] Kock, "Frobenius Algebras and 2D Topological Quantum Field Theories," CUP LMS Student Texts 59, 2004
structure MainCommutativeDiagram (cqou : CQuantumObservableUniverse)
    (sp : SubstrateParameter cqou.M)
    (inst : InstantonConnection cqou.toCRManifoldData) where
  /-- The type of first-order jet data `J¹E` of the state bundle. -/
  JetBundle : Type*
  /-- The type of field-equation solutions
      `{L_θ : Ric_{g_θ} = T^{(q)}}`. -/
  FieldEqns : Type*
  /-- The type of linearised sections `Γ(E_lin)`. -/
  LinSections : Type*
  /-- The type of q-Schrödinger solutions
      `{ψ : J ℏ_q ι_{ξ_q} D_A ψ = Ĥ_q ψ}`. -/
  Solutions : Type*
  /-- Top: Euler–Lagrange operator `E[S_q] : J¹E → FieldEqns`. -/
  euler_lagrange : JetBundle → FieldEqns
  /-- Left: jet evaluation `j : J¹E → Γ(E_lin)`. -/
  jet_eval : JetBundle → LinSections
  /-- The right arrow: substrate coupling `κ : FieldEqns → Solutions`,
      sending a Levi form to the q-Schrödinger equation it induces
      via `q(p) = 1 + |⟨L_θ, F_A⁺⟩|(p)`. -/
  substrate_coupling : FieldEqns → Solutions
  /-- Bottom: parallel transport `∇^A : Γ(E_lin) → Solutions`. -/
  parallel_transport : LinSections → Solutions
  /-- **Commutativity**: the two paths around the square agree.
      `κ ∘ E[S_q] = ∇^A ∘ j` -/
  commutes : ∀ (x : JetBundle),
    substrate_coupling (euler_lagrange x) = parallel_transport (jet_eval x)

end QOU
