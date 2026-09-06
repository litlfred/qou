---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-025-62-geometrisation
section_title: "Geometrisation"
section_number: 6.2
pages: 165-176
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
Proof. LetS be a compact orientable surface with someb boundary com-
ponents. If we glueb discs to∂S we get a closed orientable surface, hence
diﬀeomorphic toSg for someg> 0. The originalS is obtained fromSg by
removing the interiors ofb disjoint open discs. □
The compact connected orientable surfaces withχ> 0 areS2 =S0 and
D2 =S0,1, those withχ = 0 are the annulusA =S0,2 and the torusT =S1.
Corollary 6.1.10 (Smooth Jordan curve Theorem).Every smooth simple
closed curveγ⊂ R2 bounds a disc.
Proof. Consider the curveγ insideS2 = R2∪{∞}. By cuttingS2 along
γ we get one or two compact orientable surfaces with non-empty boundary
and withχ = 2 in total. The only possibility is that we get two discs. □
6.1.5. Triangulations. Likeeveryhonestsmoothcompactmanifold,com-
pact surfaces admit smooth triangulations, see Section 1.7.7. Conversely, we
may use simplicial complexes to construct smooth surfaces combinatorially.
Let X be a two-dimensional pure simplicial complex where every edge is
incident to two faces, and the link of every vertex is a circle.
Proposition 6.1.11.The complexX is the smooth triangulation of a closed
surfaceS, unique up to diﬀeomorphism.
Proof. By dualisingX we get a handle decomposition: triangles, edges,
and vertices transform into 0-, 1-, and 2-handles, and we get a smooth surface
S triangulated byX. The way the handles are attached is determined up to
isotopy, thereforeS is determined up to diﬀeomorphism. □
Warning 6.1.12. It is worth noting that this procedure (getting a unique
smooth structure from a simplicial complex) does not work in all dimensions
(here we used implicitly Lemma 6.1.1).
6.2. Geometrisation
We now prove that every surfaceSg,b,p of ﬁnite type can begeometrised,
that is it may be equipped with a hyperbolic, ﬂat, or elliptic metric. The metric
type is prescribed by the sign of the Euler characteristic of the surface.
6.2.1. Hyperbolic pair-of-pants. The sphere has of course an elliptic
structure, and the torus has many ﬂat structures, see Section 3.4.8. We now
construct hyperbolic structures on all the surfacesSg of genusg> 2, and
more generally on all the surfacesSg,b,p of negative Euler characteristic. We
start with a simple block, thepair-of-pants S0,3, with Euler characteristic−1.
Proposition 6.2.1. Given three real numbersa,b,c > 0 there is (up to
isometries) a unique complete ﬁnite-volume hyperbolic pair-of-pants with ge-
odesic boundary, with boundary curves of lengtha,b, andc.
158 6. SURFACES
a b
c
b
c c
Figure 6.5. A pair-of-pants, an annulus with one puncture, a disc with
two punctures, and a thrice-punctured sphere. The last three surfaces
may be considered as some degenerated hyperbolic pairs-of-pants where
one or more boundary lengthsa,b, orc are zero, and we get cusps instead
of geodesic boundary components there.
x
f(x)
a b
c
a b
P Q
A B
A' B'
r s
T U
l
Figure 6.6. A right-angled hexagon with alternate sides of lengtha, b
and c (left) and its construction (right), which goes as follows: take a
line l with two arbitrary pointsA and B in it (bottom black). Draw the
perpendiculars fromA and B (red). At distances a and b we ﬁnd two
points A′ and B′ and we draw again two perpendiculars (black)r and s,
with some points at inﬁnityP and Q. Draw the (unique) perpendiculars
to l pointing toP and Q (blue): they intersectl in two pointsT and U.
Note thatAT and UB have some ﬁxed length depending only ona and
b. We can vary the parameterx = TU: if x > 0 the linesr and s are
ultra-parallel and there is a unique segment orthogonal to both of some
lengthf (x).
When some length ina,b,c is zero, we mean that the geodesic boundary
is actually a cusp (recall Section 4.2.5) and hence the surface is topologically a
punctured annulusS0,2,1, a twice punctured discS0,1,2, or a thrice-punctured
sphereS0,0,3: see Figure 6.5.
To prove this proposition we construct some right-angled hexagons inH2
as in Figure 6.6-(left). Threealternate sideson a hexagon are three pairwise
non-incident sides, like thea,b,c shown in the ﬁgure. Adegenerate hexagon
is one where the length of some alternate sides is zero as in Figure 6.7.
6.2. GEOMETRISATION 159
Figure 6.7. A right-angled hexagon with parametersa,b,c > 0 degen-
erates to a pentagon, quadrilateral, or triangle with ideal vertices if one,
two, or three parameters are zero.
a b
c
a b
c
22 22
22
a b
c
22 22
22
Figure 6.8. By gluing two identical right-angled hexagons along their
black sides we get a hyperbolic pair-of-pants with geodesic boundary.
Lemma 6.2.2. Given three real numbersa,b,c > 0 there exists (up to
isometries) a unique (possibly degenerate) hyperbolic right-angled hexagon
with three alternate sides of lengtha,b, andc.
Proof. We ﬁrst supposea,b > 0. The construction of the hexagon is
depicted in Figure 6.6-(right). Ifx = 0 the blue lines coincide, henceP =Q
and f (0) = 0 . The function f : [0, +∞)→ [0, +∞) is continuous, strictly
monotonic, and with limx→∞f (x) = ∞: therefore there is precisely onex
such thatf (x) =c.
If exactly two parameters are zero, saya = b = 0, a simpler construc-
tion works: take a segment of lengthc as in Figure 6.7-(centre), draw the
perpendiculars at their endpoints, and a line connecting the endpoints of these.
If a = b = c = 0 , pick any ideal triangle. Ideal triangles are indeed
unique up to isometry: use the half-space model and recall thatPSL2(R) acts
transitively on the ordered triples of points in∂H2. □
The most degenerate case is so important that we single it out.
Corollary 6.2.3.All the ideal triangles inH2 are isometric.
160 6. SURFACES
By gluing two identical (possibly degenerate) hexagons along alternate
sides as in Figure 6.8 we construct a (possibly degenerate) hyperbolic pair-of-
pants whose geodesic boundary consists of three simple closed geodesics of
length 2a, 2b, and 2c.
Proof of Proposition 6.2.1. We have proved the existence of a geodesic
pairs-of-pants with any parametersa,b,c > 0, and we now turn to its unique-
ness. Let P be a pair-of-pants with geodesic boundary curvesC1,C 2,C 3 of
lengtha,b,c > 0.
SinceP,C 1, andC2 are compact, there are pointsx1∈C1 andx2∈C2 at
minimumdistance d =d(x1,x 2), connectedbysomecurve γ3 oflength d. The
curve is a simple geodesic orthogonal to bothC1 and C2: if not, some other
curve connectingx1 and x2 would be shorter. We construct analogously two
orthogeodesicsγ1 and γ2 connecting C2 to C3 and C3 to C1 having minimal
length.
The fact thatγ1,γ 2,γ 3 have minimal length easily implies that they are
disjoint (if they intersect, we ﬁnd shorter curves). The three orthogeodesics
subdivide P into two hexagons, with alternate sides of lengthL(γ1), L(γ2),
and L(γ3): by Lemma 6.2.2 the two hexagons are isometric, and hence the
three other alternating sides also have the same lengtha
2, b
2, andc
2. Hexagons
are unique up to isometry and hence the original pair-of-pants also are.
We can extend the argument to the more general case2a, 2b, 2c > 0
as follows. If a = 0 , a neighbourhood of the puncture is a cusp, and we
truncate it at some small horocycleC1 (we do the same ifb = 0 orc = 0).
After these truncations we get a compact pair-of-pants (whose boundary is
not geodesic at the horocycles) and decompose it into two hexagons as above.
The resulting curveγ3 is orthogonal to the horocycleC1, hence it extends to a
half-line pointing towards the puncture. The curvesγ1,γ 2,γ 3 decompose the
surface into degenerate hexagons. □
6.2.2. Hyperbolic surfaces. The pairs-of-pants can be used as building
blocks to construct topologically all ﬁnite type surfaces withχ< 0.
Proposition 6.2.4. If χ(Sg,b,p ) < 0 then Sg,b,p decomposes topologically
into−χ(Sg,b,p ) (possibly degenerate) pairs-of-pants.
Proof. Ifb +p = 0 theng> 2 and the surface decomposes easily in many
ways, see for instance Figure 6.9. Ifb +p> 0 andχ< −1, a decomposition
forSg,b,p may be obtained from one ofSg,b−1,p orSg,b,p−1 by inserting one
more (possibly degenerate) pair-of-pants. Ifχ =−1 the surface is either a
pair-of-pants, or a torus with a puncture or boundary component, which is in
turn obtained by glueing two boundary components of a pair-of-pants.□
We can use this building block to construct hyperbolic structures.
6.2. GEOMETRISATION 161
Figure 6.9. Every surface of ﬁnite type withχ < 0 decomposes into
pair-of-pants. We show here a decomposition ofS3.
Corollary 6.2.5.Ifχ(Sg,b,p )< 0 thenSg,b,p admits a complete hyperbolic
metric withb geodesic boundary components of arbitrary length.
Proof. Decompose Sg,b,p in pair-of-pants, assign an arbitrary length to
all the closed curves of the decomposition (the 6 red curves shown in Figure
6.9) and give each pair-of-pants the hyperbolic metric determined by the three
assigned boundary lengths. Everything glues to a complete hyperbolic metric
forSg,b,p thanks to Proposition 3.5.4. □
Can we geometrise the few orientable surfaces withχ> 0? Yes, but
since there are no cusps in the elliptic and ﬂat geometries we do not consider
surfaces with punctures. The compact orientable surfaces withχ> 0 are the
sphere and the disc, and they all have an elliptic metric with geodesic boundary
(represent the disc as a hemisphere). Those withχ = 0 are the torus and the
annulus, and they admit ﬂat metrics with geodesic boundary.
6.2.3. Non-orientable surfaces. The classiﬁcation of all the ﬁnite-type
non-orientable surfaces is also simple. LetSno
g be the connected sum
Sno
g = RP2#... #RP2
| {z }
g
ofg> 1 copies of the projective planeRP2.
Proposition 6.2.6. We haveχ(Sno
g ) = 2 −g. The surfaceSno
2 is diﬀeo-
morphic to the Klein bottleK shown in Figure 6.10. We have
Sg#RP2∼=Sno
2g+1.
Proof. The formula forχ follows fromχ(RP2) = 1. The Klein bottleK
may be cut along a closed curve into two Möbius strips, andRP2 minus an
open disc is a Möbius strip too, henceRP2#RP2 =K. The latter equality is
a consequence ofT #RP2∼=K#RP2 which is left as an exercise. □
162 6. SURFACES
Figure 6.10. The Klein bottle immersed inR3.
Proposition 6.2.7. Every closed, connected, non-orientable surface is dif-
feomorphic toSno
g for someg> 1.
Proof. Pick a handle decomposition of the surfaceS. Since it is non-
orientable, at least one 1-handle is twisted and forms a M¨bius strip. We have
proved thatS contains a Möbius strip, and we now remove it and substitute it
with a disc to get a new surfaceS′. We haveS =S′#RP2 and we conclude
by induction on−χ(S′). □
We may also denote bySno
g,b,p the surface obtained fromSno
g by removing
the interiors ofb discs andp points.
Exercise6.2.8. If χ(Sno
g,b,p )< 0thenSno
g,b,p decomposesintopairs-of-pants
and hence admits a complete hyperbolic metric with geodesic boundaries of
arbitrary length.
Asintheorientablecase,compactsurfaceswith χ> 0canbegeometrised:
these areRP2, the Möbius strip, and the Klein bottle. The ﬁrst has an elliptic
structure while the other two have ﬂat structures with geodesic boundary.
6.2.4. Orbifolds. We can push the classiﬁcation and geometrisation fur-
ther to compact two-dimensional orbifolds.
The ﬁnite subgroups ofO(2) are: the cyclicZ2 generated by a reﬂection,
the cyclic Zn generated by a rotation, and the dihedralD2n containing reﬂec-
tions and rotations. Therefore every singular pointx on a two-dimensional
orbifoldO is locally of one of these types:
V/ Z2, V/ Zn, V/ D2n
withV the unit ball inR2. The pointx is called respectively amirror, acone,
and acorner reﬂectorpoint ofO, see Figure 6.11.
We consider for simplicity onlylocally orientable orbifolds, i.e. orbifolds
with isotropy groups inSO(2). In other words, we exclude mirrors and corner
reﬂectors. One such orbifoldO is easily encoded as
(S,p 1,...,p k)
whereS is a surface, and the orbifoldO isS withk cone points with rotational
isotropy groups of orderp1,...,p k > 1. We do not requireO to be globally
6.2. GEOMETRISATION 163
n
n2
Figure 6.11. A mirror, a cone point, and a corner reﬂector on a two-
dimensional orbifold.
orientable, soS can be a non-orientable surface likeRP2. We deﬁne theEuler
characteristic of that orbifold as
χ(O) =χ(S)−
∑(
1− 1
pi
)
.
This deﬁnition is designed to behave well under coverings. Thedegree of an
orbifold coveringO→ O′ is the cardinality of the ﬁbre of any non-singular
point inO′.
Proposition 6.2.9. IfO→O′ is a degree-d orbifold covering then
χ(O) =d·χ(O′).
Proof. Pick a cellularisation ofO′ whose vertices contain the cone points:
it lifts to a similar cellularisation ofO. We consider all the vertices of these
cellularisations as cone points, possibly with order 1, and we get
χ(O′) =V−E +F−
∑(
1− 1
p′
i
)
=−E +F +
∑ 1
p′
i
whereV,E,F is the number of vertices, edges, and faces in the cellularisation
ofO′. The same formula holds forO:
χ(O) =−dE +dF +
∑ 1
pj
.
A cone point of orderp′
i inO′ lifts to some cone points with orderspj1,...,p jl
ofO, such that
d =
l∑
a=1
p′
i
pja
=⇒ d· 1
p′
i
=
l∑
a=1
1
pja
.
This implies thatχ(O) =d·χ(O′). □
6.2.5. Geometrisation of orbifolds.Recall that an orbifold is good if it is
coveredbyamanifold. Withacoupleofexceptions, alltheclosedtwo-orbifolds
are good and geometric.
Theorem6.2.10. Everyclosedlocallyorientable2-orbifold Oisgoodexcept
(S2,p ), (S2,p 1,p 2)
withp1⁄=p2. A good orbifoldO has an elliptic, ﬂat, hyperbolic structure⇐⇒
χ(O) is positive, zero, negative. The elliptic orbifolds are listed in Table 6.1.
164 6. SURFACES
orbifold Γ
S2 {e}
(S2,n,n ) Zn
RP2 Z2
(RP2,n ) D2n
orbifold Γ
(S2, 2, 2,n ) D2n
(S2, 2, 3, 3) T12
(S2, 2, 3, 4) O24
(S2, 2, 3, 5) I60
Table 6.1. Except the two bad cases, every locally orientable closed
orbifold O with χ(O) > 0 can be geometrised asO = S2/Γ for some
discrete Γ < O(3). In all cases Γ < SO(3) and henceO is orientable,
except RP2 and (RP2,n ) whose Γ contains the antipodal map. The groups
on the right table are the spherical Von Dyck groups, see Section 3.6.4.
The groupsT12,O 24,I 60 are the orientation-preserving isometry groups of
the tetrahedron, octahedron, and icosahedron, and are isomorphic toA4,
S4,A5 respectively.
Proof. The orbifolds (S2,p ) and (S2,p 1,p 2) are bad: subdivideS2 into
two discs, each containing at most one cone point; each disc has a unique
surface (disc) covering, but the two coverings do not match ifp ⁄= 1 or
p1⁄=p2. The remaining orbifolds withχ(O)> 0 are
S2, (S2,n,n ), RP2, (RP2,n ),
(S2, 2, 2,n ), (S2, 2, 3, 3), (S2, 2, 3, 4), (S2, 2, 3, 5)
and they can all be realised asS2/Γ for an appropriate ﬁniteΓ < O(3), see
Table 6.1. The orbifolds withχ(O) = 0 are
(S2, 2, 3, 6), (S2, 2, 4, 4), (S2, 3, 3, 3), (S2, 2, 2, 2, 2),
(RP2, 2, 2), K, T
whereK andT are the Klein bottle and the torus. The ﬁrst four orbifolds were
obtained as R2/Γ in Section 3.6.4. The orbifold(RP2, 2, 2) is R2/Γ where Γ
is generated by two glide reﬂections with orthogonal axis:
(x,y )↦→ (x + 1,−y ), (x,y )↦→ (−x,y + 1).
To prove this, consider the fundamental domain[− 1
2, 1
2]× [− 1
2, 1
2].
Ifχ(O)< 0 we construct a hyperbolic metric as we did in the surface case.
IfO = (S2,p 1,p 2,p 3) we getO = H2/Γor(p1,p2,p3) using Von Dyck groups, see
Section 3.6.4. Otherwise, the orbifold O easily decomposes along disjoint
simple closed curves (that avoid the cone points) into some basic pieces with
χ< 0, which are of the following kind:
P, (A,p ), (D,p 1,p 2)
whereP,A,D are the pair-of-pants, the annulus, and the disc, and(p1,p 2)⁄=
(2, 2). We can give a hyperbolic structure toP with any ﬁxed length at the
boundaries.
6.2. GEOMETRISATION 165
a
b c
a
b c2 2
2
a
c
b a
c
b
2
2 2
Figure 6.12. For every angleα⩽ π
2 and lengthsb,c > 0 there is a
pentagon as shown (left); by doubling it along the unmarked edges we
get a hyperbolic annulus with a cone point of angle2α. For every angles
α,β ⩽ π
2 and every lengthc >0 there is a quadrilateral as shown (right).
By doubling it along the unmarked edges we get a hyperbolic disc with
cone points of angle2α and 2β.
Analogously, wecangive aconemanifoldstructurewithgeodesicboundary
to (A,p ) (respectively, (D,p 1,p 2)) with one (two) cone point of angle2π
p ( 2π
p1
and 2π
p2
), for any ﬁxed lengths at the boundaries. We already know this for
P, and the proof for(A,p ) and (D,p 1,p 2) is similar: instead of constructing
right-angled hexagons, we construct pentagons with anglesπ
2, π
2, π
2, π
2, π
p and
quadrilaterals with anglesπ
2, π
2, π
p1
, π
p2
, and we double them, see Figure 6.12.
By gluing all the pieces we obtain a hyperbolic cone structure onO with
cone angles 2π
pi
and we apply Proposition 3.6.18 to translate it to a hyperbolic
orbifold structure. □
Recall that an orbifold is very good if it is ﬁnitely covered by a manifold. In
the following corollary we use the geometrisation to prove shortly a non-trivial
topological fact.
Corollary 6.2.11. Every good closed locally orientable 2-orbifold is very
good.
Proof. Every such orbifold is geometric, so Corollary 3.6.19 applies.□
The punctured case is also interesting whenχ(O) < 0. We deﬁne a
punctured orbifoldto be one of type
O = (Sg,0,b,p 1,...,p k).
Theorem 6.2.12.Every punctured orbifoldO withχ(O)< 0 has a hyper-
bolic structure.
Proof. Same proof as above, where we use triangular groups with possibly
ideal vertices and we allow the piecesP, (A,p ), (D,p 1,p 2) to have boundary
components and/or cone points that degenerate to cusps. To construct them
we build hexagons, pentagons, quadrilaterals with some lengths or angles that
may be zero. □
166 6. SURFACES
These punctured orbifolds are also very good for the same reason above.
It is also possible to consider orbifolds based on surfacesSg,b,p with boundary:
every boundary component can be considered in two natural but distinct ways,
eitherasamirror(hencetheorbifoldislocallynon-orientable), orasaboundary
component: to do this we need to deﬁne an appropriate notion of orbifold with
boundary.
6.2.6. Gauss–Bonnet formula.How can we compute the area of a hy-
perbolic surface? We can easily answer this question in the closed case.
Proposition 6.2.13 (Gauss–Bonnet).LetS be a closed hyperbolic surface.
We have
Area(S) =−2πχ(S).
Proof. Pick a Dirichlet domainD forS. It is a(2n)-gon with inner angles
α1,...,α 2n. By Proposition 3.2.9 we have
Area(S) = Area(D) = (2n− 2)π−
2n∑
i=1
αi.
The surfaceS is obtained fromD by gluing isometrically some pairs of edges.
We get a cellularisation ofS with somev vertices, n edges, and one faceD.
Therefore
χ(S) =v−n + 1.
Each of thev vertices is obtained by identifying some of the vertices ofD,
whose inner angles must sum to2π. Therefore we get
2n∑
i=1
αi = 2πv
and hence
Area(S) = (2n− 2)π− 2πv =−2π(v−n + 1) =−2πχ(S).
The proof is complete. □
We can extend the formula to orbifolds and to the other geometries.
Corollary 6.2.14.Let O be a closed hyperbolic, ﬂat, or elliptic locally ori-
entable 2-orbifold. We have
K· Area(O) = 2πχ(O)
whereK =−1, 0, or+1 respectively.
Proof. IfO is an orientable surface, then the equality holds: in the hyper-
bolic case this is Proposition 6.2.13, in the ﬂat case we get0 = 0, and in the
elliptic caseS =S2 and Area(S2) = 4π = 2πχ(S2).
6.2. GEOMETRISATION 167
In general there is a degree-d coveringS→O of an orientable geometric
surface S by Corollary 6.2.11. The equality holds forS and hence also forO
since
χ(S) =d·χ(O), Area(S) =d· Area(O).
The proof is complete. □
6.2.7. Lie subgroups of SO(3). The following proposition is of general
interest and is used in many diﬀerent contexts. It shows, among other things,
that orientable elliptic orbifolds arerigid: their geometry is fully determined
by their fundamental group. (Flat and hyperbolic surfaces are not rigid, as we
will soon see.)
Proposition 6.2.15.Every non-trivial proper Lie subgroup ofSO(3) is con-
jugate to one of the following:
Cn, D2n, T12, O24, I60, SO(2), SO(2) ⋊C2.
These are the orientation-preserving isometry groups of: a regularn-pyramid,
n-prism, tetrahedron, octahedron, icosahedron, cone, and cylinder.
Proof. The Lie algebrag = so(3, R) is generated by the matrices
Ax =


0 0 0
0 0 −1
0 1 0

, A y =


0 0 1
0 0 0
−1 0 0

, A z =


0 −1 0
1 0 0
0 0 0


with the relations
[Ax,Ay ] =Az, [Ay,Az ] =Ax, [Az,Ax ] =Ay.
Therefore g is isomorphic toR3 equipped with the standard vector product×.
We deduce that the only non-trivial proper sub-algebras ofg have dimension
1, and hence every non-trivial proper Lie subgroupG <SO(3) has dimension
0 or 1.
If a Lie subgroupG <SO(3) has dimension zero, it is ﬁnite. Every non-
trivial element inG is a rotation along some axis, and hence it acts onS2 with
two (antipodal) ﬁxed points. LetP⊂S2 be the set of the ﬁxed points of all
the non-trivial elements ofG.
The groupG clearly acts onP, and a double-counting argument gives
2
(
|G|− 1
)
=
∑
p∈P
(
|Gp|− 1
)
where Gp < G is the stabiliser ofp. The fundamental theorem on group
actions says that
|Gp| = |G|
|O(p)|
168 6. SURFACES
whereO(p) is the orbit ofp. Therefore
2
(
|G|− 1
)
=
∑
p∈P
( |G|
|O(p)|− 1
)
=
∑
O
(
|G|−| O|
)
where in the latter we sum on orbitsO. We divide by|G| to get
(3) 2− 2
|G| =
r∑
i=1
(
1− 1
ai
)
wherea1,...,a r are the orders of the stabilisers of ther orbits.
If r = 1 we geta1 =|G| = 1 and henceG is trivial, a contradiction. If
r = 2 we geta1 = a2 =|G| and hence every orbit is a single point, with
stabiliserG. Therefore the points are antipodal andG =Cn.
Ifr = 3 then (a1,a 2,a 3) is a triple with1
a1
+ 1
a2
+ 1
a3
> 1, that is one of
(2, 2,n ), (2, 3, 3), (2, 3, 4), (2, 3, 5).
In each case one calculates|G| using (3) and deduces the cardinalities of the
three orbits. For instance in the(2, 2,n ) case we have|G| = 2n and the orbits
have cardinality (n,n, 2). One deduces that G contains an index-two cyclic
groupCn and is the symmetry groupD2n of the prism.
In the (2, 3, 3) case we get|G| = 12 and hence the orbits have order
(6, 4, 4). The stabiliser of a point in the order-4 orbitO is a 2π
3 -rotation
that rotates the other three points: one deduces that the points inO are the
vertices of a regular tetrahedron andG is its symmetry group. The other cases
are treated analogously.
IfG has dimension one, it contains the groupSO(2) of all rotations along
some axisr. Either G = SO(2), or there is ag∈ G\ SO(2). If g(r )⁄= r,
thenG contains another SO(2) of rotations alongg(r ), and these two copies
of SO(2) generate a Lie subgroup of dimension> 2 in G, a contradiction.
Therefore every element inG\ SO(2) preserves r and is hence aπ-rotation
along an axis perpendicular tor. ThereforeG = SO(2) ⋊C2. □
