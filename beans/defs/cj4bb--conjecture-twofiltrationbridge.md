---
# cj4bb
title: 'Conjecture carrier: TwoFiltrationBridge (TwoFiltrationBridge.lean) — §3b, framework/substrate §3b carrier'
status: in-progress
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-07-05T13:20:00Z
updated_at: 2026-11-22T22:30:00Z
parent: qou-cv7z
---

§3b conjecture-class Lean carrier `instance : TwoFiltrationBridge := sorry` at folio/quantum-observable-universe/lean/QOU/BraidKnot/TwoFiltrationBridge.lean:69. The sorry IS the conjecture (per AGENTS.md §3b) — do NOT fabricate an instance (audit-dodge). Category: framework/substrate §3b carrier. Track backing/derivation status; advance only via genuine derivation or owner-directed reframing. Parent: b9cj.

### Progress (Round 71 — PR litlfred/qou#8300)
- Formalized in PR `litlfred/qou#8300` (`feat/round71-deltalambda-idempotent-ajtrefoil-n5-gbdepth-43c1`, Commit 1 `a2b0ac0a51416e015d2c71b026de5cf8836daab0`, Head `432940fd4ad329afd23f7d920528ba787ac8691a`, `scriptHash: 06c965f4587d`).

## 2026-11-22 — applicability review (wave-2, owner instruction to review older beans against current rulings)

**The carrier encodes a definition, per the 2026-11-16 demoted-conjecture review.** `/mnt/project-files/qou-demoted-conjectures/two-filtration-bridge/result.md` (summary table there): `d_II` in `conj:two-filtration-bridge` is defined by the cases the general proposition then "proves", so the statement is a tautology. The unproved content is two identifications (H-match: Goldman # on Z(H_n) intertwines with orientation reversal on periods; H-parity) plus a knot assignment. It also records an open tension with the Φ_q truncation result (max hook vs the Lusztig a-function). The honest next step is to restate the `TwoFiltrationBridge` class around H-match and H-parity, not to inhabit it. That restatement belongs with the demoted-conjecture relabel (draft PR #8088) and the owner's call. The PR #8300 note above does not change this.
