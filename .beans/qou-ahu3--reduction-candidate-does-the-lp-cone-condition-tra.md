---
# qou-ahu3
title: 'Reduction candidate: does the LP cone condition track -P_76, and via what orderings-to-NF map?'
status: todo
type: task
priority: normal
created_at: 2026-08-30T14:30:58Z
updated_at: 2026-08-30T14:36:21Z
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
