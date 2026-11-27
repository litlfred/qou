/- Copyright (c) 2026 Quantum Observable Universe Contributors. Released under Apache 2.0 license. -/

/-!
# `HeckeTemperleyLieb` — Root Module

Standalone Lean Reservoir library: Iwahori-Hecke H_n(q), Temperley-Lieb TL_n(q), Jones/Markov/Ocneanu traces, Hoefsmit seminormal irreps, and Young/SYT/Schur-Weyl.

Individual modules are built via `globs = ["HeckeTemperleyLieb", "HeckeTemperleyLieb.+"]` in `lakefile.toml`; import targeted `HeckeTemperleyLieb.<Module>` submodules directly rather than this root.
-/

set_option autoImplicit false
