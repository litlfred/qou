---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUT A TIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-002-12-statement-of-the-main-result
section_title: "Statement of the main result"
section_number: 1.2
pages: 1-4
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent p olynomials that encodes the Jones polynomial of a knot and its parallels."
---
1.3. Acknowledgement 4
2. The zeta function of a graph and the quantum MacMahon Master Theorem 4
3. The arc-graph of a knot projection 5
4. The enhanced arc-graph and the Jones polynomial 7
5. Proof of Theorem 2 8
5.1. Row and column arcs order 8
5.2. Flows on GK and monomials of GB′
K
(m1, . . . mr) 8
6. Cabling of the arc graph 9
6.1. Comparison of excess numbers 11
7. Sortings and multiplicities of ﬂows 12
7.1. Sortings 12
7.2. Sortings and the Jones polynomial 13
7.3. Proof of Theorem 7 14
Appendix A. The zeta function of a graph and the Foata-Zeilberger formula 15
A.1. The Foata-Zeilberger formula 15
Appendix B. A state sum for the Jones polynomial 16
B.1. Rotation and Excess numbers 19
Appendix C. A combinatorial counting of structures 20
References 22
1. Introduction
Date: This edition: March 7, 2005 First edition: November 22, 200 4.
S.G. was supported in part by National Science Foundation. M .L. gratefully acknowledges the support of ICM-P01-05. Thi s
work was done partly while M.L. was visiting DIM, U. Chile.
1991 Mathematics Classiﬁcation. Primary 57N10. Secondary 57M25.
Key words and phrases: knots, colored Jones function, quant um algebra, zeta functions, MacMahon Master Identity, boso ns,
fermions, arc-graph.
1
1.1. The Jones polynomial of a knot. In 1985, V. Jones discovered a celebrated invariant of knots,
the Jones polynomial, [J1]. Jones’s original formulation of the Jones polynomial was given in terms of
representations of braid groups and Hecke algebras, [J1]. It soon became apparent that the Jones polynomial
can be deﬁned as a state sum of a statistical mechanics model that uses as input a planar projection of a
knot, [J2, Tu]. As soon as the Jones polynomial was discovered, it wa s compared with the better-understood
Alexander polynomial of a knot. The latter can be deﬁned using class ical algebraic topology (such as the
homology of the inﬁnite cyclic cover of the knot complement), and its skein theory can be understood purely
topologically. On the other hand, the Jones polynomial appears to b e diﬃcult to understand topologically,
and there is a good reason for this, as was explained by Witten, [Wi]. Na mely, the Jones polynomial can
be thought of as the expectation value of Wilson loops of a 3-dimensio nal gauge theory, the Chern-Simons
theory; in general, this is hard to understand. Witten’s approach le ads to a number of conjectures that relate
limits of the Jones polynomial to geometric invariants of a knot, such as representations of the fundamental
group of its complement into compact Lie groups. A recent approac h to the Jones polynomial in terms of
D-modules and holonomic functions seems to relate well to the hyperbolic geometry of knot complement s,
[GLe, Ga2] and yet another approach to the Jones polynomial is via t he Kauﬀman bracket skein theory ,
[KL].
The goal of our paper is to present the colored Jones function as an evaluation of the inverse of a non-
commutative fermionic partition function . This result is in the form very familiar in quantum ﬁeld theory,
namely the inverse of a generalized determinant. Hence there shou ld be a quantum ﬁeld theoretic derivation
of it, which may teach us new things about how to compute path integ rals in topological quantum ﬁeld
theory.
About 10 years ago, Melvin-Morton and Rozansky independently co njectured a relation among the limiting
behavior of the colored Jones function of a knot and its Alexander p olynomial (see Corollary 1.5), [MM, Ro1,
Ro2]. D. Bar-Natan and the ﬁrst author reduced the conjecture about knot invariants to a statement about
their combinatorial weight systems , and then proved it for all weight systems that come from semisimple Lie
algebras using combinatorial Lie algebraic methods, [BG]. A combinatorial desc ription of the corresponding
weight systems was obtained in [GL]. Over the years, the MMR Conjec ture has received attention by many
researchers who gave alternative proofs, [Ch, KSA, KM, Ro3, V].
A comparison of Theorem 1 and Theorem 2 reveals a direct relation be tween the Alexander polynomial
and the colored Jones function. This should help us better underst and the topological features of the colored
Jones function.
We will introduce an auxiliary weighted directed graph, the arc-grap h, that encodes transitions of walks
along a planar projection of a knot. Our results are obtained by stu dying the non-negative integer ﬂows on
this arc-graph and applying the recently discovered q-MacMahon M aster Theorem of [GLZ].
1.2. Statement of the main result.
Deﬁnition 1.1. We consider 5r indeterminates r−
i , r+
i , u−
i , u+
i , zi, 1≤ i≤ r. Let A be a r by r matrix where
each indeterminate appears at most once in an entry, and each ent ry is an indeterminate times a power of
q. We assume q is an indeterminate which commutes with all other indeterminates. Mo reover we assume
that each column contains at most one u indeterminate, in its ﬁrst or last entry diﬀerent from z. Let L(A)
be the set of those columns of A where u appears in the last non- z-entry.
We deﬁne a noncommutative algebraA(A) generated by the indeterminates which appear in A, modulo
the commutation relations speciﬁed below. Consider any 2 by 2 minor o f A consisting of rows i and i′, and
columns j and j′ (where 1≤ i < i ′≤ r, and 1 ≤ j < j ′≤ r), writing a = aij, b = aij′ , c = ai′j, d = ai′j′ , we
have the following commutation relations (we will use the symbol = q to denote ’equality up to a power of
q’):
(1) The commutation in each row: ba = q−2ab if b =q u− or a =q u− and ba = ab otherwise. The same
rule is adapted for cd commutation.
(2) The bc commutation: bc = q−1+scb if
c =q us, b =q r−+ or
b =q us, c =q r−+ or
c =q us, b =q u−+, d =q r−+, a = z or
b =q us, c =q u−+, a =q r−+, d = z.
2
bc = q−1+s+s′
cb if b =q us, c =q us′
, a =q r−+, d =q r−+, and
bc = q−1cb otherwise.
(3) Finally we require that A is right-quantum (see [GLZ]), i.e.,
ca = qac, db = qbd, ad = da + q−1cb− qbc.
Note that the commutation relations are such that each monomial in A(A) can be brought into a q-
combination of canonical monomials∏ r
i=1 am1i
1i . . . amri
ri .
Deﬁnition 1.2. We deﬁne n-evaluation of a canonical monomial ∏ r
i=1 am1i
1i . . . amri
ri to be zero if there is ij
with mij > 0 and aij = zk and otherwise
trn
r∏
i=1
am1i
1i . . . amri
ri =
∏
i /∈L(A)
trn am1i
1i . . . amri
ri
∏
i∈L(A)
trn amri
ri . . . am1i
1i ,
and
trn(us0)p0 (rs1
i1 )p1 . . . (rsm
im )pm = q−s0p0n
m∏
i=1
pi−1∏
j=0
(1− t−si(n−j−p0−...pi−1)).
We consider a generic planar projection K of an oriented zero framed knot with r + 1 crossings and with
no kinks, together with a special arc decorated with ⋆. Let K denote the corresponding long knot obtained
by breaking the special arc. We will order the arcs of K so that they appear in increasing order as we walk
in the direction of the knot, such that the special arc is last. We will a lso order the crossings of K such that
arc ai ends at the ith crossing, for i = 1, . . . , r+ 1.
Note that K can be uniquely reconstructed from K, so that any invariant of knots gives rise to a corre-
sponding invariant of long knots. We consider transitions of K: when we walk along K, we either go under
a crossing (blue transition), or jump up at a crossing (red transitio n). Each transition from arc ai to arc aj
is naturally equipped with a non-negative integer rot( ai, aj) which can be seen from K (see Deﬁnition B.6).
We deﬁne the r by r transition matrix BK = (bij) as follows.
Deﬁnition 1.3.
bij =





q−rot(ij)usign(i)
i if j = i + 1
q−rot(ij)rsign(i)
i if aiajis a red transition
zi otherwise
The next well-known theorem (see e.g. [BG]) identiﬁes the Alexander p olynomial ∆(K) of a knot diagram
K with the determinant of BK.
Theorem 1. For every knot diagram K we have:
∆(K, t) = t det(I− BK)|q=1,zi=0,usign(i)
i =t−sign(i),rsign(i)
i =(1−t−sign(i)).
Deﬁnition 1.4. The quantum determinant of an r by r matrix A = ( aij), introduced in [FRT], may be
deﬁned by
det
q
(A) =
∑
π∈Sr
(−q)−inv(π)aπ(1)1aπ(2)2 . . . aπ(r)r,
where inv( π) equals the number of pairs 1 ≤ i < j≤ r for which π(i) > π (j). Moreover we let
Ferm(A) =
∑
J⊂{1,...,r}
(−1)|J| det
q
(AJ )
where AJ is the J by J submatrix of A.
If q = 1 then Ferm( A) = det( I− A). Recall the MacMahon Master Theorem ([MMM]), known also as
the boson-fermion correspondence
1
det(I− A) =
∞∑
n=0
tr Sn(A),
where Sn(A) is the n-th symmetric power of A.
The main result of this paper is as folows:
3
Theorem 2. For every knot diagram K we can construct a matrix B′
K from BK by a permutation of rows
and columns so that
Jn(K, q) = qδ(K,n)1/Ferm(B′
K),
n-evaluated; δ(K, n) is an integer that can be computed easily from K (see Deﬁnition 3.3).
As an immediate consequence we obtain the seminal Melvin-Morton-R ozansky Conjecture (MMR in
short), whose proof was ﬁrst given by [BG].
Corollary 1.5.
lim
n→∞
Jn(K, q1/n) = t
1
∆(K, q) .
Remark 1.6. The computational complexity of the Jones polynomial and its appro ximation is studied ex-
tensively and as far as we know, this cannot be said about non-comm utative formulas. Hence it may be
enlightening to study our formula from a computation point of view.
