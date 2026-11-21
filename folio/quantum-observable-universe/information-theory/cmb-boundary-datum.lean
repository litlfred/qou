import Mathlib.Data.Real.Basic
import Mathlib.Data.List.Basic

/-!
# QOU.CMBBoundaryDatum — CMB as boundary datum of a big bang state

The CMB (cosmic microwave background) of a big bang state:
the degree ≥ 1 jet data that survives the degree-0 vanishing.

LaTeX label: `def:cmb-boundary-datum`

Formalization: extracted from jet-horizon.lean for content-block co-location.
Source declaration: `QOU.CMBBoundaryDatum` in jet-horizon.lean

## References
- [leitner2026] §9/cmb-boundary-datum
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

/-- A big bang state: a bundle initial condition where A_0 = 0.
    (Mirror of `QOU.BigBangState`.) -/
structure BigBangState extends JetHorizon where
  /-- Number of base points in the initial configuration. -/
  numBasePoints : ℕ
  /-- At least one base point. -/
  nonempty : numBasePoints ≥ 1

/-- The CMB (cosmic microwave background) of a big bang state:
    the degree ≥ 1 jet data that survives the degree-0 vanishing. -/
-- Ref: [leitner2026] §9/cmb-boundary-datum
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

end QOU
