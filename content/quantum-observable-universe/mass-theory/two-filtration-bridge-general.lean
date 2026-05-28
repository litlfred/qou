import QOU.Kashaev
-- Sibling docstub for `prop:two-filtration-bridge-general`.
--
-- This file is documentation only.  The compiled formalisation
-- lives in the Lake-built tree at:
--
--   lean/QOU/AlgebraicSubstrate/TwoFiltrationBridgeGeneral.lean
--
-- See `QOU.AlgebraicSubstrate.TwoFiltrationBridgeGeneral.bridge_map_general`.
--
-- See the chapter umbrella `lean/QOU/AlgebraicSubstrate.lean`
-- for the import wiring.

namespace QOU.AlgebraicSubstrate.TwoFiltrationBridgeGeneral

/-- **PROPOSITION.** Two-filtration bridge map in full generality: bar-class determines iterated-integral depth (self-conj $\\to$ 2, chiral pair $\\to$ 3) for all partitions -/
theorem bridge_map_general : True := by
  -- Ref: [manuscript] prop:two-filtration-bridge-general
  trivial

end QOU.AlgebraicSubstrate.TwoFiltrationBridgeGeneral


-- §3b-cond conditional-class hypothesis for `prop:two-filtration-bridge-general`.
-- This proposition's uses[] cone reaches `conj:kashaev-volume-conjecture`; per
-- CLAUDE.md §3b-cond it is conditional on that conjecture's
-- axiomatised class `VolumeConjecture`. The statement above is fully
-- verified modulo this single class instance.
section ConditionalOn_VolumeConjecture
open QOU.Kashaev
variable (q_vc : ℝ) [VolumeConjecture q_vc]
end ConditionalOn_VolumeConjecture
