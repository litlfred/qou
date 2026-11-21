---
# qou-g5sp
title: The entire Bruhat / Coxeter-order component is unreachable from QOU.lean (9 modules, includes merged main work)
status: completed
pr: 8333
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T22:32:32Z
updated_at: 2026-11-21T14:33:40Z
parent: qou-5vkl
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

## 2026-09-07 — CLAIMED; the measurement this bean asks for is running (PR #7124)

Taking up this bean's own recommendation ("measure first — run the sweep across
all 2773, get the actual RED count"), which it could not act on because the sweep
only knew how to build the dirty closure.

Re-measured on `main` `1ec22a9040c`: **2773 on disk / 910 in root / 1863 outside
(67%)** — the ratio holds, the counts drift, as this bean already says.

**Two flags added** (`scripts/lean-library-sweep.py`):
`--all` (compile every module, 4.0 s/module measured) and `--only PREFIX`
(chunk it, because the full run writes ~610 MB against 619 MB free).

**Three measurements worth keeping regardless of how the sweep ends:**

1. **60 modules on today's main have NO olean at all**, against the 3 this bean's
   unsound proxy reported. That figure IS sound — olean presence is measured, not
   inferred from an mtime.
2. **The hardlinked shadow costs 0.22 MB/module, not 2.4 GB.** `du` says 2.4 GB,
   `df` moved 9 MB over the same 40-module run. First direct confirmation that
   #6827's hardlink change does what it claimed.
3. **The chunked result will be WEAKER than a single-run one** and must be
   reported as such: a later chunk resolves an earlier-chunk import against the
   snapshot olean, not one this run rebuilt. Same snapshot-conditionality the
   sweep already carries (`qou-56qy`), not a new hole.

**I have NOT added the 1863 imports and will not propose it here.** This bean is
right that scope is the owner's call and should follow the RED count.


## 2026-09-08 — MEASURED. All 2774 modules, 0 REDs, and this bean's headline figure was WRONG

The sizing question is answered. PR #7124.

### The headline figure is corrected: 1324 outside, not 1863

`scripts/lean-root-coverage-audit.py` measured the root's **direct import lines**
(910) and called everything else "NOT in the root". `lake build QOU` builds the
**transitive closure** — **1450** modules — so the blind spot is **1324 (47.7 %)**,
not 1863 (67 %). The script's own docstring said "import closure" while its code
summed one line each. Fixed in #7124; **quote the transitive number.** The
overstated figure had reached this bean's headline, the script's docstring, an audit
doc and a PR body.

### The measurement

All **163 chunks**, all **2774 modules** covered — distinct counts, unioned by
name (summing per-chunk totals double-counts pulled-in deps and gave an impossible
2200/2193/2774):

| | count |
|---|---|
| `ok` | **2754** |
| **RED — corpus defects** | **0** |
| UNVERIFIED — cannot judge here | 1 |
| TIMEOUT — not judged | 4 |
| SKIPPED — behind one of those | 16 |

**Outside the root closure: 1324 modules, 1323 verified ok.** The one exception is
`Machinery.HeckeH4RepDecomp`, a timeout cascade.

### One real defect, and it was genuinely in the blind spot

`QOU/Machinery/BruhatRankCriterion.lean:607` did not typecheck: `9151ad46ee5`
(`qou-1u90`) made `bruhatLe_mul_simple_of_isRightDescent` unconditional, ported
its callers across ten files, and missed this one. Fixed (`ab2189d6eb4`);
BraidKnot re-run 454 ok/1 RED → **456 ok/0 RED**. Verified it is **not** in the
transitive closure, so `lake build QOU` would not have compiled it — had it been
inside, this instance would not have supported the thesis.

### The residue is four clusters, no defects

Mathlib cache gap (`…GroupCohomology.LowDegree`) taking the **library root** with
it — so **the root is not broken, it is unverifiable here**; `Machinery.HeckeH4*`
(10, the same H4 family a sibling measured as SIGSEGV); `MathlibExt.Octonion*`
(6); `Archimedean.PauliWitness*` (2).

### Six gate defects against one real corpus defect

Never-built deps unpulled; the root getting no chunk; **stale** deps unpulled
(a snapshot olean presenting as `unknown identifier` for a lemma that is in
source); `--only QOU` prefix-matching all 2774; an unlink/write **race**
(demonstrated fixed — SkewSYTBranchingBijection UNVERIFIED → ok, two dependents
un-skipped); and a driver bug that silently no-op'd 65 chunks and **overwrote a
456-module result**. A gate this young reporting on 2774 modules is mostly
reporting on itself.

### Still open — NOT closing this bean

The scoping decision (whether to add the missing imports to `QOU.lean`) is the
owner's and is untouched. It now has its measurement: **the blind spot held exactly
one real defect across 1324 modules.**


## 🟩 RETRACTED 2026-09-13 — the root COMPILES here, and my "container resource limit" does not exist

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


## 🟩 THE SIZING QUESTION IS ANSWERED: ZERO defects in 2836 modules

`scripts/lean-library-sweep.py --package QOU --all --jobs 2` on `main`
`e22bd4561`:

    === library sweep: 2821 ok, 0 RED, 1 TIMEOUT + 0 UNVERIFIED (NOT failing),
        14 skipped (dependency red), 11426s ===

**Zero RED, zero UNVERIFIED**, 3 h 10 m, every module rebuilt from source.
Combined with this session's root-targeted run, **2830 of 2836 modules are
judged `ok` and 0 are RED in either run**; 6 remain unjudged (below).

### This is the third retraction in the arc, and it is mine

I proposed two methods for this sizing and retracted both as unsound; then I
recorded that it needed a **different build environment**. It did not. `--all`
with `--only` chunking is built for a constrained container and did the whole
library in one pass on 4 cores.

### What a 0 means here, fixed BEFORE the result landed

Read out of `lean-library-sweep.py`, not fitted afterwards. Under `--all`
nothing is trusted -- every module is rebuilt from source in topological order,
so a dependent cannot compile against a stale dependency olean. That is **5 of
my 10 corpus-typecheck REDs, structurally impossible here.** A signal death
(`rc < 0`, SIGSEGV) is classified UNVERIFIED and printed *"NOT a corpus defect
on this evidence"* -- **the other 5.** TIMEOUT is its own label. So a RED would
have been a source error against QOU source. There were none. Residual
conditionality is against **Mathlib** (restored, not rebuilt), not QOU.

### The reframing this forces on THIS bean

The two-thirds-outside-the-root finding is a **build-coverage** fact, not a
**correctness** fact. Those modules are not rotting -- every one compiles. What
is true is that **nothing routinely checks them**, which is exactly how
`BruhatRankCriterion` went red on `main` unnoticed (`qou-1u90`, #7185). Different
problem, different fix: **coverage** -- reach them from the root, or run this
sweep as the gate. Both are owner calls; neither is started.

### The honest remainder

`QOU.Machinery.HeckeH4BlockMap211` TIMEOUT at the default 1800 s, 14 skipped
behind it. Not a new problem -- it compiled **ok** in the root run two hours
earlier at the same budget; it sits near the wall. Nine of the 15 are covered by
that run. **Six are genuinely unjudged**, and four of them are exactly the
`QOU.Hecke.* H3A/H4A` family this bean named as the SIGSEGV class:

    QOU.Hecke.FullRankFromWedderburn        QOU.Hecke.MarkovTraceOnH3A
    QOU.Hecke.InstanceOnH3A                 QOU.Hecke.MarkovTraceOnH4A
    QOU.Hecke.InstanceOnH4A                 QOU.Machinery.HeckeH4RepDecomp

A `--only QOU.Hecke --timeout 5400` re-run is in flight. Until it reports these
six are **unverified, not passing**.

Full write-up:
`docs/audits/2026-09-13-every-library-module-compiles-zero-defects.md`.


## 🛑 THE CENTRAL PREMISE OF THIS BEAN IS FALSE. `lake build QOU` DOES build these modules

Every "NOT in the root" claim above -- lines 35, 98-114, 140, 202-208, 272 -- says
or implies that **`lake build QOU` does not compile the modules outside
`QOU.lean`'s import closure**. It does. The paper lakefile declares the library
with an explicit glob:

    [[lean_lib]]
    name = "QOU"
    srcDir = "."
    # WIDEN THE BUILD TO THE WHOLE TREE (bean qou-rc7b).
    globs = ["QOU", "QOU.+"]

A Lake library with no explicit `globs` defaults to `roots.map Glob.one` and
builds only its root plus that root's transitive imports -- which is the state
this bean describes. **That state ended on 2026-08-08**, a month before this bean
was opened, when `qou-rc7b` (status `done`, *"BUILD COVERAGE: `lake build` reaches
only 853 of 1618 QOU Lean modules -- 47% never compiled"*) added the glob. It is on
`origin/main` today.

So `lake build QOU` compiles **all 2836**, not a third of them. Corroborated
independently by the background build's own log, which reports
`[6459/6460] QOU.Eightfold.ObstructionClassForcesComplexType` -- a job count only
a whole-tree build reaches.

### What the numbers actually are

Measured today by walking `import` lines from `QOU.lean` transitively:

    library modules                 2836
    reachable from QOU.lean         1451   (51.2%)
    OUTSIDE the import closure      1385   (48.8%)
    direct imports listed in QOU.lean  911

**The `67%` figure asserted twice above was ALREADY CORRECTED on 2026-09-08** --
by `scripts/lean-root-coverage-audit.py`'s own `CORRECTED` block, which states the
cause (it counted the root's DIRECT import lines, not the transitive closure,
understating coverage by 540 modules) and names the four places the overstatement
reached, this bean's headline among them. Today's independent measure, 48.8%,
agrees with that script's 47.7% and with `qou-rc7b`'s 47% in August.

**So my withdrawal of the 67% is a RE-DISCOVERY, not a finding**, and I reached it
by measuring rather than by grepping my own tool -- the corpus-grep failure this
bean has now committed twice in one session.

What IS new is the **premise**, which that correction did not touch: it fixed the
count while leaving "a module outside the closure is built by nothing" standing.
The glob falsifies that, and the two errors needed separate fixing.

### The distinction the whole bean was missing

**Import closure ≠ build coverage.** Those 1385 modules are outside `QOU.lean`'s
import graph and *inside* `lake build QOU`. Both facts are true and this bean
treated the first as implying the second.

### So what IS the real gap?

Not build coverage -- **nothing runs that build automatically.** CI auto-triggers
are disabled repo-wide (`build.yml` is `workflow_dispatch`-only, owner directive
2026-06-30, Actions billing). A breaking change therefore lands and nothing
notices until an agent runs the build or a sweep by hand. That is how
`BruhatRankCriterion` went red on `main` (`qou-1u90`, #7185) -- **not** because
the module was unreachable.

That reframes the fix and **removes the decision I was about to put to the
owner**. I had named "reach them from the root, or make the sweep the gate" as an
owner call, three times, in this bean, in #7272 and in chat. The first half is
already done and has been for a month. The second half is a CI-trigger question
the owner has already ruled on twice, most recently 2026-08-09 *with this exact
failure cost on the table*, and AGENTS.md says not to re-propose it without a new
reason. I do not have one. **Withdrawn -- there is nothing here for the owner to
decide.**

### One thing a sibling should know

`BruhatRankCriterion.lean:606-610` on `main` carries, in the fix for `qou-1u90`:

    -- That commit ported its callers across ten files and missed this
    -- one, because this module is not in `QOU.lean`'s import closure, so
    -- `lake build QOU` never compiles it.

The first clause is right and the second is wrong, for the reason above. Flagged
rather than edited: it is a sibling's file and the correction is theirs to make.

**None of this touches the sizing result.** 2821 ok / 0 RED stands, and it is now
*more* interesting rather than less: those modules were being built all along.


### The premise's remaining carriers (measured 2026-09-13)

Corrected here:

  scripts/lean-root-coverage-audit.py  -- docstring; my own script

Flagged, NOT edited -- a sibling's file and a dated audit doc:

  scripts/lean-library-sweep.py:299    -- `--all` help text, "1863 of 2773 are
                                          outside the root build"; both the count
                                          and the premise are stale
  QOU/Machinery/BruhatRankCriterion.lean:610 -- "`lake build QOU` never compiles
                                          it", inside the qou-1u90 fix (#7185)
  docs/audits/2026-09-08-full-library-sweep-and-five-false-reds.md:143

The sweep help text is the one that matters most: it is read by every agent who
runs `--all --help`, and it carries BOTH the superseded 67% count AND the false
premise, in a script that is otherwise the corpus's best verification tool.


## 🟩 COMPLETE: 2836 of 2836 judged, 0 RED

Four runs, all on `main` `e22bd4561`:

| run | selector | result |
|---|---|---|
| 1 | `--only-exact QOU` (root + dirty closure) | 1451 ok, 0 RED — incl. `[1451/1451] ok QOU` |
| 2 | `--all` (every module) | 2821 ok, 0 RED, 1 TIMEOUT, 14 skipped behind it |
| 3 | `--all --only QOU.Hecke --timeout 5400` | 269 ok, 0 RED |
| 4 | `--all --only-exact QOU.Machinery.HeckeH4RepDecomp --timeout 5400` | 17 ok, 0 RED |

**Union: every one of the 2836 library modules has been compiled from source and
none is RED.** The TIMEOUT that blocked run 2, `HeckeH4BlockMap211`, passed in
run 3 at the larger budget on an uncontended machine — confirming it as a budget
artifact, not a property of the module.

### Run 4 exists because I was wrong about run 3's scope

I said the `--only QOU.Hecke` re-run would settle all six unjudged modules. It
settled five. `QOU.Machinery.HeckeH4RepDecomp` is **not under the `QOU.Hecke`
prefix** and nothing under that prefix imports it — it is a leaf — so the
selector never reached it. A namespace prefix is not a dependency closure, and I
treated it as one.

### What this closes on the SIGSEGV retraction

The four modules my bean named as the SIGSEGV class are measured and green:

    QOU.Hecke.InstanceOnH3A       ok
    QOU.Hecke.InstanceOnH4A       ok
    QOU.Hecke.MarkovTraceOnH3A    ok
    QOU.Hecke.MarkovTraceOnH4A    ok

So whatever produced those five `exit 139` results, it was **not** a property of
these modules and **not** a container limit. The observations stand; the
attribution is dead. The sweep's `UNVERIFIED` class — whose source comment cites
that very measurement as its motivating case — is the correct home for evidence
of that shape, and it is where such a result would land today.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Round 56 Implementation (PR #8333)
- Implemented on branch `claude/round56-trd0-9nnz-fixes` (commit `e33bff7d43b72a19e618441a16ae41a21af05e0e`, https://github.com/litlfred/qou/pull/8333).

## 2026-11-21 — lean-build-red drain (issue #8817, session https://claude.ai/code/session_01Qmmkt5eovX5GYdZNHqjZdu)

**Completed.** This bean's own 2026-09-13 entries already record that its premise was false: the QOU lakefile has `globs = ["QOU", "QOU.+"]` (qou-rc7b), so `lake build QOU` builds the Bruhat component. Today's whole-library lean-direct sweep at main `2ae54ab401` compiled every module under `lean/QOU` (see issue #8817; 3420 ok on the first pass, the rest blocked only on Mathlib cache gaps), including the nine Bruhat/Coxeter modules. Open PR #8333 still proposes wiring them into `QOU.lean`; that is a root-import choice, not a coverage gap.
