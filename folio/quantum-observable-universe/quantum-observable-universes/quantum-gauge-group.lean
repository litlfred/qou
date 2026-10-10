import QOU.Basic
import QOU.Glossary
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Topology.Basic
import Mathlib.Topology.ContinuousMap.Basic
import Mathlib.Geometry.Manifold.IsManifold.Basic
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.LinearAlgebra.ExteriorAlgebra.Basic


/-!
# QOU.QuantumGaugeGroup

Extracted from folio/quantum-observable-universe/lean/ for content-block co-location.
Source: folio/quantum-observable-universe/lean/QOU/QuantumGaugeGroup.lean (monolithic).
That file no longer exists — the library was split, and `QuantumGaugeGroup` now lives at
  folio/quantum-observable-universe/lean/QOU/Glossary.lean
  folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/SubstrateParameter.lean
-/

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    Mirrors the sibling block `substrate-parameter.lean`; see
    `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ

/-- **Substrate parameter** (categorical) — local prerequisite.

    Re-declared from the sibling block `substrate-parameter.lean`
    (`def:substrate-parameter`) so this sibling is a self-contained
    compilation unit — importing the library `SubstrateParameter`
    module would collide with its own `QuantumGaugeGroup`
    declaration.  Keep field-for-field in sync with the sibling. -/
structure SubstrateParameter (M : Type*) where
  /-- The categorical substrate field `q : M → R_q`. -/
  field : M → R_q

/-- **Quantum gauge group** in the ℂ realisation: the family of quantum
    groups `{SU_{q(p)}(2)}_{p ∈ M}` obtained by deforming `SU(2)` pointwise.

    LaTeX: `\label{def:quantum-gauge-group}` -/
structure QuantumGaugeGroup (M : Type*) extends SubstrateParameter M where
  /-- The quantum group at each point (opaque type family). -/
  groupAt : M → Type*

end QOU
