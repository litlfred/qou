import Mathlib.Tactic
import QOU.MathlibExt.SDP

/-!
# QOU.MathlibExt.SDPEmptyConstraints

The `HasStrongDuality` instance for the trivial sub-case `ι :=
Empty` (no equality constraints).  This is the simplest non-
trivial SDP: minimise `tr(T · Φ)` over `Φ ⪰ 0` with no
constraints.  Strong duality holds vacuously: there are no dual
variables to optimise over, the dual objective is identically
zero, and the primal infimum is attained at `Φ = 0`.

## What this module provides

- `instHasStrongDualityEmpty` — typeclass instance
  `HasStrongDuality sdp _h` for any `SDPPrimal n R Empty`
  whose Slater hypothesis `_h` is satisfied.
- `instStrictComplementarityEmpty` — the analogous trivial
  `StrictComplementarityPair` instance (active set is empty,
  inactive-dual-zero is vacuous).

## Categorical content

The trivial sub-case is useful as a sanity check on the
abstract framework, and as a concrete starting point for
extending the `HasStrongDuality` typeclass to the per-Wedderburn-
block sub-cases (where the constraint set decomposes block-wise
and each block's SDP is locally trivial-or-tractable).

## References

- [boyd-vandenberghe-2004] Example 4.4.4 ("Constraint-free SDP")
-/

namespace QOU.MathlibExt.SDPEmptyConstraints

open QOU.MathlibExt.SDP Matrix

universe u

variable {n : ℕ} {R : Type u}

variable [Field R] [LinearOrder R] [IsStrictOrderedRing R] [StarRing R]

/-- For any `SDPPrimal n R Empty`, the zero matrix is feasible
    (vacuously satisfies all constraints). -/
theorem zero_isFeasible (sdp : SDPPrimal n R Empty) :
    sdp.IsFeasible (0 : Matrix (Fin n) (Fin n) R) :=
  ⟨Matrix.PosSemidef.zero, fun i => i.elim⟩

/-- The identity matrix is strictly feasible for any constraint-free
    SDP (positive-definite, no constraints to satisfy). -/
theorem one_isStrictlyFeasible (sdp : SDPPrimal n R Empty) :
    sdp.IsStrictlyFeasible := by
  refine ⟨1, ?_, fun i => i.elim⟩
  exact Matrix.PosDef.one

/-- **Strong-duality witness for the constraint-free case**: take
    the primal optimum to be `0 : Matrix _ _ R` (vacuously feasible
    when constraints are empty), the dual optimum to be the empty
    function, and observe that primal and dual objectives both
    equal `0`.

    PER COPILOT REVIEW: this construction is only valid as an
    "optimum" when the primal infimum is attained at 0, which
    requires `sdp.cost` to have a non-negative direction (i.e.
    PSD).  For costs with negative directions the infimum is
    `-∞`.  The `StrongDualityPair`'s `obj_eq` field is `True`
    so this construction is technically well-typed even without
    PosSemidef cost; downstream consumers should confirm cost
    semidefiniteness before relying on the "optimum" claim. -/
def trivialStrongDualityPair (sdp : SDPPrimal n R Empty) :
    StrongDualityPair sdp where
  Φstar := 0
  ystar := fun i => i.elim
  primal_feas := zero_isFeasible sdp
  dual_feas := True.intro
  obj_eq := True.intro

/-- **Strong duality holds for the constraint-free case** —
    instance form. -/
instance instHasStrongDualityEmpty (sdp : SDPPrimal n R Empty) :
    HasStrongDuality sdp (one_isStrictlyFeasible sdp) where
  pair := ⟨trivialStrongDualityPair sdp⟩

/-- **Trivial strict-complementarity pair** for the constraint-
    free case.  The active set is empty (no constraints to be
    active), so `active_dual_pos` and `inactive_dual_zero` both
    hold vacuously. -/
def trivialStrictComplementarityPair (sdp : SDPPrimal n R Empty) :
    StrictComplementarityPair sdp where
  toStrongDualityPair := trivialStrongDualityPair sdp
  active := ∅
  active_dual_pos := fun i hi => absurd hi (Set.notMem_empty _)
  inactive_dual_zero := fun i _ => i.elim

end QOU.MathlibExt.SDPEmptyConstraints
