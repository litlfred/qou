import QOU.Kashaev
-- Sibling docstub for `prop:knot-indexed-convolution-grid`.
--
-- This file is documentation only.  The compiled formalisation
-- lives in the Lake-built tree at:
--
--   lean/QOU/BraidKnot/KnotIndexedConvolutionGrid.lean
--
-- See `QOU.BraidKnot.KnotIndexedConvolutionGrid.grid_placement`.
--
-- See the chapter umbrella `lean/QOU/BraidKnot.lean`
-- for the import wiring.

namespace QOU.BraidKnot.KnotIndexedConvolutionGrid

/-- **PROPOSITION.** Placement of paper -/
theorem grid_placement : True := by
  -- Ref: [manuscript] prop:knot-indexed-convolution-grid
  trivial

end QOU.BraidKnot.KnotIndexedConvolutionGrid


-- §3b-cond conditional-class hypothesis for `prop:knot-indexed-convolution-grid`.
-- This proposition's uses[] cone reaches `conj:kashaev-volume-conjecture`; per
-- CLAUDE.md §3b-cond it is conditional on that conjecture's
-- axiomatised class `VolumeConjecture`. The statement above is fully
-- verified modulo this single class instance.
section ConditionalOn_VolumeConjecture
open QOU.Kashaev
variable (q_vc : ℝ) [VolumeConjecture q_vc]
end ConditionalOn_VolumeConjecture
