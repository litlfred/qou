import Mathlib.Data.Real.Basic
import QOU.SchurWeyl.MarkovTraceInstance
import QOU.SchurWeyl.OcneanuWeightWenzl

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


/-! ### The closure, proved

The context class above only *records* that two computed numbers agree.  The
proposition behind it is an identity of traces on the Hecke tower, and it is
proved: `QOU.SchurWeyl.SeminormalRep.eq_wtrace_of_markov` shows that every
Markov trace with the convention-D parameter `z_D = q³/(q²+1)` (the trace the
recursive Markov-axiom reducer computes, since the axioms determine it) equals
the Ocneanu-weighted sum of seminormal characters.  `character_closure` states
that identity in the block's partition-sum form.

Scope: convention D only, over any field `K`, with `q ≠ 0`, `q² + 1 ≠ 0` and
`q²` not a root of unity.  The weight is `ocneanuWeight q z_D λ`; that it agrees
with the Wenzl specialisation `y_λ` used in the block prose is a separate
identification, not proved here.
-/

open QOU.SchurWeyl QOU.SchurWeyl.SeminormalRep in
/-- **Character closure** ([`prop:q-hecke-seminormal-character-closure`]).  For
any Markov trace `T` on the Hecke tower `H_{n+1}(q)` with parameter
`z_D = q³/(q²+1)` and any `x ∈ H_{n+1}(q)`,

    T.tr n x = Σ_{|λ| = n+1} W_λ · tr(ρ_λ(x)),

where `ρ_λ` is the Hoefsmit seminormal representation and `W_λ` the Ocneanu
weight.  The Markov axioms alone fix the left side; the right side is the
partition-sum form. -/
theorem character_closure {K : Type*} [Field K] (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : K) ^ i ≠ 1)
    (T : HeckeCoset.MarkovTraceFamily K q q⁻¹ (q ^ 3 / (q ^ 2 + 1)))
    (n : ℕ) (x : Hecke K q q⁻¹ n) :
    T.tr n x = ∑ ν : {ν : YoungDiagram // ν.cells.card = n + 1},
      ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν.1 * (seminormalRep q hq0 hq2 n ν.2 x).trace := by
  rw [eq_wtrace_of_markov q hq0 hq2 hq21 hgen T n x, wtrace_apply]

/-! ### The weight is Wenzl's `y_λ`

`QOU.SchurWeyl.ocneanuWeight_conventionD_eq_schurPrincipal` proves that the
convention-D Ocneanu weight is Wenzl's level-2 weight, for every Young diagram:
`ocneanuWeight q z_D λ = schurPrincipal 2 (q²) λ / (q²+1)^{|λ|}`.  Substituting
it into `character_closure` gives the closure with the Wenzl weight that the
block prose names.  That `schurPrincipal 2 Q λ` is the weight in Wenzl's paper
is the citation recorded in `QOU.QBeta.WenzlWeightVanishing`; the identity used
here is proved.
-/

open QOU.SchurWeyl QOU.SchurWeyl.SeminormalRep QOU.QBeta.WenzlWeight in
/-- **Character closure with the Wenzl weight**
([`prop:q-hecke-seminormal-character-closure`]).  Under the hypotheses of
`character_closure`,

    T.tr n x = Σ_{|λ| = n+1} (schurPrincipal 2 (q²) λ / (q²+1)^{n+1}) · tr(ρ_λ(x)). -/
theorem character_closure_wenzl {K : Type*} [Field K] (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : K) ^ i ≠ 1)
    (T : HeckeCoset.MarkovTraceFamily K q q⁻¹ (q ^ 3 / (q ^ 2 + 1)))
    (n : ℕ) (x : Hecke K q q⁻¹ n) :
    T.tr n x = ∑ ν : {ν : YoungDiagram // ν.cells.card = n + 1},
      schurPrincipal 2 (q ^ 2) ν.1 / (q ^ 2 + 1) ^ (n + 1)
        * (seminormalRep q hq0 hq2 n ν.2 x).trace := by
  rw [character_closure q hq0 hq2 hq21 hgen T n x]
  refine Finset.sum_congr rfl fun ν _ => ?_
  rw [ocneanuWeight_conventionD_eq_schurPrincipal q hq0 hq21, ν.2]

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
