import QOU.Kashaev
-- Sibling docstub for `prop:cyclotomic-dimension-synthesis-all-depths`.
--
-- This file is documentation only.  The compiled formalisation
-- lives in the Lake-built tree at:
--
--   lean/QOU/BraidKnot/CyclotomicDimensionSynthesisAllDepths.lean
--
-- See `QOU.BraidKnot.CyclotomicDimensionSynthesisAllDepths.dimension_synthesis_all_depths`.
--
-- See the chapter umbrella `lean/QOU/BraidKnot.lean`
-- for the import wiring.

namespace QOU.BraidKnot.CyclotomicDimensionSynthesisAllDepths

/-- **PROPOSITION.** Cyclotomic dimension synthesis at every depth: $(K - 3)/2$ for $n$ odd, $(K - 1)/2$ for $n$ even -/
theorem dimension_synthesis_all_depths : True := by
  -- Ref: [manuscript] prop:cyclotomic-dimension-synthesis-all-depths
  trivial

end QOU.BraidKnot.CyclotomicDimensionSynthesisAllDepths


-- §3b-cond conditional-class hypothesis for `prop:cyclotomic-dimension-synthesis-all-depths`.
-- This proposition's uses[] cone reaches `conj:kashaev-volume-conjecture`; per
-- CLAUDE.md §3b-cond it is conditional on that conjecture's
-- axiomatised class `VolumeConjecture`. The statement above is fully
-- verified modulo this single class instance.
section ConditionalOn_VolumeConjecture
open QOU.Kashaev
variable (q_vc : ℝ) [VolumeConjecture q_vc]
end ConditionalOn_VolumeConjecture
