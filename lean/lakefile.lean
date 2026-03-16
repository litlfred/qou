import Lake
open Lake DSL

package qou where
  leanOptions := #[⟨`autoImplicit, false⟩]

@[default_target]
lean_lib QOU where
  srcDir := "."

require mathlib from git
  "https://github.com/leanprover-community/mathlib4" @ "master"
