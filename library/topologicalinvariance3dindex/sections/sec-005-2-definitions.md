---
doc_id: topologicalinvariance3dindex
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-005-2-definitions
section_title: "Definitions"
section_number: 2
pages: 6-9
source_pdf: topological.invariance.3Dindex.pdf
source_sha256: 22953b4eee66dca2
toc_source: outline
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
---
De
nition 2.1. Let M be a topologically 
nite 3-manifold which is the interior of a compact
3-manifold with torus boundary components. An ideal triangulation T of M consists of a
pairwise disjoint union of standard Euclidean 3simplices e∆= ∪n
k=1 e∆k with vertex set e∆(0),
together with a collection Φ of Euclidean isometries between the 2simplices in e∆, called
face pairings, such that the quotient space (e∆\ e∆(0))/Φ is homeomorphic to M. The images
of the simplices in T may be singular in M.
De
nition 2.2. Let T be an ideal triangulation with at least 2 distinct tetrahedra. A 23
move can be performed on any pair of distinct tetrahedra of T that share a triangular face
t. We remove t and the two tetrahedra, and replace them with three tetrahedra arranged
around a new edge, which has endpoints the two vertices not on t. See Figure 1a. A 32
move is the reverse of a 23 move, and can be performed on any triangulation with a degree
3 edge, where the three tetrahedra incident to that edge are distinct.
De
nition 2.3. Let T be an ideal triangulation. A 02 move can be performed on any pair
of distinct triangular faces of T that share an edge e2. Around the edge e, the tetrahedra of
T are arranged in a cyclic sequence, which we call a book of tetrahedra. (Note that tetrahedra
may appear more than once in the book.) The two triangles and e separate the book into two
halfbooks. We unglue the tetrahedra that are identi
ed across the two triangles, duplicating
the triangles and also duplicating e. We glue into the resulting hole a pair of tetrahedra
glued to each other in such a way that there is a degree 2 edge between them. See Figure 1b.
A 20 move is the reverse of a 02 move, and can be performed on any triangulation with a
degree 2 edge, where the two tetrahedra incident to that edge are distinct, there are no face
pairings between the four external faces of the two tetrahedra, and the two edges opposite
the degree 2 edge are not identi
ed.
Remark 2.4. A 02 move is also called a lune move in the dual language of standard
spines [Mat87, Mat07, Pie88, BP97]. In [Mat87, Lem.2.1.11] and [Pie88] (see also [Pet95,
Prop.I.1.13]) it was shown that a 02 move follows from a combination of 23 moves as long
as the initial triangulation has at least 2 ideal tetrahedra.
De
nition 2.5. Let ∆3 be the standard 3simplex with a chosen orientation. Each pair of
opposite edges corresponds to a normal isotopy class of quadrilateral discs in ∆3, disjoint
from the pair of edges. We call such an isotopy class a normal quadrilateral type. Each vertex
of ∆3 corresponds to a normal isotopy class of triangular discs in ∆3, disjoint from the face
of ∆3 opposite the vertex. We call such an isotopy class a normal triangle type. Let T(k)
2Unlike for the 23 move, it is possible to make sense of the 02 move when the two triangles are not
distinct. However, we will not make use of this variant in this paper.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD
7
23
32
(a) The 23 and 32 moves.
02
20
(b) The 02 and 20 moves.
Figure 1. Moves on (topological) triangulations.
be the set of all ksimplices in T. If σ ∈T(3), then there is an orientation preserving map
∆3 →σ taking the ksimplices in ∆3 to elements of T(k), and which is a bijection between
the sets of normal quadrilateral and triangle types in ∆3 and in σ. Let □and △denote the
sets of all normal quadrilateral and triangle types in T respectively.
De
nition 2.6. Given a 3-manifold M with an ideal triangulation T, the normal surface
solution space C(M; T) is a vector subspace of R7n, where n is the number of tetrahedra
in T, consisting of vectors satisfying the compatibility equations of normal surface theory.
The coordinates of x ∈R7n represent weights of the four normal triangle types and the
three normal quadrilateral types in each tetrahedron, and the compatibility equations state
that normal triangles and quadrilaterals have to meet the 2simplices of T with compatible
weights.
A vector in R7n is called admissible if at most one quadrilateral coordinate from each
tetrahedron is non-zero and all coordinates are non-negative. An integral admissible element
of C(M; T) corresponds to a unique embedded, closed normal surface in (M, T) and vice
versa.
De
nition 2.7. (See [JR03], [KR05]) An ideal triangulation T of an orientable 3-manifold is
0-e
cient if there are no embedded normal 2-spheres or one-sided projective planes. An ideal
triangulation T is 1-e
cient if it is 0-e
cient, the only embedded normal tori are vertex-
linking and there are no embedded one-sided normal Klein bottles. An ideal triangulation T
is strongly 1-e
cient if there are no immersed normal 2spheres, projective planes or Klein
bottles and the only immersed normal tori are coverings of the vertex-linking tori.
Note that in some contexts, atoroidal is taken to mean that there is no immersed torus
whose fundamental group injects into the fundamental group of the 3manifold.
In our
context, we mean that there are no embedded incompressible tori or Klein bottles, other
than tori isotopic to boundary components. In Corollary 3.4 and Remark 3.5 we highlight
this distinction.
Note that if M is orientable, it is su
cient to consider only normal 2-spheres and tori,
except in the special case that M is a twisted I-bundle over a Klein bottle. For any embedded
normal projective plane or Klein bottle must be one-sided, so the boundary of a small regular
neighbourhood is a normal 2-sphere or torus. However in the non-orientable case, one must
8
STAVROS GAROUFALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
consider two-sided projective planes and Klein bottles. In this paper we will consider only
the orientable case.
De
nition 2.8. If e ∈T(1) is any edge, then there is a sequence (qn1, ..., qnk) of normal
quadrilateral types facing e, which consists of all normal quadrilateral types dual to e listed
in sequence as one travels around e. Then k equals the degree of e, and a normal quadri-
lateral type may appear at most twice in the sequence. This sequence is called the normal
quadrilateral type sequence for e and is well-de
ned up to cyclic permutations and reversing
the order.
De
nition 2.9. A function α: □→R is called a generalised angle structure on (M, T) if it
satis
es the following two properties:
(1) If σ3 ∈T(3) and q, q′, q′′ are the three normal quadrilateral types supported by it,
then
α(q) + α(q′) + α(q′′) = π.
(2) If e ∈T(1) is any edge and (qn1, ..., qnk) is its normal quadrilateral type sequence, then
k
X
i=1
α(qni) = 2π.
Dually, one can regard α as assigning angles α(q) to the two edges opposite to q in the
tetrahedron containing q. The triangulations we consider are of oriented manifolds, so we
may assume that the triangulation is also oriented. We 
x an ordering q →q′ →q′′ →q on
these quad types, well de
ned up to cyclic permutation. See Figure 2.
q
q′
q′′
Figure 2. The three quad types within an oriented tetrahedron, arranged in
our chosen cyclic order.
De
nition 2.10. If we restrict the angles of a generalised angle structure to be in
• [0, π], then the generalised angle structure is a semi-angle structure.
• (0, π), then the generalised angle structure is a strict angle structure.
• {0, π}, then the generalised angle structure is a taut angle structure.
The set of generalised angle structures is denoted by GA(T) and is an a
ne subspace of R3N,
where N is the number of tetrahedra in T. The subset of semi-angle structures is denoted
by SA(T), and is a closed polytope in GA(T).
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD
9
Remark 2.11. It is easy to see that a taut angle structure can only happen if every tetrahedron
has a pair of opposite edges with angles π and the other four edges have angles 0.
De
nition 2.12. For an ideal triangulation T with N tetrahedra, a quad-choice is an element
Q = (Q1, . . . , QN) ∈□N such that Qn is a choice of one of the three quad types in the nth
tetrahedron. An index structure α on T consists of 3N generalised angle structures, indexed
by the quad-choices Q, with the property that αQ(Qn) > 0 for n = 1, . . . , N, for each
quad-choice Q.
De
nition 2.13. The equations determining a generalised angle structure can be read o
as three N × N integer-valued matrices A = (¯aij), B = (¯bij) and C = (¯cij) whose rows
are indexed by the N edges of T and whose columns are indexed by the α(qj), α(q′
j), α(q′′
j )
variables respectively, where qj, q′
j, q′′
j are the quad types in the jth tetrahedron. These are
the so-called Neumann-Zagier matrices that encode the exponents of the gluing equations of
T, originally introduced by Thurston [NZ85, Thu77]. In terms of these matrices, a generalised
angle structure is a triple of vectors Z, Z′, Z′′ ∈RN that satisfy the equations
(3)
A Z + B Z′ + C Z′′ = 2π(1, . . . , 1)T,
Z + Z′ + Z′′ = π(1, . . . , 1)T .
Note that the matrix entries ¯aij,¯bij, ¯cij give the coe
cients of Zj, Z′
j, Z′′
j in the ith edge
equation corresponding to the edges of tetrahedron j facing quad types qj, q′
j, q′′
j respectively.
We can combine these into a single matrix equation
(4)

A
B
C
IN
IN
IN
 

Z
Z′
Z′′

=

2π(1, . . . , 1)T
π(1, . . . , 1)T

,
where IN is the N × N identity matrix. We call this matrix equation the matrix form of the
generalised angle structure equations.
