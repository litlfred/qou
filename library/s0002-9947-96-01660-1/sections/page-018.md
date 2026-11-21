---
doc_id: s0002-9947-96-01660-1
doc_title: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS"
section_id: page-018
section_title: "Page 18"
section_number: null
pages: 18-18
source_pdf: S0002-9947-96-01660-1.pdf
source_sha256: aa63e62b78aa5045
toc_source: undetermined
doc_brief: "Invariants of piecewise-linear 3-manifolds — This paper presents an algebraic framework for constructing in- variants of closed oriented 3-manifolds by taking a state sum model on a tri- angulation."
---
4014
JOHN W. BARRETT AND BRUCE W. WESTBURY
This results in a triangulation of the 3-ball with 2p + 1 tetrahedra. Finally do a
bistellar move of order 2 on the 3 tetrahedra ONSEn, ONSE1 and NSE1En,
replacing them by the two tetrahedra ONE1En and OSE1En.
5. Invariants of manifolds
The following is the main theorem in this paper.
Theorem 5.1. A ﬁnite semisimple spherical category of non-zero dimension de-
termines an invariant of oriented singular 3-manifolds.
Since closed (3-)manifolds are examples of singular 3-manifolds, this determines
an invariant of closed manifolds. Throughout this section, the proof refers to closed
manifolds, which, as is the general convention in this paper, are taken to be oriented.
However every statement is also true for oriented singular manifolds.
Let M be a closed simplicial manifold, J a choice of one simple object from each
isomorphism class, and K the dimension of the spherical category.
The notation in this section is as follows: for a simplicial manifold M, the edge
set is denoted E. Thus l: E →I is a labelling, and the labelled manifold is the
pair (M, l). Let v be the number of vertices of M.
Deﬁne the state sum invariant of M by a summation over the set of all labellings
by elements of J:
C(M) = K−v
X
l: E→J
Z(M, l)
Y
e∈E
dimq(l(e)).
Proof of Theorem 5.1. The rest of this section is a proof that C(M) is the mani-
fold invariant; that is, that any simplicial manifold M which triangulates a given
piecewise-linear manifold M determines the same invariant.
Let M be a simplicial complex that triangulates M.
First, C(M) does not
depend on the choice of simple objects J due to Proposition 3.3. Next it is necessary
to show that C(M) does not depend on the choice of simplicial structure for the
complex which triangulates M, and ﬁnally that it does not depend on the choice
of triangulation.
Let M1 and M2 be two diﬀerent choices of simplicial structure with the same
underlying complex and the same orientation. Then the identity map of complexes
is a combinatorial isomorphism of simplicial manifolds. By Theorem 3.9, the state
sum C(M1) is equal to a state sum over the set of labellings of M2 which are
compatible with a labelling E →J of M1.
This is not the state sum C(M2),
because the labelling of an edge in the complex runs over either the set J or the set
ˆJ={ˆa | a ∈J}. However it is equal to C(M2) because ˆa is a simple object if a is,
and ˆJ also contains one element of each isomorphism class of simple objects. The
equality follows from Proposition 3.3. This shows that C(M) does not depend on
the simplicial structure. Now it remains to consider the triangulation.
If L is a subcomplex of a complex M, and L has a simplicial structure determined
by a total order of the vertices of L, then this can be extended to a simplicial
structure of M, by extending the total order. If a complex N is obtained from the
complex M by a bistellar move, so that M = X∪σk∗∂σ3−k and N = X∪∂σk∗σ3−k,
then a choice of standard simplicial structure for ∂σ4 can be extended to X ∪∂σ4,
which contains M and N as subcomplexes. Such a choice of simplicial structure
for ∂σ4 is just the identiﬁcation of σ4 as the boundary of the standard 4-simplex,
(01234).
