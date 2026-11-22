---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-031-appendix-a-the-23-move
section_title: "Appendix A. The 2–3 move"
section_number: null
pages: 51-57
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
toc_source: outline
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
For completeness, in this appendix we give a detailed proof of the invariance of the index
under 2–3 moves, following [Garb, Sec.6] and also [DGGa]. Let M be a cusped 3-manifold
and let ϖ be an oriented multi-curve on ∂M. Consider two ideal triangulations T and eT of
M with N and N + 1 tetrahedra, respectively, related by a 2–3 move as shown in Figure 23,
matching the conventions of [DG, Sec.3.6].
2–3
3–2
4
0
1
3
2
4
0
1
3
2
¯b1
¯c1
¯a1
¯b2 ¯b3
¯a2
¯c3
¯c2 ¯a3
¯b1
¯c1
¯a1
¯b2 ¯b3
¯a2
¯c3
¯c2 ¯a3
¯a3 ¯c1
¯c3 ¯a1
¯b3
¯b1
¯a2 ¯c3
¯c2 ¯a3
¯b2
¯b3
¯a1 ¯c2
¯c1 ¯a2
¯b1
¯b2
¯a0
¯b0
¯c0
¯a4
¯b4
¯c4
¯a0
¯b0
¯c0
¯a4
¯c4
¯b4
¯c0
¯a0
¯b0
¯b4
¯a4
¯c4
¯b0
¯c0
¯a0
¯c4
¯b4
¯a4
Figure 23. The 2–3 move shown with truncated tetrahedra and labelled
vertices.
The ﬁve triangulated ends of the tetrahedra before and after are
shown in detail in the “zoomed in” pictures. The labels on the corners of the
triangles are explained in Section 4.4. All truncated triangulation pictures are
viewed from outside the tetrahedra.
The main result of this section is the following.
Theorem A.1. Suppose that T and eT are ideal triangulations related by a 2–3 move and
both admit an index structure. Then, for any [ϖ] ∈H1(∂M; Z), IT([ϖ]) = IeT([ϖ]).
Recall that the index is not changed by isotopies of ϖ and, from (25), can be written in
the form
IT(ϖ)(q) =
X
k∈ZN−r
q
P
i ki Y
j
J(Tj; k, ϖ)
52 STAVROS GAROUFALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
where the contribution from tetrahedron Tj is
J(Tj; k, ϖ) = J∆(¯aj(k, ϖ),¯bj(k, ϖ), ¯cj(k, ϖ)).
Here we can think of k as a weight on the N edges of T and the summation is over ZN−r ⊂ZN
corresponding to a set B of N −r basic edges as in Theorem 4.3.
Deﬁnition A.2. Given ϖ as above and k ∈ZN, let ϖk denote a collection of disjoint
oriented normal curves in ∂M obtained from ϖ by adding ki small linking circles around the
vertex at one end of the ith edge in T. (The circles are oriented anticlockwise if ki > 0 and
clockwise if ki < 0.)
By Remark 4.1, we can think of the coeﬃcient ¯aj(k, ϖ) as the turning number ¯aϖk,j, as
deﬁned in Section 4.4, of ϖk. Thus ¯aj(k, ϖ) is a sum of 4 turning numbers of the multi-curve
ϖk as it turns around the ¯aj corners of the triangles of the jth truncated tetrahedron, and
similarly for ¯bj(k, ϖ) and ¯cj(k, ϖ). This point of view allows us to treat the contributions
from edge weights in the index calculation in the same way as we treat the contributions
from peripheral curves.
The triangulations T and eT only diﬀer inside a bipyramid, and we label its vertices
0, 1, 2, 3, 4 as in Figure 23, where 0 and 4 are the north and south poles, and 1, 2, 3 are
on the equator. This determines 5 tetrahedra T0, . . . , T4 where Ti is the tetrahedron “oppo-
site” vertex i with vertex set obtained by omitting vertex i from the set {0, 1, 2, 3, 4}. The
bipyramid can be decomposed into the two tetrahedra T0, T4 which contain the triangle 123,
or into the three tetrahedra T1, T2, T3 which contain the edge 04. Then it suﬃces to prove
the following lemma.
Lemma A.3 (Pentagon equality for J). Let ϖ be an oriented multi-curve on ∂M as above.
Let k = (k1, . . . , kN) be a weight function on the edges of T, and let ek = (k0, k) be an
extension of k to a weight function on the edges of eT where k0 is the weight on the new edge
04 introduced in the 2–3 move. Then, with the notation above,
(36)
X
k0∈Z
qk0J(T1; (k0, k), ϖ)J(T2; (k0, k), ϖ)J(T3; (k0, k), ϖ) = J(T0; k, ϖ)J(T4; k, ϖ).
Theorem A.1 now follows immediately: In the sum (25) for IT we choose a set X of excluded
edges from a maximal tree with 1- or 3-cycle for T as in Theorem 4.3. Then the same set
of edges can be excluded from the summation for IeT, so the summation for IeT is over the
original set of basic edges B for T together with the new edge introduced in the 2–3 move.
Proof of Lemma. The plan is as follows. First, we isotope ϖ if necessary, so that it intersects
the truncated ends of the bipyramid involved in the 2–3 move in a standardised way. For a
given k, we consider ϖk, and the ϖek where ek = (k0, k) and k0 ∈Z. We calculate the left
hand side of (36) using the ϖek, and use the original version of the pentagon equality, (10),
to show that it is equal to the right hand side of (36), calculated using ϖk.
So, ﬁrst we arrange ϖ appropriately.
The induced triangulations of ∂M, T∂and eT∂,
determined by T and eT respectively are related by 1–3 and 2–2 moves as seen in Figure
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD
53
23. We isotope ϖ if necessary, so that it is normal relative to both of the two induced
triangulations of ∂M.
At each of the polar vertices of the bipyramid there is a 1–3 move on the boundary, and
we can assume, after a further isotopy if necessary, that ϖ is represented by collections of
oriented normal arcs as shown in Figure 24, with all turning numbers 0 at the new central
vertex.
¯a
¯b
¯c
¯a ¯a
¯b
¯b
¯c
¯c
Figure 24. Change in turning numbers under a 1–3 move
At each of the equatorial vertices there is a 2–2 move on the boundary, and we can represent
ϖ by a collection of oriented normal arcs in a quadrilateral of the six types shown in the
right hand side of Figure 25. (Note that either ¯s = 0 or ¯t = 0 for an embedded normal curve
ϖ.)
1
2
4
3
1
2
4
3
1
2
4
3
¯y
¯y′
¯y
¯y′
¯b
¯b′
¯b
¯b′
¯z
¯x′
¯x
¯z′
¯a
¯c′
¯c
¯a′
¯s
¯t
Figure 25. Change in turning numbers under a 2–2 move
Then the corresponding turning numbers at the corners of the triangles in the left and
centre of the ﬁgure are given by:
¯a = ¯y + ¯t, ¯c = ¯y′ −¯s, ¯a′ = ¯y′ −¯t, ¯c′ = ¯y + ¯s
and
¯x = ¯b′ −¯s, ¯z = ¯b −¯t, ¯x′ = ¯b + ¯s, ¯z′ = ¯b′ + ¯t.
54 STAVROS GAROUFALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
For example, a is the signed number of (anticlockwise) normal arcs going from edge 1 to the
vertical edge in the centre of the ﬁgure. But each such arc is a normal arc in the quadrilateral
going from edge 1 to 3 or from edge 1 to edge 4, hence ¯a = ¯y + ¯t.
In particular, we have the following relations that will be used below:
(37)
¯a + ¯a′ = ¯c + ¯c′ = ¯y + ¯y′ and ¯x + ¯x′ = ¯z + ¯z′ = ¯b + ¯b′
(38)
2¯b + ¯c′ −¯a = 2¯b + ¯a′ −¯c = ¯x′ + ¯z and 2¯b′ + ¯c −¯a′ = 2¯b′ + ¯a −¯c′ = ¯x + ¯z′.
Now ϖek is obtained from ϖ by adding small vertex linking circles around the vertices of
eT∂, and similarly ϖk is obtained from ϖ by adding small vertex linking circles around the
vertices of T∂. Note that we have a map from the turning numbers of ϖ relative to T to the
turning numbers of ϖ relative to eT. If we apply the same map to the turning numbers of
ϖk relative to T, we obtain the turning numbers of ϖ(0,k) relative to eT.
In the following, we will abbreviate our notation as follows. Let
¯aj = ¯aj(k, ϖ), ¯bj = ¯bj(k, ϖ), ¯cj = ¯cj(k, ϖ) for j = 0, 4
¯aj = ¯aj((0, k), ϖ), ¯bj = ¯bj((0, k), ϖ), ¯cj = ¯cj((0, k), ϖ) for j = 1, 2, 3.
Recall that ¯aj(k, ϖ) is the sum of ¯aϖ,j and the weights given by k on the two edges of tetra-
hedron j labelled ¯aj, and similarly for ¯bj(k, ϖ), ¯cj(k, ϖ). Thus, replacing k by ek = (k0, k)
does not change ¯aj(k, ϖ) or ¯cj(k, ϖ) but we have ¯bj(ek, ϖ) = ¯bj + k0 for j = 1, 2, 3, since the
new edge 04 is incident to angles labelled ¯bj in Figure 23.
We also let ¯Aj = ¯bj −¯cj, ¯Bj = ¯cj −¯aj, ¯Cj = ¯aj −¯bj, and note that each of these is a sum
of contributions from the 4 triangular corners of the (truncated) tetrahedron Tj. On each
of these triangles, ¯Aj, ¯Bj, ¯Cj represent inward intersection numbers of oriented normal arcs
with the sides of the triangles as shown in Figure 26.
¯a
¯A
¯b
¯C
¯c
¯B
Figure 26. Intersection numbers and turning numbers in a triangle.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD
55
Then we have
(39)
¯Aj + ¯Bj + ¯Cj = 0 for each j,
and
(40)
¯B1 + ¯B2 + ¯B3 = 0.
To prove the last equation, we look at the contribution from each of the 5 corners of the
bipyramid as shown in Figure 27. At the polar vertices 0, 4 the contribution to P
i ¯Bi =
P3
i=1 ¯ai −P3
i=1 ¯ci is zero from Figure 24, while at the equatorial vertices 1, 2, 3 this follows
from (37). Alternatively, one can look at the vertices 1, 2, 3 as shown in Figure 27, and see
that, for example, at vertex 1 the contribution to B2 is cancelled by the contribution to B3.
Similar cancellations happen at vertices 2 and 3.
Now consider the left hand side of (36). We have
J(T1; (k0, k), ϖ) = (−q
1
2)−¯c1I∆(¯c1 −¯a1,¯b1 + k0 −¯c1) = (−q
1
2)−¯c1I∆( ¯B1, ¯A1 + k0),
J(T2; (k0, k), ϖ) = (−q
1
2)−¯c2I∆(¯c2 −¯a2,¯b2 + k0 −¯c2) = (−q
1
2)−¯c2I∆( ¯B2, ¯A2 + k0),
and
J(T3; (k0, k), ϖ) = (−q
1
2)−¯a3I∆(¯a3 −¯b3 −k0, ¯c3 −¯a3) = (−q
1
2)−¯a3I∆( ¯C3 −k0, ¯B3)
= (−q
1
2)−¯a3I∆(−¯B3, −¯C3 + k0) = (−q
1
2)−¯a3I∆( ¯B1 + ¯B2, −¯C3 + k0)
using the duality identity (8) and (40).
The pentagon identity (10) can be rewritten (by replacing e3 by x3 + e0) in the form
X
e0∈Z
qe0I∆(m1, x1 + e0)I∆(m2, x2 + e0)I∆(m1 + m2, x3 + e0)
(41)
= q−x3I∆(m1 −x2 + x3, x1 −x3)I∆(m2 −x1 + x3, x2 −x3).
We apply this with e0 = k0, m1 = ¯B1, m2 = ¯B2, x1 = ¯A1, x2 = ¯A2 and x3 = −¯C3. Then
direct calculations, using the observations above, show that
(i) m1 −x2 + x3 = ¯B1 −¯A2 −¯C3 = ¯A0,
(ii) x1 −x3 = ¯A1 + ¯C3 = ¯C0,
(iii) m2 −x1 + x3 = ¯B2 −¯A1 −¯C3 = ¯B4,
(iv) x2 −x3 = ¯A2 + ¯C3 = ¯A4, and
(v) ¯c1 + ¯c2 + ¯a3 + 2x3 = ¯b0 + ¯c4 hence (−q
1
2)−¯c1−¯c2−¯a3q−x3 = (−q
1
2)−¯b0−¯c4.
Thus, multiplying (41) by (−q
1
2)−¯c1−¯c2−¯a3 gives
X
k0∈Z
qk0J(T1; (k0, k), ϖ)J(T2; (k0, k), ϖ)J(T3; (k0, k), ϖ) = (−q
1
2)−¯b0I∆( ¯A0, ¯C0)(−q
1
2)−¯c4I∆( ¯B4, ¯A4)
= J(T0; k, ϖ)J(T4; k, ϖ),
as desired.
56 STAVROS GAROUFALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
Vertex 1
Vertex 2
Vertex 3
Vertex 0
Vertex 4
¯C4
¯B4
¯B0
¯C0
¯C2
¯A3
¯A2
¯C3
¯A4
¯C4
¯A0
¯B0
¯C3
¯A1
¯A3
¯C1
¯B4
¯A4
¯C0
¯A0
¯C1
¯A2
¯A1
¯C2
¯A0
¯A4
¯C0
¯B4
¯B0
¯C4
¯B3
¯B2
¯B1
¯B3
¯B2
¯B1
¯b2
¯b3
¯b3
¯b1
¯b1
¯b2
¯b4
¯c0
¯c4
¯b0
¯c4
¯b0
¯a4
¯a0
¯a4
¯a0
¯b4
¯c0
¯a2 ¯c3
¯c2 ¯a3
¯a3 ¯c1
¯c3 ¯a1
¯a1 ¯c2
¯c1 ¯a2
¯a4
¯a0
¯b4
¯c0
¯c4
¯b0
¯A4
¯B1
¯A0
¯B1
¯B4
¯C4
¯C0
¯B0
¯B2
¯B3
¯B2
¯B3
¯A2
¯C3
¯C2
¯A3
¯C1
¯A1
¯A1
¯C1
¯A3
¯C2
¯C3
¯A2
¯b1
¯b2
¯b3
¯b1
¯b2
¯b3
¯a1
¯c1
¯c1
¯a1
¯c2
¯a3
¯a2
¯c3
¯a2 ¯c3
¯c2 ¯a3
¯a4
¯a0
¯c4
¯b4
¯b0
¯c0
Figure 27. Turning numbers and intersection numbers at all corners of the
bipyramid.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD
57
The identities (i)-(v) are proved by looking separately at the contributions from the 5
corners of the bipyramid, and carefully studying Figure 27.
For example, to prove (i), we note that
at vertex 1: ¯B1 −¯A2 −¯C3 = 0 −¯A2 −¯C3 = −¯B0 −¯C0 = ¯A0
at vertex 2: ¯B1 −¯A2 −¯C3 = −¯B3 −0 −¯C3 = ¯A3 = ¯A0
at vertex 3: ¯B1 −¯A2 −¯C3 = ¯B1 −¯A2 −0 = −¯B2 −¯A2 = ¯C2 = ¯A0
at vertex 0: ¯B1 −¯A2 −¯C3 = ¯B1 + ¯C1 + ¯A1 = 0 = ¯A0
at vertex 4: ¯B1 −¯A2 −¯C3 = ¯B1 + 0 = ¯A0
For (ii), we note that
at vertex 1: ¯A1 + ¯C3 = 0 + ¯C3 = ¯C0
at vertex 2: ¯A1 + ¯C3 = ¯C4 + ¯A4 = −¯B4 = ¯C0
at vertex 3: ¯A1 + ¯C3 = ¯A1 = ¯C0
at vertex 0: ¯A1 + ¯C3 = 0 = ¯C0
at vertex 4: ¯A1 + ¯C3 = −¯C2 −¯A2 = ¯B2 = ¯C0
The equalities (iii), (iv) are veriﬁed similarly.
Finally, to prove (v), ﬁrst note that since x3 = −¯C3 = ¯b3 −¯a3, we need to show that
¯c1 + ¯c2 −¯a3 + 2¯b3 = ¯b0 + ¯c4.
Now at vertices 0 and 4, ¯b3 = ¯b3(0, k), ϖ) = 0, since we can choose ϖ as in Figure 24.
Further, ¯aj,¯bj, ¯cj = 0 at vertex j. Thus, from Figure 27,
at vertex 0: LHS = ¯c1 + ¯c2 −¯a3 = ¯b4 + ¯c4 −¯b4 = ¯c4 = RHS from Figure 24
at vertex 4: LHS = ¯c1 + ¯c2 −¯a3 = ¯b0 + ¯a0 −¯a0 = ¯b0 = RHS from Figure 24
at vertex 1: LHS = ¯c2 −¯a3 + 2¯b3 = ¯b0 + ¯c4 by (38)
at vertex 2: LHS = ¯c1 −¯a3 + 2¯b3 = ¯b0 + ¯c4 by (38)
at vertex 3: LHS = ¯c1 + ¯c2 = ¯b0 + ¯c4 by (37).
This completes the proof of Lemma A.3.
□
