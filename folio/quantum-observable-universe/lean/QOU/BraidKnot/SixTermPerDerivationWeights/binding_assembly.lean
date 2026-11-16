import Mathlib.Data.Real.Basic

/-!
# `QOU.BraidKnot.SixTermPerDerivationWeights.binding_assembly` — intentionally empty; unreachable and superseded

This module held `BindingAssemblyContext` (four data fields — `Z`, `N`,
`atomic_mass`, `term_weights` — plus `claim_six_term_recovery`) and a `def
binding_assembly` whose body was that claim field: the self-assuming
projection of AGENTS.md §3b-cond item 5.  Both are removed (2026-09-03).

**It was also unreachable.**  The block
[`conj:six-term-per-derivation-weights`](../../../../mass-theory/six-term-per-derivation-weights.md)
refs `qou:QOU.BraidKnot.SixTermPerDerivationWeights.binding_assembly`, and
`resolveCanonicalLean` — the resolver the QA sweep uses — takes the direct
module path first when that file declares the named decl.
[`QOU/BraidKnot/SixTermPerDerivationWeights.lean`](../SixTermPerDerivationWeights.lean)
does declare `binding_assembly`, so the ref resolves **there**, never here.
Measured with the resolver itself rather than inferred from §0a.

That is the mirror image of the sibling-shadowing case §0a warns about: there
a trivial *sibling* hides a real library declaration; here a **library module
path** hides a file in its own subdirectory.  Both leave a declaration that
looks load-bearing and is read by nothing.

The two declarations also **shared a fully-qualified name** —
`QOU.BraidKnot.SixTermPerDerivationWeights.binding_assembly` was declared in
both files, in the same namespace.  No module imports either, so the clash
never surfaced; anything importing both would have failed to elaborate.

Measured across every `.lean` in `content/` on 2026-09-03: nothing names
`BindingAssemblyContext`, nothing imports either module, and `QOU.lean` does
not aggregate them.  Zero consumers.

**The claim now lives at the path the ref resolves to**, as a named
proposition over caller-supplied data carrying the manuscript's actual
five-term assembly — rather than as an `opaque … : Float` constant, which is
what that path held until 2026-09-03.

The file is kept rather than deleted so the resolver's later candidates still
find a real path, per the convention used for the fifteen shells drained
under this bean in #6276.

Bean `qou-z9ws`.
-/
