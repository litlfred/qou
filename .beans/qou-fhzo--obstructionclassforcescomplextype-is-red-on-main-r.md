---
# qou-fhzo
title: 'ObstructionClassForcesComplexType is red on main: ring and linear_combination used, never imported'
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T05:03:53Z
updated_at: 2026-09-06T05:05:58Z
---

## 2026-09-06 — found by the FIXED sweep; two missing imports; verified

`QOU/Eightfold/ObstructionClassForcesComplexType.lean` is RED on `main`. It uses
`ring` (in the `calc` at l.57) and `linear_combination` (l.68) while importing
ONLY `Mathlib.Data.ZMod.Basic`, so both tactics are out of scope:

    l.57:48 error: unknown tactic
    l.57:44 error: unsolved goals
    l.55:49 error: unsolved goals
    l.49:44 error: unsolved goals
    l.68:3  error: unknown tactic

**Proved to be a missing-import bug, not an environment artifact.** Same file,
same LEAN_PATH, two runs:

  A  file as-is on main                             -> EXIT 1, the errors above
  B  identical file + import Mathlib.Tactic.Ring
     + import Mathlib.Tactic.LinearCombination      -> EXIT 0

An olean-tree difference cannot put a tactic in scope that the source never
imports, and B fixes it with the SAME tree, so this is the source's own defect.

**Its own commit messages say so.** `79ddaea5af8` "NOT YET VERIFIED" and
`4cc13376e02` "fix a real proof error found by re-reading, not by compiling --
STILL UNVERIFIED". It was landed knowingly uncompiled; nothing here is a
surprise to its author, only unnoticed.

**Fix:** the two import lines, each annotated with the line that needs it.
Nothing else touched — no proof changed, no statement weakened.

**Verified:** `lean -DautoImplicit=false -s 65536` -> EXIT 0, zero diagnostic
bytes; no `sorry` in the file; `#print axioms` on both theorems shows only
propext / Classical.choice / Quot.sound, no sorryAx.

**Provenance worth recording:** this was found BY the fixed library sweep of
`qou-tpdg` (#6827). Before that fix the same sweep emitted 22 false
environment-REDs on this container, which would have buried a single real one.
First run after the fix on a head where main had moved 101 commits: 144 ok,
**1 RED**, and the 1 is genuine. That is the gate doing its job.
