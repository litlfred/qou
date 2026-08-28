---
# qou-phlk
title: 'DEFECT: prop:algebraic-gns-embedding claims faithfulness on H_inf(q); its proof gives H_inf/rad'
status: completed
type: bug
priority: normal
created_at: 2026-08-26T21:32:02Z
updated_at: 2026-08-28T19:30:32Z
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


## Cone walked, 2026-08-26 — and it NARROWS this bean

I filed this with *"anything that cites this proposition for faithfulness on
`H_∞(q)` inherits the over-claim. That cone has not been walked."* It has now
been walked. Five consumers; the over-claim reaches **one and a half** of them,
and — correcting my own implication — **the Lean is already right.**

### 1. `QOU/Observations/AlgebraicGnsEmbedding.lean` — CORRECT, no defect

The most consequential consumer, and it does **not** carry the over-claim. It
states faithfulness relative to the trace ideal at both places:

```lean
trM_faithful   : ∀ x, trM (star x * x) = 0 ↔ traceIdeal x
repr_faithful  : ∀ x, (∀ h, repr x h = 0) → traceIdeal x
```

and the field docstring reads *"**Faithfulness on the GNS quotient**"*. It lands
in `traceIdeal`, never at `x = 0`. So the formalisation encodes exactly the
qualified statement the proof gives, and the defect is confined to the `.md`
prose. **I should have checked this before filing** — it is the one consumer
where a formal over-claim would have mattered.

### 2. `index-of-definitions/definition-index.md:668` — inherits, trivially

The one-line summary repeats `H_∞(q) ↪ L(H)`. It mirrors the proposition, so it
is fixed by fixing the proposition; no independent judgement needed.

### 3. `non-commutative-probability-dictionary` — mild, worth a note

Says *"The Hecke algebra under the Markov trace operates as a `(W*, tr)`
probability space"*. Under D the honest object is the **quotient**, since the
trace has a nontrivial kernel. Related: item 2 reads *"the central projectors
`e_λ` partition the unit; the Plancherel measure `w_λ(q) = tr_M(e_λ)` assigns
probability mass"* — under D that mass is **zero** on a nonempty block. Not
wrong (a measure may assign zero) but the same quotient subtlety, and worth one
clause.

### 4. `algebraic-gns-embedding-cfs-consequence` — NOT affected

Speaks of *"the GNS-**image** data"*. Image, not embedding of the whole algebra;
faithfulness on `H_∞(q)` is not load-bearing.

### 5. `q-plancherel-asymptotic-skeleton` — NOT affected

*"We identify `μ_∞^(q)` with a measure on `π_GNS(H_∞(q))`"* — again the image,
which is exactly the formulation that dodges the issue.

## Revised fix

Qualify the proposition (`π_GNS : H_∞(q)/rad ↪ L(H)`, `≅ TL_∞(q)` under D); the
index line follows. Optionally one clause in the probability dictionary. **No
Lean change needed.** Smaller than filed.


## VERIFIED FIXED 2026-08-28 — bean was stale at `todo`

Fixed on main by `7bd726ace8` ("fix(qou-phlk): qualify the GNS embedding to the
trace-quotient — false as written under D"), not by me. Verified all three
surfaces rather than trusting the commit subject:

- **`.md` statement** now reads *"a faithful `*`-representation of the
  trace-quotient"* with `pi_GNS : H_inf(q)/N -> L(H)`, plus a "the quotient is
  not cosmetic" note giving the C-vs-D provenance.
- **`.ts`** carries an `authorNotes` entry recording it as a convention-migration
  casualty rather than an original error.
- **Lean needed no change, and that claim checks out.**
  `AlgebraicGnsEmbedding.lean:71` is
  `repr_faithful : forall (x : A), (forall h : H, repr x h = 0) -> traceIdeal x`
  — the conclusion is `traceIdeal x`, NOT `x = 0`, so the class always stated
  quotient-faithfulness. Same for `trM_faithful` at line 58.

The fix is exactly the "one qualifying clause" this bean predicted. Nothing
downstream moves: the TL-quotient descent argument in `qou-99qc` /
`qou-879g` was already reasoning from the proof, which was correct throughout.
