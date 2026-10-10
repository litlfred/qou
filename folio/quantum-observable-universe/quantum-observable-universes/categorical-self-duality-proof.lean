import QOU.QuantumObservableUniverse.Instanton

/-!
# QOU.categorical_self_duality

The canonical Lean source for `prop:categorical-self-duality` lives at
`folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/Instanton.lean`,
which is Lake-built under the `qou` package and declares
`QOU.categorical_self_duality`
(`inst.hodge.IsSelfDual inst.curvature`, proved by the structural
accessor `inst.self_dual`).

Per AGENTS.md §0a (no shadowing stubs) this sibling does not re-declare
the theorem; the import above re-verifies the canonical declaration so
the block's `lean.ref` (`qou:QOU.categorical_self_duality`) resolves to
the library formalization.

A previous version of this sibling re-declared the identical statement
and proof verbatim (extracted from the former monolithic
`QOU/categorical_self_duality.lean`, since removed) and collided with
the library declaration on import.
-/
