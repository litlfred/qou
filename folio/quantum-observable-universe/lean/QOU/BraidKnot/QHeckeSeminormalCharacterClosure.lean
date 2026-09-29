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


/-! ### Removed 2026-08-30 — self-assuming projections

- `character_closure_holds` — body was `ctx.claim_paths_agree`: the conclusion was the projected
  field verbatim, so the declaration restated its own hypothesis.

**Why removal.** The content is not lost: it stays in the class field each
declaration projected, which asserts the same proposition under the same
hypotheses. Only the restatement goes. That is the disposition the vacuity
ledger records for this category — *"drop the pseudo-theorem and project the
field at use sites"* — and there were no use sites: each had **zero references
anywhere in the corpus**, including in this file. A caller wanting the fact
writes the projection directly, which is what the removed body did.
Bean `qou-z9ws`.
-/

end QOU.BraidKnot.QHeckeSeminormalCharacterClosure
