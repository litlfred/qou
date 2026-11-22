import Mathlib.Tactic
import QOU.MathlibExt.SDP

/-!
# QOU.MathlibExt.SDPEmptyConstraints

The `HasStrongDuality` instance for the trivial sub-case `ι :=
Empty` (no equality constraints).  This is the simplest non-
trivial SDP: minimise `tr(T · Φ)` over `Φ ⪰ 0` with no
constraints.  There are no dual
variables, the dual objective is identically zero, and the dual slack
is the cost `T`.  So a dual-feasible point exists iff `T ⪰ 0`, and then
the primal infimum `0` is attained at `Φ = 0`.

## What this module provides

- `hasStrongDuality_empty` — `HasStrongDuality sdp _` for any
  `SDPPrimal n R Empty` whose cost is PSD.  (Until 2026-11-15 this was
  an unconditional instance, valid only because the pair's dual-feasibility
  and zero-gap fields were `True`.)
- `trivialStrictComplementarityPair` — the analogous trivial
  `StrictComplementarityPair` (active set empty), same hypothesis.

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
variable [StarOrderedRing R]

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

/-- With no constraints the dual slack is the cost itself. -/
theorem dualSlack_empty (sdp : SDPPrimal n R Empty) (y : Empty → R) :
    sdp.dualSlack y = sdp.cost := by
  simp [SDPPrimal.dualSlack]

/-- With no constraints the dual objective is `0`. -/
theorem dualObjAt_empty (sdp : SDPPrimal n R Empty) (y : Empty → R) :
    sdp.dualObjAt y = 0 := by
  simp [SDPPrimal.dualObjAt]

/-- **Strong-duality pair for the constraint-free case, given a PSD cost.**

    Primal point `0`, empty dual point.  Dual feasibility is exactly
    `cost ⪰ 0` (the dual slack *is* the cost), and both objectives are `0`.

    The hypothesis is necessary, not a convenience.  This used to be stated
    for every cost, which type-checked only because `dual_feas` and `obj_eq`
    were `True`.  For a cost with a negative direction `v` (e.g. `T = -1`,
    `n = 1`) the primal objective `tr(T Φ)` is unbounded below on `Φ ⪰ 0`
    (take `Φ = t · v vᴴ`, `t → ∞`), so there is no optimal pair at all. -/
def trivialStrongDualityPair (sdp : SDPPrimal n R Empty)
    (hcost : sdp.cost.PosSemidef) : StrongDualityPair sdp where
  Φstar := 0
  ystar := fun i => i.elim
  primal_feas := zero_isFeasible sdp
  dual_feas := by rw [dualSlack_empty]; exact hcost
  obj_eq := by simp [SDPPrimal.objAt, dualObjAt_empty]

/-- **Strong duality for the constraint-free case with PSD cost.**
    (Formerly an unconditional global instance; see
    `trivialStrongDualityPair` for why the PSD-cost hypothesis is needed.) -/
theorem hasStrongDuality_empty (sdp : SDPPrimal n R Empty)
    (hcost : sdp.cost.PosSemidef) :
    HasStrongDuality sdp (one_isStrictlyFeasible sdp) :=
  ⟨⟨trivialStrongDualityPair sdp hcost⟩⟩

/-- **Trivial strict-complementarity pair** for the constraint-
    free case with PSD cost.  The active set is empty (no constraints
    to be active), so `active_dual_pos` and `inactive_dual_zero` both
    hold vacuously. -/
def trivialStrictComplementarityPair (sdp : SDPPrimal n R Empty)
    (hcost : sdp.cost.PosSemidef) :
    StrictComplementarityPair sdp where
  toStrongDualityPair := trivialStrongDualityPair sdp hcost
  active := ∅
  active_dual_pos := fun i hi => absurd hi (Set.notMem_empty _)
  inactive_dual_zero := fun i _ => i.elim

end QOU.MathlibExt.SDPEmptyConstraints
