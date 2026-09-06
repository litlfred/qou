---
# qou-g5sp
title: The entire Bruhat / Coxeter-order component is unreachable from QOU.lean (9 modules, includes merged main work)
status: todo
type: task
priority: normal
created_at: 2026-09-06T22:32:32Z
updated_at: 2026-09-06T22:33:18Z
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
