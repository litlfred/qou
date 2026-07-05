# Mathlib import remap map (post-f897ebcf renames/splits)

Pinned Mathlib: `f897ebcf72cd16f89ab4577d0c826cd14afaafc7` (Lean `v4.24.0`).

Content-block `.lean` siblings (in chapter directories, not the `lean/`
library tree) carried `import Mathlib.X` lines pointing at modules that were
renamed / split / removed in the pinned Mathlib. This map records the
old → new remap applied. Only `import` lines were touched; no declarations,
tactics, or proof bodies were changed.

## Method

1. Extracted every `^import Mathlib…` line from all 1887 content `.lean`
   files (`find content -name '*.lean'`).
2. Cross-checked each distinct module against the pinned Mathlib master
   module list (`Mathlib.lean` @ f897ebcf, 6998 modules).
3. Modules absent from the pinned list are stale → remapped to the
   documented successor (verified present in the pinned list).

Note: `import Mathlib` (the umbrella) is valid and is **not** stale — it is
the package root, absent only from the *contents* of `Mathlib.lean`.

## Verification

- **Module resolution: machine-verified.** A probe file importing all 18
  distinct replacement modules compiles clean (`lean` v4.24.0, exit 0)
  against the restored pinned-Mathlib oleans
  (`lake-cache/qou-v4-24-0`, 2962 oleans) with
  `LEAN_PATH` set to the package `.lake/build/lib/lean` dirs.
- **Post-apply re-sweep: 0 stale** content-block imports remain.
- **Declaration-level / full proof checking is out of scope here.** Many of
  these siblings carry pre-existing breakage (parse / unknown-tactic /
  proof-goal errors) that the dead import previously masked; that breakage
  is a separate deep-drain backlog (bean `szkf`) and is *not* introduced by
  this remap. Per-file `lean`-direct results are recorded in the PR.

## Old → new module map

| Stale module (absent @ f897ebcf) | Replacement (present @ f897ebcf) | Kind |
|---|---|---|
| `Mathlib.Algebra.BigOperators.Group.Finset` | `Mathlib.Algebra.BigOperators.Group.Finset.Basic` | split → `.Basic` entry |
| `Mathlib.Algebra.Group.Units` | `Mathlib.Algebra.Group.Units.Basic` | split → `.Basic` |
| `Mathlib.Algebra.GroupPower.Basic` | `Mathlib.Algebra.Group.Basic` | deleted; power lemmas folded into `Group.Basic` + core |
| `Mathlib.Algebra.GroupPower.Order` | `Mathlib.Algebra.Order.Monoid.Unbundled.Pow` | deleted; ordered-power lemmas |
| `Mathlib.Algebra.Homology.Complex` | `Mathlib.Algebra.Homology.HomologicalComplex` | rename |
| `Mathlib.Algebra.Order.Ring.Lemmas` | `Mathlib.Algebra.Order.Ring.Basic` | split; `.Lemmas` removed |
| `Mathlib.Algebra.Polynomial.EuclideanDomain` | `Mathlib.Algebra.Polynomial.FieldDivision` | moved; carries the polynomial `EuclideanDomain` instance |
| `Mathlib.Data.Int.Defs` | `Mathlib.Data.Int.Init` | rename |
| `Mathlib.Data.Nat.Defs` | `Mathlib.Data.Nat.Basic` | split; `.Basic` re-exports basic defs |
| `Mathlib.Data.Nat.Parity` | `Mathlib.Algebra.Ring.Parity` | moved; parity now under `Algebra.Ring` |
| `Mathlib.Data.Polynomial.Basic` | `Mathlib.Algebra.Polynomial.Basic` | rename (`Data.Polynomial` → `Algebra.Polynomial`) |
| `Mathlib.Data.Rat.Basic` | `Mathlib.Data.Rat.Defs` | split; `.Defs` is the broad successor |
| `Mathlib.Geometry.Manifold.SmoothManifoldWithCorners` | `Mathlib.Geometry.Manifold.IsManifold.Basic` | rename |
| `Mathlib.LinearAlgebra.Basic` | `Mathlib.LinearAlgebra.Span.Basic` | deleted/split; span + linear-map basics |
| `Mathlib.LinearAlgebra.LinearIndependent` | `Mathlib.LinearAlgebra.LinearIndependent.Basic` | split → `.Basic` |
| `Mathlib.LinearAlgebra.Span` | `Mathlib.LinearAlgebra.Span.Basic` | split → `.Basic` |
| `Mathlib.Order.Defs` | `Mathlib.Order.Basic` | split into `Order.Defs.{LinearOrder,PartialOrder,Unbundled}`; `Order.Basic` re-exports |
| `Mathlib.Tactic.Omega` | `Mathlib.Tactic` | `Omega` module removed (omega is core); umbrella keeps it available |
| `Mathlib.Topology.ContinuousFunction.Basic` | `Mathlib.Topology.ContinuousMap.Basic` | rename (`ContinuousFunction` → `ContinuousMap`) |

19 stale modules → 18 distinct replacements
(`LinearAlgebra.Basic` and `LinearAlgebra.Span` both → `LinearAlgebra.Span.Basic`).

## Notes on split/deleted choices (module resolves; declaration-level not exhaustively verified)

For modules that were *split* or *deleted* (not a clean 1:1 rename), the
replacement targets the broadest documented successor that re-exports the
prior content:

- `GroupPower.Basic → Group.Basic`, `GroupPower.Order → Order.Monoid.Unbundled.Pow`:
  `GroupPower.*` was dissolved; monoid/group power lemmas moved into
  `Algebra.Group.Basic` and the unbundled ordered-monoid `Pow` module.
- `LinearAlgebra.Basic → LinearAlgebra.Span.Basic`: the deprecated `Basic`
  aggregate's submodule/linear-map core lives under `Span.Basic`.
- `Order.Defs → Order.Basic`: `Order.Basic` imports the three `Order.Defs.*`
  split modules.
- `Data.Nat.Defs → Data.Nat.Basic`, `Data.Rat.Basic → Data.Rat.Defs`:
  broad re-exporting successors.

If a downstream `lean`-direct run reveals a specific declaration missing
after the remap (as opposed to the pre-existing proof breakage tracked in
`szkf`), narrow the import to the exact successor module for that decl.

## Affected files by chapter (bean grouping)

- **29r5** — models-of-qous, lifting-and-descent, braids-and-knots
- **avwi** — mass-theory, mass-endomorphism
- **c0ql** — quantum-universes, particle-interactions
- **k7ki** — quantum-observable-universes
- **vj6u** — observations, information-theory, predicted-spectra, unital-groebner-bases (UGB)
