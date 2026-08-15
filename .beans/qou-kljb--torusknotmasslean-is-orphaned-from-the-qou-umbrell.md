---
# qou-kljb
title: 795 QOU library modules are never built — lake build QOU cannot see them (270 load-bearing)
status: in-progress
type: task
priority: high
created_at: 2026-08-09T02:12:05Z
updated_at: 2026-08-15T15:12:44Z
---

Surfaced while verifying PR #4824's §1 consolidation claim with the three-way
per-file drop check sibling #4840 proposed. PR #3793 had recorded, in a comment
on `TorusKnotMass.lean`, that a fabricated
`noncomputable instance : TorusKnotMass := ⟨0, rfl⟩` did not typecheck, and
that the resulting non-compiling file "escaped CI only because it is orphaned
from the `QOU` umbrella". That comment was dropped when the instance-removal
reached main by a different route.

**Both halves of #3793's claim are now confirmed.**

## 1. The typecheck claim — verified

At #3793's base (`b759f24f`) the class had **9 explicit fields** including
`factors_distinct : gauge_mass_factor ≠ scalar_mass_factor`. `⟨0, rfl⟩`
supplies 2 of 9, and `gauge_mass_factor = 0` forces
`factors_distinct : (0:ℝ) ≠ 0`, unprovable. It could not have elaborated.

## 2. The orphan/CI claim — verified by experiment

Import-closure walk from `content/quantum-observable-universe/lean/QOU.lean`:

| | count |
|---|---|
| library modules under `lean/QOU/` | 1776 |
| reachable from `QOU.lean` | 981 |
| **unreachable** | **795 (44%)** |

`content/quantum-observable-universe/lean/lakefile.toml` declares

```toml
[[lean_lib]]
name = "QOU"
srcDir = "."
```

with **no `globs` key**. Lake's default is then `globs = #[.one "QOU"]` — only
the root module and its transitive imports are built.

Confirmed by direct experiment rather than inference (throwaway package, root
`Lib.lean` + unimported `Lib/Orphan.lean`, same toolchain `v4.24.0`):

| lakefile | result |
|---|---|
| no `globs` | builds `Lib.olean` only — **`Lib/Orphan.olean` NOT built** |
| `globs = ["Lib", "Lib.+"]` | builds both |

So `lake build QOU` never elaborates them. A module in that set can be
syntactically broken, carry an uncited `sorry`, or fail to typecheck, and no
build will say so.

### Correction — how this bean first read, and why

The first version of this bean **denied** the orphan/CI claim. The reasoning
was: against the restored `lake-cache/qou-v4-24-0` tree, orphaned modules carry
`.olean` artifacts at 56% (440/785, as counted that morning), statistically indistinguishable from
reachable modules at 57% (502/874, as counted that morning), and `TorusKnotMass.olean` is present — so
orphan status appeared not to predict builtness.

That inference was wrong. The oleans are **stale artifacts** left in the build
directory from when those modules were imported or built explicitly; nothing
prunes them, and a tarball snapshot of a long-lived build dir preserves them.
Presence of an olean is evidence that a module was built *at some point*, not
that the current `lake build QOU` builds it. The experiment above tests the
mechanism directly and settles it.

Lesson worth keeping: an artifact-presence survey cannot answer a
"does-the-build-do-X" question. Test the build.

## Why this matters

For these modules (795 as of 2026-08-09) there is currently **no** automated check of any kind:

- `lake build QOU` does not build them (above);
- a library `.lean` with no `.ts`/`.md` sibling has no `.qa.json` sidecar and
  is not covered by `lean-content-siblings.yml` (AGENTS.md);
- CI auto-triggers are disabled repo-wide (`build.yml` is
  `workflow_dispatch`-only).

## Triage (step 1 — DONE 2026-08-09)

Counts re-measured against a newer `main`; the population grew 785 → **795**
as the corpus moved, which is itself the point (orphans accrue silently).

| class | count | meaning |
|---|---|---|
| **load-bearing** | **270** | a content block's `lean.ref` names this module |
| interior | 190 | reachable only from another orphan |
| dead-root candidates | 347 | no `lean.ref`, no orphan importer |

**270 load-bearing is the headline.** Those are blocks whose manifest claims a
Lean formalisation that no build has ever elaborated.

### Do they actually compile? Sampled 22 by `lean`-direct

| sample | n | result |
|---|---|---|
| load-bearing | 12 | 11 pass, 1 dep-gap |
| dead-root candidates | 10 | 10 pass |

**Zero real source errors.** The one non-pass —
`QOU.BraidKnot.symbolic_character_table` — is `object file ... does not exist`
for `QOU.BraidKnot.SytSmallShapeCounts`, i.e. it imports another orphan that
has no olean *because nothing builds it*. Not a source defect; the orphan gap
propagating into its own verification.

### Sorry hygiene holds

33 real `sorry`s across all 795 files (26 files), and **every one carries a
`-- Ref:` within 8 lines — 0 uncited**. (A first pass reported 358/323; that
regex was matching the *phrase* "sorry-free" in prose. Numbers above are with
comments stripped.)

### Revised risk — I over-cautioned

The earlier "expect breakage, could be very red" warning is **not supported**.
The sources look healthy. Two honest caveats before anyone treats that as
"safe":

1. **22 of 795 is ~2.8%.** Zero failures in 22 bounds the failure rate at
   roughly **13%** (rule of three, 95%) — so up to ~100 files could still fail.
   "Most compile" is supported; "all compile" is not.
2. **Per-file `lean`-direct ≠ a whole-library build.** Each file was checked
   alone. Compiling all 795 *into one library* can surface conflicts that
   per-file checking structurally cannot — duplicate declaration names,
   clashing instances, universe issues across modules that never met before.
   This is the residual unknown, and it is the reason to stage the work.

## Next steps

1. ~~Triage~~ — done, above.
2. **Wire up in tranches, load-bearing first.** The 270 with a `lean.ref` are
   the ones where the corpus asserts something unchecked, so they buy the most
   per unit of risk. Add imports to `QOU.lean` (or `globs = ["QOU", "QOU.+"]`)
   a directory at a time, building between tranches so a cross-module clash is
   attributable.
3. **Triage the 347 dead-roots separately** — they sample clean, so they are
   *unwired*, not rotten. Decide per subtree whether to wire or delete;
   deleting healthy proved content would be the worse error.
4. ~~Cheap guard~~ — `scripts/lean-orphan-modules.sh` (read-only, exits
   non-zero when orphans exist, so it can gate once the count is driven down).



## Claimed 2026-08-15 — branch `claude/mtcx-7c-verify-close-2026-08-15` (session qou-xz6t)

Taking step 2 ("which orphans are actually broken?"). **Not** touching the lakefile `globs` yet: this sandbox cannot run `lake build` at all (`.lake/packages/mathlib` was restored from `lake-cache/qou-v4-24-0` with no `.git`, so any dep-resolving lake call wipes 6990 oleans), so a `globs` change here would be unverifiable — exactly the kind of claim this bean's own §2 correction warns against. Surveying with `lean-direct-cone.sh --all -k`, which bypasses Lake entirely, to produce the per-module green/red list that a `globs` flip needs as its prerequisite.


## FINDING 2026-08-15 — the premise is already fixed; the 44 % figure is stale

**`lake build` DOES build these modules.** The lakefile now carries

```toml
[[lean_lib]]
name = "QOU"
srcDir = "."
globs = ["QOU", "QOU.+"]     # "WIDEN THE BUILD TO THE WHOLE TREE (bean qou-rc7b)"
```

`QOU.+` is `Glob.andSubmodules` — the module and **all** its submodules — so every `.lean` under `lean/QOU/` is in the library target whether or not `QOU.lean` imports it. This bean's §2 conclusion ("`lake build QOU` never elaborates them") was true when written on 2026-08-09 and has since been fixed by `qou-rc7b`; the bean was never closed.

**Verified by direct experiment, not inference** — the same throwaway-package method this bean's §2 used, re-run *with* `globs` set (toolchain v4.24.0, no Mathlib, so it cannot touch the restored cache):

```
lakefile: globs = ["Lib", "Lib.+"];  Lib.lean (root) + Lib/Orphan.lean (imported by nothing)
$ lake build
  ✔ [2/4] Built Lib
  ✔ [3/4] Built Lib.Orphan        ← built despite nothing importing it
produced: lean/Lib.olean, lean/Lib/Orphan.olean
```

### Consequence: two pieces of tooling now measure a premise that no longer holds

- **`content/pipeline/lean-orphan-audit.ts`** — its own header states the lakefile has *"`globs` unset"* (line ~15) and it computes reachability by walking `QOU.lean`'s imports (line ~127). Both are now wrong, so its headline "**837 of 1902 modules (44.0 %) are never built by `lake build`**" is **not** a statement about builtness. It measures *umbrella-import hygiene*, which is a real but different (and much less alarming) property.
- **`.github/workflows/lean-orphan-gate.yml`** — its rationale ("a module nothing imports is never compiled by anything, ever") no longer holds. The gate may still be wanted for umbrella hygiene, but not for the reason stated.

### The question this displaces — and it is more urgent

If `globs` builds all 1902 modules, then **any broken module makes `lake build` red right now**. This bean's own sample (153 modules, 94.8 % green, 8 failures) implies on the order of tens of genuinely-failing modules across the tree. That is no longer "unchecked code sitting in the dark" — it is a **currently-failing build**, or else those modules were fixed too.

A whole-corpus `scripts/lean-direct-cone.sh --all -k` survey is running to settle it; results to be appended here.

### Correction to my own commit on this branch

Commit `8becb91` ("register the §7c split sibling + QChebyshevFunction") justified adding those imports partly as making the modules "actually get compiled by `lake build QOU`". **That justification was wrong** — `globs` already compiled them. What the commit did correctly was satisfy `lean-orphan-gate` (which exited 1) and make the umbrella explicit; the build-coverage benefit I claimed was not real. The change is still defensible as hygiene, but the stated benefit is retracted here.
