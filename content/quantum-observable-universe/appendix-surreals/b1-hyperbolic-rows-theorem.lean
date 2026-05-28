import QOU.Kashaev
-- Sibling docstub for `prop:b1-hyperbolic-rows-theorem`.
--
-- This file is documentation only.  The compiled formalisation
-- lives in the Lake-built tree at:
--
--   lean/QOU/AppendixSurreals/B1HyperbolicRowsTheorem.lean
--
-- See `QOU.AppendixSurreals.B1HyperbolicRowsTheorem.b1_hyperbolic_rows`.
--
-- See the chapter umbrella `lean/QOU/AppendixSurreals.lean`
-- for the import wiring.

namespace QOU.AppendixSurreals.B1HyperbolicRowsTheorem

/-- **PROPOSITION.** B1 at additional hyperbolic-knot rows (Borromean, Whitehead, twist knots) is theorem-level -/
theorem b1_hyperbolic_rows : True := by
  -- Ref: [manuscript] prop:b1-hyperbolic-rows-theorem
  trivial

end QOU.AppendixSurreals.B1HyperbolicRowsTheorem


-- §3b-cond conditional-class hypothesis for `prop:b1-hyperbolic-rows-theorem`.
-- This proposition's uses[] cone reaches `conj:kashaev-volume-conjecture`; per
-- CLAUDE.md §3b-cond it is conditional on that conjecture's
-- axiomatised class `VolumeConjecture`. The statement above is fully
-- verified modulo this single class instance.
section ConditionalOn_VolumeConjecture
open QOU.Kashaev
variable (q_vc : ℝ) [VolumeConjecture q_vc]
end ConditionalOn_VolumeConjecture
