---
# vqep
title: 'EPIC fix 95 genuine Lean vacuity defects'
status: in_progress
type: epic
priority: high
created_at: 2026-06-28T00:00:00Z
updated_at: 2026-06-28T00:00:00Z
---

Fix all 95 genuine Lean vacuity defects (triage: `docs/audits/2026-06-26-vacuity-candidate-triage.md`). Playbook: `docs/audits/vacuity-fix-playbook.md`. Compile-verified Mathlib toolchain is set up and persists on disk.

**Done: 4/95** (witness_4He/8Be/12C = pattern A; descartes_braid_structure = pattern B).

Remaining 91 defects across 31 swarmable child beans - each self-contained, safe to parallelise across high-quality agents:
- `vq01` - braids-and-knots (2)
- `vq02` - information-theory (1)
- `vq03` - lean/Archimedean (8)
- `vq04` - lean/Archimedean (3)
- `vq05` - lean/ArchimedeanUniverse (4)
- `vq06` - lean/BaryonWeight (1)
- `vq07` - lean/BraidKnot (8)
- `vq08` - lean/BraidKnot (2)
- `vq09` - lean/BraidsAndKnots (2)
- `vq10` - lean/Brings (2)
- `vq11` - lean/CategoricalReeb (1)
- `vq12` - lean/CommutativeQOU (1)
- `vq13` - lean/Descent (1)
- `vq14` - lean/Encounter (1)
- `vq15` - lean/Experimental (2)
- `vq16` - lean/FeynmanPathIntegrals (1)
- `vq17` - lean/FrobeniusHopfData (1)
- `vq18` - lean/HadronicMass (1)
- `vq19` - lean/Hecke (1)
- `vq20` - lean/HyperellipticQuintic (1)
- `vq21` - lean/Interactions (2)
- `vq22` - lean/Machinery (1)
- `vq23` - lean/Molecular (5)
- `vq24` - lean/ParticleInteractions (8)
- `vq25` - lean/ParticleInteractions (4)
- `vq26` - lean/QOU-root (8)
- `vq27` - lean/QOU-root (8)
- `vq28` - lean/QuantumObservableUniverse (2)
- `vq29` - mass-theory (7)
- `vq30` - predicted-spectra (1)
- `vq31` - quantum-observable-universes (1)

Swarm protocol: one agent per child bean; set status in_progress on claim; verify each file (lake build + audit) before committing; mark completed when its file-list is 0-flags green.
