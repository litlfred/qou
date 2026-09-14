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

---

## 🟩 CONFIRMED BY MEASUREMENT, not only by AGENTS.md (2026-09-13, a second agent)

The block above reaches the right conclusion by citing AGENTS.md. This one reaches
it by running the thing, independently and before reading that block -- the two were
written in parallel and collided on rebase, which is worth keeping visible rather
than collapsing to one.


Measured on `main` `c9fd78b0a`:

    scripts/lean-library-sweep.py --package QOU --only-exact QOU --jobs 2
    === library sweep: 1451 ok, 0 RED, 0 TIMEOUT + 0 UNVERIFIED, 0 skipped, 8542s ===
    [1451/1451] ok   QOU

**What I retract.** I wrote that the SIGSEGV five "are the same container
resource limit that makes the library root unverifiable (`qou-ed8a`)". There is
no such limit. The root was short **79 Mathlib oleans**; they build from source
in 188 s, were seeded to `lake-cache/qou-v4-24-0-mathlib-gap-modules`
(`d7e3ae8c662`, 2026-09-11), and with them restored the root and its entire
1451-module dirty closure compile with nothing red, nothing timed out and
nothing unverified.

Every module flagged SIGSEGV-family or TIMEOUT passes: `HeckeH4BlockMap211`,
`HeckeH4BlockMap31` (these two *concurrently*, 137 % and 98 % CPU),
`OctonionDerivationsUpperBound`, `Witness12B`. The TIMEOUTs were CPU contention
from the old `--jobs 3` default — `nproc//jobs` gave 1 thread each — which a
sibling diagnosed in `2026-09-08-sweep-timeouts-were-contention.md` and this run
confirms from the other side.

**What survives.** The five `exit 139` observations themselves: something
segfaulted, zero bytes of diagnostic. What is withdrawn is the attribution. And
a defect in my own record — **I never named which five modules segfaulted**, so
the claim could not be checked against the thing it was about, only against a
family resemblance. Name the modules.

**Consequence for this bean's open question.** "Sizing the ~1863 root-missing
modules needs a different build environment" is also withdrawn. `--all` with
`--only` chunking is built for a constrained container and this run demonstrates
the capacity (1451 modules, 8542 s, disk comfortably inside). The sizing question
is unblocked and needs no owner decision.

**Trap found on the way, live in a fresh container (`qou-4h26`).** The first
attempt reported `556 UNVERIFIED, 880 skipped` with zero source errors — pure
path artifact. `lean-cache-restore.sh` fills the **root** mathlib tree (3559)
while the sweep reads the **paper** tree (92), and Lean resolves a package from
the first `LEAN_PATH` root holding that package's *directory*. Run
`scripts/lean-sync-olean-trees.sh` after restoring, or the sweep measures the
path rather than the corpus.

Full write-up:
`docs/audits/2026-09-13-library-root-compiles-1451-modules-zero-red.md`.
