import Lake
open Lake DSL

package qou where
  leanOptions := #[⟨`autoImplicit, false⟩]

@[default_target]
lean_lib QOU where
  srcDir := "."

-- Pin Mathlib to a tagged release matching the lean-toolchain.
-- To update: change both lean-toolchain and this tag together.
require mathlib from git
  "https://github.com/leanprover-community/mathlib4" @ "v4.15.0"
