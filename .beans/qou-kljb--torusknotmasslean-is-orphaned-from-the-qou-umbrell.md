---
# qou-kljb
title: 785 of 1659 QOU library modules are never built — lake build QOU cannot see them
status: todo
type: task
priority: high
created_at: 2026-08-09T02:12:05Z
updated_at: 2026-08-09T10:40:00Z
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
| library modules under `lean/QOU/` | 1659 |
| reachable from `QOU.lean` | 874 |
| **unreachable** | **785 (47%)** |

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

So `lake build QOU` never elaborates the 785. A module in that set can be
syntactically broken, carry an uncited `sorry`, or fail to typecheck, and no
build will say so.

### Correction — how this bean first read, and why

The first version of this bean **denied** the orphan/CI claim. The reasoning
was: against the restored `lake-cache/qou-v4-24-0` tree, orphaned modules carry
`.olean` artifacts at 56% (440/785), statistically indistinguishable from
reachable modules at 57% (502/874), and `TorusKnotMass.olean` is present — so
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

For these 785 modules there is currently **no** automated check of any kind:

- `lake build QOU` does not build them (above);
- a library `.lean` with no `.ts`/`.md` sibling has no `.qa.json` sidecar and
  is not covered by `lean-content-siblings.yml` (AGENTS.md);
- CI auto-triggers are disabled repo-wide (`build.yml` is
  `workflow_dispatch`-only).

## Next steps (needs owner scoping — NOT an idle-drain)

1. Triage the 785: genuinely dead, or merely unwired? Sample ~20 first.
2. For the "should be built" set, either add
   `globs = ["QOU", "QOU.+"]` to the lakefile or add the missing imports to
   `QOU.lean`. **Expect breakage** — some have plausibly been red for months.
   That is the point, but it makes this a scoped tranche.
3. Delete genuinely dead modules rather than leaving them to rot.
4. Add a cheap guard so a new orphan is visible at authoring time.

Do **not** flip the glob on without step 1 — turning on 785 unbuilt modules at
once could be very red, and would land that breakage on whoever is next to
touch the file.
