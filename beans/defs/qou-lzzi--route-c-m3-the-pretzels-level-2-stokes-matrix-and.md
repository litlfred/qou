---
# qou-lzzi
title: 'Route C M3: the pretzel''s level-2 Stokes matrix and the s(x) adjoint-weight test'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T17:46:35Z
updated_at: 2026-11-17T11:58:00Z
parent: qou-v2om
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

## Next step for whoever picks this up

The RING is fixed; the MATRIX is not. The single missing input, named precisely so
it is not re-derived as something else:

  the four region matrices M_R(x;q), R in {I,II,III,IV}, for the pretzel --
  equivalently the constant A, B in GL(6, Z[x^{+-1/2}]) of the analogue of
  GGM (305a).

That is a NORMALISATION, not new q-series data: the blocks are already derived
(PR #7152 SS3k, six families validated to 7.8e-19) and the operator is derived here
(PR #7333). Two routes to it:

  1. Borel-resum the six asymptotic series in each of the level-2 sectors and read
     M_R off the linear combinations, as GGM do in their SS5.5 / SS6.5 numerics.
  2. Close the level-2 FUSION rule (the open item of SS3l) -- the u-deformation of
     GZ's epsilon-derivative at the collided triple poles -- which gives the blocks
     in GGM's normalisation directly.

Route 2 is the one PR #7152 is already on, so this arc and that one converge there.

Do NOT expect the sigma_1 sigma_1 entry to settle it: by the Z/2 grading, that entry
lives entirely in the integer-q sector, which is exactly the part that is in Z[s(x)]
anyway.

## Gate correction (2026-09-13) — recorded because the mechanism generalises

The degree-6 integral gate FAILED first time: rel_residual = 1.0, |Z| ~ 1e+115.
The bug was in the GATE's convergence window, not the operator.

I wrote the condition from the QUADRATIC coefficient only:
  -(r_eff - A) eps < Im t' < A eps,  r_eff = sum alpha_j^2.
Each Phi_b(alpha_j v + beta_j) ~ exp(pi i (alpha_j v + beta_j)^2) also has a LINEAR
coefficient 2 pi i (lin + t') with lin = sum_j alpha_j beta_j, so +inf needs

    (r_eff - A) eps + Im t' + Im lin > 0 .

For 4_1 (beta = (u,0)) and 5_2 (beta = (0,u,-u)) lin is REAL, so both gates that
passed were accidentally right and hid it.  For the pretzel beta = (u/2,-u/2,-c_b),
alpha = (1,1,2), so lin = -2 c_b: the DOUBLED factor's -c_b shift grows like
exp(-4 pi i c_b v).

Fixed and re-run: rel_residual 1.0 -> 4.098e-21 and 1.0 -> 6.483e-19, with measured
Im lin = -2.31421 / -2.02254 against -2 Im c_b = -2(1.15710) / -2(1.01127) --
confirmed to every printed digit.  |Z| back to 7.07 / 11.40.

TWO THINGS WORTH CARRYING:
 - At k = 0, t_I = 0 the corrected condition reduces to eps > Im(c_b)/2, which is
   EXACTLY the constraint SS3k of PR #7152 states for this integral.  Independent
   recovery, opposite direction.
 - A gate passing on the two knots where the answer is known is NOT evidence the
   gate is right for the third.  The feature that makes the pretzel interesting --
   a complex shift inside a dilogarithm -- is the one 4_1 and 5_2 cannot test.

Nothing in the s(x) verdict moved; the operator and every symbolic gate were
untouched (G3 validates the operator pointwise at 2.2e-29 regardless).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 89 Progress (`litlfred/qou#8334`)
- **Lean 4.24.0 Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/QuantumIntegerRatioAndLevelTwoStokesBrick.lean` (`0` `sorry`, `0` `axiom`, `0` warnings; `0` CRITICAL, `0` major, `0` advisory across all directory-mode static audits).
- **80-dps Probe & Witness**: `computations/probes/quantum_integer_ratio_and_level_two_stokes_brick_probe.py` & `computations/probes/quantum-integer-ratio-and-level-two-stokes-brick.witness.json` (`scriptCommitSha = 4d6630423af48b31069a83d2407a32bd592eec79`, HEAD `c9d68807b57ef2cf531ca6340ce9802c12bf8d5d`, `allPassed = true`).
