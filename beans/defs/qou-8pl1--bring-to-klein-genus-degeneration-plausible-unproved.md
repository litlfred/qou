---
# qou-8pl1
title: 'PLAUSIBLE-NOT-PROVED: Bring → Klein quartic genus degeneration'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-flavour
created_at: 2026-08-06T00:00:00Z
updated_at: 2026-11-16T18:56:59Z
parent: qou-8lxd
---

## UPDATE 2026-08-07 — the S_4 bridge is REFUTED as an argument

`computations/s4_genus3_competitor_fermat.py` (exact Z[i], no floats):

The **Fermat quartic** `x^4 + y^4 + z^4 = 0` is a genus-3 curve whose
automorphism group `(Z/4)^2 : S_3` (order 96, every element machine-verified to
preserve the form) **contains S_4** — exhibited as `V_4 : S_3` and confirmed by
element-order profile `{1:1, 2:9, 3:8, 4:6}`, `V_4` normal, and `S_3` inducing
the full symmetric action on `V_4\{1}`.

So at least TWO distinct genus-3 curves admit `S_4`: Klein (|Aut| = 168) and
Fermat (|Aut| = 96). **The S_4 datum has no separating power.**

This is strictly stronger than the Hurwitz error already recorded below. That
error was "an upper bound is not a selection principle". This one is that even a
*fully correct* "the normalization has genus 3 and inherits S_4" argument still
does not reach the Klein quartic, because a second curve satisfies both
conditions.

**Scope-(a).** The Bring -> Klein degeneration is NOT refuted. What is refuted
is the S_4 bridge as an argument for it. The conjecture now needs a *separating
invariant*.

## Broken into sub-beans

* `qou-8p1a` — enumerate ALL genus-3 curves admitting S_4 (classification is
  known and finite; no heavy infra). **Start here** — it bounds the problem.
* `qou-8p1b` — find an invariant separating Klein from the competitor set, with
  the constraint that it must be computable from the *degeneration data*, not
  just from the candidate curves.
* `qou-8p1c` — the decisive period-matrix route. **BLOCKED on infra**: numpy,
  scipy, sage all absent here and `abelfunctions` is not on PyPI at all. Only
  `sympy` installs. Requirements and three unblock paths recorded.

## Original claim (retained)

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


---

## STALE HEADER — the degeneration is now EXCLUDED, not "plausible-not-proved" (2026-08-07)

This bean's **title and status were never updated** after the marked-pair
result. The most recent entry above records only the *Fermat* finding ("refuted
as an argument"). Since then:

* `s4_genus3_pencil_infinite_family.py` — the S_4-invariant quartics form a
  **pencil**, so infinitely many genus-3 curves admit `S_4`. The bridge is not
  merely non-selective, it is near-vacuous.
* `s4_marked_pair_obstruction.py` — **scope-(b) STRUCTURAL EXCLUSION.** The
  pinch supplies an `S_4`-stable pair of marked points, and `S_4` has *no orbit
  of size <= 2* on `P^2` (the 3-dim rep and its restriction to `A_4` are both
  absolutely irreducible). No smooth plane quartic carries such a pair, and
  Klein is not hyperelliptic.

**So the title is wrong.** This is no longer "PLAUSIBLE-NOT-PROVED": under the
chapter's own three premises (one non-separating `S_4`-invariant cycle; `S_4`
faithful on the normalization; non-hyperelliptic normalization) the degeneration
**cannot happen**. Rescue requires explicitly dropping one premise — see
`qou-8p1e`.

Left as `todo` deliberately: the *conjecture* is not dead, only this route to
it. Renaming is the owner's call.


## Progress Update — 2026-11-16 (`litlfred/qou#8155`, `f3af82fd1d99fc5eb05c0bd46bbd812b46330432`)

- **Lean 4 formalization (`folio/quantum-observable-universe/lean/QOU/Eightfold/FlavourCartanOctetDecuplet.lean`, `0` `sorry`, wired into `QOU.lean`)**:
  - Proves `bring_genus_pinching_and_s4_competitors`: formalizes the topological invariants of pinching 1 non-separating cycle from $g = 4$ to $g = 3$ ($\chi(4) = -6 \to \chi(3) = -4$, $\Delta\chi = +2$, $b_1 : 8 \to 6$), the Hurwitz bounds $84(3-1) = 168$ and $84(4-1) = 252$, and the common $S_4$ divisibility $24 \mid 120$ (Bring), $24 \mid 168$ (Klein, index 7), and $24 \mid 96$ (Fermat quartic competitor, index 4).
- **Witness (`computations/probes/flavour-cartan-octet-decuplet-degeneration.witness.json`)**: `allPassed: true` (`q0Anchor: "independent"`).
