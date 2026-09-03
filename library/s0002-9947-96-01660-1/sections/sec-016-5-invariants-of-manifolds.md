---
doc_id: s0002-9947-96-01660-1
doc_title: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS"
section_id: sec-016-5-invariants-of-manifolds
section_title: "Invariants of manifolds"
section_number: 5
pages: 18-19
source_pdf: S0002-9947-96-01660-1.pdf
source_sha256: aa63e62b78aa5045
doc_brief: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS — This paper presents an algebraic framework for constructing in- variants of closed oriented 3-manifolds by taking a state"
---
The following is the main theorem in this paper.
Theorem 5.1. A ﬁnite semisimple spherical category of non-zero dimension de-
termines an invariant of oriented singular 3-manifolds.
Since closed (3-)manifolds are examples of singular 3-manifolds, this determines
an invariant of closed manifolds. Throughout this section, the proof refers to closed
manifolds, which, as is the general convention in this paper, are taken to be oriented.
However every statement is also true for oriented singular manifolds.
LetM be a closed simplicial manifold, J a choice of one simple object from each
isomorphism class, and K the dimension of the spherical category.
The notation in this section is as follows: for a simplicial manifold M,t h ee d g e
set is denoted E.T h u sl: E→ I is a labelling, and the labelled manifold is the
pair (M,l ). Let v be the number of vertices of M.
Deﬁne the state sum invariant ofM by a summation over the set of all labellings
by elements of J:
C(M)= K−v ∑
l: E→J
Z(M,l )
∏
e∈E
dimq(l(e)).
Proof of Theorem 5.1. The rest of this section is a proof that C(M) is the mani-
fold invariant; that is, that any simplicial manifold M which triangulates a given
piecewise-linear manifoldM determines the same invariant.
Let M be a simplicial complex that triangulates M.F i r s t ,C(M)d o e sn o t
depend on the choice of simple objectsJ due to Proposition 3.3. Next it is necessary
to show that C(M) does not depend on the choice of simplicial structure for the
complex which triangulatesM, and ﬁnally that it does not depend on the choice
of triangulation.
Let M1 and M2 be two diﬀerent choices of simplicial structure with the same
underlying complex and the same orientation. Then the identity map of complexes
is a combinatorial isomorphism of simplicial manifolds. By Theorem 3.9, the state
sum C(M1) is equal to a state sum over the set of labellings of M2 which are
compatible with a labelling E → J of M1. This is not the state sum C(M2),
because the labelling of an edge in the complex runs over either the set J or the set
ˆJ={ˆa|a∈J}. However it is equal to C(M2) because ˆa is a simple object if a is,
and ˆJ also contains one element of each isomorphism class of simple objects. The
equality follows from Proposition 3.3. This shows that C(M) does not depend on
the simplicial structure. Now it remains to consider the triangulation.
IfL is a subcomplex of a complexM,a n dL has a simplicial structure determined
by a total order of the vertices of L, then this can be extended to a simplicial
structure of M, by extending the total order. If a complex N is obtained from the
complexM by a bistellar move, so thatM =X∪σk∗∂σ3−k andN =X∪∂σk∗σ3−k,
then a choice of standard simplicial structure for ∂σ4 can be extended to X∪∂σ4,
which contains M and N as subcomplexes. Such a choice of simplicial structure
for ∂σ4 is just the identiﬁcation of σ4 as the boundary of the standard 4-simplex,
(01234).
INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS 4015
Let (ij)↦→eij,f o r0≤i<j ≤ 4 be a labelling of the standard 4-simplex (01234).
This determines partition functions for each tetrahedron in the boundary,
Z(±(1234)) =
{e12 e13 e23
e34 e24 e14
}
±
,Z (±(0234)) =
{e02 e03 e23
e34 e24 e04
}
±
,
Z(±(0134)) =
{e01 e03 e13
e34 e14 e04
}
±
,Z (±(0124)) =
{e01 e02 e12
e24 e14 e04
}
±
,
Z(±(0123)) =
{
e01 e02 e12
e23 e13 e03
}
±
.
The invariance ofC(M) under bistellar moves follows from the next proposition.
Let P be the map x⊗y↦→y⊗x.
Proposition 5.2 (Orthogonality). The map
dimq(e02)
∑
e13∈J
Z(0123)Z(−0123) dimq(e13)
is equal to the identity map on H(e23,e 03,e 02)⊗H(e12,e 02,e 01).
(Biedenharn-Elliot). The equality
(
Z(0234)⊗ 1
)(
1⊗Z(0124)
)
=
∑
e13∈J
dimq(e13)
(
1⊗Z(0123)
)(
P⊗ 1
)(
1⊗Z(0134)
)(
P⊗ 1
)(
Z(1234)⊗ 1
)
holds.
These equalities hold for all choices of labels {eij} not explicitly summed over.
The proof of these will be given below, after completing the proof of Theorem
