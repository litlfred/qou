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

## Papers

The repository hosts multiple papers as a **folio**:

| Paper | Directory |
|-------|-----------|
| On the Mechanics of Quantum Observable Universes | `content/quantum-observable-universe/` |
| Controlled Double-Slit Electron Diffraction | `content/bach2013-double-slit/` |
| Integration of Skewed-Poisson Structures on Non-commutative Formal Groups | `content/fred2005-formal-groups/` |
| QOU Visualizer | `content/visualizer/` |
| Unital Gröbner--Shirshov Bases over Arbitrary Commutative Ground Rings | `content/unital-groebner-bases/` |

## Chapters (Quantum Observable Universe)

Each chapter is also published as a standalone PDF on GitHub Pages —
useful when you only want the relevant slice of the paper rather than
the full document.  The **PDF** column links to the standalone build;
the **Directory** column links to the source content objects.

| # | Directory | Title | Standalone PDF |
|---|-----------|-------|----------------|
| 0 | `introduction/` | Introduction | [front-matter.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/chapters/front-matter.pdf) |
| 1 | `notation/` | Notation | [front-matter.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/chapters/front-matter.pdf) |
| 2 | `quantum-universes/` | Quantum Universes | [quantum-universes.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/chapters/quantum-universes.pdf) |
| 3 | `quantum-observable-universes/` | Quantum Observable Universes | [quantum-observable-universes.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/chapters/quantum-observable-universes.pdf) |
| 4 | `lifting-and-descent/` | Lifting and Descent | [lifting-and-descent.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/chapters/lifting-and-descent.pdf) |
| 5 | `braids-and-knots/` | Braids and Knots | [braids-and-knots.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/chapters/braids-and-knots.pdf) |
| 6 | `models-of-qous/` | Models of QOUs | [models-of-qous.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/chapters/models-of-qous.pdf) |
| 7 | `descartes-universe/` | The Descartes Universe | [descartes-universe.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/chapters/descartes-universe.pdf) |
| 8 | `particle-interactions/` | Particle Interactions and Nuclear Structure | [particle-interactions.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/chapters/particle-interactions.pdf) |
| 9 | `observations/` | Physical Observations | [observations.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/chapters/observations.pdf) |
| 10 | `molecular-construction/` | Molecular Construction from Nucleon Braids | [molecular-construction.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/chapters/molecular-construction.pdf) |
| 11 | `organic-chemistry/` | Organic Chemistry from Hopf Chains | [organic-chemistry.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/chapters/organic-chemistry.pdf) |
| 12 | `fluid-dynamics/` | Fluid Dynamics of the Brane | [fluid-dynamics.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/chapters/fluid-dynamics.pdf) |
| 13 | `information-theory/` | Information-Theoretic Perspectives | [information-theory.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/chapters/information-theory.pdf) |
| 14 | `q-geometric-langlands/` | $q$-Geometric Langlands Correspondence | [q-geometric-langlands.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/chapters/q-geometric-langlands.pdf) |
| 15 | `glossary/` | Glossary | [front-matter.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/chapters/front-matter.pdf) |
| App | `appendix-knot-periodic-table/` | Knot-Periodic Table of the Elements | [appendix-knot-periodic-table.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/appendix-knot-periodic-table.pdf) |
| App | `appendix-knot-operations/` | Knot Operation Actions Dictionary | [appendix-knot-operations.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/appendix-knot-operations.pdf) |
| App | `appendix-transfer-matrices/` | Transfer Matrices | [appendix-transfer-matrices.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/appendix-transfer-matrices.pdf) |
| App | `appendix-atomic-mass-calculations/` | Atomic Mass Calculations | [appendix-atomic-mass-calculations.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/appendix-atomic-mass-calculations.pdf) |
| App | `appendix-qvalues/` | Q-Value Predictions from $q$ | [appendix-qvalues.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/appendix-qvalues.pdf) |
| App | `appendix-surreals/` | Surreal-number lift of QOU (appendix) | [appendix-surreals.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/appendix-surreals.pdf) |
| — | `index-of-definitions/` | Index of Definitions | [front-matter.pdf](https://litlfred.github.io/qou/papers/quantum-observable-universe/chapters/front-matter.pdf) |

## Lean 4 Formalization

The Lean 4 formalization lives in `content/quantum-observable-universe/lean/`
and covers the key mathematical structures, mass-parameter derivations,
knot theory, and categorical constructions from the manuscript.

### Coverage


Live snapshot from `scripts/lean-coverage.ts` (regenerated on each `main` publish):

| Block kind | Total | With Lean sibling | Fully formalized |
|------------|------:|------------------:|-----------------:|
| Provable claims (theorem/lemma/proposition/corollary) | 567 | 567 | **385 sorry-free (67.9%)** |
| Conjectures (open) | 132 | 132 | **121 class-axiomatised (91.7%)** |
| Definitions | 214 | 214 | — |

Class-axiomatised conjectures follow the conditional-class convention
(CLAUDE.md §3b): the conjecture is encoded as a Lean `class` with
explicit field axioms, and downstream theorems carry the class as an
`[Instance]` hypothesis — so dependent results are fully verified
by Lean modulo a single, named, axiomatised input.

### Modules

| Module | Source |
|--------|--------|
| `QOU.AlgebraicSubstrate` | `AlgebraicSubstrate.lean` |
| `QOU.AppendixSurreals` | `AppendixSurreals.lean` |
| `QOU.ArchimedeanMassFormula` | `ArchimedeanMassFormula.lean` |
| `QOU.AtomicMass` | `AtomicMass.lean` |
| `QOU.Basic` | `Basic.lean` |
| `QOU.BraidKnot` | `BraidKnot.lean` |
| `QOU.BraidTwistFlip` | `BraidTwistFlip.lean` |
| `QOU.BringsSurface` | `BringsSurface.lean` |
| `QOU.Calculations` | `Calculations.lean` |
| `QOU.CategoricalDqSquared` | `CategoricalDqSquared.lean` |
| `QOU.CategoricalMassMarkov` | `CategoricalMassMarkov.lean` |
| `QOU.ChannelSeparation` | `ChannelSeparation.lean` |
| `QOU.ClassicalLimitObstruction` | `ClassicalLimitObstruction.lean` |
| `QOU.CMBFunctor` | `CMBFunctor.lean` |
| `QOU.CODATAChain` | `CODATAChain.lean` |
| `QOU.ColorTubeFibers` | `ColorTubeFibers.lean` |
| `QOU.ComputationalHorizon` | `ComputationalHorizon.lean` |
| `QOU.Descartes` | `Descartes.lean` |
| `QOU.DescartesUniverse` | `DescartesUniverse.lean` |
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
| `QOU.orbital_fourier_decomposition` | `orbital_fourier_decomposition.lean` |
| `QOU.PAdicQuantumGroups` | `PAdicQuantumGroups.lean` |
| `QOU.PathIntegrals` | `PathIntegrals.lean` |
| `QOU.PhiQJSJ` | `PhiQJSJ.lean` |
| `QOU.PhiQPiece` | `PhiQPiece.lean` |
| `QOU.PhotonThreading` | `PhotonThreading.lean` |
| `QOU.q_gl_obstruction_calc` | `q_gl_obstruction_calc.lean` |
| `QOU.QBirchSwinnertonDyer` | `QBirchSwinnertonDyer.lean` |
| `QOU.QCollatz` | `QCollatz.lean` |
| `QOU.QGeometricLanglands` | `QGeometricLanglands.lean` |
| `QOU.qou_canonical_action` | `qou_canonical_action.lean` |
| `QOU.QuantumBloch` | `QuantumBloch.lean` |
| `QOU.QuantumObservableUniverse` | `QuantumObservableUniverse.lean` |
| `QOU.QuaternionicSpectralResolvents` | `QuaternionicSpectralResolvents.lean` |
| `QOU.RepresentationTheory` | `RepresentationTheory.lean` |
| `QOU.SkeinResolutionObstruction` | `SkeinResolutionObstruction.lean` |
| `QOU.StaircaseCornerHook` | `StaircaseCornerHook.lean` |
| `QOU.su2_emergence_dagger_unitarity` | `su2_emergence_dagger_unitarity.lean` |
| `QOU.su2_emergence_volume_determinant` | `su2_emergence_volume_determinant.lean` |
| `QOU.Su2Generators` | `Su2Generators.lean` |
| `QOU.substrate_radial_coordinate` | `substrate_radial_coordinate.lean` |
| `QOU.Torsion` | `Torsion.lean` |
| `QOU.variational_equations` | `variational_equations.lean` |
| `QOU.volume_from_rigidity` | `volume_from_rigidity.lean` |
| `QOU.AlgebraicSubstrate.*` | `19 files` |
| `QOU.AppendixSurreals.*` | `33 files` |
| `QOU.AtomicMass.*` | `1 files` |
| `QOU.BaryonWeight.*` | `1 files` |
| `QOU.Braiding.*` | `10 files` |
| `QOU.BraidKnot.*` | `121 files` |
| `QOU.BraidsAndKnots.*` | `8 files` |
| `QOU.BraidsKnots.*` | `4 files` |
| `QOU.Brings.*` | `2 files` |
| `QOU.BringsSurface.*` | `1 files` |
| `QOU.CategoricalReeb.*` | `1 files` |
| `QOU.Common.*` | `1 files` |
| `QOU.CommutativeQOU.*` | `1 files` |
| `QOU.Descartes.*` | `64 files` |
| `QOU.DescartesUniverse.*` | `4 files` |
| `QOU.Descent.*` | `1 files` |
| `QOU.Encounter.*` | `1 files` |
| `QOU.Experimental.*` | `2 files` |
| `QOU.FeynmanPathIntegrals.*` | `1 files` |
| `QOU.FlavorDressing.*` | `3 files` |
| `QOU.FluidDynamics.*` | `19 files` |
| `QOU.FrobeniusHopfData.*` | `1 files` |
| `QOU.HadronicMass.*` | `3 files` |
| `QOU.Hecke.*` | `9 files` |
| `QOU.HeckeAlgebra.*` | `8 files` |
| `QOU.HyperellipticQuintic.*` | `1 files` |
| `QOU.Information.*` | `6 files` |
| `QOU.Infra.*` | `4 files` |
| `QOU.Interactions.*` | `27 files` |
| `QOU.LiftingDescent.*` | `17 files` |
| `QOU.MagicShell.*` | `1 files` |
| `QOU.MassEndomorphism.*` | `4 files` |
| `QOU.Mathlib.*` | `10 files` |
| `QOU.MathlibExt.*` | `12 files` |
| `QOU.Molecular.*` | `7 files` |
| `QOU.Observations.*` | `10 files` |
| `QOU.ParticleInteractions.*` | `21 files` |
| `QOU.QGeometricLanglands.*` | `4 files` |
| `QOU.QuantumBloch.*` | `2 files` |
| `QOU.QuantumObservableUniverse.*` | `16 files` |
| `QOU.QuantumObservableUniverses.*` | `2 files` |
| `QOU.StaircaseCornerHook.*` | `1 files` |
| `QOU.TopologicalMass.*` | `3 files` |
| `QOU.Torsion.*` | `20 files` |
| `QOU.WedderburnMass.*` | `4 files` |

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

| Simulator | File |
|-----------|------|
| Beta Decay Braid | `simulators/beta_decay_braid.html` |
| Beta Decay Halflife | `simulators/beta_decay_halflife.html` |
| Brings Surface | `simulators/brings_surface.html` |
| Double Slit Simulator | `simulators/double_slit_simulator.html` |
| Knot Atom Diagrams | `simulators/knot_atom_diagrams.html` |
| Knot Periodic Table | `simulators/knot_periodic_table.html` |
| Knot Periodic Table Classic | `simulators/knot_periodic_table_classic.html` |
| Q Double Slit | `simulators/q_double_slit.html` |
| Quantum Brings Surface | `simulators/quantum_brings_surface.html` |
| Valley Stability | `simulators/valley_stability.html` |

## Published Artefacts (GitHub Pages)

> **Note:** If GitHub Pages is not publicly accessible, use the GitHub source
> links in the rightmost column to browse the repository directly.

| Artefact | GitHub Pages | GitHub Source |
|----------|-------------|--------------|
| Folio landing page | [index.html](https://litlfred.github.io/qou/) | [home_page/](https://github.com/litlfred/qou/tree/main/home_page) |
| Paper viewer | [papers/quantum-observable-universe/](https://litlfred.github.io/qou/papers/quantum-observable-universe/) | [folio-assistant/viewer/](https://github.com/litlfred/qou/tree/main/folio-assistant/viewer) |
| Paper (PDF) | [quantum-observable-universe.pdf](https://litlfred.github.io/qou/quantum-observable-universe.pdf) | [content/](https://github.com/litlfred/qou/tree/main/content) |
| Blueprint (interactive graph) | [blueprint/](https://litlfred.github.io/qou/blueprint/) | [blueprint/src/](https://github.com/litlfred/qou/tree/main/blueprint/src) |
| Lean interactive docs | [docs/](https://litlfred.github.io/qou/docs/) | [content/.../lean/](https://github.com/litlfred/qou/tree/main/content/quantum-observable-universe/lean) |
| Schema docs (TypeDoc) | [schema-docs/](https://litlfred.github.io/qou/schema-docs/) | [content/schema/](https://github.com/litlfred/qou/tree/main/content/schema) |
| Axiom / Gap Report | [axiom-report.txt](https://litlfred.github.io/qou/axiom-report.txt) | [.github/scripts/](https://github.com/litlfred/qou/tree/main/.github/scripts) |
| Dependency Graph | [dependency-graph.svg](https://litlfred.github.io/qou/dependency-graph.svg) | CI-generated |
| Proof Objects Manifest | [proof-objects.json](https://litlfred.github.io/qou/proof-objects.json) | CI-generated |
| Glossary | [glossary.json](https://litlfred.github.io/qou/glossary.json) | CI-generated |
| Feature branch drafts | [drafts/](https://litlfred.github.io/qou/drafts/) | CI-generated |

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

| Workflow | Purpose |
|----------|---------|
| `agent-review.yml` | AI-assisted code review |
| `blueprint.yml` | Blueprint compilation, dependency graph, doc-gen4 |
| `build-latex-image.yml` | Build LaTeX CI Docker image |
| `build-lean-mcp.yml` | Build Lean MCP Docker image |
| `deploy-folio.yml` | Deploy Folio Assistant to remote server |
| `docker-ci-image.yml` | Build general CI Docker image |
| `lean-build.yml` | Lean build and proof status updates |
| `lean_ci.yml` | Lean build, proof status, axiom report, doc generation |
| `publish.yml` | Full paper build — PDF, HTML, viewer, schema docs, deploy to gh-pages |
| `pyhecke-native-wheels.yml` | pyhecke-native wheels |
| `pyhecke.yml` | pyhecke |
| `release-folio-assistant.yml` | Release Folio Assistant package |
| `snappea_wasm.yml` | SnapPea WASM build and test |
| `sync-skills.yml` | Sync external skill packages |
| `witness-pipeline.yml` | Witness pipeline |

## Building

### Content validation and LaTeX generation

```bash
bun install                          # Install dependencies (root + content/)
bun run validate                     # Validate content objects
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
