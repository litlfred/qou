import Mathlib.Tactic

/-!
# `QOU.BraidKnot.schur_weyl_mass_decomposition` — intentionally empty; the formalisation lives in the content-block sibling

This module used to hold `SchurWeylMassContext` together with a projection that discharged the
manuscript claim from that class's own fields.  Both are removed (2026-08-31).

**Why the declaration was empty.**  The class carried the claim as its own
axioms and the accompanying declaration handed them straight back, so a
`[SchurWeylMassContext]` binder assumed nothing and the declaration
asserted nothing.  The file's own docstring said as much: *"the substantive
mathematical content is carried by the context-class axioms"*.  It is the
`proof-no-self-assuming-projection` shape of AGENTS.md §3b-cond item 5, and the
class was inhabited by `Unit` and zero (bean `qou-z9ws`).

**Why removal costs nothing readable.**  Three facts, all measured:

1. The content block's `lean.ref` is `qou:QOU.BraidKnot.schur_weyl_mass_decomposition`, and per AGENTS.md §0a
   resolution checks the **sibling first** — so the block already resolves to
   [`mass-theory/schur-weyl-mass-decomposition.lean`](../../mass-theory/schur-weyl-mass-decomposition.lean),
   never to this file.
2. That sibling carries the real formalisation: `PartitionOfN`, `qHookProduct`, `schurAtQ`, `spechtCharacter`, `schurWeylWeight`, and (since 2026-09-06) the refutations `not_a_eq_one_three_channels` and `not_additive_wedderburn_missing_partitions` -- the `a_eq_one_three_channels` this line used to name was deleted as false.
3. **Nothing imports this module** and nothing else in `content/` names the
   class (measured 2026-08-31 across every `.lean` in the tree).

So the declaration was unreachable from its own block, unreachable by import,
and vacuous where it stood.

The file is kept rather than deleted so that the `lean.ref`'s second resolution
candidate — `<lakeRoot>/QOU/BraidKnot/schur_weyl_mass_decomposition.lean` — still exists as a real path.

Bean `qou-z9ws`; `docs/audits/2026-08-30-the-remainder-is-vacuous-not-open.md`.
-/
