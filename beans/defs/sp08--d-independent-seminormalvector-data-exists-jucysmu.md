---
# sp08
title: 'D [independent]: seminormalVector_data_exists (JucysMurphy.lean:440) — OV seminormal eigenvector'
status: completed
type: task
priority: low
created_at: 2026-07-05T16:30:00Z
updated_at: 2026-09-26T11:03:23Z
parent: sp00
---

Okounkov-Vershik / Gelfand-Zetlin eigenvector existence in Mtab. Everything AROUND it is assembled sorry-free; this atomic existence is the OV theorem. Needs JM-spectrum semisimplicity + Young idempotent nonvanishing. Famous.

Parent: sp00.

## MEASURED COMPLETE 2026-09-06 (audit under `qou-1knw` follow-up)

Re-measured with `#print axioms` against freshly-rebuilt oleans. This bean was
`todo`; the declaration it tracks is proved.

`JucysMurphy.seminormalVector_data_exists` —
`[propext, Classical.choice, Quot.sound]`. Signature:
`∀ {k} [Field k] [CharZero k] (μ) (T : StandardYoungTableau μ), ∃ v ∈ SpechtSubmodule μ, v ≠ 0 ∧ ∀ s, ρ(JM s) v = cellContent(...) • v`
— \*\*only\*\* `Field` and `CharZero`. No class binder, no smuggled premise.

The bean called this "the OV theorem … Famous" and `priority: low`. It is proved,
and has been for some time.
