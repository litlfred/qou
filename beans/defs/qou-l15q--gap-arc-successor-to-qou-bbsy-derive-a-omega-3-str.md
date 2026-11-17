---
# qou-l15q
title: 'GAP (arc successor to qou-bbsy): derive A_omega = 3 structurally. W3 certified A_omega is the Stokes SYMMETRY CONSTANT (S12+S21 = 3*S11, exact q-series identity, Lean StokesSymmetryConstant). Deriving the integer 3 from the categorical drivers is open. TWO competing structural candidates, both fitting 4_1, SHARPLY SPLIT on 5_2 -- a clean discriminating test: (A) |disc(trace field)|: 4_1 -> |-3| = 3 (Lean-proved in CuspShapeBarParity: (barOdd omega)^2 = -3); 5_2 -> |-23| = 23 (Lean-proved in FiveTwoSaddleCurve: cubic y^3-2y^2+3y-1, disc -23). (B) |middle coefficient of the Alexander polynomial|: Delta_41 = -t + 3 - 1/t -> 3; Delta_52 = 2t - 3 + 2/t -> 3. So A predicts 23 for 5_2 and B predicts 3. TEST: compute the 5_2 Stokes symmetry constant c in S12 + S21 = c*S11 from GGM 2012.00062 section 6 (corpus already has 5_2 Stokes work: qbeta-5two-stokes-barodd-index, qbeta-5two-stokes-population-bridge, fivetwo_saddle_values). c = 23 confirms A; c = 3 confirms B; anything else kills both. NOTE the guard discipline: 5_2 entry series are pre-asymptotic below ~q-order 1200 at the substrate -- use a multi-cut ladder, diff >= 1 means ZERO digits. Anti-fit: this is a structural identification test with a falsifiable prediction, NOT a fit; if neither matches, report the negative.'
status: in-progress
pr: 8236
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T20:20:55Z
updated_at: 2026-11-17T06:55:00Z
parent: qou-avtq
---


## 2026-08-01 TEST RE-SCOPED before running (corpus read first)

The 4_1 -> 5_2 test as designed is ILL-POSED. The corpus already carries
the 5_2 Stokes machinery (qbeta_5two_stokes_barodd_index_probe.py, GGM
section 6): the 5_2 Stokes matrix is **3x3**, q->0 limit
[[1,4,0],[0,1,0],[-3,-9,1]] (eq 100a), with THREE off-diagonal integers
(4, -3, -9) -- versus 4_1s 2x2 [[1,3],[0,1]] with ONE (3). Rank tracks the
trace-field degree (4_1 quadratic, 5_2 cubic). So:

  * there is no single 5_2 Stokes constant to compare against 23 or 3;
  * the symmetry eq (65) that gave the 4_1 identity is a rank-2 statement
    with no 3x3 analogue -- GGMs 5_2 structural relation is the inversion
    S+^T S- = 1, which constrains a matrix PAIR, not an integer.

23 does not appear among {4,-3,-9}, but that is NOT a refutation of
candidate A (the predicted quantity is undefined here). 3 does appear as
|-3|, but that is NOT support for candidate B -- picking one of three
integers post hoc is numerology. Both candidates remain UNTESTED.

NEXT (recommended, route 3 of the scope note): re-run the same falsifiable
test on a different RANK-2 knot -- quadratic trace field, so the Stokes
constant is well-defined exactly as for 4_1 -- chosen so that
|disc| != |Alexander middle coeff| and the candidates still separate.
Cheapest well-posed route; does not require closing the rank>2 channel gap.

Scope note: docs/scope/2026-08-01-aomega-three-test-illposed.md

## 2026-08-01 ADDENDUM: route 3 (another rank-2 knot) is ALSO blocked

Rank 2 = quadratic imaginary invariant trace field. For knots in S^3 that is
essentially 4_1 alone: Reid (1991), 4_1 is the unique arithmetic hyperbolic
knot -- already cited in-corpus (hyperbolic-volume-transcendence.md,
three-knot-jet-order-independence.md). Strictly Reid gives arithmetic => 4_1,
and quadratic-imaginary => arithmetic needs integral traces, so it is NOT a
theorem that no second rank-2 knot exists -- but NO KNOWN CANDIDATE exists in
the corpus or the standard census. Route 3 has nothing to run on. Recorded as
no-known-candidate, not as a proved exclusion.

Available at rank 2 are LINKS, not knots: Whitehead and Borromean, both with
invariant trace field Q(i), |disc| = 4, both already in corpus compute
(2026-07-26-whitehead-vc-verification-and-p-exponent.md / #4400;
borromean_3d_index.py). Candidate A predicts 4 for each.

BUT that test degrades to ONE-SIDED and must not be sold as more:
  1. Candidate B is INAPPLICABLE -- links have multivariable Alexander
     polynomials, so "the middle coefficient" needs an extra choice. The test
     therefore cannot adjudicate A vs B, which was the entire point.
  2. Rank-2-ness of their Stokes matrices is PLAUSIBLE BUT UNVERIFIED (rank is
     the number of boundary-parabolic reps, not directly the field degree).
  3. A "4" is CONFOUNDED: 5_2's q->0 integers already contain a 4, and small
     integers recur; support for A would need the coincidence controlled.

RECOMMENDATION: do NOT run the link test as an adjudicator. The arc needs the
principled route first -- derive WHICH matrix element the T5 A_omega is (the
same channel gap #4447 recorded on the 4_1 side, where A_omega is sigma1sigma2
but the proven x-refinement is sigma1sigma1). That would define the rank-3
generalization and re-open 5_2, which is the better test anyway.

STATUS: "why 3" has NO cheap well-posed test. The arc is blocked on a
DERIVATION, not on compute. Scope note:
docs/scope/2026-08-01-aomega-three-test-illposed.md (Addendum).


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** disc

Evidence: The rank-2 identity is a tautology (finding 2). The bean body omits commit `9f527376a9` (2026-08-01). That commit found the rank-3 transcription is not constant (1.56–4.08) and that both candidates (

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

## 2026-11-17 — Round 52 formalization & probe witness (PR #8236, status: in-progress)

- [x] PR #8236 (`62b8fce5d1e824cf9dd59a1d9845d15631382086`): formalized `candidate_a_vs_b_degeneracy_and_fivetwo_split` and `stokes_rank_two_vs_rank_three_entry_count` in `QOU/QBeta/StokesDiagonalVsOffDiagonalAndCrossKnotSplit.lean` (`0 sorry`, `0 axiom`, `0 vacuity`), proving Candidate A (`|disc|`) and Candidate B (`|Delta middle coeff|`) coincide at `4_1` (`3 = 3`) and split by `20` at `5_2` (`23 != 3`), with `23` absent from `5_2` off-diagonal Stokes entries.
- [ ] Awaiting Merge Manager integration and owner review (kept `in-progress` per no-unilateral-closure policy).
