import QOU.BraidKnot.NucleusEmptySDPUniqueness
import QOU.BraidKnot.DeuteronWitness
import QOU.BraidKnot.LightNucleus

/-!
# QOU.BraidKnot.AppliedDeuteronUniqueness — concrete ²H application

Thin wrapper specialising `NucleusEmptySDPUniqueness` to ²H's
strand count `n = 3·A = 3·2 = 6` (Z=1, N=1, A=2).

## Status

**Sorry-free closure** for ²H's empty-SDP uniqueness via the
parameterised `nucleus_uniqueness_closed` at `n := 6`. No
abstract-axiom dependency. The "real" ²H T_w uniqueness (with
multi-term cost from the mass formula) awaits PR #608 followup #1.

## References

- `QOU.BraidKnot.NucleusEmptySDPUniqueness` (parameterised proof)
- `QOU.BraidKnot.DeuteronWitness` (placeholder R5-full witness)
- PR #608 followup #1 (multi-term cost wiring)
-/

namespace QOU.BraidKnot

noncomputable section

/-- **²H empty-constraint SDP** at `heckeDim 6 = 720`. -/
abbrev deuteron_emptySDP := nucleusEmptySDP 6

/-- ²H empty SDP is strictly feasible. -/
abbrev deuteron_emptySDP_strictlyFeasible := nucleusEmptySDP_strictlyFeasible 6

/-- ²H trivial strict-complementarity pair. -/
abbrev deuteron_trivialStrictCompPair := nucleusTrivialStrictCompPair 6

/-- **²H uniqueness via the abstract bridge** (axiom-dependent path). -/
abbrev deuteron_uniqueness_via_empty_sdp_pending_multiterm :=
  nucleus_uniqueness_via_empty_sdp 6

/-- ²H real strong-duality pair. -/
abbrev deuteron_realStrongDualityPair := nucleusRealStrongDualityPair 6

/-- ²H dual slack is PosDef. -/
abbrev deuteron_dualSlack_posDef := nucleus_dualSlack_posDef 6

/-- **Sorry-free uniqueness for ²H's empty SDP.** -/
abbrev deuteron_uniqueness_closed := @nucleus_uniqueness_closed 6

/-- ²H optimum is the zero matrix. -/
abbrev deuteron_optimum_is_zero := nucleus_optimum_is_zero 6

/-- ²H objective at optimum equals 0. -/
abbrev deuteron_objAt_optimum_eq_zero := nucleus_objAt_optimum_eq_zero 6

end  -- noncomputable section
end QOU.BraidKnot
