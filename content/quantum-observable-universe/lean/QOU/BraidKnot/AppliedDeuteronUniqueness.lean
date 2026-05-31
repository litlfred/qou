import Mathlib.Tactic
import QOU.MathlibExt.SDP
import QOU.MathlibExt.SDPEmptyConstraints
import QOU.MathlibExt.SDPRealUniqueness
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

/-! ### Interior-case closure for ²H via the ℝ-uniqueness layer

Mirrors the ³He closure in `AppliedHelium3Uniqueness.lean §6`.
The empty-constraint SDP for ²H has cost matrix `T = 1`
(identity), no equality constraints, hence dual slack
`S(y) = T - Σ y_i A_i = 1` (identity, regardless of `y` since
the sum is empty). The identity matrix is positive-DEFINITE,
so `real_strict_complementarity_unique_of_dualSlack_posDef`
applies and gives full sorry-free uniqueness.

Per the audit at `docs/coordination/2026-05-30-sdp-uniqueness-status.md`
§"Suggested follow-up §0", this closes the deuteron's only
axiom-dependent uniqueness consumer. -/

open QOU.MathlibExt.SDPRealUniqueness

/-- **Real strong-duality pair** for the ²H empty SDP. -/
def deuteron_realStrongDualityPair : RealStrongDualityPair deuteron_emptySDP where
  Φstar := 0
  ystar := fun i => i.elim
  primal_feas := zero_isFeasible deuteron_emptySDP
  dualSlack_psd := by
    show (deuteron_emptySDP.dualSlack (fun i => i.elim)).PosSemidef
    have h_eq : deuteron_emptySDP.dualSlack (fun i => i.elim) = 1 := by
      unfold SDPPrimal.dualSlack deuteron_emptySDP
      simp [Finset.sum_empty]
    rw [h_eq]
    exact Matrix.PosDef.one.posSemidef
  obj_eq_dualObj := by
    unfold SDPPrimal.objAt SDPPrimal.dualObjAt
    simp

/-- **Dual slack is PosDef** for the ²H empty SDP. -/
theorem deuteron_dualSlack_posDef :
    (deuteron_emptySDP.dualSlack deuteron_realStrongDualityPair.ystar).PosDef := by
  show (deuteron_emptySDP.dualSlack (fun i => i.elim)).PosDef
  have h_eq : deuteron_emptySDP.dualSlack (fun i => i.elim) = 1 := by
    unfold SDPPrimal.dualSlack deuteron_emptySDP
    simp [Finset.sum_empty]
  rw [h_eq]
  exact Matrix.PosDef.one

/-- **Closed sorry-free uniqueness for ²H's empty SDP** —
    via the interior-case closure of the strict-complementarity
    uniqueness theorem. No `sorry` in the chain
    `deuteron_realStrongDualityPair → deuteron_dualSlack_posDef →
    real_strict_complementarity_unique_of_dualSlack_posDef`. -/
theorem deuteron_uniqueness_closed
    {Φ' : Matrix (Fin (heckeDim 6)) (Fin (heckeDim 6)) ℝ}
    (h_feas : deuteron_emptySDP.IsFeasible Φ')
    (h_obj : deuteron_emptySDP.objAt Φ' =
             deuteron_emptySDP.objAt deuteron_realStrongDualityPair.Φstar) :
    Φ' = deuteron_realStrongDualityPair.Φstar :=
  real_strict_complementarity_unique_of_dualSlack_posDef
    deuteron_realStrongDualityPair deuteron_dualSlack_posDef
    h_feas h_obj

/-- The optimum Φ⋆ in this empty-constraint setup is the zero matrix. -/
theorem deuteron_optimum_is_zero :
    deuteron_realStrongDualityPair.Φstar =
      (0 : Matrix (Fin (heckeDim 6)) (Fin (heckeDim 6)) ℝ) := rfl

/-- The objective value at the (zero) optimum is exactly 0. -/
theorem deuteron_objAt_optimum_eq_zero :
    deuteron_emptySDP.objAt deuteron_realStrongDualityPair.Φstar = 0 := by
  unfold SDPPrimal.objAt deuteron_emptySDP
  simp [deuteron_optimum_is_zero]

end QOU.BraidKnot
