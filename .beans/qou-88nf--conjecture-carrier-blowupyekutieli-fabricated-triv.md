---
# qou-88nf
title: 'Conjecture carrier: BlowupYekutieli — fabricated trivial-zero instance, asserts nothing'
status: todo
type: task
priority: normal
created_at: 2026-08-29T19:46:36Z
updated_at: 2026-08-29T19:46:36Z
parent: qou-rq9n
---

Carrier at ConditionalClasses.lean:79; instance `blowup_yekutieli_canonical` at :113.
Field: `exists_blowup_rate : forall (T : R), 0 <= T -> exists r : R, 0 <= r /\ r <= 1 + T`.
Discharged `<0, le_refl 0, by linarith>`.

Docstring promises "the blow-up exponent is bounded above by an explicit
constant determined by the substrate scale"; the encoded bound is `1 + T`,
which involves no substrate scale, and is satisfied by r = 0 -- i.e. by NO
blow-up, the negation of the claim the class is named for.

Bound as `[BlowupYekutieli]` in **4** files (the only one of the five not at 5).
Ledger entries: 0. Parent: qou-rq9n.
