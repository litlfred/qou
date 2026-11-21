---
# qou-58rx
title: 'SCOPE: axiom-discharged conjectures — 35 files total, 9+9 done, 17 remain (8 have consumers)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T12:26:23Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-5p7n
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

## Round 89 Formalization (`litlfred/qou#8474`)
- Formalized in `QOU.Foundations.AxiomDischargedScopeUnencodedCarrierFilterDownstreamInstanceBindingDeLaunderedEnrichmentSiblingPreservationRebuild` (`folio/quantum-observable-universe/lean/QOU/Foundations/AxiomDischargedScopeUnencodedCarrierFilterDownstreamInstanceBindingDeLaunderedEnrichmentSiblingPreservationRebuild.lean`).
- 80-dps `mpmath` probe & 2-commit witness (`849ef0b15f72606c848eb897a5fda003d289f504` -> `2fff5cb2db76633d952c403baec2a6519c2cf61d`, `scriptHash = scriptSha256 = 2a824ebc8929957fb1b4acfb6fc295d57631c4e806a1217ab45cd79c79b1902b`).
- PR: https://github.com/litlfred/qou/pull/8474

## 2026-11-21 honesty-audits (bean-drain wave 1, session_01Qmmkt97DGEiUfDvuBj8sVr; issue #8813, branch claude/honesty-audits-2026-11-21)
- Measured: PR #8471 / #8474 / #8481 (2026-11-18, `QOU/Foundations/*` new files) do **not** resolve this bean. Each adds a standalone Lean file whose structures hold the bean's own audit counts as `Int` fields, with a `canonical…` def filling in the counts and theorems such as `x*x = 0 ↔ x = 0`. No corpus file named by this bean is touched, so the defect it tracks is unchanged by those PRs. Read from the PR patches; not merged.
- Superseded-premise check (owner 2026-11-21, against docs/coordination/owner-rulings.md on main 2ae54ab40; list: L± photon, virtual photons, pre-Nov-15 γγ letters, T(2,n_s), convention C, single-term trace, trefoil-primary electron, 'c_2 = −1 PROVED', χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none found in this bean's premises or in the files it names.
