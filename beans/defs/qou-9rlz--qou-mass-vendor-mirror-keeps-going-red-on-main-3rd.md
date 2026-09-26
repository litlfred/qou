---
# qou-9rlz
title: qou-mass vendor mirror keeps going red on main (3rd observation today)
status: todo
type: bug
priority: normal
created_at: 2026-08-24T18:48:51Z
updated_at: 2026-08-24T18:49:30Z
---

## Three observations in one day, all on clean `main`

`scripts/sync-qou-mass-vendor.py --check` is a **blocking** gate in
`scripts/staleness-gates.sh` (line ~76). It has been red on `main` every time I
checked today, with different contents each time:

| when | main @ | drifted |
|---|---|---|
| ~12:30 UTC | (mid-session) | 3 — `markov_trace_recursive`, `wedderburn_jones_markov`, + 1 witness |
| ~17:20 UTC | `e78b9d0cbd` | 3 (same set) |
| **18:40 UTC** | `ec736782f7` | **21 — all `data/isotopes/canonical-isotope-witness-Z*.json`** |

Each verified by stashing local changes and re-running `--check` on the
otherwise-clean rebased tree, so none of it is my branch's doing.

## Why this is a bug and not just housekeeping

The gate's own comment in `staleness-gates.sh` says it was added **"BLOCKING,
and green on arrival"** and calls out the qou-j6gb pattern — *"the checker
exists, works, ships --check, and is in no array."* It is now in the array and
main fails it anyway, which is the next stage of the same pattern: the checker
exists, is wired, is blocking, and nobody is acting on it.

The 21-file isotope drift is the sharper case: those are **package DATA**, not
modules. A consumer of `qou-mass` reads them as fact.

## What I did NOT do, deliberately

Did not bundle the fix into PR #5687 (Tranche B). All 21 are upstream drift with
no relation to that change, and folding 21 unrelated data files into a
five-function API PR would hurt review and look like scope creep. My own module
changes were already in sync — restoring the 21 left the branch clean.

## Next

1. One `chore(vendor): re-sync the mirror` commit, `--apply` + `--check`, nothing
   else in it.
2. Worth asking WHY it re-drifts: producers write sibling witnesses (AGENTS.md
   names this hazard), so any agent re-running an isotope producer without
   re-syncing re-reds the gate. If that is the mechanism, the durable fix is a
   post-producer sync step, not another manual re-sync.
