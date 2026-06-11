import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.LinearAlgebra.ExteriorAlgebra.Basic


/-!
# QOU.Observation

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/Observation.lean (monolithic)

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

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
  /-- The type of global sections `Γ(S)` of the state bundle. -/
  StateSections : Type*
  /-- The observation map `obs : Γ(S) → ℝ`. -/
  obs : StateSections → R_q
  /-- Gauge equivalence relation. -/
  gaugeEquiv : StateSections → StateSections → Prop
  /-- `obs` is constant on gauge-equivalence classes. -/
  obs_gauge_invariant : ∀ s₁ s₂, gaugeEquiv s₁ s₂ → obs s₁ = obs s₂
  /-- **Well-definedness from observability**: the adjoint vanishing
      `H⁰(M, Ad(P)) = 0` ensures all sections are gauge-equivalent. -/
  obs_well_defined : ∀ s₁ s₂, gaugeEquiv s₁ s₂

end QOU
