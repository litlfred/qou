---
# qou-ct0m
title: 'M3 [Mathlib4 Infra]: Hyperbolic 2D/3D Geometry, Triangle Groups Δ(p,q,r), Mostow Rigidity & Ohtsuki Asymptotics'
status: todo
type: feature
priority: high
tags:
    - lean
    - mathlib-gap
    - hyperbolic-geometry
    - 3-manifolds
created_at: 2026-11-19T08:19:50Z
updated_at: 2026-11-19T08:19:50Z
parent: qou-dxbw
---

## Scope & Audit Metrics (`M3_HYPERBOLIC_UNIFORMIZATION_3MANIFOLDS`)

- **Source Witness:** `computations/audits/lean-axiom-field-and-mathlib-gap-audit.witness.json`
- **Mathlib4 Target Surface:** Hyperbolic 2D/3D manifolds, Fuchsian/Kleinian triangle groups Delta(p,q,r) & Poincare uniformization, Thurston hyperbolization & Mostow rigidity, Casson–Rivin constrained angle-structure concavity, SL(2,C) Chern–Simons invariant, and Ohtsuki stationary-phase / steepest-descent saddle-point asymptotics
- **Cross-Linked Existing Beans:** `qou-5gai`, `qou-322e`, `qou-h2mb`, `qou-i0sr`, `qou-m8xt`, `qou-sd8y`, `qou-6x4m`, `qou-c8p8`, `qou-rtxm`
- **Uninstantiated / Toy Carriers:** **60** (`41` uninstantiated `class`es, `16` uninstantiated `structure`s, `3` `TOY_ONLY_INSTANCE`) across `53` `.lean` files
- **Total `Prop` Fields:** `119`  |  **Downstream Theorem/Def Consumers:** `116`
- **Standalone `axiom` / `opaque` Declarations in Cluster:** `0` `axiom`, `1` `opaque`

---

## Concrete Mathlib4 / QOU Build Plan

1. **Hyperbolic 2D/3D Metric & Fuchsian Triangle Groups $\Delta(p,q,r)$:** Re-base `QOU/Archimedean/HyperbolicMetric.lean` on Mathlib's `UpperHalfPlane` Riemannian metric (`qou-sd8y`, `qou-m8xt`) and construct concrete Fuchsian $\Delta(2,3,5) / \Delta(2,4,5)$ fundamental domains & Poincaré uniformization.
2. **Casson–Rivin Constrained Angle-Structure Concavity & Gluing Completeness:** Prove strict concavity of $\sum \Lambda(\theta_i)$ on the affine gluing subspace (`AngleStructure`, `mlgp` Gap 3) and bridge `IdealTriangulation` to cusped 3-manifold volume invariance (`HyperbolicVolumeBridge`, Thurston/Mostow interface).
3. **1D/3D Saddle-Point / Stationary-Phase Estimates for Ohtsuki & Kashaev:** Formalize quantitative Euler–Maclaurin with constant term + quadratic saddle-point bounds to instantiate `OhtsukiAsymptotic` (`FiveTwoOhtsukiBridge.lean`) and `VolumeConjecture` on concrete knots.

---

## Top Priority Uninstantiated / Toy Carriers (Ranked by Consumer Count)

| Status | Kind | Carrier (`class` / `structure`) | Consumers | Prop Flds | Data Flds | Location (`folio/quantum-observable-universe/...`) |
|---|---|---|---:|---:|---:|---|
| `UNINST` | `class` | `QOU.MathlibExt.HyperbolicVolumeBridge` | 15 | 3 | 1 | `lean/QOU/MathlibExt/ManifoldVolumeBridge.lean:174` |
| `UNINST` | `structure` | `QOU.Archimedean.TorusKnot` | 7 | 3 | 2 | `lean/QOU/Archimedean/TorusKnotGenusFourUnique.lean:23` |
| `UNINST` | `class` | `QOU.Archimedean.FiveTwoOhtsukiBridge.OhtsukiAsymptotic` | 6 | 2 | 1 | `lean/QOU/Archimedean/FiveTwoOhtsukiBridge.lean:901` |
| `UNINST` | `class` | `QOU.Archimedean.IntegerStabilityContext` | 5 | 4 | 5 | `lean/QOU/Archimedean/integer_stability.lean:33` |
| `UNINST` | `class` | `QOU.Kashaev.VolumeConjecture` | 5 | 3 | 3 | `lean/QOU/Kashaev.lean:57` |
| `UNINST` | `structure` | `QOU.Optimization.AngleStructure` | 4 | 4 | 0 | `lean/QOU/Optimization/AngleStructureFeasibility.lean:83` |
| `UNINST` | `structure` | `QOU.Archimedean.IsHypMinimizer` | 4 | 2 | 1 | `lean/QOU/Archimedean/HyperbolicGeodesic.lean:87` |
| `UNINST` | `class` | `QOU.Kashaev.VolumeConjecture` | 4 | 2 | 2 | `mass-theory/kashaev-volume-conjecture.lean:51` |
| `UNINST` | `structure` | `QOU.BraidKnot.KnotAssignment` | 4 | 1 | 2 | `lean/QOU/BraidKnot/ZeqNRhoCorrection.lean:44` |
| `UNINST` | `class` | `QOU.BraidsKnots.AtomicJSJDecomposition` | 4 | 1 | 0 | `lean/QOU/BraidsKnots/LinearJSJVolume.lean:71` |
| `UNINST` | `structure` | `QOU.Archimedean.TypedGarsideElement` | 3 | 5 | 4 | `lean/QOU/Archimedean/TypedGarsideElement.lean:32` |
| `UNINST` | `structure` | `QOU.Archimedean.QMomentum` | 3 | 2 | 2 | `lean/QOU/Archimedean/QMomentum.lean:46` |
| `UNINST` | `class` | `QOU.Archimedean.PeriodMapWeightReduction.PeriodMapWeight` | 3 | 1 | 0 | `lean/QOU/Archimedean/PeriodMapWeightReduction.lean:85` |
| `UNINST` | `class` | `QOU.Knot.FigureEightVolume.VdVWhiteheadLemma4` | 3 | 1 | 0 | `lean/QOU/Knot/WhiteheadLinkScaffold.lean:135` |
| `UNINST` | `structure` | `QOU.Archimedean.BreitWheelerPairProduction` | 2 | 4 | 4 | `lean/QOU/Archimedean/BreitWheelerPairProduction.lean:24` |
| `UNINST` | `class` | `QOU.Archimedean.BorelProperTimeMoment.BindingKernelSchwingerRepresentation` | 2 | 3 | 0 | `lean/QOU/Archimedean/BorelProperTimeMoment.lean:217` |
| `SHIM_UNIN` | `structure` | `QOU.Archimedean.VolumeTowerDecomposition` | 2 | 3 | 4 | `lean/QOU/Archimedean/HyperbolicVolumeTranscendence.lean:300` |
| `UNINST` | `structure` | `QOU.Archimedean.SpectralRing` | 2 | 2 | 3 | `lean/QOU/Archimedean/EmSpectralCompleteness.lean:37` |
| `UNINST` | `structure` | `QOU.Archimedean.CSEvaluationFaithful` | 2 | 2 | 2 | `lean/QOU/Archimedean/HyperbolicVolumeTranscendence.lean:401` |
| `UNINST` | `structure` | `QOU.Archimedean.TauS5EquivarianceReduction.GeneratorIntertwiner` | 2 | 2 | 1 | `lean/QOU/Archimedean/TauS5EquivarianceReduction.lean:91` |

---

## Standalone `axiom` / `opaque` Declarations in `M3_HYPERBOLIC_UNIFORMIZATION_3MANIFOLDS` (Sample up to 15)

- `opaque QOU.AlgebraicSubstrate.GBDepthPeriodCorrespondence.Hyperbolic3Manifold` (`mass-theory/gb-depth-period-correspondence.lean:130`)
