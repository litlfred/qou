/- Copyright (c) 2026 Quantum Observable Universe Contributors. Released under Apache 2.0 license. -/

/-!
# `QCalculus` — Root Module

Standalone Lean Reservoir library: q-numbers, Gaussian binomials, q-Pochhammer, Thomae-Jackson q-calculus, Faddeev/quantum dilogarithms, and Habiro rings.

Individual modules are built via `globs = ["QCalculus", "QCalculus.+"]` in `lakefile.toml`; import targeted `QCalculus.<Module>` submodules directly rather than this root.
-/

set_option autoImplicit false
