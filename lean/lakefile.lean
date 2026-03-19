import Lake
open Lake DSL

package qou where
  leanOptions := #[
    ⟨`autoImplicit, false⟩
  ]

@[default_target]
lean_lib QOU where
  srcDir := "."

require mathlib from git
  "https://github.com/leanprover-community/mathlib4" @ "master"

/-- Lean-QuantumInfo: quantum information theory (quantum states, channels,
    entropy, POVMs, separability).  Provides `CPTPMap`, `MState`, `POVM`,
    and von Neumann entropy definitions built on top of mathlib.
    Repository: https://github.com/Timeroot/Lean-QuantumInfo -/
require «quantumInfo» from git
  "https://github.com/Timeroot/Lean-QuantumInfo" @ "main"

/-- doc-gen4 for interactive HTML documentation with hover definitions.
    Build with: `lake build QOU:docs` -/
require «doc-gen4» from git
  "https://github.com/leanprover/doc-gen4" @ "main"
