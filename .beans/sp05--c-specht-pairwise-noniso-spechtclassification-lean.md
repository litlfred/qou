---
# sp05
title: 'C: specht_pairwise_noniso (SpechtClassification.lean:414) — distinct shapes non-isomorphic'
status: done
type: task
priority: low
parent: sp00
created_at: 2026-07-05T16:30:00Z
updated_at: 2026-07-05T16:30:00Z
---

Needs specht_isSimple (Phase A) + a distinguishing invariant. Classification leg.

Parent: sp00.

## MEASURED COMPLETE 2026-09-06 (audit under `qou-1knw` follow-up)

Re-measured with `#print axioms` against freshly-rebuilt oleans. This bean was
`todo`; the declaration it tracks is proved.

`SpechtClassification.specht_pairwise_noniso` —
`[propext, Classical.choice, Quot.sound]`, hypotheses `[Field k] [CharZero k]`
plus `nOf μ = nOf ν` and `μ ≠ ν`.
