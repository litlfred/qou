# The full-library sweep: five false reds, one real one, and what "outside the root build" costs

**Bean:** `qou-g5sp`. **PR:** #7124. **Date:** 2026-09-08.
**The run is complete: all 163 chunks, all 2774 library modules.**

## What was being measured, and why it needed measuring

`scripts/lean-root-coverage-audit.py`, re-run on `main` `1ec22a9040c`:

```
modules on disk    2773
root closure       1449   (TRANSITIVE — what `lake build` builds)
NOT in the root    1324   (48%)
```

**🛑 Those are the CORRECTED figures, and the correction is this document's own.**
The script measured the root's **direct import lines** (910) and called everything
else "not in the root", giving **1863 (67 %)**. `lake build QOU` builds the
**transitive closure**, which is **1450** modules including the root — so the gap
is **1324 (47.7 %)**, and the overstated figure had reached `qou-g5sp`'s headline,
the script's own docstring, an earlier revision of this document and a PR body
before anyone checked. The script's docstring said "import closure" while its code
summed one line each. Fixed in the same PR; **quote the transitive number.**

Half the library outside every routine build is still the finding. Bean
`qou-g5sp` established it and asked the obvious next question — *how many of the 1863 are actually
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
| shadow cost per module, TRANSIENT | — | **0.22–0.29 MB** — a `df` delta during a chunk, reclaimed at chunk end |
| shadow cost, STEADY STATE | — | **11 MB total** — 38 files with link count 1; `du`'s 2.4 GB is ~all shared inodes |
| full corpus | 3.1 h | **~70 min** |
| full corpus disk, unchunked | ~800 MB | **~640 MB** at once |
| full corpus disk, chunked | — | **one chunk's transient allocation**, which is why it fits a container at 99 % |

## Six gate defects against one real corpus defect

**That ratio is the honest headline of this work.** A gate this young reporting on
2774 modules is mostly reporting on itself, which is exactly why every red was
triaged before it was believed. Six modules came back red; five were the gate. A
sixth gate defect had no red at all and is the worst of them — see the table's
last row. They are listed in the order found, because each was indistinguishable
from a real defect until the specific check beside it was run.

| # | symptom | what it actually was | fix |
|---|---|---|---|
| 1 | `object file '…/QOU/Machinery/BruhatRankCriterion.olean' … does not exist` | `--only` filtered the population but not the **never-built** dep cone. 60 modules have no olean at all, so any importer of one across a namespace boundary was a guaranteed spurious red. 5 modules exposed; 24 such deps belong to the library root alone. | `--only` closes over them |
| 2 | the library **root got no chunk** | the driver enumerated namespaces by walking `QOU/`, and `QOU.lean` is not under `QOU/` — the same enumeration bug #6827 fixed in the closure, reintroduced one layer up | root sweeps first |
| 3 | `Unknown identifier bruhatLe_inv_iff` | **the snapshot.** The lemma exists at `CoxeterBruhat.lean:149`, that module *is* in the 24-module import closure, its namespace *is* opened — and it was added 2026-09-07 07:04 (`8ca51eb3ddc`) while the snapshot olean dates from 2026-09-06 07:04. `strings` finds the symbol 0 times. | `_standard_dirty`: `--only` closes over **stale** deps too |
| 4 | root chunk selected all **2774** modules | `--only QOU` is a **prefix** and every module starts with it. Would have ENOSPC'd at 489 MB free — the exact failure chunking exists to prevent, caused by the mechanism meant to prevent it. | `--only-exact` → 101 |
| 5 | `exit 139`, zero bytes of output | SIGSEGV on a large closure. **Not mine** — a sibling measured 5 of these on `QOU.Hecke.*` H3A/H4A (`333e491eaa4`); my sweep would have called every one RED. | new `UNVERIFIED` verdict |
| 6 | **no red at all — silence** | the driver listed every top-level entry under `QOU/`, which includes plain `.lean` **files**. `--only QOU.Basic.lean` matches nothing, so **65 chunks were silent no-ops**; worse, `${ns%.lean}.log` sent `BraidKnot.lean` to `BraidKnot.log` and a one-module no-op **overwrote a real 456-module result**. Caught only because the driver claimed 139 chunks while 69 logs carried a summary. | distinct log names + exact selector per kind |

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
and therefore **the library root itself** unjudgeable here.

> **🛑 CORRECTED 2026-09-08 — this paragraph named the wrong remedy at a wildly
> wrong price, and both errors were mine.** It read: *"Remedy is a sibling's
> `scripts/lean-restore-gap-oleans.sh`, deliberately not run mid-sweep: it fetches
> ~1.7 GiB into a `.git` already at 13 GB."* Two things are wrong.
>
> **It does not fetch 1.7 GiB.** That script fetches
> `lake-cache/qou-<slug>-mathlib-gap-modules`, whose payload is a **2.3 MB**
> tarball. I conflated it with the *full* olean cache branch, which is the 1.7 GiB
> one. The estimate was off by ~700×, and I deferred the work for hours on it.
>
> **And it is not the remedy.** That branch ships **seven** prebuilt oleans for
> content blocks; `LowDegree` is **not among them**, so running it would not have
> made the root judgeable. It was run, and did not.
>
> **The actual remedy is to build from source**, and it is cheap: the missing cone
> is **79 Mathlib modules**, all of whose sources are present, at **188 s and
> 57 MB** — `scripts/lean-build-mathlib-gap-cone.py`. With them in place the sweep
> reports `[101/101] ok QOU`: **101 ok, 0 RED, 0 UNVERIFIED, 0 skipped**.
>
> **So the library root is verifiable in this container**, and the standing
> attribution to a container resource limit (bean `qou-ed8a`, repeated in a
> sibling's merged audit) is wrong. The lesson is the cheap one: I priced a script
> from its family resemblance to another script instead of reading its own
> `git fetch`. Full write-up: PR #7157.

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

All 163 chunks completed. Counts are **distinct modules, unioned by name** — never
a sum of per-chunk totals, because a chunk reports its pulled-in cross-namespace
deps as `ok` too (the naive sum reached 2200 with 2193 still outstanding against a
library of 2774, which is how that was caught).

| | count |
|---|---|
| chunks completed | **163 of 163** |
| library modules **covered** | **2774 of 2774** — none unseen |
| `ok` | **2754** |
| **RED — corpus defects** | **0** |
| UNVERIFIED — cannot judge here | 1 |
| TIMEOUT — not judged | 4 |
| SKIPPED — behind one of the above | 16 |

### The residue is four clusters, none of them a defect

Twenty modules were never seen `ok`. They are three timeout cascades and one
missing Mathlib olean:

| cluster | n | why |
|---|---|---|
| `QOU` (the root) + `Eightfold.ObstructionH2Mathlib` | 2 | the **mathlib cache gap** — `…GroupCohomology.LowDegree` absent from both trees; the root is skipped behind it |
| `Machinery.HeckeH4*` | 10 | `HeckeH4BlockMap211` / `…31` TIMEOUT, 8 skipped behind them — **the same `QOU.Hecke*` H4 family a sibling measured as SIGSEGV** |
| `MathlibExt.Octonion*` | 6 | `OctonionDerivationsUpperBound` TIMEOUT, 5 behind it |
| `Archimedean.PauliWitness*` | 2 | `Witness12B` TIMEOUT, parent behind it |

**So the library root is not broken — it is unverifiable in this container for want
of one Mathlib olean.** That distinction is the whole purpose of the UNVERIFIED
class; under the classification this branch started with, it would have read as a
red root.

> **🟩 SUPERSEDED 2026-09-13 — the root COMPILES here now.** The missing olean was
> seeded to `lake-cache/qou-v4-24-0-mathlib-gap-modules` (7 → 86 oleans,
> `d7e3ae8c662`, 2026-09-11) and is restored by
> `scripts/lean-restore-gap-oleans.sh`. With it on disk,
> `lean-library-sweep.py --package QOU --only-exact QOU --jobs 2` on `main`
> `c9fd78b0a` reports **1451 ok, 0 RED, 0 TIMEOUT, 0 UNVERIFIED, 0 skipped**,
> ending `[1451/1451] ok QOU`. The *reasoning* in this section was right and its
> UNVERIFIED class is what made the gap legible as a gap; only the state has
> moved. See
> [`2026-09-13-library-root-compiles-1451-modules-zero-red.md`](2026-09-13-library-root-compiles-1451-modules-zero-red.md).

### The answer to `qou-g5sp`, on the corrected denominator

| | count |
|---|---|
| modules outside `lake build QOU`'s transitive closure | **1324** |
| of those, **verified ok** | **1323** |
| of those, not ok | **1** — `Machinery.HeckeH4RepDecomp`, a timeout cascade |
| **real corpus defects found in the blind spot** | **1** — `Machinery.BruhatRankCriterion`, fixed |

And the defect was genuinely in the blind spot: `BruhatRankCriterion` is **not** in
the transitive closure, so `lake build QOU` would not have compiled it — nor would
it have compiled `DominanceIsBruhat`, `BruhatReflection` or `CoxeterBruhat`. The
whole Bruhat/Coxeter component sits outside. That check matters because had the
module turned out to be *inside* the closure, this instance would not have
supported the bean's thesis at all.

**The scoping question `qou-g5sp` raises — whether to add the missing imports to
`QOU.lean` — now has its measurement: the blind spot held exactly one real defect
across 1324 modules.** That is the owner's decision and this document does not
make it.

## What this result is NOT

- **Not a single-run green.** A chunked run resolves an earlier chunk's imports
  against the snapshot, so it is strictly weaker. Stated, not buried.
- **Measured on a slightly older tree.** The sweep ran before this branch was
  rebased onto `main`; it covered **2774** modules, and the rebase brought the
  library to **2786**. So ~12 modules that landed in those 172 commits are
  unmeasured here, and the coverage split moved 1324 → **1337 of 2786** (still
  48 %). The cheap standing check for the remainder is the sweep's normal
  dirty-closure mode, not another full pass.
- **Not a single-version measurement, unless the re-run completed.** The root and
  BraidKnot chunks ran before the `UNVERIFIED` class and the caller fix landed;
  their logs are kept as `*.log.PRE-FIX` and both were staged for a clean re-run.
  An aggregate mixing pre- and post-fix logs must not be published.
- **Not a proposal about the 1863 imports.** Scope is the owner's decision and
  follows the count, per `qou-g5sp`.

## Two measurement lessons, both from getting them wrong here

**Disk: I misread it twice, in opposite directions, and both errors are the same
mistake — trusting a `df` delta.**

First, free fell 640 MB → 380 MB and the sweep was the obvious suspect, having
just been measured at 0.23 MB/module. It was innocent: the real olean tree stayed
**static at 2718** all run — the shadow's no-write-through invariant holding — and
the growth was **233 MB of this agent's own harness `tasks/*.output` captures**.
Pruning the ones already read freed 160 MB.

Then a later reading of **138 MB free** was called critical, and the recovery plan
was to delete `/tmp/lean-v4.24.0` (2.5 GB). **That directory IS the live
toolchain** — both `~/.elan/toolchains/*` entries are symlinks into it, so removing
it breaks `lean` and kills the sweep. Looking at the target before deleting is the
only thing that caught it. And the alarm was itself false: 138 MB was a **mid-chunk
trough**, and free returned to **773 MB** once the driver reclaimed the shadow.

**What to measure instead.** Take disk readings at **chunk boundaries**, and cost
the shadow by counting files whose link count is 1 rather than by `du` or a `df`
difference: **38 files, 11 MB**. Everything larger is shared inodes. A projection
built on the transient figure — that the three staged re-runs "need ~216 MB and
will not fit" — was wrong for exactly this reason.

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

> **🛑 RETRACTED 2026-09-13 by the agent whose measurement it rests on — the
> SIGSEGV half does NOT stand.** "Those modules still will not compile in this
> container" traces to my five `exit 139` results at `333e491eaa4`, and to my
> attribution of them to *"the same container resource limit that makes the
> library root unverifiable (`qou-ed8a`)"*. **That limit does not exist** — it was
> 79 missing Mathlib oleans. Every module either of us flagged as SIGSEGV-family
> or TIMEOUT compiles: `HeckeH4BlockMap211`, `HeckeH4BlockMap31`,
> `OctonionDerivationsUpperBound` and `Witness12B` are all **ok** in the
> 2026-09-13 run, the first two *concurrently*. The five `exit 139` observations
> themselves stand — something segfaulted — but the attribution was a symptom
> matched to a cone diagnosed elsewhere, and this document inherited it from me on
> family resemblance, which is the exact move it is otherwise about.
