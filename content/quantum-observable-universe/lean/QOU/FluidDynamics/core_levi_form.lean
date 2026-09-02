import Mathlib.Tactic

/-!
# `QOU.FluidDynamics.core_levi_form` — intentionally empty; the formalisation lives in the content-block sibling

This module used to hold `CoreLeviFormContext` together with a projection that
discharged all five clauses of md part (c) from that class's own fields.  Both
are removed (2026-08-31).

**Why the declaration was empty.**  `CoreLeviFormContext` carried
`levi_form_regular : Prop` as a *field* and `levi_form_active :
levi_form_regular` as a second field proving it — so the instance chose the
hypothesis **and** its proof.  Taking `levi_form_regular := True`,
`levi_form_active := trivial`, every scalar `0` (or `1` where a strict
inequality is wanted), `hom_dim_at_p := 0`, `integral_submfd_dim := 0`
satisfies every field, and `core_levi_form` returned the five implications
applied to that self-supplied proof.  A `[CoreLeviFormContext]` binder
therefore assumed nothing.  The file's own docstring said as much: *"the
substantive mathematical content is carried by the context-class axioms"*.
AGENTS.md §3b-cond item 5 (bean `qou-z9ws`).

Note also that it `extends QOU.Shared.SobolevHkRegularityContext`, which pulls
`Mathlib.Data.Real.Basic` and the archimedean setup into a claim that never
uses either — the §7c hazard, in a file whose content was zero.

**Why removal costs nothing readable.**  Three facts, all measured:

1. The content block's `lean.ref` is `qou:QOU.FluidDynamics.core_levi_form`,
   and per AGENTS.md §0a resolution checks the **sibling first** — so the
   block already resolves to
   [`fluid-dynamics/core-levi-form.lean`](../../fluid-dynamics/core-levi-form.lean),
   never to this file.
2. That sibling carries the real content: `CoreLeviData` (data only, no claim
   is a field), the md's claims as named propositions over it, and four
   derived theorems — the eigenvalue-to-aspect bridge, `core_levi_form`
   (`1 ≤ cond` and `cond = max(a⊥/a∥, a∥/a⊥)²`, both derived), the (1)⟺(2)
   equivalence of md (c), and the quantum-pressure consequence.  What it does
   not encode, it says: the `(1 + O(ℏ_q²))` factors, the `q > 1` restriction,
   and md (c) clauses (3)–(5) — which are exactly the clauses *this* file
   projected.
3. **Nothing imports this module** and nothing else in `content/` names the
   class (measured 2026-08-31 across every `.lean` and `.ts` in the tree).

So the declaration was unreachable from its own block, unreachable by import,
and vacuous where it stood.

The file is kept rather than deleted so that the `lean.ref`'s second
resolution candidate — `<lakeRoot>/QOU/FluidDynamics/core_levi_form.lean` —
still exists as a real path.

Bean `qou-z9ws`; `docs/audits/2026-08-30-the-remainder-is-vacuous-not-open.md`.
-/
