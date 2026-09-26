---
# sp02
title: 'B: standardPolytabloid_straightening (SpechtStandardBasis.lean ~291) — Garnir straightening'
status: completed
type: task
priority: low
created_at: 2026-07-05T16:30:00Z
updated_at: 2026-09-26T11:03:22Z
parent: sp00
---

Garnir relations / straightening algorithm (Sagan §2.6). Absent from Mathlib. Gives spanning leg of dim=#SYT.

Parent: sp00.

## MEASURED COMPLETE 2026-09-06 (audit under `qou-1knw` follow-up)

Re-measured with `#print axioms` against freshly-rebuilt oleans. This bean was
`todo`; the declaration it tracks is proved.

`SpechtStandardBasis.standardPolytabloid_straightening` —
`[propext, Classical.choice, Quot.sound]`. Signature:
`∀ {k} [Field k] [CharZero k] {μ} (t : Tableau μ), polytabloid t ∈ span k (range standardPolytabloid)`
— the full Garnir spanning conclusion, only `Field`/`CharZero` as hypotheses.
The bean said "Absent from Mathlib", which is true and irrelevant: it was built
in-repo.
