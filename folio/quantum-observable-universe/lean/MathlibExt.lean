/- Copyright (c) 2026 Quantum Observable Universe Contributors. Released under Apache 2.0 license. -/

/-!
# `MathlibExt` — Root Module

Tier-A selective `leanprover-community/mathlib4` core PR staging library (zero `QOU.*` and zero Tier-B imports).

Individual modules are built via `globs = ["MathlibExt", "MathlibExt.+"]` in `lakefile.toml`; import targeted `MathlibExt.<Module>` submodules directly rather than this root.
-/

set_option autoImplicit false
