---
# qou-4bmc
title: 'OWNER RULING: historical convention-C material is deprecated and leaves the corpus; audit-only'
status: todo
type: task
created_at: 2026-08-10T19:33:50Z
updated_at: 2026-08-10T19:33:50Z
---


## The ruling (owner, 2026-08-10)

> *"if historical it should be deprecated and left alone. shouldnt be in
> corpus. only audit"*

Convention-C material that is retained **because it is history** does not get
kept in place with a clarifying rename or a `convention: C` label. It is
**deprecated, moved out of the live corpus, and left alone**. The only thing
that may reference it afterwards is an audit.

This supersedes the "minimum repair: rename it" recommendation recorded in
`qou-ng7j`, which was mine and was wrong.

## Why it matters more than it looks — `binding_k_enumerator.py`

The obvious reading is that this concerns stale fields. For that producer it
does not: **the historical convention-C value is its ranking criterion.** From
its own docstring:

> ranking by joint Wedderburn-PSD-feasibility + **Markov-trace match against the
> historical `T_w(𝔥)`**
>
> Score by Markov-trace match: `tr_M(constituent_product · K)` at `H_{3A}`
> should agree with **the historical `tr_M(T_w(𝔥))`** at `H_{n_braid}` modulo
> Markov stabilization.

and the stabilization uses convention C's `z` (line 150,
`1/(q^{1/2} + q^{-1/2})`), applied at line 351 as
`historical_markov_at_braid * z ** (n_0 − n_braid)`.

So the producer **selects the canonical binding operator K by agreement with
convention-C numbers**, in live compute, and publishes
`historical_markov_at_braid` + `stabilization_z = 0.4993203341836945` into
`binding-k-enumerator.witness.json` for three atoms. Under convention D that
ranking measures agreement with history, not with the current convention.

That is materially worse than a stale field: a stale number is wrong data, this
is a wrong *selection criterion*, and the thing it selects is a canonical
object (Issue #604 deliverable 3).

## The decision this forces — needs the owner, not me

The ruling is unambiguous about the material. It does not by itself say what
happens to a producer whose *scoring function* is the historical material.
Three coherent outcomes:

1. **Re-reference it.** Keep the enumerator, replace the historical
   convention-C target with the convention-D `tr_M` of the same object. The
   search is still meaningful; only the target moves. Requires a D-convention
   `T_w(𝔥)` to exist.
2. **Deprecate the producer.** If the historical `T_w(𝔥)` *is* the reference —
   i.e. the enumerator exists to reproduce a historical identification — then
   under the ruling the whole producer is history and moves to `_deprecated/`,
   along with its witness.
3. **Split it.** Keep the PSD-feasibility enumeration (convention-independent)
   in the corpus; move the historical Markov-trace scoring into an audit.

I have not applied any of these. Deleting or retiring an Issue #604 deliverable
on my own reading of a one-line ruling is exactly the kind of scope call that
should be confirmed, and option 1 depends on a convention-D `T_w` I have not
established exists.

## Others in scope of the same ruling

- `y-lambda-jones-markov-witness.json`, `y-lambda-sdp-witness.json`,
  `y-lambda-wenzl-bridge-numeric-witness.json` — producers already in
  `_deprecated/`, witnesses still live in `computations/`. Straightforwardly
  covered: the witnesses follow their producers out.
- `audits/weight-factor-audit` C8 criterion — evaluates the convention-C `z`
  **on purpose**, and is an audit, so it is explicitly fine where it is.
- `bond-extensivity-equal-weight`'s stored `f_bond.pp = 0.4993203341836944` —
  a stored, non-recomputed value equal to `z_C`; needs classifying as history
  or as a live number before it can be sorted.

## Close condition

No live (non-`_deprecated/`, non-audit) producer or witness carries
convention-C material retained for historical reasons; the
`binding_k_enumerator` question is answered by the owner and applied; and the
three `y-lambda-*` witnesses have followed their deprecated producers.
