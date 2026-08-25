---
# qou-58rx
title: 'SCOPE: axiom-discharged conjectures — 35 files total, 9+9 done, 17 remain (8 have consumers)'
status: todo
type: task
created_at: 2026-08-08T12:26:23Z
updated_at: 2026-08-08T12:26:23Z
---


## Corrected scope

My first pass (PR #4743) reported "9 files" with the axiom-discharged conjecture
shape. **That was an undercount.** The detection required both an `instance`
keyword and a narrow `:= <axiomname>` match on one line. A looser scan finds the
real total on `main` is **35 files**.

    9   fixed in PR #4743
    9   fixed here (zero downstream consumers — safe)
   ----
   18   fixed
    8   still laundered, but HAVE CONSUMERS — needs a refactor, see below
    8   standalone `axiom`s, NOT class-discharge — need individual judgment
   ----
   35   total

Recording the corrected number because "9 de-laundered" reads as complete and
is not.

## Fixed here (9) — all zero-consumer

AlphaKCategoricalClosure, LocalInfinitesimalField, SpectralNormalForm,
QouInfraDischargesGoncharovZeta5, DiophantineBirthday, SingleVolumeIrrationality,
BorelZagierQouVolumes, **ClassicalRiemannHypothesis**, BringFigureEightDepth2Witness.

`ClassicalRiemannHypothesis` is worth naming explicitly: RH was being asserted by

    axiom classicalRiemannHypothesis_conjecture : ClassicalRiemannHypothesis
    noncomputable instance : ClassicalRiemannHypothesis := classicalRiemannHypothesis_conjecture

`alpha-k-categorical-closure` is the sharpest illustration of the anti-pattern:
its own docstring said downstream theorems "take `[AlphaKCategoricalClosure q]`
as an explicit instance hypothesis" — while a global instance sat directly
below, discharging that hypothesis for free everywhere so it never had to be
written.

## NOT fixed — 8 laundered classes WITH consumers (22 downstream files)

| class | consumers |
|---|---|
| `HabiroResidueSumEquivalence` | 4 |
| `archimedean_agreement` (×2 files) | 4 each |
| `VacuumEpsilon` | 3 |
| `q_oper_hecke` | 2 |
| `q_gl_fiber_functor` | 2 |
| `q_gl_kummer_filtration` | 1 |
| `TorusKnotMass` | 1 |
| `TwoFiltrationBridge` | 1 |

Removing these global instances breaks instance synthesis at every use site.
The correct repair is to thread `[C]` through each consumer as an explicit
hypothesis — which is the *point* of the exercise, but it is a genuine refactor
across 22 files, not a mechanical deletion. Not attempted here rather than
half-done.

## NOT fixed — 8 files with standalone axioms

`n-v-bring-action`, `n-v-leading-order-derivation`, `q-codifferential-formula-prop`
(12 axioms), `spectral-chart-correspondence`, `y-lambda-recipe-from-partition` (4),
`figure-eight-branching-rule` (2), `SDPRankEquality` (4),
`LpDualityHypothesisClass` (2).

These are **not** class-discharge laundering — the axioms are standalone named
inputs, and at least `SDPRankEquality` documents its axioms deliberately as
Mathlib-gap inputs. They may be legitimate or may not; each needs reading. Do
not batch-process them: an earlier loose grep flagged `SDPRankEquality` as
laundered and it is not.
