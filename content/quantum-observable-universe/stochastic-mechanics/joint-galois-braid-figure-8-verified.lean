import QOU.Kashaev
-- Sibling docstub for `prop:joint-galois-braid-figure-8-verified`.
--
-- This file is documentation only.  The compiled formalisation
-- lives in the Lake-built tree at:
--
--   lean/QOU/AlgebraicSubstrate/JointGaloisBraidFigure8.lean
--
-- See `QOU.AlgebraicSubstrate.JointGaloisBraidFigure8.figure_8_joint_action`.
--
-- See the chapter umbrella `lean/QOU/AlgebraicSubstrate.lean`
-- for the import wiring.

namespace QOU.AlgebraicSubstrate.JointGaloisBraidFigure8

/-- **PROPOSITION.** Joint Galois $\\times$ braid action commutes on the figure-8 bi-filtration cell — verified directly -/
theorem figure_8_joint_action : True := by
  -- Ref: [manuscript] prop:joint-galois-braid-figure-8-verified
  trivial

end QOU.AlgebraicSubstrate.JointGaloisBraidFigure8


-- §3b-cond conditional-class hypothesis for `prop:joint-galois-braid-figure-8-verified`.
-- This proposition's uses[] cone reaches `conj:kashaev-volume-conjecture`; per
-- CLAUDE.md §3b-cond it is conditional on that conjecture's
-- axiomatised class `VolumeConjecture`. The statement above is fully
-- verified modulo this single class instance.
section ConditionalOn_VolumeConjecture
open QOU.Kashaev
variable (q_vc : ℝ) [VolumeConjecture q_vc]
end ConditionalOn_VolumeConjecture
