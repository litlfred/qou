---
# qou-2yrn
title: 'AUDIT: is res!=0 => P!=NP a THEOREM or an ASSUMPTION in the corpus? (the fulcrum)'
status: completed
type: task
priority: critical
created_at: 2026-08-07T17:28:53Z
updated_at: 2026-08-19T14:01:58Z
---

The whole residue-probe program (A1/A2/C3/C4) is downstream of the implication res!=0 => P!=NP. If that implication is itself a conjecture class / axiom / hand-wave rather than a proved theorem, then computing res!=0 proves NOTHING about P vs NP -- the program is circular. Corpus-grep checklist: docs/audits, content/, computations/, coordination ledgers. Determine: is the implication (a) Lean-proved, (b) a no-instance conjecture class (honest-open), or (c) silently assumed/laundered downstream. Highest-value item in the attack list.


## VERDICT 2026-08-19: **(b) honest-open conjecture class.** Not laundered, not circular.

The implication `res ≠ 0 ⟹ P≠NP` is carried as an **instance-free Lean class**, and the
corpus says so consistently at every layer. All four corpus-grep paths run.

| layer | finding |
|---|---|
| Lean carrier | `class QouPNeqNp (decisionCost) (residual) : Prop` with one field `faithful : residual ≠ 0 → PNeqNPInQOU decisionCost`. **No instance exists anywhere** in `content/`, `computations/` or `docs/`. 0 real sorries. |
| Lean consumers | `qou_implies_p_neq_np` takes `[Q : QouPNeqNp decisionCost r]`; `qou_implies_p_neq_np_at_chi` takes `[QouPNeqNp decisionCost chiResidual]`. Hypothesis visible in the signature, so no `#print axioms` archaeology is needed to see the conditioning. Downstream (`JetHorizonScaffold.separation_of_blocked`, `JetHorizonTransfer.transfer`) are further *class fields*, not instances. |
| `computations/` | **zero** hits for any P≠NP claim. The compute layer makes no complexity claim at all. |
| `docs/audits/` | `2026-08-01-pneqnp-in-qou-two-axis-wall-inventory.md` names `res ≠ 0 ⟹ P≠NP` as "the single open link" and states outright: *"The value of the program is the localization, not a proof."* |
| content block | `conj:qou-p-neq-np` is kind `conjecture`, opens by disclaiming the unconditional Clay problem, and states "The conjecture's entire open content therefore lives in items 1–2 (faithfulness of the residue for the decision boundary), not in the non-vanishing." |

The prior laundering was real but is **already fixed**: PR #4687 (bean `qou-ex7j`, which
names this audit as its motivation) removed a fabricated `⟨0, rfl⟩` instance and a named
`axiom conj_qou_p_neq_np_faithful`, and concretized `PNeqNPInQOU` from an opaque nullary
`Prop` to `¬ FamilyPolyBounded decisionCost`.

### The circularity worry, answered precisely — and it inverts

This bean feared that computing `res ≠ 0` would prove nothing because the implication is
assumed. The real situation is sharper: **`res ≠ 0` is discharged definitionally and does
no work whatsoever.** `chiResidual` is a `def … : ℝ := -6` — a literal — and
`chiResidual_ne_zero` closes by `norm_num`. So the residue-probe program cannot be
circular *via that leg*, because that leg is not an input to anything; 100 % of the
content sits in the un-instantiated `faithful`.

The corpus already anticipates the stronger version of the worry and forecloses it:
`ObstructionGenericity` proves sorry-free that a nonzero polynomial obstruction has a
cofinite non-vanishing locus, so a concrete `χ(A) ≠ 0` at generic `q₀` is Zariski-open —
*generically true, hence easy* — and therefore cannot discharge the conjecture without
collapsing the claimed equivalence. `PNeqNpEquivalence.equivalence_collapse` machine-checks
that asserting the equivalence is exactly asserting P≠NP.

The two-axis inventory adds the structural reason no residue-style probe can ever close
it: `CocenterTraceFactor.not_trace_of_separates_commutator` proves any decision separator
is a **non-trace**, and `χ = −6` is a `K₀` invariant — on the magnitude axis, the wrong
side of the wall.

### Defect found and fixed (the actual deliverable)

The verdict is clean, but the audit surfaced three **stale artifacts still instructing
agents to rebuild the removed instance** — an attractive nuisance, since doing so is
exactly the laundering #4687 undid:

1. `docs/coordination/cited-sorry-formalization-catalog.md` row for
   `instance:QouPNeqNp` at `QouPNeqNp.lean:111` — indexes a `sorry` that no longer
   exists, in a catalog whose standing instruction is "prove it". Struck through with a
   DO-NOT-PROVE warning (not deleted, so a future cataloguing pass does not re-mint it).
   Header total left at 80 and flagged as a known-high snapshot rather than silently
   decremented to a number nobody re-measured.
2. Bean `qou-b7j7`, titled *"PROVE(lean): instance:QouPNeqNp — noncomputable instance :
   QouPNeqNp chiResidual where faithful"* — **scrapped and retitled**
   `RETIRED — DO NOT PROVE`.
3. Bean `cj2b6` — its located shape (`instance : QouPNeqNp := sorry` at line 75) is
   stale; corrected. Its do-not-fabricate warning is right and it is now the primary live
   tracker for the conjecture.

### Scope note

This bean asked a status question and it is answered; it does **not** close the
conjecture, which remains open and correctly labelled everywhere I looked.
