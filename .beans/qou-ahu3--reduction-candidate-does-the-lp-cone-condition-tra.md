---
# qou-ahu3
title: 'Reduction candidate: does the LP cone condition track -P_76, and via what orderings-to-NF map?'
status: todo
type: task
priority: normal
created_at: 2026-08-30T14:30:58Z
updated_at: 2026-08-30T14:30:58Z
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
