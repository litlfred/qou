# Quantum Observable Universe

[![Lean CI](https://github.com/litlfred/qou/actions/workflows/lean_ci.yml/badge.svg)](https://github.com/litlfred/qou/actions/workflows/lean_ci.yml)

A LaTeX mathematics paper exploring the Quantum Observable Universe (QOU),
quantum torsion, and related topics — with machine-checked Lean 4 formalization.

## Lean 4 Formalization

The `lean/` directory contains a Lean 4 formalization of the key mathematical
structures and the mass-parameter derivation from the manuscript.

| Module | Content |
|--------|---------|
| `QOU.Glossary` | Semantic registry — types for all mathematical objects |
| `QOU.KnotTheory` | Combinatorial knot representations (PD codes) |
| `QOU.KnotRegistry` | Alexander-Briggs knot registry with Knot Atlas URLs |
| `QOU.MassDerivation` | Topological mass conjecture and CODATA derivation |
| `QOU.Calculations` | Skein-deformed residue proofs and substrate derivation |
| `QOU.Basic` | Shared foundations |
| `QOU.*` (chapters) | Per-chapter formalizations |

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

The `Calculations.lean` module proves that the figure-eight volume feeds
through the mass-ratio formula to yield substrate parameter q ≈ 1.1097
within tolerance |q − 1.1097| < 0.0001.

**Interactive documentation**: [Lean docs on GitHub Pages](https://litlfred.github.io/qou/lean/docs/)

**Verification report**: [axiom-report.txt](https://litlfred.github.io/qou/axiom-report.txt) —
includes the **Theoretical Gap Report** listing every `sorry` with its
bibliographic reference and clickable DOI link.

Every `sorry` in the Lean source is preceded by a `-- Ref: [key] url` comment
linking to the foundational reference that would resolve the gap.

## Published Artefacts (GitHub Pages)

| Artefact | Link |
|----------|------|
| Landing page (paper + visualizer) | [index.html](https://litlfred.github.io/qou/) |
| Paper (HTML) | [paper.html](https://litlfred.github.io/qou/paper.html) |
| Paper (PDF) | [quantum-observable-universe.pdf](https://litlfred.github.io/qou/quantum-observable-universe.pdf) |
| Paper (Markdown) | [quantum-observable-universe.md](https://litlfred.github.io/qou/quantum-observable-universe.md) |
| Bring's Surface Visualizer | [visualizer.html](https://litlfred.github.io/qou/visualizer.html) |
| Feature Builds Manifest | [builds.json](https://litlfred.github.io/qou/builds.json) |
| Lean Interactive Docs | [lean/docs/](https://litlfred.github.io/qou/lean/docs/) |
| Axiom / Gap Report | [axiom-report.txt](https://litlfred.github.io/qou/axiom-report.txt) |
| Dependency Graph | [dependency-graph.svg](https://litlfred.github.io/qou/dependency-graph.svg) |
| Proof Objects Manifest | [proof-objects.json](https://litlfred.github.io/qou/proof-objects.json) |

Recent feature builds are listed on the [landing page](https://litlfred.github.io/qou/)
under the **Feature Builds** tab, showing the 5 most recent branch builds with
links to their PDF, diff PDF, HTML preview, and source branch.

## Structure

| File | Description |
|------|-------------|
| `main.tex` | Top-level document — includes all chapters |
| `chapters/quantum-observable-universe.tex` | Chapter 1: Quantum Observable Universe |
| `chapters/qou-elaboration.tex` | Chapter 2: Categorical & Analytic Elaboration |
| `chapters/path-integrals-and-braiding.tex` | Chapter 3: Path Integrals and Braiding |
| `chapters/lifting-of-quantum-torsion.tex` | Chapter 4: Lifting of Quantum Torsion |
| `chapters/brings-surface.tex` | Chapter 5: Bring's Surface |
| `chapters/descartes-universe.tex` | Chapter 6: Descartes Universe |
| `chapters/p-adic-quantum-groups.tex` | Chapter 7: p-Adic Quantum Observable Universe |
| `chapters/gauge-field-fluid-dynamics.tex` | Chapter 8: Gauge Field Fluid Dynamics |
| `chapters/information-theory.tex` | Chapter 9: Information Theory |
| `chapters/interpretations.tex` | Chapter 10: Interpretations |
| `chapters/experimental-evidence.tex` | Chapter 11: Experimental Evidence |
| `chapters/speculations.tex` | Chapter 12: Speculations |
| `references.bib` | BibTeX bibliography |
| `brings_surface.html` | Interactive 3D Bring's Surface visualizer |

## Building

Compile with `pdflatex` (run twice to resolve cross-references):

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Or use `latexmk`:

```bash
latexmk -pdf main.tex
```

## License

[![CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

This work is licensed under a
[Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt this material for any purpose, provided
appropriate credit is given, a link to the license is provided, and any
changes made are indicated.
