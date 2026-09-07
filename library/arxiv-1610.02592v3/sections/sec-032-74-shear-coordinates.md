---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-032-74-shear-coordinates
section_title: "Shear coordinates"
section_number: 7.4
pages: 219-230
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
Figure 7.14. The standard representation ofSg by identifying the edges
of a 4g-gon has only one vertex; if we triangulate the4g-gon we get an
ideal triangulation forSg,0,1 (left). A move that modiﬁes a triangulation
by adding a new vertex (right).
7.4. Shear coordinates
The Teichmüller space of a punctured surface may also be parametrized
using ideal triangles instead of pairs-of-pants: this viewpoint is maybe a bit
simpler, and generalises successfully to dimension three (via ideal tetrahedra).
The coordinates that it produces are calledshear coordinates.
7.4.1. Idealtriangulations. Indimensiontwoandthreeitiscustomaryto
relaxthedeﬁnitionof triangulation,originallyrestrictedtosimplicialcomplexes,
see Section 1.7.7. We prefer to deﬁne a triangulation in a looser sense, as a
ﬁnite set of triangles glued together by pairing their edges.
Let ∆1,..., ∆2k be an even number of identical copies of the standard
oriented 2-simplex. A triangulationT is a partition of the6k edges of the
triangles into3k pairs, and for each pair a simplicial isometry between the two
edges. The triangulation isoriented if the simplicial isometries are orientation-
reversing. If we glue the triangles along the isometries we get a compact
surface S: we always suppose thatS is connected andT is oriented, hence
S =Sg for someg> 0.
The surface S is triangulated with 2k triangles, 3k edges, and somep
vertices. Vertices, edges, and triangles form a cellularisation ofS, but not
necessarily a simplicial complex: for instance two or three vertices of the same
triangle ∆i can be identiﬁed to a single one along the process, as the following
exercise shows.
Exercise 7.4.1. Construct a triangulation of the torus with one vertex,
three edges, and two triangles.
Let Σ be the non-compact surface obtained by removing thep vertices of
the triangulationT fromS: we say thatT is anideal triangulationfor Σ. The
surface Σ is apunctured surface, i.e. Σ =Sg,0,p withp> 1.
Proposition 7.4.2. We haveχ(Σ) =−k <0. Every punctured surface of
negative Euler characteristic has an ideal triangulation.
212 7. TEICHMÜLLER SPACE
Figure 7.15. On an ideal triangle every edge has a unique perpendicular
which ends at the opposite vertex. The base of this perpendicular is the
midpoint of the edge and the three perpendiculars intersect in a point
called barycenter (left). There is a unique conﬁguration of three pairwise
tangent horocycles centred at the ideal vertices, and their tangency points
are the midpoints of the edges (right).
d
d1
d2
d3
1 2 3 1
'
Figure 7.16. The shear is the signed distanced between two midpoints
after the gluing. By convention the sign is positived > 0 if the points
are as shown here, that is an observer that arrives at the midpoint of an
edge sees the other midpoint on its left: we need the orientation ofT here
(left). Wedevelopatriangulationaroundapuncture v: hereh = 3 (right).
Proof. We haveχ(Σ) = χ(S)−p = p− 3k + 2k−p =−k. An ideal
triangulation forS0,0,3 is constructed by attaching∆1 and ∆2 via the obvious
maps. An ideal triangulation forSg,0,1 is constructed in Figure 7.14-(left) for
all g> 1. An ideal triangulation forSg,0,p with χ(Sg,0,p) < 0 and p> 2 is
obtained from one of these by increasingp as in Figure 7.14-(right). □
7.4.2. Hyperbolic ideal triangulations.LetT be an oriented triangula-
tionwithtriangles ∆1,..., ∆2k. Wesubstituteevery ∆i withanidealhyperbolic
triangle (recall that it is unique up to isometry) and pair the edges with some
orientation-reversing isometries. The resulting oriented punctured surfaceΣ
now inherits a hyperbolic structure of areakπ, since an ideal triangle has area
π. We callT a hyperbolic ideal triangulationfor Σ.
The edges are inﬁnite lines and the gluing isometry is not unique: indeed
there is a 1-parameter family of isometries to choose from at every pair of
7.4. SHEAR COORDINATES 213
Figure 7.17. The universal covering ofΣ is isometric to the interior of
a convex set delimited by some lines inH2, which is the intersection of
(possibly inﬁnitely many) half-planes bounded by disjoint lines.
edges, and the hyperbolic structure depends on that – although the topology
of Σ does not. To encode this dependence, we note that every edge of an
ideal triangle has a preferredmidpoint deﬁned in Figure 7.15. The orientation-
reversing isometry between two edges of two triangles is determined by the
signeddistance d (calledshear)oftheirtwomidpointsasshowninFigure7.16-
(left). The hyperbolic structure onΣ is determined by theshear coordinates
d = (d1,...,d 3k) of the 3k edges of the triangulation.
7.4.3. Complete solutions. The hyperbolic structure on Σ may be in-
complete! Recall that a hyperbolic surface is complete if and only if its uni-
versal cover isH2, so we now look at the universal cover ofΣ.
Proposition 7.4.3. The universal cover˜Σ of Σ is isometric to the interior
of the intersection of some half-planes inH2 with disjoint boundary lines (see
Figure 7.17). The surfaceΣ is complete if and only if˜Σ∼= H2.
Proof. Recall from Section 3.5.3 that there is a developing mapD : ˜Σ→
H2. We prove thatD is injective.
We can constructD as follows: the hyperbolic ideal triangulationT of Σ
lifts to a hyperbolic ideal triangulation˜T of ˜Σ with inﬁnitely many triangles.
Send a triangle of˜T to an arbitrary ideal triangle ofH2 and then develop the
map D by attaching subsequently all the triangles of˜T. At each step the
image ofD is an ideal polygon and we attach a new triangle to the exterior of
some side of the polygon. Therefore at each stepD is injective and henceD
is globally injective.
SinceD is injective we identify˜Σ with its open image inH2. Pick a point
x∈∂ ˜Σ. Every neighbourhood ofx must intersect inﬁnitely many triangles of
˜T, hence there is a sequence of edgesei of ˜T such thatd(ei,x ) is monotone
decreasing and tends to zero. Since theei are disjoint, their endpoints in∂H2
are monotone and tend to two points, which determine a linel. We must have
d(l,x ) = 0 and hencex∈l andl⊂∂ ˜Σ.
214 7. TEICHMÜLLER SPACE
1 2 3
1 2 3' ' '
1 2 3'' '' ''
1 2 3''' ''' '''
1 2 3' ' '3
l
0
s
Figure 7.18. Whend1 +... +dh⁄= 0, the isometryϕ sending ∆1 to ∆′
1
is hyperbolic, with some axisl which (up to translations) has endpoints0
and∞. Hence ϕ(z) = edz and the triangulation develops towardsl as
shown here.
We have discovered that∂ ˜Σ consists of disjoint lines. This proves that
the closure of˜Σ is the intersection of half-planes. A surfaceΣ is complete if
and only if˜Σ is complete, and hence isometric toH2. □
The hyperbolic structure onΣ depends on the shearing coordinatesd∈
R3k, and we now want to understand which values ofd produce a complete
metric. An ideal vertex v of the triangulationT is adjacent to someh tri-
angles, which we denote by∆1,..., ∆h for simplicity although there might be
repetitions, and toh edges with some shearing coordinates that we also indi-
cate byd1,...,d h for simplicity. The vertexv is a puncture ofΣ and we let
N(v ) be a small topological punctured closed disc aroundv.
Proposition 7.4.4. The punctured disc N(v ) is complete if and only if
d1 +... +dh = 0.
Proof. We construct a portion of the developing mapD : ˜Σ → H2 as
follows: we use the half-plane model and send ∆1 to H2 with v = ∞ as
in Figure 7.16-(right), then we develop the triangulation horizontally. In the
picture we haveh = 3 so we reproduce∆1, ∆2, ∆3 and then another copy∆′
1
of ∆1. Letϕ∈ PSL2(R) be the holonomy isometry that sends∆1 to ∆′
1.
If d1 +... +dh = 0 the midpoints of∆1 and ∆′
1 are at the same height
as in Figure 7.16-(right) and thereforeϕ is a parabolic mapϕ: z ↦→ z +b
for someb∈ R. ThereforeN(v ) is a truncation of the cuspH2/⟨ϕ⟩, which is
complete.
If d1 +... +dh⁄= 0 the midpoints of∆1 and ∆′
1 are at diﬀerent heights
and therefore ϕ is not parabolic. Since ∞ ∈Fix(ϕ), the isometry ϕ is a
hyperbolictransformationhavingsomeotherﬁxedpointin R. Uptotranslating
everything we may suppose thatFix(ϕ) ={0,∞}, hence the axisl ofϕ is the
vertical coordinate axis, andϕ(z) =edz withd =d1 +... +dh. The mapD
7.4. SHEAR COORDINATES 215
develops towardsl as shown in Figure 7.18: we getl⊂∂ ˜Σ, so ˜Σ⁄= H2 is not
complete. □
Summing up, we have acompleteness equationof typedi1 +... +dih = 0
for each of thep ideal vertices of the triangulation.
Corollary 7.4.5. The hyperbolic structure onΣ is complete if and only if
d satisﬁes thep completeness equations.
Proof. LetN(v )beasmallpuncturedcloseddiscat v foreveryidealvertex
v. The closure of Σ\∪vN(v ) is compact. Therefore Σ is complete if and
only if eachN(v ) is. □
7.4.4. Shear coordinates for Teichmüller space.The solution space of
the completeness equations is some linear subspaceV ⊂ R3k of dimension
at least 3k−p =−3χ(Σ)−p. Note that this is precisely the dimension of
Teich(Σ), see Section 7.3.5. We have constructed a map
sh :V −→Teich(Σ).
We will prove below thatsh is a homeomorphism and hencedimV = 3k−p.
We will use the following.
Proposition 7.4.6.Let Σ be a complete hyperbolic punctured surface. Ev-
ery ideal triangulation is isotopic to a unique hyperbolic ideal triangulation.
Proof. We describe a procedure thatstraightens every ideal triangulation
T of Σ = H2/Γ to a hyperbolic one.
Truncate the cusps of Σ to get a compact sub-surface. The ideal tri-
angulationT is now truncated to a decomposition into hexagons, each with
three boundary and three interior edges. We lift the truncated cusps and the
hexagons toH2. Truncated cusps lift to horoballs, bounded by horocycles, and
hexagons lift to hexagons (the hexagons are not geodesic, only smooth).
An interior edge of a hexagon inH2 cannot have both its endpoints in
the same horocycle, since it would form a bigon with it, and a bigon does
not decompose into hexagons (by a Euler characteristic argument). Therefore
every interior edge connects two distinct horocycles, centred at two distinct
points of∂H2. Replace this edge with the geodesic line connecting these two
ideal points.
If we do this at every interior edge we get aΓ-invariant hyperbolic ideal
triangulation of H2, which projects to a hyperbolic ideal triangulation forΣ
isotopic toT. □
We can now parametrizeTeich(Σ).
Corollary 7.4.7.The map sh is a bijection.
216 7. TEICHMÜLLER SPACE
1 2 3
1 2 3' ' '
1 2 3'' '' ''
1 2 3''' ''' '''
1 2 3' ' '3
l
0
s
Figure 7.19. Lets be a Euclidean line at hyperbolic distanceR froml.
If R is suﬃciently small, the lines does not intersect the lower edges of
∆1, ∆2, ∆3. LetS be the region lying aboves.
Proof. Proposition7.4.6showsthatineverymetrictheinitialtriangulation
T straightens to an ideal hyperbolic one and is hence realised by somed, so
sh is surjective. Moreover the straightened triangulation is unique and the
parametersdi are obtained intrinsically from it, sosh is also injective. □
7.4.5. Incomplete metrics. The shear coordinatesd may deﬁne an in-
complete metric onΣ, and we now determine its metric completionΣ.
Recall that every ideal vertexv has atotal sheardv =di1 +... +dih which
is zero precisely whenΣ is complete nearv.
Proposition 7.4.8. The metric completionΣ is a hyperbolic surface with
geodesic boundary, whose boundary lengths are the absolute values of the total
shears of the vertices.
Proof. LetN(v ) be a small closed punctured disc aroundv. Ifdv = 0 we
already know thatN(v ) is a truncated cusp. Ifdv ⁄= 0 we developN(v ) in
H2 as in Figure 7.19. The hyperbolic transformation isϕ(z) = edvz and the
points at distanceR from l form a Euclidean lines starting from 0. Pick R
small so thats does not intersect the lower edges of∆1,..., ∆h. Since s is
ϕ-invariant, it is contained in the union of all the developed triangles of Figure
7.19 and hence in˜Σ.
The lines projects to a (non-geodesic) circle inΣ aroundv, and we can
suppose that∂N (v ) is that circle. We haveN(v ) =S/γ whereS⊂H2 is the
region lying aboves. The completionS equalsS∪l and thereforeN(v ) =S/γ
is an annulus with two boundary components: the original non-geodesic∂N (v )
and a new geodesicl/γ, a curve of length|dv|. □
If dv⁄= 0, the edges of the triangulation pointing towardsv spin around
the geodesic boundary as shown in Figure 7.20-(right). The spinning direction
induces an orientation on each component of∂Σ, which depends on the sign
ofdv.
7.4. SHEAR COORDINATES 217
Figure 7.20. Near an ideal vertexv, horocycles (in blue) and edges of
the triangulation (in red) are mutually orthogonal. They behave much
diﬀerently in presence of a cusp (left) or of a geodesic boundary (right):
in a cusp, horocycles form parallel circles and edges point toward the cusp;
near a geodesic boundary, the horocycle point orthogonally toward the
boundary and the edges spin and wind around it indeﬁnitely.
Summing up, every shear coordinated = (d1,...,d 3k)∈ R3k determines
a hyperbolic surfaceΣ with somep′ cusps andb oriented geodesic boundary,
whereb +p′ =p is the number of vertices of the ideal triangulation. The sur-
face Σ is diﬀeomorphic toSg,b,p′. Let Teichor(Sg,b,p′) denote the Teichmüller
space of the surfaceSg,b,p′ equipped with an orientation of theb boundary
components: of course this is just2b copies of Teich(Sg,b,p′).
Proposition 7.4.9. The shear coordinates induce a bijection
R3k←→
⨆
b+p′=p
Teichor(Sg,b,p′).
Proof. The map sendsd ∈ R3k to the complete hyperbolic Σ, and we
now exhibit an inverse. Let Σ be a surface of ﬁnite type with a hyperbolic
structure withp′ cusps andb oriented geodesic boundary components, and
Σ = int(Σ). We may straighten any ideal triangulationT of Σ similarly as we
did in Proposition 7.4.6, with the only diﬀerence that horocycles are replaced
by oriented geodesic lines as lifts of oriented geodesic boundary components;
in the construction, we use the ﬁnal endpoint of the oriented line instead of
the ideal point of the horocycle. We get an ideal triangulation ofΣ whose
completion is Σ. □
For instance,R3 parametrizes altogether all the hyperbolic metrics on the
pair of pants, where each boundary component becomes either an oriented
geodesic or “degenerates” to a cusp.
7.4.6. References. Most of the material presented here is standard and
can be found in many books, starting from Thurston’s notes [56]. The main
reference is Farb – Margalit [18], which also contains the proof of Proposition
218 7. TEICHMÜLLER SPACE
7.2.10, that appeared originally in a paper of Bestvina, Bromberg, Fujiwara,
and Souto [5]. The proof of the Collar Lemma is taken from Hubbard [30].
CHAPTER 8
Surface diﬀeomorphisms
We describe in this chapter an analogy between the hyperbolic spaceHn
and the Teichmüller spaceTeich(Sg)of a closed orientable surfaceSg of genus
g> 1. The theory, originated from Thurston in the late 1970s, provides a
beautiful and powerful framework for the analysis of the geometric and dynam-
ical properties of the surfacesSg and of their mapping class groupMCG(Sg).
Here is a quick sketch of this analogy. We have already seen thatHn
compactiﬁes to a closed discHn, thatIsom(Hn) acts on it, that by Brouwer’s
theorem every non-trivial isometryϕ has a ﬁxed point inHn, and we have
calledϕ elliptic, parabolic, orhyperbolic according to the position of its ﬁxed
points.
We construct in this chapter a similar compactiﬁcation of the open ball
Teich(Sg) to a closed disc. The action of the mapping class groupMCG(Sg)
extends to this closed disc, and by Brouwer’s theorem every non-trivial element
ϕ of MCG(Sg) has a ﬁxed point there. According to the position of the ﬁxed
points ofϕ, we say thatϕ is ﬁnite order, reducible, orpseudo-Anosov.
If ϕ is an isometry for some hyperbolic structure ofSg, it belongs to the
ﬁrst type. Dehn twists belong to the second. The pseudo-Anosov maps are
both the most mysterious and the most important, and for their study we
need to introduce a wealth of beautiful new technology:geodesic currents,
laminations, andtrain tracks.
8.1. Thurston’s compactiﬁcation
Let Sg be a surface of genusg> 2. Recall that Teich(Sg) is the Teich-
müller space ofSg and S = S (Sg) is the set of all non-trivial simple closed
curves inSg, considered up to isotopy and orientation reversal: all the closed
curves considered in this chapter areunoriented.
Although Teich(Sg) and S are very diﬀerent in nature, we want to com-
pactify both spaces by embedding them in a single bigger space. The model
that we have in mind, and that we would like to extend to higher genus sur-
faces, is the ﬂat torus picture that was painted in Section 7.2.4.
We brieﬂy summarise it. The Teichmüller spaceTeich(T ) of the torusT
is H2 and it compactiﬁes toH2; the mapping class groupMCG(T ) acts onH2
as a discrete group of isometries; as such, the non-trivial elements ofMCG(T )
219
220 8. SURFACE DIFFEOMORPHISMS
are divided into three classes (hyperbolic, parabolic, elliptic); the simple closed
curves form a dense countable set of rational points in∂H2 = R∪{∞}.
We now may wonder whether there is an analogous identiﬁcation between
Teich(Sg) and H6g−6 that transforms Teich(Sg) into a discrete subgroup of
Isom(Hn). This is unfortunately not the case, and the compactiﬁcation of
Teich(Sg) must be constructed from scratch via diﬀerent methods: we com-
pactify Teich(Sg) by embedding it in a bigger inﬁnite-dimensional space.
8.1.1. Projectiveimmersion. InChapter7wehaveusedthelengthfunc-
tions to construct an embedding
i : Teich(Sg)↪→ RS.
We know thatTeich(Sg)is homeomorphic to an open ball of dimension6g−6,
and we want to compactify it in a geometrically meaningful way. A ﬁrst
tentative could be to take its closure inRS, but this does not work:
Proposition 8.1.1. The subspacei(Teich(Sg)) is closed inRS.
Proof. The inclusion is proper, hence closed by Proposition 7.3.10.□
We are apparently stuck, so we turn back to our model, hyperbolic space,
to get some inspiration. We recall that Hn is properly embedded in the
lorentzian Rn+1 as a hyperboloidIn. To compactify Hn, we may consider
its imageKn in RPn (the Klein model) and take the closureKn there.
We try to mimic this construction, by considering the inﬁnite-dimensional
projective space P(RS ) with the projection
π : RS\{ 0}−→ P(RS ).
We ﬁrst need to check thatTeich(Sg) embeds there.
Proposition 8.1.2. The composition
π◦i : Teich(Sg)−→ P(RS )
is injective.
Proof. Suppose by contradiction that there are two distinct pointsm,m′∈
Teich(Sg)withπ(i(m)) =π(i(m′)); thisimpliesthatthereisaconstant k >1
such that𝓁γ(m) = k·𝓁γ(m′) for allγ∈ S. That sounds very unlikely, and
we now prove that it easily leads to a contradiction.
Let γ1,γ 2∈ S be two curves withi(γ1,γ 2) = 1. We takex0 =γ1∩γ2
as a basepoint forπ1(Sg,x 0) and note that the elementsγ2∗γ1 andγ2∗γ−1
1
are represented by two more non-trivial simple closed curves inSg. It is easily
checked that the formula
tr(A)· tr(B) = tr(AB) + tr(A−1B)
8.1. THURSTON’S COMPACTIFICATION 221
holds for anyA,B∈ SL2(R). Proposition 7.3.12 implies that
2 cosh
(L(γ1)
2
)
·cosh
(L(γ2)
2
)
= cosh
(L(γ2∗γ1)
2
)
+cosh
(L(γ2∗γ−1
1 )
2
)
.
We have obtained a relation between the lengths ofγ1,γ 2,γ2∗γ1, andγ2∗γ−1
1
that holds for any hyperbolic metric onSg. It may be rewritten as:
cosh
(
L(γ1)+L(γ2)
2
)
+cosh
(
L(γ1)−L(γ2)
2
)
= cosh
(
L(γ2∗γ1)
2
)
+cosh
(L(γ2∗γ−1
1 )
2
)
.
By contradiction everym′-length isk times am-length: this equation is hence
valid after multiplying every argument byk. It is easy to check that
cosha + coshb = coshc + coshd, coshka + coshkb = coshkc + coshkd
if and only if{a,b} ={c,d}. This leads to a contradiction: the number
L(γ1) +L(γ2) is strictly bigger thanL(γ2∗γ1) orL(γ2∗γ−1
1 ), sinceγ2∗γ1
andγ2∗γ−1
1 have a non-geodesic representative of lengthL(γ1) +L(γ2). □
We have embeddedTeich(Sg) in P(RS ), and we now turn to the setS.
8.1.2. Thurston’s compactiﬁcation.We now embed S in P(RS ). A
simple closed curveγ∈ S deﬁnes a functionali(γ)∈ RS by setting:
i(γ)(η) =i(γ,η ).
We have constructed a mapi : S→ RS.
Proposition 8.1.3. The composition
π◦i : S−→ P(RS )
is injective.
Proof. Letγ1,γ 2∈ S be distinct. There is always a curveη∈ S with
i(γ1,η )⁄= 0 and i(γ2,η ) = 0. (If i(γ1,γ 2)> 0, simply takeη =γ2. Other-
wise, it is an easy exercise.) □
We will now tacitly consider bothTeich(Sg) and S as subsets ofRS.
Proposition 8.1.4. The subsets Teich(Sg) and S are disjoint inP(RS ).
Proof. For eachγ∈ S we havei(γ,γ ) = 0, while every curve has positive
length on any hyperbolic metric. □
We can now state Thurston’s compactiﬁcation theorem.
Theorem 8.1.5.The closure Teich(Sg) of Teich(Sg) in P(RS ) is homeo-
morphic to the closed discD6g−6. Its interior isTeich(Sg) and its boundary
sphere contains S as a dense subset.
222 8. SURFACE DIFFEOMORPHISMS
In particular, the closure ofS is homeomorphic to a sphereS6g−7. The
proof of Theorem 8.1.5 occupies most of this chapter and will be completed
in Section 8.3.18. We will introduce in the process various new geometric
objects that play an important role in the topology of manifolds in dimension
