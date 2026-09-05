---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-014-24-explicit-matrices
section_title: "Explicit matrices"
section_number: 2.4
pages: 13-15
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
Borel subgroup to vary, to keep the presentation explicit we will henceforth ﬁx it to beB =B0.
Therefore, points of the ﬂag Hilbert scheme will be triples:
(2.14) X =


x1 0 0 0
∗ x2 0 0
∗ ∗ ... 0
∗ ∗ ∗ xn

, Y =


y1 0 0 0
∗ y2 0 0
∗ ∗ ... 0
∗ ∗ ∗ yn

, v =


1
0
0
0


such that [X,Y ] = 0, and the vectors{XaYbv}a,b≥0 generate the spaceV . This latter condition
implies that the ﬁrst entry of v must be non-zero, so we may use the B =B0 action to ﬁx v as
in equation (2.14). Therefore, we will abuse notation and re-write (2.11) as:
(2.15) FHilbn(C2) =
{
(X,Y,v ), X,Y lower triangular, [X,Y ] = 0, vcyclic
}
/B
In this language, the map:
FHilbn(C2)
ρ
−→ C2n
is given by taking the joint eigenvalues of the matricesX andY . Therefore, we conclude that:
(2.16) FHilbn(C) =
{
(X,Y,v ) as in (2.15), Y strictly lower triangular
}
(2.17) FHilbn(point) =
{
(X,Y,v ) as in (2.15), X,Y strictly lower triangular
}
We may use the descriptions (2.15)–(2.17) to obtain the following estimates of the dimensions
of ﬂag Hilbert schemes:
dim FHilbn(C2)≥ dim (afﬁne space of (X,Y,v ))− # (equations [X,Y ] = 0)− dimB =
(2.18) =n2 + 2n− n(n− 1)
2 − n(n + 1)
2 = 2n =: exp dim FHilbn(C2)
14 EUGENE GORSKY, ANDREI NEGUT , , AND JACOB RASMUSSEN
The right hand side stands for “expected (or virtual) dimension”. Similarly, we have:
(2.19) dim FHilbn(C)≥n =: exp dim FHilbn(C)
(2.20) dim FHilbn(point)≥n− 1 =: exp dim FHilb n(point)
The reason why the expected dimension in (2.20) is n− 1 rather than 0 is that when X and
Y are both strictly lower triangular matrices, the commutator [X,Y ] = 0 is not only strictly
lower triangular, but has the ﬁrst sub-diagonal equal to zero by default. Therefore, the ﬁrst
sub-diagonal entries aren− 1 equations that need not be placed on FHilbn(point).
Example 2.5. If the inequalities in (2.18)–(2.20) were equalities, then we would conclude that
ﬂag Hilbert schemes were local complete intersections. However, this is not the case. We give
an example of how the bound in (2.20) can fail, which we learned from Ian Grojnowski. Let
n = 10, and consider the afﬁne space of matrices X,Y which are lower triangular, and have
zero blocks of sizes 1, 2, 3 and 4 on the diagonal:
(2.21) X,Y =


0 0 0 0 0 0 0 0 0 0
∗ 0 0 0 0 0 0 0 0 0
∗ 0 0 0 0 0 0 0 0 0
∗ ∗ ∗ 0 0 0 0 0 0 0
∗ ∗ ∗ 0 0 0 0 0 0 0
∗ ∗ ∗ 0 0 0 0 0 0 0
∗ ∗ ∗ ∗ ∗ ∗0 0 0 0
∗ ∗ ∗ ∗ ∗ ∗0 0 0 0
∗ ∗ ∗ ∗ ∗ ∗0 0 0 0
∗ ∗ ∗ ∗ ∗ ∗0 0 0 0


The dimension of the afﬁne space consisting of triples (X,Y,v ) equals 35 + 35 + 10 = 80 .
Since the commutator [X,Y ] = 0 must have the2×1, 3×2 and 4×3 blocks under the diagonal
equal to zero by default, the number of equations we need to impose is only 15. Taking into
account the fact that the Borel subgroup has dimension 55, we conclude that:
dim FHilb10(point)≥ 80− 15− 55 = 10> 9 = exp dim FHilb10(point)
We may translate this example in terms of ﬂags of ideals inside C[x,y ]. Let d = 4,n =
(d+1
2
)
,
and m⊂ C[x,y ] be the maximal ideal of the origin, and let us consider the locus of ﬂags:
L = (I0⊃I1⊃... ⊃In)⊂ FHilbn(point)
such that:
(2.22) I(k+1
2 ) = mk, k = 0,...,d.
By the deﬁning property of the maximal ideal m, for eachk∈{ 0,...,d − 1} the ﬂag of ideals:
mk⊃I(k+1
2 )+1⊃...I (k+2
2 )−1⊃ mk+1
can be chosen as an arbitrary complete ﬂag of vector subspaces inmk/mk+1≃ Ck+1. Since the
dimension of the corresponding ﬂag variety is
(k+1
2
)
, we conclude that:
dimL =
d−1∑
k=0
(k + 1
2
)
=
(d + 1
3
)
≫n− 1 = exp dim FHilbn(point)
FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY 15
asd becomes large (although the inequality is strict as soon as d≥ 4). This construction also
shows that the stratumL is non-empty, since there always exist ﬂags of ideals with the property
(2.22), something which was not immediately apparent from the matrix construction (2.21).
