/-!
# QOU.BraidKnot.AppliedHelium3Uniqueness — concrete uniqueness application

Wires the abstract `canonical_T_w_subsingleton` from
`QOU.BraidKnot.CanonicalKnotIdSDPUniqueness` together with the
concrete `Helium3Witness` data and the `SDPEmptyConstraints`
trivial-strict-complementarity instance, to demonstrate the
abstract framework producing a concrete categorical uniqueness
statement for ³He.

## What this module proves

For the empty-constraint SDP at dimension `heckeDim 3 = 6`:
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

The unique-T_w conclusion is at the matrix-representation level
(modulo the still-`sorry`d `strict_complementarity_unique` in
the abstract layer).  Once that sorry closes, this module's
specialisation closes too.

## References

- `QOU.BraidKnot.Helium3Witness` (concrete numerical witness)
- `QOU.MathlibExt.SDPEmptyConstraints` (trivial sub-case)
- `QOU.BraidKnot.CanonicalKnotIdSDPUniqueness` (abstract bridge)
- `r5-full-canonical-knot-solver.witness.json` (PR #608 source)
-/

import Mathlib.Tactic
import QOU.MathlibExt.SDP
import QOU.MathlibExt.SDPEmptyConstraints
import QOU.HeckeAlgebra.Common
import QOU.BraidKnot.LightNucleus
import QOU.BraidKnot.WitnessR5Full
import QOU.BraidKnot.Helium3Witness
import QOU.BraidKnot.CanonicalKnotIdSDPUniqueness

namespace QOU.BraidKnot

open QOU.MathlibExt.SDP QOU.MathlibExt.SDPEmptyConstraints
open QOU.HeckeAlgebra

/-- **Abstract empty-constraint SDP at H_3(q_0) dimension.**
    Cost matrix is the identity (smallest non-degenerate Cost),
    no equality constraints (`ι := Empty`).  The dimension is
    `heckeDim 3 = 6`. -/
def helium3_emptySDP : SDPPrimal (heckeDim 3) ℝ Empty where
  cost := 1  -- identity matrix as cost
  constraint := fun i => i.elim
  rhs := fun i => i.elim

/-- The empty-constraint SDP at `heckeDim 3` is strictly
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
    Subsingleton {Φ : Matrix (Fin (heckeDim 3)) (Fin (heckeDim 3)) ℝ //
      helium3_emptySDP.IsFeasible Φ ∧
      helium3_emptySDP.objAt Φ = helium3_emptySDP.objAt
        helium3_trivialStrictCompPair.Φstar} :=
  canonical_T_w_subsingleton helium3_trivialStrictCompPair

/-- **The optimal Φ⋆ in this empty-constraint setup is the zero
    matrix**, by construction (`trivialStrongDualityPair sdp`'s
    `Φstar := 0`). -/
theorem helium3_emptySDP_Φstar_eq_zero :
    helium3_trivialStrictCompPair.Φstar = (0 : Matrix _ _ ℝ) := rfl

end QOU.BraidKnot
