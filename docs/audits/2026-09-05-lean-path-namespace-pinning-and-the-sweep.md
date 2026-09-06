# `LEAN_PATH` pins a namespace to one root — and the library sweep was measuring itself

**Date:** 2026-09-05 · **Bean:** `qou-tpdg` · **PR:** #6827 ·
**Script:** `scripts/lean-library-sweep.py`

## The mechanism — ALREADY DOCUMENTED in the corpus; I re-derived it

**🛑 Credit first, because I initially wrote this up as a discovery and it is
not one.** Line 27 of `scripts/lean-shadow-verify.sh` already states the rule:

> *"Lean resolves a module from the first `LEAN_PATH` root holding that package
> directory, so the shadow must be complete, not a sparse overlay"*

So the mechanism was known and written down, two lines from the code I was
editing. My empty-shadow experiment tested a question that comment already
answers, and my three-way measurement below **confirms a documented fact rather
than establishing a new one**. What is genuinely new is the quantification, and
the fact that the *Python* sweep carries no equivalent comment — which is why it
was re-derived there rather than read.

**Lean commits to the first `LEAN_PATH` root that contains the module's
top-level namespace directory, and never consults a later root for anything
under that namespace.** It is not a per-file search down the path.

Measured three ways on a single import (`QOU.Mass.ColorSpectralCubicGeometry`,
whose olean is present in the real tree at 476 544 bytes), varying only what
the first root contained:

| first root on `LEAN_PATH` | real tree also on path | result |
|---|---|---|
| directory with **no `QOU/`** | yes, last | **exit 0** — falls through |
| directory with `QOU/` holding **one unrelated** module | yes, last | **exit 1**, `does not exist` |
| *(control)* real tree only | — | **exit 0** |

So a **partial overlay MASKS the tree behind it** rather than layering over it.
The error message names the *overlay* path, which reads as "this module is
missing from the corpus" when the module is present and simply unreachable.

### This is a live trap in the `lean`-direct recipe every agent uses

`AGENTS.md` prescribes `LEAN_PATH="$SP/oleans:$LP"` with the overlay **first**.
Once `$SP/oleans/QOU/` exists — which it does the moment you build one module
into it — **every** `QOU.*` import resolves against the overlay alone. The
recipe is therefore correct only if the whole QOU-side import cone is already
in the overlay.

The verification of `QOU/Braiding/SkeinNormalisation.lean` on PR #6820 passed
under that recipe **because its QOU-side cone happens to be four files**
(`SkeinNormalisation` → `WeakVertexCouplingNormalisation` →
`WeakVertexSubstitutionScale` → `WeakVertexT35TraceClosedForm`, then Mathlib),
all of which had been built into the overlay. That is luck about the cone, not
safety in the recipe. A file importing a QOU module absent from the overlay
fails with `does not exist` even though the module is on disk — and an agent
reading that would reasonably conclude the corpus is broken.

## Defect 1 — the sweep globbed a Mathlib tree the documented restore does not GUARANTEE

`LEAN_PATH` was built from `ROOT/.lake/packages/*` plus each paper's own
**build output**, and never each paper's `.lake/packages/`. The documented
sandbox restore (`AGENTS.md` §"Mathlib cache 403 fallback") populates the
**paper** one:

| Mathlib tree | `Mathlib/Tactic.olean` | `Mathlib/Data/Real/Basic.olean` | oleans |
|---|---|---|---|
| **ROOT** `.lake/packages/mathlib` | **0 bytes**, dated Aug 7 | **missing** | 1212 |
| **PAPER** `content/…/lean/.lake/packages/mathlib` | 68 040 B, Aug 29 | 785 328 B | 3477 |

Every Mathlib-importing module therefore failed with `invalid header` or
`does not exist`, and the sweep reported **22 REDs about its own environment**,
formatted identically to real findings. Fix: glob both package locations,
paper-level first.

> **🛑 CORRECTED on review — my claim was one container generalised into a
> universal.** The scripts' author measured the same two files on *their*
> container and the ROOT tree is **fine** there:
>
> | | `Mathlib/Tactic.olean` | `Mathlib/Data/Real/Basic.olean` | oleans |
> |---|---|---|---|
> | **ROOT**, their container | 68 040 B | 785 328 B | **6990** |
> | **PAPER**, their container | 68 040 B | 785 328 B | 3477 |
>
> Byte-identical, and the root is a *superset*. That is why their sweeps
> returned real findings rather than 22 environment-REDs, and why they never
> hit this.
>
> **So "the root tree is broken" is FALSE as a general claim** — it was true of
> this container only. The defensible statement is **"the root tree is not
> *guaranteed* to be populated"**: `AGENTS.md` §"Mathlib cache 403 fallback"
> fills the **paper** tree, so that is the one the documented restore
> guarantees. Globbing the root alone makes the gate's correctness
> environment-dependent *by luck*, which is not a gate — and that argument
> holds on both containers, where mine held on one.
>
> The fix is unchanged and still right; only its justification needed
> narrowing. Recorded because this is the absence-of-evidence discipline
> failing in the other direction: I measured one environment and wrote a
> universal.

## Defect 2 — the 2.3 GB shadow made the sweep unrunnable

`shutil.copytree` of the olean tree needs ~2.3 GB; this container had 1.1 GB
free against a per-session quota, so the sweep died on `ENOSPC` having judged
nothing. The shadow is now **hardlinked**: `du` reports 2.3 GB while `df` does
not move, because hardlinks allocate no blocks. `build()` unlinks its target
(and same-stem `.olean.hash` / `.ilean`) before `lean -o` writes, so a rebuild
never writes through a shared inode into the real tree. Real-copy fallback on
`OSError` for a cross-device or hardlink-hostile shadow.

**The full tree in the shadow is NECESSARY** — see the mechanism above. The
tempting simplification (skip the copy, rely on fall-through) does not work,
and shipping it would have left the sweep judging almost nothing while looking
greener.

## Result

| | before | after |
|---|---|---|
| dirty closure | 22 | 22 |
| RED | **22** (all false) | **0** |
| skipped on red dependency | 15 | **0** |
| wall time | died on `ENOSPC` | **33 s** |
| real-disk cost of the shadow | 2.3 GB (unaffordable) | **0 blocks** |

**Safety, verified rather than argued:** the real olean tree's 2660 files were
snapshotted by inode, size and mtime before the run and compared after —
**identical on all 2660**, so the hardlinked shadow provably does not mutate
the tree it links to.

The recorded baseline for this sweep was "74 stale modules, zero red" and
122 s; this container's closure is 22, and the two figures are not comparable
because the dirty closure is computed against *this* container's olean tree
(the container-scoped caveat `AGENTS.md` already states). Re-measure; do not
quote either.

## Not done here

The `AGENTS.md` `lean`-direct recipe is **not** edited on this branch — the
overlay-masking trap is recorded above and left for the author, since changing
the primary Lean verification guidance is not a change to make in passing.

**The sibling gate WAS audited, and carried the same pair.**
`scripts/lean-content-sweep.sh` delegates its entire `LEAN_PATH` and shadow
construction to `scripts/lean-shadow-verify.sh`, which had both defects —
root-only package glob, and a real `cp -a` — plus two of its own:

- **the documented `SHADOW=<dir>` reuse path never created its directory**
  (`$SHADOW` was only made by `mktemp -d` in the *unset* branch), so the
  advertised form failed on first use with `cp: cannot create directory`;
- **my own fix to the glob reintroduced the bug it fixed.** I wrote
  `ls -d <paper-pattern> <root-pattern>`, and **`ls` sorts its arguments** —
  `$ROOT/.lake/…` sorts before `$ROOT/content/…`, so the broken root tree came
  back *first* and Mathlib still resolved against it. Replaced with a loop;
  shell glob expansion keeps patterns in written order. The original was safe
  only because it had a single pattern.

Verified: `SHADOW=<dir> lean-shadow-verify.sh QOU/Braiding/SkeinNormalisation.lean`
→ **exit 0**, both dirty cone modules rebuilt, and the real tree's 2660 files
**identical in inode, size and mtime** before/after.
