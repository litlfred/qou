---
doc_id: bsmf-2002-130-3-457-0
doc_title: "Hyperideal polyhedra in hyperbolic 3-space"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-4
source_pdf: BSMF_2002__130_3_457_0.pdf
source_sha256: 63f79235d0c13ba8
toc_source: inferred
doc_brief: "Hyperideal polyhedra in hyperbolic 3-space — — A hyperideal polyhedron is a non-compact polyhedron in the hyperbolic 3-space 3 which, in the projective model for 3 ⊂ 3, is just the intersection of 3"
---
Bull. Soc. math. France
130 (3), 2002, p. 457–491
HYPERIDEAL POLYHEDRA IN HYPERBOLIC 3-SPACE
by Xiliang Bao & Francis Bonahon
Abstract. — A hyperideal polyhedron is a non-compact polyhedron in the hyperbolic
3-space
3 which, in the projective model for
3 ⊂
3, is just the intersection of
3 with a projective polyhedron whose vertices are all outside
3 and whose edges all
meet
3 . We classify hyperideal polyhedra, up to isometries of
3, in terms of their
combinatorial type and of their dihedral angles.
R´esum´e (Poly`edres hyperid´eaux de l’espace hyperbolique de dimension 3)
Un poly`edre hyperid´eal est un poly`edre non-compact de l’espace hyperbolique
3 de
dimension 3 qui, dans le mod`ele projectif pour
3 ⊂
3, est simplement l’intersection
de
3 avec un poly`edre projectif dont les sommets sont tous en dehors de
3 et dont
toutes les arˆetes rencontrent
3. Nous classiﬁons ces poly`edres hyperid´eaux, `a isom´etrie
de
3 pr`es, en fonction de leur type combinatoire et de leurs angles di´edraux.
Consider a compact convex polyhedron P, intersection of ﬁnitely many half-
spaces in one of the three n-dimensional homogeneous spaces, namely the eu-
clidean space En, the sphere Sn or the hyperbolic space Hn. The boundary of P
inherits a natural cell decomposition, coming from the faces of the polyhedron.
Texte re¸cu le 26 juin 2001, accept´e le 8 d´ecembre 2001
Xiliang Bao, Department of Mathematics, University of Southern California, Los Angeles
CA 90089-1113 (USA)
•
Computer Associates, 9740 Scranton Road # 200, San Diego,
CA 92121-1745 (USA)
•
E-mail : xiliang.bao@ca.com
Francis Bonahon, Department of Mathematics, University of Southern California, Los
Angeles CA 90089-1113, (USA)
•
E-mail : fbonahon@math.usc.edu
Url : http://math.usc.edu/~fbonahon
2000 Mathematics Subject Classiﬁcation. — 51M09.
Key words and phrases. — Hyperbolic space, polyhedron, ideal polyhedron, hyperideal.
This work was partially supported by NSF grants DMS-9504282 and DMS-9803445 from the
US National Science Foundation.
BULLETIN DE LA SOCI´ET´E MATH´EMATIQUE DE FRANCE
0037-9484/2002/457/$ 5.00
c
⃝Soci´et´e Math´ematique de France
458
BAO (X.) & BONAHON (F.)
Along each (n−2)-face e, we can measure the internal dihedral angle αe ∈]0, π[
between the two (n −1)-faces meeting along e. A natural question then arises:
If we are given an (n −1)-dimensional cell complex X with a weight αe ∈]0, π[
attached to each (n −2)-dimensional cell e, is there a convex polyhedron P
in En, Sn or Hn whose boundary has the combinatorial structure of this cell
complex X, and such that αe is the dihedral angle of P along the face e?
An explicit computation provides a full answer in the simplest case where X
is the boundary of the n-simplex. The solution involves the signatures of var-
ious minors of the symmetric n × n-matrix whose ij-entry is +1 if i = j and
is −cosαeij, where eij is the edge joining the i-th vertex to the j-th vertex,
if i̸ = j; see [6], [17]. In particular, the answer is expressed in terms of the signs
of polynomials in cos αeij. Since this condition on the angles αe is not that
easy to handle, one can expect the general case to be quite intractable, and
this indeed seems to be the case.
In general, the main technical diﬃculty is to control the combinatorics as
one deforms the polyhedron P. A typical problem occurs when a p-dimensional
face becomes (p−1)-dimensional, for instance when two vertices collide so that
a 1-dimensional face shrinks to one point.
One way to bypass this technical diﬃculty is to impose additional restric-
tions which will prevent such vertex collisions and face collapses. For instance,
one can require that all dihedral angles αe are acute, namely lie in the inter-
val ]0, 1
2π]. In this context, Coxeter [6] proved that every acute angled compact
convex polyhedron in the euclidean space En is an orthogonal product of eu-
clidean simplices, possibly lower dimensional; this reduces the problem to the
case of euclidean simplices, which we already discussed. Similarly, Coxeter also
proved that every acute angled convex polyhedron in the sphere Sn is a simplex.
The situation is more complex in the hyperbolic space Hn but, when n = 3,
Andreev was able to classify all acute angled compact convex polyhedra in H3
in terms of their combinatorics and their dihedral angles [2].
In hyperbolic space, another approach to prevent vertex collisions is to put
these vertices inﬁnitely apart, by considering (non-compact ﬁnite volume) ideal
polyhedra, where all vertices sit on the sphere at inﬁnity ∂∞Hn of Hn. In [11],
Rivin classiﬁes all ideal polyhedra in H3 in terms of their combinatorics and of
their dihedral angles. The case of acute angled polyhedra with some vertices
at inﬁnity had been earlier considered by Andreev [3].
In this paper, we propose to go one step further by considering polyhedra in
H3 whose vertices are ‘beyond inﬁnity’, and which we call hyperideal polyhedra.
These are best described in Klein’s projective model for H3. Recall that, in
this model, H3 is identiﬁed to the open unit ball in R3 ⊂RP3, that geodesics
of H3 then correspond to the intersection of straight lines of R3 with H3, and
that totally geodesic planes in H3 are the intersection of linear planes with H3.
In this projective model H3 ⊂RP3, a hyperideal polyhedron is deﬁned as the
tome 130 – 2002 – no 3
HYPERIDEAL POLYHEDRA IN HYPERBOLIC 3-SPACE
459
intersection P of H3 with a compact convex polyhedron P Proj of RP3 with the
following properties:
1) Every vertex of P Proj is located outside of H3;
2) Every edge of P Proj meets H3.
Note that we allow vertices of P Proj to be located on the unit sphere ∂∞H3
bounding H3, so that hyperideal polyhedra include ideal polyhedra as a special
case.
From now on, we will restrict attention to the dimension n = 3. Following
the standard low-dimensional terminology, we will call vertex any 0-dimensional
face or cell, an edge will be a 1-dimensional face or cell, and we will reserve the
word face for any 2-dimensional face or cell.
To describe the combinatorics of a hyperideal polyhedron P, it is convenient
to consider the dual graph Γ of the cell decomposition of ∂P, namely the graph
whose vertices correspond to the (2-dimensional) faces of P, and where two
vertices v and v′ are connected by an edge exactly when the corresponding
faces f and f ′ of P have an edge in common. Note that Γ is also the dual
graph of the projective polyhedron P Proj associated to P.
The graph Γ must be planar, in the sense that it can be embedded in the
sphere S2. In addition, Γ is 3-connected in the sense that it cannot be discon-
nected or reduced to a single point by removing 0, 1 or 2 vertices and their
adjacent edges; this easily follows from the fact that two distinct faces of P Proj
can only meet along the empty set, one vertex or one edge. A famous theorem
of Steinitz states that a graph is the dual graph of a convex polyhedron in R3
if and only if it is planar and 3-connected; see [8]. A classical consequence of 3-
connectedness is that the embedding of Γ in S2 is unique up to homeomorphism
of S2; see for instance [9, §32]. In particular, it intrinsically makes sense to talk
of the components of S2 −Γ. Note that these components of S2 −Γ naturally
correspond to the vertices of P Proj.
The results are simpler to state if, instead of the internal dihedral angle αe
of the polyhedron P along the edge e, we consider the external dihedral an-
gle θe = π −αe ∈]0, π[.
Theorem 1. — Let Γ be a 3-connected planar graph with a weight θe ∈]0, π[
attached to each edge e of Γ. There exists a hyperideal polyhedron P in H3 with
dual graph isomorphic to Γ and with external dihedral angle θe along the edge
corresponding to the edge e of Γ if and only if the following two conditions are
satisﬁed:
1) For every closed curve γ embedded in Γ and passing through the edges e1,
e2, . . . , en of Γ, !n
i=1 θei ≥2π with equality possible only if γ is the boundary
of a component of S2 −Γ;
2) For every arc γ embedded in Γ, passing through the edges e1, e2, . . . , en
of Γ, joining two distinct vertices v1 and v2 which are in the closure of the same
BULLETIN DE LA SOCI´ET´E MATH´EMATIQUE DE FRANCE
460
BAO (X.) & BONAHON (F.)
component A of S2 −Γ but such that γ is not contained in the boundary of A,
!n
i=1 θei > π.
In addition, for the projective polyhedron P Proj associated to P, a vertex of
