---
# qou-v7ms
title: 'The (2,1) shape objection is a theorem under linearity: trace-factoring functionals at one partition are 1-dimensional'
status: done
type: task
created_at: 2026-09-05T18:25:55Z
updated_at: 2026-09-05T18:25:55Z
---


Follows `qou-kp2z`, which retired the `opaque wedderburnEmbed` and found that of
`qou-qb7p`'s three reasons the `(2,1)` clause could not be discharged, two were
retired by construction and the **shape** objection survived: the embedding
assembles blocks into one matrix, while the clause needs one block's scalar
`C_{(2,1)}` split into three coefficients (volume, surface, Coulomb).

## Why this was prose and not a theorem

`qbeta_wedderburn_bridge_probe.py` said so explicitly, under a heading reading
"WHY NO LEAN THEOREM ACCOMPANIES THIS": the tempting statement — *three
independent coefficients cannot come from one scalar* — is **false as stated**,
because a single real encodes three set-theoretically. Rescuing it needs a
hypothesis, and the probe's own judgement was that manufacturing one would be
the same overreach it exists to document. That judgement was right.

## The hypothesis did not have to be manufactured

**Linearity.** This corpus already commits to it for the Markov trace —
`markovTrace_add`, `markovTrace_smul`, `markovTrace_linear` in `Common.lean`.
Under it the statement is true, and `QOU/HeckeAlgebra/WedderburnTrace.lean` now
proves it:

| declaration | content |
|---|---|
| `traceFunctional` | a functional of the form `Σ_λ c_λ · trace (x λ)` |
| `traceFunctional_injective` | distinct coefficient families give distinct functionals |
| `traceFunctional_supported_apply` | one supported at a single `λ` **is** `c_λ · trace (x λ)` — one coefficient against one number |
| `three_supported_traceFunctionals_dependent` | any three such are linearly dependent, **explicit witness**, not an existence argument |
| `markovTraceOnWedderburn_eq_traceFunctional` | the Markov trace is one of these, with `c = y_·(q₀)` — so the no-go bites the actual object, not an abstract family |

All five: `[propext, Classical.choice, Quot.sound]`.

## What it settles, and what it deliberately does not

It does **not** show the `(2,1)` clause is false. The claim may well be true.
It rules out **one route** — the route the clause itself names — whenever that
route is linear, factors through the Markov trace, and is localised at `(2,1)`.
Three independent coefficients need more than one dimension; the trace supplies
one.

**Where the room is, which is the more useful half.** `f^{(2,1)} = 2`, so the
block is `M₂(ℝ)` — **four** real dimensions, of which the trace reads one. The
information the clause wants is present in the block and destroyed by taking its
trace. A derivation that reads the block rather than its trace is not blocked by
anything here, and that is the direction a future attempt should take.

This is recorded as a constraint on the shape of a derivation, never as a
criterion to search on.

## Surfaces updated

The reader-facing block `unified-iterative-correction-proof.md` (it must not read
as the clause being refuted), and the probe — whose "no Lean theorem" section is
replaced by the theorem, with two new assertions pinning both the no-go and the
statement of where the room is. Probe 11/11.
