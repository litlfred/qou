---
# qou-mq3p
title: 'M2 [Mathlib4 Infra]: Compact Riemann Surfaces, Riemann–Roch, Hodge Decomposition & Complex Contour/Hadamard'
status: todo
type: feature
priority: high
tags:
    - lean
    - mathlib-gap
    - riemann-surfaces
    - complex-analysis
created_at: 2026-11-19T08:19:49Z
updated_at: 2026-11-21T07:40:00Z
parent: qou-dxbw
---

## Scope & Audit Metrics (`M2_RIEMANN_SURFACES_HODGE_CONTOUR`)

- **Source Witness:** `computations/audits/lean-axiom-field-and-mathlib-gap-audit.witness.json`
- **Mathlib4 Target Surface:** Compact Riemann surfaces, divisors & linear systems, Riemann–Roch & Serre duality, Hodge decomposition H^{1,0} + H^{0,1}, analytic Gauss–Bonnet 4*pi*(g-1), Weierstrass p-function, windingNumber / Cauchy residue / argument principle, and Hadamard entire-function factorization
- **Cross-Linked Existing Beans:** `qou-bmyx`, `qou-dgtf`, `qou-kp89`, `qou-n4pv`, `qou-nuxb`, `qou-wdgz`, `qou-z4jb`, `qou-c8p8`, `qou-rtxm`
- **Uninstantiated / Toy Carriers:** **16** (`7` uninstantiated `class`es, `9` uninstantiated `structure`s, `0` `TOY_ONLY_INSTANCE`) across `15` `.lean` files
- **Total `Prop` Fields:** `20`  |  **Downstream Theorem/Def Consumers:** `13`
- **Standalone `axiom` / `opaque` Declarations in Cluster:** `2` `axiom`, `5` `opaque`

---

## Concrete Mathlib4 / QOU Build Plan

1. **Winding Number, Argument Principle & Residue Theorem (`QOU/Mathlib/EllipticDivisorDegree.lean`, `ParallelogramContour.lean`):** Build piecewise-$C^1$ contour `windingNumber` and isolated-pole Cauchy residue theorem in Lean 4 to instantiate `HasArgumentPrinciple` and discharge `IsElliptic` divisor-degree zero.
2. **Compact Riemann Surface Divisors, Riemann–Roch & Riemann–Hurwitz:** Define compact 1D complex orbifolds/curves, meromorphic divisors $\mathrm{Div}(X)$, $\ell(D) - \ell(K - D) = \deg D + 1 - g$, and branched-cover Riemann–Hurwitz (`BringsRiemannHurwitzContext`, `SWPeriodResidue`).
3. **Hodge Decomposition $H^{1,0} \oplus H^{0,1}$, Analytic Gauss–Bonnet $4\pi(g-1)$ & Hadamard Factorization:** Instantiate `HodgeInvolution` on harmonic 1-forms, connect curvature integral $\int_\Sigma K\,dA = 2\pi\chi(\Sigma) = 4\pi(1-g)$, and wire Mathlib's Jensen/Nevanlinna API (`qou-bp5n`) toward `HasHadamardFactorization`.

---

## Top Priority Uninstantiated / Toy Carriers (Ranked by Consumer Count)

| Status | Kind | Carrier (`class` / `structure`) | Consumers | Prop Flds | Data Flds | Location (`folio/quantum-observable-universe/...`) |
|---|---|---|---:|---:|---:|---|
| `UNINST` | `structure` | `QOU.Brings.SWPeriodResidue` | 3 | 1 | 4 | `brings-surface/sw-period-residue-sum.lean:61` |
| `UNINST` | `structure` | `QOU.HodgeInvolution` | 2 | 1 | 1 | `lean/QOU/QuantumObservableUniverse/Structures.lean:102` |
| `UNINST` | `structure` | `QOU.HodgeInvolution` | 2 | 1 | 1 | `quantum-universes/categorical-hodge-star.lean:53` |
| `UNINST` | `class` | `QOU.ArchimedeanUniverse.BringsRiemannHurwitzContext` | 1 | 4 | 4 | `lean/QOU/ArchimedeanUniverse/brings_riemann_hurwitz.lean:40` |
| `UNINST` | `class` | `QOU.AlgebraicSubstrate.MacroscopicStabilityEquivalence` | 1 | 2 | 0 | `stochastic-mechanics/macroscopic-stability-equivalence.lean:143` |
| `UNINST` | `class` | `QOU.BraidKnot.AdelicCriticalLinePersistence` | 1 | 1 | 0 | `lean/QOU/BraidKnot/AdelicCriticalLinePersistence.lean:66` |
| `UNINST` | `class` | `QOU.Mathlib.EllipticDivisorDegree.HasArgumentPrinciple` | 1 | 1 | 0 | `lean/QOU/Mathlib/EllipticDivisorDegree.lean:217` |
| `UNINST` | `class` | `QOU.Mathlib.HadamardFactorization.HasHadamardFactorization` | 1 | 1 | 0 | `lean/QOU/Mathlib/HadamardFactorization.lean:321` |
| `UNINST` | `structure` | `QOU.CatHodgeInvolution` | 1 | 1 | 1 | `quantum-universes/categorical-hodge-star.lean:38` |
| `UNINST` | `structure` | `QOU.AlgebraicSubstrate.ClassicalRiemannZeta` | 0 | 2 | 1 | `stochastic-mechanics/classical-riemann-zeta.lean:33` |
| `SHIM_UNIN` | `class` | `QOU.BraidKnot.ClassicalRiemannHypothesis` | 0 | 1 | 0 | `lean/QOU/BraidKnot/ClassicalRiemannHypothesis.lean:36` |
| `UNINST` | `structure` | `QOU.QHarmonicForm` | 0 | 1 | 1 | `lean/QOU/QuantumObservableUniverse/Particles.lean:35` |
| `UNINST` | `structure` | `QOU.Torsion.DimensionOneReduction` | 0 | 1 | 1 | `lean/QOU/Torsion/TopologicalMass.lean:194` |
| `UNINST` | `structure` | `QOU.QHarmonicForm` | 0 | 1 | 1 | `quantum-observable-universes/fermion-boson-decomposition.lean:57` |
| `UNINST` | `structure` | `QOU.QHarmonicForm'` | 0 | 1 | 1 | `quantum-observable-universes/q-harmonic-form.lean:28` |
| `UNINST` | `class` | `QOU.EllipticStabilityLocus.EllipticStabilityLocus` | 0 | 0 | 2 | `predicted-spectra/elliptic-stability-locus.lean:41` |

---

## Standalone `axiom` / `opaque` Declarations in `M2_RIEMANN_SURFACES_HODGE_CONTOUR` (Sample up to 15)

- `opaque QOU.Archimedean.coeffEmbed` (`lean/QOU/Archimedean/WeierstrassProjection.lean:42`)
- `opaque QOU.Archimedean.weierstrassProjection` (`lean/QOU/Archimedean/WeierstrassProjection.lean:49`)
- `opaque QOU.Archimedean.weierstrassProjectionDeriv` (`lean/QOU/Archimedean/WeierstrassProjection.lean:57`)
- `axiom QOU.Archimedean.weierstrass_diff_eq_axiom` (`lean/QOU/Archimedean/WeierstrassProjection.lean:87`)
- `axiom parallelogramIntegral_inv_sub_eq_two_pi_i` (`lean/QOU/Mathlib/ParallelogramContour.lean:173`)
- `opaque QOU.EllipticStabilityLocus.WeierstrassFormHolds` (`predicted-spectra/elliptic-stability-locus.lean:33`)
- `opaque QOU.EllipticStabilityLocus.IntegerPointIdentificationHolds` (`predicted-spectra/elliptic-stability-locus.lean:38`)

## 2026-11-21 — W9: chart step, PR #8750

`QOU/RiemannSurface/ChartStep.lean`, sorry-free: point stabilisers of a finite holomorphic action (holomorphic in a chart at p) are cyclic, granted local effectiveness.

Open: the identity theorem on a connected Riemann surface (GAP `qou-4xht`, for Antigravity).
