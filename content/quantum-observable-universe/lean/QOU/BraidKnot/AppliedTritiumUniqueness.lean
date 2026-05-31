import Mathlib.Tactic
import QOU.MathlibExt.SDP
import QOU.MathlibExt.SDPEmptyConstraints
import QOU.MathlibExt.SDPRealUniqueness
import QOU.HeckeAlgebra.Common
import QOU.BraidKnot.LightNucleus
import QOU.BraidKnot.WitnessR5Full
import QOU.BraidKnot.TritiumWitness
import QOU.BraidKnot.CanonicalKnotIdSDPUniqueness

/-!
# QOU.BraidKnot.AppliedTritiumUniqueness

Mirror of `AppliedHelium3Uniqueness` for ³H, with the same
empty-constraint SDP setup at `heckeDim 9 = 9! = 362880` (the
tritium's H_9 strand count = 3·3).

The SDP setup is identical to ³He's H_9 case (³H and ³He share
n_0 = 9), but the witness data is provisional (Hoefsmit-H_5
Python port pending).

## Open work

The "real" tritium uniqueness statement awaits the Python H_5
Hoefsmit port (PR #608 deferred-Hoefsmit-H5).  At that point,
the `R5FullWitness LightNucleus.tritium` placeholder gets
replaced by a real witness, and the strict-complementarity
certificate gets concrete numerical Wedderburn-block min-eigs.

## References

- `QOU.BraidKnot.TritiumWitness` (placeholder R5-full witness)
- `QOU.MathlibExt.SDPEmptyConstraints` (trivial sub-case)
- `QOU.BraidKnot.CanonicalKnotIdSDPUniqueness` (abstract bridge)
- PR #608 deferred-Hoefsmit-H5
-/

namespace QOU.BraidKnot

open QOU.MathlibExt.SDP QOU.MathlibExt.SDPEmptyConstraints
open QOU.HeckeAlgebra

/-- **Empty-constraint SDP at the tritium's H_9 dimension**
    (`heckeDim 9 = 9! = 362880`).  Used for the abstract-
    uniqueness framework demonstration; the concrete H_9
    Hoefsmit-based SDP awaits the Python port. -/
def tritium_emptySDP : SDPPrimal (heckeDim 9) ℝ Empty where
  cost := 1
  constraint := fun i => i.elim
  rhs := fun i => i.elim

theorem tritium_emptySDP_strictlyFeasible :
    tritium_emptySDP.IsStrictlyFeasible :=
  one_isStrictlyFeasible tritium_emptySDP

def tritium_trivialStrictCompPair :
    StrictComplementarityPair tritium_emptySDP :=
  trivialStrictComplementarityPair tritium_emptySDP

theorem tritium_uniqueness_via_empty_sdp_pending_hoefsmit :
    Subsingleton {Φ : Matrix (Fin (heckeDim 9)) (Fin (heckeDim 9)) ℝ //
      tritium_emptySDP.IsFeasible Φ ∧
      tritium_emptySDP.objAt Φ = tritium_emptySDP.objAt
        tritium_trivialStrictCompPair.Φstar} :=
  canonical_T_w_subsingleton tritium_trivialStrictCompPair

/-! ### Interior-case closure for ³H via the ℝ-uniqueness layer

Mirrors the ³He closure in `AppliedHelium3Uniqueness.lean §6`.
The empty-constraint SDP for ³H has cost matrix `T = 1`
(identity), no equality constraints, hence dual slack
`S(y) = T - Σ y_i A_i = 1` (identity). The identity matrix is
positive-DEFINITE, so `real_strict_complementarity_unique_of_
dualSlack_posDef` applies and gives full sorry-free uniqueness.

Per the audit at `docs/coordination/2026-05-30-sdp-uniqueness-status.md`
§"Suggested follow-up §0", this closes the tritium's only
axiom-dependent uniqueness consumer. -/

open QOU.MathlibExt.SDPRealUniqueness

/-- **Real strong-duality pair** for the ³H empty SDP. -/
def tritium_realStrongDualityPair : RealStrongDualityPair tritium_emptySDP where
  Φstar := 0
  ystar := fun i => i.elim
  primal_feas := zero_isFeasible tritium_emptySDP
  dualSlack_psd := by
    show (tritium_emptySDP.dualSlack (fun i => i.elim)).PosSemidef
    have h_eq : tritium_emptySDP.dualSlack (fun i => i.elim) = 1 := by
      unfold SDPPrimal.dualSlack tritium_emptySDP
      simp [Finset.sum_empty]
    rw [h_eq]
    exact Matrix.PosDef.one.posSemidef
  obj_eq_dualObj := by
    unfold SDPPrimal.objAt SDPPrimal.dualObjAt
    simp

/-- **Dual slack is PosDef** for the ³H empty SDP. -/
theorem tritium_dualSlack_posDef :
    (tritium_emptySDP.dualSlack tritium_realStrongDualityPair.ystar).PosDef := by
  show (tritium_emptySDP.dualSlack (fun i => i.elim)).PosDef
  have h_eq : tritium_emptySDP.dualSlack (fun i => i.elim) = 1 := by
    unfold SDPPrimal.dualSlack tritium_emptySDP
    simp [Finset.sum_empty]
  rw [h_eq]
  exact Matrix.PosDef.one

/-- **Closed sorry-free uniqueness for ³H's empty SDP** —
    via the interior-case closure of the strict-complementarity
    uniqueness theorem. No `sorry` in the chain
    `tritium_realStrongDualityPair → tritium_dualSlack_posDef →
    real_strict_complementarity_unique_of_dualSlack_posDef`. -/
theorem tritium_uniqueness_closed
    {Φ' : Matrix (Fin (heckeDim 9)) (Fin (heckeDim 9)) ℝ}
    (h_feas : tritium_emptySDP.IsFeasible Φ')
    (h_obj : tritium_emptySDP.objAt Φ' =
             tritium_emptySDP.objAt tritium_realStrongDualityPair.Φstar) :
    Φ' = tritium_realStrongDualityPair.Φstar :=
  real_strict_complementarity_unique_of_dualSlack_posDef
    tritium_realStrongDualityPair tritium_dualSlack_posDef
    h_feas h_obj

/-- The optimum Φ⋆ in this empty-constraint setup is the zero matrix. -/
theorem tritium_optimum_is_zero :
    tritium_realStrongDualityPair.Φstar =
      (0 : Matrix (Fin (heckeDim 9)) (Fin (heckeDim 9)) ℝ) := rfl

/-- The objective value at the (zero) optimum is exactly 0. -/
theorem tritium_objAt_optimum_eq_zero :
    tritium_emptySDP.objAt tritium_realStrongDualityPair.Φstar = 0 := by
  unfold SDPPrimal.objAt tritium_emptySDP
  simp [tritium_optimum_is_zero]

end QOU.BraidKnot
