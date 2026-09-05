---
# qou-556v
title: Coulomb cannot come from ANY bounded-degree bond graph — the chain result is the handshake lemma
status: completed
type: task
priority: normal
created_at: 2026-09-05T08:14:00Z
updated_at: 2026-09-05T08:21:04Z
---


Branch `claude/q407-self-assuming-projections-2026-08-21`. Generalises the chain
result merged in PR #6777.

## The claim

`qbeta_chain_cannot_carry_coulomb_or_surface_probe.py` showed a chain carries
`2/Z` of the proton pairs and so cannot produce `a_C Z(Z-1)/A^(1/3)`. That proof
used nothing about a path except **its degree is 2**. Every edge set the corpus
has built is degree-bounded:

| edge set | edges | max degree | source |
|---|---|---|---|
| canonical chain | `A-1` | 2 | `atom_braid_word_3A` |
| max-contact convex deltahedra | `3A-6` | 5 | GAP-1 / `qou-lzoh` |
| bounded-degree packing | `kA/2` | `k <= 12` | `qou-kqdn` (completed 2026-09-05) |

So the useful statement is about the class, not the member: **no sum over the
edges of a degree-bounded graph, with a `Z`-independent per-bond energy, grows
like `Z^2`.** By the handshake lemma `2E = sum of degrees <= dZ`, so
`E / C(Z,2) <= d/(Z-1) -> 0`.

This closes a route rather than nibbling at one: Coulomb is not a missing term
in the bond graph, it is outside the bond-graph *form*. Which is physically
right — Coulomb is `1/r` long-range, not contact.

## CORPUS-GREP FIRST — what is nearby and why none of it is this

- `QOU/Hecke/BindingExtensivity.lean` `exists_pow_gt_linear` — exponential vs
  linear (`t^n` vs `s*n`), not quadratic vs linear. Different growth classes.
- `QOU/Mass/UniformBondSimpleGraphExclusion.lean` `b3Uniform_nonpos` — 3-body
  uniform bonds, a sign result on `e3 - 3*e2`.
- `QOU/Mass/CoordinationSurfaceDeficit.lean` (`qou-kqdn`) — the SURFACE term
  from the same bounded-degree model, closed today by a sibling. Complementary:
  the boundary deficit is what a degree bound *gives* you; this bean is what it
  *forbids*. Not redoing it.
- `qou-nial` — the root-cause bean this generalises. Will be appended on close.

## THE ESCAPE HATCH, stated up front

The theorem bites only for a per-bond energy that does not itself grow with `Z`.
A law with `epsilon(Z) ~ Z` is untouched by it. That is the honest limit, and it
is in the Lean docstring rather than only here — a reader who wants Coulomb
inside the bond graph must go through a `Z`-dependent bond energy, and should be
made to say so.

## RESULT (2026-09-05) — proved, instantiated, and one correction to GAP-1

**Lean:** `content/quantum-observable-universe/lean/QOU/Hecke/BoundedDegreeCoulomb.lean`,
registered in `QOU.lean`. 4 declarations, all `[propext, Classical.choice,
Quot.sound]`, `lean`-direct exit 0 in 5.6 s, no warnings.

- `two_mul_card_edge_le` — degree-sum formula as a bond-count bound: a
  `SimpleGraph` with every degree `<= d` has `2E <= dn`.
- `edge_share_le` — the covered share of pairs is at most `d/(n-1)`.
- `exists_gt_bounded_degree_bond_sum` — for any `eps >= 0`, `d >= 0`, `c > 0`
  there is an `N` past which EVERY graph with that degree bound has
  `eps*E < c*(n(n-1)/2)`.
- `bond_sum_lt_pair_target` — the same on the graph itself.

**Probe:** `computations/qbeta/qbeta_bounded_degree_cannot_carry_coulomb_probe.py`
(7/7, 30 dps, float64-guard clean, 2548-nuclide AME selection).

Share of proton pairs covered, `d/(Z-1)`:

| Z | chain d=2 | deltahedra d=5 | close packing d=12 |
|---:|---:|---:|---:|
| 20 | 10.53 % | 26.32 % | 63.16 % |
| 50 | 4.08 % | 10.20 % | 24.49 % |
| 82 | **2.47 %** | 6.17 % | **14.81 %** |

The bound applies to the induced PROTON subgraph whatever the assignment, since
an induced subgraph's degrees are bounded by the parent's. So no proton-siting
model can rescue it.

**The escape hatch, measured.** To reproduce the SEMF term a bounded-degree law
needs `eps(Z) >= 2 a_C (Z-1)/(d A^(1/3))`, which runs

    4He 0.073180  ->  16O 0.322705  ->  56Fe 0.759088  ->  208Pb 1.588103  MeV

a span of **21.7x**, and dividing out `(Z-1)/A^(1/3)` flattens it to 1.000 to
working precision — the requirement is linear in `Z-1` and nothing else. The
corpus's letters `b_pp`, `b_pn`, `b_nn` are NUMBERS. This is a function of the
nucleus, so the hatch is a different form of law, not a re-tuning.

At 208Pb the omitted SEMF Coulomb term is **47.7 %** of the total binding
(781.3 of 1636.4 MeV), so it is not something the law can carry in its error bar.

## Correction to GAP-1 (`qou-lzoh`) — `3A-6` is degree-5-admissible only to A=12

A triangulated sphere has average degree `2E/A = 6 - 12/A`, so max degree exceeds
5 exactly when `A > 12`; and there are exactly eight convex deltahedra, the
largest the icosahedron at 12 vertices. GAP-1's table is A=5,6,7 and correct
there; extrapolating `3A-6` past A=12 silently raises the degree bound. **This
does not touch GAP-1's result or this theorem** — the theorem holds for any `d`,
and the larger `d` still loses — it only fixes which `d` to quote. Recorded as an
assertion in the probe so it cannot drift back.

## What this closes, and the sibling it does NOT duplicate

Closes: "Coulomb is a missing TERM in the bond graph". It is outside the
bond-graph FORM. Physically right — Coulomb is `1/r`, a contact graph is not.

Does NOT touch the surface term, and the contrast is the useful part: the SAME
degree bound *supplies* the surface term (`QOU/Mass/CoordinationSurfaceDeficit.lean`,
`qou-kqdn`, completed by a sibling session earlier today) because a boundary
deficit is what bounded degree gives you. One bound, two opposite consequences:
fix the edge set and the surface term appears; fix it and Coulomb still does not.
