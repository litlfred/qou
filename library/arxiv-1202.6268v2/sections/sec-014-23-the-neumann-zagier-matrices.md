---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-014-23-the-neumann-zagier-matrices
section_title: "The Neumann-Zagier matrices"
section_number: 2.3
pages: 12-14
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
and redundancy. We have already observed that any one of the ed ge constraints (
2.3) can
be removed. Let us then ignore the edge I =N. We can also use ( 2.4) to eliminate one of
the three shapes for each tetrahedron. We choose this canonica lly to be Z ′
i, though which
pair of edges is labelled Z ′
i depends on the choice of quad type for the tetrahedron. Then
the ﬁrst N− 1 edge equations and the meridian ( µ) equation are equivalent to
(2.6)
N∑
j=1
(
AijZj + BijZ ′′
j
)
=iπν i, i = 1,...,N,
THE QUANTUM CONTENT OF THE GLUING EQUATIONS 13
where
(2.7) Aij =
{
Gij− G′
ij I⁄=N
GN +1,j − G′
N +1,j i =N Bij =
{
G′′
ij− G′
ij I⁄=N
G′′
N +1,j − G′
N +1,j i =N ;
and
(2.8) νi :=
{
2−∑ N
j=1 G′
ij i⁄=N
−∑ N
j=1 G′
N +1,j i =N.
We will generally assume Z, Z ′′, and ν to be column vectors, and write AZ + BZ ′′ =iπν.
The matrices ( G, G′, G′′) as well as ( A, B,ν ) can easily be obtained from SnapPy [
CDW],
as is illustrated in Appendix D.
The Neumann-Zagier matrices A and B have a remarkable property: they are the top two
blocks of a 2 N× 2N symplectic matrix [ NZ85]. It follows that
(2.9) ABT = BAT,
and that the N× 2N block ( A B ) has full rank. This symplectic property is crucial for
deﬁning the state integral of [ Dim], for deﬁning our formal power series invariant ZM (ℏ),
and for the combinatorial proofs of topological invariance of the 1 -loop invariant. A detailed
discussion of the symplectic properties of the Neumann-Zagier mat rices A, B is given in
Appendix A.
2.4. Combinatorial ﬂattenings. We now have all ingredients to deﬁne what is a combi-
natorial ﬂattening.
Deﬁnition 2.1. Given an ideal triangulation T ofM, a combinatorial ﬂattening is a collec-
tion of 3N integers (fi,f ′
i,f ′′
i )∈ Z3 for i = 1,...,N that satisfy
(2.10a) fi +f ′
i +f ′′
i = 1, i = 1,...,N,
(2.10b)
N∑
i=1
(
GIifi + G′
Iif ′
i + G′′
Iif ′′
i
)
=
{
2 I = 1,...,N
0 I =N + 1 .
Note that if we eliminate f ′ using Equation (
2.10a), a ﬂattening is a pair of vectors
(f,f ′′)∈ Z2N that satisﬁes
(2.11) Af + Bf ′′ =ν.
Evidently, Equation ( 2.11) is a system of linear Diophantine equations. Neumann proved in
[Neu92, Lem.6.1] that every ideal triangulation T has a ﬂattening.
Remark 2.2. Combinatorial ﬂattenings should not be confused with the (geomet ric) ﬂat-
tenings of [ Neu04, Defn.3.1]. The latter ﬂattenings are coherent choices of logarithm s for
the shape parameters z,z ′,z ′′ of a complex solution to the gluing equations. On the other
hand, our combinatorial ﬂattenings are independent of a solution t o the gluing equations. In
the rest of the paper, the term ﬂattening will mean a combinatorial ﬂattening in the sense
of Deﬁnition 2.1.
14 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
