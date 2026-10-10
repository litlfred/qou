---
# qou-7q5m
title: 'NT-T5: bridge — GGM eq-49 as W_q-module vs the proved q-lift kernel; non-diagonal equivalence-or-obstruction via RSZ invariants (continues qou-m3ze after the diagonal-gauge scope-(b) prune)'
status: completed
type: task
created_at: 2026-07-20T03:21:57Z
updated_at: 2026-08-07T00:00:00Z
---

## Already answered — by an audit dated the same day this bean was filed

[`docs/audits/2026-07-20-qlift-routeA-rsz-invariants.md`](../docs/audits/2026-07-20-qlift-routeA-rsz-invariants.md)
§5 settles exactly the question in the title, and settles it for **arbitrary
GL₂ gauge**, not merely the diagonal gauges pruned by `qou-m3ze`:

> **Scope-(b) structural exclusion.** C1 and C2 are **inequivalent as
> q-difference modules over ℂ((x)) and ℂ({x}), at both local points 0 and ∞**
> — no gauge `F ∈ GL₂` with formal or convergent Laurent coefficients in
> `x = q^m` (at either point) maps one to the other.

The two kernels:

| | operator |
|---|---|
| **C1** (proved q-involution / q-Borel form) | `[m+2]_q·b_{m+2} = b_{m+1} + b_m` |
| **C2** (GGM eq 49, arXiv:2012.00062 p. 14) | `y_{m+1} − (2 − q^m)·y_m + y_{m−1} = 0` |

Invariants cited, both gauge-invariant by construction — which is why they
reach non-diagonal gauges that the coefficient-matching route could not:

| invariant | C1 | C2 | RSZ authority |
|---|---|---|---|
| ∞-slopes | `{½, ½}` | `{−1, +1}` | Thm 2.2.1 (Newton polygon is a module invariant) + Thm 2.2.4 (slope filtration) |
| exponents at 0 | complex pair, `u² + (q−1)u + (q−1) = 0`, disc `(q−1)(q−5) < 0` for `1 < q < 5` | `{1, 1}` mod `q^ℤ` | §2.2.2.1 (fuchsian classification) |

Either mismatch alone is decisive; there are two independent ones.

The bean was created 2026-07-20 03:21 as the follow-on to the diagonal prune,
the audit landed the same day, and the bean was never closed. Nothing further
was required of it — this is the corpus-grep pattern AGENTS.md warns about
(PRs #1515 / #1532 / #1543), caught on inspection 2026-08-07.

## Independent cross-check from the ∞-side ramification work

`computations/qbeta/c3_w2_c1_ramification_leading_blocks.py` (landed
2026-08-06, 3/3 assertions) recomputed C1's ∞ Newton polygon from scratch,
in a separate convention, without consulting this audit. It finds a **single
edge of slope ½ spanning `i = 0..2`** — i.e. slope ½ with multiplicity 2, the
multiset `{½, ½}`. That reproduces the audit's C1 row independently.

It additionally supplies data the audit did not carry: ramification index
`d = 2`, and the leading blocks `B₁,₂ = ±√(q−1)/q`. Those sharpen the
mismatch — C2's integral slopes `{−1,+1}` need no ramification at all, while
C1 requires index 2. A module needing ramification cannot be gauge-equivalent
to one that does not.

## Consequence for the c₃ front

The GGM eq-49 route to C1 is closed, in both directions and under all gauges.
Effort on the c₃ Stokes front should go to the routes that do not presuppose
that identification — `qou-odh5` (extract the two C1 Stokes multipliers via
q-Borel/theta resummation, ingredients now in hand) and `qou-0e66` (the
McPhail–Snyder diagrammatic state-sum route).

This does **not** touch the separate GGM-as-*source-of-data* beans
(`qou-bvgw` GGM Stokes dictionary extraction, `qou-8j0d` 4₁ index assembly):
using GGM's computed Stokes data as an external anchor is a different claim
from asserting the two modules are equivalent, and only the latter is excluded.
