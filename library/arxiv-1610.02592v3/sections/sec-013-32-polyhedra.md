---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-013-32-polyhedra
section_title: "Polyhedra"
section_number: 3.2
pages: 86-90
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
A polyhedron inHn is a natural geometric object, that may be used to vi-
sualise discrete groups inIsom(Hn) and hence hyperbolic manifolds. Polyhedra
may sometimes be combined to form some tessellations of the space.
3.2.1. Polyhedra. A half-space in Hn is the closure of one of the two
portions of space delimited by a hyperplane. We say that a set of half-spaces
is locally ﬁnite if their boundary hyperplanes are.
Deﬁnition 3.2.1. An-dimensional polyhedron P in Hn is the intersection
of a locally ﬁnite set of half-spaces. We also assume thatP has non-empty
interior.
A subsetS⊂ Hn isconvex ifx,y ∈S implies that the segment connecting
x,y is also contained inS (such a segment is a half-line or a line if one or
both points lie in∂Hn). Every polyhedronP is clearly convex because it is the
intersection of convex sets. Its closureP in Hn is also convex.
Let H⊂ Hn be a half-space containing the polyhedronP. If non-empty,
the intersectionF =∂H∩P is called aface of P. The supporting subspace
of F is the smallest subspace ofHn containing F; thedimension of a face is
the dimension of its supporting subspace. A face of dimension0, 1, andn− 1
is called avertex, anedge, and afacet.
Exercise 3.2.2. If non-empty, the intersection of faces ofP is a face.
Exercise 3.2.3. Everyk-dimensional face is a polyhedron in its supporting
k-dimensional space.
The convex hullof a setS⊂ Hn is the intersection of all the convex sets
containingS.
Exercise 3.2.4. The convex hull of ﬁnitely many points inHn that are not
contained in a hyperplane is a compact polyhedron. Conversely, every compact
polyhedron has ﬁnitely many vertices and is the convex hull of them.
Everything we said holds with no modiﬁcations forRn. OnSn some care
should be taken: some deﬁnitions need to be modiﬁed slightly to take into
accounttheannoyingpresenceofantipodalpoints. Weglossoverthistechnical
point.
3.2.2. Finite polyhedra. We now enlarge slightly the class of compact
polyhedra by admitting ﬁnitely many vertices at inﬁnity.
Deﬁnition 3.2.5. Aﬁnite polyhedronis the convex hull of ﬁnitely many
pointsx1,...,x k∈ Hn that are not contained in the closure of a hyperplane.
The xi’s that lie in∂Hn are calledideal vertices, while the usual vertices
ofP are theﬁniteor actual vertices. The ideal vertices form the setP\P.
3.2. POLYHEDRA 79
Figure 3.1. The coneC over a domainD⊂O has volume proportional
to the area ofD (left). If the domain is compact, the cone has ﬁnite
volume: therefore a ﬁnite polyhedron has ﬁnite volume (right).
Exercise 3.2.6. A ﬁnite polyhedronP has ﬁnitely many faces and is the
convex hull of its ideal and ﬁnite vertices.
Wewanttoestimatethevolumeofﬁnitepolyhedra, andtodothisweneed
a lemma. Given a horosphereO centred atp∈ ∂Hn and a domainD⊂ O,
the cone C of D over p is the union of all the half-lines exiting fromD and
pointing towardsp, see Figure 3.1.
Lemma 3.2.7. Let O be a horosphere centred atp∈ ∂Hn, D⊂ O any
domain andC the cone overD. The following equality holds:
Vol(C) = VolO(D)
n− 1
where VolO is the (n− 1)-dimensional volume in the ﬂat(n− 1)-manifoldO.
Proof. LetO have some heightxn =h as in Figure 3.1-(left). We obtain
Vol(C) =
∫
D
dx
∫ ∞
h
1
tndt = 1
n− 1
∫
D
dx
hn−1 = 1
n− 1· VolO(D).
The proof is complete. □
We now turn to ﬁnite polyhedra.
Proposition 3.2.8. Every ﬁnite polyhedron has ﬁnite volume.
Proof. For every ideal vertex ofP, a small horoball centred atp intersects
P into a cone that has ﬁnite volume. The polyhedronP decomposes into
ﬁnitely many cones and a bounded region, see Figure 3.1-(right). □
A ﬁnite polyhedron without ﬁnite vertices is called anideal polyhedron.
80 3. HYPERBOLIC MANIFOLDS
Figure 3.2. A triangle with at least an ideal vertex (left). The area
of a triangle with ﬁnite vertices can be derived as the area diﬀerence of
triangles with one ideal vertex (right).
3.2.3. Polygons. A polygon is just a polyhedron of dimension two. In
contrast with Euclidean geometry, a strikingly simple formula relates the area
of a ﬁnite polygon with its inner angles. We deﬁne the inner angle of an ideal
vertex to be zero.
Proposition 3.2.9. A polygonP with inner anglesα1,...,α n has area
Area(P ) = (n− 2)π−
n∑
i=1
αi.
Proof. Every polygon decomposes into triangles, and it suﬃces to prove
the formula on these. Consider ﬁrst a triangleT with at least one vertex at
inﬁnity. We use the half-plane model and send this vertex to∞ as in Figure
3.2-(left). We suppose that the red dot is the origin ofR2, hence
T =
{
(r cosθ,y )|β⩽θ⩽π−α, y>r sinθ
}
and we get
Area(T ) =
∫
T
1
y 2dxdy =
∫ β
π−α
∫ ∞
r sinθ
−r sinθ
y 2 dydθ
=
∫ β
π−α
−r sinθ
[
− 1
y
]∞
r sinθ
dθ =
∫ π−α
β
r sinθ
r sinθdθ
=
∫ π−α
β
1 =π−α−β.
The area of a triangle with ﬁnite verticesABC is deduced as in Figure 3.2-
(right) using the formula
Area(ABC) = Area(AB∞) + Area(BC∞)− Area(AC∞).
The proof is complete. □
3.2. POLYHEDRA 81
Figure 3.3. The regular icosahedron and dodecahedron.
The sum of the inner angles of a hyperbolic polygon is strictly smaller than
that of a Euclidean polygon with the same number of sides, and the diﬀerence
between these two numbers is precisely its area.
Corollary 3.2.10.Every ideal triangle has areaπ.
3.2.4. Platonic solids. The theory of three-dimensional polyhedra inH3
is very rich: we limit ourselves to the study of the platonic solids.
The ﬁve Euclidean platonic solids are the regular tetrahedron, the cube,
the regular octahedron, icosahedron, and dodecahedron. We now see that
each platonic solidP⊂ R3 generates a nice continuous family of solids in the
three geometries H3, R3, andS3.
To construct this family we ﬁx any pointx in H3 and representP centred
at x with varying size. To do this, we putP inside the Euclidean tangent
space Tx H3 centred at the origin and with some radiust >0. Consider the
image of its vertices by the exponential map and take their convex hull. We
indicate byP (−t) the resulting polyhedron inH3. The polyhedronP (−t) is
combinatorially equivalent toP and has the same symmetries ofP.
We extend this family to the other geometries as follows. The polyhedron
P (0) is the EuclideanP (unique up to dilations), andP (t) with t > 0 is
the sphericalP, constructed as above withS3 instead of H3: we ﬁxx∈S3,
take a copy ofP inside TxS3 with radiust, project its vertices, and take the
convex hull. We deﬁne the sphericalP (t) only fort∈ (0, π
2 ]: whent = π
2 it
degenerates to a hemisphere. We also deﬁneP (−∞) as the ideal hyperbolic
platonic solid obtained by sending all the vertices at inﬁnity.
We have deﬁned a polyhedronP (t) for all t ∈ [−∞, π
2 ], that lies in
H3, R3,S 3 depending on whether t is negative, null, or positive. In some
sense the polyhedronP (t) depends continuously ont also when it crosses
the valuet = 0: when t→ 0 the polyhedron inH3 orS3 shrinks, and every
polyhedron tends to a Euclidean one when shrunk.
In particular the dihedral angleθ(t) of P (t) varies continuously witht∈
[−∞, π
2 ]. The function θ(t) is strictly monotone and we now determine its
image. Thevertexvalence ofP isthenumberofedgesincidenttoeachvertex.
82 3. HYPERBOLIC MANIFOLDS
polyhedron θ = π
3 θ = 2π
5 θ = π
2 θ = 2π
3
tetrahedron ideal H3 S3 S3 S3
cube ideal H3 H3 R3 S3
octahedron ideal H3 S3
icosahedron H3
dodecahedron ideal H3 H3 H3 S3
Table 3.1. The platonic solids with dihedral angleθ that divide 2π.
Proposition 3.2.11. Letn∈{ 3, 4, 5} be the vertex valence ofP. It holds
θ
([
−∞,π
2
])
=
[n− 2
n π,π
]
.
Proof. Sinceθ is continuous and monotone increasing, it suﬃces to show
thatθ(−∞) = n−2
n π andθ(π
2 ) =π.
By intersecting the ideal polyhedronP (−∞) with a small horosphereO
centred at an ideal vertexv we get a regularn-gon in the Euclidean plane
O, with interior anglesn−2
n π. The dihedral angle at an edgee incident tov
is measured by intersectingP (−∞) with any hypersurface orthogonal toe:
sinceO is orthogonal toe we getθ(−∞) = n−2
n π.
The polyhedronP (π
2 ) is a hemisphere and henceθ(π
2 ) =π. □
For some values oft, the platonic solidP (t) may have nice dihedral angles
θ(t), for instance angles that divide 2π. In the Euclidean world, the only
platonic solid with such nice dihedral angles is the cube. In the hyperbolic and
spherical world we ﬁnd more.
The platonic solids with dihedral angles that divide2π are listed in Table
3.1. The table is just a consequence of Proposition 3.2.11: it suﬃces to know
the Euclidean dihedral angles forP, and all the angles bigger (smaller) than
this value are spherical (hyperbolic).
Inparticular, therearefourright-angledplatonicsolids: thesphericaltetra-
hedron, the Euclidean cube, the hyperbolic dodecahedron, and the ideal hy-
perbolic octahedron.
