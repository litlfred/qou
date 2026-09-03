---
# qou-9552
title: 'Descartes knot eigenbasis: all_summands_detected discards the summand index'
status: todo
type: task
priority: normal
created_at: 2026-09-03T21:19:44Z
updated_at: 2026-09-03T21:20:09Z
---

Found while repairing `braids-and-knots/knot-eigenbasis-complete.lean` on
`claude/sap-sibling-tree-2026-09-03` (PR #6539). Recorded rather than fixed:
different block, and its own docstring already discloses the gap.

**Where.** `content/quantum-observable-universe/brings-surface/descartes-knot-eigenbasis.lean:215`

```lean
  all_summands_detected : ∀ (n : ℕ) (hn : n ≥ 1),
    let sw := schurWeyl n hn
    ∀ (_ : Fin sw.numSummands),
    ∃ (jonesVal : ℝ), jonesVal ≠ 0
```

**What is wrong.** Two things, and the second is worse than the one fixed next door:

1. The summand index is bound as `_` — explicitly discarded, so nothing is said *per summand*.
2. `jonesVal` is a **free real** tied to no trace, no braid and no character. So the field asserts that `ℝ` has a non-zero element. Any instance discharges it with `⟨1, one_ne_zero⟩` — and `descartes_knot_eigenbasis` at line 246 does exactly that for the trace it constructs (`tr := fun _ _ => 1`).

The sibling defect in `knot-eigenbasis-complete.lean::summands_detected` was milder: `μ` was bound and unused, but the detected quantity was at least the real `markov.tr (braid_rep β)`.

**What the file already admits.** `descartes_knot_eigenbasis`'s docstring is honest that the detector is one constant for every summand: *"Full per-summand completeness — the distinct character value on each irreducible for general `n` — is the concrete `n = 3` content of `descartes_n3_both_detected` below; the general-`n` character formula is upstream."* So this is a known gap the *type* does not reflect, not a hidden one.

**Shape of the fix**, mirroring what landed next door (commit `c85cd09a591`): give `DescartesMarkovTrace` a per-summand component and quantify detection over it, so the `Fin sw.numSummands` argument occurs in the body. That will make `descartes_knot_eigenbasis`'s current proof (`⟨-(D.q + D.q⁻¹), _⟩`, the same value for every index) fail — which is the point: the general-`n` character formula is what is missing, and it is upstream.

**Not urgent.** Nothing downstream depends on the vacuous field being true, because it is true of everything.
