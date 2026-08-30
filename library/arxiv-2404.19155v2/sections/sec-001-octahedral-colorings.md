---
doc_id: arxiv-2404.19155v2
doc_title: "Octahedral coordinates from the Wirtinger presentation Calvin McPhail-Snyder Duke University calvin@sl2.site"
section_id: sec-001-octahedral-colorings
section_title: "Octahedral colorings"
section_number: null
pages: 3-7
source_pdf: 2404.19155v2.pdf
source_sha256: 45b9ed90006536b3
doc_brief: "Octahedral coordinates from the Wirtinger presentation Calvin McPhail-Snyder Duke University calvin@sl2.site — Letρ be a representation of a knot group (or more generally, the funda- mental group of"
---
from a representation of the fundamental group of the tangle complement given in terms
of the Wirtinger presentation.
Section 3 We describe the geometrically-derived holonomy of an octahedral coloring and use
it to justify our definition of the octahedral coloring associated to a representation.
Section 4 We explain how conjugating a representation ρ acts on the induced octahedral
coloring and use this to show that every representation is conjugate to one coming from
a coloring.
Section 5 We give some applications of our results to the Neumann-Zagier–Yokota potential
function and the Volume Conjecture.
Acknowledgements
I would like to thank Andy Putman for a comment on my MathOverflow question [McP23]
about knot groups that led me to the proof of Theorem 3. I would also like to thank Seonhwa
Kim for some useful comments on an early draft of the paper and for introducing me to relevant
work of Sakuma and Yokota [SY18] and Garoufalidis, Moffatt, and Thurston [GMT16]. Finally,
I thank the anonymous referee for helpful comments that lead to an improved exposition.
Conventions
All tangles are smooth and oriented. Our convention is that tangle diagrams go from left to right,
so composition of tangles is horizontal and disjoint union is vertical. Our sign conventions the
2. Octahedral colorings 3
1
2
2′
1′
1
2
2′
1′
Figure 1: Positive (left) and negative (right) crossings with our standard labeling.
1 Usually these are called the “edges” of the
diagram, but we do not want to confuse them
with edges of ideal polyhedra in the octahe-
dral decomposition.
j =i↑
j′ =i↓
i
Figure 2: In this case we say that regionj′ is
below regionj across segmenti. We write
j = i↑ andj′ = i↓ to refer to the regions
adjacent to segmenti.
2 Such a coloring will necessarily assign ev-
ery segment in an arc the same group element,
but we will soon consider octahedral color-
ings that do not have this property.
and typical labeling of the parts of a crossing are given in Figure 1. Composition of paths is also
read left to right:fg means followf theng. For this reason we usually assume an eigenvector
is a row vector, not a column vector. However, we writee1, e2 for the standard column vector
basis of C2. For (column) vectorsu1,u 2 we write det (u1,u 2) for the determinant of the matrix
with columnsu1,u 2, i.e. for the standard antisymmetric pairing on C2.
2. Octahedral colorings
Definition 2.1. The complement of a tangleT is its complement as a submanifold of [0, 1]3.
We writeπ(T ) for the fundamental group of the complement. SupposeT hasn incoming and
m outgoing boundary points and letD be a diagram ofT . We can think ofD as a decorated
4-valent graphG embedded in [0, 1]× [0, 1] withn edges intersecting [0, 1]×{ 0} andm edges
intersecting [0, 1]×{ 1}. We assign names to various parts ofD:
• The segments ofD are the edges1 ofG.
• An arc ofD is a set of adjacent over-segments.
• A component ofD is a set of adjacent segments; these are in bijection with connected
components ofT .
• A region ofD is a connected component of the complement ofG, equivalently a vertex
of the dual graph ofG. Regions are adjacent across segments, and our convention is to
say that regionj′ is below regionj when they are arranged as in Figure 2. In this case
we callj the region abovei and writej =i↑. Similarlyj′ is the region belowi, written
j =i↓.
Proposition 2.2. LetD be a diagram of a tangleT . The choice ofD gives a presentation for
π(T ) with one generatorwi for each arc and one relation
w2′ =w−1
1 w2w1 (positive) (1)
w1′ =w2w1w−1
2 (negative) (2)
at each crossing, where the indices are as in Figure 1. (At a positive crossing 1 and 1′ are
the same arc.) We call this the Wirtinger presentation ofπ(T ) and denote it byπ(D). Ifi is a
segment ofD we writewi for the associated Wirtinger generator. ⌟
Definition 2.3. LetD be a diagram of a tangleT andG be a group. A G-coloring ofD is a
functioni7→gi assigning each segment an element ofg, subject to the Wirtinger relations (1)
and (2) at each crossing.2
2. Octahedral colorings 4
(g1,L 1)
(g2,L 2)
(g−1
1 g2g1,L 2g1)
(g1,L 1)
(g1,L 1)
(g2,L 2)
(g2,L 2)
(g2g1g−1
2 ,L 1g−1
2 )
Figure 3: Rules for decorated SL2(C) colorings.
By Proposition 2.2G-colorings ofD are in bijection with representationsρ :π(D)→G.
It turns out that octahedral coordinates correspond to slightly more data: they describe both a
representation ofπ(T ) and some extra data on the boundary of a regular neighborhood ofT .
Definition 2.4. A decorated representation ρ of a tangle T is a representation ρ : π(T )→
SL2(C) with a choice of invariant line for each meridian ofT .
More formally, each componenti of the oriented tangle has a conjugacy class of meridians
[wi]⊂ π(T ). For a representative wi we choose a line Li⊂ C2 (thought of as a set of row
vectors) with
Liρ(wi) =Li.
This does not depend on the choice of representative: ifw′
i =y−1wiy is any other representative
of the conjugacy class we assign it the lineLiρ(y), since
Liρ(y)ρ(y−1wiy) =Liρ(y).
This choice is called a decoration of componenti, and a decoration ofρ is a decoration of each
of its components. A decoration ofρ induces an equivalent decoration of any conjugateg−1ρg
in a similar way.
Generically a knot has two decorations, as a diagonalizable matrix has two eigenspaces.
When trρ(w) =±2 butρ̸=±1 is nontrivial (i.e. whenρ is boundary-parabolic) there is only
one decoration, and whenρ(w) =±1 is trivial there are infinitely many. Similar statements
apply to links and tangles.
Definition 2.5. A decorated SL2(C)-coloring assigns each segment i a group element gi∈
SL2(C) and a 1-dimensional subspaceLi⊂ C2 invariant undergi, subject to the rule that
L2′ =L2g1 (positive) (3)
L1′ =L1g2 (negative) (4)
These are summarized in Figure 3.
In our example we cannot multiply two segment colors because (g,L ) and (h,L′) do not
determine an eigenspace ofgh, but we can conjugate them. As such the set of pairs (g,L ) with
the binary operation
(g,L )◁ (h,L′) = (h−1gh,Lh )
form an algebraic structureQ called a quandle. Quandles generalize the conjugation structure
of a group and appear in many places in knot theory. Decorated SL2(C)-colorings can be
characterized as determining homomorphism from the fundamental quandle of the tangle to
Q.
2. Octahedral colorings 5
[KKY18] H. Kim, S. Kim, and S. Yoon, “Oc-
tahedral developing of knot complement. I:
Pseudo-hyperbolic structure”. arXiv doi
[McP22] C. McPhail-Snyder, Hyperbolic struc-
tures on link complements, octahedral decom-
positions, and quantum sl2. arXiv
Proposition 2.6. Decorated representationsρ :π(D)→ SL2(C) are in bijection with deco-
rated SL2(C)-colorings ofD. ⌟
Because SL2(C) is the double cover of the isometry group PSL2(C) of hyperbolic space a
choice ofρ :π(T )→ SL2(C) determines a (generalized) hyperbolic structure on the tangle
complement. However, this description is rather abstract, and frequently one wants to instead
describe the hyperbolic structure by gluing together geometric ideal tetrahedra. Any tangle
diagram determines an octahedral decomposition [KKY18; McP22] of its complement in a
standard way, which gives the topological data of the gluing. The geometric information is
determined by complex numbers called shape parameters, which are in turn determined by an
octahedral coloring of the digram as defined below. We discuss the shape parameters further
in Section 5.
Definition 2.7. An octahedral color is a tripleχ = (a,b,m )∈ (C\{ 0})3 of nonzero complex
numbers. When we work with an indexed set{χi}i∈I of colors we typically writeai,bi,mi
for their components. An octahedral coloring of a tangle diagramD is an assignmenti7→χi =
(ai,bi,mi) of an octahedral color to every segmenti so that at every positive crossing
a1′ =a1A−1
a2′ =a2A where
A = 1− m1b1
b2

1− a1
m1

1− 1
m2a2
(5)
b1′ = m2b2
m1

1−m2a2

1− b2
m1b1
−1
b2′ =b1

1− m1
a1

1− b2
m1b1
(6)
m1′ =m1 m2′ =m2(7)
and at every negative crossing
a1′ =a1 ˜A−1
a2′ =a2 ˜A where
˜A = 1− b2
m1b1
(1−m1a1)

1− m2
a2

.
(8)
b1′ = m2b2
m1

1− a2
m2

1− m1b1
b2

b2′ =b1

1− 1
m1a1

1− m1b1
b2
−1(9)
m1′ =m1 m2′ =m2(10)
Our goal is to obtain an octahedral coloring from a decoratedSL2(C)-coloring. The relevant
geometry of the ideal tetrahedra is most naturally described in terms of the face-pairing maps of
the triangulation. These define a representation of a fundamental groupoid with one basepoint
for each tetrahedron. This groupoid is closely related (but not quite the same as) the fundamental
groupoid studied in Section 3. In contrast, the Wirtinger generators are global and have a
single common basepoint. To relate these to the fundamental groupoid we need to keep track
of change-of-basepoint data using additional colors called shadows.
