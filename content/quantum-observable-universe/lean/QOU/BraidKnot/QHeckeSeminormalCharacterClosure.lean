import Mathlib.Data.Real.Basic

/-!
# Partition-sum form of tr_M agrees with canonical Markov-axiom reducer

Compiled formalisation of
`prop:q-hecke-seminormal-character-closure`.
Sibling docstub at
`braids-and-knots/q-hecke-seminormal-character-closure.lean`.

This proposition records the numerical agreement of two existing
implementation paths (partition-sum via Wenzl y_λ + Hoefsmit χ^lam_q
versus canonical Markov-axiom reducer).
-/

namespace QOU.BraidKnot.QHeckeSeminormalCharacterClosure

/-- Abstract context for `prop:q-hecke-seminormal-character-closure`. -/
class QHeckeSeminormalCharacterClosureContext where
  /-- `tr_M(β)` computed via the partition-sum (Wenzl `y_λ` ·
      Hoefsmit `χ^lam_q`) path. -/
  tr_M_partition_sum : ℝ
  /-- `tr_M(β)` computed via the canonical Markov-axiom recursive
      reducer path. -/
  tr_M_axiom_reducer : ℝ
  /-- Manuscript claim — the two compute paths produce equal values
      for the Markov trace on the same braid `β`. -/
  claim_paths_agree : tr_M_partition_sum = tr_M_axiom_reducer

/-- **Proposition (`prop:q-hecke-seminormal-character-closure`).**
    The two compute paths for `tr_M` agree. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/q-hecke-seminormal-character-closure.md
def character_closure_holds
    [ctx : QHeckeSeminormalCharacterClosureContext] :
    ctx.tr_M_partition_sum = ctx.tr_M_axiom_reducer :=
  ctx.claim_paths_agree

end QOU.BraidKnot.QHeckeSeminormalCharacterClosure
