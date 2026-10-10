---
# qou-fxym
title: 'A3 (headline): prove REV_n = O(sqrt n) — the beta-bound is the weak step, not the (l,W) reduction'
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-10-10T07:03:49Z
updated_at: 2026-10-10T07:03:49Z
parent: qou-3e6w
---

Parent epic `qou-3e6w`.  **This is the arc's headline problem**, and it has been untouched by every
tranche since 2026-09-13 — each of which says so explicitly in `qou-hok7`.  Split out on
2026-10-10 so it stops being a closing caveat on other people's work.

## The claim to prove

`REV_n = O(√n)` — equivalently, `M_n ≤ e_∞·√(2n) + o(√n)`, with `e_∞` the certified constant of
#7335/#7349.  `REV_n` is the **free energy over partition shapes**: energy = excess hook length,
entropy = shape multiplicity.

## What is established

- The `Θ(√n)` **coefficient is identified**: `A√2` with `A = e_∞` (#7294).
- `e_∞` has a **value** and, since #7349, is a **maximum over a proved window** rather than a
  search result: `2.43929645512078402706542884314` at `(s_t, s_b) = (8,8)`, window `s ≤ 27`.
- `deg Z_n` is **derived in closed form** (2026-09-07), and the exact divisor is `q^{deg_n}`,
  computable cheaply at any `n` by the max-plus route.
- `log p(n) ~ π√(2n/3) = 2.5651√n` is itself `Θ(√n)`, measured to `n = 4000`.
- **The `(ℓ,W)` reduction is TIGHT** (#7081) — Jensen is optimal per distance class and the
  inter-class coupling factor *shrinks* with `ℓ` (1.208 at `ℓ=8` → 1.072 at `ℓ=60`; 1.128 at the
  maximiser's `ℓ=22`, i.e. 8.2 % of `B` against a ~3× gap).

## 🛑 The honest status of the bound itself

**Sub-linearity is MEASURED over `n ≤ 44`, not proved.**  Nothing in the arc proves it.

**And I diagnosed the weak step backwards once; the correction is the finding.**  The `(ℓ,W)`
reduction being tight means the loss is *not* there — so the **β-bound of #7070 is itself the weak
step**.  The reduction is a faithful instrument, and what it faithfully reports is that the thing
feeding it is loose.

## 🛑 The data cannot distinguish `√n` from `n^{3/4}` (2026-09-07)

Measured, with a control I ran because the inference was tempting: with `α = 1/8`, `C·α = 0.771`
far exceeds what the composition allows — **and `n ≤ 40` sits below the peak of the very statistic
being read**, so the exponent read off it is not the asymptotic exponent.  I refused that
inference; do not re-draw it.

The discriminator is the sibling bean **`qou-0ie7`** (the dropped `Σβ = n + ℓ(ℓ−1)/2` constraint),
which is the one remaining relaxation of size and is a *fresh formulation*, not another bound on
the same object.

## Four routes already tried, all through MOMENTS, all failed

Recorded in `qou-hok7` (2026-09-06, "Four routes to REV closed").  **The suggested attack is to
stop going through moments.**  Three further conjectures of mine on the Jensen step were refuted
in #7093, and the reformulation that survived is worth reusing: write the `β`'s by their partial
gap sums, which makes the object the **ground state of a one-dimensional repulsive gas with hard
walls**.  That is what to bound.

## Formalize-first note

Per the repo's §"Formalize-first probe discipline": this is exactly a *wide/expensive search over
a hypothesis class*, so find the invariant the whole class must satisfy before scanning again.
The `e_∞` leg's own history is the precedent — the concave-relaxation + supergradient certificate
replaced an unenumerable 1e10-block search with a 27-wide proved window.

**Do not close this bean** — its subject is an open conjecture.  And do not report a measured
exponent as a proved one.
