---
# cj8c
title: 'Conjecture carrier: jet_convergence_classical_limit (jet_convergence_classical_limit.lean) — §3b, framework/substrate §3b carrier'
status: in-progress
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-07-05T13:20:00Z
updated_at: 2026-10-04T15:14:30Z
parent: qou-j5ch
---

§3b conjecture-class Lean carrier `instance : jet_convergence_classical_limit := sorry` at folio/quantum-observable-universe/lean/QOU/BraidKnot/jet_convergence_classical_limit.lean:44. The sorry IS the conjecture (per AGENTS.md §3b) — do NOT fabricate an instance (audit-dodge). Category: framework/substrate §3b carrier. Track backing/derivation status; advance only via genuine derivation or owner-directed reframing. Parent: b9cj.



**2026-08-01 (PR #4489):** FIXED — removed a FABRICATED trivial instance ⟨fun _=>0,0,tendsto_const_nhds⟩ (audit-dodge). Class was already content-bearing; now instance-less + sorry-free, matching sibling jet_filtered. Conjecture remains OPEN.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-01 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
