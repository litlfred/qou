---
# qou-yaig
title: 'Take over qou-pdg9''s open orders: settle c2(4He) and c3 under Borromean'
status: completed
type: task
priority: normal
created_at: 2026-09-06T13:34:53Z
updated_at: 2026-09-06T14:10:19Z
---

## What this takes over, and from whom

PR #6931 (merged `fb13d307c7`) refuted the CENTRAL FINDING of #6559 — that the
ratio `c2.h^2 / c1.h` is monotone through 1 across `A` — and deliberately left
two things unsettled, both flagged as `qou-pdg9`'s call on their probe rather
than done unilaterally:

1. **`c2(4He)`** — the committed `P_OF["4He"] = 3`. One series order is lost to
   the 0/0 seminormal quotients, so `d.p = 2` and `d.coeff(2)` is unavailable.
   Every other case already has its `c2`. Without this one number, #6559's
   surviving claim *"the expansion crosses over between A = 3 and A = 4"* is
   **untested, not disproved**.
2. **`c3`** — not re-measured at all under Borromean, so #6607 is
   grouped-CONDITIONAL rather than refuted.

Owner instruction 2026-09-06 13:2x: *"Take over derivation and keep going."*

## Measured before running anything: `c2` has NO closed form

`c1` HAS one — `(a.Z + b.N)(2^-(A+1) - 2^-2A) - 4(i_pp - i_nn)2^-2A` — which is
how `c1(4He) = 7/128` was PREDICTED and then confirmed twice over (#6931). The
obvious move was to predict `c2(4He)` the same way. **It does not work, and this
was established rather than assumed.**

Exhaustive search over subsets of a 15-function basis
(`Z.D, N.D, dI.E, D, E, Z.E, N.E, A.E, A.D, ZZ.D, NN.D, ZN.D, ZZ.E, NN.E, ZN.E`),
requiring an exact fit to **all six** grouped values AND **all five** known
Borromean values: **ZERO subsets up to size 5.**

The quadratic terms were in the basis on purpose, not as padding. `tr_M`
factorises across the two nucleons (disjoint strand sets, #6919), which makes
the **log**-derivative additive at first order — so second order was expected to
carry a `phi_p.phi_n` cross term. **It does not fit either.** So `c1`'s
per-letter additivity is special to first order, there is nothing to predict
from, and the number has to be computed.

That negative is worth as much as the measurement it justifies: it says the
closed form does NOT propagate up the h_q expansion.

## Scope

Scope-(a) throughout: a statement about a series ordering in one braid-word
convention, not about the physics. And note that no value of `c2(4He)` restores
#6559's ARGUMENT — the Borromean column is `0.8174, 1.2385, INFINITE, 4.9045,
0.9722`, neither monotone nor ordered by `A`. Only its `A = 4` CONCLUSION is in
question here.

## Route for `c3`, once `c2` lands

Same producer, one order further: `c3` needs `a3`, hence `d.p > 3`. The five
small cases already sit at committed `P` values that reach it (`pp/pn/nn` at
`P = 6`, `T/3He` at `P = 5`); only `4He` would need `P = 5`, which is the
expensive one. So `c3` at `A = 2, 3` is cheap and `c3` at `A = 4` is not.


## MEASURED 2026-09-06 — item 1 settled, and the answer SPLITS

    c2(4He) borromean = 439/512      a0 = 7/128   a1 = 7/128   a2 = 411/512
    ratio c2.h^2 / c1.h = 1.5535     (295 s at P = 4, d.p = 3)

**The endpoint SURVIVES; the location does NOT.** #6559 said the expansion
"crosses over BETWEEN A = 3 and A = 4", which asserts two things:

- **ratio > 1 at A = 4** — TRUE, 1.5535, and by MORE than under grouped (1.4639).
- **ratio < 1 below** — FALSE. Under Borromean it is already 4.9045 at `T`
  (A = 3) and 1.2385 at `pn` (A = 2). There is no crossing THERE.

So the conclusion is right at its endpoint and wrong about where the crossing
happens, and the argument stays refuted (#6931). The full Borromean column:

    pp 0.8174   pn 1.2385   nn INFINITE   T 4.9045   3He 0.9722   4He 1.5535

**I caught my own over-claim in the probe's own output.** Its first verdict
printed "#6559's crossover CLAIM survives" — too generous, since it decides only
one of the two conjuncts. Fixed in the probe before the result was written up
anywhere else.

## The controls matter as much as the number

Three passed before the new value was trusted: `a0 = 7/128` against the derived
floor two ways, and `a1 = 7/128` against the `c1(4He)` measured in #6931.

That second one is worth naming: **#6931's own probe could only assert
`c1(4He) = 7/128` circularly** — it was the closed-form prediction fed back in as
its own target, and the PR body said so. This run reaches it by an independent
route (exact series at P = 4, no closed form involved) and gets the same value.
The circular row is now closed.

Also noted, unexplained: `a0 = a1 = 7/128` exactly at 4He under Borromean — the
classical floor and the leading coefficient coincide. Not claimed as meaningful.

## Item 2 (`c3`) — still open, and now better scoped

Same producer, one order further: `c3` needs `a3`, hence `d.p > 3`. The five
small cases already sit at committed `P` that reach it; only `4He` needs `P = 5`.
Given P = 4 cost 295 s and the per-order growth here is steep (the [8,4] and
[7,5] blocks alone were 50 s and 59 s at P = 4), P = 5 at n = 12 is the expensive
one and should be launched with the long-compute logging discipline.


## ITEM 2 MEASURED — and #6607's conclusion SURVIVES

    case  A   c1     c2       c3       c2h²/c1h    c3h³/c2h²
    pp    2   1/8    33/32    67/16      0.8174      0.4023
    pn    2   1/16   25/32    43/8       1.2385      0.6817
    nn    2   0      1/16     27/4       INFINITE   10.7008
    T     3   1/64   99/128   101/16     4.9045      0.8087
    3He   3   1/8    157/128  839/128    0.9722      0.5295
    4He   4   7/128  439/512  (P=5)      1.5535      (open)

5/5 controls passed — every case reproduced its recorded c0, c1 AND c2 first.

**Read the two ratio columns TOGETHER; neither says it alone.** First -> second
order overtakes (four of five finite ratios at or above 1). Second -> third does
NOT (four of five well below 1). So this is not a divergent expansion with each
order beating the last — it has ONE BAD ORDER, the second, after which terms
resume shrinking.

That is exactly the shape #6607 concluded from the grouped word (its 4He ratio
was 247.98·h/29.8965 = 0.8219, likewise below 1). **So #6607's conclusion
survives the ordering change at the A reached here.**

Three documents, three different fates, which is worth keeping straight:

    #6559  argument REFUTED (#6931); crossover LOCATION false; ENDPOINT survives
    #6607  conclusion SURVIVES at A = 2, 3; A = 4 still open
    #6931  its own "A=4 untested" bullet now superseded by the measurement

`nn` is the outlier at BOTH orders (INFINITE, then 10.7008) for one reason:
`c1(nn) = 0` exactly. A case whose first order vanishes has no scale for later
orders to be measured against — read it out of the trend, not into it.

## What stays open

- **`c3` at A = 4**, which is where #6607's interest lies. Needs `P = 5` against
  a committed `P_OF` of 3 — a separate long-compute run, deliberately not buried
  in a five-case sweep.
- **`c4`**, which `pp/pn/nn` could supply at their committed `P = 6`, was not
  extracted. Five points across two `A` is a shape, not a convergence proof.


## COMPLETE — both takeover items settled, plus the two gaps they exposed

    case  A   c1     c2       c3        c4         c2/c1     c3/c2     c4/c3
    pp    2   1/8    33/32    67/16     -585/128   0.8174    0.4023   -0.1081
    pn    2   1/16   25/32    43/8       109/192   1.2385    0.6817    0.0105
    nn    2   0      1/16     27/4        27/32    INFINITE 10.7008    0.0124
    T     3   1/64   99/128   101/16    (P=6)      4.9045    0.8087    —
    3He   3   1/8    157/128  839/128   (P=6)      0.9722    0.5295    —
    4He   4   7/128  439/512  1329/256  (P=6)      1.5535    0.5999    —

30 controls across four probes; every case reproduced every already-recorded
coefficient before its new one was read.

**#6607's conclusion HOLDS at its own headline case.** `c3(4He) = 1329/256`,
ratio 0.5999 < 1 (352 s at P = 5). Its grouped 4He ratio was 0.8219, likewise
below 1 — so the conclusion is robust to the convention change even though the
numbers moved.

**The c3 column has NO A trend**: 0.4023, 0.6817, 0.8087, 0.5295, 0.5999 across
A = 2, 3, 4 — flat in the 0.4-0.8 band. That is sharper than "comparable": the
ratio is not drifting toward 1 as A grows.

**The settling is a trend, not a fluctuation.** c4 at A = 2 gives |c4/c3| of
0.011 and 0.012 — about forty times smaller than the c3/c2 step. So the picture
is: overtakes once at order 2, shrinks at 3, collapses at 4.

Recorded, not built on: pp's c4 = -585/128 is the first NEGATIVE coefficient in
the family (one sign, one order, one A); and nn behaves at order 4 despite being
the sole outlier at orders 2 and 3, so its c1 = 0 degeneracy washes out.

## Still open, and named rather than quietly closed

- **c4 at A = 3 and A = 4** — needs P = 6 at n = 9 and n = 12. Not attempted.
- **c5 and beyond** — nothing here bounds them. Four orders at one A is a shape.
- **Grouped c3 at A = 2, 3 was never re-derived**, so the row-by-row
  grouped-vs-Borromean comparison that exists for c2 does not exist for c3.


## c4 COMPLETE at all three A — and the trend reading needs care

465 s at P = 6, twelve controls (four per case), every case reproducing its
recorded c0, c1, c2, c3 before its c4 was read.

    case   A        c4       c4h⁴/c3h³
    pp     2  -585/128        -0.1081
    pn     2   109/192         0.0105
    nn     2     27/32         0.0124
    T      3   743/384         0.0304
    3He    3 10001/1536        0.0984
    4He    4 43079/6144        0.1338

**Every A collapses**, so the one-bad-order shape is a property of THE EXPANSION
rather than an artefact of the two-nucleon case — which is exactly what the
A = 2 result alone could not establish, and why this run was worth doing.

**🛑 But there is NO clean A trend, and the column invites one.** The magnitudes
look like they rise with A (0.0105, 0.0124 -> 0.0304, 0.0984 -> 0.1338). They do
not support it: the scatter WITHIN A = 2 is as large as the variation ACROSS A.

    within A = 2   0.0105 .. 0.1081   10.3x
    across all A   0.0105 .. 0.1338   12.7x

pp alone (-0.1081) exceeds both A = 3 values in magnitude and is comparable to
A = 4's. So the honest statement is scatter in a band below ~0.14 with no clean
A dependence. That differs from the c3 column, which is genuinely FLAT
(0.4023 .. 0.5999) rather than merely trendless-with-scatter — a distinction
worth keeping, since "flat" and "no detectable trend given the scatter" are not
the same claim.

pp's c4 is also the only negative coefficient in the family, and it is what
breaks the apparent trend — so it is doing real work in the argument and must
not be dropped as an outlier.

## Now genuinely closed

Every gap this bean named is measured: c2(4He), c3 at all six cases, c4 at all
three A. What remains unbounded by anything here is c5 and beyond, which would
need P >= 7 throughout.

## 🛑 RETRACTION 2026-09-07 — "nothing to predict from" was WRONG

This bean concluded, from a zero-fit exhaustive search, that `c2`'s per-letter
additivity does not propagate and "the number has to be computed". PR #6966
carried that further: "c1's per-letter additivity is special to first order and
does not propagate up the expansion."

**A closed form for `c2` exists.** `atom_bond_product_closed_form_probe.py`
(bean `qou-qqm4`, `369f4bb0a7`, landed while #6966 was open) gives

    tr(atom) = PROD_nucleons a(1 + r.e + q.e^2)
             * PROD_bonds  (1/2)(1 + rho_b.e + tau_b.e^2)

reproducing **c0, c1 AND c2 for A = 2..5, 9/9, no free parameter**. Verified by
running it here rather than trusting the commit message: `9/9 — c0, c1 and c2
all reproduced`.

**The measurement I made is fine; the conclusion I drew is not.** The zero-fit
result stands exactly as measured — there is no closed form in a `(Z, N)` basis.
But my basis contained no bond variable, so it could not have found this form
however many subsets it enumerated, and **a negative about a basis is not a
negative about the quantity**. Multiplicativity does propagate to second order;
it propagates over BLOCKS and BONDS rather than per letter.

This is the scope-(a)/(b) failure AGENTS.md is strict about, committed by an
agent who quoted that very discipline in the same PR: I had scope-(a) evidence
(this construction, in this basis, does not fit) and wrote something that reads
scope-(b) (the quantity has no closed form).

**`c2(4He) = 439/512` is unaffected and is now INDEPENDENTLY CORROBORATED** —
their 9/9 covers 4He. Two routes, same number.

Their form has its own limits: sorted orderings only, orders 0-2, `A <= 5`, not
proved. So `c2` is not "solved" — but it is decisively more than "nothing to
predict from".

## THE PRODUCT REACHES c3 TOO (2026-09-07) — 8/8

The retraction above asked the obvious next question: qou-qqm4's block-and-bond
product stops at order 2 because each factor is a quadratic. Does it carry `c3`?

**It does.** Add one cubic per factor and change nothing else:

    nucleon   a(1 + r.e + q.e^2 + s.e^3)      s_p = 75/4    s_n = 19
    bond      (1/2)(1 + rho.e + tau.e^2 + ups.e^3)   ups_pp = -1/2

    case   A     a3 (raw)    c3 = a2+a3    source
    pp     2       105/32         67/16    live
    pn     2       149/32          43/8    live
    nn     2       107/16          27/4    live
    3p     3     1717/256      2109/256    live
    T      3      711/128        101/16    live
    3He    3       349/64       839/128    live
    3n     3         51/8        219/32    live
    4He    4     2247/512      1329/256    RECORDED, independent
    5He    5      675/256     6393/2048    prediction, no target

**8/8, no parameter fitted to any c3.** The five new parameters were measured
exactly where the originals were — `s` on a ONE-NUCLEON free word at n = 3,
`ups_b` on a ONE-INTERFACE word at A = 3 — so every multi-interface row is a real
test.

**The 4He row is the one that counts.** `c3(4He) = 1329/256` was measured in this
same bean by a 352 s exact series at P = 5, before this form was extended, and
4He contributes to no input here. Two completely different routes, same rational.

**A cross-check that the extension is honest**: my order-3 bond measurement gives
`bond pp = (1/2)(1, 2, 1/2, -1/2)`, whose first three entries reproduce
qou-qqm4's recorded `(1/2)(1, 2, 1/2)` exactly. I am extending their object, not
re-parameterising it.

## What this settles about my retracted claim

#6966 said multiplicativity is "special to first order and does not propagate up
the expansion". It propagates to order 2 (qou-qqm4) and now to order 3 (here).
The claim was not merely mis-scoped — it was wrong in the direction that matters,
and each order measured since has made it more wrong. Worth recording plainly.

## Scope — inherited, and NOT weakened here

SORTED orderings only; A <= 5; NOT PROVED. `pnp` remains the discriminating
untested case. This extends the ORDER reach, not the ORDERING reach, and says
nothing about whether the product survives an unsorted word.

`c4` is the next rung and is untested by this: it would need a quartic per
factor, and nothing here indicates whether the pattern continues or stops.

## PRE-REGISTERED 2026-09-07 08:45 UTC — before the nn quartic was measured

The bond rows, as measured, written (1/2)(1, rho, tau, ups, chi):

    pp   (1,  2, 1/2, -1/2, 1/4)
    pn   (1,  0, 3/2, -3/2, 31/12)
    nn   (1, -2, 5/2, -5/2, ?)      <- chi still measuring

`rho = p_b - n_b` and `tau = 1/2 + n_b` hold in all three (qou-qqm4's pattern).
`ups = -tau` holds in all three — three hits, no freedom left, and NOT predicted
by that description.

**The falsifiable part.** Fitting `chi` on the two bonds that have it:

    linear in n     chi = 1/4 + (7/3)n        ->  chi_nn = 59/12
    linear in tau   chi = -11/12 + (7/3)tau   ->  chi_nn = 59/12

🛑 **THOSE ARE NOT TWO INDEPENDENT RULES AGREEING.** `tau = 1/2 + n` is itself
linear in `n`, so both are the SAME two-parameter family relabelled, fitted to
two points, with zero degrees of freedom left over. Their agreement is an
identity, not evidence. Recording that explicitly because "two different rules
give the same answer" is precisely how a 2-point fit gets mistaken for a
derivation, and this bean has already had to retract one over-reading.

**So `chi_nn = 59/12` is a prediction with no support behind it beyond the fit.**
It is written down here BEFORE the measurement so the running `nn` extraction can
falsify it on arrival, rather than being "explained" afterwards. If `chi_nn`
comes back anything else, this family is dead and the quartic has structure the
cubic did not.

The `ups = -tau` relation is the one worth watching: it was NOT fitted — it fell
out of three independent measurements — so if a quartic analogue exists it should
be visible without tuning.

## PREDICTION REFUTED 2026-09-07 09:20 — as pre-registered, and that is the point

    bond nn:  (1/2)(1, -2, 5/2, -5/2, 9/4)      chi_nn = 9/4

**Predicted 59/12 (= 4.917). Measured 9/4 (= 2.25).** The linear-in-n /
linear-in-tau family is dead. It was written down before the measurement
precisely so it could die this way rather than be quietly replaced by whatever
the number turned out to fit.

**The quartic column is not even monotone:**

    pp   1/4      pn   31/12      nn   9/4
         0.25          2.583           2.25

So `chi` rises then falls across the bonds. No linear rule in `n`, `tau`, or
anything else two-parameter can produce that, and I will not go looking for a
three-parameter one — three points and three parameters is not a finding.

**`ups = -tau` SURVIVES, 3/3.** `ups_nn = -5/2` against `tau_nn = 5/2`. The
relation that was NOT fitted holds; the one that WAS fitted broke. That
asymmetry is the only thing here worth carrying forward.

## 🛑 AND I FOUND A DEFECT IN MY OWN PROBE, mid-run

At `K = 4` the table printed headers `a4` / `c4` over values that were `a3` /
`c3`: lines 251, 260, 269 and 270 hardcoded indices 2 and 3 rather than
`K-1` and `K`. This is the SAME mislabelling class I fixed in this file
yesterday, reintroduced one commit later in code I wrote to avoid it.

**The verdict is unaffected and the run is not wasted.** The failure check
compares the FULL coefficient vector (`if d_pred != d_live`), so an order-4
disagreement is still caught — it is the display and the per-row flag that were
wrong, not the test. Fixed to derive both indices from `K`; `K = 3` is unchanged
(`K-1, K` = 2, 3), so #7002's merged result is untouched.

The nn row is now in the `K = 4` input cache, so the corrected table can be
regenerated without re-earning the 2.7 h of bond measurement — which is exactly
what that cache was added for, one commit before it was needed.

## DERIVED 2026-09-07 — and the derivation DEFLATES my own claim from an hour ago

Owner asked to try deriving the recursion. It derives, and what it shows is that
there was less there than I said.

**k=1 is an algebraic identity.** A bond joins exactly TWO nucleons, so
`p_b + n_b = 2` always. With qou-qqm4's `rho = p - n` and `tau = 1/2 + n`:

    n = 1 - rho/2   =>   tau = 1/2 + (1 - rho/2) = 3/2 - rho/2

and the measured k=1 rung is `tau = -1/2*rho + 3/2`. The same statement. Nothing
new was found there.

**The general version kills the "overdetermined" framing outright.** Indexing the
bonds by `n = 0, 1, 2`:

    c0  [1, 1, 1]              2nd diff 0        AFFINE in n
    c1  [2, 0, -2]             2nd diff 0        AFFINE
    c2  [1/2, 3/2, 5/2]        2nd diff 0        AFFINE
    c3  [-1/2, -3/2, -5/2]     2nd diff 0        AFFINE
    c4  [1/4, 31/12, 9/4]      2nd diff -8/3     NOT affine

If three coefficients are all affine in `n`, the three bonds are COLLINEAR in
that 3-space and a 2-term relation exists AUTOMATICALLY. **The third equation is
not independent of the other two**, so "3 equations, 2 unknowns, overdetermined,
therefore a real test" was wrong. I wrote that in commit `8bf62d2ad6` and it is
corrected before merge.

It also explains the break for free: k=3 fails because `c4` is the FIRST
non-affine coefficient. Not a surprise to investigate — a consequence.

## What actually survives

    k=1   DERIVED, identity from rho, tau, p+n=2
    k=2   NOT derived — equivalent to  ups = -tau  — still OPEN
    k=3   REFUTED — c4 is the first non-affine coefficient

`ups = -tau` is the one real fact. `c3` being affine in `n` at all is a genuine
constraint on three measured rationals, and it is NOT supplied by qou-qqm4's
description, which covers `rho` and `tau` only — correctly called there "three
values with one spare dof". This is a relation with none.

**A guess that fails, recorded so it is not re-tried.** `tau, -tau` at orders 2
and 3 suggests a factor `tau*e^2/(1+e)`, whose order-4 term would be `+tau`, i.e.
`c4 = 1/2, 3/2, 5/2`. Measured is `1/4, 31/12, 9/4`. Refuted.

**And what is NOT a finding:** `c4` is quadratic in `n` by construction — any
three points are — so fitting a quadratic there has zero content. Not done.
