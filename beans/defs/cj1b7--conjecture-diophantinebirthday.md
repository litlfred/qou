---
# cj1b7
title: 'Conjecture carrier: DiophantineBirthday (DiophantineBirthday.lean) — §3b, famous-open (aspirational §3b encoding)'
status: todo
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-07-05T13:20:00Z
updated_at: 2026-11-22T21:58:00Z
parent: qou-3kkl
---

§3b conjecture-class Lean carrier `instance : DiophantineBirthday := sorry` at folio/quantum-observable-universe/lean/QOU/AppendixSurreals/DiophantineBirthday.lean:50. The sorry IS the conjecture (per AGENTS.md §3b) — do NOT fabricate an instance (audit-dodge). Category: famous-open (aspirational §3b encoding). Track backing/derivation status; advance only via genuine derivation or owner-directed reframing. Parent: b9cj.


## 2026-11-21T12:09:57Z — location corrected; supersession check (bean drain, pnp-collatz sibling, https://claude.ai/code/session_01Qmmkt4pcG1jyT27PJvFyQ3)

Superseded-premise check (owner request 2026-11-21): this bean rests on none of the superseded premises (photon L±, virtual photons, Convention C, one-term trace, trefoil electron, T(2,n_s), fitted/CODATA values in proofs). It is pure number theory.

The body's carrier description is stale. On main `2ae54ab40` there is **no** `instance : DiophantineBirthday := sorry`. `DiophantineBirthday.lean:115` declares `class DiophantineBirthday (trajectory : ℝ → ℕ → ℕ) : Prop` with one field `algebraic_logarithmic`; **no instance exists anywhere** (grep over `folio/**/*.lean`; the only hit is the commented-out history at line 128). The open state is the absence of an instance (honest §3b). The file also proves the class is data-sensitive: `nonempty_of_const_zero` (satisfiable) and `not_of_quadratic` (refutable), so it is not vacuous. Consumer: `transcendental_of_not_logarithmic`, sorry-free. Status unchanged: open, stays in-progress/todo per rule 13a.

## Claim reset and applicability review 2026-11-22T21:40:00Z

Reset in-progress -> todo on owner card 2026-11-22 ("Do all three", analytic-conjectures drain thread). No bean update or main commit was carrying this claim. Re-claim with `bun run beans:claim` if you pick it up.

Applicability check against the rulings in force on 2026-11-22 (docs/coordination/owner-rulings.md): strand colour states, the rescaled generator b = -qX, convention D, photon norm 1, block-level U(1)_em charge, the photon/electron words. Verdict: Still applies. Pure number theory, no dependence on any physics ruling. Carrier is the class at DiophantineBirthday.lean (no instance), as the 2026-11-21 note says.

## 2026-11-22T21:58:00Z: applicability review — APPLIES

Owner instruction 2026-11-22 ("reviewed for applicability ... critical analysis"). Checked against docs/coordination/owner-rulings.md on origin/main, git log since the bean's last update, and the state of every PR it cites. Pure number theory (re-checked 2026-11-21, confirmed here).


Correction 2026-11-22T22:00:00Z: the reset note above lists "photon norm 1" among the rulings checked. That wording was wrong: the 2026-11-22 ruling keeps the photon as 1 + phi0 s0 + phi1 s1 + phi01 s0 s1^-1 with its fixed constant term 1, not a norm-one definition. No verdict here depended on it.
