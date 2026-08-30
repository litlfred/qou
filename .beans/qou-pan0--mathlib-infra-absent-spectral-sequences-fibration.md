---
# qou-pan0
title: 'Mathlib infra absent: spectral sequences, fibration LES, octonions and G2'
status: todo
type: task
priority: normal
created_at: 2026-08-24T14:13:56Z
updated_at: 2026-08-24T14:13:56Z
---

Surveyed 2026-08-24 against the pinned Mathlib (Lean 4.24.0) by listing the
olean tree, not by guessing.

## Absent entirely

| wanted | status |
|---|---|
| **Spectral sequences** | **no `SpectralSequence` oleans at all.** Mathlib has `HomologicalComplex`, `ChainComplex`, derived categories — the substrate an algebraic spectral sequence needs — but nobody has built the `E_r`-page abstraction. `QOU/Mathlib/SpectralSequence.lean` (402 lines) is the corpus's own shim, and it is currently vacuous (`qou-fngs`). |
| **Long exact sequence of a fibration** | `Topology/Homotopy/HomotopyGroup` exists with a `Group` instance, so `π_n` is available — but there is **no LES**. `SU(2) → SU(3) → S⁵` cannot be stated as an exact sequence today. |
| **Octonions / Cayley–Dickson / G₂** | absent. `ColourComplexStructure.lean` already records this ("Mathlib has `Quaternion` but no octonions"). |
| **Symplectic topology** | Lagrangians, Dehn twists, Floer cohomology — nowhere near. Seidel's LES (`uploads/0105186v2.pdf`) is decades out. |

## Present and usable

- `Matrix.specialUnitaryGroup` — enough for the concrete `SU(2) ⊄ SU(3)`
  normality witness in `qou-ko4g`, but **not** Lie-group structure theory
  (maximal subgroups, embeddings, root systems).
- `Quaternion` — the `ℍ` rung.
- `ShortComplex.Exact` and the homological-algebra stack — enough for the
  abstract exact-triangle lemma.
- `Equiv.Perm` with centre results — enough for the order-120 trap.

## Nothing is needed from the literature

All of it is textbook: Hatcher §4.2 for the fibration LES, Weibel / McCleary
for spectral sequences, Baez *The Octonions* for `G₂/SU(3) = S⁶` and
`G₂/SO(4)`, Coxeter for the icosians, Wolf for the quaternionic symmetric
spaces. **The gap is formalisation, not knowledge** — which is worth stating
plainly, because "we need a reference" and "we need six months of Lean" are
very different asks and only the second one is true.

## Order of attack, if this is ever funded

1. Algebraic spectral sequences on `HomologicalComplex` — most reusable,
   entirely standard, and the only one the GB-filtration claim actually needs.
2. Fibration LES — needed only if the SU(2)→SU(3)→S⁵ route is pursued, and
   `qou-ko4g` shows the *non-normality* result already blocks the naive lift
   without it.
3. Octonions — large, and `OctonionInvariantObstruction` shows the S₅-equivariant
   route is excluded anyway.
