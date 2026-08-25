---
# qou-nxxw
title: free-neutron-decay.py writes its witness relative to CWD, so re-runs silently orphan at the repo root
status: todo
type: bug
priority: normal
created_at: 2026-08-25T02:06:23Z
updated_at: 2026-08-25T02:06:53Z
---

## What

`computations/free-neutron-decay.py` writes `free-neutron-decay.witness.json`
relative to the **current working directory**, not to its own directory. Run
from the repo root — which is how every agent runs producers — it creates an
untracked orphan at `./free-neutron-decay.witness.json` and leaves the tracked
`computations/free-neutron-decay.witness.json` untouched.

Every other producer uses `HERE / "<name>.witness.json"` or `_pb.witness_path`.

## Why it matters more than a stray file

**It makes a re-run look like a reproduction.** Measured this session, three
times in a row on this one witness:

    committed  computations/free-neutron-decay.witness.json  q0 = 1.1099785955541805  (value B)
    re-run     ./free-neutron-decay.witness.json             q0 = 1.1099785827513808  (proton)

I concluded twice that "a fresh re-run reproduces B, so the witness is not
stale." Both times the run had written somewhere else and I was diffing the
committed file against itself. The witness IS stale, by the full 11.5 ppb mu-p
tension, and the producer computes at proton today (`from q_parameter import Q
as q0`, and `q_parameter.Q` resolves proton for this stem — it is in no
manifest list).

The first of those two wrong conclusions was compounded by a second defect
below, so it took three runs to see.

## Second defect on the same witness: `scriptFile` names a CONSUMER

`computations/free-neutron-decay.witness.json` carries
`scriptFile: "derived_masses.py"`. `derived_masses.py` only READS this witness
(line 148, `_FREE_NEUTRON_WITNESS`, for typed-crossing net coefficients); the
writer is `free-neutron-decay.py`. So the provenance field points at a
consumer, and any tool that resolves producer-from-witness — including the
triage I was running — re-runs the wrong script and gets a no-op it reads as
a reproduction.

## Do NOT drain the staleness here

Re-running this producer moves every number by ~11.54 ppb. `derived_masses.py`
`_q_0()` says so in its own docstring: *"Changing the read would move every
number this module emits by ~11.54 ppb, which is the `qou-1c4y` sweep."* That
sweep is the gated bulk migration. Fix the two mechanical defects (write path,
`scriptFile`); leave the value alone.

## Likely the same mechanism elsewhere

Seven untracked `chi-*-at-qca0128e8-50dps.witness.json` files were sitting in
the tree this session, present when an earlier audit ran and absent later — I
attributed them to someone's cleanup. Same shape: producers writing witnesses
into the cwd. Worth a sweep of write paths, not just read paths. A grep for
cwd-relative `.witness.json` opens finds 5 live files, but 4 are audits READING
by name; `free-neutron-decay.py` is the only confirmed writer so far.
