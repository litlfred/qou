# The full-library sweep: five false reds, one real one, and what "outside the root build" costs

**Bean:** `qou-g5sp`. **PR:** #7124. **Date:** 2026-09-08.
**Status of the counts below: PROVISIONAL — the run is still in flight.** Every
figure marked `[PENDING]` is unfilled on purpose; do not quote this document's
aggregate until they are replaced and this line is deleted.

## What was being measured, and why it needed measuring

`scripts/lean-root-coverage-audit.py`, re-run on `main` `1ec22a9040c`:

```
modules on disk    2773
imported by root    910
NOT in the root    1863   (67%)
```

`lake build QOU` builds the root's import closure and nothing else, so two thirds
of the QOU library is outside every routine build. Bean `qou-g5sp` established
that and asked the obvious next question — *how many of the 1863 are actually
broken?* — then recorded, correctly, that it could not answer it. Its author's
own words: the sizing question "stands unanswered, now for a measured reason."

Two sizing shortcuts had already been tried and retracted, both by that author:

1. **Count who has a built `.olean`.** Invalid: **2722 of 2735 olean mtimes are
   one timestamp**, the bulk cache restore. The whole population is one snapshot,
   so counting it cannot separate current from stale.
2. **`scripts/lean-corpus-typecheck.py` over 1131 modules → 10 REDs.** Invalid for
   a sharper reason: it compiles against whatever oleans are on disk, and in this
   container that tree is a patchwork. **Zero of the 10 were corpus defects.**

Both failed identically, and the failure is worth naming because this document
repeats it four more times: **inferring a property of the CORPUS from a property
of this container's BUILD STATE.**

## The method that does answer it

`scripts/lean-library-sweep.py` compiles each module **from source, in
topological order**, into a hardlinked shadow olean tree, never invoking `lake`
(so the restored cache is not evicted). That is why it is the repo's gate. What it
could not do was cover the whole library: `--all` was added for the population,
and `--only PREFIX` so the run could be chunked — because the shadow's
newly-written oleans are the only real bytes it costs, and reclaiming them between
chunks is what fits the run into a container at 99 %.

### Cost, measured rather than projected

| quantity | projected | measured |
|---|---|---|
| per-module wall | 4.0 s | **1.5 s** |
| real shadow bytes per module | — | **0.23 MB** (`df`; `du` says 2.4 GB for the hardlinked tree) |
| full corpus | 3.1 h | **~70 min** |
| full corpus disk | ~800 MB | **~640 MB**, or one namespace at a time when chunked |

## Five false reds, each of which taught the classifier something

Six modules came back red. **Five were the gate, not the corpus.** They are
listed in the order they were found, because each one was indistinguishable from a
real defect until the specific check beside it was run.

| # | symptom | what it actually was | fix |
|---|---|---|---|
| 1 | `object file '…/QOU/Machinery/BruhatRankCriterion.olean' … does not exist` | `--only` filtered the population but not the **never-built** dep cone. 60 modules have no olean at all, so any importer of one across a namespace boundary was a guaranteed spurious red. 5 modules exposed; 24 such deps belong to the library root alone. | `--only` closes over them |
| 2 | the library **root got no chunk** | the driver enumerated namespaces by walking `QOU/`, and `QOU.lean` is not under `QOU/` — the same enumeration bug #6827 fixed in the closure, reintroduced one layer up | root sweeps first |
| 3 | `Unknown identifier bruhatLe_inv_iff` | **the snapshot.** The lemma exists at `CoxeterBruhat.lean:149`, that module *is* in the 24-module import closure, its namespace *is* opened — and it was added 2026-09-07 07:04 (`8ca51eb3ddc`) while the snapshot olean dates from 2026-09-06 07:04. `strings` finds the symbol 0 times. | `_standard_dirty`: `--only` closes over **stale** deps too |
| 4 | root chunk selected all **2774** modules | `--only QOU` is a **prefix** and every module starts with it. Would have ENOSPC'd at 489 MB free — the exact failure chunking exists to prevent, caused by the mechanism meant to prevent it. | `--only-exact` → 101 |
| 5 | `exit 139`, zero bytes of output | SIGSEGV on a large closure. **Not mine** — a sibling measured 5 of these on `QOU.Hecke.*` H3A/H4A (`333e491eaa4`); my sweep would have called every one RED. | new `UNVERIFIED` verdict |

Defect 3 deserves emphasis. It is `--all`'s own conflation, written into the flag
by the author of this document: **`--all` says *verify* every module; it does not
say every olean is *wrong*.** Those are different facts and a restricted run needs
the second. The separation is `_standard_dirty`.

### The `UNVERIFIED` verdict

Three non-zero exits say nothing about a module's source: killed by a signal,
non-zero with no diagnostic at all, and a missing object file. All three are now
counted and listed apart from RED and **do not fail the run**, exactly as TIMEOUT
does not (`qou-xumu`). The reason string names the missing *module*, not the first
120 characters of its path.

One is live and consequential:
`Mathlib.RepresentationTheory.Homological.GroupCohomology.LowDegree` is absent
from **both** mathlib olean trees, which makes `QOU.Eightfold.ObstructionH2Mathlib`
and therefore **the library root itself** unjudgeable here. Remedy is a sibling's
`scripts/lean-restore-gap-oleans.sh`, deliberately not run mid-sweep: it fetches
~1.7 GiB into a `.git` already at 13 GB, and that move is on record as having
taken a container to 402 MB free, where the harness cannot write its own output
and every command fails.

## The one real defect, and why nothing had caught it

`QOU/Machinery/BruhatRankCriterion.lean:607` does not typecheck on `main`:

```
error: Application type mismatch: The argument
  CoxeterDihedralDescent.dihedralExact_le_three cs (Matsumoto.An_le_three N)
has type   CoxeterRankTwo.DihedralExact cs
but is expected to have type   BruhatLe cs ?m.27 ?m.28
```

`9151ad46ee5` (`qou-1u90`, "the Matsumoto/Bruhat arc is now unconditional")
discharged the `DihedralExact cs` and `∀ i j, i ≠ j → M i j ≠ 0` hypotheses of
`bruhatLe_mul_simple_of_isRightDescent` and removed them from its signature. That
commit **ported its callers across ten files and got every one it could see
right.** It did not touch this file.

`QOU.Machinery.BruhatRankCriterion` is one of the nine modules `qou-g5sp` found
absent from `QOU.lean`'s import closure. `lake build QOU` never compiles it. So it
has not typechecked since 2026-09-07 with nothing in the repo able to notice —
which is the bean's thesis as an instance rather than an argument.

**How it was distinguished from the five above**, since #3 looked identical: **all
12 of its dependencies were rebuilt from source in the same run and it still
failed.** That is the whole test. `BruhatReflection` went green under exactly that
treatment; this did not.

Fixed by dropping the two obsolete arguments (`ab2189d6eb4`) — no proof changed,
no statement weakened. Verified: 13 ok / 0 RED on the same command that gave
12 ok / 1 RED; the module blocked behind it (`QOU.BraidKnot.DominanceIsBruhat`)
green too at 14 ok / 0 RED; `#print axioms` gives `propext`, `Classical.choice`,
`Quot.sound` and **no `sorryAx`**; no `sorry` in the file. Current `main` still
carries the defect, untouched since this branch diverged, so the fix is live and
not a duplicate — checked because #6909 had been made obsolete exactly that way.

## Results

| | count |
|---|---|
| chunks completed | `[PENDING]` of 163 |
| modules `ok` | `[PENDING]` |
| **RED** (corpus defects) | `[PENDING]` |
| **UNVERIFIED** (cannot judge here) | `[PENDING]` |
| **TIMEOUT** (not judged) | `[PENDING]` |

## What this result is NOT

- **Not a single-run green.** A chunked run resolves an earlier chunk's imports
  against the snapshot, so it is strictly weaker. Stated, not buried.
- **Not about current `main`.** This tree is 149 commits behind.
- **Not a single-version measurement, unless the re-run completed.** The root and
  BraidKnot chunks ran before the `UNVERIFIED` class and the caller fix landed;
  their logs are kept as `*.log.PRE-FIX` and both were staged for a clean re-run.
  An aggregate mixing pre- and post-fix logs must not be published.
- **Not a proposal about the 1863 imports.** Scope is the owner's decision and
  follows the count, per `qou-g5sp`.

## Two measurement lessons, both from getting them wrong here

**Disk: check your own output captures before blaming the compute.** Free fell
640 MB → 380 MB mid-run and the sweep was the obvious suspect, having just been
measured at 0.23 MB/module. It was innocent: the real olean tree stayed **static
at 2718** the whole run — the shadow's no-write-through invariant holding — and the
growth was **233 MB of this agent's own harness `tasks/*.output` captures**.
Pruning the ones already read freed 160 MB. Test shadows freed only 22 MB, being
nearly all hardlink.

**`nohup` does not survive here.** Two runs were reaped when the session idled,
one 363 of 436 modules into chunk 1 of 162, with no abort line and no summary — a
log tail reads exactly like a run still in progress. A plain foreground call that
the harness backgrounds itself completed the identical work. Durability now comes
from the on-disk chunk logs: the driver skips any chunk whose log carries a
summary, so a killed process loses at most one chunk.

## Convergence with the sibling on this bean

Independently, on a different branch, a sibling hit the **same** stale-olean class
— `CoxeterDihedralDescent` reporting `unknown identifier
bond_ne_zero_of_pow_eq_one`, against this branch's `BruhatReflection` /
`bruhatLe_inv_iff`. Same chain, same shape, same root cause. **Two independent
confirmations of one negative**, which is worth more than either alone. Their
remedy was rebuilding root-first by hand; `_standard_dirty` now does it
automatically, so the class cannot recur silently.

They also judged the full extension infeasible here, on two grounds: SIGSEGV
closures and ~860 MB disk. **The disk half is what the chunking answers.** The
SIGSEGV half stands untouched — those modules still will not compile in this
container; they are now labelled unverified rather than mistaken for defects.
