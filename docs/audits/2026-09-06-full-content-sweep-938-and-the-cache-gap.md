# The full content sweep: 938 files, 8 RED, and none of the 8 is the corpus

**Date:** 2026-09-06 · **Bean:** `qou-tpdg` · **Branch:** `claude/lean-sweep-wrong-mathlib-tree-2026-09-05` (PR #6827)

The content half of the Lean gate had never been run to completion on this
container — PR #6827's own body lists it under *"Not claimed"*. It has now run,
at its **true scope**, and produced three results that must be kept separate
because two of them are about the environment rather than the corpus.

## 1. The sweep is 938 files, not 261 — and `AGENTS.md` says 261

```
=== swept 938, RED 8 ===
```

`AGENTS.md` §"`exit 0` is a claim about the SNAPSHOT" — the repo's primary Lean
verification guidance — says *"261 content blocks"*. That figure predates a
sibling's coverage fix, which `scripts/lean-content-sweep.sh` records in its own
header:

> *"…is the wrong population: measured 2026-09-05 there are 938 content-block
> `.lean` files and that filter reached 263 of them. The other 675 import only
> Mathlib — they are still content blocks, still compiled by nothing else in the
> repo… A 28%-coverage sweep reporting "0 red" is the kind of green this whole
> bean is about."*

Measured here independently, both populations:

| population | count |
|---|---|
| content-block `.lean` files (all) | **938** |
| of those, carrying an `import QOU` line | **262** |

So the stale figure understates the gate's scope by **3.6×**. Corrected in
`AGENTS.md` in this commit. This is documentation currency, not a defect in
anything: the sibling's fix landed and the guidance did not follow it.

## 2. All 8 REDs are a gap in the restored olean cache, not corpus defects

Every one of the 8 is the same error class — a missing Mathlib olean, named at
the file's own `import` line:

| missing module | blocks affected |
|---|---|
| `Mathlib.Topology.FiberBundle.Basic` | `reeb-bundle`, `vertex-operator`, `categorical-transfer-matrix` |
| `Mathlib.RingTheory.HopfAlgebra.Basic` | `gb-depth-period-correspondence`, `hq-bi-filtration`, `tannaka-krein-reconstruction` |
| `Mathlib.Analysis.Complex.UpperHalfPlane.Basic` | `algebraic-geometric-dilog-equivalence` |
| `Mathlib.Analysis.Real.Pi.Bounds` | `w-boson-mass-discrepancy` |

**Established, not inferred.** Three checks, in increasing strength:

- **The modules are absent from BOTH olean trees**, so this is not #6827's
  paper-tree-first ordering hiding a tree that has them:

  | module | paper tree | root tree |
  |---|---|---|
  | `Analysis.Complex.UpperHalfPlane.Basic` | MISSING | MISSING |
  | `Topology.FiberBundle.Basic` | MISSING | MISSING |
  | `RingTheory.HopfAlgebra.Basic` | MISSING | MISSING |
  | `Analysis.Real.Pi.Bounds` | MISSING | MISSING |

- **It reproduces with no shadow and no sweep at all** — plain restored cache,
  `LEAN_PATH="$LP"`, one file:

  ```
  reeb-bundle.lean:1:0: error: object file '…/Mathlib/Topology/FiberBundle/Basic.olean'
    of module Mathlib.Topology.FiberBundle.Basic does not exist
  ```

- **The gap is exactly 4 modules wide.** Of the **252** distinct Mathlib modules
  directly imported anywhere in the content-block corpus, **4** are missing from
  the restored cache — the four above, and nothing else.

**So the corpus result is: 930 of 938 verifiable and green; 8 unverifiable on
any container restoring `lake-cache/qou-v4-24-0`.** That is a gap in the cache
branch relative to what the corpus imports, and it is invisible to a sweep that
reports it as RED — which is why it is recorded here rather than left as eight
red lines in a log.

**Do not "fix" these 8 by editing the content blocks.** Their imports are
legitimate; the cache is short. The fix is at the cache branch (a reseed that
includes these four cones), or a documented expected-RED list so the gate
distinguishes *cannot verify* from *fails*.

## 3. The real olean tree DID change mid-sweep — and neither sweep did it

The safety invariant #6827 asserts is that the hardlinked shadow never writes
through into the real olean tree. The before/after snapshot over the QOU tree
came back **2660 → 2713**: 0 deleted, **53 new**, **62 rewritten** in place.

**That is not the sweep.** Read the write path rather than trusting the diff —
`scripts/lean-shadow-verify.sh` writes only inside `$SHADOW` and unlinks before
writing:

```sh
out="$SHADOW/${m//./\/}.olean"
rm -f "$out" "${out%.olean}.olean.hash" "${out%.olean}.ilean"
(cd "$PKG" && LEAN_PATH="$LP" lean $LEAN_OPTS "${src#$PKG/}" -o "$out")
```

The writer was the **SessionStart background build**, `scripts/lean-build-bg.sh`,
which this session's compaction re-fired: `/tmp/qou-lean-build-status.json` is
stamped `07:31` — during the sweep — with `{"status": "failed", "attempts": 5}`,
and all 115 changed paths are under `QOU/`, `QOU.olean` among them, which is what
`lake build QOU` produces and what no sweep touches.

**Methodological consequence, and it applies to every future run of either
sweep:** the before/after olean-tree invariant is **not attributable to the
sweep** unless the background build is quiesced first. This run's diff would have
read as *"the shell verifier mutates the real tree"* — a false accusation against
the fix under review, in the direction that would have blocked a correct change.
A concurrent `lake build` is also the eviction hazard `AGENTS.md` documents
(6990 → 334 mathlib oleans, silent), so it is not merely a measurement nuisance.

## 4. `lake build` independently confirms PR #6909

The same background build is the strongest evidence yet for the *other* PR, and
it is evidence neither I nor the sweep produced. It ran on **#6827's branch**,
which contains **no `.lean` change at all**, and reported exactly 8 errors:

```
✖ [6459/6460] Building QOU.Eightfold.ObstructionClassForcesComplexType (6.4s)
error: QOU/Eightfold/ObstructionClassForcesComplexType.lean:57:48: unknown tactic
error: QOU/Eightfold/ObstructionClassForcesComplexType.lean:57:44: unsolved goals
error: QOU/Eightfold/ObstructionClassForcesComplexType.lean:55:49: unsolved goals
error: QOU/Eightfold/ObstructionClassForcesComplexType.lean:49:44: unsolved goals
error: QOU/Eightfold/ObstructionClassForcesComplexType.lean:68:3: unknown tactic
error: QOU/Eightfold/ObstructionClassForcesComplexType.lean:64:74: unsolved goals
error: Lean exited with code 1
error: build failed
```

Same file, same six source positions #6909 reports. So the defect is confirmed by
**`lake build` itself**, the canonical path — not only by `lean`-direct and not
only by the sweep. And `[6459/6460]` says lake built 6459 modules with this as the
sole failure, so the library is otherwise green **library-wide**, a stronger
statement than the library sweep's 145-module dirty closure can make.

## Two count coincidences, neither of which means anything

Both are recorded because each is exactly the shape that produces a wrong
inference, and one of them already did.

- **8 content-sweep REDs vs 8 `lake build` errors.** Different sets entirely:
  the first is four missing Mathlib oleans across eight content blocks, the
  second is six source positions in one library file plus two rollup lines.
- **8 REDs vs the "8 REDs from my empty-shadow experiment" in PR #6827's body.**
  That body says they are *"artifacts of that experiment, not corpus findings"*.
  Given the cache gap measured above — reproducible with **no shadow at all** —
  that attribution is **unestablished**, and most likely wrong: the experiment
  coincided with a gap that was there the whole time. The experiment's log is not
  recoverable, so this cannot be settled either way; the sentence is corrected on
  the PR rather than left standing.

## What is not claimed

- Whether the 4 missing modules were absent from the cache seed or evicted later
  is **not** established. `lake update` (06:44), `lake exe cache get` (07:01) and
  `lake build` (07:24–07:31) all ran on this container before the measurement, and
  any of them could have moved the tree.
- Nothing here re-runs `lake build QOU` deliberately to investigate; on a restored
  tree that is the documented eviction hazard, and the log that answered the
  question already existed at `/tmp/qou-lake-build.log`.
