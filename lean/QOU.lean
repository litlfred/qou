/-!
# Quantum Observable Universe — Lean 4 Formalisation

This library contains formal definitions, theorem statements, and
proof stubs for the paper *Quantum Observable Universe* (F. C. Leitner).

Each module carries:
- proper mathematical structures with typed fields,
- theorem statements with genuine mathematical content,
- `sorry` placeholders for proofs requiring deep reasoning,
- docstrings linking to LaTeX labels and Mathlib4 counterparts.

## Module overview

### Foundations
- `QOU.Prelude`            Self-contained mathematical foundations

### Chapter 1 — Quantum Observable Universe
- `QOU.Basic`              Core categorical definitions (Defs 1.1–1.4)
- `QOU.FrobeniusHopf`      Frobenius–Hopf algebra structure
- `QOU.Instanton`          Instanton connections, irreducibility, self-duality
- `QOU.SubstrateParameter` Substrate parameter, quantum gauge group, Planck constant
- `QOU.ContactGeometry`    CR manifolds, Reeb fields, fermions, bosons
- `QOU.QDeformation`       q-deformed differential operators

### Chapter 2 — Lifting of Quantum Torsion
- `QOU.BraneTower`         Jet prolongation, brane tower, descent

### Chapter 6 — Path Integrals and Braiding
- `QOU.BraidGroup`         Braid group B₃, S₃, SU(2) basis, Dic₃
- `QOU.QuantumGroup`       Quantum group U_q(𝔰𝔲(2))

### Chapter 7 — Bring's Surface
- `QOU.BringsSurface`      Bring's surface, chiral elliptic curve

### Chapter 8 — Descartes Universe
- `QOU.DescartesUniverse`  Descartes condition and theorem

### Index
- `QOU.Defs`               Auto-generated index of all labelled items
-/

import QOU.Prelude
import QOU.Basic
import QOU.FrobeniusHopf
import QOU.Instanton
import QOU.SubstrateParameter
import QOU.ContactGeometry
import QOU.QDeformation
import QOU.BraneTower
import QOU.BraidGroup
import QOU.QuantumGroup
import QOU.BringsSurface
import QOU.DescartesUniverse
import QOU.Defs
