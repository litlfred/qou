import Mathlib.Data.Real.Basic
import Mathlib.Data.List.Basic

/-!
# QOU.CMBFunctor — CMB functor

The CMB functor extracts degree ≥ 1 jet data surviving a boundary horizon.
Composition of the horizon functor ∂ with the colimit of (A₁/A₀ ⊕ A₂/A₀)
over the boundary.

LaTeX label: `def:cmb-functor`

Formalization: extracted from jet-horizon.lean for content-block co-location.
Source declaration: `QOU.CMBFunctor` in jet-horizon.lean

## References
- [leitner2026] §9/cmb-functor
-/

-- Prerequisite types mirrored from jet-horizon.lean (`QOU.JetHorizon` library
-- module) so this co-location extract compiles standalone. The canonical
-- definitions live in `QOU/JetHorizon.lean`; these copies keep the file
-- independently checkable without depending on the (uncached) library olean.

namespace QOU

/-- A graded jet algebra: type family indexed by degree k ∈ ℕ, with sections
    at each degree. (Mirror of `QOU.GradedJetAlgebra`.) -/
structure GradedJetAlgebra where
  /-- The type of sections at degree k. -/
  sections : ℕ → Type*
  /-- The zero section at each degree. -/
  zero : ∀ k, sections k
  /-- Inclusion A_k ↪ A_{k+1}. -/
  inclusion : ∀ k, sections k → sections (k + 1)

/-- A jet horizon: a locus where the degree-0 algebra vanishes.
    (Mirror of `QOU.JetHorizon`.) -/
structure JetHorizon where
  /-- The graded jet algebra over the chart. -/
  algebra : GradedJetAlgebra
  /-- At the horizon, every degree-0 section equals zero. -/
  degree_zero_vanishes : ∀ (s : algebra.sections 0), s = algebra.zero 0
  /-- There exists a non-trivial degree-1 section at the horizon. -/
  degree_one_leaks : ∃ (s : algebra.sections 1), s ≠ algebra.zero 1
  /-- There exists a non-trivial degree-2 section at the horizon. -/
  degree_two_leaks : ∃ (s : algebra.sections 2), s ≠ algebra.zero 2

/-- A big bang state. (Mirror of `QOU.BigBangState`.) -/
structure BigBangState extends JetHorizon where
  /-- Number of base points in the initial configuration. -/
  numBasePoints : ℕ
  /-- At least one base point. -/
  nonempty : numBasePoints ≥ 1

/-- The CMB of a big bang state: degree ≥ 1 jet data surviving the degree-0
    vanishing. (Mirror of `QOU.CMBBoundaryDatum`.) -/
structure CMBBoundaryDatum where
  /-- The big bang state whose CMB this is. -/
  source : BigBangState
  /-- A non-trivial degree-1 section (winding mode). -/
  degree_one_witness : source.algebra.sections 1
  /-- The degree-1 section is non-trivial. -/
  degree_one_nontrivial : degree_one_witness ≠ source.algebra.zero 1
  /-- A non-trivial degree-2 section (curvature mode). -/
  degree_two_witness : source.algebra.sections 2
  /-- The degree-2 section is non-trivial. -/
  degree_two_nontrivial : degree_two_witness ≠ source.algebra.zero 2

/-- The observable subcategory configuration. (Mirror of `QOU.ObservableConfig`.) -/
structure ObservableConfig where
  /-- The graded jet algebra. -/
  algebra : GradedJetAlgebra
  /-- There exists a non-trivial degree-0 section. -/
  degree_zero_nontrivial : ∃ (s : algebra.sections 0), s ≠ algebra.zero 0

/-- An aeon: a connected component of the observable subcategory.
    (Mirror of `QOU.Aeon`, restricted to the fields this extract uses.) -/
structure Aeon where
  /-- The observable configurations in this aeon. -/
  configs : Type*
  /-- Each configuration is observable. -/
  observable : configs → ObservableConfig
  /-- Boundary: jet horizons reachable as limits of directed diagrams. -/
  boundary : List JetHorizon

/-- The CMB functor value: the degree ≥ 1 data surviving a
    boundary horizon. Composition of ∂ with the colimit of
    (A_1/A_0 ⊕ A_2/A_0) over the boundary. -/
-- Ref: [leitner2026] §9/cmb-functor
structure CMBFunctorValue where
  /-- The source aeon. -/
  source : Aeon
  /-- The boundary horizon from which CMB data is extracted. -/
  horizon : JetHorizon
  /-- The horizon is in the aeon's boundary. -/
  in_boundary : horizon ∈ source.boundary
  /-- The CMB data at this horizon. -/
  cmb : CMBBoundaryDatum
  /-- The CMB's algebra matches the horizon's algebra. -/
  algebra_match : cmb.source.algebra = horizon.algebra

end QOU
