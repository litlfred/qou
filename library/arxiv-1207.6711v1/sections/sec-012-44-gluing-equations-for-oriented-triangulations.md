---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-012-44-gluing-equations-for-oriented-triangulations
section_title: "Gluing equations for oriented triangulations"
section_number: 4.4
pages: 10-13
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
T . The gluing equations are indexed by (non-vertex) integral points of T deﬁned below and
come in three ﬂavors: edge equations, face equations, and interior equations. In Section 4.6
we generalize the gluing equations to all concrete triangulations.
GLUING EQUATIONS FOR PGL( n, C)-REPRESENTATIONS OF 3-MANIFOLDS 11
1 3
2
0
3
2
0
0
1
3
2
z1 ''
z0
z2 '
(a) z0z′′
1z′
2 = 1
1 3
2
0
3
2
0
0
1
3
2
z1200,0
1100
z0102,1
0101
z0120,2
0110 (b) z1100
1200,0z0101
0102,1z0110
0120,2 = 1
Figure 5. Edge equations for n = 2 (traditional notation) and n = 5.
Recall that T is an identiﬁcation of ˆM with a quotient of a disjoint union of standard
simplices. Hence,T comes naturally equipped with a map
(4.6) q :
∐
∆3
n→ˆM.
Deﬁnition 4.4. An integral point ofT is a point p in
q
(∐
∆3
n(Z)
)
⊂ˆM.
We view p as an equivalence class of pairs ( t, ∆) with t∈ ∆3
n(Z) and ∆ ∈T and write
(t, ∆)∈p if (t, ∆) is a representative of p. The set of all integral points of T is denoted by
T (Z).
Deﬁnition 4.5. Let p be an integral point of T represented by (t, ∆).
(i) We call p a vertex point if t is a vertex of ∆ 3
n(Z).
(ii) We call p an edge point if t is on an edge of ∆ 3
n(Z).
(iii) We call p a face point if t is on a face ∆ 3
n(Z).
(iv) We call p an interior point if t is in the interior of ∆ 3
n(Z), i.e. if t∈ ∆3
n(Z+).
We denote the set of non-vertex integral points by ˙Tn(Z).
Deﬁnition 4.6. A shape assignment on an ordered triangulation T is a shape assignment
ze
s,∆ for each simplex ∆ ∈T such that for each non-vertex integral point p∈ ˙Tn(Z), the
generalized gluing equation
(4.7)
∏
(t,∆)∈p
∏
t=s+e
ze
s,∆ = 1.
is satisﬁed. The variety of shape assignments on T is denoted by Vn(T ).
Note that the gluing equation for an integral point p sets equal to 1 the product of the
shape parameters of all edges of subsimplices such that the edge midpoint intersects p. The
generalized gluing equations come in three diﬀerent ﬂavors depending on the type of the
integral point p.
12 STA VROS GAROUF ALIDIS, MATTHIAS GOERNER, AND CHRISTIAN K. ZICKERT
0
21
3
0
21
3
∆0 ∆1
z0011
2011,0z1001
1021,0z1010
1012,0| {z }
t0=2022
z0011
0211,1z0101
0121,1z0110
0112,1| {z }
t1=0222
= 1
Figure 6. A face equation for n = 6. The indicated face-pairing is encoded by the permu-
tation σ = (0231)∈S4.
3
2
0
1
z1121
1100
z2210
0011
z1211
1010
z2111
0110z2120
0101
z1220
1001
z0011
2210z0101
2120z0110
2111z1001
1220z1010
1211z1100
1121| {z }
t=2221
= 1
Figure 7. An internal equation for n = 7.
• Edge equations: If p is an edge point, the equation is similar to the usual gluing
equation in that the number of terms equals the length of the edge cycle. There are
n− 1 edge gluing equations per edge of T involving shape parameters at diﬀerent
levels. See Figure 5.
• Face equations: If p is a face point, the product consists of six terms with three
terms from each of the two simplices sharing the face. There are
(n−1
2
)
equations per
face. See Figure 6.
• Internal equations: If p is an interior point, the equation consists of six terms
involving subsimplices of the same simplex, i.e. this equation is independent of the
triangulation. There are
(n−1
3
)
equations per simplex. See Figure 7.
Remark 4.7. There are no vertex equations. If p is a vertex point, (4.7) is tautologically
satisﬁed since the product is empty.
GLUING EQUATIONS FOR PGL( n, C)-REPRESENTATIONS OF 3-MANIFOLDS 13
