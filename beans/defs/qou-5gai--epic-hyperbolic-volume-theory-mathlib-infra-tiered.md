---
# qou-5gai
title: Hyperbolic-volume theory Mathlib infra (tiered H1-H5) — the T2 blocker
status: in-progress
type: feature
priority: medium
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T17:05:00Z
updated_at: 2026-11-17T10:08:09Z
parent: qou-c8p8
---

The single blocker behind `qou-idvt` **T2**, `qou-7y3g`, and `qou-krvm` **(iv)**.
All three are stuck on the same thing: **Mathlib has no hyperbolic geometry at
all**, so "the hyperbolic volume of an ideal tetrahedron" cannot even be
*stated*, let alone proved.

## The gap, measured (2026-08-08) — not assumed

Enumerated over the restored Mathlib olean tree (`lake-cache/qou-v4-24-0`),
**6990 modules**:

| probe | hits |
|---|---|
| modules matching `*hyperbol*` | **0** |
| modules matching `*clausen*` / `*lobachev*` | **0** |
| declarations containing `Hyperbolic` / `Lobachevsky` / `Clausen` | **0** |
| `UpperHalfPlane` | present, but **`Analysis/Complex/UpperHalfPlane` only** |

The one hit is the **2-dimensional modular-forms** upper half plane: a complex
domain with an `SL₂` action, carrying **no Riemannian metric, no volume form,
no geodesics**. It is not a hyperbolic-geometry library and does not generalise
to `H³`. So the gap is total, not partial.

## Why this is infra-scale

`qou-7y3g` already recorded the verdict and it is correct: *"Mathlib has no
hyperbolic-volume theory for ideal tetrahedra — no Lobachevsky function, no
ideal-simplex volume, no Mostow rigidity. Proving this in Lean means building
that infrastructure first. This is infra-scale, not a session-scale task."*

What has changed since that was written: the **analytic** half is now done
(see "What is already built" below), so the remaining work is exactly the
**geometric measure theory**, and it can be tiered.

## ⚠ REPRESENTATION DECISION (2026-08-08) — H1 picked the wrong one

**H1 was written on `ℝ × ℝ × ℝ`. That choice makes H2 structurally impossible
and should be migrated to `Fin 3 → ℝ` before more is built on it.** Measured,
not guessed — each row is an `infer_instance` / `#check` run against the
restored cache:

| representation | Haar / scaling (H2) | Fubini (H4-2) |
|---|---|---|
| `ℝ × ℝ × ℝ` — **H1's current choice** | ❌ `volume.IsAddHaarMeasure` **fails to synthesize**; so does `IsAddRightInvariant`. `Mathlib.MeasureTheory.Measure.Haar.Prod` **does not exist** | ✅ `lintegral_prod` applies directly |
| `Fin 3 → ℝ` / `EuclideanSpace ℝ (Fin 3)` | ✅ `IsAddHaarMeasure`, `IsAddRightInvariant`, `finrank = 3`, `Measure.addHaar_smul` all available | ✅ via `measurePreserving_piFinSuccAbove`, which splits one coordinate off measure-preservingly into `ℝ × (Fin 2 → ℝ)` |

So the Pi representation has **both**; Prod has only Fubini. I chose Prod in H1
optimizing for the Fubini step without checking the Haar side — H2's dilation
invariance (`Lebesgue's λ³` vs `the density's 1/λ³`) needs `addHaar_smul`, which
Prod cannot supply.

**Recommendation: migrate H1 to `Fin 3 → ℝ`** (mechanically `p.2.2 ↦ p 2`)
before H2 or H4-2 is attempted. Until that happens, treat H1 as a correct object
on an inconvenient carrier: everything proved in it stands, but it is a dead end
for the rest of the series. The H1 file header carries the same warning.

## Tiers

**H1 — the hyperbolic volume measure on `H³`.** Define upper half-space and
`μ_hyp = volume.withDensity (z ↦ 1/z³)`. Pure Mathlib measure theory
(`Measure.withDensity` exists); no geometry needed. **The right starting point.**

**H2 — the invariances that make it the hyperbolic measure.**
  * horizontal translation `(x,y,z) ↦ (x+a, y+b, z)` — Lebesgue is translation
    invariant and the density does not see `x,y`;
  * dilation `(x,y,z) ↦ (λx, λy, λz)`, `λ > 0` — Lebesgue scales by `λ³`, the
    density `1/z³` by `1/λ³`, and **they cancel**. This is the substantive one
    and is the reason the metric is `dx²+dy²+dz²)/z²`.
  Both are provable from Mathlib's Haar/`Measure.map` API. **No `sorry`, no
  axiom** — if a piece resists, bean it, do not assume it.

**H3 — the ideal tetrahedron as a region.** The solid over a Euclidean triangle
cut by the three hemispheres on its edges; the dihedral angles `(α,β,γ)` of the
ideal vertices. Definitional but fiddly; the place to be careful that the
*definition* is right rather than convenient.

**H4 — `Vol(α,β,γ) = Λ(α)+Λ(β)+Λ(γ)` (Milnor).** THE hard tier and the actual
`qou-idvt` T2. Integrate `μ_hyp` over the H3 region and land on the Λ-sum. Needs
H1-H3 plus a real Fubini/substitution argument.

**H5 — consumers.** Only after H4: `Vol(4₁) = 2·V_tet` (`qou-7y3g`), and the
volume functional's concavity **on the polytope** (`qou-krvm` (iv)) rather than
on the single simplex.

## What is already built (do not redo — corpus-grep first)

The **analytic** side is complete and sorry-free, so H4 has its target in hand:

| result | where |
|---|---|
| `Λ(t) = Cl₂(2t)/2`, `Λ_neg/zero/pi_div_two/pi` | `BlochWignerLobachevsky.lean` |
| `Λ' = -log(2 sin t)`, `Λ'' = -cot` (T1) | `LobachevskyDerivative.lean`, PR #4744 |
| pointwise Hessian negative definite | `IdealTetrahedronConcavity.lean` |
| **T3** `StrictConcaveOn ℝ angleSimplex volChart` | `IdealTetrahedronVolumeConcavity.lean`, PR #4773 |
| **T4** regular triple is the unique maximiser; max value `= Cl₂(π/3)` | `LobachevskyMaximum.lean`, PR #4773 |
| `continuous_Lob`, `Lob_pi_sub` | same, PR #4773 |
| `Cl₂` continuity / duplication / `Cl₂(2π-θ) = -Cl₂θ` / `Cl₂(π/3) > 0` | `Knot/Clausen.lean` |

So H4's statement is `hypVolume (idealTet α β γ) = Lob α + Lob β + Lob γ`, with
the right-hand side already a fully developed object.

## GUARD (inherited from qou-7y3g, and it is the point)

**Do NOT axiomatise the volume identity as a Lean class and consume it
downstream.** That is the laundering AGENTS.md forbids. Until H4 is proved:

* `volChart` stays **defined** as the Λ-sum, and every statement about it is
  labelled analytic, not geometric (both PR #4773 headers do this);
* `Vol(4₁) = 2·V_tet` stays **numerical, labelled numerical** (`qou-7y3g`);
* no `sorry`-ed instance, no conditional class standing in for H4.

A tier that cannot be closed gets a bean, not a `sorry`.

## Links

* `qou-idvt` T2 — the same gap, named from the ideal-tetrahedron side
* `qou-7y3g` — `Vol(4₁)=2V_tet`, `Vol(B₃)=2V_oct`, blocked on H4/H5
* `qou-krvm` (iv) — the volume functional on the m004/L6a4 polytopes, blocked on H5
* `08a2` — the keystone de-abstraction EPIC this belongs under



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.



Former title (before 2026-10-04, when this became a story under a programme epic): EPIC: hyperbolic-volume theory Mathlib infra (tiered H1-H5) — the T2 blocker

### Progress Update (2026-11-17, Round 59 — lane-e667)
- **PR:** `litlfred/qou#8291` (`https://github.com/litlfred/qou/pull/8291`), head `97f9ffaed50b1b3971470d9bc651293cd4f935e3` (`COMMIT1 = 9f95671d31537da41246588ea9801b300607f995`), labeled `ready-to-merge` + `release`, `ready: 97f9ffaed50b1b3971470d9bc651293cd4f935e3` (`https://github.com/litlfred/qou/pull/8291#issuecomment-6944908884`).
- **Lean 4.24.0 Module:** `folio/quantum-observable-universe/lean/QOU/Foundations/HyperbolicScalingDescartesCubicFarkasDuality.lean` (wired into `QOU.lean`; `0` `sorry`, `0` `axiom`, `0` warnings, `0` CRITICAL/major/advisory across all 6 static vacuity & borrowed-name audits):
  - `qou-322e`: `chordal_step_symmetry_diagonal_and_concatenation` over `CommRingCarrier R`.
  - `qou-4tsl`: `alternating_two_wedge_antisym_and_three_wedge_vanishing` and `alternating_two_wedge_ring_antisym_and_diag` over `Int` and `CommRingCarrier R`.
  - `qou-5gai`: `dilation_cube_jacobian_density_cancellation` over `CommRingCarrier R`.
  - `qou-7y3g`: `classical_av4_cubic_factorization_and_complex_roots` over `Int`.
  - `qou-9h4t`: `primal_dual_slack_gap_and_complementary_slackness` over `Int`.
- **80-dps Probe & 2-Commit Witness:** `computations/probes/hyperbolic_scaling_descartes_cubic_farkas_duality_probe.py` + `computations/probes/hyperbolic-scaling-descartes-cubic-farkas-duality.witness.json` (`scriptHash = 9b07010b5e8c`, `scriptCommitSha = 9f95671d31537da41246588ea9801b300607f995`, `allPassed = True`).
- **Adversarial Cross-Review (Round 59):** Verified `litlfred/qou#8276` (`1909a7bd3bec6ebbdc594cc42f836c8a59fb6451`, `0` advisories) and remediated `3 major, 2 advisory` borrowed-name findings on sibling PR `litlfred/qou#8261`, pushing `77aeb5c622eb2876245d1628c2f107b5f85999f8` and posting `ready: 77aeb5c622eb2876245d1628c2f107b5f85999f8` (`https://github.com/litlfred/qou/pull/8261#issuecomment-6942739479`).
- **Status:** Kept at `in-progress` pending Merge Manager verification and merge.
