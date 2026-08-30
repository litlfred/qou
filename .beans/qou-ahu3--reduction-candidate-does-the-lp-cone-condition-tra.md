---
# qou-ahu3
title: 'Reduction candidate: does the LP cone condition track -P_76, and via what orderings-to-NF map?'
status: todo
type: task
priority: normal
created_at: 2026-08-30T14:30:58Z
updated_at: 2026-08-30T14:52:52Z
---

NEXT TRANCHE, opened 2026-08-30 after PR #6095 merged (d43f261ed1).

WHERE THIS COMES FROM. prop:toffoli-lp-stability's proof reduces feasibility of
G.t >= 0 to "the positivity of P_77 . W_std with the appropriate sign from" the
flip amplitude. Two things are now established about that step:

  1. P_77 * W_std > 0 for every q > 0 -- proved, toffoliDiagonal_mul_wStd_pos.
     The first factor never obstructs; everything at issue is the off-diagonal.
  2. A sign-INHERITING reduction is structurally excluded -- proved,
     toffoliFlip_mul_coneCoord_nonpos: sign P_76 = -sign t_(0,1) identically,
     because P_76 = -hbar * S/(2(q^2+1)^2) with S > 0 on all of R.

So the surviving candidate is a reduction with a NEGATIVE proportionality: the
cone condition tracking -P_76 rather than P_76.

THE TWO QUESTIONS, in order.

(a) Does it track? Measured so far only at q0 and only for the 8 orderings
    (probe toffoli_nf_coordinates_and_lp_feasibility.py): G.t >= 0 held in all
    8, and 2 of those trivially (G is entrywise non-negative and t is too for
    the all-proton ordering). That is one anchor. Sweep q over (0,1) and
    (1,inf) and check whether the componentwise sign pattern of G.t follows
    -P_76 across q = 1. If it does not, the negative-proportionality candidate
    dies too and the reduction has no surviving form.

(b) Via what map? This is the harder half and it is the ORIGINAL gap. G.t is a
    6-vector over the Hecke NF basis [(), (0,), (1,), (0,1), (1,0), (0,1,0)];
    P_77/P_76 are entries of an 8x8 matrix indexed by strand-type orderings
    (decode(k), 2^3 = 8). No map between the index sets is recorded anywhere.
    The natural candidate: each ordering k determines an element
    T_q(k) = prod_i (a_i sigma_i + b_i) in H_3(q) whose NF coordinates are
    computable (the probe already does this), and the 8x8 entries are built
    from traced volumes of those same chains -- so the map, if it exists, runs
    ordering -> element -> NF coordinates, and the 8x8 is a matrix of Markov
    traces rather than a change of basis. Whether the cone condition on the
    NF side has ANY expression in terms of the 8x8 entries is exactly what is
    unproved.

WATCH OUT. markov_trace(ordering) in the recorded construction is prod_i V_i --
a PRODUCT OF TRACES, not the trace of the product. tr_M is not multiplicative
across sigma_0 and sigma_1 (they do not commute), so that step is itself an
assumption worth checking before building anything on top of it. It may be the
real defect.

FORMALIZE-FIRST applies: before sweeping q widely, look for an invariant that
prunes. The sign identity above is the precedent -- it killed the whole
sign-inheriting family in two lines.


## RETRACTED 2026-08-30 — the multiplicativity hazard is refuted, by me

The "WATCH OUT" above flagged markov_trace(ordering) = prod_i V_i as a product
of traces rather than the trace of the product, and called it possibly "the
real defect". It is not a defect at all, and the flag is withdrawn.

The factorisation follows from the DEFINING MARKOV PROPERTY alone --
tr(x . sigma_last) = z tr(x) -- with no convention, no anchor and no extra
assumption. For chain elements x = a s0 + b and y = c s1 + d:

    tr(x y) = ac tr(s0 s1) + ad tr(s0) + bc tr(s1) + bd tr(1)
            = ac z^2 + ad z + bc z + bd          [Markov, twice]
            = (z a + b)(z c + d) = V_0 . V_1

The chains are built generator-by-generator in INCREASING index order, which is
exactly the shape the Markov property handles. Non-commutativity of s0 and s1
is irrelevant because the property is applied to the last generator each time.

MEASURED: all 8 strand-type orderings agree, symbolically in BOTH q and z, so
it is neither a convention artefact nor an anchor coincidence
(computations/probes/toffoli_markov_factorisation.py). The NF word (0,1,0)
never occurs in any T_q, so no unproven trace value enters the comparison --
checked, not assumed.

PROVED sorry-free: QOU.Information.tracedVolume_product_eq_trace_of_markov,
stated with the trace values as HYPOTHESES so it is a theorem about the Markov
property rather than about any convention.

CONSEQUENCE FOR THIS TRANCHE. The cheap decisive check I put first has come
back clean, so it does NOT collapse the tranche. The construction is sound and
question (b) -- the orderings-to-NF map -- is unaffected and remains the hard
half. Question (a), whether the cone condition tracks -P_76 across q = 1, is
untouched and is now the next thing to measure.

This also removes a reason to distrust the 8x8: its entries are honest Markov
traces of honest H_3(q) elements. What is still missing is a relation between
those entries and the 6-dimensional cone condition, not a fix to the entries.


## MEASURED 2026-08-30 — question (a) answered: the candidate is REFUTED

The negative-proportionality candidate predicted feasible <-> -P_76 > 0 <-> q > 1.
Measured across the threshold (probe toffoli_cone_threshold.py):

    q <= 0.8   infeasible    -P_76 < 0     consistent
    q = 0.9    FEASIBLE      -P_76 < 0     CONTRADICTS
    q = 0.95   FEASIBLE      -P_76 < 0     CONTRADICTS
    q >= 1.05  feasible      -P_76 > 0     consistent

The cone condition DOES have a threshold -- but at q ~ 0.8945, strictly below
1, while -P_76 changes sign exactly at 1. So no reduction of the cone condition
to the sign of P_76 holds, with EITHER proportionality. Question (a) is closed
negative, and with the sign-inheriting form already excluded by
toffoliFlip_mul_coneCoord_nonpos, the reduction as the proof states it has no
surviving form.

## A POSITIVE FINDING: exactly ONE constraint governs

Of the six components of G.t, five stay strictly positive across the threshold.
Only row 5 -- the NF word (0,1,0) = sigma_0 sigma_1 sigma_0, the LONGEST word --
changes sign. So the LP cone condition for the q-Toffoli is a SINGLE
inequality, not six. That is new and is the natural handle on question (b): a
map to the 8x8 only has to explain one constraint.

## THE THRESHOLD'S EXACT VALUE IS UNDETERMINED, and I nearly claimed otherwise

q_c ~ 0.894480292910614763779 (about 50 trustworthy digits).

PSLQ at degree 10 returns [1,0,-1,0,1,0,-1,0,0,0,-1], i.e.
1 - q^2 + q^4 - q^6 - q^10, evaluating to ~5e-51 at q_c. DO NOT QUOTE IT.
AGENTS.md's entropy bound puts degree 10 at ~58 digits needed and there are
~58 available, so there is no headroom and the hit is not evidence. Degrees 2
through 8, which do have headroom, return nothing.

TWO ERRORS OF MINE ALONG THE WAY, both from the same cause:
  - I first read the degree-10 hit as the answer.
  - I then "REJECTED" it after a dps-160 run -- but the residual was IDENTICAL
    to the dps-80 run (-1.50343e-51 both times), because
    pyhecke.gram.gram_matrix_mp SATURATES near 60 digits: its Markov weights
    are built at _GRAM_MP_DPS = 60, and its dps=80 and dps=160 outputs are
    bit-identical. Every digit past ~58 was noise, so the rejection rested on
    noise just as the acceptance had.
Neither verdict stands. The honest state is UNDETERMINED.

## WHAT WOULD SETTLE IT

A symbolic Gram in q. Then row 5 gives the threshold as the root of an explicit
polynomial with no PSLQ involved. Blocker: that needs a GENERAL H_3 normal-form
multiplication. The `mul` in toffoli_nf_coordinates_and_lp_feasibility.py was
written for products of the shape (a s0 + b)(c s1 + d) and raises on (0,1,0,1),
which the full 6x6 Gram requires. Either extend it (braid + quadratic relations
to NF) or use pyhecke's own reducer with a symbolic q.

Recorded Gram identities, verified to 40 dps, useful for that build:
    G[0][1] = z(q)        G[0][3] = z(q)^2        G[0][5] = P_77(q)
i.e. the Gram's first row IS the trace vector, as prop:operator-selection-lp
says (G_1j = tr_M(b_j) = t_j).


## RESOLVED 2026-08-30 — the threshold is EXACT, and my "REJECTED" was the error

The blocker recorded above was a general H_3 NF multiplication. It is a FINITE
12-entry right-multiplication table (s_i^2 = h s_i + 1, braid s0s1s0 = s1s0s1),
not a research problem. With it the Gram is symbolic in q -- validated against
pyhecke.gram.gram_matrix_mp at five values of q to ~1e-37 -- and row 5 is

    (G t)_5 = (q^10 + q^6 - q^4 + q^2 - 1) / (q^2 + 1)^2

The numerator is IRREDUCIBLE over Q with EXACTLY ONE positive real root,

    q_c = 0.894480292910614763779004984173341677394988638886...

matching the bisected value to 1.14e-46.

MY CORRECTION. PSLQ had returned 1 - q^2 + q^4 - q^6 - q^10, which is exactly
-1 times this numerator. PSLQ WAS RIGHT. I declined to quote it (correctly --
the entropy bound gives no headroom at degree 10) and then went further and
"REJECTED" it on a dps-160 run. That second step was wrong: gram_matrix_mp
saturates near 60 digits, so the extra digits were noise and the rejection
rested on noise exactly as an acceptance would have. Withholding judgement was
right; converting that into a refutation was not. The way out was to stop
fitting and derive.

FORMALIZED, sorry-free (file now 27 theorems, 0 sorries):
  coneRow5Numerator / coneRow5Poly    the constraint and its u = q^2 form
  coneRow5Numerator_eq                the substitution
  quad_pos                            3u^2 - 2u + 1 > 0 (negative discriminant)
  coneRow5Poly_strictMono             strictly increasing on u >= 0
  coneRow5Numerator_one               = 1 at q = 1, so STRICTLY satisfied there
  coneRow5Numerator_half_neg          < 0 at q = 1/2, so a root lies below 1
  cone_threshold_ne_amplitude_threshold
      THE PAYOFF: P_76(1) = 0 while (G t)_5's numerator = 1 > 0 at q = 1.

THE ARC'S CONCLUSION. The two thresholds are DIFFERENT and provably so: the
amplitude vanishes at q = 1, the cone constraint is strictly satisfied there
and turns at q_c < 1. Sign-inheriting reductions were already excluded
(toffoliFlip_mul_coneCoord_nonpos); a negative proportionality would require
the thresholds to coincide, and they do not. So the reduction that
prop:toffoli-lp-stability asserts has NO surviving form, and that is now proved
rather than measured.

QUESTION (b) -- the orderings-to-NF map -- is untouched and remains open, but
is now a much smaller target: one constraint, with an explicit polynomial.
