---
# cj2b6
title: 'Conjecture carrier: QouPNeqNp (QouPNeqNp.lean) — §3b, framework/substrate §3b carrier'
status: todo
type: task
priority: low
parent: b9cj
created_at: 2026-07-05T13:20:00Z
updated_at: 2026-07-05T13:20:00Z
---

§3b conjecture-class Lean carrier `instance : QouPNeqNp := sorry` at content/quantum-observable-universe/lean/QOU/Information/QouPNeqNp.lean:75. The sorry IS the conjecture (per AGENTS.md §3b) — do NOT fabricate an instance (audit-dodge). Category: framework/substrate §3b carrier. Track backing/derivation status; advance only via genuine derivation or owner-directed reframing. Parent: b9cj.

STATE (2026-07-24 week-review). The chippable program around this carrier has LANDED on main, all sorry-free — do NOT re-derive:
- `ObstructionGenericity.lean` (d7682e8a): nonzero obstruction vanishes at finitely many params ⇒ non-vanishing is cofinite/generic.
- `PNeqNpEquivalence.lean` (bcc71d44): §3b-cond decomposition of the equivalence into `ResidueFaithfulness` (soundness res≠0⇐P≠NP auto; faithfulness res≠0⇒P≠NP = the open leg); `equivalence_collapse`, `chi_mod_vanishes_iff` (−6 mod n = 0 ⇔ n|6), `nontorsion_of_one_lt` — sorry-free.
- χ(A)=−6 chain cited (f6c7b9cd) via `ex:chi-minus-six-derivation` + `prf:qou-obstruction-reduction`; cited complexity layer + counting/decision gap isolated (6c8d4d73); Wenzl bridge stages 1–2 (ccd66dcc, 5308e0b3) discharge the semisimplicity leg sorry-free.
The SOLE remaining open content = the faithfulness direction (res≠0 ⇒ P≠NP), which needs a formal complexity-theory layer (P, NP as an opaque Prop today). Large research gap, NOT a quick chip; the honest `sorry` stays. Active sibling on the semisimplicity/Wedderburn frontier: PR #4114 (Wenzl tranche 2). See beans qou-b8wj (review), qou-e32b (faithfulness leg), qou-yprr (Wenzl coord).
