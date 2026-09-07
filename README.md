# Quantum Observable Universe

[![Lean CI](https://github.com/litlfred/qou/actions/workflows/lean_ci.yml/badge.svg)](https://github.com/litlfred/qou/actions/workflows/lean_ci.yml)
[![Build & Publish](https://github.com/litlfred/qou/actions/workflows/publish.yml/badge.svg)](https://github.com/litlfred/qou/actions/workflows/publish.yml)
[![Blueprint](https://github.com/litlfred/qou/actions/workflows/blueprint.yml/badge.svg)](https://github.com/litlfred/qou/actions/workflows/blueprint.yml)

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

[`content/quantum-observable-universe/`](content/quantum-observable-universe/) · [full PDF](https://github.com/litlfred/qou/blob/gh-pages/papers/quantum-observable-universe/quantum-observable-universe.pdf)

| # | Chapter | Source | PDF |
|---|---------|--------|-----|
| 0 | Introduction | [`introduction/`](content/quantum-observable-universe/introduction/) | — |
| 1 | Quantum Universes | [`quantum-universes/`](content/quantum-observable-universe/quantum-universes/) | — |
| 2 | Quantum Observable Universes | [`quantum-observable-universes/`](content/quantum-observable-universe/quantum-observable-universes/) | — |
| 3 | Models of QOUs | [`models-of-qous/`](content/quantum-observable-universe/models-of-qous/) | — |
| 4 | Lifting and Descent | [`lifting-and-descent/`](content/quantum-observable-universe/lifting-and-descent/) | — |
| 5 | Braids and Knots | [`braids-and-knots/`](content/quantum-observable-universe/braids-and-knots/) | — |
| 6 | Bring's Surface | [`brings-surface/`](content/quantum-observable-universe/brings-surface/) | — |
| 7 | The Mass Endomorphism | [`mass-endomorphism/`](content/quantum-observable-universe/mass-endomorphism/) | — |
| 8 | Knots, Particles, and Confinement | [`knots-particles-confinement/`](content/quantum-observable-universe/knots-particles-confinement/) | — |
| 9 | The Eightfold Way and Flavor Structure | [`eightfold-way/`](content/quantum-observable-universe/eightfold-way/) | — |
| 10 | Nuclear Interactions and Binding | [`nuclear-interactions/`](content/quantum-observable-universe/nuclear-interactions/) | — |
| 11 | q-Hyperbolic Geometry | [`climax-volume-mass/`](content/quantum-observable-universe/climax-volume-mass/) | — |
| 12 | Mass Analysis | [`mass-theory/`](content/quantum-observable-universe/mass-theory/) | — |
| 13 | Gravity and Spacetime Emergence | [`gravity-spacetime/`](content/quantum-observable-universe/gravity-spacetime/) | — |
| 14 | Predicted Particle Spectra | [`predicted-spectra/`](content/quantum-observable-universe/predicted-spectra/) | — |
| 15 | Physical Observations | [`observations/`](content/quantum-observable-universe/observations/) | — |
| 16 | Molecular Construction from Nucleon Braids | [`molecular-construction/`](content/quantum-observable-universe/molecular-construction/) | — |
| 17 | Organic Chemistry from Hopf Chains | [`organic-chemistry/`](content/quantum-observable-universe/organic-chemistry/) | — |
| 18 | Fluid Dynamics of the Brane | [`fluid-dynamics/`](content/quantum-observable-universe/fluid-dynamics/) | — |
| 19 | Stochastic Mechanics | [`stochastic-mechanics/`](content/quantum-observable-universe/stochastic-mechanics/) | — |
| 20 | Information-Theoretic Perspectives | [`information-theory/`](content/quantum-observable-universe/information-theory/) | — |
| 21 | Measurement and Observation | [`measurement-observation/`](content/quantum-observable-universe/measurement-observation/) | — |
| 22 | $q$-Geometric Langlands Correspondence | [`q-geometric-langlands/`](content/quantum-observable-universe/q-geometric-langlands/) | — |
| 23 | Glossary | [`glossary/`](content/quantum-observable-universe/glossary/) | [glossary.pdf](https://github.com/litlfred/qou/blob/gh-pages/papers/quantum-observable-universe/glossary.pdf) |
| App | Knot-Periodic Table of the Elements | [`appendix-knot-periodic-table/`](content/quantum-observable-universe/appendix-knot-periodic-table/) | [appendix-knot-periodic-table.pdf](https://github.com/litlfred/qou/blob/gh-pages/papers/quantum-observable-universe/appendix-knot-periodic-table.pdf) |
| App | Knot Operation Actions Dictionary | [`appendix-knot-operations/`](content/quantum-observable-universe/appendix-knot-operations/) | — |
| App | Knot Operations Dictionary — archimedean evaluations at the substrate | [`appendix-knot-operations-archimedean/`](content/quantum-observable-universe/appendix-knot-operations-archimedean/) | — |
| App | Transfer Matrices | [`appendix-transfer-matrices/`](content/quantum-observable-universe/appendix-transfer-matrices/) | [appendix-transfer-matrices.pdf](https://github.com/litlfred/qou/blob/gh-pages/papers/quantum-observable-universe/appendix-transfer-matrices.pdf) |
| App | Mass and Binding Algorithms | [`appendix-mass-binding-algorithms/`](content/quantum-observable-universe/appendix-mass-binding-algorithms/) | — |
| App | Toward the Standard Model | [`appendix-standard-model/`](content/quantum-observable-universe/appendix-standard-model/) | — |
| App | Normal Form Witnesses | [`appendix-nf-witnesses/`](content/quantum-observable-universe/appendix-nf-witnesses/) | — |
| App | Imaginary part of the complex volume: $Q$-values from $q$ | [`appendix-qvalues/`](content/quantum-observable-universe/appendix-qvalues/) | — |
| App | Surreal-number lift of QOU (appendix) | [`appendix-surreals/`](content/quantum-observable-universe/appendix-surreals/) | — |
| App | Surreal-number lift at the substrate (archimedean appendix) | [`appendix-surreals-archimedean/`](content/quantum-observable-universe/appendix-surreals-archimedean/) | — |
| — | Index of Definitions | [`index-of-definitions/`](content/quantum-observable-universe/index-of-definitions/) | [index-of-definitions.pdf](https://github.com/litlfred/qou/blob/gh-pages/papers/quantum-observable-universe/index-of-definitions.pdf) |
| 24 | Notation | [`notation/`](content/quantum-observable-universe/notation/) | — |

### Controlled Double-Slit Electron Diffraction

[`content/bach2013-double-slit/`](content/bach2013-double-slit/)

| # | Chapter | Source | PDF |
|---|---------|--------|-----|
| 0 | Controlled Double-Slit Electron Diffraction | [`double-slit-experiment/`](content/bach2013-double-slit/double-slit-experiment/) | — |

### Unital Gröbner--Shirshov Bases over Arbitrary Commutative Ground Rings

[`content/unital-groebner-bases/`](content/unital-groebner-bases/)

| # | Chapter | Source | PDF |
|---|---------|--------|-----|
| 0 | Introduction | [`introduction/`](content/unital-groebner-bases/introduction/) | — |
| 1 | Unital Gröbner--Shirshov Bases over Arbitrary Commutative Ground Rings | [`unital-groebner-bases-chapter/`](content/unital-groebner-bases/unital-groebner-bases-chapter/) | — |
| 2 | Buchberger's Theorem and the PBW Corollary | [`buchberger-and-pbw/`](content/unital-groebner-bases/buchberger-and-pbw/) | — |

### Integration of Skewed-Poisson Structures on Non-commutative Formal Groups

[`content/fred2005-formal-groups/`](content/fred2005-formal-groups/)

| # | Chapter | Source | PDF |
|---|---------|--------|-----|
| 0 | Formal Groups and the Lifting Theorem | [`formal-groups-chapter/`](content/fred2005-formal-groups/formal-groups-chapter/) | — |

### QOU Visualizer

[`content/visualizer/`](content/visualizer/)

| # | Chapter | Source | PDF |
|---|---------|--------|-----|
| 0 | Overview | [`overview/`](content/visualizer/overview/) | — |

> PDF links point at the published build on the `gh-pages` branch through github.com, so they resolve for anyone with access to this repository — public or private — and GitHub renders them inline. A chapter with no published PDF shows `—`.

<!-- folio:toc:end -->


## Lean 4 Formalization

The Lean 4 formalization lives in `content/quantum-observable-universe/lean/`
and covers the key mathematical structures, mass-parameter derivations,
knot theory, and categorical constructions from the manuscript.

### Coverage


Live snapshot from `scripts/lean-coverage.ts`, refreshed by `readme_sync`.
Covers every paper in the folio that carries Lean sources — the figures below
had drifted badly while this table was maintained by hand.

<!-- folio:lean-coverage:begin -->

| Paper | Block kind | Total | With Lean sibling | Fully formalized |
|-------|------------|------:|------------------:|-----------------:|
| On the Mechanics of Quantum Observable Universes | Provable claims | 745 | 738 | **736 sorry-free (98.8%)** |
| | Conjectures (open) | 173 | 170 | **161 class-axiomatised (93.1%)** |
| | Definitions | 257 | 257 | — |
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
| `QOU.FlavorDressing` | `FlavorDressing.lean` |
| `QOU.frobenius_dagger_positive_definite` | `frobenius_dagger_positive_definite.lean` |
| `QOU.frobenius_relation` | `frobenius_relation.lean` |
| `QOU.GaugeFieldFluidDynamics` | `GaugeFieldFluidDynamics.lean` |
| `QOU.Glossary` | `Glossary.lean` |
| `QOU.GradedFrobeniusHopf` | `GradedFrobeniusHopf.lean` |
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
| `QOU.scratch_pmass` | `scratch_pmass.lean` |
| `QOU.scratch_skein` | `scratch_skein.lean` |
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
| `QOU.AlgebraicSubstrate.*` | `37 files` |
| `QOU.AlphaEM.*` | `1 files` |
| `QOU.Appendix.*` | `1 files` |
| `QOU.AppendixQValues.*` | `1 files` |
| `QOU.AppendixSurreals.*` | `44 files` |
| `QOU.Archimedean.*` | `196 files` |
| `QOU.ArchimedeanUniverse.*` | `5 files` |
| `QOU.AtomicMass.*` | `1 files` |
| `QOU.BaryonWeight.*` | `1 files` |
| `QOU.Braiding.*` | `14 files` |
| `QOU.BraidKnot.*` | `375 files` |
| `QOU.BraidsAndKnots.*` | `74 files` |
| `QOU.BraidsKnots.*` | `7 files` |
| `QOU.Brings.*` | `4 files` |
| `QOU.BringsSurface.*` | `7 files` |
| `QOU.CategoricalReeb.*` | `3 files` |
| `QOU.Common.*` | `10 files` |
| `QOU.CommutativeQOU.*` | `1 files` |
| `QOU.Conjectures.*` | `5 files` |
| `QOU.Descent.*` | `1 files` |
| `QOU.Eightfold.*` | `16 files` |
| `QOU.EightfoldWay.*` | `2 files` |
| `QOU.Encounter.*` | `1 files` |
| `QOU.Experimental.*` | `2 files` |
| `QOU.FeynmanPathIntegrals.*` | `1 files` |
| `QOU.FlavorDressing.*` | `4 files` |
| `QOU.FluidDynamics.*` | `35 files` |
| `QOU.FrobeniusHopfData.*` | `1 files` |
| `QOU.GaugeFieldFluidDynamics.*` | `1 files` |
| `QOU.Geometry.*` | `1 files` |
| `QOU.Habiro.*` | `3 files` |
| `QOU.HadronicMass.*` | `3 files` |
| `QOU.Hecke.*` | `30 files` |
| `QOU.HeckeAlgebra.*` | `9 files` |
| `QOU.HyperellipticQuintic.*` | `4 files` |
| `QOU.Information.*` | `39 files` |
| `QOU.Infra.*` | `4 files` |
| `QOU.Interactions.*` | `33 files` |
| `QOU.IwahoriHecke.*` | `7 files` |
| `QOU.Knot.*` | `82 files` |
| `QOU.Knots.*` | `1 files` |
| `QOU.KnotTheory.*` | `4 files` |
| `QOU.LiftingDescent.*` | `22 files` |
| `QOU.Machinery.*` | `88 files` |
| `QOU.MagicShell.*` | `1 files` |
| `QOU.Mass.*` | `75 files` |
| `QOU.MassEndomorphism.*` | `9 files` |
| `QOU.MassTheory.*` | `108 files` |
| `QOU.Mathlib.*` | `169 files` |
| `QOU.MathlibExt.*` | `114 files` |
| `QOU.Molecular.*` | `11 files` |
| `QOU.Observations.*` | `11 files` |
| `QOU.Optimization.*` | `4 files` |
| `QOU.OptionE.*` | `5 files` |
| `QOU.ParticleInteractions.*` | `36 files` |
| `QOU.QBeta.*` | `255 files` |
| `QOU.QGeometricLanglands.*` | `4 files` |
| `QOU.QuantumBloch.*` | `2 files` |
| `QOU.QuantumComputationalUniversality.*` | `1 files` |
| `QOU.QuantumObservableUniverse.*` | `19 files` |
| `QOU.QuantumObservableUniverses.*` | `10 files` |
| `QOU.Resurgence.*` | `4 files` |
| `QOU.SchurWeyl.*` | `66 files` |
| `QOU.Shared.*` | `5 files` |
| `QOU.StandardModel.*` | `20 files` |
| `QOU.Substrate.*` | `5 files` |
| `QOU.TopologicalMass.*` | `3 files` |
| `QOU.Torsion.*` | `21 files` |
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
| `UGB.GrobnerShirshov.*` | `13 files` |
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
| Beta Decay Braid | `simulators/beta_decay_braid.html` |
| Beta Decay Halflife | `simulators/beta_decay_halflife.html` |
| Brings Surface | `simulators/brings_surface.html` |
| Double Slit Simulator | `simulators/double_slit_simulator.html` |
| Knot Atom Diagrams | `simulators/knot_atom_diagrams.html` |
| Knot Periodic Table | `simulators/knot_periodic_table.html` |
| Q Double Slit | `simulators/q_double_slit.html` |
| Quantum Brings Surface | `simulators/quantum_brings_surface.html` |
| Valley Stability | `simulators/valley_stability.html` |

<!-- folio:simulators:end -->

## Published Artefacts

Every artefact below is committed to the **`gh-pages` branch of this
repository**, so the middle column resolves for anyone with repository access
— whether or not the Pages site is public — and GitHub renders PDFs, SVGs and
JSON inline.  The right-hand column is the same file served as a web page,
which needs GitHub Pages to be publicly accessible; use it for the artefacts
that are only useful rendered (the viewer, the API docs).

| Artefact | On `gh-pages` (any collaborator) | Rendered (needs public Pages) |
|----------|----------------------------------|-------------------------------|
| Folio landing page | [index.html](https://github.com/litlfred/qou/blob/gh-pages/index.html) | [/](https://litlfred.github.io/qou/) |
| Paper viewer | [papers/quantum-observable-universe/](https://github.com/litlfred/qou/tree/gh-pages/papers/quantum-observable-universe) | [/papers/quantum-observable-universe/](https://litlfred.github.io/qou/papers/quantum-observable-universe/) |
| Paper (PDF) | [quantum-observable-universe.pdf](https://github.com/litlfred/qou/blob/gh-pages/quantum-observable-universe.pdf) | [/quantum-observable-universe.pdf](https://litlfred.github.io/qou/quantum-observable-universe.pdf) |
| Lean interactive docs | [lean/docs/](https://github.com/litlfred/qou/tree/gh-pages/lean/docs) | [/lean/docs/](https://litlfred.github.io/qou/lean/docs/) |
| Schema docs (TypeDoc) | [schema-docs/](https://github.com/litlfred/qou/tree/gh-pages/schema-docs) | [/schema-docs/](https://litlfred.github.io/qou/schema-docs/) |
| Python API docs | [python-api/](https://github.com/litlfred/qou/tree/gh-pages/python-api) | [/python-api/](https://litlfred.github.io/qou/python-api/) |
| Rust API docs | [rust-api/](https://github.com/litlfred/qou/tree/gh-pages/rust-api) | [/rust-api/](https://litlfred.github.io/qou/rust-api/) |
| Axiom / Gap Report | [axiom-report.txt](https://github.com/litlfred/qou/blob/gh-pages/axiom-report.txt) | [/axiom-report.txt](https://litlfred.github.io/qou/axiom-report.txt) |
| Dependency Graph | [dependency-graph.svg](https://github.com/litlfred/qou/blob/gh-pages/dependency-graph.svg) | [/dependency-graph.svg](https://litlfred.github.io/qou/dependency-graph.svg) |
| Proof Objects Manifest | [proof-objects.json](https://github.com/litlfred/qou/blob/gh-pages/proof-objects.json) | [/proof-objects.json](https://litlfred.github.io/qou/proof-objects.json) |
| Glossary | [glossary.json](https://github.com/litlfred/qou/blob/gh-pages/glossary.json) | [/glossary.json](https://litlfred.github.io/qou/glossary.json) |
| Feature branch drafts | [drafts/](https://github.com/litlfred/qou/tree/gh-pages/drafts) | [/drafts/](https://litlfred.github.io/qou/drafts/) |

> The **Blueprint** row and the `docs/` row that used to sit here have been
> removed: neither `blueprint/` nor `docs/` exists on `gh-pages`, so both
> links were dead in either column.  The Lean docs are published at
> `lean/docs/`, which is what the row above points at.

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
| `content/schema/` | Type system, Zod schemas, builder functions |
| `content/pipeline/` | Validation, rendering, build pipelines |
| `content/quantum-observable-universe/` | Main paper — chapters, appendices, Lean |
| `content/quantum-observable-universe/lean/` | Lean 4 formalization (`lakefile.toml`, `QOU/`) |
| `folio-assistant/` | Platform: MCP server, auth, viewer, chat UI, simulators |
| `folio-assistant/viewer/` | Paper viewer SPA + Pyodide cache |
| `folio-assistant/simulators/` | Interactive HTML/WebGL visualizations |
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
| `references.bib` | Auto-generated BibTeX (source: `content/schema/references.ts`) |
| `home_page/` | Jekyll landing page for GitHub Pages |

## CI/CD Workflows

<!-- folio:workflows:begin -->

| Workflow | Purpose |
|----------|---------|
| `build-lean-mcp.yml` | Build Paper Assistant Image |
| `build.yml` | build |
| `doc-gen4.yml` | Build Lean Documentation (doc-gen4) |
| `lake-cache-refresh.yml` | Lake cache refresh (orphan-branch family) |
| `lean-axiom-guard.yml` | lean-axiom-guard |
| `lean-content-siblings.yml` | lean-content-siblings |
| `lean-orphan-gate.yml` | lean-orphan-gate |
| `lp-dual-gate.yml` | lp-dual-gate |
| `paper-builder-image.yml` | Build paper-builder Docker image |
| `probe-float64-gate.yml` | probe-float64-gate |
| `pyhecke-native-wheel.yml` | pyhecke-native-wheel |
| `witness-staleness.yml` | witness-staleness |

<!-- folio:workflows:end -->

## Building

### Content validation and LaTeX generation

```bash
bun install                          # Install dependencies (root + content/)
bun run scripts/run-validate.ts content/quantum-observable-universe   # Validate content objects
bun run build:content                # Generate chapters/*.tex from content objects
```

### Paper compilation

```bash
latexmk -pdf main.tex               # Compile PDF from generated LaTeX
```

### Lean formalization

```bash
cd content/quantum-observable-universe/lean
lake build                           # Build all Lean modules
```

### Folio Assistant

```bash
cd folio-assistant && bun install
bun run start                        # Start MCP server
bun run start:http                   # Start in HTTP mode
```

### Schema documentation

```bash
bun run build:docs                   # Generate TypeDoc documentation
```

## License

[![CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

This work is licensed under a
[Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt this material for any purpose, provided
appropriate credit is given, a link to the license is provided, and any
changes made are indicated.
