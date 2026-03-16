/-!
# Quantum Observable Universe — Lean 4 Formalisation Stubs

This library contains formal statement stubs for the definitions, theorems,
propositions, and lemmas presented in the paper
*Quantum Observable Universe* (F. C. Leitner).

Each declaration carries:
- a docstring linking back to the LaTeX label and chapter,
- references to the closest Mathlib4 counterparts where they exist, and
- a `sorry` placeholder for the proof / construction.

The stubs are intended as scaffolding: contributors can replace `sorry`
with actual proofs, gradually building a machine-checked companion to the
paper.

## Modules

- `QOU.Basic`          Core categorical definitions (Defs 1.1–1.2)
- `QOU.FrobeniusHopf`  Frobenius–Hopf algebra structure
- `QOU.BraidGroup`     Braid group on three strands and S₃
- `QOU.QuantumGroup`   Quantum group U_q(𝔰𝔲(2))
- `QOU.Defs`           Auto-generated index of all labelled items
-/

import QOU.Basic
import QOU.FrobeniusHopf
import QOU.BraidGroup
import QOU.QuantumGroup
import QOU.Defs
