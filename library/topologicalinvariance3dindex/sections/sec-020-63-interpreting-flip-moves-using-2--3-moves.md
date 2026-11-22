---
doc_id: topologicalinvariance3dindex
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-020-63-interpreting-flip-moves-using-2--3-moves
section_title: "Interpreting flip moves using 2--3 moves"
section_number: 6.3
pages: 39-40
source_pdf: topological.invariance.3Dindex.pdf
source_sha256: 22953b4eee66dca2
toc_source: outline
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
---
ip moves using 23 moves. In order to carry out step (1) of our plan
in Remark 6.31, we will interpret the 
ip moves in terms of the 23 and 32 moves allowed
in Theorem 1.1.
40 STAVROS GAROUFALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
(1) First, consider a 23 
ip in one polyhedron. This is simply a 23 move. Since the
triangulations on either side of the move are in XEP
M , they are both 1e
cient by
Remark 6.18. Therefore the triangulations have the same index by Theorem 1.1.
(2) Second, consider an external 22 
ip. See Figure 19a. The base of the pyramid is on
a face of the polyhedron that is glued to a polygonal pillow. The two triangles on
the base of the pyramid are glued to either a single tetrahedron in the pillow, or two
tetrahedra in either the polygonal pillow or the polyhedron on the other side of the
polygonal pillow.
• If the two triangles are glued to a single tetrahedron then we are in the situation
shown in the top diagram of Figure 19a, and we can perform a 32 move, which
performs the 
ip to the polyhedron, and removes the single tetrahedron from
the layered triangulation of the polygonal pillow.
• Otherwise, we perform a 23 move, which performs the 
ip to the polyhedron,
and adds a 
at tetrahedron to the layered triangulation of the polygonal pillow.
(Note that we could use only this move, even in the previous case; the dierence
between the two options is a 02 move.)
Once again, the triangulations on either side of the move are in XEP
M , so they are both
1e
cient and the triangulations have the same index.
(3) Lastly, consider an internal 22 
ip. See Figure 19b. We can perform a 23 move
followed by a 32 move, which together perform the 
ip. Since the four vertices in
the circuit are coplanar, at the intermediate step we introduce a 
at tetrahedron.
The intermediate triangulation is not in XEP
M , since it includes a 
at tetrahedron in a
polyhedron, and so the polyhedron does not have a regular triangulation. However,
the intermediate triangulation still has a natural semiangle structure in the obvious
way, and so it is 1e
cient, and again the three triangulations involved all have the
same index.
The arguments so far show that we can achieve step (1) of Remark 6.31. Now we need to
deal with step (2).
