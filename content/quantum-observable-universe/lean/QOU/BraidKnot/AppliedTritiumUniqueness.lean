import QOU.BraidKnot.NucleusEmptySDPUniqueness
import QOU.BraidKnot.TritiumWitness
import QOU.BraidKnot.LightNucleus

/-!
# QOU.BraidKnot.AppliedTritiumUniqueness — concrete ³H application

Thin wrapper specialising `NucleusEmptySDPUniqueness` to ³H's
strand count `n = 3·A = 3·3 = 9` (Z=1, N=2, A=3). Shares `n_0 = 9`
with ³He; the SDP setup is the same up to the witness data.

## Status

**Sorry-free closure** for ³H's empty-SDP uniqueness via the
parameterised `nucleus_uniqueness_closed` at `n := 9`. No
abstract-axiom dependency. The "real" ³H T_w uniqueness (with
Hoefsmit-H_5 cost basis) awaits the Python port (PR #608 deferred-
Hoefsmit-H5).

## References

- `QOU.BraidKnot.NucleusEmptySDPUniqueness` (parameterised proof)
- `QOU.BraidKnot.TritiumWitness` (placeholder R5-full witness)
- PR #608 deferred-Hoefsmit-H5
-/

namespace QOU.BraidKnot

noncomputable section

/-- **³H empty-constraint SDP** at `heckeDim 9 = 362880`. -/
abbrev tritium_emptySDP := nucleusEmptySDP 9

/-- ³H empty SDP is strictly feasible. -/
abbrev tritium_emptySDP_strictlyFeasible := nucleusEmptySDP_strictlyFeasible 9

/-- ³H trivial strict-complementarity pair. -/
abbrev tritium_trivialStrictCompPair := nucleusTrivialStrictCompPair 9

/-- **³H uniqueness via the abstract bridge** (axiom-dependent path). -/
abbrev tritium_uniqueness_via_empty_sdp_pending_hoefsmit :=
  nucleus_uniqueness_via_empty_sdp 9

/-- ³H real strong-duality pair. -/
abbrev tritium_realStrongDualityPair := nucleusRealStrongDualityPair 9

/-- ³H dual slack is PosDef. -/
abbrev tritium_dualSlack_posDef := nucleus_dualSlack_posDef 9

/-- **Sorry-free uniqueness for ³H's empty SDP.** -/
abbrev tritium_uniqueness_closed := @nucleus_uniqueness_closed 9

/-- ³H optimum is the zero matrix. -/
abbrev tritium_optimum_is_zero := nucleus_optimum_is_zero 9

/-- ³H objective at optimum equals 0. -/
abbrev tritium_objAt_optimum_eq_zero := nucleus_objAt_optimum_eq_zero 9

end  -- noncomputable section
end QOU.BraidKnot
