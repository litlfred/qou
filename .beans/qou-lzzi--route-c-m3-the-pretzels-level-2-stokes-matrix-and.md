---
# qou-lzzi
title: 'Route C M3: the pretzel''s level-2 Stokes matrix and the s(x) adjoint-weight test'
status: in-progress
type: task
priority: normal
created_at: 2026-09-13T17:46:35Z
updated_at: 2026-09-13T18:46:02Z
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

## Result (2026-09-13) — s(x) VERDICT: NO; it is sigma = s(x^{1/2}) - 1

**The mechanism.** Newton polygon of `N(X)` in q; leading polynomial per segment.

| knot | segments (roots @ slope) | leading polynomial | roots |
|---|---|---|---|
| 4_1 | 2 @ -1/2 | `(Y+1)(xY+1)` | -1, -1/x |
| 5_2 | 3 @ -1/2 | `(Y+1)(Y+x)(Y+1/x)` | -1, -x, -1/x |
| (-2,3,7) | **2 @ -1, then 4 @ -1/2** | `-(Y^2-1)`; `(Y^2-1)(Y^2+sigma Y+1)` | +-1; +-1, -x^{1/2}, -x^{-1/2} |

So `s(x) = e1 = e2` of 5_2's pole-offset set {1, x, 1/x} — the ADJOINT WEIGHT SET.
That is why s(x), and only s(x), appears in GGM (188)/(307). It is not an ansatz.

**Pretzel.** The polygon splits 2 + 4 across a q^{1/2} step — the level-2 signature,
derived from the state integral with nothing else assumed — and the x-dependent
exponents are the adjoint weights of the SQUARE ROOT: `sigma = x^{1/2} + x^{-1/2}`.

`sigma^2 = s(x) + 1`, and `Y^2 - (S+1)` is irreducible over Q(S): a **degree-2
extension of Z[s(x)]**. An exact Z/2 grading (invariance under the simultaneous flip
(q^{1/2}, x^{1/2}) -> (-q^{1/2}, -x^{1/2})) makes sigma-parity = q-half-integrality,
so **entries at INTEGER powers of q DO lie in Z[s(x)]** — which is why the parent
session's derived sigma_1 sigma_1 index is a polynomial in s(zeta) with integer
zeta-powers — and half-integer ones do not. Level 2 and the quadratic extension are
one phenomenon.

**Degree 6 = rank 6**, derived independently of Garoufalidis-Zagier: two from the unit
dilogarithms, four from the doubled `Phi_b(2v - c_b)` (it shifts by -2ib).

**STILL OPEN (scope a).** This fixes the RING, not the explicit matrix. GGM fix the
GL(r) normalisation per knot ((186a)-(186d)/(94a)-(94d) -> (187a)/(305a)); no held
source prints the analogue for a rank-6 level-2 knot. That is the precise missing
input, and it is a normalisation, not new q-series data.

Audit: `docs/audits/2026-09-13-pretzel-level2-stokes-matrix.md`. PR #7333.
