---
# qou-88nf
title: 'Conjecture carrier: BlowupYekutieli — fabricated trivial-zero instance, asserts nothing'
status: todo
type: task
priority: normal
created_at: 2026-08-29T19:46:36Z
updated_at: 2026-08-30T07:22:32Z
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



## STILL OPEN 2026-08-30 — and now the ONLY vacuous carrier in the file (PR #6122)

Its three siblings were re-encoded and left the vacuous population; `CriticalExponent`
had already. This one could not be, and the reason is specific rather than effort:

**The docstring names a bound it never gives.** "An explicit constant determined by
the substrate scale" says a constant exists and not which. The encoded bound
`1 + T` involves no substrate scale at all and is satisfied by `r = 0` — by NO
blow-up, the negation of the claim the carrier is named for.

The other three were fixed by transcribing a claim their docstrings already made.
Writing a bound here would mean **choosing the constant myself**, which is the step
separating transcription from invention: `r <= f(q0)` for an `f` I picked would
look exactly like the other three fixes and be a fitted value wearing their clothes.

**What closing it needs**, so this is not re-derived: the Yekutieli blow-up rate as
an explicit function of the substrate modulus, from the source `conj:blowup-yekutieli`
points at. With that in hand the encoding is the same shape as its siblings — the
exponent as a class parameter, the field bounding it by that function, and the gate
a refutation probe showing some rate is excluded.

Stated at the declaration in ConditionalClasses.lean so a reader hits it there.
