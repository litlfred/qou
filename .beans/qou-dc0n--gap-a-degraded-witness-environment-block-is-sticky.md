---
# qou-dc0n
title: 'GAP: a degraded witness environment block is sticky and the guard goes silent'
status: completed
type: task
created_at: 2026-08-23T13:41:28Z
updated_at: 2026-08-23T13:41:28Z
---


## Measured 2026-08-23 (found while fixing `qou-a9li` on PR #5494)

`WitnessBuilder.save` refreshes `computedAt` but **preserves the on-disk
`environment` block** when the payload is unchanged. The staleness guard
compares the freshly-collected environment against **what is on disk** —
so once a weak record has been written, re-running with the libraries
restored does not repair it, and the guard **stops warning**.

Observed sequence, all on `reeb-g-structural-identity.witness.json`:

| step | env recorded | guard |
|---|---|---|
| run in a container missing clarabel/numpy/scipy, mpmath 1.3.0 | full block preserved (payload unchanged) | ⚠ warns |
| payload changed (my tolerance fix) → fresh write | **degraded**: numpy/scipy/clarabel dropped, mpmath 1.3.0 | ⚠ warns |
| `pip install` the recorded libs, re-run | **still degraded** — block preserved, only `computedAt` moved | **silent** |
| `rm` the witness, re-run | full block restored, matches the replaced copy byte-for-byte | silent (correctly) |

**Why it matters.** The guard's own advice is *"install it and re-run
rather than committing the weaker record"* — and following that advice
verbatim does not work. Worse, the guard goes quiet at exactly the moment
the record is wrong, so an agent that follows the instruction and re-runs
gets a clean run and commits degraded provenance believing it was fixed.

**Workaround today:** delete the witness before re-running, not just
re-run. `computedAt` moving while `environment` does not is the tell.

**Not fixed here** — this is `qou_substrate/witness.py` behaviour and
belongs in its own change, not on a q₀ re-pin PR. Candidate fixes: refresh
`environment` whenever it is collected regardless of payload equality, or
have the guard compare against the *incoming* collection rather than the
on-disk copy, or refuse to preserve a block that is a strict subset of the
one it replaces.

Related: `qou-a9li` (where it surfaced), and the `q0-anchor-consistency-audit`
witness on PR #5494, which was declined for the same degraded-provenance
reason before this mechanism was understood.

## FIXED 2026-08-23 — `environment` is now monotonic

`tools/qou-substrate/python/qou_substrate/witness.py`. Root cause located
exactly: `save()`'s preserve branch **returns above**
`_check_environment_regression`, and `environment` is in
`_EPHEMERAL_META_FIELDS`, so a witness differing *only* in that block counts
as substantively equal and takes that branch — discarding the fresh block and
skipping the guard in one move.

The masking is deliberate and correct for *lateral* changes (a 3.11↔3.12
runtime swap should not rewrite an identical witness). What it also swallowed
was the two non-lateral directions. Fix keeps the anti-churn intent and makes
the block monotonic:

| new vs on-disk | before | now |
|---|---|---|
| stronger (repair) | discarded, file kept weak | **written** — provenance recovered |
| weaker | kept, **silent** | kept, **warned** |
| lateral / equal | preserved silently | preserved silently (unchanged) |

`_environment_is_repair` requires *nothing dropped, nothing downgraded, and at
least one add or upgrade*. Mixed (drops one, adds another) counts as a
**regression**, not a repair — losing a recorded library is provenance damage
whatever arrived with it.

**Monotonicity is what keeps the CI drift loop from coming back.** Only upward
moves write, so two containers alternating cannot ping-pong the file: the
weaker one never writes, and a repair is idempotent once applied. Pinned by
`test_repair_is_idempotent_so_two_containers_cannot_ping_pong`.

**Proved against both versions through the public `save()` API** (the unit
tests import the new helpers, so they cannot run on the old code and prove
nothing by themselves). Same three-step sequence measured on
`reeb-g-structural-identity`:

```
ORIGINAL: REPAIR FAILED: re-running with libs restored left ['mpmath','python']   exit 1
FIXED:    ALL OK                                                                  exit 0
```

**One correction to this bean's original write-up.** It implied the old code
degraded the block on the preserve path. It does not — the preserve branch
kept the on-disk copy in both versions. The old defects were precisely (a) the
repair was impossible and (b) the regression was silent. The degraded *write*
happens on the other path, when the payload also changed, and that behaviour is
unchanged: the block should describe the run that produced the numbers.

Tests: `tools/qou-substrate/tests/test_environment_block_repair.py` (6).
Full suite 86 passed · vendor sync in sync.

`computations/substrate/witness_base.py` is a pure re-export shim over this
module, so there is no second copy to fix and the qou-mass vendored path picks
the fix up for free — checked, because AGENTS.md records that this mirror once
drifted badly enough to mask the very defect its test existed to catch.
