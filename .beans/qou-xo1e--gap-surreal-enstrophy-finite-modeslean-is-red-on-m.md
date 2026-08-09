---
# qou-xo1e
title: 'GAP: surreal_enstrophy_finite_modes.lean is red on main — add/neg declared twice in QOU.FluidDynamics'
status: todo
type: task
created_at: 2026-08-09T00:03:26Z
updated_at: 2026-08-09T00:03:26Z
---


## The breakage

`content/quantum-observable-universe/lean/QOU/FluidDynamics/surreal_enstrophy_finite_modes.lean`
does **not compile on `main`** — 15 errors from `lean`-direct, all traceable to
one root cause.

`add` and `neg` are each declared **twice**, both times directly inside
`namespace QOU.FluidDynamics` (opened at line 62, closed at 1158) with **no
nested namespace** to separate them:

| line | declaration | intended subject |
|---|---|---|
| 83  | `theorem neg` | `Infinitesimal` |
| 87  | `theorem add` | `Infinitesimal` |
| 144 | `theorem add` | `IsFinite` |
| 156 | `theorem neg` | `IsFinite` |

So the second pair collides:

```
144:8: error: `QOU.FluidDynamics.add` has already been declared
156:8: error: `QOU.FluidDynamics.neg` has already been declared
```

The remaining 13 errors are the cascade: call sites use dot notation
(`hx.add`, `.mul`, `.pow`) on hypotheses of type `IsFinite x` / `Infinitesimal x`,
which resolves against the *unfolded* `∃ …`, giving
`Exists.add` / `Exists.mul` / `Exists.pow` / `Function.add` — none of which exist.
Two `rcases` failures at 877 and 938 follow from the same unresolved terms.

## Likely fix (unverified — needs someone who knows this file)

Qualify the four theorems into per-predicate namespaces so dot notation
resolves: `Infinitesimal.neg` / `Infinitesimal.add` and `IsFinite.add` /
`IsFinite.neg`, plus whatever `IsFinite.mul` / `IsFinite.pow` the call sites at
628–938 expect. Because `IsFinite` and `Infinitesimal` are plain
`def … : Prop := ∃ …`, dot notation may still unfold to `Exists`; if so the
predicates need to be non-reducible or restructured. **That is a judgment call
about the file's intended API, not a mechanical rename** — hence this bean
rather than a drive-by fix.

## How it was found, and one correction

Surfaced by the `qou-qint` q-integer consolidation sweep (PR #4838): the
migration's auto-revert refused this file. My first reading was that *adding*
`import QOU.MathlibExt.QIntegerCanonical` caused the collision, i.e. that the
canonical module's import cone declared a competing `QOU.FluidDynamics.add`.

**That was wrong.** Verifying the **pristine** file — no import, no edit — gives
the identical 15 errors, one line earlier. The import had only shifted line
numbers. The file was already broken and the canonical module is innocent.
Recorded because the misreading was one step from a false bug report against
QIntegerCanonical.

## Blocks

The `qInt` at line 192 (`∑ j ∈ range k, q ^ j`, an exact `qIntGeo` duplicate)
cannot be consolidated until the file compiles. It is the only site in its
batch left unmigrated.

## Related

Fourth red-or-unchecked file surfaced by this line of work:

- `QOU/Archimedean/QMomentum.lean` — `writhe` outside its namespace; **fixed** in #4791.
- `braids-and-knots/chi-std-pernucleon-closed-form.lean` — red on main, still open.
- `qou-orph` / `qou-k448` — the orphan-module class.
- `qou-87ms` — why the preflight does not catch these (working-tree-only scope).
