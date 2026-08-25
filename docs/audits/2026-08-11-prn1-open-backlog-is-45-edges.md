# The `prn1` restoration backlog is 45 edges, and 92 % of the scan is not it

Generated 2026-08-11 while opening tranche 7. Bean: `prn1`. Companion to
[`2026-08-10-prune-restoration-prose-corroboration.md`](2026-08-10-prune-restoration-prose-corroboration.md).

The candidate scan (`scripts/scan-uses-candidates.ts`) reports **581** rows:
labels a block's own prose names that its `uses[]` does not reach. Six tranches
have been drawn from it and 47 edges have landed, at a steady 3–4 of 6.

Intersecting those 581 rows against the **170 corroborated edges** — the ones
the prune actually removed *and* whose source prose still names them — gives a
different picture of how much work is left.

## Only 45 of the 581 are prn1 restorations

| | rows |
|---|---|
| scan candidates | 581 |
| — of which the prune removed | **45** |
| — of which were **never declared** | 536 (92.3 %) |

The other 536 are not restorations. They are blocks whose prose names a label
the manifest never pointed at, which is the corpus's ordinary condition: the
corroboration audit's own warning is that *relatedness is not dependency*, and
a mention that was never an edge has no prune record arguing it should become
one. Adding them is authoring a new graph relation, not repairing a damaged
one — the bulk population `prn1` exists to prevent.

## Where the other 125 corroborated edges went

Every one of the 170 accounted for, by the filter that now removes it:

| disposition | edges |
|---|---|
| **OPEN** | **45** |
| already declared (landed in tranches 1–6, or never lost) | 43 |
| rejection ledger — read and declined | 23 |
| now transitively reachable (a landed edge supplies the path) | 18 |
| forward-pointing | 15 |
| `interprets` already carries it | 13 |
| source or target unpositioned in reading order | 13 |

The 18 "now transitively reachable" are the post-batch reduction working as
intended: edges the earlier tranches made redundant without anyone deciding
they were wrong.

## Two whole source kinds have a zero hit rate

Split by the source block's kind:

| source kind | pruned (in scope) | never declared |
|---|---|---|
| `prf:` | **0** | 148 |
| `tbl:` | **0** | 54 |
| `sec:` | **0** | 30 |
| `alg:` | **0** | 5 |
| `lem:` | **0** | 1 |
| `rem:` | 11 | 141 |
| `prop:` | 17 | 39 |
| `conj:` | 2 | 43 |
| `def:` | 7 | 20 |
| others | 8 | 55 |

**238 candidates — 41 % of the scan — sit in kinds where the prune took
nothing.** They are the largest apparent backlog and the emptiest.

### `prf:` is the class worth naming

148 candidates, 88 distinct proof blocks, and not one of them is a pruned edge.
The reason is a convention the corpus already holds: **a proof block declares
its parent statement and nothing else.**

| proof blocks | with `uses[]` | declaring exactly one entry |
|---|---|---|
| 438 | 434 | 391 (89 %) |

A proof naming the definitions and lemmas its argument invokes is what a proof
does. The corpus does not promote those mentions to edges, and the prune never
removed any, so there is nothing here to restore. Whether proof-only
dependencies *should* be declared is a live editorial question — it is simply
not this bean's, and answering it by working these 148 rows one at a time would
change the convention corpus-wide without anyone deciding to.

`tbl:` looks like the same shape one kind over: an extracted data table naming
the proposition it came from. That relation runs parent → table, which is what
`proofs[]`-style navigation already expresses.

## What this changes

The remaining tranches draw from the 45, not the 581. At the observed 3–4 of 6
that is roughly seven or eight more tranches, and then this bean is done —
against ~97 tranches if the scan's full output were treated as the queue.

The scan is still the right instrument; it simply answers a broader question
than the bean asks. Intersecting its output with `corroborated.json` before
tranching is the missing step, and the 45 are listed in the tranche-7 PR.
