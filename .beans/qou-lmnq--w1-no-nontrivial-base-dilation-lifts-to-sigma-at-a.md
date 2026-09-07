---
# qou-lmnq
title: 'W1: no nontrivial base dilation lifts to Sigma at all — the branch sextic''s constant and linear coefficients force lambda = 1, closing the ''operator on Sigma'' escape #6738 left open'
status: completed
type: task
priority: normal
created_at: 2026-09-05T07:50:07Z
updated_at: 2026-09-05T08:12:56Z
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



## RESULT (2026-09-05, PR #6769)

**Scope (b), invariant = the branch sextic's own coefficients.** An automorphism of Sigma covering z -> lambda z permutes the six finite branch points (D squarefree, D(0) = 16 != 0), so D(lambda z) = c D(z); the constant term forces c = 1 and the linear term then forces lambda = 1. Only the identity dilation lifts to Sigma — every lambda, every q, root of unity or not. Lean QOU.Mass.DilationBranchLocusRigidity.dilation_scaling_rigid, sorry-free, generic char-0 field, lean-direct exit 0, axioms clean.

Complementary to Bezivin-Ramis rather than a corollary: it constrains no coefficient field and covers the root-of-unity case that theorem excludes by hypothesis.

Control that makes it mean something: the same solve on z^6 - 1 returns all six sixth roots of unity, so the null result is a property of the sextic's nonzero constant AND linear coefficients, not of the searcher. Weaker fallback recorded: lambda.B = B alone gives lambda^6 = 1 (product of roots = 16/16 = 1). Substrate lambda = q0^2 = 1.2320524541667639 fails both.

Composition (this is the point): c3_w1_cover_monodromy.py already concluded D_q lives on the 3-sheeted cover, not the base. This says the dilation cannot follow it there. The dilation route is now closed in the base coordinate (#6695), the ramified local coordinate (#6738), and Sigma itself.

NOT excluded: a base map that is not a dilation; route 2 (root-of-unity FIBRE monodromy), now the live route; route 3 (RSZ/Sauloy import). D_q is NOT constructed.

Audit: docs/audits/2026-09-05-w1-dilation-does-not-lift-to-sigma.md
