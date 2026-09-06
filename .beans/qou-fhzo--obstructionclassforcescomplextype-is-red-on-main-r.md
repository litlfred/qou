---
# qou-fhzo
title: 'ObstructionClassForcesComplexType is red on main: ring and linear_combination used, never imported'
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T05:03:53Z
updated_at: 2026-09-06T13:04:32Z
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


## 2026-09-06 06:4x UTC — rebased onto 468e99858c9; whole gate now green

Sweep on the rebased head (#6827's fixed script, run from a scratch copy — main's
copy cannot run on this container):

| library | result |
|---|---|
| Fred2005 | 1 ok, 0 RED, 6s |
| QOU | **145 ok, 0 RED**, 268s |
| UGB | 22 ok, 0 RED, 97s |

`[17/145] ok QOU.Eightfold.ObstructionClassForcesComplexType` — the fix clears the
RED against the sweep, not just under a hand-run `lean`. Prior head was 144 ok / 1 RED.

Second fact from the same run, kept separate because it is NOT this PR's doing:
main's new commit 468e99858c9 (touches QOU/HeckeAlgebra/WedderburnConstruction.lean)
introduced no red. QOU closure 144 -> 145 on that churn (head-scoped, not drift).

Real QOU olean tree identical on all 2660 by inode+size+mtime before/after.
Pushed as 4ef23f7e2ef. Still waiting on merge permission.


## 2026-09-06 ~13:0x UTC — re-verified on main +142 (62 .lean changes); #6827 has MERGED

#6827 (qou-tpdg) merged: b44cc2e1081 / 3144214a1bb / 5ccaa32ed4b are on main, so the
FIXED sweep is now main's own gate and no scratch copy is needed.

STILL NEEDED after 142 commits: main's version of the file still imports only
`Mathlib.Data.ZMod.Basic` (checked with git show origin/main:<file>), and no main
commit touched it.

Rebased to ca56f257fbd. Library sweep on that head, with the merged fixes:

| library | result |
|---|---|
| Fred2005 | 2 ok, 0 RED, 82s |
| QOU | **273 ok, 0 RED**, 557s |
| UGB | 23 ok, 0 RED, 89s |

`ok QOU.Eightfold.ObstructionClassForcesComplexType` — this fix clears the only RED,
on the largest closure measured yet (273, up from 145/201/206 as the root-enumeration
and max() fixes landed). All three library roots green.

Real QOU olean tree IDENTICAL on all 2718 by inode+size+mtime, with NO concurrent
lake build this time (status file empty) — so the invariant reads clean without
needing the timestamp argument.

BLOCKED ON: owner merge permission only. NOTE the github MCP server disconnected
this turn, so this result could not be posted as a PR comment; it is recorded here
instead. Post it to #6909 when the MCP tools are available again.
