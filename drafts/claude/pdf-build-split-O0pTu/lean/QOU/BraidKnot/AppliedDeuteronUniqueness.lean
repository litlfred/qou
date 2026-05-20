import Mathlib.Tactic
import QOU.MathlibExt.SDP
import QOU.MathlibExt.SDPEmptyConstraints
import QOU.HeckeAlgebra.Common
import QOU.BraidKnot.LightNucleus
import QOU.BraidKnot.WitnessR5Full
import QOU.BraidKnot.DeuteronWitness
import QOU.BraidKnot.CanonicalKnotIdSDPUniqueness

/-!
# QOU.BraidKnot.AppliedDeuteronUniqueness

Mirror of `AppliedHelium3Uniqueness` for ²H, with the same
empty-constraint SDP setup at `heckeDim 2 = 2!! = 2` (the
deuteron's H_2 sub-block is trivial; the actual deuteron lives
at H_6 with 6! = 720 dimensions, but for the abstract uniqueness
framework demonstration we use the empty-constraint setup at the
size determined by `heckeDim n` for whatever `n` we choose).

For ²H, we use `n := 6` (the deuteron's strand count) and
`heckeDim 6 = 720`.  The empty-constraint SDP at this dimension
is feasible (identity is PosDef) and the trivial strict-
complementarity pair gives the same `Subsingleton` uniqueness
conclusion as helium3, modulo the multi-term-cost dependency
flagged in the witness placeholder.

## Open work

The "real" deuteron uniqueness statement awaits the multi-term
cost re-run (PR #608 followup #1) — at that point, the
`R5FullWitness LightNucleus.deuterium` placeholder gets replaced
by a real witness recording the canonical `6_2` knot, and the
SDP setup uses non-trivial constraints derived from the
multi-term cost function.

## References

- `QOU.BraidKnot.DeuteronWitness` (placeholder R5-full witness)
- `QOU.MathlibExt.SDPEmptyConstraints` (trivial sub-case)
- `QOU.BraidKnot.CanonicalKnotIdSDPUniqueness` (abstract bridge)
- PR #608 followup #1 (multi-term cost wiring)
-/

namespace QOU.BraidKnot

open QOU.MathlibExt.SDP QOU.MathlibExt.SDPEmptyConstraints
open QOU.HeckeAlgebra

/-- **Empty-constraint SDP at the deuteron's H_6 dimension**
    (`heckeDim 6 = 720`).  Used for the abstract-uniqueness
    framework demonstration; the concrete multi-term-cost SDP
    at H_6 awaits PR #608 followup #1. -/
def deuteron_emptySDP : SDPPrimal (heckeDim 6) ℝ Empty where
  cost := 1
  constraint := fun i => i.elim
  rhs := fun i => i.elim

theorem deuteron_emptySDP_strictlyFeasible :
    deuteron_emptySDP.IsStrictlyFeasible :=
  one_isStrictlyFeasible deuteron_emptySDP

def deuteron_trivialStrictCompPair :
    StrictComplementarityPair deuteron_emptySDP :=
  trivialStrictComplementarityPair deuteron_emptySDP

theorem deuteron_uniqueness_via_empty_sdp_pending_multiterm :
    Subsingleton {Φ : Matrix (Fin (heckeDim 6)) (Fin (heckeDim 6)) ℝ //
      deuteron_emptySDP.IsFeasible Φ ∧
      deuteron_emptySDP.objAt Φ = deuteron_emptySDP.objAt
        deuteron_trivialStrictCompPair.Φstar} :=
  canonical_T_w_subsingleton deuteron_trivialStrictCompPair

end QOU.BraidKnot
