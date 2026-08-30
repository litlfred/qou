import QOU.QuantumObservableUniverse.Instanton

/-!
# QOU.categorical_irreducible — Irreducibility of categorical instantons

The canonical Lean source for `lem:categorical-irreducible` lives at
`content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/Instanton.lean`,
which is Lake-built under the `qou` package and declares
`QOU.categorical_irreducible`. Per AGENTS.md §0a (no shadowing stubs) this
sibling does not re-declare the theorem; the import above re-verifies the
canonical declaration so the block's `lean.ref`
(`qou:QOU.categorical_irreducible`) resolves to the library formalization.

## Why this file stopped declaring anything (2026-08-23)

It carried its own `QOU.categorical_irreducible` — the **same
fully-qualified name** as the library's — proved by projecting the
structure field `qou.adjoint_vanishing`:

    theorem categorical_irreducible (qou : QuantumObservableUniverse R)
        (f g : (𝟙_ qou.C) ⟶ qou.adjointObj) : f = g :=
      @Subsingleton.elim _ qou.adjoint_vanishing f g

Two defects, one of which had already been diagnosed elsewhere:

1. **Name collision.** The twin sibling `categorical-irreducible-proof.lean`
   was converted to a note-only importer for exactly this reason, and says
   so: the old declaration *"collided with it on import"*. That conversion
   was applied to one of the two blocks sharing the ref and missed this
   one, so the collision survived — and the two blocks, carrying the
   *identical* `lean.ref`, resolved to *different* declarations.
2. **The claim was assumed, not derived.** `qou.adjoint_vanishing` is the
   vanishing itself, so the theorem restated a hypothesis. The block's own
   proof (`prf:categorical-irreducible`) derives it from trace-freeness of
   `Ad(A)` plus non-degeneracy of `∫_A`; the library now carries those two
   as the hypotheses of `HasCategoricalIrreducibility` and performs the
   cancellation step.

`adjoint_hom_subsingleton` went with it (same projection of the same field;
zero references anywhere in the corpus).
-/
