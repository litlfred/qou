/-!
# QOU.SubstrateParameter

Extracted from lean-archive/ for content-block co-location.
Source: lean-archive/QOU/SubstrateParameter.lean (monolithic)
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

/-- **Substrate parameter** (abstract): a ring homomorphism
    `ι : ℤ[q, q⁻¹] → k` specialising the Lusztig integral form
    `U^ℤ_q(su(2))` to a value `q₀ ∈ k×`.  The base-changed algebra
    `U^ℤ_q ⊗_{ℤ[q,q⁻¹]} k` is the quantised enveloping algebra at `q₀`.

    When the quantum universe is fibred over a space `M`, `q₀` may vary
    point-to-point yielding a *substrate field* `q : M → k×`.

    LaTeX: `\label{def:substrate-parameter}` -/
structure SubstrateParameter (M : Type*) where
  /-- The substrate field `q : M → ℝ` with `q(p) ≥ 1`.
      In the abstract setting this is the composition
      `M → Spec(k) → Spec(ℤ[q, q⁻¹])`. -/
  field : M → ℝ
  /-- Invertibility: `q(p) > 0` for all `p`. -/
  field_pos : ∀ (p : M), 0 < field p
  /-- Lower bound: `q(p) ≥ 1` (classicality bound).
      At `q = 1` all q-deformed operators recover their classical
      counterparts; `q > 1` is the quantum regime. -/
  field_ge_one : ∀ (p : M), 1 ≤ field p
  /-- The specialised value `q₀(p)` is never a root of unity,
      ensuring semisimplicity of the quantum group at each point.
      Encoded as: `q(p)^k ≠ 1` for all `k ≥ 1`. -/
  not_root_of_unity : ∀ (p : M) (k : ℕ), k ≥ 1 → field p ^ k ≠ 1

end QOU
