import Mathlib.Tactic
import Mathlib.Data.Real.StarOrdered
import QOU.MathlibExt.SDP
import QOU.MathlibExt.SDPEmptyConstraints
import QOU.MathlibExt.SDPRealUniqueness
import QOU.HeckeAlgebra.Common
import QOU.BraidKnot.CanonicalKnotIdSDPUniqueness

/-!
# QOU.BraidKnot.NucleusEmptySDPUniqueness — generic empty-SDP uniqueness

Parameterised over the strand-count `n : ℕ` (= `3A` where `A = Z + N`
is the nucleon count). Provides ONCE the sorry-free closure of the
strict-complementarity uniqueness theorem for the empty-constraint
SDP at `heckeDim n`, then per-nucleus `Applied*Uniqueness` files
specialise via `abbrev`.

## What this generalises

The previously-duplicated per-nucleus files
(`AppliedHelium3Uniqueness.lean`, `AppliedDeuteronUniqueness.lean`,
`AppliedTritiumUniqueness.lean`) repeated the same proof three
times with only the dimension parameter `n` changing. This module
collapses the duplication: each per-nucleus file becomes a thin
wrapper supplying its `n` value.

## What's nucleus-specific (NOT in this module)

The **real** per-nucleus SDP — with its actual cost function from
the mass formula and its actual non-empty constraints from the
quark / sheet structure — IS nucleus-specific. This module covers
only the abstract-framework demonstration via the empty-constraint
SDP at the appropriate dimension. The "pending" qualifiers in the
existing per-nucleus theorem names (`_pending_multiterm` for ²H,
`_pending_hoefsmit` for ³H) refer to the multi-term cost wiring and
Hoefsmit basis port — separate substantive work.

## What this gives

For any `n : ℕ`:

- `nucleusEmptySDP n` — the SDP at dimension `heckeDim n` with
  identity cost and no constraints
- `nucleusEmptySDP_strictlyFeasible n` — strictly-feasible witness
- `nucleusTrivialStrictCompPair n` — trivial strict-complementarity
  pair (active set empty, Φ⋆ = 0)
- `nucleus_uniqueness_via_empty_sdp n` — Subsingleton uniqueness via
  the abstract `canonical_T_w_subsingleton` (axiom-dependent path)
- `nucleusRealStrongDualityPair n` — concrete real strong-duality
  pair (Φ⋆ = 0, identity dualSlack)
- `nucleus_dualSlack_posDef n` — `dualSlack = 1` is PosDef
- `nucleus_uniqueness_closed n` — **sorry-free uniqueness** via
  `real_strict_complementarity_unique_of_dualSlack_posDef`, no
  axiom dependency
- `nucleus_optimum_is_zero n` — Φ⋆ = 0 by rfl
- `nucleus_objAt_optimum_eq_zero n` — obj at Φ⋆ = 0 by simp

## Usage

```lean
-- AppliedHelium3Uniqueness.lean
abbrev helium3_emptySDP := nucleusEmptySDP 9
abbrev helium3_uniqueness_closed := @nucleus_uniqueness_closed 9
```

Adding a new nucleus (e.g. ⁴He at n = 12):

```lean
-- AppliedHelium4Uniqueness.lean
abbrev helium4_emptySDP := nucleusEmptySDP 12
abbrev helium4_uniqueness_closed := @nucleus_uniqueness_closed 12
```

## References

- `QOU.MathlibExt.SDPRealUniqueness` (the ℝ-uniqueness layer this
  parameterised proof composes with)
- `QOU.MathlibExt.SDPEmptyConstraints` (the trivial sub-case)
- `QOU.BraidKnot.CanonicalKnotIdSDPUniqueness` (the abstract bridge)
- `docs/coordination/2026-05-30-sdp-uniqueness-status.md` (the
  audit that motivated this refactor)
-/

namespace QOU.BraidKnot

open QOU.MathlibExt.SDP QOU.MathlibExt.SDPEmptyConstraints
open QOU.MathlibExt.SDPRealUniqueness
open QOU.HeckeAlgebra

variable (n : ℕ)

/-- **Generic empty-constraint SDP at Hecke dimension `heckeDim n`.**
    Cost matrix is the identity; no equality constraints
    (`ι := Empty`). Parameter `n` is the nucleus's strand count
    `3A` where `A = Z + N`. -/
def nucleusEmptySDP : SDPPrimal (heckeDim n) ℝ Empty where
  cost := 1
  constraint := fun i => i.elim
  rhs := fun i => i.elim

/-- The empty-constraint SDP at `heckeDim n` is strictly feasible
    (identity matrix is positive-definite, no constraints to
    violate). -/
theorem nucleusEmptySDP_strictlyFeasible :
    (nucleusEmptySDP n).IsStrictlyFeasible :=
  one_isStrictlyFeasible _

/-- **Trivial strict-complementarity pair for the generic empty
    SDP** — instantiated from `SDPEmptyConstraints`. Active set
    is empty; the optimum is at `Φ⋆ = 0`. -/
def nucleusTrivialStrictCompPair :
    StrictComplementarityPair (nucleusEmptySDP n) :=
  trivialStrictComplementarityPair _

/-- **Generic Subsingleton uniqueness via the abstract bridge.**
    Under the trivial strict-complementarity pair for the
    empty-constraint SDP, the primal optimum is unique among
    feasible matrices achieving the same objective.

    Depends on the `strict_complementarity_unique_axiom`
    (Boyd-Vandenberghe §5.5 + Todd §3.4). For the sorry-free
    closure see `nucleus_uniqueness_closed` below. -/
theorem nucleus_uniqueness_via_empty_sdp :
    Subsingleton {Φ : Matrix (Fin (heckeDim n)) (Fin (heckeDim n)) ℝ //
      (nucleusEmptySDP n).IsFeasible Φ ∧
      (nucleusEmptySDP n).objAt Φ = (nucleusEmptySDP n).objAt
        (nucleusTrivialStrictCompPair n).Φstar} :=
  canonical_T_w_subsingleton (nucleusTrivialStrictCompPair n)

/-- **Trivial Φ⋆ is the zero matrix** (by construction). -/
theorem nucleusEmptySDP_Φstar_eq_zero :
    (nucleusTrivialStrictCompPair n).Φstar =
      (0 : Matrix (Fin (heckeDim n)) (Fin (heckeDim n)) ℝ) := rfl

/-! ## Sorry-free closure via the ℝ-uniqueness layer

The empty-constraint SDP has cost matrix `T = 1` (identity), no
equality constraints, hence dual slack
`S(y) = T - Σ y_i A_i = 1` (identity, regardless of `y` since the
sum is empty). The identity matrix is positive-DEFINITE, so
`real_strict_complementarity_unique_of_dualSlack_posDef` applies
and gives full sorry-free uniqueness.

This closure is **dimension-independent**: the proof at `n = 6`
(²H), `n = 9` (³H, ³He), `n = 12` (⁴He), `n = 18` (⁶Li),
`n = 27` (⁹Be), `n = 33` (¹¹B), or any other `n` is identical.
The previous per-nucleus files duplicated this proof three times. -/

/-- **Real strong-duality pair** for the generic empty SDP. -/
def nucleusRealStrongDualityPair : RealStrongDualityPair (nucleusEmptySDP n) where
  Φstar := 0
  ystar := fun i => i.elim
  primal_feas := zero_isFeasible _
  dualSlack_psd := by
    show ((nucleusEmptySDP n).dualSlack (fun i => i.elim)).PosSemidef
    have h_eq : (nucleusEmptySDP n).dualSlack (fun i => i.elim) = 1 := by
      unfold SDPPrimal.dualSlack nucleusEmptySDP
      simp [Finset.sum_empty]
    rw [h_eq]
    exact Matrix.PosDef.one.posSemidef
  obj_eq_dualObj := by
    unfold SDPPrimal.objAt SDPPrimal.dualObjAt
    simp

/-- **Dual slack is PosDef** for the generic empty SDP. -/
theorem nucleus_dualSlack_posDef :
    ((nucleusEmptySDP n).dualSlack
      (nucleusRealStrongDualityPair n).ystar).PosDef := by
  show ((nucleusEmptySDP n).dualSlack (fun i => i.elim)).PosDef
  have h_eq : (nucleusEmptySDP n).dualSlack (fun i => i.elim) = 1 := by
    unfold SDPPrimal.dualSlack nucleusEmptySDP
    simp [Finset.sum_empty]
  rw [h_eq]
  exact Matrix.PosDef.one

/-- **Sorry-free uniqueness for the generic empty SDP** — via the
    interior-case closure of the strict-complementarity uniqueness
    theorem. No `sorry` in the chain
    `nucleusRealStrongDualityPair → nucleus_dualSlack_posDef →
    real_strict_complementarity_unique_of_dualSlack_posDef`. -/
theorem nucleus_uniqueness_closed
    {Φ' : Matrix (Fin (heckeDim n)) (Fin (heckeDim n)) ℝ}
    (h_feas : (nucleusEmptySDP n).IsFeasible Φ')
    (h_obj : (nucleusEmptySDP n).objAt Φ' =
             (nucleusEmptySDP n).objAt (nucleusRealStrongDualityPair n).Φstar) :
    Φ' = (nucleusRealStrongDualityPair n).Φstar :=
  real_strict_complementarity_unique_of_dualSlack_posDef
    (nucleusRealStrongDualityPair n) (nucleus_dualSlack_posDef n)
    h_feas h_obj

/-- The optimum Φ⋆ is the zero matrix. -/
theorem nucleus_optimum_is_zero :
    (nucleusRealStrongDualityPair n).Φstar =
      (0 : Matrix (Fin (heckeDim n)) (Fin (heckeDim n)) ℝ) := rfl

/-- The objective value at the (zero) optimum is exactly 0. -/
theorem nucleus_objAt_optimum_eq_zero :
    (nucleusEmptySDP n).objAt (nucleusRealStrongDualityPair n).Φstar = 0 := by
  unfold SDPPrimal.objAt nucleusEmptySDP
  simp [nucleus_optimum_is_zero]

/-! ## Active-empty closure route (matches the empirical-witness language)

`nucleus_uniqueness_closed` above closes uniqueness through the
dual-slack-PosDef interior argument.  The R5-full witnesses report the
result in the *active-set* language ("all Wedderburn-block min-eigs > 0
⟹ active set empty"), so we also expose the closure through the
active-empty theorem
`real_strict_complementarity_unique_of_active_empty_and_cost_posDef`.
For the empty-constraint SDP (`ι = Empty`) the active set is empty by
construction and the cost is the PosDef identity, so this route is also
sorry-free and axiom-free — and its hypotheses match the R5-full
witness's reported `active = ∅` certificate directly (e.g. ³He at
`n = 9`: the three Wedderburn-block min-eigs 1.87, 0.53, 0.53 are all
> 0).  This is the first BraidKnot-layer consumer of the active-empty
closure (previously only `SDPRealUniqueness` referenced it). -/

/-- **Trivial real strict-complementarity pair** for the empty SDP:
    empty active set, optimum `Φ⋆ = 0`.  (`ι = Empty`, so the
    active/inactive dual obligations are discharged by `Empty.elim`.) -/
def nucleusTrivialRealStrictCompPair :
    RealStrictComplementarityPair (nucleusEmptySDP n) where
  toRealStrongDualityPair := nucleusRealStrongDualityPair n
  active := ∅
  active_dual_pos := fun i => i.elim
  inactive_dual_zero := fun i => i.elim

/-- **Sorry-free, axiom-free uniqueness via the active-empty route.**
    Discharged by
    `real_strict_complementarity_unique_of_active_empty_and_cost_posDef`
    (active set empty + identity cost PosDef).  Complements
    `nucleus_uniqueness_closed` (dual-slack-PosDef route) with the
    argument whose hypotheses match the R5-full witness's `active = ∅`
    finding directly. -/
theorem nucleus_uniqueness_closed_via_active_empty
    {Φ' : Matrix (Fin (heckeDim n)) (Fin (heckeDim n)) ℝ}
    (h_feas : (nucleusEmptySDP n).IsFeasible Φ')
    (h_obj : (nucleusEmptySDP n).objAt Φ' =
             (nucleusEmptySDP n).objAt (nucleusTrivialRealStrictCompPair n).Φstar) :
    Φ' = (nucleusTrivialRealStrictCompPair n).Φstar :=
  real_strict_complementarity_unique_of_active_empty_and_cost_posDef
    (nucleusTrivialRealStrictCompPair n) rfl
    (Matrix.PosDef.one : ((nucleusEmptySDP n).cost).PosDef)
    h_feas h_obj

end QOU.BraidKnot
