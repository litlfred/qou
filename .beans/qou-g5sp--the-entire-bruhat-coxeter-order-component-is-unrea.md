---
# qou-g5sp
title: The entire Bruhat / Coxeter-order component is unreachable from QOU.lean (9 modules, includes merged main work)
status: todo
type: task
priority: normal
created_at: 2026-09-06T22:32:32Z
updated_at: 2026-09-07T17:08:22Z
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


## The cheap proxy for "how many of the 1845 fail" DOES NOT WORK — negative recorded

Immediately after recommending "measure first", I tried the obvious cheap proxy and it is
invalid.  Recording it so the next agent does not spend the same hour.

**The proxy.** A module with a built `.olean` compiled at some point; so count how many of the
1845 have one, and compare olean mtime against source mtime for staleness.  It gives a
tempting answer:

    of the 1845 modules outside the root:
       have a built olean : 1842   (100%)
          of those, olean older than source : 36
       NO olean at all    : 3   -- and they are EXACTLY the three the sweep flagged
                                  (Eightfold.ObstructionClassForcesComplexType,
                                   MassTheory.LeadingOrderTraceCoefficient,
                                   MassTheory.MirrorAsymmetrySign)

Read naively that says the uncertain set is ~39 rather than 1845, and the whole decision
collapses to something tractable.  **Do not report it.  Both halves are unsound.**

**Why.** Olean mtimes are not build times here:

    olean mtimes by day:  2026-08-23  1
                          2026-08-24  2
                          2026-08-29  8
                          2026-08-30  1
                          2026-08-31  1
                          2026-09-06  2722

**2722 of 2735 share one timestamp** -- the bulk cache restore.  So:

- **"1842 have an olean" attests to the state at the cache's build, not to current source.**
  It is the same snapshot-conditionality that `qou-56qy` is about, one level up: the whole
  olean population is one snapshot, so counting it cannot discriminate current from stale.
- **"36 older than source" is meaningless**, and worse than merely weak.  In a fresh clone
  the SOURCE mtimes are checkout times too, so that comparison is between two artificial
  timestamps, neither of which is a build or an edit.  36 is not a lower bound on anything.

**What the data does support, stated at its real strength:** whatever build seeded the cache
on 2026-09-06 produced oleans for all but three of these modules, and those three are the
three independently known to be red.  That is suggestive -- the corpus largely compiled as of
that build -- and it is not evidence about `main` today.

**What would actually answer it:** compile them, or determine which sources have changed in
commits after the cache's build commit (by `git log`, never by mtime) and compile only those.
The first is the honest measurement; the second is a genuine shortcut but needs the cache's
commit, which is not recorded in the tree.

So the recommendation is unchanged and its cost estimate stands: **a real compute, not a
five-minute job.**  I now have direct evidence for that rather than an assumption, which is
the one thing this attempt was worth.


## Re-measured at merge time — the counts drift, the ratio does not

The figures above were taken on `main` `8432b885fb`.  Re-run at merge time on
`4370f5d322`:

    modules on disk   2735 -> 2752
    imported by root   890 ->  899
    NOT in the root   1845 -> 1853   (67% both times)
    BraidKnot          409 ->  410 missing of 436

**So the exact counts are a moving target and the RATIO is the durable finding.**
Two thirds of the QOU library sits outside `lake build QOU`, and that held across
~140 commits of main.  Quote `scripts/lean-root-coverage-audit.py`'s output with the
sha you ran it on; do not quote a number from this bean as current.

That is the whole reason the script is in the PR rather than just the numbers.


## 🛑 THE CORPUS TYPECHECK CANNOT SIZE THE GAP. My own tool's RED is unsound.

I built `scripts/lean-corpus-typecheck.py` to answer "how many of the modules outside
the root are actually broken", ran it to 1131 of 2752 modules, and got **10 REDs**.

**Zero of the 10 are corpus defects.** Every one is an artifact:

| count | what it actually was |
|---|---|
| 5 | **stale dependency oleans** -- Bruhat/Coxeter chain |
| 5 | **SIGSEGV**, `exit 139`, zero bytes of output -- `QOU.Hecke.*` H3A/H4A family |
| 1 | timeout, which is not a verdict either |

**The stale-olean five, traced to the root.**  `CoxeterDihedralDescent` reported
`unknown identifier bond_ne_zero_of_pow_eq_one`.  That identifier IS in the source
(`CoxeterDihedralOrder.lean:322`) and IS on main -- it was absent only from the OLEAN,
which I had built hours earlier at `490064f240`, before main added it.  Everything
downstream then reported `Application type mismatch` against the old signature.
**Rebuilding the six modules root-first made all six exit 0 with no source change.**

**The SIGSEGV five** are the same container resource limit that makes the library root
unverifiable (`qou-ed8a`) -- zero bytes of diagnostic, which is the tell.

### The methodological point, which is the real finding

The script compiles each module against **whatever oleans happen to be on disk**.  In
this container the olean tree is a patchwork -- restored cache, plus my hand rebuilds at
several different commits, plus whatever a partial SessionStart `lake build` left.  So a
RED is a statement about the disk, not about the corpus.

I had documented the PASS side of this ("not current, merely not-self-broken") and wrote
the exact opposite for the RED side: *"a FAIL is unconditional: the file does not
typecheck as it stands."*  **That sentence was wrong**, and it is now replaced in the
docstring, with the measurement, plus a warning printed above every RED list.

**This is the SECOND unsound sizing method I have proposed for this bean**, after the
olean-existence proxy further up.  Both were mine, and both failed the same way: they
inferred a property of the CORPUS from a property of this container's BUILD STATE.

### What would actually answer it

Rebuild each module's dependency chain from source before judging it -- which is exactly
what `scripts/lean-library-sweep.py` does, and why that is the repo's gate and this is
not.  On the dirty closure it reports **196 ok / 1 RED**, the 1 being the root's SIGSEGV.

Extending that to all 1853 means a full from-source build in topological order.  This
container cannot do it: large closures SIGSEGV, and disk is ~860 MB.  **So the sizing
question stands unanswered, and it is now unanswered for a measured reason rather than
an assumed one.**  That is the third estimate of its cost and the first with evidence.
