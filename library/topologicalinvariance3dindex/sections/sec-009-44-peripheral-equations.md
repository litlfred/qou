---
doc_id: topologicalinvariance3dindex
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-009-44-peripheral-equations
section_title: "Peripheral equations"
section_number: 4.4
pages: 18-19
source_pdf: topological.invariance.3Dindex.pdf
source_sha256: 22953b4eee66dca2
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
---
rst, for simplicity, that ∂M consists of a single torus,
and let ϖ be an oriented simple closed curve in ∂M that is in normal position with respect
to the induced triangulation T∂ of ∂M . Let
(13) (aϖ|bϖ|cϖ) = (¯aϖ,1..., ¯aϖ,N| ¯bϖ,1,..., ¯bϖ,N| ¯cϖ,1,..., ¯cϖ,N)
denote the vector in Z3N computed as follows. See Figure 7.
Vertex 0 Vertex 1
Vertex 2 Vertex 3 Z
Z
Z′
Z′
Z′′ Z′′
¯b0
ϖ
¯a0
ϖ
¯c0
ϖ
¯c3
ϖ
¯b3
ϖ
¯a3
ϖ
¯c2
ϖ ¯b2
ϖ
¯a2
ϖ
¯a1
ϖ
¯b1
ϖ
¯c1
ϖ
Figure 7. Each term of the turning number vector (aϖ|bϖ|cϖ) is calculated
as a sum of the signed number of times the curve ϖ turns anticlockwise around
the corners of the triangular ends of the truncated tetrahedra. Edges and arcs
on the back side of the tetrahedron are drawn with dashed lines.
The term ¯al
ϖ counts the signed number of normal arcs of ϖ that turn anticlockwise around
the corner of the truncated tetrahedron associated to the variable Z, at vertex number l of
this tetrahedron. The entry in the vector aϖ for this tetrahedron is ∑3
l=0 ¯al
ϖ, and similarly
for the bϖ and cϖ terms. We suppress the vertex number superscripts from now on, since
this data is implied by the location of the labels in the 
gures.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 19
If we eliminate Z′
j using Zj +Z′
j +Z′′
j =π, then we obtain the vector in Z2N
(14) (aϖ|bϖ) = (aϖ−bϖ|cϖ−bϖ)
as well as the scalar
(15) νϖ =−
N∑
j=1
bϖ,j.
Similarly, we can de
ne turning number vectors (aϖ|bϖ|cϖ)∈ Z3N and (aϖ|bϖ)∈ Z2N for
any oriented multi-curve ϖ on ∂M (i.e. a disjoint union of oriented simple closed normal
curves on ∂M ).
More generally, suppose that M is a 3-manifold whose boundary ∂M consists of r≥ 1
tori T1,...,T r. Let ϖ = (ϖ1,...,ϖ r) where ϖh is an oriented multi-curve on Th for each
h = 1,...,r . Then we will use the notation
(16) (aϖ|bϖ|cϖ) =
r∑
h=1
(aϖh|bϖh|cϖh), (aϖ|bϖ) =
r∑
h=1
(aϖh|bϖh), and νϖ =
r∑
h=1
νϖh.
Remark 4.1 . Suppose that ϖ = Ci is a small linking circle on ∂M around one of the two
vertices at the ends of the ith edge, with Ci oriented anticlockwise as viewed from a cusp of
M . Then
(aϖ|bϖ|cϖ) = (¯ai1..., ¯aiN| ¯bi1,..., ¯biN| ¯ci1,..., ¯ciN)
gives the coe
cients of the ith edge equation as a special case of this construction.
