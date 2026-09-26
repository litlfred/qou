---
# sp07
title: 'C [capstone]: sn_rational_specht_split (SnWedderburnPartitionBridge.lean:232,427)'
status: completed
type: task
priority: low
created_at: 2026-07-05T16:30:00Z
updated_at: 2026-09-26T11:03:23Z
parent: sp00
---

Rational OV-labelled Wedderburn: Q S_n = prod Matrix indexed by partitions. Needs A+B+C + Q-splitness. Capstone.

Parent: sp00.

## MEASURED COMPLETE 2026-09-06 (audit under `qou-1knw` follow-up)

Re-measured with `#print axioms` against freshly-rebuilt oleans. This bean was
`todo`; the declaration it tracks is proved.

`SnWedderburnPartitionBridge.sn_rational_specht_split` —
`[propext, Classical.choice, Quot.sound]`.

\*\*This one needed the closest reading, and nearly read the other way.\*\* It carries
`[SnIsotypicSpechtSplit R]`, and its proof is `⟨(sn_isotypic_specht_split n).choose⟩`
which just unpacks that class's single field. Taken alone that is `X ⊢ X` — the
§3b-cond pattern, and the class docstring even says it exists because "Mathlib
lacks char-0 rationality (Maschke) for S_n".

It is nonetheless \*\*established\*\*, because `SnIsotypicSpechtSplitInstance`
\*\*inhabits the class\*\* — `instSnIsotypicSpechtSplit`, itself axiom-clean, built
from `SpechtWedderburnGeneral.spechtEquiv` (enabled by `QOU.Mathlib.rskBurnsideHolds`),
`algEquivMatrix` for the matrix form, and `SpechtCentralC2Scalar.spechtProduct_centralC2`
for the C₂ clause. Its header states the consequence directly: "until now
\*\*nothing inhabited it\*\* … the results carrying it are unconditional."

So: conditional in \*form\*, established in \*fact\*. Anyone re-auditing this should
check the instance before concluding either way.
