---
# qou-i7ju
title: hadron-knot-table.witness.json is stale on main and its producer cannot finish
status: todo
type: task
priority: high
created_at: 2026-08-30T13:40:13Z
updated_at: 2026-08-30T13:40:13Z
---

`computations/hadron-knot-table.witness.json` disagrees with its own producer
**on `main` today**, before any pending change, and the producer cannot be
re-run to completion in an agent container.

## The pre-existing staleness — measured, and not caused by any open PR

`tr_M(protium)` computed from the current tree is **1.1463376906350053**; the
committed witness asserts **1.123183539266**. That is a 2.1 % disagreement in
a committed published number.

Verified it is not attributable to the in-flight nucleon change (PR #6214) by
computing it **with that change stashed** — identical to the digit,
`1.1463376906350053`. Protium goes through `build_atom_nf`, which that PR does
not touch. So the drift is main's, from some earlier change to the atom
builder or its cone that never regenerated this witness.

Nothing flags it: the witness-staleness machinery keys on `scriptHash` /
`scriptCommitSha`, not on whether the recorded assertions still reproduce.

## Why it cannot be fixed the ordinary way

The producer does not finish. Measured directly 2026-08-30: the three A=1
atoms (`proton`, `neutron`, `protium`) complete in **under 20 seconds**, then
**deuterium** — the first bound atom — runs indefinitely. Killed after
~3.5 minutes of silence here; AGENTS.md records a 50-minute run terminated by
its own timeout, with 16 further atoms after it.

The witness is written **once, after all 19 atoms**, so a partial run produces
nothing. Truncating the `ATOMS` list would produce a *different* witness, not a
regenerated one. Hand-editing the numbers is forbidden.

## What would actually unblock it

Three routes, in increasing order of effort:

1. **Run it where it can finish.** Nothing about the producer is wrong; it is
   simply long. An environment with hours of budget regenerates it as-is.
2. **Make the producer checkpoint** — emit or update the witness incrementally
   per atom rather than once at the end. Then a bounded run refreshes the rows
   it reached, and the wall becomes a partial-coverage question rather than an
   all-or-nothing one. This is a producer change and wants its own decision.
3. **Find the deuterium wall.** AGENTS.md's own note records that the
   `scipy.sparse` boundary once blamed for this was fixed (`da645cf0f32`,
   `46dcfc62a57`) and that what remains is cost, not a defect — `O(dim·nnz)`
   over σ's nonzeros. Whether that cost is reducible has not been looked at.

## Consequence for PR #6214

That PR adds the σ₀² gluon term and moves two more of this witness's
assertions — `tr_M(proton)` +50.00 %, `tr_M(neutron)` +57.50 %. It does **not**
create the staleness; the witness is already stale independently. Blocking a
correct, thrice-cross-checked change behind a pre-existing defect it did not
cause, and cannot fix, would be the wrong trade — but the resulting witness
carries three known-stale assertions instead of one and that must be stated
wherever it is read.
