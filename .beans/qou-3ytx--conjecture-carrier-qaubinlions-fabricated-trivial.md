---
# qou-3ytx
title: 'Conjecture carrier: QAubinLions — fabricated trivial-zero instance, asserts nothing'
status: completed
type: task
priority: normal
created_at: 2026-08-29T19:46:33Z
updated_at: 2026-08-30T07:22:32Z
parent: qou-rq9n
---

Carrier at lean/QOU/AlgebraicSubstrate/ConditionalClasses.lean:43; instance `qAubinLions_canonical` at :103.
Field: `exists_compactness_constant : forall (E : R), 0 <= E -> exists K : R, 0 <= K /\ K <= 2 * E`.
Discharged `<0, le_refl 0, by linarith>`.

DOCSTRING OVER-CLAIM (this is the sharp one): the class doc says
*"Concrete content: K scales linearly with the energy bound (the Aubin-Lions
embedding constant)."* The field says only that SOME non-negative K under 2E
exists, which 0 satisfies. Linear scaling is not encoded anywhere. This is
precisely what `proof-claims-unencoded` exists to catch and does not.

Bound as `[QAubinLions]` in 5 files. Ledger entries: 0.
Fix is authorial: encode the q-Aubin-Lions compactness statement.
Parent: qou-rq9n.
