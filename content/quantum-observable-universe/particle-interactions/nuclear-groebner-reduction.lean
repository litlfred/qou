/-!
# nuclear-groebner-reduction — sibling stub

The canonical Lean source for `prop:nuclear-groebner-reduction` lives
at
`content/quantum-observable-universe/lean/QOU/Descartes/NuclearGroebnerReduction.lean`,
which is Lake-built under the `qou` package and declares
`QOU.Descartes.nuclear_groebner_reduction`.

This sibling stub satisfies the sibling lookup so the content-block
manifest's `lean.ref` (`qou:QOU.Descartes.nuclear_groebner_reduction`)
resolves cleanly via the Lake tree.

**Authoring note (open):** the canonical Lean file is currently typed
over `ℝ` (with archimedean hypotheses `1 < q`).  Per CLAUDE.md §7c the
algebraic core belongs over the generic ground ring `R_q = ℤ[q,q⁻¹]`
with an archimedean specialisation in a separate file.  A stalled
R_q-typed copy previously lived at
`content/quantum-observable-universe/descartes-universe/nuclear-groebner-reduction.lean`
with the key decl commented out (`-- (archimedean; not meaningful over
R_q)`); that orphan triple was deleted in this PR because its `.ts`
was not wired into any chapter manifest.  Refactor to the generic
R_q form remains open work.

Ref: [manuscript] §particle-interactions
-/

import QOU.Descartes.NuclearGroebnerReduction
