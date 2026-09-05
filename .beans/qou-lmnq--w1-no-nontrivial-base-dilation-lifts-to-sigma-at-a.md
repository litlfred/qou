---
# qou-lmnq
title: 'W1: no nontrivial base dilation lifts to Sigma at all — the branch sextic''s constant and linear coefficients force lambda = 1, closing the ''operator on Sigma'' escape #6738 left open'
status: todo
type: task
created_at: 2026-09-05T07:50:07Z
updated_at: 2026-09-05T07:50:07Z
---

## Question (2026-09-05, follows qou-7fnr / #6738)

#6695 excluded a rational q-connection on the base z-line; #6738 excluded the local q-dilation t -> mu t with rational-in-t coefficients. Both are about the COEFFICIENT FIELD. #6738 closed by naming what survives: 'coefficients not rational in a coordinate, or an operator on Sigma'.

This tranche tests the second alternative, and it does not need the rationality theorem at all. An automorphism sigma : Sigma -> Sigma covering the base dilation z -> lambda z must carry ramification points to ramification points, so it permutes the finite branch locus B = { D = 0 }, D the branch sextic 16z^6+24z^5+35z^4+50z^3+35z^2+24z+16. Same root multiset (D is squarefree) means D(lambda z) = c D(z). The CONSTANT term gives 16 = 16c so c = 1; the LINEAR term then gives 24 lambda = 24 so lambda = 1.

So the only dilation that lifts is the identity — for every lambda, root of unity or not, at every q. Complementary to Bezivin-Ramis rather than dependent on it.

## PLAN
1. Corpus-grep (six paths) for prior branch-locus-invariance / dilation-lift work.
2. Lean: branchSextic scaling rigidity, sorry-free, generic char-0 field, via Polynomial coeff extraction (the #6695 technique).
3. Exact probe: D squarefree, D(0) = 16 != 0, product of roots = 1, the (lambda, c) solve returning only (1,1); the deck-transformation half (disc = -D not a square in C(z) since D is squarefree of degree 6, so the Galois group is S_3 and Aut(Sigma/P^1) is trivial); and the substrate value lambda = q0^2 ~ 1.232 != 1.
4. Audit doc; scope note; qou-d8de route-1 entry strengthened to cover the Sigma chart.
