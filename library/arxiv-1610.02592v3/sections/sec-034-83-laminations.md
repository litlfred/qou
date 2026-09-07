---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-034-83-laminations
section_title: "Laminations"
section_number: 8.3
pages: 246-266
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
8.3. LAMINATIONS 239
Figure 8.4. A geodesic lamination inH2.
8.3. Laminations
In this section we characterize geometrically the currentsα∈ C contained
in the “light cone,”i.e. those withi(α,α ) = 0 . Every such current may be
represented as ameasured geodesic lamination, a closed subset ofSg foliated
by geodesics and equipped with a transverse measure. These unexpected ob-
jects play an important part in the topology of manifolds of dimension two and
three.
8.3.1. Geodesiclaminations. LetS = H2/Γ beahyperbolicsurface. Re-
call that in this chapter we consider geodesics only as subsets ofS, neglecting
their parametrisation.
A geodesic laminationλ is a set of disjoint simple complete geodesics inS,
whose union is a closed subset ofS. Each geodesic may be closed or open and
is called aleaf; their union is thesupport ofλ. We will often confuseλ with
its support for simplicity, since the support determines the set of geodesics in
all the interesting cases (see below).
The following examples of geodesic laminations are fundamental:
• a geodesic multicurve (that is a ﬁnite set of disjoint simple closed
geodesics) inS;
• a set of disjoint lines inH2 whose union is closed.
A lamination inH2 may be particularly complicated, see Figure 8.4. Recall
that G = G (H2) is the set of all lines inH2, with its natural topology.
Exercise 8.3.1. A setλ of disjoint lines inH2 forms a closed set inH2 if
and only ifλ is closed when considered as a subset ofG.
If a set of disjoint lines inH2 is not closed, it suﬃces to take its closure
to get a lamination. Every lamination in S = H2/Γ lifts to a Γ-invariant
lamination in H2, hence the laminations inS are in natural bijection with the
Γ-invariant laminations inH2.
240 8. SURFACE DIFFEOMORPHISMS
8.3.2. Local behaviour. A geodesic lamination is often too complicated
to be determined with full precision. In fact, its topology is already quite
involved, and we now start by examining it locally. Letλ be a geodesic lamina-
tion on a hyperbolic surfaceS = H2/Γ. The following exercise may be proved
by passing to the universal coverH2.
Exercise 8.3.2. Every pointp∈ λ has an open neighbourhoodU and a
chartU→ (−1, 1)× (−1, 1) that sendsp to (0, 0) andλ∩U to (−1, 1)×J
for some closed subsetJ⊂ (0, 1).
What kind of J ⊂ (0, 1) may arise? It is possible to construct some
laminations in H2 or in some simple hyperbolic surfaces like cusps and tubes,
where their support is the whole manifold. In this caseJ is the full interval
(0, 1). These cases are however of no interest for us, because of the following.
Proposition 8.3.3. IfS has ﬁnite volume, thenJ has empty interior.
Proof. Suppose by contradiction thatJ contains some open interval. This
open interval determines a set of leaves ofλ, whose lift inH2 forms an open
subsetU⊂ H2 foliatedintolines. Itslimitin ∂H2 hasnon-emptyinterior S. By
Corollary 5.1.14 there is a hyperbolic transformationγ∈ Γ with an attracting
limit point inS. This implies easily that there areγ-translates of some lines
inU that intersect some lines ofU transversely, a contradiction. □
Corollary 8.3.4. If S has ﬁnite volume, every geodesic laminationλ in S
has empty interior and is determined by its support.
8.3.3. Complementary regions. Let λ⊂S be a geodesic lamination in
a hyperbolic surfaceS = H2/Γ. A complementary region(shortly, aregion)
is a connected component of the open complementS\λ. The abstract
completion of a complementary region is a hyperbolic surface with non-empty
geodesic boundary consisting of lines and/or circles.
In general, a complementary region may have genus and/or inﬁnitely many
boundary components. Note that in any case there are at most countably
many regions, and hence only countably many leaves ofλ may be incident to
a region: ifλ has uncountably many leaves (this will be the typical case), most
leaves are not incident to any region (compare this with the Cantor subset in
[0, 1], which contains uncountably many points, but only countably many of
them are adjacent to some complementary open segment).
Proposition 8.3.5. A geodesic laminationλ⊂ Sg in a closed hyperbolic
surfaceSg = H2/Γ has at most4g− 4 complementary regions. The boundary
of each region has ﬁnitely many components.
Proof. Everycomplementaryregionhasareaatleast π(theareaofanideal
triangle) and a region with inﬁnitely many boundary components has inﬁnite
area. By Gauss-Bonnet we getArea(Sg) =−2πχ(Sg) = (4g− 4)π. □
We say that a laminationλ⊂Sg is full if every region is an ideal polygon.
8.3. LAMINATIONS 241
8.3.4. Transverse measures. Let λ⊂ S be a geodesic lamination in a
hyperbolic surfaceS. Atransverse arctoλ is the support of a simple regular
curve α: [a,b ]→S transverse to each leaf ofλ, whose endpointsα(a) and
α(b) are not contained inλ.
Deﬁnition 8.3.6. Atransverse measurefor a laminationλ⊂S is a locally
ﬁnite Borel measureLα on each transverse arcα such that:
(1) ifα′⊂α is a sub-arc ofα, the measureLα′ is the restriction ofLα;
(2) the support ofLα isα∩λ;
(3) the measure is invariant through isotopies of transverse arcs.
In particular every arcα transverse toλ has a ﬁnitelength, deﬁned as
the total measure of the arc. The arc has length zero if and only ifα∩λ =
∅. A measured geodesic laminationis a geodesic lamination equipped with a
transverse measure.
Example 8.3.7. A geodesic multicurveλ ⊂ S has a natural transverse
measure: for any transverse arcα, the measureLα on α is just the Dirac
measure supported on the ﬁnite setα∩λ.
More generally, we may assign a positive weightai > 0 at each component
λi ofλ and deﬁne a measured geodesic lamination by giving the weightai at
each intersectionα∩γi. By varying weights we get distinct measured geodesic
laminations with the same support.
8.3.5. Currents and measured geodesic laminations.Let Sg = H2/Γ
be a closed hyperbolic surface. We now construct a natural bijection between
the measured geodesic laminations onSg and the geodesic currentsλ with
i(λ,λ ) = 0, i.e. those lying in the “light cone.” We see a measured geodesic
lamination inSg as a Γ-invariant measured geodesic lamination inH2.
Letλ∈ C be a geodesic current withi(λ,λ ) = 0. By Remark 8.2.24 the
support ofλ is a closedΓ-invariant subset ofG formed by disjoint lines, hence
a Γ-invariant lamination inH2. The geodesic current induces also a transverse
measure as follows. Letα be an arc transverse to the laminationλ. Up to
cuttingα in ﬁnitely many arcs we may suppose that it intersects each leaf of
λ in at most one point. We deﬁne the measure of a Borel setU⊂α as the
λ-measure in G of the lines inλ that it intersects.
Exercise 8.3.8. This transverse measure satisﬁes the axioms of Deﬁnition
8.3.6 and givesλ the structure of aΓ-invariant measured geodesic lamination.
Proposition 8.3.9. We have just deﬁned a bijection
{
currentsλ withi(λ,λ ) = 0
}
←→
{
measured geodesic laminations in Sg
}
Proof. We deﬁne the inverse map by transforming aΓ-invariant measured
geodesic laminationλ into a geodesic current with supportλ⊂ G as follows.
For every leafl of λ, we pick a small transverse arcα that intersects all the
242 8. SURFACE DIFFEOMORPHISMS
leavesin aneighbourhood Ul ofl inλ, eachonce. The measureonαtranslates
into a measure onUl, and all the measures on these small setsUl match to
yield a measure onλ thanks to Proposition 1.3.4. □
We denote byML⊂ C the set of all the measured geodesic laminations
on Sg, henceforth identiﬁed with the currents lying in the “light cone”. With
this identiﬁcationML is independent on the auxiliary hyperbolic metric onSg.
Recall that a multicurve onSg is a ﬁnite collection of disjoint non-trivial
simpleclosedcurves. Amulticurvedeterminesameasuredgeodesiclamination:
considern parallel components as a single one with weightn, take the geodesic
representativeoftheresultingessentialmulticurve(keepingthesameweights),
and use Example 8.3.7. We obtain the inclusions
S⊂ M⊂ ML⊂ C
where S and M are the sets of simple closed curves and multicurves inSg.
8.3.6. Some properties. We can now use our knowledge of the geodesic
currents to get some information about the measured geodesic laminations.
Proposition 8.3.10. Let λ⊂Sg be a measured geodesic lamination. For
every p∈∂H2, there are at most two lines in the preimage˜λ⊂ H2 incident
top, and if there are two, none of them projects to a closed geodesic inλ.
Proof. If there are at least three linesl1,l 2,l 3 incident top, withl2 lying
strictly betweenl1 and l3, we may ﬁnd a small arcα transverse to ˜λ, whose
supportliesbetween l1 andl3, thatintersectsl2 andpossiblyotherlinesincident
to p, and no other line of˜λ (use Proposition 8.3.3 nearl2 here). The lines
intersected byα form a pencil with positive mass. By Proposition 8.2.8 the
pencil consists of a single line, the axis of a hyperbolic elementϕ∈ Γ.
On the other hand, ifp is the endpoint of the axis of someϕ, then no
other leafl ⊂ ˜λ can be incident top, otherwise inﬁnitely many linesϕi (l)
would also be, and the same argument above would give a contradiction.□
Exercise 8.3.11. There are some geodesic laminations inSg that do not
support any transverse measure.
Hint. Construct a geodesic laminationλ⊂Sg consisting of some disjoint
simple closed curves and ﬁnitely many open leaves that wind around them (see
Section 7.4.5). The pre-image˜λ⊂ H2 contradicts Proposition 8.3.10. □
8.3.7. Intersection form. What is the geometric meaning of the inter-
section formi of two geodesic currents, when applied to a measured geodesic
lamination? Let λ be a measured geodesic lamination in a hyperbolic closed
surfaceSg = H2/Γ. Three cases are relevant for us:
(1) Ifγ isasimpleclosedgeodesic, theneither γ iscontainedin λ, andwe
geti(γ,λ ) = 0, orγ is disjoint fromλ, and we still geti(γ,λ ) = 0, or
8.3. LAMINATIONS 243
γ is transverse toλ, and in that casei(λ,γ ) equals the full measure
L(γ) ofγ as a transverse curve toλ.
(2) Ifλ′ is another measured geodesic lamination, theni(λ,λ′) “counts”
the (possibly inﬁnitely many) transverse intersections ofλ and λ′
with respect to the product of the two transverse measures.
(3) If m is a hyperbolic metric, theni(λ,m ) measures the “length” of
λ with respect tom, that is the integral overλ of the usual length
weighted with the transverse measure.
We now consider a non-geodesic non-trivial simple closed curveγ trans-
verseto λ, andwedenoteby L(γ)itsfulltransverse λ-measure. Thequantities
L(γ) andi(γ,λ ) need not to be equal in this case (becauseγ is not geodesic),
but this phenomenon is easily controlled by a suitable version of the bigon
criterion.
Proposition 8.3.12.We haveL(γ)>i(γ,λ ) and the equality holds⇐⇒γ
forms no bigon with any leaf ofλ.
Proof. We follow the proof of Theorem 6.3.10. Let˜λbe thecounterimage
of λ in H2. A lift ˜γ of γ has distinct endpoints in∂H2 and ˜γ must intersect
the leaves of˜λ whose endpoints are linked with them. The curve˜γ intersects
each such leaf only once and no other leaf⇔ ˜γ forms no bigon with any leaf
of ˜λ⇔γ forms no bigon with any leaf ofλ. □
Proposition 8.3.13. If λ ∈ ML is full, we havei(λ,α ) > 0 for every
currentα that is not a measured sublamination ofλ.
Proof. Ifi(λ,α ) = 0 then every linel in the support ofα is either a leaf
of λ or an inﬁnite diagonal in some complementary ideal polygon; a diagonal
would be an atomic point inα that would cover a closed geodesic and could
be added toλ contradicting Proposition 8.3.10. □
8.3.8. Train tracks. How can one construct a measured geodesic lami-
nation, concretely? There are some nice combinatorial tools designed to this
purpose, called train tracks.
A train track in a closed surfaceSg is a closed subsetτ ⊂ Sg built by
taking a ﬁnite set of points (calledvertices orswitches) and joining them with
disjoint arcs calledbranches. We require that every switch looks locally like
Figure 8.5-(1): all branches have the same tangent line, and there is at least
one branch at each side.
Thecomplementaryregions ofτ aretheabstractclosuresoftheconnected
components of Sg\τ. Each complementary region is naturally a compact
surface with ﬁnitely many singular vertices in its boundary having “zero interior
angle”. Inthedeﬁnitionofatraintrack, wealsorequirethatnocomplementary
region be a disc, an annulus, a monogon, or a bigon, as in Figure 8.5. An
example is shown in Figure 8.6. The exclusion of these complementary regions
is essential to get the following.
244 8. SURFACE DIFFEOMORPHISMS
(1)
(2)
Figure 8.5. A switch containsa> 1 and b> 1 branches on each side:
here a = 3 and b = 2 (1). The complementary regions of a train track
contain no discs, annuli, monogons, or bigons (2).
Figure 8.6. A train track on the genus-three surfaceS3.
Exercise 8.3.14. A train track contains at most−6χ(Sg) switches and
at most−2χ(Sg) regions; it contains−6χ(Sg) switches if and only if every
switch is trivalent and every complementary region is a triangle. The sphere
and the torus contain no train track.
Hint. Make the appropriate Euler characteristic computation. □
Exercise 8.3.15. Construct a train track with−2χ(Sg) triangular comple-
mentary regions inSg for everyg> 2.
Hint. Take a pants decomposition and add three arcs (tangent to the
boundary) inside each pants to decompose it into two triangular regions.□
We obtain a ﬁniteness property.
Corollary 8.3.16. There are only ﬁnitely many train tracksτ in Sg up to
diﬀeomorphism (but not up to isotopy!).
8.3. LAMINATIONS 245
Figure 8.7. Decompose S into pairs of pants and annuli, so that each
simple closed curve separates a pair of pants from an annulus. We mark
a blue point in each curve.
Figure 8.8. Identify each pair of pants and annulus with one of these
two ﬁxed models.
Proof. There are only ﬁnitely many combinatorial types forτ, its comple-
mentary regions, and the way they are adjacent. □
8.3.9. Weight systems. A weight systemon a train trackτ⊂Sg is the
assignment of a non-negative real number, calledweight, to each branch ofτ,
such that at every vertex theswitch conditionholds: the sum of the weights
on the left branches should be equal to the sum of the weights on the right
branches.
Let w be an integral weight system, that is one whose weights are all
integers. The integral weight systemw determines a closed 1-manifold inSg
as follows: replace every branch with weighta witha parallel copies of it, and
pair all the branches at every switch in the obvious way (this is possible thanks
to the switch condition).
Proposition 8.3.17. The resulting closed 1-manifold is a multicurve.
Proof. Since no complementary region ofτ is a disc or monogon, the
complementary regions of the closed 1-manifold have non-positive Euler char-
acteristic (exercise). □
Our aim now is to use the train tracks to parametrise all the multicurves in
Sg. Later on, wewillextend everythingfrom multicurves tomeasured geodesic
laminations.
8.3.10. A parametrisation forM. Let Sg have genusg> 2. We now
construct ﬁnitely many train tracks that parametrise all the multicurves inSg,
246 8. SURFACE DIFFEOMORPHISMS
andtothispurposeweﬁxaframesimilartotheoneusedintheFenchel-Nielsen
parametrisation of the Teichmüller space.
We decomposeSg into pairs of pants and annuli as in Figure 8.7. We mark
(in blue) an arbitrary point in each closed curve and we also ﬁx once for all a
diﬀeomorphism (preserving orientation and marked points) between each pair
ofpantsandannuluswiththecorrespondingmodelinFigure8.8. Theresulting
parametrisation of M will depend also on these ﬁxed diﬀeomorphisms.
Let a colouring be the assignment of a tripleai,bi,ci of non-negative
numbers to each annulus of the decomposition, such that one of the following
equalities holds:
ai =bi +ci, b i =ci +ai, c i =ai +bi.
We assign the colourai to each of the two curves that bound the annulus.
Since there are− 3
2χ(Sg) = 3g− 3 annuli, we get− 9
2χ(Sg) = 9g− 9 colours
overall. The colouring is integral if the colours are integers and also the
following holds: for each pair of pants, the sumai +aj +ak of the colours of
its boundary curves must be even.
We now transform each colouring into a weighted train trackτ as follows.
The boundary components of each pair-of-pantsP are coloured by some triple
ai,aj,ak. We insert inP a portion of train track as in Figure 8.9: its shape
depends on the position of the point[ai,aj,ak] in RP2 and its weights depend
linearly onai,aj,ak. Note that there are ﬁnitely many possible shapes overall.
We extend the train track inside each annulusA coloured withai,bi,ci as
shown in Figure 8.10. Again, the shape of the portion depends on the position
of [ai,bi,ci ] in RP2. As a result we get a train trackτ with integral weights
and hence a multicurve.
Proposition 8.3.18. The construction produces a bijection
{
integral colourings
}
←→ M.
Proof. We start by proving surjectivity. Given a multicurveµ∈ M, we
minimise its intersections with our decomposition into pants and annuli: now
µ intersects every pair of pantsP into non-trivial simple closed curves and arcs
(an arc is trivial if it forms a bigon with∂P).
By decomposingP into two hexagons, and minimising the intersections of
the curves and arcs with them, one deduces easily thatP contains only three
isotopy classes of non-trivial closed curves (one parallel to each component of
∂P) and six isotopy classes of non-trivial arcs (one connecting every pair of
components of∂P). Note that isotopies arenot required to ﬁx∂P pointwise.
We isotope all the closed curves away fromP and place them inside the
adjacent annuli, so there are only arcs. As above, we check easily that the
isotopy class of the whole set of arcs inP is determined by the intersection
numbersai,aj,ak with the components of∂P and is hence represented by the
corresponding train track portion from Figure 8.9.
8.3. LAMINATIONS 247
[1,0,0]
[0,1,0] [0,0,1]
[1,1,0] [1,0,1]
[0,1,1]
ak
aj
a -i j aka -
ai aj ak   -j+ ak ai aj   -+
aj ak ai   -+
2 2
2
2
aia -k aja -i
2
aiaj
ai
aiak
a -j aia -k
2
Figure 8.9. The portion of weighted train track in a pair of pants
P is determined by the point Q = [ ai,aj,ak] ∈ RP2. Having non-
negative entries, the point Q is contained in the triangle with vertices
[1, 0, 0], [0, 1, 0], [0, 0, 1]. This triangle subdivides into four sub-triangles
by adding the vertices[0, 1, 1], [1, 0, 1], [1, 1, 0] and the shape of the train
track depends on which sub-triangle containsQ. The three edges of the
train track are given the weights indicated in the ﬁgure: these are the only
weights that sum toai,aj,ak at the boundaries. WhenQ lies in the fron-
tier of two or more triangles some branch has weight zero and we delete
it: the diﬀerent shapes prescribed by the adjacent triangles coincide after
deleting this branch.
We now turn to annuli. On each annulusA, there is only one isotopy class
of non-trivial arcs and one isotopy class of non-trivial closed curves. However,
an arc may wind many times aroundA and we are not allowed to use isotopies
that move∂A anymore because the conﬁguration inP is already ﬁxed: one
deduces easily that the triples(a,b,c ) from Figure 8.10 describe precisely all
the possible conﬁgurations.
The injectivity is surprisingly simple to prove: the conﬁguration ofµ that
minimises its intersections with the decomposition into pairs of pants and
248 8. SURFACE DIFFEOMORPHISMS
Figure 8.10. The portion of weighted train track in each annulusA
is determined by the pointQ = [a,b,c ] = [ ai,bi,ci ] ∈ RP2. By hy-
pothesis Q is contained in the boundary of the triangle with vertices
[1, 0, 0], [0, 1, 0], [0, 0, 1]. The boundary subdivides into three segments
and the shape of the train track depends on which segment containsQ.
WhenQ is a vertex some branch has weight zero and we delete it.
a
b
c a
b
c{
{
{
(1) (2) (3)
a
{
Figure8.11. Howtoconstructalaminationfromaweightedtraintrack.
Here we have a switch with weightsa, b, c (1) and the switch condition
a =b +c allows all the Euclidean rectangles (2) to glue (3).
annuli is unique thanks to Proposition 6.3.24 and hence the numbersai,bi,ci
are easily determined byµ. The proof is complete. □
We have found a complete combinatorial parametrisation for the setM,
and we now want to extend it toML.
8.3.11. Topological laminations. A train track τ in Sg with integer
weights parametrises a multicurve. We now show that, more generally, a
weighted train track parametrises a measured geodesic lamination.
The construction goes as follows. First, we remove all the branches with
zero weight, and we replace every branch of weighta >0 with a Euclidean
8.3. LAMINATIONS 249
rectangle of widtha and with arbitrary length as in Figure 8.11-(2). Thanks to
the switch conditions, these rectangles glue nicely at each switch as in Figure
8.11-(3).
In Figure 8.11-(3) we see that all the lines from left- and right-rectangles
are matched in a 1-1 correspondence, with a ﬁnite number of exceptions. At
each exception, somem> 1 left-lines are matched to somen> 1 right-lines
at some point, and we havem +n = 3 or 4. We call these lines and points
singular.
After gluing the rectangles we get a closed subsetλ ofSg foliated by lines,
with ﬁnitely many singular points and lines. We now eliminate the singular
points and lines by cuttingλ carefully along them: ifm +n = 4 this amounts
simply to doubling the singular point; ifm +n = 3 we double the singular leaf
by opening a small open corridor in the foliation, starting from the singular
point and digging along the leaf. Since the singular leaf may be non-compact,
for the process to converge inSg we need to shrink the width of the corridor
suﬃciently fast.
After this cut we get a closed subset ofSg, which we still nameλ, nicely
partitioned into disjoint lines that may be either open or closed: we call it a
topological lamination. After the cut every rectangle of typeL× [0,a ] as in
Figure 8.11 transforms into a setL×J where J is obtained by cutting[0,a ]
along (at most) countably many points. Note thatJ may be a Cantor set.
The setJ inherits from [0,a ] a Borel measure with total massa. This
measure gives a transverse measure to the leaves of the rectangleL×J, and
λ inherits the structure of a measured topological lamination (the notion of a
transverse measure is exactly the same as in the geodesic case).
It only remains to promote the topological lamination to a geodesic lam-
ination: this is usually done by straightening its leaves. We describe this
procedure only for a particular class of train tracks: the ones introduced in the
previous section to parametriseM.
8.3.12. A parametrisation forML. We now extend the arguments of
Section 8.3.10 from multicurves to laminations.
We ﬁx a decomposition ofSg into pants and annuli. Every colouring
(ai,bi,ci ) produces a weighted train track, which in turn parametrises a mea-
sured topological laminationλ. We ﬁx a hyperbolic structureSg = H2/Γ.
The laminationλ can bestraightened to a measured geodesic lamination
¯λ as follows. A leaf l of λ is either a closed curve in some annulusA, or
it intersects every annulusA and pair of pantsP in non-trivial arcs: in both
cases, every lift ofl in H2 is a curve with two distinct limit endpoints in∂H2,
see Figure 8.12. We replace every lift ofl with the unique line having these
endpoints, and we do this for every leafl ofλ.
The result is aΓ-invariant closed set of disjoint lines inH2 that project to
a geodesic lamination ¯λ in Sg. The transverse measure onλ easily induces
250 8. SURFACE DIFFEOMORPHISMS
Figure 8.12. The decomposition into pants and annuli ofSg is homo-
topic to a geodesic pants decomposition (with each curve counted twice)
whose counterimage inH2 consists of inﬁnitely many disjoint ultraparallel
lines as in the picture. We show that the lift of a leafl ofλ in H2 has two
distinct endpoints in∂H2: if l is a closed curve in an annulusA, then it
is isotopic to a closed geodesic and we are done; ifl intersects annuli and
pairs of pants into non-trivial arcs, its lift intersects the ultraparallel lines
forming no bigons, hence it intersects each line at most once: therefore it
has disjoint limits at±∞ (left). The straightening replaces the lift with
the unique line with these endpoints (right).
one on the straightened ¯λ: it suﬃces to consider transverse arcs contained
in the decomposition into pairs of pants and annuli. Note that some parallel
closed leaves ofλ may have collapsed to a single atom closed geodesic in¯λ.
Proposition 8.3.19. The construction induces a bijection
{
colourings
}
←→ ML.
Proof. WeadapttheproofofProposition8.3.18, startingwithsurjectivity:
given a measured geodesic laminationλ, we determine a colour (ai,bi,ci )
representing it.
The decomposition into pairs of pants and annuli is homotopic to a ge-
odesic pants decompositionµ = γ1⊔... ⊔γ3g−3 (with each curve counted
twice). We setai =i(γi,λ ).
The measured geodesic laminationλ∈ ML decomposes asλ =λ0⊔λ1
whereλ0 =∑
ikiγi is a weighted pants decomposition with support inµ and
λ1 is transverse toµ. Ifki⁄= 0 then necessarilyai = 0 and we setbi =ci =ki.
At every pair of pantsP the three coloursai,aj,ak determine a portion
of weighted train track as prescribed by Figure 8.9. The intersectionλ1∩P
consists of geodesic and hence non-trivial arcs: therefore the weighted train
track describes faithfully this portion of measured geodesic lamination, up to
isotopy. The numbers bi and ci are then determined by the way these two
portions wind and match alongγi. The colours(ai,bi,ci ) parametriseλ.
The choices of the colours(ai,bi,ci ) were forced by the intersection ofλ
with the two pantsP adjacent toγi (exercise). This shows injectivity. □
8.3. LAMINATIONS 251
gg
Figure 8.13. A monotonic curve γ intersects the products L×J in
monotonic paths (left) and forms no bigons outside the products (right).
We have parametrised ML, and we now investigate its topology. The
space of all colourings(ai,bi,ci ) forms the subsetC×...×C⊂ R3×...× R3
where C⊂ R3 is the cone based on the origin over the sides of the triangle
with vertices (1, 1, 0), (0, 1, 1), and (1, 0, 1), and is homeomorphic to R2.
The space of colourings is homeomorphic toR2·(3g−3) = R6g−6, that is to the
Teichmüller space itself!
The parametrisation identiﬁesML with C×... ×C. We want to show
that this identiﬁcation is a homeomorphism, and to this purpose we study the
intersection form.
8.3.13. Intersection form. We now show that the intersection formi
between curves and laminations has a surprisingly simple behaviour after that
we parametrise the spaceML asC×... ×C.
We note thatC×... ×C is a piecewise-linear object inR9g−9, that is it
is the support of a simplicial complex. Recall that a continuous map between
simplicial complexes issimplicial if it sends each simplex onto a simplex in an
aﬃne linear way, and it ispiecewise linearif it restricts to a simplicial map on
some subdivisions. Finally, the map ishalf-integral piecewise linearif all the
aﬃne linear maps have half-integer (possibly integer) coeﬃcients.
Proposition 8.3.20. For everyγ∈ S the map
C×... ×C→ R
λ↦−→i(γ,λ )
is half-integral piecewise linear.
Proof. A colour (ai,bi,ci )∈ C×... ×C deﬁnes a weighted train track
τ and hence a measured topological laminationλ, obtained by substituting
every edge ofτ with some productL×J of horizontal leaves. Thanks to
Proposition 8.3.12 the intersectioni(γ,λ ) is realized by some representative
γ which is either a leaf ofλ or is transverse toλ and forms no bigon with any
leaf ofλ.
We say that a closed curve transverse toλ is monotonic if
252 8. SURFACE DIFFEOMORPHISMS
Figure 8.14. If a monotonic curveγ forms a bigon with a leafα, by
cutting carefullyτ along γ we construct a portion of train track on this
bigon containingα and with truncated edges exiting orthogonally fromγ
(left). We then simplify the triangles adjacent toγ (right).
(1) it intersects every productL×J into arcs that are monotonic in
both coordinates, and the same monotonicity is preserved when the
curve goes from one productL×J to an adjacent one as in Figure
8.13-(left);
(2) it makes no bigons outside the rectangles as in Figure 8.13-(right).
Concerning (1), a horizontal path inL×J disjoint fromλ is allowed, but
it must keep being horizontal on the adjacent products.
A simple closed curve that forms no bigons with any leaf ofλ can be easily
isotoped to be monotonic. Conversely, we now prove that a monotonic curve
γ forms no bigons with any leaf ofλ. If it did, by cuttingτ alongγ we would
get an abstract bigon with a portion of train track as in Figure 8.14-(left). Ifγ
is adjacent to some triangles as in Figure 8.14-(right) we close them as shown
there. Finally, by doubling the bigon alongγ we get a train track on a disc,
and by doubling again we build a train track in a sphere, which is absurd (one
checks easily that no complementary region is a disc, annulus, monogon, or
bigon: there are no bigons because we have closed the triangles as in Figure
8.14-(right)).
Theλ-transversal lengthL(γ) of a monotonicγ is the sum of the lengths
of the sub-paths intersecting sequences of productsL×J as in Figure 8.13-
(left). One checks easily that the length of each sub-path is a half-integer
linear combination of the colours(ai,bi,ci ). Therefore L(γ) = i(γ,λ ) is a
half-integer combination of the colours.
If we vary the colouring(ai,bi,ci ) a little, the curveγ keeps being mono-
tonic in the same way as before, except when a portion ofγ is horizontal: in
that case the new monotonicity depends on how the colouring varies. In all
cases, the newγ is still monotonic, hence bigonless, henceL(γ) = i(γ,λ )
again.
If there are no horizontal portions inγ, the lengthL(γ) varies linearly with
the same integral formula found above. If there are horizontal portions, then
8.3. LAMINATIONS 253
the colour lies in a hyperplane ofR9g−9, and there are two diﬀerent linear
formulas joining there. Hencei(γ,λ ) is half-integral piecewise linear. □
The mapλ↦→ i(γ,λ ) is also obviously homogeneous, in the sense that
i(γ,tλ ) =ti (γ,λ ) for allt> 0.
The proof of Proposition 8.3.20 contains a recipe for calculatingi(γ,λ ). It
suﬃces to putγ in monotonic position and then add the contributions of each
monotonic arc. For instance, thei-th curveγi of the pants decomposition has
an obvious monotone position givingi(γi,λ ) =ai.
The coloursbi andci do not have such an immediate description, but the
following holds anyway.
Exercise 8.3.21. There exist ﬁnitely many simple closed curvesγj whose
intersections i(λ,γj ) determine the colouring (ai,bi,ci ) representing λ in a
half-integral piecewise-linear continuous fashion.
Hint. Choose some additional curves as in Proposition 7.3.4 and compute
their intersections withλ. □
8.3.14. The Thurston boundary.We can ﬁnally determine the topology
ofthemeasuredgeodesiclaminationsspace MLandoftheThurstonboundary
of the Teichmüller space.
Proposition 8.3.22. The colouring parametrisation induces a homeomor-
phism ML∼= R6g−6.
Proof. The map ML→ C×... ×C∼= R6g−6 is continuous by Exercise
8.3.21. It is proper: if the colours(ai,bi,ci ) stay bounded, the intersections
i(λ,γi )withﬁnitelymanyﬁllingcurvesγi staybounded,andhence λmovesina
compact set by Proposition 8.2.26. The continuous map is a homeomorphism
by Proposition 7.3.11. □
Let now PML⊂ PC be the set of allprojective measured laminations,
that is the image ofML\ 0 in PC. The set PML contains the projective
simple closed curvesPS and the projective multicurvesPM.
Theorem 8.3.23.The following homeomorphism holds
∂Teich(Sg) = PML∼=S6g−7.
The set PS is dense inPML.
Proof. The homeomorphismML∼= R6g−6 induces PML∼=S6g−7. Con-
cerning the Thuston boundary, we know from Section 8.2.18 and Proposition
8.2.34 that
PS⊂∂Teich(Sg)⊂ PML.
We now show thatPS is dense inPML, and this concludes the proof.
First, we prove thatPM is dense in PML. Rational colours (ai,bi,ci )
form a dense subset ofC×... ×C and project to a dense subset ofPML.
254 8. SURFACE DIFFEOMORPHISMS
Every rational colour is a multiple of an integer colour, which represents a
multicurve.
Second, we prove thatPS is dense inPM. Letµ be a multicurve inSg.
Up to acting viaMCG(Sg) we may suppose thatµ is supported on the pants
decomposition γ1,...,γ 3g−3 used to deﬁneC×... ×C, henceµ is deﬁned
by some integral colour(ai,bi,ci ) = (0,bi,bi ). Now pick any simple closed
curveγ witha′
i =i(γ,γi )> 0 for alli, represented by some colours(a′
i,b′
i,c′
i ).
By Dehn twistingγ along theγi we vary the pairb′
i,c′
i as we please, and by
twisting at the correct rates we construct a sequence of simple closed curves
that converge projectively to[µ]. □
The mapping class groupMCG(Sg) acts naturally on the whole setC of
currents and in particular it acts by homeomorphisms on∂Teich(Sg).
The identiﬁcation of∂Teich(Sg) = PML with the projectivisation ofC×
... ×C is of course not canonical because it depends on a decomposition of
Sg into pairs of pants and annuli. However, Proposition 8.3.20 and Exercise
8.3.21 imply that any two diﬀerent identiﬁcations diﬀer by some projective
integral piecewise-linear homeomorphisms, hence the Thurston boundary has
a natural projective integral piecewise linearstructure, called PIP for short,
which is preserved byMCG(Sg). In particular PML contains some natural
rational points, and these arePM.
8.3.15. Aprojection. Thereaderhasprobablynotedthatthecoordinates
that yield the homeomorphismsTeich(Sg)∼= R6g−6 and∂Teich(Sg)∼=S6g−7
are quite similar: they both depend on a pants decompositionµ plus some
additional marking, and every curve of the pants decomposition contributes
roughly with two parameters, a “length” and a “twist”. It would now be rea-
sonable to expect that both these coordinates merge nicely to give a global
homeomorphism Teich(Sg)∼=D6g−6, but this is unfortunately not the case.
The proof that Teich(Sg) is homeomorphic toD6g−6 is disappointingly
indirect. Weﬁrstprovethat Teich(Sg)isatopologicalmanifoldwithboundary,
by constructing some charts. To construct a chart, we ﬁrst build a map
q : Teich(Sg)→ ML
that depends only on a ﬁxed pants decompositionµ. For a given hyperbolic
metricm∈ Teich(Sg), we construct a measured geodesic laminationq(m) as
follows. We straightenµ to its geodesic representative (with respect tom),
andweconsiderseparatelyeachgeodesicpairofpants P ofthedecomposition.
We ﬁrst show thatP has a natural partial foliation, that depends only on its
metric, whose leaves are not geodesics. We then glue these partial foliations
to get a partial foliation onSg, and then straighten it to a geodesic lamination
q(m).
The natural partial foliation onP is constructed as follows. Letgij be the
unique orthogeodesic connecting thei-th andj-th boundary component ofP,
8.3. LAMINATIONS 255
(1) (2)
Figure 8.15. Every geodesic pair of pantsP has a natural partial folia-
tion: theshapeofthefoliationisdeterminedbythesub-trianglecontaining
Q = [a1,a 2,a 3] in Figure 8.9, wherea1,a 2,a 3 are the lengths of∂P; the
two pictures shown here correspond to two cases. In each case, there
are three rectangles: each is theR-neighbourhood of the corresponding
(unique) orthogeodesic (drawn in blue), andR is the linear combination
ofa1,a 2,a 3 prescribed by Figure 8.9, that is the unique combination that
guarantees that the three rectangles match nicely as in the ﬁgure (1). We
cut the geodesic pantsP along the three blue orthogeodesics and get two
right-angled hexagons. Since by hypothesis the three red sides have length
>ε/2, one sees easily that the central triangle has diameter bounded by
some constantC′ depending only onε, and hence every leaf in each of the
three rectangles is shorter than someC′′ that also depends only onε (2).
for all 1⩽i,j ⩽ 3. Leta1,a 2,a 3 be the lengths of the boundaries ofP. We
consider the pointQ = [a1,a 2,a 3] in the triangle of Figure 8.9, pick the three
orthogeodesicsgij isotopic to the three curves indicated in the sub-triangle of
Figure 8.9 containingQ, and thicken eachgij to a metricR-neighbourhood
of gij, whereR is the linear combination ofa1,a 2,a 3 indicated in Figure 8.9.
TheR-neighbourhood is naturally foliated into (non-geodesic) arcs staying at
ﬁxed distance fromgij and the foliated neighbourhoods cover nicely much of
the pair of pantsP, as shown in Figure 8.15-(1). Every foliated rectangle is
equipped with a natural transverse measure induced by the orthogonal distance
between leaves.
The partial foliations of all the pairs of pants ofSg glue to a singular
measured foliation forSg, which straightens as prescribed in Section 8.3.12 to
a measured geodesic laminationq(m).
Letµ =γ1⊔... ⊔γ3g−3 be our original pants decomposition.
Proposition 8.3.24. The mapq restricts to a homeomorphism
q : Teich(Sg)−→
{
λ∈ ML
⏐⏐i(λ,γi )> 0∀i
}
.
Proof. Compare the coordinates (li,θi ) for Teich(Sg) and (ai,bi,ci ) for
ML. The map q sends (li,θi ) to (li,bi,ci ) for some (bi,ci ) that depends
homeomorphically onθi∈ R for eachi. Note thatai =i(λ,γi ). □
8.3.16. The fundamental lemma.We now show that the projectionq
distorts very little the lengths of the simple closed curves, as long as we put
256 8. SURFACE DIFFEOMORPHISMS
a lower bound on the lengths of the curvesγ1,...γ 3g−3 of the ﬁxed pants
decompositionµ. This technical fact is called the Fundamental Lemma [19].
For every ε > 0, we deﬁneV (ε) ⊂ Teich(Sg) to be the open subset
consisting of all metricsm such thati(m,γi )>ε for alli.
Lemma 8.3.25. For every simple closed curveα∈ S there exists a con-
stantC >0 such that, for allm∈V (ε), we have
i(q(m),α )⩽i(m,α )⩽i(q(m),α ) +C.
Proof. We representq(m) as a singular partial foliation, without straight-
ening it. The transverse measure of q(m) is just the length of orthogonal
geodesics, hence theq(m)-measure of any piecewise-transverse closed curve
is smaller or equal than its length: this proves thati(q(m),α )⩽i(m,α ).
We prove the other inequality. Ifα =γi theni(m,α ) =i(q(m),α ), so we
suppose thati(α,µ )> 0. Up to isotopy we may takeα to be monotonically
transverse toq(m), recall the proof of Proposition 8.3.20. The curveα inter-
sects each pair of pantsP into some essential arcsβ that cross each foliated
rectangle monotonically.
We can easily homotope each of these arcsβ⊂α∩P with ﬁxed endpoints
into a (not necessarily simple!) piecewise smooth arc that decomposes into
ﬁnitely many sub-arcs, that are alternatively contained either in a component
of ∂P or in a leaf of some foliated rectangle. Each sub-arc in a component
of ∂P may make many full turns (and hence may not be injective). Each of
the three rectangles contains at most one leaf that is a sub-arc ofβ. We
arrange the homotopy eﬃciently so that the newβ has the same transverse
q(m)-measure as before.
The transverseq(m)-measure ofβ on the sub-arcs in∂P is equal to its
length, whereas on the leaf sub-arcs it is zero. Therefore them-length ofβ is
equal to its measure plus the length of at most 3 leaves of some rectangles in
P. Figure 8.15-(2) shows that each such leaf is shorter than some constant
C′′ that depends only onε.
Note thatα is decomposed intoi(α,µ ) arcs likeβ. By homotoping each
β as above we ﬁnd a homotopic representative forα whose length is at most
the q(m)-measure ofα plus C = 3i(α,µ )C′′. The length of any homotopic
representative is greater or equal than the lengthi(m,α ) of the geodesic one,
and this proves the second inequality. □
Corollary8.3.26. Letmi∈V (ε)beadivergingsequencein Teich(Sg). The
sequence converges inTeich(Sg)⇐⇒the sequence[q(mi )]∈ PMLdoes, and
in this case they tend to the same limit.
Proof. Ifmi converges to some[α]∈ PML, we haveλimi→α for some
real numbers λi → 0. By the fundamental lemma, for every simple closed
8.3. LAMINATIONS 257
curveγ∈ S we get
⏐⏐i
(
λimi,γ
)
−i
(
λiq(mi ),γ
)⏐⏐→ 0.
Therefore λiq(mi ) converges (on a subsequence) to aβ ∈ ML such that
i(α,γ ) =i(β,γ ) for allγ∈ S. Exercise 8.3.21 givesβ =α.
The other implication is analogous. □
8.3.17. Atopologicalchart. Pickanarbitrary [λ]∈ PML =∂Teich(Sg).
We now construct an explicit neighbourhood of[λ] in Teich(Sg).
Letµ =γ1⊔... ⊔γ3g−3 be a pants decomposition such thati(γi,λ )> 0
for alli. We ﬁxε> 0 and deﬁne as aboveV (ε)⊂ Teich(Sg) as the set of all
the metricsm such thati(γi,m )>ε for alli. We deﬁne similarlyW⊂ PML
as the set of all[α] such thati(γi,α )> 0 for alli. We have[λ]∈W.
Proposition 8.3.27. We have
π(q(V (ε))) =π(q(Teich(Sg))) =W.
The setW∪V (ε) is an open neighbourhood of[λ] in Teich(Sg).
Proof. Proposition 8.3.24 implies the second equality, the ﬁrst holds be-
cause every [α]∈W is represented by anα withi(γi,α )>ε.
The setsW and V (ε) are open in PML and Teich(Sg) respectively. If
W∪V (ε) were not open inTeich(Sg), there would be a sequencemi⁄∈V (ε) of
metrics converging to some[α]∈W. On a subsequence we may suppose that
i(mi,γj )<ε for some ﬁxedj and thereforei(α,γi ) = 0, a contradiction. □
We have found an open neighbourhood of[λ] and we now want to deter-
mine its topology.
Proposition 8.3.28. There is a homeomorphism
φ:W∪V (ε)−→U
onto an open subsetU⊂H of a half-spaceH⊂ R6g−6, withφ(W ) =U∩∂H.
Proof. We complete the pants decompositionµ to a ﬁlling setµ′∈ C of
simple closed curves inSg, considered as a current. We know from Proposi-
tion 8.2.28 that the metricsm with i(m,µ′)⩽M form a compact subset in
Teich(Sg). We deﬁne the map
φ:W∪V (ε)−→W× [0, 1]
x↦−→
{ (x, 0) if x∈W,
(π(q(x)),e−i(q(x),µ′)) if x∈V (ε).
The mapφ is continuous: if a sequencemi ∈ V (ε) of metrics tends to
[α]∈ PML, theni(mi,µ′)→∞ , hencei(q(mi ),µ′)→∞ bythefundamental
lemma. Moreoverπ(q(mi ))→ [α] by Corollary 8.3.26. Summing up, we get
thatφ(mi )→ ([α], 0) =φ([α]).
