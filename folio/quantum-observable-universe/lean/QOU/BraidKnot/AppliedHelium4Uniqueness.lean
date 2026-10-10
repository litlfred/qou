import QOU.BraidKnot.NucleusEmptySDPUniqueness

/-!
# QOU.BraidKnot.AppliedHelium4Uniqueness — concrete ⁴He application

Thin wrapper specialising `NucleusEmptySDPUniqueness` to ⁴He's
strand count `n = 3·A = 3·4 = 12` (Z=2, N=2, A=4).

## Status

**Sorry-free closure** for ⁴He's empty-SDP uniqueness via the
parameterised `nucleus_uniqueness_closed` at `n := 12`. No
abstract-axiom dependency.

⁴He is the heaviest tracked light-nucleus in the QOU R5-full
solver post Sprint 2 (atom-braid extension landed ⁴He as a verified
case for `conj:atom-braid-exterior-algebra`).

## References

- `QOU.BraidKnot.NucleusEmptySDPUniqueness` (parameterised proof)
- Sprint 2 atom-braid extension (commit `57783eebb`)
-/

namespace QOU.BraidKnot

noncomputable section

/-- **⁴He empty-constraint SDP** at `heckeDim 12`. -/
abbrev helium4_emptySDP := nucleusEmptySDP 12

/-- ⁴He empty SDP is strictly feasible. -/
abbrev helium4_emptySDP_strictlyFeasible := nucleusEmptySDP_strictlyFeasible 12

/-- ⁴He trivial strict-complementarity pair. -/
abbrev helium4_trivialStrictCompPair := nucleusTrivialStrictCompPair 12

/-- **⁴He uniqueness via the abstract bridge** (axiom-dependent path). -/
abbrev helium4_uniqueness_via_empty_sdp := nucleus_uniqueness_via_empty_sdp 12

/-- ⁴He real strong-duality pair. -/
abbrev helium4_realStrongDualityPair := nucleusRealStrongDualityPair 12

/-- ⁴He dual slack is PosDef. -/
abbrev helium4_dualSlack_posDef := nucleus_dualSlack_posDef 12

/-- **Sorry-free uniqueness for ⁴He's empty SDP.** -/
abbrev helium4_uniqueness_closed := @nucleus_uniqueness_closed 12

/-- ⁴He optimum is the zero matrix. -/
abbrev helium4_optimum_is_zero := nucleus_optimum_is_zero 12

/-- ⁴He objective at optimum equals 0. -/
abbrev helium4_objAt_optimum_eq_zero := nucleus_objAt_optimum_eq_zero 12

end  -- noncomputable section
end QOU.BraidKnot
