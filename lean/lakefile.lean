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

/-- doc-gen4 for interactive HTML documentation with hover definitions.
    Build with: `lake build QOU:docs` -/
require «doc-gen4» from git
  "https://github.com/leanprover/doc-gen4" @ "main"
