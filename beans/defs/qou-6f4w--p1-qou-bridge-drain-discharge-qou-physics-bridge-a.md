---
# qou-6f4w
title: 'P1 [QOU Bridge Drain]: Discharge QOU Physics-Bridge Axiom-Field Classes, Shim Guards & Toy Instances'
status: todo
type: feature
priority: high
tags:
    - lean
    - qou-bridge-gap
    - axiom-field-audit
    - de-vacuification
created_at: 2026-11-19T08:19:51Z
updated_at: 2026-11-19T08:19:51Z
parent: qou-dxbw
---

## Scope & Audit Metrics (`QOU_BRIDGE_OR_PHYSICS_GAP`)

- **Source Witness:** `computations/audits/lean-axiom-field-and-mathlib-gap-audit.witness.json`
- **Cross-Linked Existing Epics:** `qou-6qbv` (*De-vacuify Lean :True carriers*), `qou-c8p8` (*close class field debt*), `08a2` (*keystone de-abstraction*), `qou-rtxm`
- **Uninstantiated / Toy Carriers:** **866** (`457` uninstantiated `class`es, `396` uninstantiated `structure`s, `13` `TOY_ONLY_INSTANCE`) across `647` `.lean` files
- **Total `Prop` Fields:** `1766`  |  **Downstream Theorem/Def Consumers:** `1394`
- **Standalone Physics/Bridge `axiom` / `opaque` Declarations:** `41` `axiom`, `53` `opaque`

---

## Concrete Discharge & Honesty Triage Plan

1. **Discharge Provable Algebraic / Rational-Certificate Bridges Now:**
   - Replace uninstantiated confinement LP/SDP premise carriers (`ConfinementSDPData`, `OperatorSelectionLP`, `ConfinementGradingCorrespondence`) on concrete nuclei/hadrons using the full-rank GPMT Gram completion + Two-Term Photon QED closed-form certificates (`QOU/Interactions/TwoTermPhotonGPMTConfinementSDP.lean`).
   - Instantiate `BringsEulerCharacteristicContext` (`euler_eq : eulerChar = -6` in `lean/QOU/ArchimedeanUniverse/brings_euler_characteristic.lean:103`) from explicit genus-4 Riemann–Hurwitz / cellular Euler count $2 - 2g = -6$ once `M2` lands.
   - Replace skeleton/toy instances (`TowerSummandRealization` in `lean/QOU/PhiQJSJ.lean:55`, `ClassicalLimitStpart`, `CemeteryGroupEmergence`, `ShellClosureNFTermCount`, `TensorGenerationFree`) with genuine non-zero algebraic realizations.
2. **Eliminate Unpinned `: Prop` & Free-Data Premise Laundering:**
   - Audit and repair the `34` carriers with unpinned `: Prop` fields and `43` shim-guarded carriers so every conditional theorem states its exact mathematical hypothesis rather than a free proposition variable.
3. **Explicitly Label Genuinely Open Conjectures (`§3b-cond`):**
   - For irreducible open physical conjectures (`WittenKappaGramDeterminant`, `BringZeroModeBlochClass`, `HorizonStructure` / `PNeqNP`, `BigBangHeatDeath`), keep explicit `Conjecture` naming and block-manifest `conditional` status rather than fabricating toy instances.

---

## Named Flagship Physics-Bridge Carriers

| Status | Kind | Carrier (`class` / `structure`) | Consumers | Prop Flds | Data Flds | Location (`folio/quantum-observable-universe/...`) |
|---|---|---|---:|---:|---:|---|
| `SHIM_UNIN` | `class` | `QOU.Archimedean.BringZeroModeBlochClass` | 1 | 1 | 0 | `lean/QOU/Archimedean/EmCouplingBringZeroMode.lean:306` |
| `UNINST` | `class` | `QOU.ArchimedeanUniverse.BringsEulerCharacteristicContext` | 5 | 1 | 2 | `lean/QOU/ArchimedeanUniverse/brings_euler_characteristic.lean:103` |
| `UNINST` | `class` | `QOU.ParticleInteractions.ConfinementSDPData` | 2 | 3 | 4 | `mass-theory/confinement-sdp.lean:17` |
| `TOY_ONLY` | `class` | `QOU.BraidKnot.ConfinementGradingCorrespondence` | 2 | 1 | 2 | `lean/QOU/BraidKnot/ConfinementGradingCorrespondence.lean:34` |
| `TOY_ONLY` | `class` | `QOU.PhiQJSJ.TowerSummandRealization` | 2 | 1 | 1 | `lean/QOU/PhiQJSJ.lean:55` |
| `SHIM_UNIN` | `structure` | `QOU.ComputationalHorizon.HorizonStructure` | 0 | 0 | 1 | `information-theory/computational-horizon.lean:243` |
| `UNINST` | `class` | `QOU.Information.QouPNeqNp` | 2 | 1 | 0 | `lean/QOU/Information/QouPNeqNp.lean:89` |

---

## Top 20 High-Consumer QOU Physics-Bridge Axiom Carriers

| Status | Kind | Carrier (`class` / `structure`) | Consumers | Prop Flds | Data Flds | Location (`folio/quantum-observable-universe/...`) |
|---|---|---|---:|---:|---:|---|
| `UNINST` | `structure` | `QOU.CategoricalQExtDeriv` | 20 | 2 | 5 | `lean/QOU/QuantumObservableUniverse/Instanton.lean:28` |
| `UNINST` | `structure` | `QOU.QuantumUniverse` | 16 | 7 | 9 | `lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean:210` |
| `UNINST` | `structure` | `QOU.CategoricalLagrangian` | 16 | 1 | 4 | `lean/QOU/QuantumObservableUniverses/QDifferentialGeometry.lean:69` |
| `UNINST` | `structure` | `QOU.AntipodeIndependence.FrobeniusHopfDataPreAxiom` | 15 | 3 | 8 | `lean/QOU/QuantumObservableUniverse/AntipodeIndependence.lean:53` |
| `UNINST` | `structure` | `QOU.Archimedean.GramMatrix` | 14 | 1 | 1 | `nuclear-interactions/gram-weighted-qvalue.lean:20` |
| `UNINST` | `structure` | `QOU.ComputationalHorizon.ResolutionTree` | 13 | 3 | 2 | `information-theory/computational-horizon.lean:63` |
| `UNINST` | `structure` | `QOU.BundleInitialConditions` | 13 | 1 | 1 | `measurement-observation/bundle-initial-conditions.lean:62` |
| `UNINST` | `structure` | `QOU.QuantumObservableUniverse` | 12 | 5 | 6 | `lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean:405` |
| `UNINST` | `structure` | `QOU.RecursiveBraneTower` | 12 | 5 | 1 | `lifting-and-descent/recursive-brane-tower.lean:27` |
| `UNINST` | `structure` | `QOU.Braiding.SpectralIdempotentData` | 12 | 2 | 1 | `mass-theory/hecke-markov-transition.lean:47` |
| `UNINST` | `class` | `QOU.AlgebraicSubstrate.QouObstructionReductionContext` | 11 | 7 | 6 | `lean/QOU/AlgebraicSubstrate/qou_obstruction_reduction.lean:52` |
| `UNINST` | `structure` | `QOU.BraidKnot.SpinInvolution` | 11 | 6 | 1 | `knots-particles-confinement/spin-involution.lean:33` |
| `UNINST` | `structure` | `QOU.BraidKnot.SpinInvolution` | 10 | 6 | 2 | `mass-theory/spin-involution-lp-dual-invariance.lean:70` |
| `UNINST` | `class` | `QOU.QBeta.StateIntegral.Recursion` | 10 | 5 | 0 | `lean/QOU/QBeta/StateIntegralRecursionLattice.lean:86` |
| `UNINST` | `structure` | `QOU.Archimedean.BetaDecayData` | 10 | 5 | 5 | `predicted-spectra/hadron-half-life.lean:50` |
| `UNINST` | `structure` | `QOU.Brings.ColorTubeCoordinates` | 10 | 4 | 9 | `brings-surface/color-tube-coordinates.lean:26` |
| `UNINST` | `structure` | `QOU.Torsion.ArchimedeanMassFormula` | 10 | 4 | 2 | `lean/QOU/ArchimedeanMassFormula.lean:56` |
| `UNINST` | `class` | `QOU.StandardModel.ThetaQCDFraming.BarInvolution` | 10 | 4 | 1 | `lean/QOU/StandardModel/ThetaQcdFramingCp.lean:73` |
| `UNINST` | `structure` | `QOU.WedderburnMass.FilteredAlgebra` | 10 | 3 | 1 | `mass-theory/curvature-rank-gb-stratification.lean:42` |
| `UNINST` | `structure` | `QOU.MassCore.CellularDepth.OrthIdem` | 10 | 2 | 0 | `mass-theory/cellular-depth-filtration.lean:72` |

---

## Standalone Physics-Bridge `axiom` / `opaque` Declarations (Sample up to 18)

- `opaque QOU.BraidKnot.tauM_n` (`braids-and-knots/markov-trace-inductive-limit.lean:51`)
- `axiom QOU.Archimedean.single_term_limit` (`climax-volume-mass/q-momentum.lean:132`)
- `axiom QOU.VertexAlgebra.AlgElement.embed_succ` (`climax-volume-mass/vertex-algebra-relations.lean:117`)
- `axiom QOU.VertexAlgebra.AlgElement.mul` (`climax-volume-mass/vertex-algebra-relations.lean:125`)
- `axiom QOU.VertexAlgebra.observability` (`climax-volume-mass/vertex-algebra-relations.lean:198`)
- `axiom QOU.VertexAlgebra.self_dual_curvature` (`climax-volume-mass/vertex-algebra-relations.lean:299`)
- `opaque QOU.AeonBoundary.AeonRecyclingHolds` (`information-theory/aeon-boundary-generates-chart.lean:31`)
- `opaque QOU.QuantumComputationalUniversality.QuadraticLevelHolds` (`information-theory/quantum-computational-universality.lean:51`)
- `opaque QOU.QuantumComputationalUniversality.QuantumUniversalityHolds` (`information-theory/quantum-computational-universality.lean:60`)
- `opaque QOU.QuantumComputationalUniversality.DescentDecompositionHolds` (`information-theory/quantum-computational-universality.lean:67`)
- `opaque QOU.QuantumComputationalUniversality.InformationContentHolds` (`information-theory/quantum-computational-universality.lean:73`)
- `axiom QOU.Torsion.neutron_mass_from_substrate_axiom` (`knots-particles-confinement/categorical-neutron.lean:71`)
- `axiom QOU.Torsion.proton_mass_from_substrate_axiom` (`knots-particles-confinement/categorical-proton.lean:69`)
- `opaque QOU.BraidsAndKnots.HeckeNormalForm` (`knots-particles-confinement/confinement-grading-correspondence-conditional.lean:50`)
- `opaque QOU.BraidsAndKnots.confinementLevel` (`knots-particles-confinement/confinement-grading-correspondence-conditional.lean:63`)
- `opaque QOU.BraidKnot.confined` (`knots-particles-confinement/confinement-phase-stratification.lean:42`)
- `opaque QOU.BraidKnot.mu` (`knots-particles-confinement/confinement-phase-stratification.lean:49`)
- `opaque QOU.BraidKnot.sigmaF` (`knots-particles-confinement/confinement-phase-stratification.lean:52`)
