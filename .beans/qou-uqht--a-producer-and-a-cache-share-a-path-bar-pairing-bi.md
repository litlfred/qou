---
# qou-uqht
title: 'A producer and a cache share a path: bar_pairing_binding_observable overwrites three committed chi witnesses'
status: completed
type: task
priority: normal
created_at: 2026-08-23T22:13:29Z
updated_at: 2026-08-23T23:08:53Z
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


---

## RESOLVED 2026-08-23 (ee3ed1a09) — and it was a KEY NAME, not a q0 mismatch

The diagnosis in this bean was right about the mechanism (a producer and a
cache sharing a path) and wrong about the trigger. It said the clobber fires
"on a q₀ mismatch". It fires on **every run**, because the cache-key lookup
named fields that no committed witness carries:

    cached_q = w.get("q_str", w.get("q_0_50dps_str", w.get("q_inv_50dps_str")))

The witnesses store the value under `q_0_50dps` / `q_inv_50dps`, no `_str`
suffix. All three lookups returned `None`, so `cached_q == q_str` was False
unconditionally.

Measured:

    cache hits, old chain :  4 / 12
    cache hits, new chain : 12 / 12

The four that hit are exactly the `-free-` variants — the ones this function
writes itself, which emit `q_str`. Every `atom` variant missed, including
`chi-helium-4-h12-at-q0-50dps` at n=12.

Verified at HEAD rather than inferred: `chi-deuteron-h6-at-q0-50dps.witness.json`
has `q_str=None`, `q_0_50dps_str=None`, `q_inv_50dps_str=None` and
`q_0_50dps='1.1099785827513808075916690956107688798744991218736'` — **exactly
the value the function requests.** The cache was correct and unusable at the
same time.

And it was silent: both "cache miss" messages are guarded on
`cached_q is not None` / `cached_dps is not None`, so a `None` printed nothing.

## The second symptom this also explains

`bar_pairing_binding_observable.py` had been timing out at **900.1 s**, twice,
and was on the undrainable list for it. It was recomputing the full n=12 chi
table through `pn.chi_lambda_all_partitions_mpfr` on every run. **With the
cache reached it completes in 1 second, rc=0.**

A sibling had reported this producer as referencing `chi_lambda_of_word`
directly, which made the 03569d001 numpy/object-dtype fix the obvious suspect
for the timeout. It does not reference it at all — grep finds zero hits, and
its hot path is the Rust mpfr kernel. That sibling's conclusion (the perf fix
did not clear the timeouts) was correct; only the stated reason was wrong.

## Resolution taken

Widened the fallback chain to include the bare names, suffixed names first so
a witness written by this function still wins. The three clobbered witnesses
are restored from HEAD and **stay** restored — a full run now leaves them
untouched (`git status` clean afterwards). Shape guard 5 collapsed -> 1.

The option-(a) path this bean proposed — move the cache to a non-witness path —
is no longer forced, since the cache now hits and never rewrites a committed
file in normal operation. It remains the more robust design and is worth doing
if anyone touches this again: a producer's output and a consumer's cache
sharing a path is a latent trap even when the key works.
