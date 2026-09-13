# The library root `QOU` compiles here — 1451 modules, 0 RED. Three claims retracted, one of them mine

*2026-09-13, measured on `main` `c9fd78b0a`.*

## The measurement

```
scripts/lean-library-sweep.py --package QOU --only-exact QOU --jobs 2

  library modules        2833
    source-changed        2699
    never built (new)      134
    DIRTY CLOSURE         1451
    snapshot-current      1382
  parallelism: --jobs 2 x 2 thread(s) = 4 of 4 cores
  ...
  [1451/1451] ok   QOU

=== library sweep: 1451 ok, 0 RED, 0 TIMEOUT + 0 UNVERIFIED (NOT failing),
    0 skipped (dependency red), 8542s ===
```

**The library root compiled.** So did every one of the 1451 modules in its dirty
closure, in 2 h 22 m on a 4-core container, with nothing left unverified and
nothing skipped.

## What this retracts

### 1. "The root is unverifiable in this container" — MINE, and wrong on its premise

I wrote, in bean `qou-ed8a` and again in `qou-g5sp`, that the library root is
*"unverifiable in this container, not broken: SIGSEGV on its 896-module closure
**even with all imports present**."*

The imports were **not** all present. 79 Mathlib oleans were missing; the cone
builds from source in 188 s and packages to 22 MB. The gap is closed on
`lake-cache/qou-v4-24-0-mathlib-gap-modules` (7 → 86 oleans, `d7e3ae8c662`,
2026-09-11) and `scripts/lean-restore-gap-oleans.sh` restores it. With them on
disk the root compiles, as measured above.

The clause that made this an *inference* rather than a measurement is "even with
all imports present" — I never checked that, and it was false. AGENTS.md already
names the misattribution; this is the run that closes it.

### 2. "The SIGSEGV half stands untouched — those modules still will not compile in this container"

[`2026-09-08-full-library-sweep-and-five-false-reds.md`](2026-09-08-full-library-sweep-and-five-false-reds.md)
§"they also judged the full extension infeasible here" leaves this standing,
resting on my five `exit 139` results at `333e491eaa4`. Every module a sibling
or I flagged as SIGSEGV or TIMEOUT compiled **ok** in this run:

| module | prior verdict | here |
|---|---|---|
| `Machinery.HeckeH4BlockMap211` | TIMEOUT (`--jobs 3`), and called SIGSEGV-family | **ok** |
| `Machinery.HeckeH4BlockMap31` | TIMEOUT (`--jobs 3`) | **ok** |
| `MathlibExt.OctonionDerivationsUpperBound` | TIMEOUT | **ok** |
| `Archimedean.PauliWitness.Witness12B` | TIMEOUT — 1471 s exclusive vs an 1800 s budget | **ok** |

`HeckeH4BlockMap211` and `31` ran **concurrently** here, at 137 % and 98 % CPU,
and both finished inside the budget. So they pass *with* contention at
`--jobs 2 × 2 threads`; what killed them was the old `--jobs 3` default giving
`nproc//jobs = 1` thread each. That is exactly the diagnosis
[`2026-09-08-sweep-timeouts-were-contention.md`](2026-09-08-sweep-timeouts-were-contention.md)
reached, now confirmed from the other side — it predicted these would pass, and
they do.

**What is NOT retracted:** my five `exit 139` observations themselves. Something
segfaulted; zero bytes of diagnostic is a real thing I saw. What is withdrawn is
the *attribution* — "the same container resource limit that makes the library
root unverifiable" — because that limit does not exist, and because I matched a
symptom to a cone I had diagnosed elsewhere instead of measuring these modules.
The four named above are now measured and pass; the exact five that segfaulted
were never named in my bean, which is its own defect and the reason this could
not be checked directly.

### 3. "Sizing the root-missing modules needs a different build environment"

I recorded that measuring how many of the ~1863 modules outside the root build
are genuinely broken could not be done here, after retracting two unsound methods
for it. `--all` with `--only` chunking exists precisely to fit a constrained
container, and this run demonstrates the capacity: 1451 modules, 8542 s, peak
disk comfortably inside the container. The question is no longer blocked.

## The trap that cost the first attempt, live in a fresh container

The first run of this sweep reported `556 UNVERIFIED, 880 skipped` and **zero
source errors** — every one a path artifact. `scripts/lean-cache-restore.sh`
populated the **root** tree (3559 mathlib oleans) while the sweep reads the
**paper** tree, which had **92**. Lean resolves a package from the first
`LEAN_PATH` root holding that package's *directory*, not the first holding the
*module*, so a partial paper `Mathlib/` wins for the whole of Mathlib and the
complete root tree is never consulted. This is bean `qou-4h26`, and
`scripts/lean-sync-olean-trees.sh` is the fix (both trees → 3564).

**A cache restore alone is not sufficient in a fresh container.** The restore
script's own success message is not evidence the sweep can see what it restored.
Sequence that works:

```sh
scripts/lean-cache-restore.sh        # ~3480 mathlib oleans -> root tree
scripts/lean-restore-gap-oleans.sh   # 86 gap oleans -> both trees
scripts/lean-sync-olean-trees.sh     # union-hardlink; both trees -> 3564
scripts/lean-library-sweep.py --package QOU --only-exact QOU --jobs 2
```

## Scope

This is a statement about `main` at `c9fd78b0a` and about the **root's dirty
closure**, not about the whole library: 1382 of the 2833 modules were
snapshot-current and not rebuilt, and 1382 more sit outside this closure
entirely. It does not measure the `~1863 outside the root` population — it
establishes that measuring it here is possible, which is a different claim and
the one being made.

The `source-changed 2699` line is a fresh-checkout artifact (every source file
carries the clone's mtime), not real staleness; the sweep's own
`snapshot-current` split is what keeps that from inflating the closure to
everything.
