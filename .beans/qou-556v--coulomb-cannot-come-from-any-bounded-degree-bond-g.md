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

## 🛑 REFRAMED 2026-09-05 (owner) — it is the FALLOFF, not the coupling

Both sections above called a `Z`-dependent per-bond energy "the escape hatch".
The arithmetic is right; the framing is not, and it aims a successor at
re-tuning a letter. **A bond graph is a kernel truncated at range 1.** Coulomb
is `1/r` with no truncation. That is the defect; the `eps(Z)` requirement is its
symptom.

Weighting the captured pairs by `1/r` (uniform ball, `R = r0 A^(1/3)`, `k = 12`):

| iso | Z | A | pairs captured | ENERGY captured |
|---|---:|---:|---:|---:|
| 4He | 2 | 4 | 100 % | **1587 %** |
| 16O | 8 | 16 | 100 % | 360 % |
| 40Ca | 20 | 40 | 63.2 % | 180 % |
| 56Fe | 26 | 56 | 48.0 % | 153 % |
| 120Sn | 50 | 120 | 24.5 % | 101 % |
| 208Pb | 82 | 208 | 14.8 % | **73.1 %** |

The contact model **overshoots light nuclei by 16x** and undershoots heavy ones,
crossing near Sn. **A ratio on both sides of 1 is not repairable by rescaling
any letter**, constant or growing. The scalings say why: a contact sum is
`k Z / 2` — linear in `Z`, no `A` at all — against `(3/5) Z(Z-1)/R` for the
true sum, so the ratio runs as `A^(1/3)/Z`.

**The repair is a decay kernel over ALL pairs**, which is a weighted COMPLETE
graph — degree `Z-1`, exactly the case the theorem excludes. So theorem and
physics agree, and more tightly than the first statement suggested: the
bond-graph form truncates range, and Coulomb does not.

Landed on all four surfaces: this bean, the Lean docstring, the probe (with two
new assertions pinning the 1587 %/73.1 % crossing so it cannot drift into a
docstring-only figure), and the synthesis audit. Corrects the framing shipped in
PR #6783 — the theorem and every number in it stand unchanged.

## 2026-09-05 (owner) — the three channels, their decay rates, and the options

*"There are several channels — EM, strong, weak. They each have their own decay
rate, potentially visible in the perturbation theory. Those three rates are not
necessarily independent, so we need to be careful."*

Right on both counts, and the framework makes both precise.

**The native falloff is Yukawa.** Adding a bond MULTIPLIES the Markov trace by
`b < 1`, so `b^d(i,j) = exp(-mu.d(i,j))` with `mu = -ln b`: exponential in graph
distance. That puts the three channels on one axis, the mediator mass:

| channel | mediator | mu | pair sum over n sites |
|---|---|---:|---|
| weak | W, 80.4 GeV | 407 /fm | O(n) |
| strong | pion, 139.6 MeV | 0.707 /fm | O(n) |
| EM | photon, **massless** | 0 | **Theta(n^2)** |

**So Coulomb is not "a longer-range bond" — it is the massless boundary**, a
different growth class. Every `q`-derived rate is strictly positive because
`b < 1`, so no choice of letters reaches it. Analytic twin of this bean's
degree-side theorem.

## The rates carry ONE constraint and one free parameter

`b_pp.b_nn = 1/[2]_q^2` is an identity, so

    L_pp + L_nn = 2 ln[2]_q      EXACTLY   (0.489899 + 0.907262 = 1.397162)

and `L_pn` sits between them by the averaging convention. Three rates, one
constraint, one free parameter `q`. Scale-free consequence: the RANGE ratios
`lambda_pp : lambda_pn : lambda_nn = 1.8519 : 1.3405 : 1` are derived with no
length scale — the p-p channel is 1.85x longer-ranged than n-n.

## A false alarm, recorded so nobody raises it

The per-site sum is `sum_k |S_k| exp(-mu k)`. For a TREE at bounded degree `d`,
`|S_k| <= d(d-1)^(k-1)` and convergence needs `mu > ln(d-1)`. Against the corpus
letters that looks alarming — only `L_nn` clears `ln 2` at `d = 3`, and **none**
of the three clears `ln(d-1)` at `d >= 4`. **A nuclear packing is not a tree:**
in R^3 the shells grow polynomially (`~k^2`) and every `mu > 0` converges.
Nothing follows from the tree row, and it is pinned as an assertion so it is not
re-raised.

## What DOES follow: the range-1 truncation is not self-consistent

On the fcc shell counts `10k^2+2` (12, 42, 92, 162, ...) the framework's own
decay reaches

| letter | b | effective sites | vs 12 contacts |
|---|---:|---:|---:|
| pp | 0.612688 | **173.23** | **14.44x** |
| pn | 0.508230 | 66.52 | 5.54x |
| nn | 0.403628 | 28.06 | 2.34x |

Truncating at range 1 discards ~93 % of the p-p weight the same framework's
decay rate supplies.

## The options, ranked by cost

**(a) Sum `b^d(i,j)` over ALL pairs at the derived letters.** No new parameter —
it is the letters the corpus already has, applied at their own range. Fixes a
14x self-inconsistency and is the strong channel done properly. **Does not touch
Coulomb**: the per-site sum stays finite, so the constant moves 14x and the
growth class does not.

**(b) A separate `mu = 0` channel for EM.** A different growth class cannot be a
bond letter; it has to enter as its own term. That is the honest shape of the
Coulomb repair.

**(c) Re-tuning any letter.** Excluded twice over: the rates carry one
constraint, and no positive `mu` reaches quadratic growth.

Artifacts: `QOU/Hecke/ChannelRangeGrowthClass.lean` (5 decls, axiom-clean,
`lean`-direct exit 0) and
`computations/qbeta/qbeta_channel_range_growth_class_probe.py` (7/7).
