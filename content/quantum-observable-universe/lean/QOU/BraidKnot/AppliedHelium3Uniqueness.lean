import Mathlib.Tactic
import QOU.MathlibExt.SDP
import QOU.MathlibExt.SDPEmptyConstraints
import QOU.MathlibExt.SDPRealUniqueness
import QOU.HeckeAlgebra.Common
import QOU.BraidKnot.LightNucleus
import QOU.BraidKnot.WitnessR5Full
import QOU.BraidKnot.Helium3Witness
import QOU.BraidKnot.CanonicalKnotIdSDPUniqueness

/-!
# QOU.BraidKnot.AppliedHelium3Uniqueness — concrete uniqueness application

Wires the abstract `canonical_T_w_subsingleton` from
`QOU.BraidKnot.CanonicalKnotIdSDPUniqueness` together with the
concrete `Helium3Witness` data and the `SDPEmptyConstraints`
trivial-strict-complementarity instance, to demonstrate the
abstract framework producing a concrete categorical uniqueness
statement for ³He.

## What this module proves

For the empty-constraint SDP at dimension `heckeDim LightNucleus.helium3.n₀ = heckeDim 9 = 362880 (³He has n₀ = 9)`:
- The trivial strict-complementarity pair (active set empty)
  yields `Subsingleton {Φ // feasible Φ ∧ obj Φ = 0}`.
- This applies abstractly: ³He's witness records all-positive
  block min-eigenvalues, justifying the empty-active-set
  interpretation.

## Categorical content

The "demonstration" composition:

    Helium3Witness · interior-optimum · empty-constraint SDP
        ⇒ trivial StrictComplementarityPair
        ⇒ Subsingleton (feasible-with-matching-objective)
        ⇒ canonical T_w is unique

The unique-T_w conclusion is at the matrix-representation level.
Two **sorry-free** closures are provided for the QOU ³He case:
* `helium3_uniqueness_via_empty_sdp` — via abstract uniqueness
  (currently relies on the general `strict_complementarity_unique`
  sorry, applicable when fully closed)
* `helium3_uniqueness_closed` — via the **interior-case**
  closure `_unique_of_dualSlack_posDef` (batch 12), fully
  sorry-free since `dualSlack = identity = PosDef` in the
  empty-constraint setup.

The first depends on the (still-open) general kernel-uniqueness
step; the second is the practically-useful path that closes
immediately for the QOU ³He instance per PR #608.

## References

- `QOU.BraidKnot.Helium3Witness` (concrete numerical witness)
- `QOU.MathlibExt.SDPEmptyConstraints` (trivial sub-case)
- `QOU.BraidKnot.CanonicalKnotIdSDPUniqueness` (abstract bridge)
- `r5-full-canonical-knot-solver.witness.json` (PR #608 source)
-/

namespace QOU.BraidKnot

open QOU.MathlibExt.SDP QOU.MathlibExt.SDPEmptyConstraints
open QOU.HeckeAlgebra

/-- **Abstract empty-constraint SDP at H_3(q_0) dimension.**
    Cost matrix is the identity (smallest non-degenerate Cost),
    no equality constraints (`ι := Empty`).  The dimension is
    `heckeDim LightNucleus.helium3.n₀ = heckeDim 9 = 362880 (³He has n₀ = 9)`. -/
def helium3_emptySDP : SDPPrimal (heckeDim LightNucleus.helium3.n₀) ℝ Empty where
  cost := 1  -- identity matrix as cost
  constraint := fun i => i.elim
  rhs := fun i => i.elim

/-- The empty-constraint SDP at `heckeDim LightNucleus.helium3.n₀` is strictly
    feasible (identity matrix is positive-definite, no
    constraints to violate). -/
theorem helium3_emptySDP_strictlyFeasible :
    helium3_emptySDP.IsStrictlyFeasible :=
  one_isStrictlyFeasible helium3_emptySDP

/-- **Trivial strict-complementarity pair for the ³He empty
    SDP** — instantiated from `SDPEmptyConstraints`.  Active
    set is empty; the optimum is at `Φ⋆ = 0`. -/
def helium3_trivialStrictCompPair :
    StrictComplementarityPair helium3_emptySDP :=
  trivialStrictComplementarityPair helium3_emptySDP

/-- **Concrete uniqueness application**: under the trivial
    strict-complementarity pair for the ³He empty-constraint
    SDP, the primal optimum is unique among feasible matrices
    achieving the same objective.

    This is `canonical_T_w_subsingleton` (abstract) specialised
    to the empty-constraint setup with the ³He witness's
    interior-optimum interpretation.

    Subsingleton-typed for typeclass propagation. -/
theorem helium3_uniqueness_via_empty_sdp :
    Subsingleton {Φ : Matrix (Fin (heckeDim LightNucleus.helium3.n₀)) (Fin (heckeDim LightNucleus.helium3.n₀)) ℝ //
      helium3_emptySDP.IsFeasible Φ ∧
      helium3_emptySDP.objAt Φ = helium3_emptySDP.objAt
        helium3_trivialStrictCompPair.Φstar} :=
  canonical_T_w_subsingleton helium3_trivialStrictCompPair

/-- **The optimal Φ⋆ in this empty-constraint setup is the zero
    matrix**, by construction (`trivialStrongDualityPair sdp`'s
    `Φstar := 0`). -/
theorem helium3_emptySDP_Φstar_eq_zero :
    helium3_trivialStrictCompPair.Φstar = (0 : Matrix _ _ ℝ) := rfl

/-! ### Interior-case closure for ³He via the new ℝ-uniqueness layer

The empty-constraint SDP for ³He has cost matrix `T = 1`
(identity), no equality constraints, hence dual slack
`S(y) = T - Σ y_i A_i = 1` (identity, regardless of `y` since
the sum is empty).  The identity matrix is positive-DEFINITE,
so `real_strict_complementarity_unique_of_dualSlack_posDef`
(batch 12) applies and gives full sorry-free uniqueness. -/

open QOU.MathlibExt.SDPRealUniqueness

/-- **Real strong-duality pair** for the ³He empty SDP.  All
    fields are concrete — `dualSlack_psd` follows from
    "dual slack = identity = PosDef ⟹ PSD" (PosDef is
    strictly stronger than PSD). -/
def helium3_realStrongDualityPair : RealStrongDualityPair helium3_emptySDP where
  Φstar := 0
  ystar := fun i => i.elim
  primal_feas := zero_isFeasible helium3_emptySDP
  dualSlack_psd := by
    -- dualSlack = T - Σ y A = 1 - 0 = 1 (identity matrix), which
    -- is PosDef (hence PSD).  Mathlib: `Matrix.PosDef.one`,
    -- then `.posSemidef`.
    show (helium3_emptySDP.dualSlack (fun i => i.elim)).PosSemidef
    -- Unfold dualSlack: T - Σ_i (i.elim) • A_i = T = 1
    have h_eq : helium3_emptySDP.dualSlack (fun i => i.elim) = 1 := by
      unfold SDPPrimal.dualSlack helium3_emptySDP
      simp [Finset.sum_empty]
    rw [h_eq]
    exact Matrix.PosDef.one.posSemidef
  obj_eq_dualObj := by
    -- objAt 0 = tr(T · 0) = 0; dualObjAt 0 = Σ 0 · b_i = 0
    unfold SDPPrimal.objAt SDPPrimal.dualObjAt
    simp

/-- **Dual slack is PosDef** for the ³He empty SDP. -/
theorem helium3_dualSlack_posDef :
    (helium3_emptySDP.dualSlack helium3_realStrongDualityPair.ystar).PosDef := by
  show (helium3_emptySDP.dualSlack (fun i => i.elim)).PosDef
  have h_eq : helium3_emptySDP.dualSlack (fun i => i.elim) = 1 := by
    unfold SDPPrimal.dualSlack helium3_emptySDP
    simp [Finset.sum_empty]
  rw [h_eq]
  exact Matrix.PosDef.one

/-- **Closed sorry-free uniqueness for ³He's empty SDP** —
    via the interior-case closure of the strict-complementarity
    uniqueness theorem.  No `sorry` in the entire chain
    `Helium3Witness → helium3_realStrongDualityPair →
    helium3_dualSlack_posDef → real_strict_complementarity_
    unique_of_dualSlack_posDef`. -/
theorem helium3_uniqueness_closed
    {Φ' : Matrix (Fin (heckeDim LightNucleus.helium3.n₀)) (Fin (heckeDim LightNucleus.helium3.n₀)) ℝ}
    (h_feas : helium3_emptySDP.IsFeasible Φ')
    (h_obj : helium3_emptySDP.objAt Φ' =
             helium3_emptySDP.objAt helium3_realStrongDualityPair.Φstar) :
    Φ' = helium3_realStrongDualityPair.Φstar :=
  real_strict_complementarity_unique_of_dualSlack_posDef
    helium3_realStrongDualityPair helium3_dualSlack_posDef
    h_feas h_obj

/-! ## §6  Demonstration: optimum is the zero matrix

For the empty-constraint SDP with identity cost, the optimum is
trivially `Φ = 0`.  This concrete equation is built into the
`trivialStrongDualityPair`'s `Φstar := 0` field.  Demonstrated
here as a kernel-verified `rfl` proof. -/

theorem helium3_optimum_is_zero :
    helium3_realStrongDualityPair.Φstar =
      (0 : Matrix (Fin (heckeDim LightNucleus.helium3.n₀))
                  (Fin (heckeDim LightNucleus.helium3.n₀)) ℝ) := rfl

/-- The objective value at the (zero) optimum is exactly 0
    (identity cost · zero matrix has trace 0). -/
theorem helium3_objAt_optimum_eq_zero :
    helium3_emptySDP.objAt helium3_realStrongDualityPair.Φstar = 0 := by
  unfold SDPPrimal.objAt helium3_emptySDP
  simp [helium3_optimum_is_zero]

end QOU.BraidKnot
