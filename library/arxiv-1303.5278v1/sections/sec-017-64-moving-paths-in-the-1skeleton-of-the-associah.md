---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-017-64-moving-paths-in-the-1skeleton-of-the-associah
section_title: "Moving paths in the 1–skeleton of the associahedron using 2–3 and 0–2 moves"
section_number: 6.4
pages: 41-43
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
moves. In order to carry out step (2) of our plan in Remark 6.30, we need to modify the
layered triangulations in the polygonal pillows. We will do this using the 2–3, 3–2, 0–2 and
2–0 moves allowed in Theorems 1.1 and 5.1.
Having completed step (1), we have two triangulations,T1 and T2, which agree on the
polyhedra but may diﬀer in the polygonal pillows. LetQ be a polygonal pillow. Since T1
and T2 agree on the polyhedra glued to either side ofQ, they agree on the triangulations of
the polygonal facesQ+ and Q−. Call these triangulationst+ and t−.
The next well-known theorem concerns the identiﬁcation of the set of triangulations of
an n-gon with the vertices of theassociahedronKn−2, and the set of geometric bistellar
ﬂips with the edges ofKn−2. The associahedron Kn−2 was introduced by Stasheﬀ [Sta63].
An identiﬁcation ofKn−2 with a convex polytope in Euclidean space was given in the ap-
pendix to [Sta97]. The cellular decomposition of the polytopeKn−2 (and in particular, its
2-skeleton) is discussed at length in the above references and also in [Lod04]. The fact that
the 2-dimensional faces of the associahedron are squares and pentagons also follows from
MacLane’s coherence theorem [Mac71]. A vast generalization of regular triangulations of
point conﬁgurations was studied by Gelfand-Kapranov-Zelevinsky, and in [GKZ94, Sec.7.3]
it is explained how to identify the secondary polytope of 2-dimensional conﬁgurations with
the associahedron.
Theorem6.31. The set of triangulations of ann–gon and the set of diagonal ﬂips connecting
them correspond to the vertices and edges of a convex polytope called theassociahedron. The
set of 2–cells of the associahedron consists of squares and pentagons. Each square corresponds
to two commuting diagonal ﬂips (as in Deﬁnition 6.4) on two 4-gons whose interiors are
disjoint. Each pentagon corresponds to apentagon relation between the ﬁve triangulations
of a pentagon. See Figure 20.
Our two layered triangulations of the polygonal pillowQ can be represented as two paths
p1 andp2 inthe1–skeletonoftheassociahedronthatbothstartatthevertexcorrespondingto
t− and end at the vertex corresponding tot+. Since the fundamental group of the 2–skeleton
X(2) of a CW complexX satisﬁesπ1(X(2)) = π1(X), it follows that the 2–skeleton of a
convex polytope is simply connected, and every loop along the 1-skeleton can be trivialized
by moving pieces of it across the 2-cells. It follows that the 2–skeleton of the associahedron
is simply connected, and so we can homotopep1 top2, ﬁxing endpoints, by moving the path
across some ﬁnite sequence of the 2–cells. To be precise, we can homotopep1 to p2 with a
combination of the following moves and their inverses.
(1) Removea backtracking, thatis, replaceasegmentofapathoftheform ...,t 1,t 2,t 1,...
with ...,t 1,... , wheret1 and t2 are related by a diagonal ﬂip.
(2) Move a path that follows two consecutive sides of a square 2–cell to follow the other
two sides.
(3) Move a path that follows three consecutive sides of a square 2–cell to follow the other
side.
(4) Delete a part of a path that goes around all four sides of a square 2–cell.
42 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
(a) A square 2–cell of the asso-
ciahedron.
(b) A pentagon 2–cell of the associahedron.
Figure 20. The 2–cells of the associahedron.
(5) Move a path that follows three consecutive sides of a pentagon 2–cell to follow the
other two sides.
(6) Move a path that follows four consecutive sides of a pentagon 2–cell to follow the
other side.
(7) Delete a part of a path that goes around all ﬁve sides of a pentagonal 2–cell.
These moves can be achieved as follows.
• Move (1) corresponds to performing a 2–0 move on the triangulation. Since the two
triangulations are both inXEP
M , they are both 1–eﬃcient by Remark 6.18. Therefore
the two triangulations have the same index by Theorem 5.1.
• Move (2) does not change the layered triangulation at all, it only swaps the order in
which we add two non-overlapping ﬂat tetrahedra to the layering.
• Move (3) can be made by applying move (2) followed by move (1).
• Move (4) can be made by applying move (2) followed by move (1) twice.
• Move (5) corresponds to performing a 3–2 move on the triangulation. As before,
since the two triangulations are both inXEP
M , they are both 1–eﬃcient by Remark
6.18. Therefore the two triangulations have the same index by Theorem 1.1(b).
• Move (6) can be made by applying move (5) followed by move (1).
• Move (7) can be made by applying move (5) followed by move (1) twice.
Proof of Theorem 1.8.We have shown in this section that given any two triangulations in
XEP
M , the steps in Remark 6.30 can be made using 2–3, 3–2, 0–2 and 2–0 moves which preserve
the index. Thus the entire class of triangulations has the same index. SinceXEP
M depends
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 43
only on the topology ofM, we can take the index of any of these triangulations for the value
of the index for the manifold, and this depends only on the topology ofM. □
Proof of Theorem 1.9.Fix a cusped hyperbolic manifoldM and T ∈ XEP
M . T consists of
two types of tetrahedra: the ones that subdivide the ideal hyperbolic cells of the Epstein-
Penner cell decomposition ofM, and the ones that are parts of the pillows. The former
have geometric shapes (i.e., shapes that are in the upper half plane), and the latter have
real non-degenerate shapes. By construction, the shapesZT satisfy the gluing equations of
T, proving part (a). Their arguments also satisfy the gluing equations, proving part (c).
Also by construction, the shapesZT and ZT′ are related by 2–3, 3–2, 0–2 and 2–0 moves
if the corresponding triangulationsT and T′ are related by the same moves. □
