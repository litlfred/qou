---
# cj2b6
title: 'Conjecture carrier: QouPNeqNp (QouPNeqNp.lean) — §3b, framework/substrate §3b carrier'
status: todo
type: task
priority: low
created_at: 2026-07-05T13:20:00Z
updated_at: 2026-08-19T14:01:10Z
parent: b9cj
---

§3b conjecture-class Lean carrier `instance : QouPNeqNp := sorry` at content/quantum-observable-universe/lean/QOU/Information/QouPNeqNp.lean:75. The sorry IS the conjecture (per AGENTS.md §3b) — do NOT fabricate an instance (audit-dodge). Category: framework/substrate §3b carrier. Track backing/derivation status; advance only via genuine derivation or owner-directed reframing. Parent: b9cj.

STATE (2026-07-24 week-review). The chippable program around this carrier has LANDED on main, all sorry-free — do NOT re-derive:
- `ObstructionGenericity.lean` (d7682e8a): nonzero obstruction vanishes at finitely many params ⇒ non-vanishing is cofinite/generic.
- `PNeqNpEquivalence.lean` (bcc71d44): §3b-cond decomposition of the equivalence into `ResidueFaithfulness` (soundness res≠0⇐P≠NP auto; faithfulness res≠0⇒P≠NP = the open leg); `equivalence_collapse`, `chi_mod_vanishes_iff` (−6 mod n = 0 ⇔ n|6), `nontorsion_of_one_lt` — sorry-free.
- χ(A)=−6 chain cited (f6c7b9cd) via `ex:chi-minus-six-derivation` + `prf:qou-obstruction-reduction`; cited complexity layer + counting/decision gap isolated (6c8d4d73); Wenzl bridge stages 1–2 (ccd66dcc, 5308e0b3) discharge the semisimplicity leg sorry-free.
The SOLE remaining open content = the faithfulness direction (res≠0 ⇒ P≠NP), which needs a formal complexity-theory layer (P, NP as an opaque Prop today). Large research gap, NOT a quick chip; the honest `sorry` stays. Active sibling on the semisimplicity/Wedderburn frontier: PR #4114 (Wenzl tranche 2). See beans qou-b8wj (review), qou-e32b (faithfulness leg), qou-yprr (Wenzl coord).


## Location corrected 2026-08-19 (audit `qou-2yrn`)

This bean's body says the carrier is `instance : QouPNeqNp := sorry` at
`QouPNeqNp.lean:75`. **That shape and that line are both stale** — there is no
instance in the file at all, and no `sorry`. Current state on main:

- `class QouPNeqNp (decisionCost : M → ℕ → ℕ) (residual : ℝ) : Prop` (line 89), one
  field `faithful : residual ≠ 0 → PNeqNPInQOU decisionCost` — the conjecture.
- **No instance anywhere in the corpus.** The open state is represented by the
  *absence* of an instance, which is the honest §3b form, rather than by a `sorry`.
- Consumers carry `[QouPNeqNp …]` explicitly (`qou_implies_p_neq_np`,
  `qou_implies_p_neq_np_at_chi`); file has 0 real sorries.

The do-not-fabricate warning this bean carries is **correct and still load-bearing** —
it is now the primary live tracker for the conjecture, since the sibling bean `qou-b7j7`
(which asked an agent to *prove* the instance) has been scrapped as an attractive
nuisance. History: an earlier revision carried a fabricated `⟨0, rfl⟩` instance
(sign-backwards, this bean's own finding) and then a named `axiom` discharging it; both
were removed by PR #4687 (bean `qou-ex7j`).

Also worth recording for whoever picks this up: the `res ≠ 0` half of the implication is
**not** where the difficulty is. `chiResidual` is a `def … : ℝ := -6` and
`chiResidual_ne_zero` closes by `norm_num`, so that leg is discharged definitionally.
The entire open content is the `faithful` transfer — consistent with the content block,
which says so explicitly and notes that a concrete non-vanishing is Zariski-open (hence
generically true) and so cannot discharge the conjecture on its own.
