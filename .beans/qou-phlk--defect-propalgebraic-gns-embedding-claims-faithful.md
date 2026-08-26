---
# qou-phlk
title: 'DEFECT: prop:algebraic-gns-embedding claims faithfulness on H_inf(q); its proof gives H_inf/rad'
status: todo
type: bug
priority: normal
created_at: 2026-08-26T21:32:02Z
updated_at: 2026-08-26T21:32:31Z
---

Found while answering `qou-879g`. Scope-(a); the fix is one qualifying clause,
not a retraction of the block.

## The mismatch

[`prop:algebraic-gns-embedding`](content/quantum-observable-universe/observations/algebraic-gns-embedding.md)
states:

> *"The GNS construction yields a separable Hilbert space `H` and a **faithful**
> `*`-representation `π_GNS : H_∞(q) ↪ L(H)`. This embeds the pre-Archimedean
> Hecke algebra as a concrete operator algebra."*

Its own proof,
[`prf:algebraic-gns-embedding`](content/quantum-observable-universe/observations/algebraic-gns-embedding-proof.md),
establishes something weaker and says so:

> *"…the GNS space is the Temperley–Lieb quotient `H_∞(q)/rad ≅ TL_∞(q)`, **not**
> `H_∞(q)` itself."*

and closes faithfulness as *"`a = 0` **in the trace-quotient**"*.

## Why it is a real defect and not a reading

Under the canonical convention D the radical is **nonzero** — `y_λ = 0` for
`ℓ(λ) ≥ 3` — so `π_GNS` genuinely fails to be injective on `H_∞(q)`. Measured at
n=3 (`computations/qbeta/qbeta_which_algebra_the_decay_channel_lives_in_probe.py`,
11/11): the central idempotent `e_(1³)` is nonzero and the trace form annihilates
its entire ideal. A nonzero element the representation cannot see.

The proof's own parenthetical records that this is convention-dependent: *"Under
the excised convention C every `y_λ` was non-zero and `N` collapsed to 0."* So the
statement was **true under C** and became false when D was made canonical
(2026-08-15). It is a convention-migration casualty, not an original error.

## The fix

Qualify the statement to the trace-quotient — `π_GNS : H_∞(q)/rad ↪ L(H)`
faithful, `≅ TL_∞(q)` under D — which is exactly what the proof establishes. The
`uses:` cone (`prop:wedderburn-weight-canonical`) is unaffected.

## Check the downstream cone before editing

Anything that cites this proposition for *faithfulness on `H_∞(q)`* — rather
than on the quotient — inherits the over-claim. That cone has not been walked.
