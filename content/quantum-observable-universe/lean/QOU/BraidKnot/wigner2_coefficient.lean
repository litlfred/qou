import Mathlib.Tactic

/-!
# `QOU.BraidKnot.wigner2_coefficient` — intentionally empty; the formalisation lives in the content-block sibling

This module used to hold `Wigner2CoefficientContext` together with a projection that discharged the
manuscript claim from that class's own fields.  Both are removed (2026-08-31).

**Why the declaration was empty.**  The class carried the claim as its own
axioms and the accompanying declaration handed them straight back, so a
`[Wigner2CoefficientContext]` binder assumed nothing and the declaration
asserted nothing.  The file's own docstring said as much: *"the substantive
mathematical content is carried by the context-class axioms"*.  It is the
`proof-no-self-assuming-projection` shape of AGENTS.md §3b-cond item 5, and the
class was inhabited by `Unit` and zero (bean `qou-z9ws`).

**Why removal costs nothing readable.**  Three facts, all measured:

1. The content block's `lean.ref` is `qou:QOU.BraidKnot.wigner2_coefficient`, and per AGENTS.md §0a
   resolution checks the **sibling first** — so the block already resolves to
   [`mass-theory/wigner-2-coefficient.lean`](../../mass-theory/wigner-2-coefficient.lean),
   never to this file.
2. That sibling carries the real formalisation: `a_rho`, `paired_sum_identity`, `sum_involution_double`, `self_conjugate_trace`.
3. **Nothing imports this module** and nothing else in `content/` names the
   class (measured 2026-08-31 across every `.lean` in the tree).

So the declaration was unreachable from its own block, unreachable by import,
and vacuous where it stood.

The file is kept rather than deleted so that the `lean.ref`'s second resolution
candidate — `<lakeRoot>/QOU/BraidKnot/wigner2_coefficient.lean` — still exists as a real path.

Bean `qou-z9ws`; `docs/audits/2026-08-30-the-remainder-is-vacuous-not-open.md`.
-/
