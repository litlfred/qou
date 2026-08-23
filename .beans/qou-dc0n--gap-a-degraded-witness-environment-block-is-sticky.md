---
# qou-dc0n
title: 'GAP: a degraded witness environment block is sticky and the guard goes silent'
status: todo
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
