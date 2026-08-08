---
# qou-lkdf
title: 'The default-target `lake build` has never been verified end to end — "lake green" still means targeted builds'
status: todo
type: task
priority: medium
tags:
    - lean
    - infra
    - ci
    - qou-lkrd
created_at: 2026-08-08T17:30:00Z
updated_at: 2026-08-08T17:30:00Z
---

## What is open

Every Lean claim in the 5₂ lane is verified by **targeted** builds
(`lake build QOU.QBeta.FiveTwoTransport`, and so on, one target per module).
Nobody has run the **default** target — plain `lake build` — to completion and
seen it green.

An attempt on 2026-08-08 was killed by a container restart at ~7200 log lines
with no verdict. That is the entire state of knowledge: **unknown**, not green
and not red.

## Why this is a distinct bean from qou-lkrd and qou-orph

* `qou-lkrd` claimed the default target was **red** on main with 22 errors in
  two modules. **That claim is now false** — re-measured, both modules build
  clean. It was recorded against a ~194-commit-stale base. Do not quote it.
* `qou-orph` establishes that `lake build` compiles only `QOU.lean`'s import
  closure — 786 of 1644 modules (47.8%, at `origin/main` `ee66f30102`) are never
  built. True, and about the modules **outside** the closure.

Neither answers the question here: **does the closure itself build?** That is
what a reviewer hears when told "lake green", and it is not what has been
verified. The scope lesson survived `qou-lkrd`'s retraction and belongs here.

## Attack vectors

### E1 — Just run it, in the background, and record the result with its base sha
`lake build` from `content/quantum-observable-universe/lean`, backgrounded, with
a generous timeout, logging to a file. The only real requirement is that it
**survives the session** — the last attempt died with the container. Record the
verdict *and* the `origin/main` sha, per `qou-mfst`'s format rule; a bare
"green" ages into a false claim within a day at this repo's merge rate.

### E2 — If red: triage by module, do not wire anything
Failures will be main-side and outside this lane (the closure is mostly other
people's work). Produce a per-module list with the actual error, open a bean per
owner-ish cluster, and **do not fix them from a feature branch** — that is how
you collide with siblings. `qou-lkrd`'s original triage is the template; its
*method* was fine, only its base was stale.

### E3 — If green: wire it into a gate, and make the gate say which target it ran
The point is not the one-off result, it is that "lake green" should stop being
ambiguous. A workflow step running the default target, named so the log
distinguishes it from targeted builds. Note CI auto-triggers are disabled
repo-wide since 2026-06-30 for Actions billing, so it would be
`workflow_dispatch`-only like the other two gates — still worth having as the
thing a human can run and quote.

### E4 — Cheap partial: build the closure of just the touched subtree
If the full default target is too slow to be practical, `lake build QOU` with a
timeout still exercises the closure and gives a partial answer. Report it as
partial — **do not let a timeout read as a pass.** That substitution is this
lane's signature failure mode and it has recurred twelve times.

## Do this first

E1. It is one command, it needs no decisions, and its outcome picks between E2
and E3. The only discipline that matters is not reporting the answer until the
command actually finishes — an empty log is not a pass, and a wrapper's exit
code is not lake's.

## Refs

* `qou-lkrd` (the retracted red claim, and the surviving scope lesson),
  `qou-orph` (the 47.8% outside the closure), `qou-mfst` (record the base sha)
* PRs #4776, #4777, #4701 — all three state their Lean verification as
  *targeted per-module builds*, deliberately

**The 5₂ sum rule remains verified to 80 dps, unproved.**
