---
# qou-bc09
title: 'The many-body term is located and has the wrong sign: the alpha-free 4He ceiling'
status: completed
type: task
priority: normal
created_at: 2026-09-01T05:07:55Z
updated_at: 2026-09-01T05:08:17Z
---


RESOLVED 2026-09-01 -- computations/probes/three_body_term_has_the_wrong_sign_probe.py,
6/6. This is the negative result the arc was heading toward, and it bounds what
the bond graph can do.

WHERE THE MANY-BODY TERM LIVES. Attaching nucleon 3 to a prefix on nucleons 1-2,
as the functional P -> tr(P.A)/tr(P) over 20 random prefix words:

  k=1 (chain, bonded to its neighbour only)  EXACTLY RANK ONE
      one constant, spread < 1e-12, and it independently reproduces the arc's
      recorded transfer scalar F_pp = 0.385581983466
  k=2 (all-pairs, bonded to both)            NOT rank one
      same prefixes give 0.196 .. 0.696

Mechanism, and it is mechanical: the 1-3 bond is the band generator
(T5 T4 T3)(T2+d)(T3 T4 T5)^-1, which routes strand 2 THROUGH strands 3-5 -- the
middle nucleon. It therefore does not commute past the prefix, and that failure
to commute IS the three-body term. Nothing else in the construction makes one.

THE SIGN, AT EVERY A=3 ORDERING (L = log(tr_free/tr_atom); true K3 vs naive sum):

  ppp -0.168557 (-11.47%)   pnp -0.166607  (-9.04%)
  ppn -0.236512 (-12.83%)   pnn -0.243095 (-10.75%)
  npp -0.236512 (-12.83%)   nnp -0.243095 (-10.75%)
  npn -0.340054 (-15.04%)   nnn -0.362074 (-13.30%)

NEGATIVE IN ALL EIGHT. Larger L is more binding, so the three-body term REMOVES
binding -- and 4He is the isotope that needs 62 % more.

IT BREAKS A SYMMETRY THE NUCLEUS HAS. Reversal is exact (pnn vs nnp, 0.0e0) but
permutation is not: pnp vs ppn 4.1686 %, npn vs nnp 5.0477 % -- identical bond
multisets, differing only in WHICH NUCLEON IS IN THE MIDDLE, the one the band
routing passes through. A physical nucleus has no middle, so that 4-5 % is a
labelling artifact of embedding the bond graph in a line. Same defect measured
at ~4 % in chain_telescopes_and_ordering_sensitivity, now with its cause named.

IT EXPLAINS NO-DISTANCE-DECAY RATHER THAN CONTRADICTING IT. The far p-n bond's
own value matches the adjacent p-n bond to 1.11e-15 while the triangle defect is
-0.236512: the bond's OWN invariant is routing-independent; its COMMUTATOR with
what it passes through is not. One gives no decay, the other sub-additivity.
TRAP: compare like with like -- in ppn the far bond is p-n, so it compares
against gen 5, not the p-p bond at gen 2. Against the wrong one it reads as a
0.187 discrepancy and looks like decay. A5 caught me making exactly that error.

THE alpha-FREE CEILING:
  B(2H)  exact        2.833163 MeV   AME  2.224566   +27.36 %
  B(4He) naive sum   17.181143 MeV   AME 28.295661   -39.28 %
  model B(4He)/B(2H) <=  6.0643      AME 12.7196     short by 2.0975x

alpha CANCELS in the ratio, so no normalisation fixes it. 2H is a single bond and
therefore exact -- no many-body term is possible at A=2. The 4He figure is the
naive pairwise sum, containing NO many-body term at all; to reach 12.72 those
terms would have to be large and POSITIVE, where all eight measured are negative.

CONSEQUENCE FOR L2 1PPQ. The target is 8 meV on 28.3 MeV. This construction is
short by 2.10x -- ~13 orders away -- and the all-pairs topology's correction over
the chain moves it further away. The remaining 4He binding is NOT in the bond
graph. The convention questions settled earlier in this arc (qou-6pt7, qou-kb25)
move 1-3 % and are irrelevant at this scale.

CAVEAT ON THE BOUND: one-sided with one unmeasured input. B(2H) is exact and the
naive B(4He) has no many-body content, so it is an upper bound PROVIDED A=4
many-body terms are non-positive -- measured for all eight THREE-body terms at
A=3, NOT measured for the genuine FOUR-body term, which needs H_12. The weaker
unconditional statement is still sufficient: a pairwise sum with no many-body
content gives 6.0643 against 12.7196.
