---
# qou-8pl1
title: 'PLAUSIBLE-NOT-PROVED: Bring → Klein quartic genus degeneration'
status: todo
type: task
created_at: 2026-08-06T00:00:00Z
updated_at: 2026-08-06T00:00:00Z
---

## Claim (plausible, not proved)

Pinching an `S_4`-invariant 1-cycle on the Bring surface `Σ_4` (genus 4,
`Aut = S_5`) yields, after normalisation, the Klein quartic `Σ_3` (genus 3,
`Aut = PSL(2,7)`, order 168 = the Hurwitz bound).

## What IS established

* `S_4` is the maximal common subgroup: index 5 in `S_5`, and the point
  stabiliser of the `PSL(2,7)` action on the 7 Fano points (index 7).
* `S_4` acts transitively on the 3 lines through the fixed point, on the 4 lines
  not through it, and on the 6 remaining points; the 3 local lines partition the
  6 remaining points into 3 pairs. Machine-verified (`s4_fano_action.py`,
  `s4_bridge_verification.py`).
* Pinching gives a nodal curve of arithmetic genus 4, geometric genus 3, and the
  `S_4` symmetry survives (it fixes the vanishing cycle).

## Why it is NOT proved — the argument on offer is invalid

The chapter argued: "the Hurwitz bound forces `Aut` to be at most `PSL(2,7)`,
and since `S_4` embeds in `PSL(2,7)` as a point stabiliser, the enhancement is
the unique maximal option."

The Hurwitz bound `|Aut| <= 84(g-1) = 168` is an **upper** bound. It does not
force `Aut = PSL(2,7)`; the generic genus-3 curve has small or trivial
automorphism group. That `S_4` embeds shows the enhancement is *available*, not
that it *occurs*. Nothing rules out the normalisation being a genus-3 curve with
`Aut = S_4` exactly, or any other group containing `S_4`. **Maximality is not
selection.** The inference has been withdrawn from
`eightfold-way/color-su3-from-g2.md`.

## What would settle it

Exhibit the curve. Concretely: compute the period matrix of the pinched surface
and match it against the Klein quartic's, or identify the normalisation's
defining equation directly. Either direction (confirm or refute) is publishable
content — a refutation would kill the octonionic colour route's geometric leg.

## Scope discipline

This is a scope-(a) "not established" item, NOT a scope-(b) structural
exclusion. Nothing proved forbids the degeneration; only the offered argument
fails.
