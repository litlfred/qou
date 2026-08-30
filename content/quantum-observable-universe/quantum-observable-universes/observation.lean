import QOU.Basic
import QOU.Glossary
import QOU.QuantumObservableUniverse.CategoricalFoundations
import QOU.QuantumObservableUniverse.CRRealisation
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

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

universe u v

attribute [local instance] QuantumUniverse.catInst QuantumUniverse.monInst

/-- **Observation** as a categorical endomorphism `O : A → A` in `C`.

    An observation preserves the Frobenius form and induces a substrate
    perturbation `q ↦ q + δq` via the Hopf coaction.

    LaTeX: `\label{def:observation}` -/
structure Observation {R : Type*} [CommRing R]
    (qou : QuantumObservableUniverse.{u, v} R) where
  /-- The observation morphism `O : A → A` in `C`. -/
  morphism : qou.frobHopf.obj ⟶ qou.frobHopf.obj
  /-- **Frobenius compatibility**: `λ ∘ O = λ` — the observation preserves
      the Frobenius form. -/
  frobenius_compat :
    morphism ≫ qou.frobHopf.frobeniusForm = qou.frobHopf.frobeniusForm
  /-- **Substrate perturbation** `δq`, carried as a morphism `𝟙 → 𝟙`.

      Scope warning: this is *free data*, not a derived quantity.  The
      narrative describes `δq` as **determined by** the Hopf coaction, but
      nothing in this structure ties `substrate_shift` either to
      `qou.frobHopf`'s comultiplication or to `morphism` — any endomorphism
      of the unit inhabits the field.  Deriving it (or constraining it by a
      coaction equation) is open; until then do not read an inhabitant of
      `Observation` as evidence that the shift is coaction-induced. -/
  substrate_shift :
    (𝟙_ qou.C) ⟶ (𝟙_ qou.C)

/-- **Archimedean observation**: concrete realisation of `Observation` on a
    CR manifold as a gauge-equivariant endomorphism of the state bundle.

    LaTeX: `\label{rem:observation-archimedean}` -/
structure ArchimedeanObservation (cqou : CQuantumObservableUniverse) where
  /-- The type of global sections `Γ(S)` of the state bundle. -/
  StateSections : Type*
  /-- The observation map `obs : Γ(S) → ℝ`.

      Was `StateSections → R_q` while this very docstring said `→ ℝ`, and the
      structure is named **Archimedean**Observation with the label
      `rem:observation-archimedean`. The library copy
      (`lean/QOU/QuantumObservableUniverse/GaugeTheory.lean:250`) always had
      `ℝ`. Bean `qou-u87j`. -/
  obs : StateSections → ℝ
  /-- Gauge equivalence relation. -/
  gaugeEquiv : StateSections → StateSections → Prop
  /-- `obs` is constant on gauge-equivalence classes. -/
  obs_gauge_invariant : ∀ s₁ s₂, gaugeEquiv s₁ s₂ → obs s₁ = obs s₂
  /-- **Well-definedness from observability**: the adjoint vanishing
      `H⁰(M, Ad(P)) = 0` ensures all sections are gauge-equivalent. -/
  obs_well_defined : ∀ s₁ s₂, gaugeEquiv s₁ s₂

end

end QOU
