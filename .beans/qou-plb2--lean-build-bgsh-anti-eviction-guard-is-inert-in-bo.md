---
# qou-plb2
title: lean-build-bg.sh anti-eviction guard is INERT in both directions on a trace-paired restore
status: todo
type: task
priority: normal
created_at: 2026-09-13T05:41:01Z
updated_at: 2026-09-13T05:41:01Z
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
