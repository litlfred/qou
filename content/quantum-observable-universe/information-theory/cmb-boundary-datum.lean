/-!
# QOU.CMBBoundaryDatum — CMB as boundary datum of a big bang state

The CMB (cosmic microwave background) of a big bang state:
the degree ≥ 1 jet data that survives the degree-0 vanishing.

LaTeX label: `def:cmb-boundary-datum`

Formalization: extracted from jet-horizon.lean for content-block co-location.
Source declaration: `QOU.CMBBoundaryDatum` in jet-horizon.lean

## References
- [manuscript] §9/cmb-boundary-datum
-/

-- Prerequisite types from jet-horizon.lean
-- (not independently compilable; see jet-horizon.lean for full context)

namespace QOU

/-- The CMB (cosmic microwave background) of a big bang state:
    the degree ≥ 1 jet data that survives the degree-0 vanishing. -/
-- Ref: [manuscript] §9/cmb-boundary-datum
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
