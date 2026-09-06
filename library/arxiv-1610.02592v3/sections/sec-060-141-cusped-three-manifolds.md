---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-060-141-cusped-three-manifolds
section_title: "Cusped three-manifolds"
section_number: 14.1
pages: 429-441
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
We know that every cusped ﬁnite-volume complete hyperbolic surface is
constructed by gluing isometrically ﬁnitely many ideal triangles along their
edges (see Proposition 7.4.6). Likewise, we now construct plenty of cusped
hyperbolicthree-manifoldsbygluingisometricallyﬁnitelymanyidealtetrahedra
along their faces.
14.1.1. Ideal tetrahedra.Ideal triangles are all isometric, but ideal tetra-
hedra are not! We now show that they can be described up to isometry by a
single complex parameterz withℑz >0.
An ideal tetrahedron is determined by its four ideal verticesv1,v 2,v 3,v 4∈
∂H3. We use the half-space model H3 and recall that ∂H 3 = C∪{∞}
and Isom+(H3) = PSL2(C), hence there is a unique orientation-preserving
isometry ofH3 that sends the verticesv1,v 2,v 3,v 4 respectively to 0, 1,∞,z
for somez. Up to mirroring with the orientation-reversing reﬂectionz↦→ ¯z
we can suppose thatℑz >0.
421
422 14. HYPERBOLIC THREE-MANIFOLDS
Figure 14.1. An ideal tetrahedron with three vertices in0, 1,∞ in the
half-space mode is determined by the positionz∈ C∪{∞} of the fourth
vertex. A small horosphere centred at the ideal vertex intersects the tetra-
hedron in a Euclidean triangle uniquely determined up to similarities.
z z
z
0 1
z
z-1
z
1
1- z
z-1
z
z-1
z
1
1- z 1
1- z
Figure 14.2. At each ideal vertex we have a Euclidean triangle deﬁned
up to similarities: each vertex of the triangle has a well-deﬁned complex
angle (left). We can assign the complex angles directly to the edges of
the tetrahedron. The argument is the dihedral angle of the edge (right).
Remark 14.1.1. By deﬁnition the numberz is thecross-ratio of the four
complex numbersv1,v 2,v 3,v 4.
A horosphere centred at the vertexv3 =∞ is a horizontal Euclidean plane
that intersects the ideal tetrahedron in a Euclidean triangle as in Figure 14.1.
The oriented similarity class of the triangle depends only on the vertexv3,
because a horosphere change results in a dilation: we can represent it as a
triangle in C = R2 with vertices at0, 1, andz as in Figure 14.2-(left). The
complex angleof a vertex of the triangle is the ratio of the two adjacent sides,
taken with clockwise order and seen as complex numbers. The three complex
14.1. CUSPED THREE-MANIFOLDS 423
Figure 14.3. A truncated tetrahedron.
angles are shown in Figure 14.2-(left) and are:
z, 1
1−z, z− 1
z .
The argument is the usual angle, and the modulus is the ratio of the two
lengths of the adjacent sides.
Proposition13.1.2showsthatsomesymmetriesofanidealtetrahedronact
on its vertices like the alternating groupA4 and hence transitively. Therefore
every vertex has the same triangular section as in Figure 14.2-(left), and all
the sections can be encoded by assigning the complex numbers directly to the
edges of ∆ as shown in Figure 14.2-(right). These labels on the edges are
called moduli and determine the ideal tetrahedron up to orientation-preserving
isometries of H3. The argument of a modulus is the dihedral angle of the
edge.
On a regular ideal tetrahedron the triangular sections are equilateral and
hence all edges have the same modulusz =e
πi
3 .
14.1.2. Ideal triangulations. Let ∆1,..., ∆n be identical copies of the
standard oriented 3-simplex. As in the two-dimensional case, atriangulation
T isapartitionofthe 4n facesofthetetrahedrainto 2n pairs, andforeachpair
asimplicialisometrybetweenthetwofaces. Thetriangulationis oriented ifthe
simplicial isometries are orientation-reversing. If we glue the tetrahedra along
the simplicial isometries we get a topological spaceX, which is not necessarily
a topological manifold. LetM be X minus the vertices of the triangulation:
we say thatT is anideal triangulationforM.
Proposition 14.1.2. IfT is oriented thenM is a topological 3-manifold,
homeomorphic to the interior of a compact oriented manifold with boundary.
Proof. To prove thatM is a manifold we only need to check that a point
x∈ e in an edgee has a neighbourhood homeomorphic to an open ball. A
cycle of tetrahedra is attached toe, and sinceT is oriented we are certain
that a neighbourhood ofx is a cone over a 2-sphere and not over a projective
plane.
424 14. HYPERBOLIC THREE-MANIFOLDS
Figure 14.4. If we manage to glue all the tetrahedra incident to an
edge e inside H3 as shown, the hyperbolic structure is deﬁned also ine
(left). Let z1,...,z h be the complex moduli assigned to the sides of the
h incident tetrahedra (hereh = 5). We can glue everything inH3 if and
only ifz1··· zh = 1 and the arguments sum to2π (right).
If we truncate the tetrahedra as in Figure 14.3 before gluing them, we get
a compact manifoldN⊂ M with boundary such thatM\N∼= ∂N× [0, 1).
ThereforeM is homeomorphic toint(N). □
We will always suppose thatT is oriented andM is connected, soM =
int(N) for some compactN with boundary. Every ideal vertexv inT is locally
a cone over a small triangulated closed surfaceΣ⊂M obtained by truncating
the tetrahedra incident tov. We call such aΣ the link ofv.
14.1.3. Hyperbolic ideal triangulations.LetT be an oriented ideal tri-
angulation with tetrahedra ∆1,..., ∆n of a 3-manifoldM. We now substi-
tute every ∆i with an ideal hyperbolic tetrahedron and pair their faces with
orientation-reversing isometries. As opposite to the two-dimensional case, the
ideal hyperbolic tetrahedra are not unique (they depend on a complex modulus
zi) but the isometric pairing of their faces is uniquely determined in virtue of
the following.
Proposition 14.1.3. Given two ideal triangles ∆ and ∆′, every bijection
between the ideal vertices of∆ and of ∆′ is realised by a unique isometry.
Proof. We see the ideal triangles inH2 and recall that for any two triples
of points in∂H2 there is a unique isometry sending pointwise the ﬁrst triple to
the second. Alternatively, we may use the barycentric decomposition shown in
Figure 7.15-(left). □
14.1. CUSPED THREE-MANIFOLDS 425
If we substitute each∆i with an ideal hyperbolic tetrahedron, we immedi-
ately get a well-deﬁned hyperbolic structure onM minus the edges ofT. We
now try to extend this hyperbolic structure to the edges: we can do this if
we are able to glue all theh tetrahedra around each edgee inside H3 as in
Figure 14.4. Letz1,...,z h be the complex moduli associated to the edges of
the h tetrahedra incident toe. As shown in the ﬁgure, ifz1··· zh = 1 and
the sum of their argument is2π (and not some higher multiple of2π) then all
tetrahedra can be glued simultaneously insideH3 and the hyperbolic structure
extends naturally toe. If this holds at every edgee ofT then M inherits
a hyperbolic structure andT is said to be ahyperbolic (or geometric) ideal
triangulation forM.
14.1.4. Consistency equations. We want to parametrize the hyperbolic
structures onM that may be constructed in this way from a ﬁxed ideal triangu-
lationT. We pick an arbitrary edge for every tetrahedron∆i and assign to it a
complex variablezi withℑzi > 0, and the other edges of∆i are automatically
labeled by one of the variableszi, zi−1
zi
, or 1
1−zi
as indicated in Figure 14.2
(recall that the tetrahedra are oriented). As we have seen, for every edgee in
T we obtain an equation of type
w1··· wh = 1
(to which we must add the condition that the sum of the arguments is2π),
where eachwj equalszi, zi−1
zi
, or 1
1−zi
for somei.
Wehavethusobtainedasystemof consistencyequations, withavariable zi
for each tetrahedron and an equationw1··· wh = 1 for each edge. A solution
z = (z1,...,z n) to these equations produces a hyperbolic ideal triangulation
and hence a hyperbolic structure onM. Recall that we assumeℑzi > 0 ∀i.
As in the two-dimensional case, the resulting hyperbolic structure is not
necessarily complete, and to get a complete hyperbolic manifold we must add
more equations.
14.1.5. Completeness equations. Our aim is to construct a complete
ﬁnite-volume hyperbolic metric onM. By Corollary 4.2.18 ifM has such a
metric the link of every ideal vertex ofT is a triangulated torus and identiﬁes
a cusp ofM, so we will henceforth suppose that the links of all vertices are
tori. In other wordsM is the interior of a compact 3-manifoldN bounded by
somec >0 tori.
Letz = (z1,...,z n) be a solution to the consistency equations, providing
a hyperbolic structure toM. Every boundary torusT⊂∂N is triangulated by
T: every triangle inT is the truncation triangle of some∆i and hence inherits
the complex moduli of the three adjacent edges of∆i as in Figure 14.5-(left),
thus it has a Euclidean structure well-deﬁned up to similarities. We want to
study the following problem: do these Euclidean structures on the triangles
426 14. HYPERBOLIC THREE-MANIFOLDS
w2
w1
w3
w4
w6
w5
w7 w9
w8 w10
w11
w12
w13 w14
w15
w17
w16
w18w19
w20w21
w23w24
w22
w25
w27
w26
w29
w30
w28
w2
w1
w3
Figure 14.5. Every boundary torusT ⊂ ∂N is triangulated, and each
trianglehasaEuclideanstructurewell-deﬁneduptosimilaritiesandinherits
three complex moduliw1,w 2,w 3 at its vertices (left). At every vertex of
the triangulation, the product of the adjacent moduli is1, for instance
here w12w15w16w19w23 = 1. The red path contributes toµ(γ) with the
factor−w30w29w25w24w23w19w20 (right).
w1
w2
w3 w1
w2
w3
Figure 14.6. This move forγ does not aﬀectµ(γ).
glue to form a Euclidean structure onT? We will see thatM is complete if
and only if the answer is “yes” at each boundary torusT.
Pick γ∈ π1(T ) = H1(T, Z)∼= Z2. We representγ as a simplicial path
in the triangulation ofT and then deﬁneµ(γ)∈ C∗ to be (−1)|γ| times the
product of all the complex moduli thatγ encounters at its right side, with|γ|
being the number of edges ofγ, see Figure 14.5-(right).
Proposition 14.1.4.The elementµ(γ) is well-deﬁned andµ:π1(T )→ C∗
is a homomorphism.
Proof. Two diﬀerent paths forγ are related by moves as in Figure 14.6.
This move does not aﬀectµ(γ) since w1w2w3 =−1 and the product of the
moduli around a vertex is+1. The mapµ is clearly a homomorphism. □
LetC(T )⊂M be a closed collar of the torusT inN, intersected withM.
It is diﬀeomorphic toT× [0, +∞).
Proposition 14.1.5. The following facts are equivalent:
(1) the homomorphismµ is trivial,
14.1. CUSPED THREE-MANIFOLDS 427
(2) there is a Euclidean structure onT that induces all the moduli,
(3) the manifoldC(T ) is complete and contains a truncated cusp.
Proof. The equivalence (1)⇔(2) is a simple exercise. If (2) holds we may
choose small horosections of all the hyperbolic tetrahedra incident tov that
match to give a Euclidean torusT∗⊂C(T ). The non-compact part ofC(T )
bounded byT∗ is a truncated cusp with baseT∗ and is thus complete. On
the other hand, if (1) does not hold, there is a path of horosections from a
tetrahedron to itself which ends at a bigger height and we conclude thatC(T )
is not complete as in the two-dimensional case, see the proof of Proposition
7.4.8. □
Corollary 14.1.6.The hyperbolic manifoldM is complete⇐⇒µ is trivial
for every torusT⊂∂N.
Fix for every boundary torusT two generatorsm,l for H1(T, Z). The
homomorphismµ is trivial⇐⇒the following two equations are satisﬁed:
µ(m) = 1, µ (l) = 1.
Each equation is of some typew1··· wk = 1. We get two equations for each
of thec boundary tori and hence2c equations in total, called thecompleteness
equations for the triangulationT. We summarise our discussion:
Proposition 14.1.7.LetT be an ideal triangulation ofM = int(N) withn
tetrahedraand ∂N consistingof c tori. Ifapoint z = (z1,...,z n)withℑzi > 0
satisﬁes then consistency equations and the2c completeness equations, then
M admits a ﬁnite-volume complete hyperbolic metric.
14.1.6. Examples. On a triangulationT, thevalence of an edgee is the
number of tetrahedra incident to it, counted with multiplicity. The simplest
kinds of solutions arise in the following construction.
Proposition 14.1.8. LetT be a triangulation where all edges have va-
lence six. The point (e
πi
3,...,e
πi
3 ) is a solution of both the consistency and
completeness equations and deﬁnes a hyperbolic structure where all the ideal
tetrahedra are regular.
Proof. Note that whenz =e
πi
3 the tetrahedron is regular and we get
z = z− 1
z = 1
1−z =e
πi
3.
Therefore the moduli aree
πi
3 everywhere. The consistency equations are sat-
isﬁed since(e
πi
3 )6 = 1 and also the completeness equations are, because by
assigninglength1toeachedgeofthetriangulationofatorus T wegetaglobal
Euclidean structure onT tessellated into isometric equilateral triangles. □
428 14. HYPERBOLIC THREE-MANIFOLDS
F
J
J
RP
F
P R
Figure 14.7. An oriented triangulation with2tetrahedra: faces with the
same letterF,J,P,R are paired with a simplicial map that matches the
letters. We get two edges with valence six (the red and white dots).
P P
FF
J
L
RY G G
QQ
J
L
RY
Figure 14.8. By pairing the faces of two ideal regular octahedra as
shown we get a cusped complete hyperbolic three-manifold. Faces with
the same letter are paired with the unique isometry that matches the
letters. We get six edges with valence four (marked with coloured dots).
Figure 14.7 shows an ideal triangulation with two tetrahedra and two
edges, each with valence six: this deﬁnes a cusped ﬁnite-volume complete
hyperbolic three-manifoldM that decomposes into two regular ideal tetrahe-
dra.
Every ﬁnite covering˜M of M is another example: the ideal triangulation
T lifts to an ideal triangulation˜T where all the edges have valence six. Since
the fundamental groupπ1(M) is residually ﬁnite (see Proposition 4.3.9) there
are plenty of such coverings.
Exercise 14.1.9. Construct a triangulationT with one tetrahedron and
one edge. The edge has valence six and hence the construction of Proposition
14.1.8 produces a cusped hyperbolic manifold. Note however that the triangu-
lation is not orientable and a cusp section is a Klein bottle! This non-orientable
hyperbolic manifold is called theGieseking manifold.
14.1. CUSPED THREE-MANIFOLDS 429
Similar kinds of “regular” examples may be constructed using some other
platonic solids. The ideal regular octahedron is particularly interesting and
useful because it is right-angled, see Section 3.2.4. If we pick ﬁnitely many
oriented regular ideal octahedraO1,...,O h and pair orientation-reversingly
their triangular faces in a way that every resulting edge has valence four, we
construct a ﬁnite-volume cusped hyperbolic manifoldM because 4× π
2 = 2π.
An example with two octahedra is shown in Figure 14.8.
We can further decompose each regular ideal octahedron into four non-
regular ideal tetrahedra (there are three ways to do this: you must choose a
diagonal connecting two opposite vertices) to get an ideal triangulationT for
M. The moduli of each such tetrahedron are
i, 1
1−i = 1 +i
2 , i− 1
i = 1 +i
and they satisfy the consistency and completeness equations in a less trivial
waythanbefore. Theedgesoftheresultingtriangulationhavevaryingvalences
4, 6, and 8.
14.1.7. SnapPea. It is of course hard to construct ideal triangulations by
hand, except in some very symmetric and simple cases like the one just de-
scribed. And it is even more diﬃcult to solve the consistency and completeness
equations.
There is a beautiful computer program that does all this for you! This is
SnapPea, writtenbyJeﬀWeeksinthe1980s. UsingSnapPeayoucandrawany
link diagramL and the program immediately constructs an ideal triangulation
for the complement ofL in S3. Then it uses the Newton method to ﬁnd a
numericalsolutiontotheconsistencyandcompletenessequations: thesolution
is only numerical, but then one can use somea posterioriargument to conﬁrm
it rigorously.
For instance, if we draw the trefoil knot, SnapPea triangulates its com-
plement and ﬁnds no solution to the equations: this is not surprising since its
complement is Seifert and hence not hyperbolic, see Proposition 11.2.5.
If we draw the ﬁgure-eight knot in Figure 14.9-(left), SnapPea constructs
precisely the ideal triangulation of Figure 14.7, and we have hence discovered
that the complement of the ﬁgure-eight knot is hyperbolic and decomposes
into two ideal regular tetrahedra.
We may draw links with many components, and discover for instance that
the complement of the Borromean rings from Figure 14.9-(right) is hyperbolic
and decomposes into two right-angled ideal regular octahedra. We can also
Dehn-ﬁll some boundary components to obtain more cusped manifolds that
are not link complements inS3.
SnapPea can calculate numerically a wealth of geometrical invariants with
some precision, including the volume and the ﬁrst segment of the geodesic
spectrum. It can manipulate manifolds (Dehn-ﬁlling, drilling along short simple
430 14. HYPERBOLIC THREE-MANIFOLDS
Figure 14.9. The ﬁgure-eight knot and the Borromean rings arehyper-
bolic, that is their complements admit complete hyperbolic metrics.
tetrahedra 1 2 3 4 5 6 7
1 cusp 2 9 52 223 913 3388
2 cusps 4 11 48 162
3 cusps 1 2
Table14.1. Thenumberofcuspedorientablehyperbolicthree-manifolds
that can be triangulated with at most 7 ideal tetrahedra.
closed geodesics, ﬁnite covers) and change triangulations. It provides beautiful
pictures of the Dirichlet domain and of the cusp shapes.
Is SnapPea guaranteed to ﬁnd a hyperbolic structure onM if there is one?
No, it is not, although in practice it succeeds most of the time. The fact
thatM is hyperbolic does not guarantee that there is a solution to Thurston’s
equations on a given triangulationT, and the existence of a solution does not
guarantee that SnapPea will be able to ﬁnd it.
We note that for most ideal triangulationsT of a hyperbolicM there is
no solution to Thurston’s equations, and SnapPea is clever enough to modify
T to increase the probability to ﬁnd one. In all known examples, a cusped
hyperbolic M admits at leastone geometric ideal triangulation, but whether
this holds true for all cusped hyperbolic 3-manifoldsM is still an open question.
14.1.8. Cusped census. As with knots tabulations, topologists have used
computerstolistthecuspedhyperbolicmanifoldsthatcanbetriangulatedwith
few ideal tetrahedra.
The number of cusped hyperbolic orientable manifolds that can be ideally
triangulated withn tetrahedra (and not less thann) is written in Table 14.1
for alln⩽ 7. The 1-cusped manifolds withn = 2, 3 are listed with more detail
in Table 14.2 and the 2-cusped ones withn = 4 are in Table 14.3. These
14.1. CUSPED THREE-MANIFOLDS 431
Name Volume Homology Symmetry SG C
M21 2.0298832128 Z D4 1.09 a
M22 2.0298832128 Z + Z5 Z2 + Z4 0.86 a
M31 2.5689706009 Z + Z5 D4 0.65 c
M32 2.5689706009 Z + Z3 D4 0.65 c
M33 2.6667447834 Z + Z2 D4 0.63 c
M34 2.6667447834 Z + Z6 D4 0.63 c
M35 2.7818339124 Z Z 2 0.51 c
M36 2.8281220883 Z D4 0.56 c
M37 2.8281220883 Z Z 2 0.58 c
M38 2.8281220883 Z + Z7 D4 0.56 c
M39 2.9441064867 Z Z 2 0.43 c
Table 14.2. The 1-cusped orientable hyperbolic manifolds that can be
triangulated with at most 3 ideal tetrahedra. The nameMij indicates that
the manifold is the one withj-th smallest volume among those that can
be triangulated withi tetrahedra. The column SG shows the length of
the shortest closed geodesic (volume and SG values are truncated after
few digits). The column C indicates whether the manifold is achiral (a) or
chiral (c), that is if it admits an orientation-reversing isometry or not.
Name Volume Homology Symmetry SG C
M42
1 3.6638623767 Z + Z D8 1.06 c
M42
2 3.6638623767 Z + Z D8 0.96 c
M42
3 4.0597664256 Z + Z D12 0.86 c
M42
4 4.0597664256 Z + Z D8 0.86 a
Table 14.3. The 2-cusped orientable hyperbolic manifolds that can be
triangulated with 4 ideal tetrahedra. The nameMik
j indicates that the
manifold is thek-cusped one withj-th smallest volume among those that
triangulate withi tetrahedra.
tables were produced by Callahan – Hildebrand – Weeks [10] in 1999 via a
computer enumeration.
The ﬁgure-eight knot complement isM21, whileM22 is another hyperbolic
manifold that decomposes into two regular ideal tetrahedra: it is not a knot
complement in S3 since its homology is not Z, but it is the complement
of a knotK in the lens spaceL(5, 1), called the ﬁgure-eight knot sibling.
This knot is obtained by performing a(−5)-surgery on one component of the
Whitehead link shown in Figure 14.10: since this component is trivial, the
surgered manifold isL(5, 1) and the other unsurgered component is our knot
K. Both manifolds M21 and M22 have volume 2.0298832128... since the
volume of the ideal regular tetrahedron is3Λ
(π
3
)
= 1.0149416064...
432 14. HYPERBOLIC THREE-MANIFOLDS
Figure 14.10. A remarkable sequence of hyperbolic links. These are the
ﬁgure eight knot, theWhitehead link, and some particularchain linkswith
3,4,5 components.
c 3 4 5 6 7 8 9 10 11 12 13 14
torus 1 0 1 0 1 1 1 1 1 0 1 1
satellite 0 0 0 0 0 0 0 0 0 0 2 2
hyperbolic 0 1 1 3 6 20 48 164 551 2176 9985 46969
Table 14.4. The number of torus, satellite, and hyperbolic prime knots
withc crossings, for allc⩽ 14.
Themanifold M42
1 istheWhiteheadlinkcomplement, thatcanbeobtained
by pairing the faces of a single ideal regular octahedronO. Indeed the volume
ofO is 8Λ
(π
4
)
= 3.6638623767...
After the ﬁgure eight knot and the Whitehead link, a notable sequence
of hyperbolic links inS3 with increasing number of components is shown in
Figure 14.10. Their complements are conjectured to be the smallest hyper-
bolic manifolds withi = 1,..., 5 cusps (see the references at the end of the
chapter).
14.1.9. Hyperbolic knots. How many hyperbolic knots inS3 are there?
There are inﬁnitely many hyperbolic knots, and inﬁnitely many non-hyperbolic
knots. Geometrisation translates hyperbolicity into an appealing topological
condition:
Theorem 14.1.10.A knotK⊂S3 is either a torus knot, a satellite knot,
of a hyperbolic knot.
Proof using geometrisation. Proposition 11.2.11 says thatK is either a
torus knot, a satellite knot, or has simple complementM. In the latter case
M is hyperbolic by Corollary 12.9.6. □
Note that the three cases are mutually exclusive. The number of prime
knots withc⩽ 14crossings in each of the three classes is shown in Table 14.4,
taken from Hoste – Thistlethwaite – Weeks [29]: the table shows a strong
predominance of hyperbolic knots, but it is unknown whether it persists also
whenc tends to inﬁnity.
