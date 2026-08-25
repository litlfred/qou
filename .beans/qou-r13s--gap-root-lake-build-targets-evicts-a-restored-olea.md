---
# qou-r13s
title: 'GAP: root `lake build <targets>` EVICTS a restored olean cache — 6990 to 334 measured'
status: todo
type: bug
priority: high
created_at: 2026-08-15T21:04:18Z
updated_at: 2026-08-15T21:04:54Z
---

## What

Running the `/prepare-merge` step-4 command from the repo root

    lake build QOU UGB Fred2005

against a root workspace whose Mathlib oleans were **restored from
`lake-cache/qou-v4-24-0`** does not build the paper libraries. It starts
recompiling Mathlib from source AND deletes the restored oleans as it goes.

Measured 2026-08-15 on PR #5106, three checks 10 minutes apart:

| | before | during | after kill |
|---|---|---|---|
| `.lake/packages/mathlib` oleans | **6990** | — | **334** |
| oleans written in last 10 min | — | 536 | — |
| ...of those, under `mathlib/aesop/batteries` | — | **520** | — |
| ...of those, under `QOU`/`UGB`/`Fred2005` | — | **0** | — |

Zero paper-library progress in ten minutes, and the cache the session depended
on was destroyed. Recovery is a full re-fetch + extract of the 1.6 GB cache
tarball.

## Why

AGENTS.md already records the mechanism for the seeding direction (bean
`02kc`): oleans restored by `tar` carry no `.trace` files, so **Lake treats
them as stale, rebuilds them, and evicts them**. What was not recorded is that
this fires on an ordinary *consumer* `lake build` of named library targets —
not just on a seeding attempt — and that it is silent: the output looks like
normal build progress, so a `timeout 3000` will happily burn the full 50
minutes producing nothing.

`local/prepare-merge` §4 warns about a *cold* root cache compiling Mathlib
from source. This is worse and differently shaped: the cache is **warm by
olean count** (6990 looks fully populated, which is why I proceeded), and the
build destroys it anyway. Counting oleans is not a validity check for the
cache — the traces are.

## What to do instead

For verification — which is what step 4 is for — use `lean`-direct against the
real import cone, per AGENTS.md §"QA is agent-owned; CI is a backup":

    export LEAN_PATH="<paper>/.lake/build/lib/lean:<root>/.lake/packages/*/.lake/build/lib/lean"
    lean path/to/Changed.lean          # exit 0 = checks, sorry-free

On PR #5106 that verified the one changed file in **2.4 s** against the same
cone the aborted `lake build` was 50 minutes into not reaching.

## Fix candidates

1. **`local/prepare-merge` §4** — add the eviction case beside the cold-cache
   case, and say that a high olean count does not mean the cache is usable.
   Give `lean`-direct as the sanctioned step-4 gate when the cache is restored
   rather than built.
2. **A guard in the restore recipe** — after `tar xzf`, drop a marker
   (`.lake/RESTORED-NO-TRACES`) and have anything that shells out to `lake
   build` at the root refuse, or warn loudly, when it is present.
3. **Seed traces alongside oleans**, if Lake's trace format permits it, so a
   restored cache is indistinguishable from a built one. This is the real fix
   and the largest; 1 and 2 are cheap and immediate.

Related but distinct: `qou-lkrd` (bare-`lake build` default-target scope gap —
that one builds *nothing*; this one builds the *wrong thing* destructively).
