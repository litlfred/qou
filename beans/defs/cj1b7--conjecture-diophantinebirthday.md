---
# cj1b7
title: 'Conjecture carrier: DiophantineBirthday (DiophantineBirthday.lean) — §3b, famous-open (aspirational §3b encoding)'
status: in-progress
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-07-05T13:20:00Z
updated_at: 2026-10-04T15:25:49Z
parent: qou-3kkl
---

§3b conjecture-class Lean carrier `instance : DiophantineBirthday := sorry` at folio/quantum-observable-universe/lean/QOU/AppendixSurreals/DiophantineBirthday.lean:50. The sorry IS the conjecture (per AGENTS.md §3b) — do NOT fabricate an instance (audit-dodge). Category: famous-open (aspirational §3b encoding). Track backing/derivation status; advance only via genuine derivation or owner-directed reframing. Parent: b9cj.


## 2026-11-21T12:09:57Z — location corrected; supersession check (bean drain, pnp-collatz sibling, https://claude.ai/code/session_01Qmmkt4pcG1jyT27PJvFyQ3)

Superseded-premise check (owner request 2026-11-21): this bean rests on none of the superseded premises (photon L±, virtual photons, Convention C, one-term trace, trefoil electron, T(2,n_s), fitted/CODATA values in proofs). It is pure number theory.

The body's carrier description is stale. On main `2ae54ab40` there is **no** `instance : DiophantineBirthday := sorry`. `DiophantineBirthday.lean:115` declares `class DiophantineBirthday (trajectory : ℝ → ℕ → ℕ) : Prop` with one field `algebraic_logarithmic`; **no instance exists anywhere** (grep over `folio/**/*.lean`; the only hit is the commented-out history at line 128). The open state is the absence of an instance (honest §3b). The file also proves the class is data-sensitive: `nonempty_of_const_zero` (satisfiable) and `not_of_quadratic` (refutable), so it is not vacuous. Consumer: `transcendental_of_not_logarithmic`, sorry-free. Status unchanged: open, stays in-progress/todo per rule 13a.
