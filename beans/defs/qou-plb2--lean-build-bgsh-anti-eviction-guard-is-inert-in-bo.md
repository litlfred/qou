---
# qou-plb2
title: lean-build-bg.sh anti-eviction guard is INERT in both directions on a trace-paired restore
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T05:41:01Z
updated_at: 2026-11-21T14:33:40Z
parent: qou-5vkl
---

## Measured 2026-09-13 by the lean-verifier subagent, on this container

`scripts/lean-build-bg.sh` runs at SessionStart and has a guard meant to skip
`lake build` when it sees a restored olean cache. **The guard cannot fire on the
cache the repo actually ships.**

- It is keyed on `n_olean > 100 && n_trace == 0`, i.e. it protects only the
  *untraced* restores the old blanket rule described. The live seed
  `a792c46d01b` is **100 % trace-paired** (6492 oleans / 6492 paired traces), so
  `n_trace != 0` and the guard **falls through to `lake build`**.
- It also picks the wrong tree for the purpose: `mathlib_lib` resolves to the
  **per-paper** `packages/mathlib/.lake/build/lib/lean` when that directory
  exists, and after a `lake update` that holds **5** oleans (`Cache/*`, the
  `cache` executable) — under the 100 threshold, so it cannot fire on that
  branch either. **The restored 3480 oleans at the ROOT are never looked at.**

So on a restored container the guard is inert in both directions, and a
`lake build` re-fires on **every session start and every compaction**.

## Why it matters
AGENTS.md documents the eviction it is supposed to prevent: a concurrent
`lake build` against a restored tree took root mathlib oleans **6990 -> 334**,
and of 536 oleans written in ten minutes **zero** were QOU/UGB/Fred2005. It is
silent — the output reads as ordinary build progress. The restore it would
destroy costs a **1.70 GiB** fetch (1m33s) plus 58 s extract.

## Workaround that works today (not a fix)
Read `/tmp/qou-lean-build-status.json` — it names the current step without any
`pgrep` self-match — and kill the chain **by PID**: the script, its `lake
update`, and the `cache get` child. Never `pkill -f`, which kills the calling
shell too. `cache get` is futile here regardless: the Azure blob 403s every
shard (measured **1655 failed / 0 downloaded of 7335**) — the documented
firewall, not a repo fault.

`flock` on `/home/user/qou/.lake-build.lock` makes the script exit immediately
and is the cheap session-scoped suppression, but taking it is a config change.

## Disposition
Not fixed here. The correct guard keys on the **root** tree and on olean count
alone, not on `n_trace == 0` — but editing a SessionStart hook is a config
change and §"ASK THE OWNER BEFORE CHANGING THINGS" puts it outside the two
exemptions (it neither increases precision nor is fixed by a corpus artifact).
**Owner call.** Default if nothing is done: every session on this container
risks silently losing its restore, and the loss is invisible until a `lean`
run fails for a reason that looks like a source error.

Full measurement in `.claude/agent-memory/lean-verifier/MEMORY.md` (TRAP entry,
2026-09-13).


## Sibling beans on the SAME script — checked, not duplicates

The existence check surfaced two. I created this bean before reading them, then
read them; they are distinct defects in `scripts/lean-build-bg.sh` and its
library, so this stands, but it should not be read in isolation.

- **`qou-n6u5`** (bug, **completed**) — *"calls two functions that do not exist,
  so the local-mathlib redirect never runs"*: `mathlib_local_available` and
  `mathlib_enable_local_redirect` were undefined, so Step 0 was dead code.
  **Verified fixed 2026-09-13**: both are now defined in
  `scripts/lib/lean-env.sh` at lines 130 and 141, and `lean-build-bg.sh:177-178`
  resolves against them. The `completed` status is accurate — recorded because a
  completed bean is worth re-checking rather than trusting, and this one holds
  up. Different part of the script from this bean's guard.
- **`qou-4h26`** (todo) — *"the paper mathlib olean tree is ~1678 modules short
  of the root tree, so `scripts/lean-content-sweep.sh` emits ~855 phantom
  MISSING-OLEAN REDs"*. **Corroborated and then some**: measured here the root
  tree holds **3480** mathlib oleans and the paper tree **6**, a 3474 gap rather
  than 1678. The 6 are `Cache/*` — the `cache` executable built by the killed
  `lake update`, not a partial mathlib. It does **not** bite a `lean`-direct run
  on this container, because `scripts/lean-direct-env.sh` sets an 11-entry
  `LEAN_PATH` spanning all eight root package build dirs plus all three paper
  build dirs, so the root tree is on the path; and there is exactly **one**
  `Mathlib/` olean root here, so nothing shadows. That is a statement about
  `lean`-direct, not about `lean-content-sweep.sh`, which `qou-4h26` still owns.

Three open-or-recent beans now touch this one script. That density is itself
worth noting to whoever next edits it.

## 2026-11-21 — lean-build-red drain (issue #8817, session https://claude.ai/code/session_01Qmmkt5eovX5GYdZNHqjZdu)

**Completed.** `scripts/lean-build-bg.sh` on main has an early guard (owner OK 2026-11-15, lines ~176-196) that skips lake update / cache get / build whenever a restored Mathlib tree holds more than 3000 oleans, whatever the trace state, unless `QOU_FORCE_LAKE_BUILD=1`. That makes it act in both directions. The root cause of the eviction it guards against is now measured and fixed separately: see qou-r13s (missing `.git` in restored package dirs).
