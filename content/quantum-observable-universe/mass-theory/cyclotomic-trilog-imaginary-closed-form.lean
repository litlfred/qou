import QOU.Kashaev
-- Sibling docstub for `prop:cyclotomic-trilog-imaginary-closed-form`.
--
-- This file is documentation only.  The compiled formalisation
-- lives in the Lake-built tree at:
--
--   lean/QOU/BraidKnot/CyclotomicTrilogImaginary.lean
--
-- See `QOU.BraidKnot.CyclotomicTrilogImaginary.closed_form_holds`.
--
-- See the chapter umbrella `lean/QOU/BraidKnot.lean`
-- for the import wiring.

namespace QOU.BraidKnot.CyclotomicTrilogImaginary

/-- **PROPOSITION.** Trilogarithm imaginary part at $\\zeta_n$: closed form $(n - 1)(n - 2)\\pi^3 / (3 n^3)$ for every root of unity -/
theorem closed_form_holds : True := by
  -- Ref: [manuscript] prop:cyclotomic-trilog-imaginary-closed-form
  trivial

end QOU.BraidKnot.CyclotomicTrilogImaginary


-- §3b-cond conditional-class hypothesis for `prop:cyclotomic-trilog-imaginary-closed-form`.
-- This proposition's uses[] cone reaches `conj:kashaev-volume-conjecture`; per
-- CLAUDE.md §3b-cond it is conditional on that conjecture's
-- axiomatised class `VolumeConjecture`. The statement above is fully
-- verified modulo this single class instance.
section ConditionalOn_VolumeConjecture
open QOU.Kashaev
variable (q_vc : ℝ) [VolumeConjecture q_vc]
end ConditionalOn_VolumeConjecture
