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
# QOU.self_dual_curvature

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/self_dual_curvature.lean (monolithic)

**Ground ring**: `ℝ` (geometric/analytic realisation).
Uses ℝ-specific analysis (trig, norms, real powers).
NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Proposition (Self-duality of the curvature).**
    When `dim_ℝ M = 5` (CR dimension `n = 2`, so `dim_ℝ H = 4`), the
    curvature of an instanton connection, restricted to `H`, is self-dual
    with respect to the Hodge star `*_H` determined by the Webster metric.

    LaTeX: `\label{prop:self-dual-curvature}`
    Proof: The contact form `θ` splits `TM = H ⊕ ℝξ`.  By the Bogomolny
    decomposition, `YM(A) = ∫‖F⁺‖² + ∫‖F⁻‖²`.  Minimisation forces
    `F⁻ = 0`, which is precisely `⋆_H F_A|_H = F_A|_H`. -/
theorem self_dual_curvature (cqou : CQuantumObservableUniverse)
    (hn : cqou.n = 2)
    (inst : InstantonConnection cqou.toCRManifoldData) :
    (inst.hodgeStar hn).IsSelfDual inst.curvature_H :=
  inst.self_dual hn

end QOU
