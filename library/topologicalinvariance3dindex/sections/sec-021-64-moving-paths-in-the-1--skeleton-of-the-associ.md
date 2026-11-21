---
doc_id: topologicalinvariance3dindex
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-021-64-moving-paths-in-the-1--skeleton-of-the-associ
section_title: "Moving paths in the 1--skeleton of the associahedron using 2--3 and 0--2 moves"
section_number: 6.4
pages: 40-43
source_pdf: topological.invariance.3Dindex.pdf
source_sha256: 22953b4eee66dca2
toc_source: outline
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
---
moves. In order to carry out step (2) of our plan in Remark 6.31, we need to modify the
layered triangulations in the polygonal pillows. We will do this using the 23, 32, 02 and
20 moves allowed in Theorems 1.1 and 5.1.
Having completed step (1), we have two triangulations, T1 and T2, which agree on the
polyhedra but may dier in the polygonal pillows. Let Q be a polygonal pillow. Since T1
and T2 agree on the polyhedra glued to either side of Q, they agree on the triangulations of
the polygonal faces Q+ and Q−. Call these triangulations t+ and t−.
The next well-known theorem concerns the identi
cation of the set of triangulations of
an n-gon with the vertices of the associahedron Kn−2, and the set of geometric bistellar

ips with the edges of Kn−2. The associahedron Kn−2 was introduced by Stashe [Sta63].
An identi
cation of Kn−2 with a convex polytope in Euclidean space was given in the ap-
pendix to [Sta97]. The cellular decomposition of the polytope Kn−2 (and in particular, its
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD
41
32
23
v1
v2
v3
v4
v1
v2
v3
v4
(a) Two possible ways to perform
an external 22 move, depending
on whether or not there is a suit-
able 
at tetrahedron in the polygo-
nal pillow that the base of the pyra-
mid is glued to.
22
23
32
v1
v2
v3
v4
(b) An internal 22 
ip, obtained
by performing a 23 move followed
by a 32 move. At the intermediate
step we get a 
at tetrahedron with
vertices v1 through v4.
Figure 19. The possible 22 moves on a triangulation of a point con
gura-
tion, realised using 23 and 32 moves. Again in each case, vertices v1 through
v4 are coplanar.
2-skeleton) is discussed at length in the above references and also in [Lod04]. The fact that
the 2-dimensional faces of the associahedron are squares and pentagons also follows from
MacLane's coherence theorem [Mac71]. A vast generalization of regular triangulations of
point con
gurations was studied by Gelfand-Kapranov-Zelevinsky, and in [GKZ94, Sec.7.3]
it is explained how to identify the secondary polytope of 2-dimensional con
gurations with
the associahedron.
Theorem 6.32. The set of triangulations of an ngon and the set of diagonal 
ips connecting
them correspond to the vertices and edges of a convex polytope called the associahedron. The
set of 2cells of the associahedron consists of squares and pentagons. Each square corresponds
to two commuting diagonal 
ips (as in De
nition 6.4) on two 4-gons whose interiors are
disjoint. Each pentagon corresponds to a pentagon relation between the 
ve triangulations
of a pentagon. See Figure 20.
Our two layered triangulations of the polygonal pillow Q can be represented as two paths
p1 and p2 in the 1skeleton of the associahedron that both start at the vertex corresponding to
t−and end at the vertex corresponding to t+. Since the fundamental group of the 2skeleton
X(2) of a CW complex X satis
es π1(X(2)) = π1(X), it follows that the 2skeleton of a
convex polytope is simply connected, and every loop along the 1-skeleton can be trivialized
by moving pieces of it across the 2-cells. It follows that the 2skeleton of the associahedron
is simply connected, and so we can homotope p1 to p2, 
xing endpoints, by moving the path
42 STAVROS GAROUFALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
(a) A square 2cell of the asso-
ciahedron.
(b) A pentagon 2cell of the associahedron.
Figure 20. The 2cells of the associahedron.
across some 
nite sequence of the 2cells. To be precise, we can homotope p1 to p2 with a
combination of the following moves and their inverses.
(1) Remove a backtracking, that is, replace a segment of a path of the form . . . , t1, t2, t1, . . .
with . . . , t1, . . ., where t1 and t2 are related by a diagonal 
ip.
(2) Move a path that follows two consecutive sides of a square 2cell to follow the other
two sides.
(3) Move a path that follows three consecutive sides of a square 2cell to follow the other
side.
(4) Delete a part of a path that goes around all four sides of a square 2cell.
(5) Move a path that follows three consecutive sides of a pentagon 2cell to follow the
other two sides.
(6) Move a path that follows four consecutive sides of a pentagon 2cell to follow the
other side.
(7) Delete a part of a path that goes around all 
ve sides of a pentagonal 2cell.
These moves can be achieved as follows.
• Move (1) corresponds to performing a 20 move on the triangulation. Since the two
triangulations are both in XEP
M , they are both 1e
cient by Remark 6.18. Therefore
the two triangulations have the same index by Theorem 5.1.
• Move (2) does not change the layered triangulation at all, it only swaps the order in
which we add two non-overlapping 
at tetrahedra to the layering.
• Move (3) can be made by applying move (2) followed by move (1).
• Move (4) can be made by applying move (2) followed by move (1) twice.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD
43
• Move (5) corresponds to performing a 32 move on the triangulation. As before,
since the two triangulations are both in XEP
M , they are both 1e
cient by Remark
6.18. Therefore the two triangulations have the same index by Theorem 1.1(b).
• Move (6) can be made by applying move (5) followed by move (1).
• Move (7) can be made by applying move (5) followed by move (1) twice.
Proof of Theorem 1.8. We have shown in this section that given any two triangulations in
XEP
M , the steps in Remark 6.31 can be made using 23, 32, 02 and 20 moves which preserve
the index. Thus the entire class of triangulations has the same index. Since XEP
M depends
only on the topology of M, we can take the index of any of these triangulations for the value
of the index for the manifold, and this depends only on the topology of M.
□
Proof of Theorem 1.9. Fix a cusped hyperbolic manifold M and T ∈XEP
M . T consists of
two types of tetrahedra: the ones that subdivide the ideal hyperbolic cells of the Epstein-
Penner cell decomposition of M, and the ones that are parts of the pillows. The former
have geometric shapes (i.e., shapes that are in the upper half plane), and the latter have
real non-degenerate shapes. By construction, the shapes ZT satisfy the gluing equations of
T, proving part (a). Their arguments also satisfy the gluing equations, proving part (c).
Also by construction, the shapes ZT and ZT′ are related by 23, 32, 02 and 20 moves
if the corresponding triangulations T and T′ are related by the same moves.
□
