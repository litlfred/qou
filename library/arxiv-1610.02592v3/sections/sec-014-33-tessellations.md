---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-014-33-tessellations
section_title: "Tessellations"
section_number: 3.3
pages: 90-97
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
A tessellation is a nice paving ofHn made of polyhedra. Not only tessel-
lations are beautiful objects, but they are also tightly connected with discrete
groups of Isom(Hn) and hence with hyperbolic manifolds.
Deﬁnition 3.3.1. Atessellation of Hn (or Rn,Sn) is a locally ﬁnite set of
polyhedra that cover the space and may intersect only in common faces.
Some examples in spherical and Euclidean space are shown in Figure 3.4.
We now construct some families explicitly.
3.3. TESSELLATIONS 83
Figure 3.4. A tessellation ofS2 into squares, hexagons, and decagons,
and a tessellation ofR3 into truncated octahedra.
Figure 3.5. The tessellations (2, 3, 3), (2, 3, 4) and (2, 3, 5) of the sphere.
3.3.1. Triangles. We want to deﬁne some nice tessellations ofH2, R2,
and S2 into triangles. The following exercise says that every triple of acute
angles is realised by some triangle in the appropriate geometry.
Exercise3.3.2. Giventhreerealnumbers 0<α,β,γ ⩽ π
2 thereisatriangle
∆ with inner anglesα,β,γ inside H2, R2, orS2 depending on whether the sum
α +β +γ is smaller, equal, or bigger thanπ.
Let a,b,c > 2 be three natural numbers and∆ be a triangle with inner
angles π
a, π
b, π
c. The triangle ∆ lies in H2, R2, orS2 depending on whether
1
a + 1
b + 1
c is smaller, equal, or bigger than 1. In all cases, by mirroring iteratively
∆ along its edges we construct a tessellation of the space.
The triples realisable inS2 are (2, 2,c ), (2, 3, 3), (2, 3, 4), and (2, 3, 5):
the last three tessellations are shown in Figure 3.5 and are connected to the
platonic solids. They consist of24, 48, and 120 triangles.
The triples realisable inR2 are (2, 3, 6), (2, 4, 4), and(3, 3, 3): the tessel-
lations are shown in Figure 3.6. There are inﬁnitely many triples realisable in
H2, and some are shown in Figure 3.7.
84 3. HYPERBOLIC MANIFOLDS
Figure 3.6. The tessellations(2, 3, 6), (2, 4, 4), and(3, 3, 3) of the Eu-
clidean plane.
Figure 3.7. The tessellations (2, 3, 7), (2, 4, 5), and (3, 3, 4) of the hy-
perbolic plane.
In the hyperbolic plane we can also use triangles with vertices at inﬁnity,
which have inner angle zero by deﬁnition.
Exercise 3.3.3. Given three real numbers0⩽α,β,γ ⩽ π
2 with sum smaller
thanπ there is a triangle∆⊂ H2 with inner anglesα,β,γ .
For any triple(a,b,c ) of numbers inN∪{∞} with 1
a + 1
b + 1
c < 1 we may
take the triangle∆⊂ H2 with inner anglesπ
a, π
b, π
c and reﬂect it iteratively
to get a tessellation ofH2.
The triple (∞,∞,∞) gives a nice tessellation into ideal triangles called
the Farey tessellationand shown in Figure 3.8.
3.3.2. Platonic solids. We now turn to tessellations of 3-dimensional
spaces. Table 3.1 displays a ﬁnite list of platonic solidsP with dihedral an-
gles 2π
k contained in H3, R3, orS3. For each solid in the list, by reﬂecting
iterativelyP along its faces we get a tessellation of the space.
The Figures 3.9, 3.10, and 3.11 show the tessellations ofH3, H3, and
S3 by regular dodecahedra with dihedral anglesπ
2, π
3, and 2π
3 . The ﬁrst two
tessellations contain inﬁnitely many polyhedra and appear in the ﬁgures as
seen by an observer ﬂoating insideH3. The reader is invited to observe the
diﬀerences between the ﬁrst two tessellations of the hyperbolic space. The
3.3. TESSELLATIONS 85
Figure 3.8. The Farey tessellation(∞,∞,∞) of the hyperbolic plane.
Figure 3.9. The tessellation ofH3 into right-angled regular dodecahe-
dra, seen from insideH3.
third tessellation contains ﬁnitely many polyhedra and the ﬁgure shows its
stereographic projection inR3.
3.3.3. Regulartessellations. Platonicsolidsare regular, thatistheyhave
many symmetries. A notion of regularity may be deﬁned in all dimensions for
polyhedra and tessellations as follows.
Every tessellation inHn, Rn, orSn has a symmetry group, consisting of all
the isometries of the ambient space that preserve it. Aﬂagis a sequence of
facesf0⊂... ⊂fn of the tessellation withdimfi =i. A tessellation isregular
if the symmetry group acts transitively on ﬂags.
86 3. HYPERBOLIC MANIFOLDS
Figure 3.10. The tessellation ofH3 into ideal regular dodecahedra with
dihedral angleπ
3, seen from insideH3. Note that all vertices lie at inﬁnity.
Figure 3.11. The tessellation ofS3 into 120 regular dodecahedra with
dihedralangle 2π
3 , transposedinto R3 viathestereographicprojection, that
transforms straight faces into round ones but preserves the angles.
3.3. TESSELLATIONS 87
Figure 3.12. The tessellations of H2 with Schläﬂi symbols{4,∞},
{∞, 4}, and{∞,∞}.
These deﬁnitions apply also to polyhedra. We note that a regular poly-
hedron in Rn, considered up to similarities, may be interpreted as a regular
tessellation inSn−1, and vice versa.
The Schläﬂi notationbeautifully encodes various regular tessellations, in
all dimensions and in all geometries. The symbol{n} with n> 3 denotes
the regularn-gon, that is a regular tessellation ofS1 by n congruent arcs,
and by extension{∞} denotes the regular tessellation ofR by inﬁnitely many
congruent segments.
The symbol{p,q}denotes a regular tessellation inH2, R2,orS2 byp-gons
whereq of them meet at every vertex. The ﬁve platonic solids are
{3, 3},{3, 4},{3, 5},{4, 3},{5, 3},
thesymbols{3, 6},{4, 4},and{6, 3}denotethetworegulartessellationsof R2
into equilateral triangles, squares, and regular hexagons, and every other pair
{p,q} denotes a tessellation of regularp-gons inH2 with angles 2π
q , that meet
atq at every vertex. We can also interpret{p,∞} as a regular tessellation of
H2 into ideal regularp-gons (the Farey tessellation is{3,∞}) and{∞,q} as
a regular tessellation of∞-gons that meet atq at every vertex, whose edges
form aq-regular tree (a tree whereq edges meet at every vertex). Finally
{∞,∞} is a regular tessellation of ideal∞-gons. See Figure 3.12
The symbol{p,q,r } denotes a regular tessellation in H3, R3, or S3 by
polyhedra{p,q} wherer of them meet at every edge. We deduce from Table
3.1 that the regular tessellations ofS3 are
{3, 3, 3},{3, 3, 4},{3, 3, 5},{3, 4, 3},{4, 3, 3},{5, 3, 3}.
These are the six regular polyhedra (usually calledpolytopes) in dimension
four: we will encounter them again in Chapter 12.2.3. The symbol{4, 3, 4}
indicates the tessellation ofR3 into cubes, and
{3, 3, 6},{3, 4, 4},{3, 5, 3},{4, 3, 5},{4, 3, 6},{5, 3, 4},{5, 3, 5},{5, 3, 6}
88 3. HYPERBOLIC MANIFOLDS
Figure 3.13. In the tessellation{6, 3, 3} of H3 every polyhedron has
inﬁnitelymanyhexagonalfaces,whoseverticesalllieinasinglehorosphere.
denotethetessellationsof H3 intoplatonicsolids. Itisalsopossibletointerpret
more triples{p,q,r } in an appropriate way, sometimes by representing the
vertices of the polyhedra as space-like vectors in the hyperboloid model.
Every regular tessellation has adual regular tessellation obtained by tak-
ing the barycenters of all the cells involved. The dual of {a,b,...,z } is
{z,...,b,a }. Duals of ideal tessellations involve inﬁnite polyhedra: for in-
stance{6, 3, 3} is shown in Figure 3.13.
The story continues in four dimensions: we denote by{p,q,r,s } a reg-
ular tessellation made of polytopes of type{p,q,r } that meet ins at every
codimension-two face. With the same techniques of Section 3.2.4 we can
identify the regular polytopes inH4, R4 andS4 with dihedral angles that divide
2π, and the corresponding tessellations of the ambient space – that we are
unfortunately unable to see.
3.3.4. Voronoitessellations. Intheprevioussectionwehaveconstructed
some tessellations by exploiting the symmetries of regular polyhedra: we can
probably extend these methods to less symmetric polyhedra, but how far can
we go? How can we construct highly non-regular tessellations?
There is a strikingly simple procedure that transforms every discrete setS
of points inHn into a tessellation, called theVoronoi tessellationof S. The
construction goes as follows.
For every pointp∈S we deﬁne
D(p) =
{
q∈ Hn ⏐⏐d(q,p )⩽d(q,p′) ∀p′∈S
}
.
