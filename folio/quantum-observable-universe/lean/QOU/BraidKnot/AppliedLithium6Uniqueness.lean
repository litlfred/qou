import QOU.BraidKnot.NucleusEmptySDPUniqueness

/-!
# QOU.BraidKnot.AppliedLithium6Uniqueness — concrete ⁶Li application

Thin wrapper specialising `NucleusEmptySDPUniqueness` to ⁶Li's
strand count `n = 3·A = 3·6 = 18` (Z=3, N=3, A=6).

## Status

**Sorry-free closure** for ⁶Li's empty-SDP uniqueness via the
parameterised `nucleus_uniqueness_closed` at `n := 18`. No
abstract-axiom dependency.

⁶Li was added as a verified atom-braid case in Sprint 2 (commit
`57783eebb`); this file lifts the same to the SDP-uniqueness layer.

## References

- `QOU.BraidKnot.NucleusEmptySDPUniqueness` (parameterised proof)
- Sprint 2 atom-braid extension
-/

namespace QOU.BraidKnot

noncomputable section

/-- **⁶Li empty-constraint SDP** at `heckeDim 18`. -/
abbrev lithium6_emptySDP := nucleusEmptySDP 18

/-- ⁶Li empty SDP is strictly feasible. -/
abbrev lithium6_emptySDP_strictlyFeasible := nucleusEmptySDP_strictlyFeasible 18

/-- ⁶Li trivial strict-complementarity pair. -/
abbrev lithium6_trivialStrictCompPair := nucleusTrivialStrictCompPair 18

/-- **⁶Li uniqueness via the abstract bridge** (axiom-dependent path). -/
abbrev lithium6_uniqueness_via_empty_sdp := nucleus_uniqueness_via_empty_sdp 18

/-- ⁶Li real strong-duality pair. -/
abbrev lithium6_realStrongDualityPair := nucleusRealStrongDualityPair 18

/-- ⁶Li dual slack is PosDef. -/
abbrev lithium6_dualSlack_posDef := nucleus_dualSlack_posDef 18

/-- **Sorry-free uniqueness for ⁶Li's empty SDP.** -/
abbrev lithium6_uniqueness_closed := @nucleus_uniqueness_closed 18

/-- ⁶Li optimum is the zero matrix. -/
abbrev lithium6_optimum_is_zero := nucleus_optimum_is_zero 18

/-- ⁶Li objective at optimum equals 0. -/
abbrev lithium6_objAt_optimum_eq_zero := nucleus_objAt_optimum_eq_zero 18

end  -- noncomputable section
end QOU.BraidKnot
