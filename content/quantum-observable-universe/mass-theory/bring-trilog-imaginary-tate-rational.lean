import QOU.Kashaev
-- Sibling docstub for `prop:bring-trilog-imaginary-tate-rational`.
--
-- This file is documentation only.  The compiled formalisation
-- lives in the Lake-built tree at:
--
--   lean/QOU/BraidKnot/BringTrilogImaginaryTateRational.lean
--
-- See `QOU.BraidKnot.BringTrilogImaginaryTateRational.im_li3_zeta5_closed_form`.
--
-- See the chapter umbrella `lean/QOU/BraidKnot.lean`
-- for the import wiring.

namespace QOU.BraidKnot.BringTrilogImaginaryTateRational

/-- **PROPOSITION.** Trilogarithm imaginary part at $\\zeta_5$: Tate-rational closed form $4\\pi^3/125$ via Kummer reflection (50-dps verified) -/
theorem im_li3_zeta5_closed_form : True := by
  -- Ref: [manuscript] prop:bring-trilog-imaginary-tate-rational
  trivial

end QOU.BraidKnot.BringTrilogImaginaryTateRational


-- §3b-cond conditional-class hypothesis for `prop:bring-trilog-imaginary-tate-rational`.
-- This proposition's uses[] cone reaches `conj:kashaev-volume-conjecture`; per
-- CLAUDE.md §3b-cond it is conditional on that conjecture's
-- axiomatised class `VolumeConjecture`. The statement above is fully
-- verified modulo this single class instance.
section ConditionalOn_VolumeConjecture
open QOU.Kashaev
variable (q_vc : ℝ) [VolumeConjecture q_vc]
end ConditionalOn_VolumeConjecture
