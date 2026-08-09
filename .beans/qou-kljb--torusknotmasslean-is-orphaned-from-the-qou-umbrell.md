---
# qou-kljb
title: 795 QOU library modules are never built — lake build QOU cannot see them (270 load-bearing)
status: todo
type: task
priority: high
created_at: 2026-08-09T02:12:05Z
updated_at: 2026-08-09T19:20:00Z
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
