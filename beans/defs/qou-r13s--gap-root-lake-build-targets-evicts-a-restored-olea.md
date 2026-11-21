---
# qou-r13s
title: 'GAP: root `lake build <targets>` EVICTS a restored olean cache — 6990 to 334 measured'
status: completed
type: bug
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T21:04:18Z
updated_at: 2026-11-21T15:14:27Z
parent: qou-5vkl
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

## Re-measured 2026-09-04 — the PREMISE has moved; the eviction has not been retested

Fix candidate 3 above ("seed traces alongside oleans ... This is the real fix")
**has landed on the seeding side.** What had not landed is the consumer side
noticing.

`lake-cache/qou-v4-24-0` was reseeded **2026-08-31** (`a2bf415e7a7`,
*"lake-cache: qou at v4-24-0 (6172 oleans, 2443 own)"*). Measured by
stream-listing all 27 parts:

| | |
|---|---|
| oleans in the archive | **6172** |
| oleans with their own `.trace` sibling | **6170** |
| **paired trace coverage** | **100.0 %** |
| unpaired | 2, both QOU own-package (`ChiLambdaW0SignWeighting`, `wigner2_coefficient`) |
| archive size | 2,514,511,602 B (2.34 GiB) across 27 parts — was ~1.6 GB / 18 |

Both seeders refuse a sub-90 % seed as of `c76810d3e4e` (2026-08-07), so a
traced archive is now the expected state rather than an accident.

**Count PAIRED traces, never total.** My first pass counted extensions — 6172
olean against 6182 trace — which is the exact metric
`folio-assistant/scripts/lake-cache.sh` documents as *not a coverage*: a Lake
tree carries many traces belonging to no olean (`cache.trace`, `lake.trace`,
`*.c.o.export.trace`), and the naive ratio reads **192 %** on a 13-olean tree.
Only the paired figure means anything.

### What this changes, and what it does not

**Changed:** the restore recipe's stated ground — *"a restored tarball carries
oleans but no `.trace` files"* — is false for this branch, and the
unconditional `touch .lake/RESTORED-NO-TRACES` it justified now asserts
something false **in the blocking direction**: it forbids a build on a tree
whose traces are present. Replaced in both copies by
[`scripts/lake-restore-trace-check.sh`](../scripts/lake-restore-trace-check.sh),
which sets *or clears* the marker from a measurement and so cannot go stale the
same way. Its `--selftest` asserts both directions plus the naive-ratio trap.

**NOT changed — and this bean stays open for it:** the 2026-08-15 eviction
(6990 -> 334) is real and is **not retracted**. Traces are **necessary** for
Lake to accept a restored olean; they are **not shown sufficient** — a trace
records input hashes, so Lake can still rebuild if the tree it hashes differs.
**Whether `lake build` on a TRACED restore still evicts is UNTESTED.** Testing
it costs a real root build and risks the cache it would be testing, so it is a
deliberate non-measurement, not an oversight. Until someone spends that,
`lean`-direct remains the recommended gate.

### Two further defects found in the same recipe (same PR)

- **`FETCH_HEAD` is mutable** and the main recipe read it ~27 times across
  minutes of streaming; a concurrent `git fetch` splices the tarball from two
  revisions, silently. The *addon* recipe 400 lines below already pinned the sha
  with the comment *"pin ONCE -- FETCH_HEAD is mutable"*; the main one did not.
- **The two copies had drifted.** AGENTS.md carries the `trap` that reaps the
  multi-GB scratch file (a leak AGENTS.md itself records driving a container to
  92K free); the skill copy — which AGENTS.md calls "the full proven recipe" —
  had a bare `mktemp` and no trap, so following the pointer got you the
  unfixed version.

PR #6636.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-04 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-21 — lean-build-red drain (issue #8817, session https://claude.ai/code/session_01Qmmkt5eovX5GYdZNHqjZdu)

**Root cause measured, and it is not the traces.** On a byte copy of a fresh `lake-cache/qou-v4-24-0` restore (3915 oleans in `.lake/packages`), `lake build --no-build Mathlib.Algebra.Group.Defs` printed, for all 8 restored packages,

    info: mathlib: URL has changed; deleting '.../.lake/packages/mathlib' and cloning again

and left **2** oleans. `--no-build` did not prevent it: the deletion happens while Lake resolves dependencies, before any build. The tarball carries oleans and traces but no `.git` and no sources, so Lake cannot read the package remote. `lean_mathlib_url_fix` (`scripts/lib/lean-env.sh`) returns early when `.git` is absent, so it is a no-op after every tarball restore.

**Answer to the open question in this bean** ("whether lake build on a TRACED restore still evicts is UNTESTED"): with `.git` and sources at the manifest rev, it does not. Same copy, after restoring the oleans into lake-cloned package dirs: `lake build --no-build Mathlib.Analysis.Complex.Basic Mathlib.Tactic Mathlib.RepresentationTheory.Basic` exit 0, "All targets up-to-date (3086 jobs)", olean count unchanged.

**Fix on branch `claude/lean-build-red-2026-11-21`** (`33a0869e7c`): new `scripts/lake-restore-package-git.sh` gives each restored git package a shallow checkout at its manifest rev (about 11 s for all 8); `lean-cache-restore.sh` calls it on both paths, non-fatal. Re-tested from a clean copy: script exit 0, then `lake build --no-build Mathlib.Tactic Mathlib.Analysis.Complex.Basic` "All targets up-to-date (3085 jobs)". Scope: dependency oleans only. QOU oleans rebuilt by lean-direct have no matching traces, so `lake build QOU` still recompiles QOU (without evicting Mathlib). Stays in-progress until the branch merges.

2026-11-21: fix on draft PR #8878 (scripts/lake-restore-package-git.sh, wired into lean-cache-restore.sh). Stays in-progress until merge.

2026-11-21: merged in PR #8878 (main 1ec5ab23d9).
