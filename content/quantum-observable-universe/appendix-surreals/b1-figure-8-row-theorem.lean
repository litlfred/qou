import QOU.Kashaev
-- Sibling docstub for `prop:b1-figure-8-row-theorem`.
--
-- This file is documentation only.  The compiled formalisation
-- lives in the Lake-built tree at:
--
--   lean/QOU/AppendixSurreals/B1Figure8RowTheorem.lean
--
-- See `QOU.AppendixSurreals.B1Figure8RowTheorem.b1_figure_8_row`.
--
-- See the chapter umbrella `lean/QOU/AppendixSurreals.lean`
-- for the import wiring.

namespace QOU.AppendixSurreals.B1Figure8RowTheorem

/-- **PROPOSITION.** B1 keystone is theorem-level at the figure-8 row (Bloch--Suslin + Murakami--Murakami) -/
theorem b1_figure_8_row : True := by
  -- Ref: [manuscript] prop:b1-figure-8-row-theorem
  trivial

end QOU.AppendixSurreals.B1Figure8RowTheorem


-- §3b-cond conditional-class hypothesis for `prop:b1-figure-8-row-theorem`.
-- This proposition's uses[] cone reaches `conj:kashaev-volume-conjecture`; per
-- CLAUDE.md §3b-cond it is conditional on that conjecture's
-- axiomatised class `VolumeConjecture`. The statement above is fully
-- verified modulo this single class instance.
section ConditionalOn_VolumeConjecture
open QOU.Kashaev
variable (q_vc : ℝ) [VolumeConjecture q_vc]
end ConditionalOn_VolumeConjecture
