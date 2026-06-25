import QOU.BraidKnot.NucleusEmptySDPUniqueness

/-!
# QOU.BraidKnot.AppliedNitrogen14Uniqueness — concrete ¹⁴N application

Thin wrapper specialising `NucleusEmptySDPUniqueness` to ¹⁴N's
strand count `n = 3·A = 3·14 = 42` (Z=7, N=7, A=14).

¹⁴N is the bottleneck of the CNO cycle in stars more massive than
the Sun, making it observationally critical for stellar evolution.

## Status

**Sorry-free closure** for ¹⁴N's empty-SDP uniqueness via the
parameterised `nucleus_uniqueness_closed` at `n := 42`. No
abstract-axiom dependency. R5-full witness not yet provisioned;
this module pre-provisions the uniqueness scaffolding.

## References

- `QOU.BraidKnot.NucleusEmptySDPUniqueness` (parameterised proof)
-/

namespace QOU.BraidKnot

noncomputable section

/-- **¹⁴N empty-constraint SDP** at `heckeDim 42`. -/
abbrev nitrogen14_emptySDP := nucleusEmptySDP 42

/-- ¹⁴N empty SDP is strictly feasible. -/
abbrev nitrogen14_emptySDP_strictlyFeasible := nucleusEmptySDP_strictlyFeasible 42

/-- ¹⁴N trivial strict-complementarity pair. -/
abbrev nitrogen14_trivialStrictCompPair := nucleusTrivialStrictCompPair 42

/-- **¹⁴N uniqueness via the abstract bridge** (axiom-dependent path). -/
abbrev nitrogen14_uniqueness_via_empty_sdp := nucleus_uniqueness_via_empty_sdp 42

/-- ¹⁴N real strong-duality pair. -/
abbrev nitrogen14_realStrongDualityPair := nucleusRealStrongDualityPair 42

/-- ¹⁴N dual slack is PosDef. -/
abbrev nitrogen14_dualSlack_posDef := nucleus_dualSlack_posDef 42

/-- **Sorry-free uniqueness for ¹⁴N's empty SDP.** -/
abbrev nitrogen14_uniqueness_closed := @nucleus_uniqueness_closed 42

/-- ¹⁴N optimum is the zero matrix. -/
abbrev nitrogen14_optimum_is_zero := nucleus_optimum_is_zero 42

/-- ¹⁴N objective at optimum equals 0. -/
abbrev nitrogen14_objAt_optimum_eq_zero := nucleus_objAt_optimum_eq_zero 42

end  -- noncomputable section
end QOU.BraidKnot
