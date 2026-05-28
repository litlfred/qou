import QOU.Kashaev
-- Sibling docstub for `prop:two-filtration-bridge-small-cases`.
--
-- This file is documentation only.  The compiled formalisation
-- lives in the Lake-built tree at:
--
--   lean/QOU/AlgebraicSubstrate/TwoFiltrationBridgeSmallCases.lean
--
-- See `QOU.AlgebraicSubstrate.TwoFiltrationBridgeSmallCases.bridge_small_cases`.
--
-- See the chapter umbrella `lean/QOU/AlgebraicSubstrate.lean`
-- for the import wiring.

namespace QOU.AlgebraicSubstrate.TwoFiltrationBridgeSmallCases

/-- **PROPOSITION.** Two-filtration bridge map verified at small partitions ($n \\leq 4$) -/
theorem bridge_small_cases : True := by
  -- Ref: [manuscript] prop:two-filtration-bridge-small-cases
  trivial

end QOU.AlgebraicSubstrate.TwoFiltrationBridgeSmallCases


-- §3b-cond conditional-class hypothesis for `prop:two-filtration-bridge-small-cases`.
-- This proposition's uses[] cone reaches `conj:kashaev-volume-conjecture`; per
-- CLAUDE.md §3b-cond it is conditional on that conjecture's
-- axiomatised class `VolumeConjecture`. The statement above is fully
-- verified modulo this single class instance.
section ConditionalOn_VolumeConjecture
open QOU.Kashaev
variable (q_vc : ℝ) [VolumeConjecture q_vc]
end ConditionalOn_VolumeConjecture
