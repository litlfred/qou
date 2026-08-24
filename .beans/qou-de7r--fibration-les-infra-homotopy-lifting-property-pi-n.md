---
# qou-de7r
title: 'Fibration LES infra: homotopy lifting property + pi_n functoriality + middle exactness'
status: completed
type: task
priority: normal
created_at: 2026-08-24T19:05:22Z
updated_at: 2026-08-24T19:23:56Z
blocking:
    - qou-jbfx
---

Item 2 of qou-pan0. Building the topological side that would feed QOU/Mathlib/LongExactSequence.lean.

Branch: claude/mt7r-archimedean-eval-2026-08-24

Mathlib survey (against the pinned oleans, by enumerating module contents, not guessing):
- HAS: HomotopyGroup / GenLoop / Cube.boundary, ContinuousMap.Homotopy{,With,Rel}, HomotopicRel.comp_continuousMap, Topology.Homotopy.Lifting (covering maps only: IsCoveringMap.liftHomotopy etc).
- ABSENT: any topological fibration predicate. 'Fibration' in the olean tree occurs only in Order/UpperLower/Fibration and the abstract CategoryTheory model-category / simplicial-set files, none of which touch HomotopyGroup.
- ABSENT: any induced map pi_n(X) -> pi_n(Y). GenLoop has no 'map'.

Scope: (1) HasHomotopyLiftingProperty predicate, (2) induced maps, (3) exactness at the middle spot. (4) connecting map delta is out of scope.


## Landed 2026-08-24 (branch claude/mt7r-archimedean-eval-2026-08-24)

Three modules, all green under `scripts/lean-direct-cone.sh
QOU.Mathlib.FibrationExactness` (exit 0, no warnings), every declaration
`#print axioms`-clean (`[propext, Classical.choice, Quot.sound]`, no `sorryAx`),
**zero `sorry` in the source**.

| file | content |
|---|---|
| `QOU/Mathlib/HomotopyLifting.lean` | `HasHomotopyLiftingProperty`, `HasHomotopyLiftingPropertyRel` (stationary rel a subset), `IsHurewiczFibration`, `IsSerreFibration`; `id` has it, fibrations compose, `A = emptyset` collapses Rel to absolute; **a trivial bundle `B x F -> B` satisfies both, for every `Y` and every `A`** |
| `QOU/Mathlib/HomotopyGroupFunctor.lean` | `genLoopMap`, `homotopyGroupMap`, `homotopyGroupHom` (MonoidHom), functoriality, `map_const` |
| `QOU/Mathlib/FibrationExactness.lean` | `Fibre`, `fibreIncl`, **exactness at the MIDDLE spot** (`homotopyGroupMap_eq_const_iff`, `range_homotopyGroupHom_eq_ker`), plus `injective..._of_subsingleton_fibre` and a `Fin (n+1)` spelling |

Registered in `scripts/lean-axiom-guard.py` as `clean` (3 entries) so a
regression is caught.

## What did NOT land, precisely

1. **The connecting map delta and exactness at the other two spots.** Not
   attempted. Constructing delta needs a *choice* of lift plus a second lifting
   argument for well-definedness on classes (lifts of homotopic cubes are
   vertically homotopic), and then the identification of `pi_n(E,F,e)` with
   `pi_n(B,b)` — i.e. relative homotopy groups, which Mathlib also lacks.
2. **`SerreCubePairBridge`** — that the plain HLP against a cube implies the
   stationary-relative HLP against `(I^n, boundary I^n)`. True classically (the
   pair homeomorphism `(I^n x I, I^n x 0 u dI^n x I) = (I^n x I, I^n x 0)`,
   Hatcher §4.2), stated as a named `Prop` in `HomotopyLifting.lean`, **proved
   nowhere and used nowhere**. Deliberately not a `sorry`ed theorem: a `sorry`
   would leak `sorryAx` into the axiom check of everything downstream.

So the exactness theorem takes the *relative* lifting property as its
hypothesis. That hypothesis is discharged for a trivial bundle, so nothing here
is vacuous — but a reader who has a Serre fibration still owes item 2.

## pi_3(SU(2)) = Z is still far

Needs, beyond delta: `SU(2) = S^3` as topological spaces; `pi_n(S^n) = Z`
(Hurewicz or degree theory — Mathlib has neither for `n >= 2`); and Lie-group
topology for the `SU(2) -> SU(3) -> S^5` bundle to even be a fibration. None of
those is in Mathlib and none is touched here.
