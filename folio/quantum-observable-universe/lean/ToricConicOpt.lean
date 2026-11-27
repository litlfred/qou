/- Copyright (c) 2026 Quantum Observable Universe Contributors. Released under Apache 2.0 license. -/

/-!
# `ToricConicOpt` — Root Module

Standalone Lean Reservoir library: Sturmfels-Thomas toric chambers, Graver test sets, symmetry-reduced LP/SDP duality certificates, and Farkas/Slater conic optimization.

Individual modules are built via `globs = ["ToricConicOpt", "ToricConicOpt.+"]` in `lakefile.toml`; import targeted `ToricConicOpt.<Module>` submodules directly rather than this root.
-/

set_option autoImplicit false
