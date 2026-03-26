/-!
# QOU.Observation

Extracted from lean-archive/ for content-block co-location.
Source: lean-archive/QOU/Observation.lean (monolithic)
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

/-- **Observation** as a categorical endomorphism `O : A → A` in `C`.

    An observation preserves the Frobenius form and induces a substrate
    perturbation `q ↦ q + δq` via the Hopf coaction.

    LaTeX: `\label{def:observation}` -/
structure Observation {k : Type*} [Field k]
    (qou : QuantumObservableUniverse.{u, v} k) where
  /-- The observation morphism `O : A → A` in `C`. -/
  morphism : @CategoryTheory.Hom _ qou.catInst qou.frobHopf.obj qou.frobHopf.obj
  /-- **Frobenius compatibility**: `λ ∘ O = λ` — the observation preserves
      the Frobenius form. -/
  frobenius_compat : morphism ≫ qou.frobHopf.frobeniusForm =
    qou.frobHopf.frobeniusForm
  /-- **Substrate perturbation**: the induced shift `δq` is determined by
      the Hopf coaction.  Encoded as a morphism `𝟙 → 𝟙`. -/
  substrate_shift :
    @CategoryTheory.Hom _ qou.catInst (𝟙_ qou.C) (𝟙_ qou.C)

/-- **Archimedean observation**: concrete realisation of `Observation` on a
    CR manifold as a gauge-equivariant endomorphism of the state bundle.

    LaTeX: `\label{rem:observation-archimedean}` -/
structure ArchimedeanObservation (cqou : CQuantumObservableUniverse) where
  /-- The type of global sections `Γ(E)` of the state bundle. -/
  StateSections : Type*
  /-- The observation map `obs : Γ(E) → ℝ`. -/
  obs : StateSections → ℝ
  /-- Gauge equivalence relation. -/
  gaugeEquiv : StateSections → StateSections → Prop
  /-- `obs` is constant on gauge-equivalence classes. -/
  obs_gauge_invariant : ∀ s₁ s₂, gaugeEquiv s₁ s₂ → obs s₁ = obs s₂
  /-- **Well-definedness from observability**: the adjoint vanishing
      `H⁰(M, Ad(P)) = 0` ensures all sections are gauge-equivalent. -/
  obs_well_defined : ∀ s₁ s₂, gaugeEquiv s₁ s₂

end QOU
