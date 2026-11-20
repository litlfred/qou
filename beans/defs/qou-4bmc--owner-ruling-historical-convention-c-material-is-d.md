---
# qou-4bmc
title: 'OWNER RULING: historical convention-C material is deprecated and leaves the corpus; audit-only'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T19:33:50Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-cdx1
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

## Applied: `binding_k_enumerator` (owner chose option 2)

Producer and witness moved to `computations/_deprecated/`. Nothing imported the
module — all four apparent consumers referenced it in **comments and
docstrings** only, and an earlier grep matched that prose and overstated the
blast radius. Work list dropped 45 → 43 witnesses; future cascades no longer
burn 3600 s timing it out.

**Retiring the producer did not retire its output.** The K it selected is
already a literal in live compute:

- `gap_a1_binding_k_sdp_feasibility.py:288` — *"only K = σ_3^2 is taken from
  binding_k_enumerator.py"*
- `multiterm_cost_deuteron_hopf_probe.py:36` — *"From
  binding-k-enumerator.witness.json for K = [3, 3]"*

So a canonical object selected by a convention-C ranking is still in the corpus,
now with its provenance deprecated out from under it. Deciding whether
`K = σ_3²` survives convention D is a separate question from deprecating the
thing that chose it, and it is not answered by this move.

## NOT applied: the three `y-lambda-*` witnesses — they are not clear-cut

I said these were straightforward (producers already in `_deprecated/`, so the
witnesses follow). **They are not.** `y-lambda-jones-markov-witness.json` has
live consumers, including *paper content*:

| consumer | kind |
|---|---|
| `computations/binding_a3plus_joint_ji_combiner.py` | live producer |
| `mass-theory/alpha-k-derivation-procedure-proof.md` | content block |
| `mass-theory/wedderburn-bratteli-recursion.lean` | content block sibling |
| `mass-theory/wedderburn-bratteli-recursion-proof.md` | content block |

Moving it breaks content references, which is a different order of change from
retiring an unused producer. The other two were not checked — the sweep timed
out — so their status is unknown, not clear.

This is the same shape as `qou-rohl` (a convention-C witness with no producer
feeding six live consumers): **a witness whose producer is deprecated is not
thereby unused.** The ruling says history leaves the corpus; it does not say
what to do when the corpus is still reading it. That needs answering per
witness, with the content blocks in scope.


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

The owner ruling that historical convention-C material is deprecated and
leaves the corpus, audit-only. A ruling to be ENACTED, not a site to measure.
Live until the material moves.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8419, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
