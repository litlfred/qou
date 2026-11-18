# Quantum Observable Universe

A formal mathematics paper exploring the Quantum Observable Universe (QOU)
with machine-checked **Lean 4** formalization, **content-object architecture**
(TypeScript + Markdown + Lean triples), and an interactive **Folio Assistant**
platform for browsing, reviewing, and exploring the work.

## Content-Object Architecture

Content is organized as **atomic knowledge units** — each definition,
theorem, remark, or proof is a self-contained file triple:

```
content/<paper>/<chapter>/
  <block>.ts    ← Typed manifest (kind, label, dependencies, metadata)
  <block>.md    ← Narrative content (Markdown + TeX snippets)
  <block>.lean  ← Lean 4 formalization (when required by block kind)
```

The pipeline validates content objects against Zod schemas, checks
cross-references, renders LaTeX, and runs AST validation before
producing `chapters/*.tex` output. LaTeX is a **rendering target**,
not the source of truth.

## Contents

One section per paper in the folio.  The **Source** column links to the
content objects; the **PDF** column links to the published standalone build,
and shows `—` for a chapter that has not been published.

<!-- Generated — regenerate with `readme_sync` (MCP) or, from the platform
     checkout, `bun run readme:sync`.  Edits between any `folio:*:begin` /
     `folio:*:end` pair in this file are lost; everything else is authored
     prose and is never touched. -->

<!-- folio:toc:begin -->

### On the Mechanics of Quantum Observable Universes

[`folio/quantum-observable-universe/`](folio/quantum-observable-universe/) · [full PDF](https://github.com/litlfred/qou/blob/gh-pages/papers/quantum-observable-universe/quantum-observable-universe.pdf)

| # | Chapter | Source | PDF |
|---|---------|--------|-----|
| 0 | Introduction | [`introduction/`](folio/quantum-observable-universe/introduction/) | — |
| 1 | Quantum Universes | [`quantum-universes/`](folio/quantum-observable-universe/quantum-universes/) | — |
| 2 | Quantum Observable Universes | [`quantum-observable-universes/`](folio/quantum-observable-universe/quantum-observable-universes/) | — |
| 3 | Models of QOUs | [`models-of-qous/`](folio/quantum-observable-universe/models-of-qous/) | — |
| 4 | Lifting and Descent | [`lifting-and-descent/`](folio/quantum-observable-universe/lifting-and-descent/) | — |
| 5 | Braids and Knots | [`braids-and-knots/`](folio/quantum-observable-universe/braids-and-knots/) | — |
| 6 | Bring's Surface | [`brings-surface/`](folio/quantum-observable-universe/brings-surface/) | — |
| 7 | The Mass Endomorphism | [`mass-endomorphism/`](folio/quantum-observable-universe/mass-endomorphism/) | — |
| 8 | Knots, Particles, and Confinement | [`knots-particles-confinement/`](folio/quantum-observable-universe/knots-particles-confinement/) | — |
| 9 | The Eightfold Way and Flavor Structure | [`eightfold-way/`](folio/quantum-observable-universe/eightfold-way/) | — |
| 10 | Nuclear Interactions and Binding | [`nuclear-interactions/`](folio/quantum-observable-universe/nuclear-interactions/) | — |
| 11 | q-Hyperbolic Geometry | [`climax-volume-mass/`](folio/quantum-observable-universe/climax-volume-mass/) | — |
| 12 | Mass Analysis | [`mass-theory/`](folio/quantum-observable-universe/mass-theory/) | — |
| 13 | Gravity and Spacetime Emergence | [`gravity-spacetime/`](folio/quantum-observable-universe/gravity-spacetime/) | — |
| 14 | Predicted Particle Spectra | [`predicted-spectra/`](folio/quantum-observable-universe/predicted-spectra/) | — |
| 15 | Physical Observations | [`observations/`](folio/quantum-observable-universe/observations/) | — |
| 16 | Molecular Construction from Nucleon Braids | [`molecular-construction/`](folio/quantum-observable-universe/molecular-construction/) | — |
| 17 | Organic Chemistry from Hopf Chains | [`organic-chemistry/`](folio/quantum-observable-universe/organic-chemistry/) | — |
| 18 | Fluid Dynamics of the Brane | [`fluid-dynamics/`](folio/quantum-observable-universe/fluid-dynamics/) | — |
| 19 | Stochastic Mechanics | [`stochastic-mechanics/`](folio/quantum-observable-universe/stochastic-mechanics/) | — |
| 20 | Information-Theoretic Perspectives | [`information-theory/`](folio/quantum-observable-universe/information-theory/) | — |
| 21 | Measurement and Observation | [`measurement-observation/`](folio/quantum-observable-universe/measurement-observation/) | — |
| 22 | $q$-Geometric Langlands Correspondence | [`q-geometric-langlands/`](folio/quantum-observable-universe/q-geometric-langlands/) | — |
| 23 | Glossary | [`glossary/`](folio/quantum-observable-universe/glossary/) | [glossary.pdf](https://github.com/litlfred/qou/blob/gh-pages/papers/quantum-observable-universe/glossary.pdf) |
| App | Knot-Periodic Table of the Elements | [`appendix-knot-periodic-table/`](folio/quantum-observable-universe/appendix-knot-periodic-table/) | [appendix-knot-periodic-table.pdf](https://github.com/litlfred/qou/blob/gh-pages/papers/quantum-observable-universe/appendix-knot-periodic-table.pdf) |
| App | Knot Operation Actions Dictionary | [`appendix-knot-operations/`](folio/quantum-observable-universe/appendix-knot-operations/) | — |
| App | Knot Operations Dictionary — archimedean evaluations at the substrate | [`appendix-knot-operations-archimedean/`](folio/quantum-observable-universe/appendix-knot-operations-archimedean/) | — |
| App | Transfer Matrices | [`appendix-transfer-matrices/`](folio/quantum-observable-universe/appendix-transfer-matrices/) | [appendix-transfer-matrices.pdf](https://github.com/litlfred/qou/blob/gh-pages/papers/quantum-observable-universe/appendix-transfer-matrices.pdf) |
| App | Mass and Binding Algorithms | [`appendix-mass-binding-algorithms/`](folio/quantum-observable-universe/appendix-mass-binding-algorithms/) | — |
| App | Toward the Standard Model | [`appendix-standard-model/`](folio/quantum-observable-universe/appendix-standard-model/) | — |
| App | Normal Form Witnesses | [`appendix-nf-witnesses/`](folio/quantum-observable-universe/appendix-nf-witnesses/) | — |
| App | Imaginary part of the complex volume: $Q$-values from $q$ | [`appendix-qvalues/`](folio/quantum-observable-universe/appendix-qvalues/) | — |
| App | Surreal-number lift of QOU (appendix) | [`appendix-surreals/`](folio/quantum-observable-universe/appendix-surreals/) | — |
| App | Surreal-number lift at the substrate (archimedean appendix) | [`appendix-surreals-archimedean/`](folio/quantum-observable-universe/appendix-surreals-archimedean/) | — |
| — | Index of Definitions | [`index-of-definitions/`](folio/quantum-observable-universe/index-of-definitions/) | [index-of-definitions.pdf](https://github.com/litlfred/qou/blob/gh-pages/papers/quantum-observable-universe/index-of-definitions.pdf) |
| 24 | Notation | [`notation/`](folio/quantum-observable-universe/notation/) | — |

### Controlled Double-Slit Electron Diffraction

[`folio/bach2013-double-slit/`](folio/bach2013-double-slit/)

| # | Chapter | Source | PDF |
|---|---------|--------|-----|
| 0 | Controlled Double-Slit Electron Diffraction | [`double-slit-experiment/`](folio/bach2013-double-slit/double-slit-experiment/) | — |

### Unital Gröbner--Shirshov Bases over Arbitrary Commutative Ground Rings

[`folio/unital-groebner-bases/`](folio/unital-groebner-bases/)

| # | Chapter | Source | PDF |
|---|---------|--------|-----|
| 0 | Introduction | [`introduction/`](folio/unital-groebner-bases/introduction/) | — |
| 1 | Unital Gröbner--Shirshov Bases over Arbitrary Commutative Ground Rings | [`unital-groebner-bases-chapter/`](folio/unital-groebner-bases/unital-groebner-bases-chapter/) | — |
| 2 | Buchberger's Theorem and the PBW Corollary | [`buchberger-and-pbw/`](folio/unital-groebner-bases/buchberger-and-pbw/) | — |

### Integration of Skewed-Poisson Structures on Non-commutative Formal Groups

[`folio/fred2005-formal-groups/`](folio/fred2005-formal-groups/)

| # | Chapter | Source | PDF |
|---|---------|--------|-----|
| 0 | Formal Groups and the Lifting Theorem | [`formal-groups-chapter/`](folio/fred2005-formal-groups/formal-groups-chapter/) | — |

### QOU Visualizer

[`folio/visualizer/`](folio/visualizer/)

| # | Chapter | Source | PDF |
|---|---------|--------|-----|
| 0 | Overview | [`overview/`](folio/visualizer/overview/) | — |

> PDF links point at the published build on the `gh-pages` branch through github.com, so they resolve for anyone with access to this repository — public or private — and GitHub renders them inline. A chapter with no published PDF shows `—`.

<!-- folio:toc:end -->


## Lean 4 Formalization

The Lean 4 formalization lives in `folio/quantum-observable-universe/lean/`
and covers the key mathematical structures, mass-parameter derivations,
knot theory, and categorical constructions from the manuscript.

### Coverage


Live snapshot from `scripts/lean-coverage.ts`, refreshed by `readme_sync`.
Covers every paper in the folio that carries Lean sources — the figures below
had drifted badly while this table was maintained by hand.

<!-- folio:lean-coverage:begin -->

| Paper | Block kind | Total | With Lean sibling | Fully formalized |
|-------|------------|------:|------------------:|-----------------:|
| On the Mechanics of Quantum Observable Universes | Provable claims | 736 | 727 | **727 sorry-free (98.8%)** |
| | Conjectures (open) | 203 | 197 | **175 class-axiomatised (86.2%)** |
| | Definitions | 271 | 271 | — |
| Unital Gröbner--Shirshov Bases over Arbitrary Commutative Ground Rings | Provable claims | 10 | 10 | **10 sorry-free (100%)** |
| | Conjectures (open) | 0 | 0 | **0 class-axiomatised (0%)** |
| | Definitions | 12 | 12 | — |
| Integration of Skewed-Poisson Structures on Non-commutative Formal Groups | Provable claims | 6 | 6 | **6 sorry-free (100%)** |
| | Conjectures (open) | 0 | 0 | **0 class-axiomatised (0%)** |
| | Definitions | 6 | 6 | — |

<!-- folio:lean-coverage:end -->

Class-axiomatised conjectures follow the conditional-class convention
(AGENTS.md §3b): the conjecture is encoded as a Lean `class` with
explicit field axioms, and downstream theorems carry the class as an
`[Instance]` hypothesis — so dependent results are fully verified
by Lean modulo a single, named, axiomatised input.

### Modules

<!-- folio:lean-modules:begin -->

**On the Mechanics of Quantum Observable Universes**

| Module | Source |
|--------|--------|
| `QOU.AlgebraicSubstrate` | `AlgebraicSubstrate.lean` |
| `QOU.AppendixSurreals` | `AppendixSurreals.lean` |
| `QOU.Archimedean` | `Archimedean.lean` |
| `QOU.ArchimedeanMassFormula` | `ArchimedeanMassFormula.lean` |
| `QOU.ArchimedeanUniverse` | `ArchimedeanUniverse.lean` |
| `QOU.AtomicMass` | `AtomicMass.lean` |
| `QOU.Basic` | `Basic.lean` |
| `QOU.BraidKnot` | `BraidKnot.lean` |
| `QOU.BraidTwistFlip` | `BraidTwistFlip.lean` |
| `QOU.BringCone` | `BringCone.lean` |
| `QOU.BringConeGauge` | `BringConeGauge.lean` |
| `QOU.BringConeIcosahedral` | `BringConeIcosahedral.lean` |
| `QOU.BringConeSplit` | `BringConeSplit.lean` |
| `QOU.BringConeSplitChirality` | `BringConeSplitChirality.lean` |
| `QOU.BringHeckeCommensurability` | `BringHeckeCommensurability.lean` |
| `QOU.BringLatticeSpan` | `BringLatticeSpan.lean` |
| `QOU.BringLatticeSpanFiniteQuotient` | `BringLatticeSpanFiniteQuotient.lean` |
| `QOU.BringsSurface` | `BringsSurface.lean` |
| `QOU.Calculations` | `Calculations.lean` |
| `QOU.CategoricalDqSquared` | `CategoricalDqSquared.lean` |
| `QOU.CategoricalDynamics` | `CategoricalDynamics.lean` |
| `QOU.CategoricalMassMarkov` | `CategoricalMassMarkov.lean` |
| `QOU.ChannelSeparation` | `ChannelSeparation.lean` |
| `QOU.ClassicalLimitObstruction` | `ClassicalLimitObstruction.lean` |
| `QOU.CMBFunctor` | `CMBFunctor.lean` |
| `QOU.CODATAChain` | `CODATAChain.lean` |
| `QOU.ColorTubeFibers` | `ColorTubeFibers.lean` |
| `QOU.ComputationalHorizon` | `ComputationalHorizon.lean` |
| `QOU.dq_squared` | `dq_squared.lean` |
| `QOU.Elaboration` | `Elaboration.lean` |
| `QOU.emergence_to_quantum_flat` | `emergence_to_quantum_flat.lean` |
| `QOU.Encounter` | `Encounter.lean` |
| `QOU.FeynmanPathIntegrals` | `FeynmanPathIntegrals.lean` |
| `QOU.FHWExponentWindow` | `FHWExponentWindow.lean` |
| `QOU.FlavorDressing` | `FlavorDressing.lean` |
| `QOU.frobenius_dagger_positive_definite` | `frobenius_dagger_positive_definite.lean` |
| `QOU.frobenius_relation` | `frobenius_relation.lean` |
| `QOU.GaugeFieldFluidDynamics` | `GaugeFieldFluidDynamics.lean` |
| `QOU.Glossary` | `Glossary.lean` |
| `QOU.GradedFrobeniusHopf` | `GradedFrobeniusHopf.lean` |
| `QOU.GrothendieckChern` | `GrothendieckChern.lean` |
| `QOU.GroundRingAnnotations` | `GroundRingAnnotations.lean` |
| `QOU.GroundRingCore` | `GroundRingCore.lean` |
| `QOU.HadronicMass` | `HadronicMass.lean` |
| `QOU.Hecke` | `Hecke.lean` |
| `QOU.HeckeAlgebra` | `HeckeAlgebra.lean` |
| `QOU.HorizonFunctor` | `HorizonFunctor.lean` |
| `QOU.InformationTheory` | `InformationTheory.lean` |
| `QOU.Infra` | `Infra.lean` |
| `QOU.Intent` | `Intent.lean` |
| `QOU.Interactions` | `Interactions.lean` |
| `QOU.JetHorizon` | `JetHorizon.lean` |
| `QOU.Kashaev` | `Kashaev.lean` |
| `QOU.KnotComplement` | `KnotComplement.lean` |
| `QOU.KnotRegistry` | `KnotRegistry.lean` |
| `QOU.KnotTheory` | `KnotTheory.lean` |
| `QOU.LiftingDescent` | `LiftingDescent.lean` |
| `QOU.LightningPath` | `LightningPath.lean` |
| `QOU.MassComputationChainRoadmap` | `MassComputationChainRoadmap.lean` |
| `QOU.MassDerivation` | `MassDerivation.lean` |
| `QOU.MassEndomorphism` | `MassEndomorphism.lean` |
| `QOU.MathConstants` | `MathConstants.lean` |
| `QOU.MathlibExt` | `MathlibExt.lean` |
| `QOU.MobiusEnergy` | `MobiusEnergy.lean` |
| `QOU.MobiusMutualChannel` | `MobiusMutualChannel.lean` |
| `QOU.MobiusRegulator` | `MobiusRegulator.lean` |
| `QOU.MotivesArchimedean` | `MotivesArchimedean.lean` |
| `QOU.ObservableSubcategory` | `ObservableSubcategory.lean` |
| `QOU.OneLoopEdgeLattice` | `OneLoopEdgeLattice.lean` |
| `QOU.OneLoopPrefactorInvariance` | `OneLoopPrefactorInvariance.lean` |
| `QOU.orbital_fourier_decomposition` | `orbital_fourier_decomposition.lean` |
| `QOU.PAdicQuantumGroups` | `PAdicQuantumGroups.lean` |
| `QOU.PathIntegrals` | `PathIntegrals.lean` |
| `QOU.PhiQJSJ` | `PhiQJSJ.lean` |
| `QOU.PhiQPiece` | `PhiQPiece.lean` |
| `QOU.PhotonThreading` | `PhotonThreading.lean` |
| `QOU.q_gl_obstruction_calc` | `q_gl_obstruction_calc.lean` |
| `QOU.QBeta` | `QBeta.lean` |
| `QOU.QBirchSwinnertonDyer` | `QBirchSwinnertonDyer.lean` |
| `QOU.QCollatz` | `QCollatz.lean` |
| `QOU.QGeometricLanglands` | `QGeometricLanglands.lean` |
| `QOU.qou_canonical_action` | `qou_canonical_action.lean` |
| `QOU.QuantumBloch` | `QuantumBloch.lean` |
| `QOU.QuantumObservableUniverse` | `QuantumObservableUniverse.lean` |
| `QOU.QuaternionicElectroweak` | `QuaternionicElectroweak.lean` |
| `QOU.QuaternionicSpectralResolvents` | `QuaternionicSpectralResolvents.lean` |
| `QOU.RepresentationTheory` | `RepresentationTheory.lean` |
| `QOU.Resurgence` | `Resurgence.lean` |
| `QOU.scratch_matrix` | `scratch_matrix.lean` |
| `QOU.SelectionRules` | `SelectionRules.lean` |
| `QOU.Shared` | `Shared.lean` |
| `QOU.SkeinResolutionObstruction` | `SkeinResolutionObstruction.lean` |
| `QOU.StaircaseCornerHook` | `StaircaseCornerHook.lean` |
| `QOU.su2_emergence_dagger_unitarity` | `su2_emergence_dagger_unitarity.lean` |
| `QOU.su2_emergence_volume_determinant` | `su2_emergence_volume_determinant.lean` |
| `QOU.Su2Generators` | `Su2Generators.lean` |
| `QOU.substrate_radial_coordinate` | `substrate_radial_coordinate.lean` |
| `QOU.Torsion` | `Torsion.lean` |
| `QOU.TypedCrossingsEncoding` | `TypedCrossingsEncoding.lean` |
| `QOU.variational_equations` | `variational_equations.lean` |
| `QOU.volume_from_rigidity` | `volume_from_rigidity.lean` |
| `QOU.AlgebraicSubstrate.*` | `41 files` |
| `QOU.AlphaEM.*` | `2 files` |
| `QOU.AppendixQValues.*` | `1 files` |
| `QOU.AppendixSurreals.*` | `50 files` |
| `QOU.Archimedean.*` | `227 files` |
| `QOU.ArchimedeanUniverse.*` | `5 files` |
| `QOU.AtomicMass.*` | `1 files` |
| `QOU.BaryonWeight.*` | `1 files` |
| `QOU.Braiding.*` | `27 files` |
| `QOU.BraidKnot.*` | `445 files` |
| `QOU.BraidsAndKnots.*` | `89 files` |
| `QOU.BraidsKnots.*` | `7 files` |
| `QOU.Brings.*` | `15 files` |
| `QOU.BringsSurface.*` | `13 files` |
| `QOU.CategoricalReeb.*` | `3 files` |
| `QOU.Common.*` | `10 files` |
| `QOU.CommutativeQOU.*` | `1 files` |
| `QOU.Conjectures.*` | `5 files` |
| `QOU.Descent.*` | `1 files` |
| `QOU.Eightfold.*` | `49 files` |
| `QOU.EightfoldWay.*` | `2 files` |
| `QOU.Encounter.*` | `4 files` |
| `QOU.Experimental.*` | `2 files` |
| `QOU.FeynmanPathIntegrals.*` | `2 files` |
| `QOU.FlavorDressing.*` | `4 files` |
| `QOU.FluidDynamics.*` | `42 files` |
| `QOU.FrobeniusHopfData.*` | `3 files` |
| `QOU.GaugeFieldFluidDynamics.*` | `1 files` |
| `QOU.Geometry.*` | `1 files` |
| `QOU.Habiro.*` | `4 files` |
| `QOU.HadronicMass.*` | `3 files` |
| `QOU.Hecke.*` | `98 files` |
| `QOU.HeckeAlgebra.*` | `14 files` |
| `QOU.HyperellipticQuintic.*` | `4 files` |
| `QOU.Information.*` | `43 files` |
| `QOU.Infra.*` | `4 files` |
| `QOU.Interactions.*` | `36 files` |
| `QOU.IwahoriHecke.*` | `38 files` |
| `QOU.Knot.*` | `88 files` |
| `QOU.Knots.*` | `1 files` |
| `QOU.KnotTheory.*` | `4 files` |
| `QOU.KZ.*` | `25 files` |
| `QOU.LiftingDescent.*` | `24 files` |
| `QOU.Machinery.*` | `96 files` |
| `QOU.MagicShell.*` | `1 files` |
| `QOU.Mass.*` | `239 files` |
| `QOU.MassEndomorphism.*` | `9 files` |
| `QOU.MassTheory.*` | `184 files` |
| `QOU.Mathlib.*` | `218 files` |
| `QOU.MathlibExt.*` | `213 files` |
| `QOU.Molecular.*` | `12 files` |
| `QOU.Observations.*` | `14 files` |
| `QOU.OneDim.*` | `4 files` |
| `QOU.Optimization.*` | `11 files` |
| `QOU.OptionE.*` | `5 files` |
| `QOU.OrientedSkein.*` | `4 files` |
| `QOU.ParticleInteractions.*` | `36 files` |
| `QOU.ProofHygiene.*` | `1 files` |
| `QOU.QBeta.*` | `316 files` |
| `QOU.QGeometricLanglands.*` | `4 files` |
| `QOU.QuantumBloch.*` | `2 files` |
| `QOU.QuantumComputationalUniversality.*` | `1 files` |
| `QOU.QuantumObservableUniverse.*` | `29 files` |
| `QOU.QuantumObservableUniverses.*` | `13 files` |
| `QOU.QuantumUniverse.*` | `1 files` |
| `QOU.QuarkState.*` | `23 files` |
| `QOU.Resurgence.*` | `4 files` |
| `QOU.SchurWeyl.*` | `136 files` |
| `QOU.Shared.*` | `7 files` |
| `QOU.StandardModel.*` | `29 files` |
| `QOU.Substrate.*` | `6 files` |
| `QOU.TopologicalMass.*` | `3 files` |
| `QOU.Torsion.*` | `24 files` |
| `QOU.TransferMatrices.*` | `1 files` |
| `QOU.WedderburnMass.*` | `4 files` |

**Unital Gröbner--Shirshov Bases over Arbitrary Commutative Ground Rings**

| Module | Source |
|--------|--------|
| `UGB.BuchbergerPBW` | `BuchbergerPBW.lean` |
| `UGB.GrobnerShirshov` | `GrobnerShirshov.lean` |
| `UGB.Introduction` | `Introduction.lean` |
| `UGB.UnitalGroebner` | `UnitalGroebner.lean` |
| `UGB.BuchbergerPBW.*` | `3 files` |
| `UGB.GrobnerShirshov.*` | `15 files` |
| `UGB.Introduction.*` | `1 files` |
| `UGB.UnitalGroebner.*` | `7 files` |

**Integration of Skewed-Poisson Structures on Non-commutative Formal Groups**

| Module | Source |
|--------|--------|
| `Fred2005.FormalGroups` | `FormalGroups.lean` |

<!-- folio:lean-modules:end -->

### Knot Registry

Every knot in the formalization carries an Alexander-Briggs index, a QOU
physical identity, a SnapPy-verified hyperbolic volume, and a persistent
link to [The Knot Atlas](http://katlas.org/).

| A-B Index | QOU Identity | Hyperbolic Volume | Knot Atlas |
|-----------|-------------|-------------------|------------|
| 0₁ | Neutrino (SU(2) vacuum) | 0 | [0_1](http://katlas.org/wiki/0_1) |
| 3₁ | Electron (Gen 1, B₃ monodromy) | 0 (torus knot) | [3_1](http://katlas.org/wiki/3_1) |
| 4₁ | Muon (Gen 2, mass residue) | 2.0298832128 | [4_1](http://katlas.org/wiki/4_1) |
| 0₁ | Photon (exceptional divisor) | 0 | [0_1](http://katlas.org/wiki/0_1) |

Every `sorry` in the Lean source is preceded by a `-- Ref: [key] url` comment
linking to the foundational reference that would resolve the gap.

## Folio Assistant

The **Folio Assistant** (`folio-assistant/`) is the platform layer providing:

- **MCP Server** — Model Context Protocol server for AI-assisted editing
- **Viewer** — Web-based paper viewer with paper/visualizer toggle
- **Chat UI** — Assistant interface with role-based access (reader/collaborator/owner)
- **Simulators** — Interactive WebGL/HTML visualizations
- **Feedback** — User feedback collection (committed to main)
- **Auth** — Dual OAuth (Google viewers + GitHub collaborators)

### Interactive Simulators

<!-- folio:simulators:begin -->

| Simulator | File |
|-----------|------|
| Beta Decay Braid | [`simulators/beta_decay_braid.html`](simulators/beta_decay_braid.html) |
| Beta Decay Halflife | [`simulators/beta_decay_halflife.html`](simulators/beta_decay_halflife.html) |
| Brings Surface | [`simulators/brings_surface.html`](simulators/brings_surface.html) |
| Double Slit Simulator | [`simulators/double_slit_simulator.html`](simulators/double_slit_simulator.html) |
| Knot Atom Diagrams | [`simulators/knot_atom_diagrams.html`](simulators/knot_atom_diagrams.html) |
| Knot Periodic Table | [`simulators/knot_periodic_table.html`](simulators/knot_periodic_table.html) |
| Q Double Slit | [`simulators/q_double_slit.html`](simulators/q_double_slit.html) |
| Quantum Brings Surface | [`simulators/quantum_brings_surface.html`](simulators/quantum_brings_surface.html) |
| Valley Stability | [`simulators/valley_stability.html`](simulators/valley_stability.html) |

<!-- folio:simulators:end -->

## Published Artefacts

Every artefact below is committed to the **`gh-pages` branch of this
repository**, and the link column resolves for anyone with repository access
— whether or not the Pages site is public — because these are `github.com`
blob/tree URLs rather than `litlfred.github.io` ones.  GitHub renders PDFs,
SVGs and JSON inline.

> **The rendered GitHub Pages site is DEPRECATED (owner, 2026-09-27), and the
> `litlfred.github.io/qou/` column has been dropped from this table.** It was
> not a working surface: measured on 2026-09-27, the `gh-pages` head is
> **2026-07-08** (*"deploy: update PDF with \pm error formatting"*), so the
> rendered column advertised an 81-day-old snapshot as though it were current.
>
> **It is dormant rather than unrefreshable, and an earlier draft of this note
> got that wrong.** The paper build still has a live producer: the platform's
> `publish.yml`, reached from `.github/workflows/build.yml` and pinned to
> `.folio-assistant-pin`. It is `workflow_dispatch`-only and nobody has
> dispatched it since 2026-06-30. What genuinely has no producer left is the
> `lean/` subtree — `doc-gen4.yml` (461 runs, last conclusion `failure`,
> 2026-06-30) is deprecated to `fsh-guts/deprecated/workflows/`.
>
> **The branch itself is NOT removed and the links below still work.** It stays
> as a file store: ~3,000 files under `lean/` (the doc-gen4 render), ~7,300 under `drafts/`, plus the
> paper PDFs and manifests.  Deleting it would break every chapter-PDF link in
> the table further up this README, which is why the deprecation stops at the
> rendering.

| Artefact | On `gh-pages` (any collaborator) |
|----------|----------------------------------|
| Folio landing page | [index.html](https://github.com/litlfred/qou/blob/gh-pages/index.html) |
| Paper viewer | [papers/quantum-observable-universe/](https://github.com/litlfred/qou/tree/gh-pages/papers/quantum-observable-universe) |
| Paper (PDF) | [quantum-observable-universe.pdf](https://github.com/litlfred/qou/blob/gh-pages/quantum-observable-universe.pdf) |
| Lean interactive docs | [lean/](https://github.com/litlfred/qou/tree/gh-pages/lean) |
| Schema docs (TypeDoc) | [schema-docs/](https://github.com/litlfred/qou/tree/gh-pages/schema-docs) |
| Python API docs | [python-api/](https://github.com/litlfred/qou/tree/gh-pages/python-api) |
| Rust API docs | [rust-api/](https://github.com/litlfred/qou/tree/gh-pages/rust-api) |
| Axiom / Gap Report | [axiom-report.txt](https://github.com/litlfred/qou/blob/gh-pages/axiom-report.txt) |
| Dependency Graph | [dependency-graph.svg](https://github.com/litlfred/qou/blob/gh-pages/dependency-graph.svg) |
| Proof Objects Manifest | [proof-objects.json](https://github.com/litlfred/qou/blob/gh-pages/proof-objects.json) |
| Glossary | [glossary.json](https://github.com/litlfred/qou/blob/gh-pages/glossary.json) |
| Feature branch drafts | [drafts/](https://github.com/litlfred/qou/tree/gh-pages/drafts) |

> The **Blueprint** row and the `docs/` row that used to sit here have been
> removed: neither `blueprint/` nor `docs/` exists on `gh-pages`, so both
> links were dead in either column.  The Lean docs are published at
> `lean/` (index `lean/index.html`), which is what the row above points at. They
> were rebuilt 2026-10-11 with doc-gen4, pruned to the QOU, UGB and Fred2005
> modules and wrapped in the harness navbar; until then they sat at `lean/docs/`
> and covered only 27 of those modules.
>
> `docs/` is still absent, and now deliberately so — `docs-site.yml` builds the
> Jekyll docs site and uploads it as a **workflow artifact**; its gh-pages
> write step was removed with this deprecation.  It had never fired: the step
> was gated `if: inputs.publish` with `default: false`, and across all 5 runs
> of that workflow no `docs/` directory was ever created on the branch.

## Libraries

The compute pipeline is layered into reusable packages so external researchers can run their own explorations without cloning the paper repository. See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for the full layered diagram + library coherence status.

### Python (PyPI)

| Package | Source | Role |
|---|---|---|
| [`qou-substrate`](tools/qou-substrate/) | `tools/qou-substrate/` | Substrate parameter `q_0`, mpmath 50-dps precision discipline, `WitnessBuilder`. The 1.1k-LOC foundation — 7 in-repo direct importers (≈67 % transitive, via `pyhecke`). |
| [`pyhecke`](tools/pyhecke/) | `tools/pyhecke/` | Hecke algebra, Gram matrix, Markov trace, tower binding. Primary domain library — 19 in-repo direct importers. |
| [`pyhecke-native`](tools/pyhecke-native/) | `tools/pyhecke-native/` | PyO3 bindings into `hecke-engine` for Rust-accelerated Markov trace. 15 in-repo direct importers. |
| [`qou-mass`](qou-mass/) | `qou-mass/` | High-level facade: `predict("4He")`, `compute_tr_M(Z, N)`, `canonical_braid(Z, N)`. Ships vendored per-Z shards; alpha (`v0.1.0a1`). Canonical wiring example: [`computations/qou_mass_canonical_wiring_example.py`](computations/qou_mass_canonical_wiring_example.py). |
| [`witness-schema`](schemas/witness-schema/) | `schemas/witness-schema/` | Pydantic v2 models for the `*.witness.json` interchange format (Python). Also JSON Schema + Zod (TypeScript). |

### TypeScript / npm

| Package | Source | Role |
|---|---|---|
| `@litlfred/witness-schema` | `schemas/witness-schema/js/` | Zod schemas + JSON Schema for `*.witness.json` (Node, Deno, Bun, browser). |
| `@litlfred/hecke-engine-node` | `tools/hecke-engine-node/` | napi-rs native bindings into `hecke-engine` (Node.js, server-side). |
| `@litlfred/hecke-engine-wasm` | `tools/hecke-engine-wasm/` | wasm-bindgen build of `hecke-engine` for in-browser symbolic compute. |

### Rust (crates)

| Crate | Source | Role |
|---|---|---|
| `hecke-engine` | `tools/hecke-engine/` | Gröbner-Shirshov reducer, Gram matrix, Hoefsmit seminormal, Markov-trace, Wenzl LR, Clarabel SDP backend (opt-in). Currently path-only (not on crates.io due to Clarabel fork + MPFR system deps). |
| `pyhecke-native` | `tools/pyhecke-native/` | PyO3 binding crate (built into the `pyhecke-native` PyPI wheel). |
| `hecke-engine-wasm` | `tools/hecke-engine-wasm/` | WASM-bindgen crate, MPFR-free surface. |

## Project Structure

| Path | Description |
|------|-------------|
| `content/` | **Authoritative content objects** (`.ts` + `.md` + `.lean` triples) |
| `folio/schema/` | Type system, Zod schemas, builder functions |
| `content/pipeline/` | Validation, rendering, build pipelines |
| `folio/quantum-observable-universe/` | Main paper — chapters, appendices, Lean |
| `folio/quantum-observable-universe/lean/` | Lean 4 formalization (`lakefile.toml`, `QOU/`) |
| `folio-assistant/` | Platform: MCP server, auth, viewer, chat UI |
| `folio-assistant/viewer/` | Paper viewer SPA + Pyodide cache |
| `fsh-guts/deprecated/` | PARKED pre-Skills/Tools client-side rendering: the 11 interactive HTML/WebGL simulators and `ruby-3d-viewer.html`. Moved 2026-09-26 on owner ruling (static just-the-docs render instead); kept, not deleted — "we can pull out later if we need". |
| `computations/` | Python compute scripts + `*.witness.json` (in-repo Layer 3) |
| `qou-mass/` | `qou-mass` PyPI package — external-researcher facade (Layer 3 alt.) |
| `tools/qou-substrate/` | `qou-substrate` PyPI package — q₀, precision, WitnessBuilder (Layer 2a) |
| `tools/pyhecke/` | `pyhecke` PyPI package — Hecke/Gram/trace (Layer 2b) |
| `tools/pyhecke-native/` | `pyhecke-native` PyPI wheel — PyO3 → hecke-engine |
| `tools/hecke-engine/` | `hecke-engine` Rust crate — canonical compute core (Layer 1) |
| `tools/hecke-engine-{wasm,node,r,jvm,c}/` | Multi-language bindings of `hecke-engine` |
| `schemas/witness-schema/` | `witness-schema` PyPI + npm — cross-language `*.witness.json` schemas |
| `blueprint/src/` | LeanBlueprint source (dependency graph) |
| `deploy/` | Remote MCP deployment (Docker Compose, Caddy, auth) |
| `.github/workflows/` | CI/CD: Lean build, publish, blueprint, deploy |
| `.claude/skills/` | AI skill definitions (local + synced packages) |
| `scripts/` | Build, setup, and utility scripts |
| `main.tex` | LaTeX preamble (rendering target, not source of truth) |
| `chapters/*.tex` | Generated LaTeX chapters (from content pipeline) |
| `references.bib` | Auto-generated BibTeX (source: `folio/schema/references.ts`) |
| `home_page/` | Jekyll landing page for GitHub Pages |

## CI/CD Workflows

<!-- folio:workflows:begin -->

| Workflow | Purpose |
|----------|---------|
| `atomic-mass-gen-check.yml` | Atomic-mass generated-file drift |
| `build-lean-mcp.yml` | Build Paper Assistant Image |
| `build.yml` | build |
| `compute-qa.yml` | compute-QA (all gates, publish to qa-reports) |
| `deploy-folio.yml` | Deploy Folio |
| `discussions-maintain.yml` | Maintain discussion archive |
| `kg-vocabulary-gate.yml` | kg-vocabulary-gate |
| `lake-cache-refresh.yml` | Lake cache refresh (orphan-branch family) |
| `lean-axiom-guard.yml` | lean-axiom-guard |
| `lean-content-siblings.yml` | lean-content-siblings |
| `lean-orphan-gate.yml` | lean-orphan-gate |
| `lp-dual-gate.yml` | lp-dual-gate |
| `paper-builder-image.yml` | Build paper-builder Docker image |
| `probe-float64-gate.yml` | probe-float64-gate |
| `pyhecke-native-wheel.yml` | pyhecke-native-wheel |
| `witness-refresh.yml` | Witness refresh (commit-back to main) |
| `witness-staleness.yml` | witness-staleness |
| `word-provenance-gate.yml` | word-provenance-gate |

<!-- folio:workflows:end -->

## Building

### Paper PDF (LaTeX)

One command, from the repository root: content blocks -> LaTeX -> `latexmk`,
then a gate on the final-pass log (errors, undefined citations and references).

```bash
scripts/setup-folio-assistant.sh                       # once: the platform checkout
bun run scripts/run-validate.ts folio/quantum-observable-universe   # validate content objects
scripts/build-paper-pdf.sh                             # -> build/paper/main.pdf
```

It needs `latexmk`, TeX Live and `cm-super` (scalable fonts: `microtype` aborts
on page 1 without them). Page layout (wide text block, narrow margins, single
spacing) is [`folio/quantum-observable-universe/latex/layout.tex`](folio/quantum-observable-universe/latex/layout.tex);
macros the shared preamble no longer carries are in
[`latex/macros.tex`](folio/quantum-observable-universe/latex/macros.tex).

### Lean formalization

```bash
cd folio/quantum-observable-universe/lean
lake build                           # Build all Lean modules
```

### Folio Assistant

```bash
cd folio-assistant && bun install
bun run start                        # Start MCP server
bun run start:http                   # Start in HTTP mode
```

### Schema documentation

The schema reference is generated by the platform (`cat-harness-tools/scripts/gen-schema-docs.ts`)
and published with its docs. qou's own TypeDoc build was retired on 2026-10-04: it
re-documented the platform's schemas from inside qou. Its config is kept at
`fsh-guts/deprecated/docs-site/typedoc.json`.

## License

[![CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

This work is licensed under a
[Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt this material for any purpose, provided
appropriate credit is given, a link to the license is provided, and any
changes made are indicated.
