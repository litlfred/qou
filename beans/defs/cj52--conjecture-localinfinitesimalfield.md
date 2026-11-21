---
# cj52
title: 'Conjecture carrier: LocalInfinitesimalField (LocalInfinitesimalField.lean) — §3b, framework/substrate §3b carrier'
status: todo
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-07-05T13:20:00Z
updated_at: 2026-11-20T08:32:31Z
parent: qou-3kkl
---

§3b conjecture-class Lean carrier `instance : LocalInfinitesimalField := sorry` at folio/quantum-observable-universe/lean/QOU/AppendixSurreals/LocalInfinitesimalField.lean:49. The sorry IS the conjecture (per AGENTS.md §3b) — do NOT fabricate an instance (audit-dodge). Category: framework/substrate §3b carrier. Track backing/derivation status; advance only via genuine derivation or owner-directed reframing. Parent: b9cj.


**2026-11-20T08:32:31Z — owner-approved status change (coordinator session_01VQDpPdnjTBLBcPi6D5gj61, PR #8542 batch C):** in-progress → todo. Open conjecture: stale claim released; never to be completed while the conjecture is open (AGENTS rule 13a).


## 2026-11-21T12:09:57Z — location corrected; supersession check (bean drain, pnp-collatz sibling, https://claude.ai/code/session_01Qmmkt4pcG1jyT27PJvFyQ3)

Superseded-premise check (owner request 2026-11-21): rests on none of the superseded premises; pure surreal/standard-part mathematics.

The body's carrier description is stale. On main `2ae54ab40` there is **no** `instance : LocalInfinitesimalField := sorry`. `LocalInfinitesimalField.lean:102` declares `class LocalInfinitesimalField (X : Type v) (K : Type u) [SurrealField K] …`; **no instance exists anywhere** (the only grep hit, line 119, is commented-out history of a removed `axiom`). Sorry-free consumers in the file: `standardPart_eq_zero`, `standardPart_const`, `leadingCoeff_eq`, `exists_distinct_points`, `sub_infinitesimal`, `not_forall_eq_const`, plus `not_of_subsingleton` (refutes it on a subsingleton `X`, so it is not trivially inhabited). Caveat inherited from bean `hypr` §CORRECTION: `SurrealField`'s birthday axioms admit a two-valued birthday, so any `SurrealField`-generic statement is weaker than its prose. Status unchanged: open.
