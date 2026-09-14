---
# qou-srb1
title: 'PERF: lean-shadow-verify.sh rebuild phase is SERIAL — 3 of 4 cores idle for the whole shadow build'
status: completed
type: task
priority: normal
tags:
    - lean
    - infra
    - perf
created_at: 2026-09-13T18:10:00Z
updated_at: 2026-09-14T18:40:00Z
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


## 🟩 DONE — parallelised by topological level (PR #7387, 2026-09-14)

Owner-authorised and implemented. `$ORDER` now carries one topological **level**
per line; each level compiles concurrently, levels run in sequence.

### The win, and it is nearly linear

Controlled A/B over **40 mutually independent modules** (one level, no
barriers), same modules both arms, page cache pre-warmed, nothing else running:

| arm | wall | user | sys | cores used |
|---|---|---|---|---|
| 1 job × 4 threads | **3m05.2** | 2m36.5 | 51.7 s | **1.12** |
| 2 jobs × 2 threads | **1m34.3** | 2m40.3 | 47.1 s | **2.20** |

**1.96×, CPU time unchanged** (3m28 vs 3m27) — no overhead penalty, the same
work spread across cores.

**The `1.12` is the finding under the finding.** Lean's *own* threading gets
barely one core on these modules even at `LEAN_NUM_THREADS=4`. That is why job
parallelism pays at all, and it is worth knowing for anything else in this repo
that assumes `LEAN_NUM_THREADS` is doing the work.

## 🛑 THIS BEAN'S PREMISE WAS WRONG, AND IT WAS MINE

The title says **"3 of 4 cores idle"**. That was **inferred from seeing one
`lean` process in `ps`, not measured** — and one `lean` process is not one core.
Measured serial utilisation is **1.12–1.20 cores**, so ~2.8 are idle rather than
3, and more to the point the figure was never established the way the bean
implies. The headroom is real; the evidence offered for it was not.

## 🛑 AND IT DOES NOT ALWAYS WIN — measured, not hypothesised

A cone-40 target (39 modules over **15 levels**, 2.6 per level) ran
**2m52.8 parallel against 2m45.5 serial — 4.4 % SLOWER**, with user and sys both
up. A level of one module is serial plus an `xargs` spawn.

So the answer depends entirely on **level shape**:

| cone | modules | levels | per level | verdict |
|---|---|---|---|---|
| one content sibling | 39 | 15 | 2.6 | **4.4 % slower** |
| full content sweep | 1478 | 27 | ~55 (widest 555) | the regime it is for |

**The sweep case is NOT measured end-to-end.** The A/B would have cost ~12 h of
machine time — the parallel arm alone projected 5.5 h — so what is established
is the mechanism (1.96× on a wide level) and the shape, never a sweep-level
number. The script says exactly that rather than implying a speedup it does not
have.

Note also that the "260 modules" in this bean's own §measured block is
**container-scoped and has already moved**: the same union cone measured **1478**
a day later, because main advanced 252 commits and the dirty set grew to 2646.

### The naive `xargs -P` hazard this bean predicted — quantified

The bean warned that a naive `xargs -P` over `$ORDER` would be wrong. It is, and
the margin is large. The old scan mutated `done` **inside** the loop, so a module
later in `need` than one it imports saw that import already `done` and joined the
**same pass**. Over the whole 2880-module graph:

| | levels/passes | widest | edges in the same or a later level |
|---|---|---|---|
| new (frozen `done`) | 27 | 1305 | **0** |
| old passes | 18 | 1569 | **834** |

`QOU.AlgebraicSubstrate.ConditionalCorollaries` imports
`QOU.AlgebraicSubstrate.ConditionalClasses`, and the old algorithm put **both in
pass 0**. Flattened serially that order was still correct, so this is not a
latent bug being fixed — it is the invariant parallelism needs being
established, and 834 is what it was worth.

### The other properties the bean said must survive

- **Per-module `rm -f` before `lean -o`** — kept, per module. Verified the real
  olean tree is byte-identical (path, mtime, size across 2793 oleans) after a
  parallel rebuild **and** after one killed with `SIGKILL` mid-write: a partial
  write lands on a fresh shadow inode, never through the hardlink.
- **Fail-fast** — seeded failure prints the error body, exits 1, later levels
  never start. `xargs` lets in-flight siblings finish so an `ok` can follow the
  failure; correct, and now documented so nobody "fixes" it.
- **Jobs divide nproc**, `LEAN_NUM_THREADS = nproc/jobs`, `REBUILD_JOBS` to
  override. Only 2×2 and 1×4 were measured here; `lean-library-sweep.py`'s
  "3×1" comparison is *its* workload and is no longer cited as if it were this
  one.
- **Per-module logs** under `$SHADOW/.rb/` — the single shared `.rb.log` would
  have been interleaved into an unreadable report by concurrent workers.

### The follow-up this leaves open

The narrow-cone regression is a **level-barrier artifact**, not a mechanism one.
A global work queue — start a module the moment its own deps are done rather
than when its whole level is — removes the barrier and with it the loss. Not
done here: it is a larger change to the one script that guards the olean tree,
and the level version is the smaller reviewable step. Worth its own bean if
anyone wants the narrow case to stop losing.

Status → completed.
