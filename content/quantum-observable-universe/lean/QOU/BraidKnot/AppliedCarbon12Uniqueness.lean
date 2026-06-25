import QOU.BraidKnot.NucleusEmptySDPUniqueness

/-!
# QOU.BraidKnot.AppliedCarbon12Uniqueness — concrete ¹²C application

Thin wrapper specialising `NucleusEmptySDPUniqueness` to ¹²C's
strand count `n = 3·A = 3·12 = 36` (Z=6, N=6, A=12).

¹²C is the third triple-α product (3·⁴He → ¹²C via the Hoyle
state at 7.65 MeV), making it the gateway to all heavier
nucleosynthesis in stellar interiors.

## Status

**Sorry-free closure** for ¹²C's empty-SDP uniqueness via the
parameterised `nucleus_uniqueness_closed` at `n := 36`. No
abstract-axiom dependency. The QOU framework does not yet have
an R5-full witness for ¹²C; this module pre-provisions the
uniqueness scaffolding for when that witness lands.

## References

- `QOU.BraidKnot.NucleusEmptySDPUniqueness` (parameterised proof)
-/

namespace QOU.BraidKnot

noncomputable section

/-- **¹²C empty-constraint SDP** at `heckeDim 36`. -/
abbrev carbon12_emptySDP := nucleusEmptySDP 36

/-- ¹²C empty SDP is strictly feasible. -/
abbrev carbon12_emptySDP_strictlyFeasible := nucleusEmptySDP_strictlyFeasible 36

/-- ¹²C trivial strict-complementarity pair. -/
abbrev carbon12_trivialStrictCompPair := nucleusTrivialStrictCompPair 36

/-- **¹²C uniqueness via the abstract bridge** (axiom-dependent path). -/
abbrev carbon12_uniqueness_via_empty_sdp := nucleus_uniqueness_via_empty_sdp 36

/-- ¹²C real strong-duality pair. -/
abbrev carbon12_realStrongDualityPair := nucleusRealStrongDualityPair 36

/-- ¹²C dual slack is PosDef. -/
abbrev carbon12_dualSlack_posDef := nucleus_dualSlack_posDef 36

/-- **Sorry-free uniqueness for ¹²C's empty SDP.** -/
abbrev carbon12_uniqueness_closed := @nucleus_uniqueness_closed 36

/-- ¹²C optimum is the zero matrix. -/
abbrev carbon12_optimum_is_zero := nucleus_optimum_is_zero 36

/-- ¹²C objective at optimum equals 0. -/
abbrev carbon12_objAt_optimum_eq_zero := nucleus_objAt_optimum_eq_zero 36

end  -- noncomputable section
end QOU.BraidKnot
