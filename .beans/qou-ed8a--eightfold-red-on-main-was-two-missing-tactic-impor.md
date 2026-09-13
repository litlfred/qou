---
# qou-ed8a
title: Eightfold RED on main was two missing tactic imports -- and the library root's red is a container segfault, not a defect
status: todo
type: task
priority: normal
created_at: 2026-09-07T09:57:19Z
updated_at: 2026-09-13T10:39:44Z
---

## The fix (PR #7039)

`QOU.Eightfold.ObstructionClassForcesComplexType` had been RED on `main` since #6909.
Cause: the file imported only `Mathlib.Data.ZMod.Basic`, so `ring` and
`linear_combination` did not exist -- reported as **`unknown tactic`** at lines 55, 57
and 68.  The four accompanying "unsolved goals" errors are simply the goals those
tactics were meant to close; line 57 left

    (m + 1) * (x + x) = (2 * m + 1) * x + x

which is exactly `ring`'s job.  **The proofs were always correct.**  Fix is two import
lines, no proof text touched.  Both theorems `#print axioms` clean, no `sorryAx`.

Sweep before / after: `lean-library-sweep.py --package QOU` 166 ok / **2 RED** ->
166 ok / **1 RED**.

## TRAP: the library root's RED is NOT a corpus defect, and my first reading was wrong

I twice wrote that the root `QOU` is red "only because it imports Eightfold".  It is
not.  After the fix, `RED QOU` remains, and two measurements say why:

1. The sweep reports `RED QOU` with **no error lines at all** -- which is itself the
   tell.  Run directly, the root names a **missing olean**
   (`QOU.MathlibExt.HeckeToTemperleyLieb`), not a source error.  Exactly **7 of the
   root's 896 imports** had no olean; all 7 had sources present.  They are recent
   `main` landings that the restored cache predates.
2. With all 7 built (they compile clean, and the count then goes to 0), the root
   **still** fails: `exit 139`, **SIGSEGV**, loading the 896-module closure.  A
   container resource limit, reproducible, unrelated to any source.

**So the root is UNVERIFIABLE in this container, not broken.**  Do not "fix" it by
editing `QOU.lean` -- there is nothing there to fix -- and do not report a green root
from this container, because you cannot get one.

This is the same shape as the earlier finding that 8 content-block REDs were all
missing Mathlib oleans and zero were corpus defects: **a RED with no compiler
diagnostic is an environment verdict, not a mathematical one.**  Check for that before
reading any sweep RED as a defect.

## TRAP: `pgrep -fc '<name>'` counts its own wrapper

Separately, and it cost real time: I monitored the long-running corpus typecheck with
`pgrep -fc '[l]ean-corpus-typecheck'` and it returned 1 for a job that had been **dead
for half an hour** -- the match was the enclosing shell's own command line, not the
Python process.  Two status reports said "healthy, progressing" about a stopped run.

Use `ps -eo pid,etime,args | grep '[c]orpus-typecheck'`, or better, check that the
CHECKPOINT LINE COUNT is advancing between calls.  A process check that cannot
distinguish the job from the command that asks about it is not a process check.

Relaunching under `setsid ... < /dev/null` (detached from the session's process group)
is what made it survive; the plain `nohup ... &` form did not.


## 🛑 STALE 2026-09-13 — the diagnosis in the title and body is contradicted on `main`

This bean's body reads *"the root **still** fails: `exit 139`, **SIGSEGV**,
loading the 896-module closure. A container resource limit, reproducible,
unrelated to any source."*

**AGENTS.md contradicts that by name** (§Manual fallback, the `lake-cache` block):

> *"That was attributed to a container resource limit (bean `qou-ed8a`, repeated
> in a sibling's merged audit); **it is not one** — it is 79 missing oleans,
> 188 s to build, 22 MB to fetch."*

The carrier exists: [`scripts/lean-restore-gap-oleans.sh`](scripts/lean-restore-gap-oleans.sh)
against the addon orphan branch `lake-cache/qou-v4-24-0-mathlib-gap-modules`,
which went **7 → 86 oleans** in `d7e3ae8c662`. The 79 added are the transitive
cone of `Mathlib.RepresentationTheory.Homological.GroupCohomology.LowDegree`,
which `QOU.Eightfold.ObstructionH2Mathlib` needs and behind which the library
root `QOU` is SKIPPED.

To measure after restoring:
`python3 scripts/lean-library-sweep.py --all --only-exact QOU`
(NOT bare `lean`-direct — that pins the wrong olean tree and reports a missing
*QOU* module, which is a sibling the sweep builds into its shadow.)

**The title itself carries the wrong diagnosis**, so a title-scan propagates it.
Reported, not fixed — this is someone else's bean. Found by triage, not re-measured
here: I did not re-run the sweep.
