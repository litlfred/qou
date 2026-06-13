import QOU.BraidKnot.NucleusEmptySDPUniqueness
import QOU.BraidKnot.Helium3Witness
import QOU.BraidKnot.LightNucleus

/-!
# QOU.BraidKnot.AppliedHelium3Uniqueness — concrete ³He application

Thin wrapper specialising `NucleusEmptySDPUniqueness` to ³He's
strand count `n = 3·A = 3·3 = 9` (Z=2, N=1, A=3).

For the abstract framework demonstration via the empty-constraint
SDP at `heckeDim 9 = 362880`, all theorems carry over from the
parameterised module with `n := 9`. The `Helium3Witness` import
is retained for callers that consume the concrete numerical
witness data alongside the uniqueness theorems.

## Status

**Sorry-free closure** for ³He's empty-SDP uniqueness via the
parameterised `nucleus_uniqueness_closed` at `n := 9`. No
abstract-axiom dependency. The "real" ³He T_w uniqueness (with
multi-term cost from the mass formula) awaits the cost-wiring
work; see audit
`docs/coordination/2026-05-30-sdp-uniqueness-status.md`.

## References

- `QOU.BraidKnot.NucleusEmptySDPUniqueness` (parameterised proof)
- `QOU.BraidKnot.Helium3Witness` (concrete numerical witness)
- `r5-full-canonical-knot-solver.witness.json` (PR #608 source)
-/

namespace QOU.BraidKnot

/-- **³He empty-constraint SDP** at `heckeDim 9`. -/
abbrev helium3_emptySDP := nucleusEmptySDP 9

/-- ³He empty SDP is strictly feasible. -/
abbrev helium3_emptySDP_strictlyFeasible := nucleusEmptySDP_strictlyFeasible 9

/-- ³He trivial strict-complementarity pair. -/
abbrev helium3_trivialStrictCompPair := nucleusTrivialStrictCompPair 9

/-- **³He uniqueness via the abstract bridge** (axiom-dependent path). -/
abbrev helium3_uniqueness_via_empty_sdp := nucleus_uniqueness_via_empty_sdp 9

/-- ³He Φ⋆ is the zero matrix. -/
abbrev helium3_emptySDP_Φstar_eq_zero := nucleusEmptySDP_Φstar_eq_zero 9

/-- ³He real strong-duality pair. -/
abbrev helium3_realStrongDualityPair := nucleusRealStrongDualityPair 9

/-- ³He dual slack is PosDef. -/
abbrev helium3_dualSlack_posDef := nucleus_dualSlack_posDef 9

/-- **Sorry-free uniqueness for ³He's empty SDP.** -/
abbrev helium3_uniqueness_closed := @nucleus_uniqueness_closed 9

/-- **Sorry-free ³He uniqueness via the active-empty route** — the
    argument whose hypotheses match the R5-full witness's `active = ∅`
    finding (all three Wedderburn-block min-eigs > 0). -/
abbrev helium3_uniqueness_closed_via_active_empty :=
  @nucleus_uniqueness_closed_via_active_empty 9

/-- ³He optimum is the zero matrix. -/
abbrev helium3_optimum_is_zero := nucleus_optimum_is_zero 9

/-- ³He objective at optimum equals 0. -/
abbrev helium3_objAt_optimum_eq_zero := nucleus_objAt_optimum_eq_zero 9

end QOU.BraidKnot
