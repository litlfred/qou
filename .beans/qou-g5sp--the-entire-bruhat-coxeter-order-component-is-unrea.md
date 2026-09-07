---
# qou-g5sp
title: The entire Bruhat / Coxeter-order component is unreachable from QOU.lean (9 modules, includes merged main work)
status: todo
type: task
priority: normal
created_at: 2026-09-06T22:32:32Z
updated_at: 2026-09-07T05:14:01Z
---

## The finding

Measured on `claude/mathas-314-descent-2026-09-06` @ `6c5e47d2e5`, over the QOU package:

**Not one of the nine modules of the Bruhat / Coxeter-order component appears in
`QOU.lean`**, and none of them is reachable from anything that does:

    Machinery/CoxeterBruhat            Machinery/CoxeterBruhatOrder
    Machinery/CoxeterDeletion          Machinery/CoxeterRankTwo
    Machinery/BruhatRankCriterion      IwahoriHecke/BruhatReflection
    IwahoriHecke/BruhatSubword         BraidKnot/TwInverseBruhat
    BraidKnot/DominanceIsBruhat

Method (both halves matter -- "absent from the root" is not "unreachable"):

    for m in <the nine>; do grep -c "\.$m\$" QOU.lean; done          -> 0 for all nine
    for each importer of each: is the IMPORTER in QOU.lean?           -> 0 for all

Every importer is itself one of the nine, so the component is a connected chunk
disconnected from the root.  `Machinery/CoxeterCommutingTransversal` IS listed, which is
what makes the absence easy to miss by eye.

## Why it matters

`lake build QOU` builds the root's import closure, so **none of this is built by it**, and
neither is it seen by any sweep that starts from the root.  This is not hypothetical or
branch-local: `Machinery/CoxeterBruhat` and `IwahoriHecke/BruhatReflection` are on `main`
via #6894 / #6899 (merged), so **already-merged work is outside the root build**.

Distinct from `qou-tpdg`, which is that the library sweep pointed at the wrong Mathlib tree /
never swept the root.  This is the complementary defect: even a correct root sweep would not
see these, because they are not in the root.

## What I did NOT do, and why

I did not add the import.  I cannot verify the effect here:

  * `lean QOU.lean` with only the QOU build dir on `LEAN_PATH` fails at line 3 --
    **the QOU library root imports `UGB`**, so a lean-direct check of it needs all three
    package build dirs (`content/{unital-groebner-bases,fred2005-formal-groups}/lean/.lake/
    build/lib/lean`).  Worth knowing on its own; it is not documented anywhere I found.
  * with all three on the path it **segfaults** (exit 139) loading the 889-import closure.
  * `lake build` is not an option in this container -- it evicts the restored olean cache
    (AGENTS.md) and filled the disk twice this session.

So a one-line addition to `QOU.lean` here would be an unverifiable change to the file that
gates the whole library build.  Someone with a working `lake build` should do it.

## Suggested fix

Adding `import QOU.BraidKnot.DominanceIsBruhat` alone pulls in eight of the nine transitively
(all but `CoxeterRankTwo`, which reaches only `CoxeterDeletion`), so two lines cover the
component.  Verify with a real `lake build QOU` before landing -- note
`BruhatRankCriterion.bruhatLe_of_rk_le` carries a documented `sorry` (Bjorner-Brenti Thm
2.1.5), which is a warning and not a build failure.


## 2026-09-07 — THREE CORRECTIONS TO THIS BEAN, and the finding is ~200x bigger

### 1. "This container cannot run a lake build to verify a QOU.lean change" — MISLEADING

The claim was that verifying such a change needs `lake build`, which cannot run here.
`lake build` still cannot; but **`scripts/lean-library-sweep.py` CAN, and it verifies the
root module `QOU` directly.**  Measured today: 14-module dirty closure, **111 s**, disk did
not move.

It was true of the sweep as it stood when I wrote it and is false of the sweep as it stands
now: bean `qou-tpdg` / PR #6827 replaced the 2.3 GB `copytree` with a **hardlinked** shadow
(`du` says 2.3 GB, `df` does not move) precisely because it "died on ENOSPC having judged
nothing" at the same 1.1 GB free I was reasoning from.  I reasoned from the old cost and did
not re-check.  **The sibling had already fixed the thing I declared impossible.**

### 2. "Adding `import QOU.BraidKnot.DominanceIsBruhat` pulls in eight of the nine; two lines
cover the component" — WRONG.  It is FOUR.

Closure computed rather than eyeballed.  `DominanceIsBruhat` reaches only `CoxeterBruhat` and
`BruhatRankCriterion`; it does **not** reach the `BruhatReflection` -> `BruhatSubword` ->
`CoxeterBruhatOrder` chain at all.  The four modules that are not imported by any other of
the nine, and so must be named explicitly:

    import QOU.BraidKnot.DominanceIsBruhat
    import QOU.BraidKnot.TwInverseBruhat
    import QOU.IwahoriHecke.BruhatReflection
    import QOU.Machinery.CoxeterRankTwo

Verified: those four have closure 9 of 9.

### 3. THE NINE ARE A SYMPTOM.  67 % of the QOU library is not in the root.

Measured on `main` `8432b885fb`, walking `QOU/**.lean` against the root's `import` lines:

    modules on disk   2735
    imported by root   890
    NOT in the root   1845   (67 %)

Reproducible: [`scripts/lean-root-coverage-audit.py`](scripts/lean-root-coverage-audit.py)
(added with this bean update; `--list <NS>` enumerates one namespace).  Quote its output, not
this paragraph -- my first ad-hoc count said QBeta 152 and the script says 151.

By namespace, worst first: **BraidKnot 409 missing of 435 (94 %)**, Archimedean 162/236,
QBeta 151/291, MassTheory 106/154, Mass 95/160, Mathlib 90/211, MathlibExt 74/157,
Machinery 71/94, Hecke 56/69, BraidsAndKnots 55/80, AppendixSurreals 44/51, SchurWeyl 39/75.

So `lake build QOU` builds **a third of the library**, and the nine I found are 0.5 % of what
is outside it.  This is not recorded in any bean; `qou-tpdg` measures the root's 883 imports
but not what they omit.

### Why I did NOT just add the four

I started to, then stopped, for two reasons that are worth writing down:

- **The root is RED on `main` already**, independently of this.  Sweep on `main`: 10 ok,
  3 RED, 1 skipped -- `QOU` (the root), `Eightfold.ObstructionClassForcesComplexType`
  (pre-existing, #6909), and `MassTheory.LeadingOrderTraceCoefficient`, a **duplicate
  `c1Closed`** I confirmed and reported on PR #6920, which owns those files.  A four-line
  addition cannot be verified green against a red root.
- **Four of 1845 is a token, not a fix**, and the four are arbitrary -- their only claim is
  that they are mine.  Picking them would make the number look addressed while leaving the
  condition untouched.

### The decision this needs (owner's, not mine)

Adding 1845 imports is not a mechanical sweep to be run unattended: most have never been
built by the root, so the true count of failures behind them is **unmeasured**, and the
honest next step is to measure it before anyone proposes a fix.  That measurement is a real
compute (a full-corpus sweep), not a five-minute job.

My recommendation, marked as judgement: **measure first** -- run the sweep across all 2735
rather than the dirty closure, get the actual RED count, and decide scope from that.  The
no-op is that `lake build QOU` keeps silently covering a third of the library, which is the
status quo and is safe but means the root build's green is worth much less than it looks.
