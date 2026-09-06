---
doc_id: arxiv-1401.5542v1
doc_title: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 1401.5542v1.pdf
source_sha256: f7cd278a274f37c5
doc_brief: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS — The Ptolemy coordinates for boundary-unipotent SL(n, C)-representations of a 3-manifold group were introduced in [7] inspired by theA-coordinates on"
---
1.1. The Ptolemy coordinates 2
1.2. Decorated SL(2 , C)-representations 2
1.3. Obstruction classes and PSL(2 , C)-representations 4
1.4. Our results 4
2. Notation 6
2.1. Triangulations 6
2.2. Miscellaneous 7
3. The Ptolemy varieties 7
3.1. The SL(2 , C)-Ptolemy variety 7
3.2. Obstruction classes 8
4. The diagonal action 9
4.1. The reduced Ptolemy varieties 9
4.2. Shapes and gluing equations 11
4.3. Proof that α∗ is basic 11
5. The Ptolemy ﬁeld and the trace ﬁeld 12
5.1. Explicit description of the Ptolemy ﬁeld 12
5.2. The setup of the proof 12
5.3. Proof for one cusp 13
5.4. The general case 13
5.5. Proof of Proposition 1.9 15
6. Ptolemy varieties for n> 2 16
6.1. Deﬁnition of the Ptolemy variety 16
Date: November 27, 2024.
S. G. and C. Z. were supported in part by the NSF.
1991 Mathematics Classiﬁcation. Primary 57N10. Secondary 57M27.
Key words and phrases: Ptolemy coordinates, trace ﬁeld, 3-manifolds.
1
arXiv:1401.5542v1  [math.GT]  22 Jan 2014
2 STA VROS GAROUF ALIDIS, MATTHIAS GOERNER, AND CHRISTIAN K. ZICKERT
6.2. The diagonal action 16
6.3. Representations 17
6.4. Proof that α∗ is basic 18
References 20
1. Introduction
1.1. The Ptolemy coordinates. The Ptolemy coordinates for boundary-unipotent repre-
sentations of a 3-manifold group in SL( n, C) were introduced in Garoufalidis–Thurston–
Zickert [7] inspired by the A-coordinates on higher Teichm¨ uller space due to Fock and
Goncharov [4]. In this paper we will focus primarily on representations in SL(2 , C) and
PSL(2, C).
Given a topological ideal triangulationT of an oriented compact 3-manifoldM, a Ptolemy
assignment (for SL(2, C)) is an assignment of a non-zero complex number (called a Ptolemy
coordinate) to each 1-cell ofT , such that for each simplex, the Ptolemy coordinates assigned
to the edges εij satisfy the Ptolemy relation
(1.1) c03c12 +c01c23 =c02c13.
The set of Ptolemy assignments is thus an aﬃne variety P2(T ), which is cut out by homo-
geneous quadratic polynomials.
In this paper we deﬁne the Ptolemy ﬁeld of a boundary-unipotent representation and
show that it is isomorphic to the trace ﬁeld. This gives rise to an eﬃcient algorithm for
exact computation of the trace ﬁeld of a hyperbolic manifold.
1.2. Decorated SL(2, C)-representations. The precise relationship between Ptolemy as-
signments and representations is given by
(1.2){
Points in
P2(T )
}
oo 1−1 //
{
Natural (SL(2, C),P )-
cocycles on M
}
oo 1−1 //
{
Generically decorated
(SL(2, C),P )-representations
}
.
The concepts are brieﬂy described below, and the correspondences are illustrated in Figures 5
and 3. We refer to Section 2 for a summary of our notation. The bijections of (1.2) ﬁrst
appeared in Zickert [12] (in a slightly diﬀerent form), and were generalized to SL( n, C)-
representations in Garoufalidis–Thurston–Zickert [7].
• Natural cocycle: Labeling of the edges of each truncated simplex by elements in
SL(2, C) satisfying the cocycle condition (the product around each face is 1). The
long edges are counter diagonal, i.e. of the form
( 0−x−1
x 0
)
, and the short edges are
non-trivial elements in P . Identiﬁed edges are labeled by the same group element.
• Decorated representation: A decoration of a boundary-parabolic representation ρ is
an assignment of a coset gP to each vertex of ˆ~M which is equivariant with respect
to ρ. A decoration is generic if for each edge joining two vertices, the two P -cosets
gP , hP are distinct as B-cosets. This condition is equivalent to det( ge1,he 1)⁄= 0.
THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS 3
Two decorations are considered equal if they diﬀer by left multiplication by a group
elementg.
1
0
3
2
c02
c23c01 c12
c03
c13
0
1
2
3
α
β
i
j
k
cij cjk
cki i
j
k
β =
(
1− ckicijcjk
0 1
)
α =
(
0 −c−1
ij
cij 0
)
α
β
Figure 1. Ptolemy as-
signment; the Ptolemy
relation (1.1) holds.
Figure 2. Natural co-
cycle; α is counter-di-
agonal, β∈P .
Figure 3. From
Ptolemy assignments
to natural cocycles.
g1P
g0P g2P
g3P
 gjP
giP i
j
cij = det(gie1,gje1)
Figure 4. Decoration; equivariant as-
signment of cosets.
Figure 5. From decorations to
Ptolemy assignments.
By ignoring the decoration, (1.2) yields a map
(1.3) R: P2(T )→
{
(SL(2, C),P )-representations
}/
Conj.
The representation corresponding to a Ptolemy assignment is given explicitly in terms of the
natural cocycle.
Remark 1.1. Note that a natural cocycle canonically determines a representation of the
edge path groupoid of the triangulation of M by truncated simplices.
Remark 1.2. Every boundary-parabolic representation has a decoration, but a representa-
tion may have only non-generic decorations. The map R is thus not surjective in general,
and the image depends on the triangulation. However, if the triangulation is suﬃciently
ﬁne,R is surjective (see [7]). The preimage of a representation depends on the image of the
peripheral subgroups (see Proposition 1.9).
4 STA VROS GAROUF ALIDIS, MATTHIAS GOERNER, AND CHRISTIAN K. ZICKERT
1.3. Obstruction classes and PSL(2, C)-representations. There is a subtle distinction
between representations in SL(2 , C) versus PSL(2, C). The geometric representation of a
hyperbolic manifold always lifts to an SL(2, C)-representation, but for a one-cusped manifold,
no lift is boundary-parabolic (any lift will take a longitude to an element of trace −2 [2]).
The obstruction to lifting a boundary-parabolic PSL(2 , C)-representation to a boundary-
parabolic SL(2, C)-representation is a class in H 2(ˆM; Z/2Z). For each such class there is a
Ptolemy varietyPσ
2 (T ), which maps to the set of PSL(2, C)-representations with obstruction
class σ. More precisely, Pσ
2 (T ) is deﬁned for each 2-cocycle σ∈ Z 2(ˆM; Z/2Z), and up to
canonical isomorphism only depends on the cohomology class of σ. The Ptolemy variety for
the trivial cocycle equals P2(T ). The analogue of (1.2) is
(1.4)
{
Points in
Pσ
2 (T )
}
oo 1−1 //



Lifted natural
(PSL(2, C),P )-cocycles
with obstruction cocycle σ



// //



Generically decorated
(PSL(2, C),P )-representations
with obstruction class σ


.
A lifted natural cocycle is deﬁned as above, except that the product along a face is now ±I,
where the sign is determined by σ. The right map is no longer a 1-1 correspondence; the
preimage of each decorated representation is the choice of lifts, i.e. parametrized by a cocycle
in Z 1(ˆM; Z/2Z). We refer to [7] for details. As in (1.3), ignoring the decoration yields a
map
(1.5) R: Pσ
2 (T )→
{
(PSL(2, C),P )-representations
with obstruction class σ
}/
Conj.
which is explictly given in terms of the natural cocycle.
Theorem 1.3 (Garoufalidis–Thurston–Zickert [7]). If M is hyperbolic, and all edges of T
are essential, the geometric representation is in the image of R.
Remark 1.4. IfT has a non-essential edge, all Ptolemy varieties will be empty. Hence,
if Pσ
2 (T ) is non-empty for some σ, and if M is hyperbolic, the geometric representation is
detected by the Ptolemy variety of the geometric obstruction class.
