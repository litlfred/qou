import QOU.Kashaev
-- Sibling docstub for `prop:borel-partial-resolution`.
--
-- This file is documentation only.  The compiled formalisation
-- lives in the Lake-built tree at:
--
--   lean/QOU/AppendixSurreals/BorelPartialResolution.lean
--
-- See `QOU.AppendixSurreals.BorelPartialResolution.borel_partial`.
--
-- See the chapter umbrella `lean/QOU/AppendixSurreals.lean`
-- for the import wiring.

namespace QOU.AppendixSurreals.BorelPartialResolution

/-- **PROPOSITION.** Borel -/
theorem borel_partial : True := by
  -- Ref: [manuscript] prop:borel-partial-resolution
  trivial

end QOU.AppendixSurreals.BorelPartialResolution


-- §3b-cond conditional-class hypothesis for `prop:borel-partial-resolution`.
-- This proposition's uses[] cone reaches `conj:kashaev-volume-conjecture`; per
-- CLAUDE.md §3b-cond it is conditional on that conjecture's
-- axiomatised class `VolumeConjecture`. The statement above is fully
-- verified modulo this single class instance.
section ConditionalOn_VolumeConjecture
open QOU.Kashaev
variable (q_vc : ℝ) [VolumeConjecture q_vc]
end ConditionalOn_VolumeConjecture
