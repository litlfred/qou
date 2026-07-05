---
# s1ik
title: 'Lean-formalize the Phase-5q closed-form exact-Q identity (currently sympy-verified only, 11/11): product identity over generic CommRing'
status: todo
type: task
created_at: 2026-07-03T00:20:51Z
updated_at: 2026-07-03T00:20:51Z
---


## SUBSUMED FINDING (2026-07-05, PR #3329)

The "Phase-5q closed-form product identity over generic CommRing" this bean
asks to formalize **already exists sorry-free** in
`content/quantum-observable-universe/mass-theory/interface-knot-markov-z.lean`:

- `interfaceTrace {R} [CommRing R] (z h tvac : R) : List Bool -> R` — the
  product closed form;
- `interface_knot_markov_z` — folds positive `z` / negative `z-h`, no sorry;
- `interface_knot_markov_z_bar_symmetric` — averaged `z-h/2` (division-free `2z-h`).

The only unproved residual in the FULL closed form is the Phase-5l constituent
factorisation `tr_M(beta_vac) = prod_i tr_M(constituent_i)`
(`tmli_constituent_composite_agreement.lean`, honest `sorry` field) — a genuine
cabled-braid Markov-trace multiplicativity theorem. General Markov traces are
NOT multiplicative, and `beta_H` is unlinked to the constituents in the abstract
class, so it needs real Markov-peel + cabling infrastructure. This is
research-grade and NOT the sympy identity this bean describes.

**Recommend:** close s1ik as subsumed, or re-scope to the Phase-5l
multiplicativity gap (tracked by its own content block). Owner decision.
