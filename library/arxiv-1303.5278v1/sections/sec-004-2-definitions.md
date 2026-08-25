---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-004-2-definitions
section_title: "Definitions"
section_number: 2
pages: 6-9
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
Deﬁnition 2.1.LetM be an orientable topologically ﬁnite 3-manifold which is the interior
of a compact 3-manifold with torus boundary components. An ideal triangulation T of
M consists of a pairwise disjoint union of standard Euclidean 3–simplices,~∆ = ∪n
k=1~∆k,
together with a collection Φ of Euclidean isometries between the 2–simplices in~∆, called
face pairings, such that the quotient space(~∆\~∆(0))/Φ is homeomorphic toM. The images
of the simplices inT may be singular inM.
Deﬁnition 2.2.Let T be an ideal triangulation with at least 2 distinct tetrahedra. A2–3
move can be performed on any pair of distinct tetrahedra ofT that share a triangular face
t. We removet and the two tetrahedra, and replace them with three tetrahedra arranged
around a new edge, which has endpoints the two vertices not ont. See Figure 1a. A 3–2
move is the reverse of a 2–3 move, and can be performed on any triangulation with a degree
3 edge, where the three tetrahedra incident to that edge are distinct.
Deﬁnition 2.3.Let T be an ideal triangulation. A0–2 movecan be performed on any pair
of distinct triangular faces ofT that share an edgee2. Around the edgee, the tetrahedra of
T are arranged in a cyclic sequence, which we call abook of tetrahedra. (Note that tetrahedra
may appear more than once in the book.) The two triangles ande separate the book into two
half–books. We unglue the tetrahedra that are identiﬁed across the two triangles, duplicating
the triangles and also duplicatinge. We glue into the resulting hole a pair of tetrahedra
glued to each other in such a way that there is a degree 2 edge between them. See Figure 1b.
A 2–0 moveis the reverse of a 0–2 move, and can be performed on any triangulation with a
degree 2 edge, where the two tetrahedra incident to that edge are distinct, there are no face
pairings between the four external faces of the two tetrahedra, and the two edges opposite
the degree 2 edge are not identiﬁed.
Remark 2.4. A 0–2 move is also called alune move in the dual language of standard
spines [Mat87, Mat07, Pie88, BP97]. In [Mat87, Lem.2.1.11] and [Pie88] (see also [Pet95,
Prop.I.1.13]) it was shown that a 0–2 move follows from a combination of 2–3 moves as long
as the initial triangulation has at least2 ideal tetrahedra.
Deﬁnition 2.5.Let ∆3 be the standard 3–simplex with a chosen orientation. Each pair of
opposite edges corresponds to a normal isotopy class of quadrilateral discs in∆3, disjoint
from the pair of edges. We call such an isotopy class anormal quadrilateral type. Each vertex
of ∆3 corresponds to a normal isotopy class of triangular discs in∆3, disjoint from the face
of ∆3 opposite the vertex. We call such an isotopy class anormal triangle type. Let T(k)
2Unlike for the 2–3 move, it is possible to make sense of the 0–2 move when the two triangles are not
distinct. However, we will not make use of this variant in this paper.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 7
2–3
3–2
(a) The 2–3 and 3–2 moves.
0–2
2–0
(b) The 0–2 and 2–0 moves.
Figure 1. Moves on (topological) triangulations.
be the set of allk–simplices inT. If σ∈ T(3), then there is an orientation preserving map
∆3→σ taking thek–simplices in∆3 to elements ofT(k), and which is a bijection between
the sets of normal quadrilateral and triangle types in∆3 and inσ. Let □ and∆ denote the
sets of all normal quadrilateral and triangle types inT respectively.
Deﬁnition 2.6.Given a 3-manifold M with an ideal triangulationT, the normal surface
solution space C(M; T) is a vector subspace ofR7n, where n is the number of tetrahedra
in T, consisting of vectors satisfying thecompatibility equations of normal surface theory.
The coordinates of x∈ R7n represent weights of the four normal triangle types and the
three normal quadrilateral types in each tetrahedron, and the compatibility equations state
that normal triangles and quadrilaterals have to meet the 2–simplices ofT with compatible
weights.
A vector in R7n is called admissible if at most one quadrilateral coordinate from each
tetrahedron is non-zero and all coordinates are non-negative. An integral admissible element
of C(M; T) corresponds to a unique embedded, closednormal surface in (M, T) and vice
versa.
Deﬁnition 2.7.(See [JR03], [KR05]) An ideal triangulationT of an orientable3-manifold is
0-eﬃcientif there are no embedded normal 2-spheres or one-sided projective planes. An ideal
triangulation T is 1-eﬃcient if it is 0-eﬃcient, the only embedded normal tori are vertex-
linking and there are no embedded one-sided normal Klein bottles. An ideal triangulationT
is strongly 1-eﬃcientif there are no immersed normal 2–spheres, projective planes or Klein
bottles and the only immersed normal tori are coverings of the vertex-linking tori.
Note that in some contexts, “atoroidal” is taken to mean that there is no immersed torus
whose fundamental group injects into the fundamental group of the 3–manifold. In our
context, we mean that there are no embedded incompressible tori or Klein bottles, other
than tori isotopic to boundary components. In Corollary 3.3 and Remark 3.4 we highlight
this distinction.
Note that ifM is orientable, it is suﬃcient to consider only normal 2-spheres and tori,
except in the special case thatM is a twistedI-bundle over a Klein bottle. For any embedded
normal projective plane or Klein bottle must be one-sided, so the boundary of a small regular
neighbourhood is a normal 2-sphere or torus. However in the non-orientable case, one must
8 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
consider two-sided projective planes and Klein bottles. In this paper we will consider only
the orientable case.
Deﬁnition 2.8.If e∈ T(1) is any edge, then there is a sequence(qn1,...,q nk) of normal
quadrilateral types facinge, which consists of all normal quadrilateral types dual toe listed
in sequence as one travels arounde. Then k equals the degree ofe, and a normal quadri-
lateral type may appear at most twice in the sequence. This sequence is called thenormal
quadrilateral type sequencefore and is well-deﬁned up to cyclic permutations and reversing
the order.
Deﬁnition 2.9.A functionα: □→ R is called ageneralised angle structure on(M, T) if it
satisﬁes the following two properties:
(1) If σ3∈ T(3) and q,q′,q′′ are the three normal quadrilateral types supported by it,
then
α(q) +α(q′) +α(q′′) =π.
(2) Ife∈ T(1) is any edge and(qn1,...,q nk) is its normal quadrilateral type sequence, then
k∑
i=1
α(qni) = 2π.
Dually, one can regardα as assigning anglesα(q) to the two edges oppositeq in the tetra-
hedron containingq. The triangulations we consider are of oriented manifolds, so we may
assume that the triangulation is also oriented. We ﬁx an orderingq→q′→q′′→q on these
quad types, well deﬁned up to cyclic permutation. See Figure 2.
q q′ q′′
Figure 2. The three quad types within an oriented tetrahedron, arranged in
our chosen cyclic order.
Deﬁnition 2.10.If we restrict the angles of a generalised angle structure to be in
• [0,π ], then the generalised angle structure is asemi-angle structure.
• (0,π ), then the generalised angle structure is astrict angle structure.
•{ 0,π}, then the generalised angle structure is ataut angle structure.
The set of generalised angle structures is denoted byGA(T) and is an aﬃne subspace ofR3N,
where N is the number of tetrahedra inT. The subset of semi-angle structures is denoted
by SA(T), and is a closed polytope inGA(T).
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 9
Remark 2.11. Itiseasytoseethatatautanglestructurecanonlyhappenifeverytetrahedron
has a pair of opposite edges with anglesπ and the other four edges have angles0.
Deﬁnition2.12.Foranidealtriangulation T withN tetrahedra, aquad-choice isanelement
Q = (Q1,...,Q N)∈ □N such thatQn is a choice of one of the three quad types in thenth
tetrahedron. An index structureα on T consists of 3N generalised angle structures, indexed
by the quad-choices Q, with the property that αQ(Qn) > 0 for n = 1,...,N , for each
quad-choiceQ.
Deﬁnition 2.13.The equations determining a generalised angle structure can be read oﬀ
as threeN×N matrices A = (¯aij), B = (¯bij) and C = (¯cij) whose rows are indexed by the
N edges ofT and whose columns are indexed by theα(qj),α (q′
j),α (q′′
j ) variables respectively,
whereqj,q′
j,q′′
j are the quads type in thejth tetrahedron. These are the so-calledNeumann-
Zagier matricesthat encode the exponents of thegluing equationsof T, originally introduced
by Thurston [NZ85, Thu77]. In terms of these matrices, a generalised angle structure is a
triple of vectorsZ,Z′,Z′′∈ RN that satisfy the equations
(3) AZ + BZ′ + CZ′′ = 2π(1,..., 1)T, Z +Z′ +Z′′ =π(1,..., 1)T.
Note that the matrix entries ¯aij,¯bij, ¯cij give the coeﬃcients ofZj,Z′
j,Z′′
j in the ith edge
equation corresponding to the edges of tetrahedronj facing quad typesqj,q′
j,q′′
j respectively.
We can combine these into a single matrix equation
(4)
(
A B C
IN IN IN
)

Z
Z′
Z′′

 =
(
2π(1,..., 1)T
π(1,..., 1)T
)
,
where IN is theN×N identity matrix. We call this matrix equationthe matrix form of the
generalised angle structure equations.
