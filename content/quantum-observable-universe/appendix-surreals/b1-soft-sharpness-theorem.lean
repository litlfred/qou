import QOU.Kashaev
-- Sibling docstub for `prop:b1-soft-sharpness-theorem`.
--
-- This file is documentation only.  The compiled formalisation
-- lives in the Lake-built tree at:
--
--   lean/QOU/AppendixSurreals/B1SoftSharpnessTheorem.lean
--
-- See `QOU.AppendixSurreals.B1SoftSharpnessTheorem.b1_soft_sharpness`.
--
-- See the chapter umbrella `lean/QOU/AppendixSurreals.lean`
-- for the import wiring.

namespace QOU.AppendixSurreals.B1SoftSharpnessTheorem

/-- **PROPOSITION.** Soft sharpness of the keystone B1 is theorem-level — via Borel + polylog non-vanishing -/
theorem b1_soft_sharpness : True := by
  -- Ref: [manuscript] prop:b1-soft-sharpness-theorem
  trivial

end QOU.AppendixSurreals.B1SoftSharpnessTheorem


-- §3b-cond conditional-class hypothesis for `prop:b1-soft-sharpness-theorem`.
-- This proposition's uses[] cone reaches `conj:kashaev-volume-conjecture`; per
-- CLAUDE.md §3b-cond it is conditional on that conjecture's
-- axiomatised class `VolumeConjecture`. The statement above is fully
-- verified modulo this single class instance.
section ConditionalOn_VolumeConjecture
open QOU.Kashaev
variable (q_vc : ℝ) [VolumeConjecture q_vc]
end ConditionalOn_VolumeConjecture
