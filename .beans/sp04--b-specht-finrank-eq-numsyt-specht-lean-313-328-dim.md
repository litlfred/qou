---
# sp04
title: 'B: specht_finrank_eq_numSYT (Specht.lean:313,328) — dim S^mu = #SYT'
status: done
type: task
priority: low
parent: sp00
created_at: 2026-07-05T16:30:00Z
updated_at: 2026-07-05T16:30:00Z
---

The standard-basis theorem = triangular independence (sp03) + straightening spanning (sp02). Closes once both land.

Parent: sp00.

## MEASURED COMPLETE 2026-09-06 (audit under `qou-1knw` follow-up)

Re-measured with `#print axioms` against freshly-rebuilt oleans. This bean was
`todo`; the declaration it tracks is proved.

`SpechtStandardBasis.specht_finrank_eq_numSYT` —
`[propext, Classical.choice, Quot.sound]`. Signature:
`∀ {k} [Field k] [CharZero k] (μ), finrank k (SpechtSubmodule μ) = numSYT μ`.
The bean said "Closes once both land" (sp02 + sp03); both landed, and it closed.
`SpechtStandardBasis.lean:50` has said \*\*sorry-free\*\* in its own status table
for some time.
