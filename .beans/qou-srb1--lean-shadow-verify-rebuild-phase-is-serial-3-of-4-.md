---
# qou-srb1
title: 'PERF: lean-shadow-verify.sh rebuild phase is SERIAL — 3 of 4 cores idle for the whole shadow build'
status: todo
type: task
priority: normal
tags:
    - lean
    - infra
    - perf
created_at: 2026-09-13T18:10:00Z
updated_at: 2026-09-13T18:10:00Z
---

## The finding

`scripts/lean-shadow-verify.sh`'s rebuild phase compiles the dirty closure one
module at a time:

```sh
for m in $ORDER; do
  ...
  if ! (cd "$PKG" && LEAN_PATH="$LP" lean $LEAN_OPTS "${src#$PKG/}" -o "$out") ...
done
```

The phase that *follows* it — `scripts/lean-content-sweep.sh` compiling its
targets against the finished shadow — is parallel (`-j`, default 3). So on the
4-core container this repo runs in, the rebuild leaves **3 of 4 cores idle**
for its entire duration while the compile phase after it saturates them.

## Measured 2026-09-13

A full content sweep (938 targets, bean `qou-g5sp`):

| phase | work | wall |
|---|---|---|
| shadow rebuild | 260 modules, serial | **~65 min** |
| target compile | 938 files, `-j 2` | **~24 min** |

So the serial phase cost ~2.7× the parallel one while doing under a third of
the module count. `ORDER` is already a topological sort, so the information
needed to parallelise it is present — modules at the same topological level are
independent.

## Why this is NOT urgent, and why it is not a one-line fix

- The rebuild is **once per shadow**, and `SHADOW=<dir>` reuses it across runs.
  An agent sweeping repeatedly pays it once.
- The dirty closure is **container-scoped**: 260 here, 74 in the container
  AGENTS.md quotes. On a container whose olean tree is fresh it may be near
  zero, and this costs nothing.
- Parallelising a topological rebuild wants care. The naive `xargs -P` over
  `$ORDER` is wrong — it must respect levels, and the current loop's
  `rm -f "$out"` before `lean -o` exists specifically because the shadow is
  **hardlinked** to the real olean tree (a write without the unlink lands on
  the shared inode and mutates the tree the shadow exists to protect). Any
  parallel version must preserve that per-module unlink, and its
  before/after olean-count invariant must still hold.

## Suggested shape

Group `$ORDER` into topological *levels* (a module's level is 1 + max level of
its dirty imports), then run each level with a bounded `-P`. Keep `-P` a
divisor of `nproc` for the reason `lean-library-sweep.py --jobs` already
documents: `LEAN_NUM_THREADS` is derived as `nproc // jobs`, so a non-divisor
wastes the remainder.

## How it was found

In passing, while running the full content sweep for `cscb` / `qou-e7xv`
(`docs/audits/2026-09-13-every-content-sibling-compiles-zero-red.md`). Not
fixed there — it is someone's arc, the sweep's own result did not depend on it,
and a speculative parallelisation of the one script that guards the olean tree
is exactly the change that wants its own review.
