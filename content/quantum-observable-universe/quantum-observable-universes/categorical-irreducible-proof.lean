import QOU.QuantumObservableUniverse.Instanton

/-!
# QOU.categorical_irreducible

The canonical Lean source for `lem:categorical-irreducible` lives at
`content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/Instanton.lean`,
which is Lake-built under the `qou` package and declares
`QOU.categorical_irreducible` (the per-instance form backed by the
`HasCategoricalIrreducibility` typeclass).

Per AGENTS.md §0a (no shadowing stubs) this sibling does not re-declare
the theorem; the import above re-verifies the canonical declaration so
the block's `lean.ref` (`qou:QOU.categorical_irreducible`) resolves to
the library formalization.

A previous version of this sibling carried the deprecated accessor form
`(qou : QuantumObservableUniverse k) → Subsingleton ((𝟙_ _) ⟶ qou.adjointObj)`
proved by projecting the structure field `qou.adjoint_vanishing`
(see `AUDIT-REPORT.md` line 183: "Returns own hypothesis `adj_vanish`");
it was superseded by the library's per-instance formalization and
collided with it on import.
-/
