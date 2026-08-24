---
# qou-d8m1
title: Tie ArchimedeanSubstrateField to SubstrateParameter — here eval is constructible, unlike qou-mt7r
status: todo
type: task
priority: normal
created_at: 2026-08-24T06:57:02Z
updated_at: 2026-08-24T06:57:02Z
---

Follow-up left by `qou-6ome` and `qou-mt7r`.

## The gap

The §7c split (`qou-6ome`) gave the library two layers:

| layer | field |
|---|---|
| `SubstrateParameter M` | `field : M → QOU.GroundRing.R_q` (categorical) |
| `ArchimedeanSubstrateField M` | `field : M → ℝ` (order axioms) |

Nothing relates them. Same defect `qou-mt7r` just closed for the
`MarkovTraceContext` family: the archimedean layer's values are free of the
categorical layer's, so `field_ge_one` and `not_root_of_unity` constrain a real
function unconnected to this universe's substrate parameter.

## Why this half is EASIER than qou-mt7r, and the reason matters

In `qou-mt7r` the coefficient ring `R` is an opaque `CommRing`, so
`eval : R →+* ℝ` had to be **assumed** — see
`QOU/Shared/ArchimedeanEval.lean`, which says so and machine-checks how little
an instance costs (`ofRingHom`).

Here `R_q = LaurentPolynomial ℤ`. Evaluation at a nonzero real is an **ordinary
constructible ring hom**, not a hypothesis. So this side can carry a real
`ι : R_q →+* ℝ, q ↦ q₀` and derive `ArchimedeanSubstrateField.field := ι ∘ sp.field`
rather than positing coherence.

That makes it a genuinely stronger fix than the one `qou-mt7r` could manage,
and it is the reason not to copy that file wholesale.

## Do not build a second mechanism

Both sides want the same thing and it is not a new abstraction: it is
`RingHom _ ℝ`, already in Mathlib. Reuse it; do not invent a parallel notion.

## Still not the τ-functor

Constructibility of `ι` does not touch the archimedean τ-functor wall
(`QOU/Archimedean/TauFunctorTargetSpec.lean`). `ι` is an evaluation of the
ground ring; τ is a functor from the braided category. Do not let the first
being available read as progress on the second.

## Blast radius, not yet measured

20 library modules carry `ArchimedeanSubstrateField`. Whether the tie belongs on
that structure or on a mixin (as `qou-mt7r` chose, to spare 12 pre-archimedean
descendants) needs the same parent-first check before costing it.
