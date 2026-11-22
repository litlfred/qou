import QOU.Archimedean.NuclearGroebnerReduction


/-!
# nuclear-groebner-reduction — sibling stub

The canonical Lean source for `prop:nuclear-groebner-reduction` lives at
`folio/quantum-observable-universe/lean/QOU/Archimedean/NuclearGroebnerReduction.lean`,
which is Lake-built under the `qou` package and declares
`QOU.Archimedean.nuclear_groebner_reduction` together with its
supporting structures (`HeckeElement`, `isReduced` and
`max_word_length_bound`; the former `normal_form_exists_unique` axiom was
removed on 2026-08-25 as formally defective).

This sibling re-exports that module (via `import`) so the content-block
manifest's `lean.ref` (`qou:QOU.Archimedean.nuclear_groebner_reduction`)
resolves cleanly against the Lake tree, without shadowing the real
declaration with a duplicate stub (per AGENTS.md §"No shadowing stubs").

**Authoring note (open):** the canonical Lean file is currently typed
over `ℝ` (with archimedean hypotheses `1 < q`).  Per AGENTS.md §7c the
algebraic core belongs over the generic ground ring `R_q = ℤ[q,q⁻¹]`
with an archimedean specialisation in a separate file.  Refactor to the
generic R_q form remains open work.

Ref: [leitner2026] §particle-interactions
-/
