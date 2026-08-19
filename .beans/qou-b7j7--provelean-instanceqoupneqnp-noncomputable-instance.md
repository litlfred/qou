---
# qou-b7j7
title: 'RETIRED — DO NOT PROVE: instance:QouPNeqNp was removed as laundering (#4687); supplying it would re-launder the conjecture'
status: scrapped
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - infra-blocked
created_at: 2026-08-01T23:31:05Z
updated_at: 2026-08-19T14:00:25Z
parent: qou-k1mq
---

**File:** `QOU/Information/QouPNeqNp.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/Information/QouPNeqNp.lean

### `instance:QouPNeqNp`  —  line 111  ·  tier **B** (infra-blocked / open-conjecture)
- **Proposition:** `noncomputable instance : QouPNeqNp chiResidual where faithful `
- **Cited:** `[manuscript]`
  - [manuscript] quantum-observable-universe/information-theory/qou-p-neq-np.ts
- **Tractability:** §3b conjecture-instance: P ≠ NP — open.
- **Next step:** This sorry IS the open QOU conjecture (§3b instance). No proof attempt — it is the honest open marker. Close only by a genuine derivation, never a fabricated instance.


## SCRAPPED 2026-08-19 (audit `qou-2yrn`) — this bean asked for the laundering, not the proof

**Do not action this bean, and do not regenerate it from the catalog.**

The `sorry` this bean tracked was
`noncomputable instance : QouPNeqNp chiResidual where faithful := sorry` in
`QOU/Information/QouPNeqNp.lean`. It **no longer exists**: PR #4687 (bean `qou-ex7j`)
deliberately removed it, along with a named `axiom conj_qou_p_neq_np_faithful` that had
been discharging the same field.

The reason it was removed is the reason this bean must not be actioned. With a global
instance in scope, `qou_implies_p_neq_np_at_chi` typechecks with **no visible
hypothesis** — it reads as an unconditional QOU-scoped P≠NP separation, and its
dependence on the conjecture is discoverable only by running `#print axioms`. That is
precisely the "Axiomatization is NOT a Proof" pattern in AGENTS.md. This bean's own
title ("PROVE(lean): instance:QouPNeqNp") instructs the next agent to put it back.

### Verified state on main, 2026-08-19

- `class QouPNeqNp (decisionCost) (residual) : Prop` with the single field
  `faithful : residual ≠ 0 → PNeqNPInQOU decisionCost`.
- **No instance of it exists anywhere** — checked across `content/`, `computations/`
  and `docs/`; the only hits are prose and this catalogue lineage.
- Both consumers carry the hypothesis explicitly: `qou_implies_p_neq_np` takes
  `[Q : QouPNeqNp decisionCost r]`, `qou_implies_p_neq_np_at_chi` takes
  `[QouPNeqNp decisionCost chiResidual]`.
- `QouPNeqNp.lean` has **0 real sorries**.

### Where the live item lives

The conjecture is still open — what is retired is the *instance-shaped carrier*, not the
mathematics. `cj2b6` tracks the conjecture and already carries the do-not-fabricate
warning. The catalogue row that generated this bean is struck through in
`docs/coordination/cited-sorry-formalization-catalog.md` with the same warning, so a
future cataloguing pass does not mint this bean again.
