---
# qou-m7a2
title: 'Conjecture carrier: RegularityBreakdown — fabricated trivial-zero instance, asserts nothing'
status: completed
type: task
priority: normal
created_at: 2026-08-29T19:46:36Z
updated_at: 2026-08-30T07:22:32Z
parent: qou-rq9n
---

Carrier at ConditionalClasses.lean:90; instance `regularity_breakdown_canonical` at :117.
Field: `exists_breakdown_measure : forall (s : R), 0 <= s -> exists mu : R, 0 <= mu /\ mu <= s`.
Discharged `<0, le_refl 0, hs>`.

Docstring: "Regularity breakdown is concentrated on a measure-zero set." The
field asserts some non-negative mu <= s exists; mu = 0 satisfies it for every
s, so the statement is true whether or not breakdown is concentrated anywhere.
Note the discharger reuses the hypothesis `hs` directly -- the proof term is
the hypothesis, which is the clearest possible signal the conclusion adds
nothing to it.

Bound as `[RegularityBreakdown]` in 5 files. Ledger entries: 0.
Parent: qou-rq9n.
