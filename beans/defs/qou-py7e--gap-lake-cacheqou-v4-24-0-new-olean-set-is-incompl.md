---
# qou-py7e
title: 'GAP: lake-cache/qou-v4-24-0-new olean set is incomplete (missing Mathlib.Algebra.Module.LinearMap.Polynomial)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T15:19:39Z
updated_at: 2026-10-04T15:20:08Z
parent: qou-5vkl
---


Found while re-verifying PR #4913 (2026-08-10, branch
`claude/stalled-prs-wrap-up-uja5th`).

`content/.../QOU/MathlibExt/EndBaseChange.lean` imports
`Mathlib.Algebra.Module.LinearMap.Polynomial` directly. That olean is **absent**
from the restored set, so `lean`-direct fails with

    error: object file '.../Mathlib/Algebra/Module/LinearMap/Polynomial.olean'
    of module Mathlib.Algebra.Module.LinearMap.Polynomial does not exist

which is a **cache gap, not a defect in the file**. Confirmed the import is not
gratuitous: deleting it leaves `Algebra.TensorProduct.basis` and
`LinearMap.toMatrix_baseChange` unknown and the proof with unsolved goals.

Mathlib *sources* are not in the cache either (`.lake/packages/mathlib/Mathlib/`
does not exist), so the missing module cannot be rebuilt locally — restoring the
cache does not make you able to fill its own holes.

Consequences for other agents:

- Read `does not exist` on a **Mathlib** module as a cache gap. Do not report
  the file under test as failing to compile.
- The H4 cone is missing from this same cache branch (see `qou-x64l`), so this
  is not an isolated hole.

Next step: re-seed the cache branch from a build that includes the missing
modules, or record the covered module set alongside the tarball so a restoring
agent can tell up front what is not in it.

## 2026-08-10 — quantified, and the blocked verification is now DONE

**The gap is 58%, not "a module".** At the pinned rev
(`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`) Mathlib has **6996** modules;
`lake-cache/qou-v4-24-0-new` carries **2970**. **4026 absent.** The seed captures
the import cone QOU needed at seed time, so any file importing outside it hits
`object file ... does not exist`.

**`EndBaseChange.lean` now verifies.** This was the concrete cost of the gap — a
file merged in #4913 that no one had checked. Cloned Mathlib sources at the
pinned rev (github egress works; the cache ships oleans only, so it cannot fill
its own holes), built the missing cone, and ran it:

- `lean`-direct **exit 0**
- `#print axioms QOU.MathlibExt.endBaseChangeEquiv` → `[propext, Classical.choice, Quot.sound]`
- same for `endBaseChangeEquiv_tmul`

So #4913's own reported verification is confirmed independently. Closing the
gap took **13 modules, 0 failures** against 46 of its cone already present.

**Delivered instead of a re-seed:** `scripts/build-missing-oleans.py` — walks the
import graph from a target and builds bottom-up only what is absent. A re-seed
would push a 2.1 GB tarball to a load-bearing infra branch to add 13 modules,
and would go stale the next time anyone imports outside the new cone; the script
fixes the whole class for the cost of one file. Documented in
`local/lean-environment-setup` §"The restored cache is PARTIAL".

Three traps recorded there, each of which cost time:
1. symlinking the source tree fails — `lean` rejects inputs resolving outside root;
2. running `lean` from outside the repo hits `no default toolchain configured`
   (elan's override is per-directory) — call the toolchain binary by path;
3. these sandboxes run as **root**, so `~` is `/root`, not `/home/user`. My own
   first draft defaulted to `~/mathlib-src` and reported "sources not found" on
   the machine that had them. Caught by the script's self-check, not by review.

**Still open:** whether to re-seed at all. Recommendation: don't re-seed on
demand — instead record the covered module set alongside the tarball so a
restoring agent can see the 58% up front rather than discovering it as a
mystery build error.
