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
| Unital Gröbner Bases over Arbitrary Commutative Ground Rings | `content/unital-groebner-bases/` |

## Chapters (Quantum Observable Universe)

| # | Directory | Title |
|---|-----------|-------|
| 0 | `introduction/` | Introduction |
| 1 | `quantum-universes/` | Quantum Universes |
| 2 | `quantum-observable-universes/` | Quantum Observable Universes |
| 3 | `lifting-and-descent/` | Lifting and Descent |
| 4 | `braids-and-knots/` | Braids and Knots |
| 5 | `models-of-qous/` | Models of QOUs |
| 6 | `descartes-universe/` | The Descartes Universe |
| 7 | `observations/` | Physical Observations |
| 8 | `algebraic-substrate/` | The Algebraic Substrate |
| 9 | `information-theory/` | Information-Theoretic Perspectives |
| 10 | `glossary/` | Glossary |
| App | `appendix-knot-periodic-table/` | Knot-Periodic Table of the Elements |
| App | `appendix-transfer-matrices/` | Transfer Matrices |
| — | `index-of-definitions/` | Index of Definitions |

## Lean 4 Formalization

The Lean 4 formalization lives in `content/quantum-observable-universe/lean/`
and covers the key mathematical structures, mass-parameter derivations,
knot theory, and categorical constructions from the manuscript.

**Important — two kinds of `.lean` files:**

1. **Lake-buildable sources** (`content/<paper>/lean/QOU/...`) — the
   Lake project with `lakefile.toml` + `lean-toolchain`. `lake build`
   compiles these; Mathlib is in scope; MCP tools (`lean_check`,
   `lean_build`) operate on this tree. **All new proofs/definitions
   that need to type-check belong here.**
2. **Sibling `.lean` stubs** (next to a content block's `.ts` + `.md`,
   e.g. `content/<paper>/<chapter>/<block>.lean`) — co-located
   type-signature / documentation placeholders. **These are not in
   the Lake project tree.** `lake build` does not compile them,
   Mathlib is not in scope, and their declarations are invisible to
   other files unless explicitly imported.

The `scripts/lean-audit.ts` audit indexes **both** so manifest
cross-references (`lean: { decl, file }`) resolve either way — but
resolving to a sibling does not mean the declaration compiles, only
that the name is reserved somewhere in the repo. See `CLAUDE.md §8a`
and `.claude/skills/local/lean-completeness-audit.md` for the full
rules.

### Modules

| Module | Source |
|--------|--------|
| `QOU.ArchimedeanMassFormula` | `ArchimedeanMassFormula.lean` |
| `QOU.Basic` | `Basic.lean` |
| `QOU.BringsSurface` | `BringsSurface.lean` |
| `QOU.Calculations` | `Calculations.lean` |
| `QOU.CODATAChain` | `CODATAChain.lean` |
| `QOU.Descartes` | `Descartes.lean` |
| `QOU.DescartesUniverse` | `DescartesUniverse.lean` |
| `QOU.Elaboration` | `Elaboration.lean` |
| `QOU.GaugeFieldFluidDynamics` | `GaugeFieldFluidDynamics.lean` |
| `QOU.Glossary` | `Glossary.lean` |
| `QOU.GroundRingAnnotations` | `GroundRingAnnotations.lean` |
| `QOU.HadronicMass` | `HadronicMass.lean` |
| `QOU.InformationTheory` | `InformationTheory.lean` |
| `QOU.KnotRegistry` | `KnotRegistry.lean` |
| `QOU.KnotTheory` | `KnotTheory.lean` |
| `QOU.LightningPath` | `LightningPath.lean` |
| `QOU.MassDerivation` | `MassDerivation.lean` |
| `QOU.MathConstants` | `MathConstants.lean` |
| `QOU.MobiusEnergy` | `MobiusEnergy.lean` |
| `QOU.PAdicQuantumGroups` | `PAdicQuantumGroups.lean` |
| `QOU.PathIntegrals` | `PathIntegrals.lean` |
| `QOU.PhotonThreading` | `PhotonThreading.lean` |
| `QOU.QuantumObservableUniverse` | `QuantumObservableUniverse.lean` |
| `QOU.RepresentationTheory` | `RepresentationTheory.lean` |
| `QOU.Torsion` | `Torsion.lean` |
| `QOU.Descartes.*` | `6 files` |
| `QOU.QuantumObservableUniverse.*` | `9 files` |
| `QOU.Torsion.*` | `6 files` |

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
| Brings Surface | `simulators/brings_surface.html` |
| Double Slit Simulator | `simulators/double_slit_simulator.html` |
| Knot Atom Diagrams | `simulators/knot_atom_diagrams.html` |
| Knot Periodic Table | `simulators/knot_periodic_table.html` |
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
| `release-folio-assistant.yml` | Release Folio Assistant package |
| `snappea_wasm.yml` | SnapPea WASM build and test |
| `sync-skills.yml` | Sync external skill packages |

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
