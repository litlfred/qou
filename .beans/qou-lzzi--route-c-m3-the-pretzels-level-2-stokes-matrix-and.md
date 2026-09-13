---
# qou-lzzi
title: 'Route C M3: the pretzel''s level-2 Stokes matrix and the s(x) adjoint-weight test'
status: in-progress
type: task
priority: normal
created_at: 2026-09-13T17:46:35Z
updated_at: 2026-09-13T18:36:31Z
---

## Claimed 2026-09-13 — the OPERATOR route (branch `claude/pretzel-level2-stokes-2026-09-13`, PR #7333)

Distinct from PR #7152's residue/GZ-block route, which stalled at the level-2
FUSION rule (audit SS3k/SS3l: the index is the weight-1 component of an
epsilon-expansion at collided triple poles). This route never needs the fusion
rule, because it works upstream of the blocks.

**The construction.** GGM (187a)/(305a) build `S+(x;q)` from the fundamental
solution matrix `W_m(x;q)` of a linear q-difference equation ((332) for the
Theorem-28 family, (276) for 5_2). The q -> 0 Stokes entries are built from
that operator's q -> 0 characteristic roots, so deriving the pretzel's operator
answers the s(x) question directly.

**Derived here** (contour shift v -> v - ib + Faddeev's functional equation):
`P(X) = q^{A/2} w N(X) - X^A`, X = e^{2 pi b v} acting as the descendant shift.

| knot | N(X) coefficients | offsets |
|---|---|---|
| 4_1 | (1, (1+x)/q^{1/2}, x/q) | {x, 1} |
| 5_2 | (1, s(x)/q^{1/2}, s(x)/q, q^{-3/2}) | {1, x, 1/x} = adjoint weights |
| (-2,3,7) | degree 6, x only via sigma = x^{1/2} + x^{-1/2} | see below |

5_2 reproduces GGM (276) EXACTLY, and s(x) = x + 1 + 1/x is e1 = e2 of the
adjoint offset set -- that is the mechanism behind (188)/(307).
