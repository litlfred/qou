---
layout: default
title: QOU Formalization
---

# Quantum Observable Universe — Formalization

This project formalizes the mathematical content of the
[QOU manuscript](quantum-observable-universe.pdf) in Lean 4.

## Documentation

| Resource | Description |
|----------|-------------|
| [Blueprint](blueprint/) | Interactive dependency graph with proof status |
| [Blueprint (PDF)](blueprint.pdf) | Print version of the formalization blueprint |
| [API Documentation](docs/) | doc-gen4 interactive Lean documentation |
| [Axiom Report](axiom-report.txt) | Verification report with sorry audit |
| [Dependency Graph](dependency-graph.svg) | Visual proof dependency graph |

## Knot Registry

| A-B Index | QOU Identity | Hyperbolic Volume | Knot Atlas |
|-----------|-------------|-------------------|------------|
| 0₁ | Neutrino | 0 | [0_1](http://katlas.org/wiki/0_1) |
| 3₁ | Electron | 0 (torus knot) | [3_1](http://katlas.org/wiki/3_1) |
| 4₁ | Muon | 2.0298832128 | [4_1](http://katlas.org/wiki/4_1) |

## Status

The formalization tracks the manuscript's theorem-like environments.
Each `sorry` in the Lean source is annotated with a `-- Ref: [key] url`
comment linking to the foundational reference.
