---
# qou-5nj1
title: 'Conjecture carrier: NSCounterexample — fabricated trivial-zero instance, asserts nothing'
status: completed
type: task
priority: normal
created_at: 2026-08-29T19:46:34Z
updated_at: 2026-08-30T07:22:32Z
parent: qou-rq9n
---

Carrier at ConditionalClasses.lean:55; instance `ns_counterexample_canonical` at :107.
Field: `exists_singularity_time : forall (D0 : R), 0 <= D0 -> exists T : R, 0 <= T`.
Discharged `fun _ _ => <0, le_refl 0>`.

The field does not mention the initial datum in its conclusion at all -- `D0`
is bound and then unused, so the statement is literally "there exists a
non-negative real". The docstring names the intended content ("the vorticity
diverges in L-infinity as t -> T*") and none of it is present; the field's own
sub-docstring concedes "Trivially: T* = 0 works."

Bound as `[NSCounterexample]` in 5 files. Ledger entries: 0.
Fix is authorial: state finite-time singularity formation (q-deformed
Beale-Kato-Majda). Parent: qou-rq9n.
