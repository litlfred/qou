# Library-tree Lean sweep — the cone builder was broken, and 38 modules are red (73 % coverage)

**Date:** 2026-08-08 · **Bean:** `qou-k448` · **Branch:** `claude/k448-library-lean-red-sweep-2026-08-08`
**Tier:** survey / tooling. **No math claims. No content changed. No fit.**

## Why this exists

`QOU/Eightfold/WeylInvarianceQDeformation.lean` was found **red on `main`** by accident
(PR #4727) — not by any checker. The structural reason it survived:

- All **1611** `.lean` files under `content/**/lean/QOU/**` are **un-sidecar'd** (no
  `<block>.qa.json`), so `lean-content-siblings.yml` does not cover them.
- Repo-wide CI auto-triggers are disabled (owner directive 2026-06-30, Actions billing).

So nothing reads the library tree at all, and a red file can sit indefinitely. This
sweep asks: **how many others are there?**

## The tooling was structurally broken

`scripts/lean-direct-cone.sh` — the intended instrument — could not survey anything.
Its topo-sort does `os.walk("QOU")`, which enumerates 1621 modules but **never sees the
root aggregator `lean/QOU.lean`**, because that file is a *sibling* of the `QOU/`
directory, not inside it. So `imp["QOU"]` is absent, `visit("QOU")` treats the target as
a zero-import leaf, `ORDER = ["QOU"]`, and `lean` is invoked directly on the ~1000-import
aggregator with no dependencies built. The observed
`QuadraticIrrationalBadlyApproximable.olean does not exist` was **not a red module** —
that module was simply never scheduled.

Fixed on this branch, along with `--all` (whole-corpus mode), `--keep-going`, a
`--min-free-gb` disk guard, capped failure logs, and an incremental TSV report. The
dependent-blocking propagation is the load-bearing part: it is what separates a
**genuine** error from a **cascade**.

## Results — 1187 of 1622 modules settled (73.2 %)

| status | count | meaning |
|---|---|---|
| `ok` | 665 | compiled **this run** |
| `up-to-date` | 471 | olean already present and newer than source — **not recompiled this run** |
| **`error`** | **38** | genuine failure |
| **`blocked`** | **13** | not compiled; a transitive dependency is red (cascade) |

**Bounds:** genuine reds are **38** (lower bound = measured). The upper bound including
cascade-suspects is **51**. The 13 blocked trace to only **6 distinct red roots**:

| red root | blocks |
|---|---|
| `KnotTheory.Vassiliev.ChordDiagram` | 5 |
| `Machinery.HeckeTauAssignmentGroupoidFunctor` | 3 |
| `Mathlib.SpectralSequence` | 2 |
| `Mass.ComplexVolumeZeta4Partner` | 1 |
| `BraidKnot.SubstrateEWHypotheses` | 1 |
| `QuantumBloch.PentagonUvCommutation` | 1 |

## Failure shapes

| count | shape |
|---|---|
| **19** | **`Invalid field` — dot-notation onto a field the environment does not contain** |
| 14 | other |
| 2 | parse error (`unexpected token`) |
| 2 | unknown identifier / other |
| 1 | ⚠ **suspect classification** — see below |

The dominant class is coherent and actionable: 19 of 38 are `Invalid field`, the classic
signature of **Mathlib API drift** (a field or lemma renamed upstream, leaving
dot-notation dangling). Example: `QBeta/FaddeevModularDouble.lean:117` —
`Invalid field 'sq_eq_one_of_bar_even': The environment does not contain
'Eq.sq_eq_one_of_bar_even'`.

**One row is suspect and is NOT counted as confirmed:** `QOU.Mathlib.HeckeAlgebra`'s
captured `error_head` is a *warning* (`204:5: warning: unused variable 'I'`), not an
error. Either the classifier captured the wrong line or the module is not actually red.
So the confirmed count is **37–38**, pending one manual check.

## Honest limits on this number

Read these before citing anything above.

1. **Coverage is 73.2 %, not 100 %.** The run did not finish: throughput collapsed from
   ~122 modules/10 min to ~7/10 min as the frontier moved from cheap leaf modules into
   deep Mathlib-heavy cones, and the container then restarted. The surviving
   `.partial` TSV is the data.
2. **Coverage is NOT a random sample.** The topo-order frontier settles shallow cones
   first, so the surveyed set is biased toward cheap leaves and the **unsurveyed 435
   modules are systematically Mathlib-heavier**. The 38/1187 ≈ 3.2 % rate therefore
   **must not be extrapolated** to the corpus — deeper modules plausibly fail at a
   different rate in either direction.
3. **The 471 `up-to-date` modules were not recompiled this run.** They had oleans newer
   than source, so they compiled successfully at *some* point, but this run is not fresh
   evidence for them. Freshly-verified-this-run is **665**.
4. **Per-module failure logs did not survive** the container restart
   (`/tmp/lean-cone-logs/` is empty); only the TSV's truncated `error_head` column
   remains. Re-running is needed for full diagnostics on any individual module.

## Retro-invalidation — do not cite the earlier number

An earlier pre-fix sweep in the same session reported **129 reds in 490 files** using
per-file `lean-verify.sh` with no dependency ordering. **That number is junk** and must
not be cited. Without a built QOU olean tree, most failures were missing-olean cascades,
not genuine errors — in a hand-check of the first 62 red logs, 42 were missing-olean and
only 20 had a real `error:`. The cascade-vs-genuine distinction is exactly what the
dependent-blocking fix supplies, and the corrected picture (38 genuine against 13
blocked) shows cascades are a **small** fraction once the cone is built properly.

## What to do next

1. **Confirm or drop the one suspect row** (`Mathlib.HeckeAlgebra`).
2. **Finish coverage** — re-run `--all -k -j3` on the 435 unsettled modules. Cheap now
   that ~1268 QOU oleans exist; the expensive part is already banked.
3. **Fix the 6 cascade roots first** — that clears 13 blocked modules for the price of 6.
4. **Triage the 19 `Invalid field` cases as one class**, not 19 tickets: they are
   probably a small number of upstream renames.
5. **Close the structural hole.** A green library tree today says nothing about tomorrow
   while nothing watches it. Either sidecar the library tree or add a periodic cone
   build; otherwise this survey decays immediately.
