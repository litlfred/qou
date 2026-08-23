---
# qou-uqht
title: 'A producer and a cache share a path: bar_pairing_binding_observable overwrites three committed chi witnesses'
status: todo
type: task
created_at: 2026-08-23T22:13:29Z
updated_at: 2026-08-23T22:13:29Z
---

`computations/bar_pairing_binding_observable.py` uses three **committed
witnesses** as its own private cache. `_load_or_compute_chi()` (~line 108)
looks for `chi-{atom}-h{n}-at-{q_tag}-50dps.witness.json`, compares the cached
`q_str` and `dps` against what it wants, and on a mismatch **recomputes and
overwrites the committed file** with a 12-key cache record —
`legacy.write_text(json.dumps({...}))` at line 152. No `WitnessBuilder`
anywhere in the file.

## What that costs

Measured 2026-08-23, when a regeneration sweep tripped it on three files:

    chi-deuteron-h6-at-q0-50dps    114 -> 60  leaves (47% gone)
    chi-tritium-h9-at-q0-50dps     302 -> 172 leaves (43% gone)
    chi-helium-3-h9-at-q0-50dps    302 -> 172 leaves (43% gone)

The witnesses lost `scriptHash`, `commitSha`, `computedAt`, `durationMs`,
`scriptCommitSha`, `engine`, `engineVersion`, `producer`, `q0Anchor`,
`q0Value`, `q_0_50dps`, `N`, `Z`, `convention`, `description` and
`tr_M_at_q0`, and gained `_provenance`, `kind`, `q_str`.

It is **not truncation** — all three carry `partial: false` with
`n_partitions == n_partitions_total` (11/11, 30/30, 30/30). They are complete
by their own declaration. A longer timeout would not have helped. It is a
schema regression: a cache record written over a witness.

`tr_M_at_q0` is payload, not provenance. That is real data loss.

## Why it is silent

Losing `scriptHash` removes the witness from the self-staleness audit, so it
reads as "not stale" forever. Losing `q0Anchor`/`q0Value` removes it from the
q0 constant staleness gate. Both are BLOCKING gates and both go quieter, not
louder. The blocking provenance gate now catches the loss (5ee66d05a), but the
clobber itself is untouched: run the producer again and it happens again.

## The fix is a path, not a gate

A producer's output and a consumer's cache must not be the same file. Either

  (a) point the cache at a non-witness path (`.cache/` or a `*.cache.json`
      sibling) and leave the committed witnesses read-only to this script; or
  (b) if these files genuinely ARE this script's output, make it write them
      through `WitnessBuilder` so the full envelope is written every time —
      and then the q0-mismatch recompute is legitimate rather than destructive.

(a) is almost certainly right: the files carry `N`, `Z`, `convention`,
`description` and `tr_M_at_q0`, none of which the cache record reproduces, so
something else authored them.

## Related, distinct

Same family as the dead `chi` cache removed in 93e24e23d — that one silently
never hit; this one silently clobbers. And the 29 raw-JSON producers in bean
qou-nm6y's orbit strip provenance by omission; this one strips it by
overwriting.

To restore the three files if nothing has been committed over them:
`git checkout -- <the three paths>`. Re-running the producer reproduces the
damage until the path is separated.

Found by `witness_shape_guard` (4 collapsed / 43 modified) during the
native-wheel regeneration on `claude/mass-table-comprehensive-triage`;
root-caused by the self-staleness drain running alongside it.
