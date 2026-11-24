import Mathlib.Tactic

/-!
# `QOU.BraidKnot.HeckeBaerStarGeneric.hecke_baer_star_generic` — intentionally empty

This module used to hold `HeckeBaerStarGenericContext` together with a
projection that discharged the manuscript claim from that class's own fields.
Both are removed (2026-08-31).

**Why the declaration was empty.**  The class carried the claim as its own
axioms and the accompanying declaration handed them straight back, so a
`[HeckeBaerStarGenericContext]` binder assumed nothing.  AGENTS.md §3b-cond
item 5; the class was inhabited by `Unit` and zero (bean `qou-z9ws`).

**Why removal costs nothing readable.**  Measured 2026-08-31:

1. The content block's `lean.ref` is
   `qou:QOU.BraidKnot.HeckeBaerStarGeneric.hecke_baer_star_generic`, and per
   AGENTS.md §0a resolution checks the **sibling first** — so the block already
   resolves to
   [`mass-endomorphism/hecke-baer-star-generic.lean`](../../../../mass-endomorphism/hecke-baer-star-generic.lean),
   never to this file.
2. That sibling carries the real formalisation: `class BaerStarRing`,
   `theorem matrix_algebra_baer_right`, `def failure_locus`,
   `theorem hecke_baer_star_generic_sketch`.
3. **Nothing imports this module**, and nothing else in `content/` names the
   class.

The file is kept rather than deleted so the `lean.ref`'s second resolution
candidate still exists as a real path.

Bean `qou-z9ws`; `docs/audits/2026-08-30-the-remainder-is-vacuous-not-open.md`.
-/
