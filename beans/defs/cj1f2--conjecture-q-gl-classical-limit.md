---
# cj1f2
title: 'Conjecture carrier: q_gl_classical_limit (q_gl_classical_limit.lean) — §3b, framework/substrate §3b carrier'
status: todo
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-07-05T13:20:00Z
updated_at: 2026-11-22T21:58:00Z
parent: qou-m9o4
---

§3b conjecture-class Lean carrier `instance : q_gl_classical_limit := sorry` at folio/quantum-observable-universe/lean/QOU/QGeometricLanglands/q_gl_classical_limit.lean:50. The sorry IS the conjecture (per AGENTS.md §3b) — do NOT fabricate an instance (audit-dodge). Category: framework/substrate §3b carrier. Track backing/derivation status; advance only via genuine derivation or owner-directed reframing. Parent: b9cj.

## Claim reset and applicability review 2026-11-22T21:40:00Z

Reset in-progress -> todo on owner card 2026-11-22 ("Do all three", analytic-conjectures drain thread). No bean update or main commit was carrying this claim. Re-claim with `bun run beans:claim` if you pick it up.

Applicability check against the rulings in force on 2026-11-22 (docs/coordination/owner-rulings.md): strand colour states, the rescaled generator b = -qX, convention D, photon norm 1, block-level U(1)_em charge, the photon/electron words. Verdict: Still applies. The body's `instance : q_gl_classical_limit := sorry` is stale: on main the file declares `class q_gl_classical_limit (R) [Ring R]` with no instance, plus three proved eigenvalue lemmas. Generic ring, so b = -qX (a unit rescaling) does not change the class.

## 2026-11-22T21:58:00Z: applicability review — APPLIES

Owner instruction 2026-11-22 ("reviewed for applicability ... critical analysis"). Checked against docs/coordination/owner-rulings.md on origin/main, git log since the bean's last update, and the state of every PR it cites. Generic-ring class with no instance; the body's `instance := sorry` is stale. A unit rescaling of the generator (b = -qX) does not change it.


Correction 2026-11-22T22:00:00Z: the reset note above lists "photon norm 1" among the rulings checked. That wording was wrong: the 2026-11-22 ruling keeps the photon as 1 + phi0 s0 + phi1 s1 + phi01 s0 s1^-1 with its fixed constant term 1, not a norm-one definition. No verdict here depended on it.
