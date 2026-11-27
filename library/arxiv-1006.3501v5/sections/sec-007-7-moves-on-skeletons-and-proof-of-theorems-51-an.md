---
doc_id: arxiv-1006.3501v5
doc_title: "On two approaches to 3-dimensional TQFTs"
section_id: sec-007-7-moves-on-skeletons-and-proof-of-theorems-51-an
section_title: "Moves on skeletons and proof of Theorems 5.1 and 6.1"
section_number: 7
pages: 16-22
source_pdf: 1006.3501v5.pdf
source_sha256: e939aec50387ce2d
toc_source: outline
doc_brief: "On two approaches to 3-dimensional TQFTs — W e prove that|M |C = τZ(C)(M ) for any closed oriented 3-manifold M and for any spherical fusion category C of non-zero dimension."
---
The proof of Theorems 5.1 and 6.1 given at the end of the section is ba sed on a
study of transformations of skeletons of a closed 3-manifold M .
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 17
7.1. Moves on skeletons. The symbols # v, #e, #r will denote the number of
vertices, edges, and regions of a skeleton of M , respectively. We deﬁne four moves
T1−T4 on a skeleton P ofM transformingP into a new skeleton of M , see Figure 3.
The “phantom edge move” T1 keeps P as a polyhedron and adds one new edge
connecting distinct vertices of P (this edge is an arc in P meeting P (1) solely at
its endpoints and has the valence 2). This move preserves # v, increases # e by 1,
and either preserves #r or increases #r by 1. The “contraction move” T2 collapses
into a point an edge e of P with distinct endpoints. This move is allowed only
when at least one endpoint of e is the endpoint of some other edge. The move T2
decreases both # v and #e by 1 and preserves # r. The “percolation move” T3
pushes a branch b of P through a vertex x of P . The branch b is pushed across a
small disk D lying in another branch of P atx so that D∩P (1) =∂D∩P (1) ={x}
and both these branches are adjacent to the same component of M\P . This move
preserves #v and increases both # e and #r by 1. The “bubble move” T4 adds
to P an embedded disk D+⊂M such that D+∩P =∂D+⊂P\P (1), the circle
∂D+ bounds a disk D− in P\P (1), and the 2-sphere D+∪D− bounds a ball
in M meeting P precisely along D−. A point of the circle ∂D+ is chosen as a
vertex and the circle itself is viewed as an edge of the resulting skelet on. This move
increases #v and #e by 1 and # r by 2.
PSfrag replacements T1 T2
PSfrag replacements
T1
T2
T3
PSfrag replacements
T1
T2
T3
T4
Figure 3. Local moves on skeletons
The orientation of the skeletons produced by the moves T1−T4 onP is induced
by the orientation of P except for the small disk regions created by T3, T4 whose
orientation is chosen arbitrarily.
The moves T1−T4 have obvious inverses. The move T −1
1 deletes a 2-valent
edge e with distinct endpoints; this move is allowed only when both endpoints
of e are endpoints of some other edges and the orientations on both sid es of e are
compatible. We call the moves T1−T4 and their inverses primary moves . In the
sequel, we tacitly assume the right to use ambient isotopies of skelet ons in M . In
other words, ambient isotopies are treated as primary moves.
Lemma 7.1. Any two skeletons of M can be related by primary moves.
We will prove this lemma in Section 7.4 using the deﬁnitions and results of the
next two subsections.
7.2. F urther moves. We introduce several additional moves on skeletons of M .
We begin with two versions T ′
4 and T ′′
4 of the bubble move, see Figure 4. The
moveT ′
4 adds to a skeleton P an embedded disk D+ as inT4 with the only diﬀerence
that the circle ∂D+ meets P (1) in a single point x and bounds a disk in a region r
18 V. TURAEV AND A. VIRELIZIER
of P . The move T ′
4 can be expanded as a product of primary moves as follows.
First, if x is not a vertex of P , then turn x into a vertex by T −1
2 . Then glue a disk
to r by T4. After that, T1 adds an edge in r connecting x to the vertex on this
circle, and ﬁnally T2 collapses this edge to a point. This gives T ′
4(P ).
The move T ′′
4 transforms P into P∪D+, where D+ is a disk in a small neigh-
borhood of a point of an edge e ofP such that D+∩P =∂D+ and the set ∂D+∩e
consists of 2 points. Under this move, e splits into 3 subedges e1,e 2,e 3 numerated
so that ∂e2 =D+∩e. We construct a sequence of primary moves turning P∪D+
intoP . First, T2 collapses e2 to a point, then T −1
3 pushes∂D+ to one region. The
resulting skeleton is T ′
4(P ); by the above it can be transformed into P by primary
moves. The inverse sequence of moves transforms P into P∪D+. Thus, T ′′
4 is a
composition of primary moves.
PSfrag replacements
T ′
4
PSfrag replacements
T ′
4
T ′′
4
Figure 4. The moves T ′
4 and T
′′
4
For any non-negative integersm,n withm+n≥ 1, we deﬁne a move on skeletons
T m,n, see Figure 5. This move is sometimes called a m + 1→n + 1 move for the
numbers of vertices in the picture before and after the move. The move T m,n
preserves orientation in all “big” regions; the orientation in the sma ll triangular
regions created or destroyed by T m,n may be arbitrary. In the case n = 0, this move
is allowed only when the orientations of the top and bottom regions on the left are
compatible. The move inverse to T m,n is T n,m. Note that T m,n is a composition
of primary moves. To see this, split T m,n as a product of a move T (m) and the
inverse of T (n) as shown in Figure 5. The move T (m) is obtained by applying m
times the move T2 to collapse the edges in the m− 1 small triangles on the left to
the vertex x and then applying T −1
3 to the vertical branch m− 1 times to remove
the loops at x resulting from the third edges of these triangles.
7.3. Special skeletons. We brieﬂy recall the theory of special skeletons due to
Casler, Matveev, and Piergallini (see, for example, Chapter 1 of [M at]). A special
2-polyhedron Q is a compact 2-polyhedron such that: all components of Int( Q)
are open 2-disks, Q\ Int(Q) has no circle components, and every point of Q has a
neighborhood homeomorphic to an open subset of the set
(10) {(x1,x 2,x 3)∈ R3|x3 = 0, orx1 = 0 andx3> 0, orx2 = 0 andx3< 0}.
Then Q\ Int(Q) is a graph with only 4-valent vertices. The edges of this graph
yield a canonical stratiﬁcation of Q; this turns Q into a stratiﬁed 2-polyhedron. All
edges of Q have valence 3 and all vertices of Q are adjacent to 6 branches. Since
all regions of Q are disks, Q is orientable.
A special skeleton or shorter an s-skeleton of a closed 3-manifold M is an oriented
special 2-polyhedron Q⊂ M such that M\Q is a disjoint union of open 3-balls.
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 19
PSfrag replacements
T m,n
{ }
T (m)
(T
(n) )−1
m
n
Figure 5. The move T m,n
Any s-skeleton of M is a skeleton of M in the sense of Section 6.2. For example, the
2-skeleton of the cellular subdivision of M dual to a triangulation is a s-skeleton
of M (the regions are provided with arbitrary orientation).
Lemma 7.2. Any skeleton P of M can be transformed by the primary moves into
a special skeleton.
Proof. The transformation proceeds in ﬁve steps.
Step 1. Adding if necessary new edges by T1, we can ensure that all regions of P
are disks. This condition will be preserved through the rest of the c onstruction.
Step 2. Let e be an edge of P of valence 2. We apply T ′′
4 at a point of e. Let
e1,e 2,e 3 be the subedges of e as in the deﬁnition of T ′′
4 . Delete e2 via T −1
1 and
contract both e1 and e3 via T2 (the orientation of the small disks created by T ′′
4
should be chosen so that T −1
1 can be applied). The resulting skeleton has one 2-
valent edge less and two new trivalent edges. Continuing by induction , we obtain
a skeleton, still denoted P , whose all edges have valence ≥ 3.
Step 3. If P has an edge e of valence n≥ 4, then apply T −1
2 to add a new
vertexx insidee. This splits e into two subedges e1 ande2. Next apply T3 pushing
one of the branches of P at x across a small disk D lying in an adjacent branch
and touching e atx. This move creates a trivalent edge ∂D and keeps all the other
edges. Then apply T −1
2 to insert a new edge e+ between e1 and e2. The valence
ofe+ isn− 1. Finally, apply T2 twice to contract e1 ande2. The resulting skeleton
diﬀers from the original one in that the edge e is replaced with a trivalent edge
and an ( n− 1)-valent edge. Continuing by induction, we obtain a skeleton, still
denoted P , whose all edges are trivalent.
Step 4. Let ( ∂Bx, Γ x) be the link of a vertex x∈ P . If the graph Γ x is dis-
connected, then we modify P near x as follows. Pick two edges α1,α 2 of Γ x lying
on diﬀerent components of Γ x and adjacent to the same component of ∂Bx\ Γ x.
Let bi be the branch of P at x containing αi and let ui,v i be the endpoints of αi
for i = 1, 2 (possibly, ui = vi). The branches b1, b2 are adjacent to the same
component X of M\P . Apply T ′
4 adding to P a disk D+ so that x∈ ∂D+⊂ b1
and Int(D+)⊂ X. Then apply T3 to push D+ through x into b2. In the new
position, the circle ∂D+ is formed by a loop in b1 and a loop in b2, both based
at x. The graph Γ x is modiﬁed under this transformation as follows: one deletes
the edges α1,α 2 and adds a quadrilateral (formed by 4 vertices and 4 edges) and
also 4 additional edges connecting the vertices of the quadrilatera l to u1,v 1,u 2,v 2,
respectively. The resulting graph has one component less than Γ x. Continuing by
induction, we obtain a skeleton, still denoted P , such that the link graphs of all
vertices of P are connected.
20 V. TURAEV AND A. VIRELIZIER
Step 5. At the previous steps we transformed the original skeleto n into a skele-
tonP such that all regions are disks, all edges are trivalent, and the link g raphs of all
vertices are connected. Since all edges of P are trivalent, P (1)∩ Int(P ) =∅. By the
deﬁnition of a stratiﬁed 2-polyhedron, P\P (1)⊂ Int(P ). Thus, Int( P ) = P\P (1)
is a disjoint union of open disks.
We call a vertex x ofP standard if there is a homeomorphism of a neighborhood
ofx inP onto the set (10) carrying x into the point (0, 0, 0). If all vertices of P are
standard, then all points of P have neighborhoods homeomorphic to an open subset
of (10), and the graph P (1) =P\Int(P ) has no circle components (every component
of P (1) contains a vertex of P and all vertices are incident to 4 half-edges). In this
case, P is a s-skeleton.
If a vertex x∈P is non-standard, then we “blow up” P in a neighborhood of x
as follows. Let B =Bx⊂M be a small (closed) ball neighborhood of x such that
P∩B is the cone over Γ x =P∩∂B . The connected trivalent graph Γ x splits the
2-sphere ∂B into 2-disks. Set
P ′ = (P\ Int(B))∪∂B.
The 2-polyhedron P ′ has the same edges and vertices as P except that all edges
incident to x are cut near x, the vertex x is deleted, and the edges and vertices
of Γ x are added. This turns P ′ into a stratiﬁed 2-polyhedron. The set M\P ′ is
a disjoint union of M\P and an open 3-ball. We provide the regions of P ′ lying
in P with the induced orientation and orient the regions of P ′ lying in ∂B in an
arbitrary way. This turn P ′ into a skeleton of M . Since all edges of P are trivalent,
the graph Γ x is trivalent, i.e., every vertex of Γ x is incident to three half-edges of Γ x.
Therefore all new vertices of P ′ are standard. Below we construct a sequence of
primary moves P ′→P . The inverse sequence transforms P in P ′. Blowing up P
at all non-standard vertices, we transform P into a s-skeleton.
To construct a sequence of primary moves P ′ → P , pick a maximal tree in
Γ x ⊂ (P ′)(1) and collapse it to a point by several T2-moves. This gives a new
skeletonP ′′ ofM . The edges of P ′′ lying in ∂B are trivalent loops forming a wedge
of n≥ 1 circles based at a point y∈ ∂B . At least one of these loops, S, bounds
a disk D⊂∂B in the complement of the other loops. Let b⊂∂B\ Int(D) be the
region of P ′′ adjacent to S from the exterior, and let b′⊂ (M−B)∪S be the
third region of P ′′ adjacent to S. If n≥ 2, then applying T −1
3 to b at the vertex y
of P ′′, we change the way in which b is glued to the rest of P ′′ so that ∂b does not
pass along S anymore. Under this move, the region D of P ′′ unites with b′. After
the move, the regions of P ′′∩∂B distinct from D form a 2-sphere meeting the rest
of the skeleton along a wedge of n− 1 loops. Continuing by induction we reduce
ourselves to the case n = 1. In this case, apply ( T ′
4)−1 once. This gives a skeleton
isotopic to P . □
7.4. Proof of Lemma 7.1. In view of Lemma 7.2, we need only to prove that
any two s-skeletons of M can be related by primary moves. By MP-moves on s-
skeletons (for Matveev and Piergallini), we mean the moves T 2,1, T 1,2 = (T 2,1)−1,
and (T ′′
4 )±1, see Figure 6 for T 2,1. All MP-moves transform s-skeletons into s-
skeletons and are compositions of primary moves. Therefore it is en ough to show
that any two s-skeletons of M are related by MP-moves. Applying if necessary T ′′
4 ,
we can ensure that given s-skeletons have ≥ 2 vertices, and that their complements
in M consist of the same number of open 3-balls. By Theorem 1.2.5 of [Mat], the
special 2-polyhedra underlying these s-skeletons can be related b y a ﬁnite sequence
of moves T 1,2, T 2,1. This implies our claim up to the choice of orientation of the
regions. The latter indeterminacy can be eliminated because for any region r of a
s-skeleton P , there is a sequence of MP-moves transforming P into P−, where P−
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 21
is P with opposite orientation in r and the same orientation in all other regions.
Indeed, the branches of P adjacent to the sides of r form a cylinder neighborhood
of ∂r in P− Int(r). Pushing r in a normal direction so that ∂r sweeps half of this
cylinder, we obtain a solid cylinder r× [0, 1]⊂ M meeting P at r∪ (∂r× [0, 1]),
wherer =r×{ 0}. Set r′ =r×{ 1}. Then P ′ =P∪r′ is a s-skeleton of M , where
the regions of P ′ contained in P receive the induced orientation and the orientation
of the region r′ is opposite to that of r. We can transform P ′ intoP by MP-moves
pushing ∂r ′ inside r and eventually eliminating r′. This transformation involves
one move T 1,2, several moves T 2,1, and one move ( T ′′
4 )−1 at the end. A similar
elimination of r from P ′ givesP−. Hence P and P− are related by MP-moves.
PSfrag replacements
T 2,1
Figure 6. The move T 2,1
7.5. Proof of Theorems 5.1 and 6.1. The state sum |M|C does not depend on
the choice of the representative set I by the naturality of FC and of the contraction
maps. By Lemma 7.1, to prove the rest of the theorems, we need on ly to prove the
invariance of the right-hand side of Formula (9) under the moves T1−T4 on P .
The move P
T1
→ P ′ involves two distinct vertices of P and modiﬁes their link
graphs by adding a new vertex u (respectively, v) inside an edge. The colorings
of P ′ assigning diﬀerent colors to the regions of P ′ lying on diﬀerent sides of the
new edge contribute zero to the state sum by Lemma 4.2(a) (there are no such
colorings if these regions coincide). The colorings of P ′ assigning the same color
i∈I to these regions contribute the same as the colorings of P assigning i to the
region of P containing the new edge:
(11) ∗u,v FC

PSfrag replacementsi i
i i
u
v

 = FC

PSfrag replacements
iuv
i
i

 = (dim( i))−1 FC

PSfrag replacements
iuv
i
i

 .
Here the ﬁrst equality follows from Lemma 4.2(d) and the second equ ality can be
deduced from this lemma or proved directly using that Hom C(i⊗i∗, 1) = k evi
and Hom C(1,i⊗i∗) = k coevi. The factor dim( i) on the right-hand side of (11) is
compensated by the change in the Euler characteristics of the reg ions.
The invariance under T2 follows from Lemma 4.2(d). The invariance under T3
follows from Lemma 4.2(c) with two vertical strands on the left-han d side. Here
i∈I is the color of the disk region created by the move. The invariance un der T4
follows from Lemma 4.3. Here i∈I is the color of the big region where the move
proceeds and k,l ∈ I are the colors of the small disks created by the move. The
factor dim(i) dim(C) is compensated by the change in the number of components of
M\P and in the Euler characteristic. We use the equality ∗e(FC(Γ v)) = N 1
i⊗k⊗l,
where e and v are respectively the edge and the vertex forming the boundary of
the small disks.
22 V. TURAEV AND A. VIRELIZIER
7.6. Remarks. 1. The invariant|M|C of a closed connected oriented 3-manifold M
can be generalized to an arbitrary spherical fusion category C (without the assump-
tion that dim(C) is invertible in k). Indeed, the right-hand side of Formula (9) is
the product of (dim(C))−|P | and a certain sum which we denote Σ C(P ). The deﬁni-
tion of Σ C(P )∈ k applies to an arbitrary spherical fusion category C. Let us call a
special skeleton P⊂M an s-spine ifM\P is an open ball and P has at least two
vertices. By [Mat], M has a s-spine P and any two s-spines of M can be related
by the moves T 1,2, T 2,1 in the class of s-spines. The arguments above imply that
Σ C(P ) is preserved under these moves. Therefore ||M||C = Σ C(P ) is a topological
invariant of M . If dim(C) is invertible, then ||M||C = dim(C)|M|C.
2. A stratiﬁed 2-polyhedron P ′ is a subdivision of a stratiﬁed 2-polyhedron P if
they have the same underlying 2-polyhedron, all vertices of P are among the vertices
of P ′, and all edges of P are unions of edges of P ′. Then P ′\ (P ′)(1)⊂ P\P (1)
and therefore an orientation of P induces an orientation of P ′. If P is a skeleton of
a closed 3-manifold M , then any subdivision P ′ of P is also a skeleton of M . As
an exercise, the reader may relate P and P ′ by the moves T ±1
1 , T ±1
2 .
