---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-045-112-knots-and-links
section_title: "Knots and links"
section_number: 11.2
pages: 353-360
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
a genus-g Heegaard splitting ofS3 obtained by stabilisingg times the genus-0
Heegaard splitting ofS3.
11.1.4. Triangulations. Smooth triangulations are somehow related to
Heegaard splittings, at least in one direction.
Every compact manifold admits a smooth triangulation (see Section 1.7.7)
and in dimension three we can luckily prove a converse statement, much as
we did in dimension two (in Section 6.1.5).
Let X be a three-dimensional pure simplicial complex, where: every face
is incident to two tetrahedra, every edge is contained in a cycle of adjacent
tetrahedra, and the link of every vertex is a sphere.
Proposition 11.1.6.The complexX is the smooth triangulation of a closed
three-manifoldM, unique up to diﬀeomorphism.
Proof. By dualisingX we get a handle decomposition: tetrahedra, trian-
gles, edges, and vertices determine 0-, 1-, 2-, and 3-handles. This procedure
constructs a smooth closed three-manifoldM triangulated byX. The way
handles are attached is determined up to isotopy, and henceS is determined
up to diﬀeomorphism. □
As we did with surfaces, it is worth noting that this procedure (getting
a unique smooth structure from a simplicial complex) does not work in all
dimensions (here we used implicitly the non-obvious Proposition 9.2.1).
Topologistsusuallyprefertoloosenthenotionof“triangulation” byallowing
self- and multiple adjacencies between tetrahedra, see Section 14.1.2. What is
important to note here is that, no matter what the deﬁnition of “triangulation”
is, a triangulated three-manifold always has a well-deﬁned smooth structure
determined only by the combinatorics of the triangulation. This shows that
smooth three-manifolds can be treated combinatorially, for instance by a com-
puter.
A relation between triangulations and Heegaard splittings is the following:
a smooth triangulation of a closed manifold witht tetrahedra gives rise to
a dual handle decomposition and hence to a Heegaard splitting of genust.
A fundamental diﬀerence between the two notions is that there is a bounded
numberofclosedthree-manifoldstriangulatedbyatmost t tetrahedraforevery
t, while there are inﬁnitely many manifolds with Heegaard genus at mostg for
everyg> 1.
11.2. Knots and links
Knots and links are fundamental and beautiful objects in geometric topol-
ogy. Knots and links inS3 have a combinatorial and mildly two-dimensional
nature because they can be treated as planar diagrams, but they should be
considered as intrinsically three-dimensional objects.
346 11. CONSTRUCTIONS OF THREE-MANIFOLDS
Figure 11.2. Every knot may be described via a planar diagram with
over/under crossings (left) and its tubular neighbourhood is a knotted
solid torus (right).
11.2.1. Deﬁnition.A link in a 3-manifoldM is a compact submanifold
of dimension one. Being compact, it consists of ﬁnitely many circles, and a
connected link is called aknot. Links and knots are usually considered up to
ambient isotopy.
Every link inS3 can be projected to a plane: if the link is generic with re-
spect to the projection, its image is adiagram as in Figure 11.2-(left). Every
link inS3 can be described via a diagram and can be thus treated combina-
torially, but it is important to note that the same link can be represented via
inﬁnitely many diagrams and it is hard in general to tell whether two given
diagrams represent the same link. Thetrivial knot(or unknot)K⊂S3 is the
one that has a planar diagram without crossings.
11.2.2. Chirality. The mirror image of a knot or link is obtained by re-
ﬂecting it with respect to any plane inS3. On a diagram, this operation is
realised simply by inverting all crossings simultaneously.
A knot ischiral if it is not isotopic to its mirror image, andachiral oth-
erwise. For instance, the trivial knot is achiral, but the trefoil knot (shown in
Figure 11.2) is chiral. As in the rest of this book, we mostly ignore orientation
issues and often consider implicitly two mirrored knots or links as equivalent.
11.2.3. Link complement. The tubular neighbourhood of a linkL in an
orientableM consists of solid tori by Proposition 1.1.13, and thelink comple-
ment ofL is the three-manifold with boundary obtained fromM by removing
the interiors of these solid tori. IfM is compact, the link complement also is.
Proposition 11.2.1. Let K⊂S3 be a knot. The complement ofK is an
irreducible manifold. Moreover, the following facts are equivalent:
(1) K is trivial,
(2) K bounds a disc inS3,
(3) the complement ofK is a solid torus.
11.2. KNOTS AND LINKS 347
Figure 11.3. Connected sum of knots: put two knots in disjoint balls
and connect them with a band as shown.
Proof. The complement ofK is irreducible by Proposition 9.2.15. The
implication (1)⇒(2) is the smooth Jordan curve theorem, and (2)⇒(1) holds
because all discs in a connected three-manifold are isotopic.
A trivial knot thickens to a standardly embedded solid torus, whose com-
plement is a solid torus: hence (1)⇒(3). Conversely, if the complement ofK
is a solid torus thenS3 decomposes into two solid tori asS3 =L(1,q ). The
meridian of the complement solid torus extends to a disc with boundaryK,
hence (3)⇒(2). □
Corollary 11.2.2.All Heegaard tori forS3 are isotopic
Proof. A Heegaard torusT⊂S3 is by deﬁnition a torus that decomposes
S3 into two solid tori. By the proposition the core of one of these solid tori is
alwaysisotopictoatrivialknotandhence T isisotopictoastandardtorus. □
A link complement inS3 can be reducible: this holds precisely when there
is a sphereΣ⊂ S3 disjoint from the linkL that cutS3 into two balls, each
containing some components ofL. In that case we say that the link issplit.
Corollary 11.2.3. Let L⊂S3 be a non-trivial knot or non-split link. The
link complement is Haken.
Proof. Thelinkcomplement M isirreduciblebyassumption; byProposition
9.2.30, ifM contains an essential disc then it is a solid torus and henceL is
the trivial knot, which is excluded. NowM is Haken by Corollary 9.4.5. □
11.2.4. Prime knots. There is an operation on knots inS3 called con-
nected sum, similar to the one on manifolds and described in Figure 11.3. A
connected sum istrivial if one of the two knots is trivial; a non-trivial knot
is prime if it is not the result of a non-trivial connected sum, andcomposite
otherwise.
The crossing number of a knot is the minimum number of crossings in
a diagram describing it. Prime knots with small crossing number have been
tabulated since the XIX century: at present all the prime knots with up to
16 crossing have been classiﬁed (by Hoste – Thistlethwaite – Weeks [29] in
1998) and the ﬁrst 14 numbers of them are listed in Table 11.1. The prime
knots with⩽ 7 crossings are shown in Figure 11.4: the ﬁrst three in the list
are the unknot, thetrefoil, and theﬁgure-eight knot.
348 11. CONSTRUCTIONS OF THREE-MANIFOLDS
c 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
n 1 0 0 1 1 2 3 7 21 49 165 552 2176 9988 46972
Table 11.1. The numbern of prime knots withc crossings, for allc⩽ 14.
Figure 11.4. Prime knots inS3 with at most7 crossings. The knots31
and 41 are thetrefoil and theﬁgure-eightknots respectively.
Figure 11.5. A connected sum produces a sphere (dotted in the ﬁgure)
intersecting the knot in two points.
A connected sum gives rise to a sphere which intersects the new knot in
two points, see Figure 11.5. The sphere intersects the knot complement into
an essential annulus.
11.2.5. Torus knots. We now introduce a simple and natural family of
prime knots. Consider the standardly embedded torusT⊂S3 with meridian
m and longitudel oriented as in Figure 11.6. A pair(p,q ) of coprime integers
11.2. KNOTS AND LINKS 349
Figure 11.6. The meridianm (red) and longitudel (blue) of a standard
torus are oriented as shown here, like a right-hand screw.
Figure 11.7. The torus knot(2,−7) and the torus link(2,−8).
determines a simple closed curve inT that is homologically qm +pl, and
such a curve is called a(p,q )-torus knot. More generally, a pair of integers
(a,b ) determines a multicurve inT that is homologicallybm +al, called an
(a,b )-torus link.
For instance, the trefoil knot is a(2,−3)-torus knot. More examples are
in Figure 11.7. The knots31, 51, and 71 from Figure 11.4 are torus knots.
Exercise 11.2.4. If|p|⩽ 1 or|q|⩽ 1 the torus knot is the unknot. The
torusknotswithparameters (p,q ), (−p,−q), and(q,p )areisotopic, thetorus
knot with parameters(p,−q) is the mirror image of(p,q ).
The complement of a torus knot is a quite simple kind of Seifert manifold.
In the following we suppose thatp,q > 1 are coprime.
Proposition 11.2.5. The complement of a (p,q )-torus knot is a Seifert
manifold ﬁbering over the orbifold(D,p,q ). More precisely, it is
(
D, (p,r ), (q,s )
)
where (r,s ) is any pair such thatps +qr = 1.
Proof. LetK⊂T⊂S3 be the (p,q )-torus knot. The pair(r,−s) deter-
mines another simple closed curveα⊂T that intersectsK in one point. The
350 11. CONSTRUCTIONS OF THREE-MANIFOLDS
Figure 11.8. The Hopf link is the(2, 2)-torus link.
complement ofK in a tubular neighbourhoodT×[−1, 1] ofT is diﬀeomorphic
toP×S1, whereP is a pair of pants. On the toriT×{− 1} and T× 1 the
curves∂P×{ pt} and{pt}× S1 are isotopic toα andK.
The complement of T× [−1, 1] in S3 consists of two solid tori, with
meridians (1, 0) and (0, 1). Read in the basis(α,K ) the meridians are(q,s )
and (p,r ). The complement of K in S3 is obtained fromP×S1 by ﬁlling
these curves and hence we get
(
D, (p,r ), (q,s )
)
. □
In particular the complement of the trefoil knot is
(
D, (2, 1), (3, 1)
)
. If we
suppose p,q > 2, two torus knots with distinct (unordered) parameters have
non-diﬀeomorphic complements and hence are not isotopic. Our intuition says
that a torus knot is prime, and we can prove this rigorously.
Proposition 11.2.6. Every torus knot is prime.
Proof. IfK is obtained as a non-trivial connected sum, there is an essential
annulus in the complement, whose boundary curves are meridians ofK. There
is only one essential annulus in
(
D, (p,r ), (q,s )
)
and its boundary curves are
not meridians. □
The (2, 2)-torus link is called theHopf linkand is drawn in Figure 11.8.
Exercise 11.2.7. The complement of the Hopf link isT× [0, 1]. Any two
distinct ﬁbres of the Hopf ﬁbration form a Hopf link.
11.2.6. Satellite knots. We have discovered that che composite knots
contain essential annuli in their complement, and we now look for essential
tori. It is convenient to introduce the following deﬁnition.
Deﬁnition 11.2.8. A knotK⊂S3 is asatellite if its complement contains
an essential torus.
We now formulate an equivalent and more inspiring deﬁnition of satellite
knots which justiﬁes the terminology. A knot in a solid torusD2×S1 is local if
it is contained in a ball, and acore if it is isotopic to{x}×S1. An embedding
ϕ:D2×S1 ↪→S3 is trivial (or unknotted) if the image of a core is a trivial
knot.
11.2. KNOTS AND LINKS 351
Figure 11.9. Two satellite knots.
Proposition 11.2.9. A knot K ⊂ S3 is satellite⇐⇒ it is the image of
a knotK′⊂ D2×S1 which is neither local nor a core, along a non-trivial
embeddingϕ:D2×S1↪→S3.
Proof. A knotK =ϕ(K′) constructed in this way is satellite, because the
torusϕ(S1×S1) is essential in the complement ofK: it is incompressible (on
one side becauseϕ is non-trivial, and on the other becauseK′ is not local)
and not∂-parallel (becauseK′ is not a core).
Conversely, ifK is a satellite knot then its complement contains an essen-
tial torusT ⊂ S3. As every torus inS3, the torusT bounds a solid torus.
SinceT is essential, the knotK is contained in this solid torus in a non-local
and non-core way. Moreover the solid torus is knotted, otherwiseT would be
compressible on the other side. □
The non-trivial embeddingϕ sends the core curve ofD2×S1 to some
non-trivial knotH⊂S3 called thecompanion ofK: we should think ofK as
orbiting as a “satellite” around its companionH, with orbit pathK′. WhenK′
is contained in the boundary of the solid torusD2×S1 the satellite knotK is
called acable knot. Some examples are shown in Figure 11.9.
11.2.7. Simple complements. Recall from Section 9.4.7 that a compact
three-manifold is simple if it contains no essential sphere, disc, torus, and
annulus. Which knots have a simple complement? To answer to this question,
weneedagenerallemmaonthree-manifoldsthatidentiﬁesthefewcaseswhere
there are essential annuli without essential tori.
Lemma 11.2.10. Let M be irreducible and∂-irreducible, with boundary
consisting of tori. The manifold M contains no essential tori but contains
some essential annuli⇐⇒it is diﬀeomorphic to one of the following:
(
D, (p1,q 1), (p2,q 2)
)
,
(
A, (p,q )
)
, P ×S1
withp1,p 2> 2. HereP is a pair of pants.
352 11. CONSTRUCTIONS OF THREE-MANIFOLDS
Proof. Propositions 10.4.9 and 10.4.11 imply that the Seifert manifolds
listed contain vertical essential annuli, but not essential tori.
Conversely, letM containanessentialannulus A. Supposethat Aconnects
two distinct boundary toriT,T ′ ofM. A regular neighbourhood ofT∪T′∪A
is diﬀeomorphic toP×S1, and its boundary contains a third torusT′′⊂M.
Since T′′ cannot be essential, it is either boundary parallel or bounds a solid
torus inM, andM is diﬀeomorphic respectively toP×S1 or a Dehn ﬁlling
of it. In the latter case, the Dehn ﬁlling is not ﬁbre-parallel becauseM is
∂-reducible (use Corollary 10.3.43), hence we get a Seifert manifold of type(
A, (p,q )
)
.
IfA connects one boundary component to itself we conclude similarly and
may also getM =
(
D, (p1,q 1), (p2,q 2)
)
. □
We can now state and prove an important trichotomy on knots.
Proposition 11.2.11.Every knotK⊂S3 is either a torus knot, a satellite
knot, or has a simple complement.
Proof. We only need to prove that if the complementM contains an
essential annulus and no essential tori thenK is a torus knot. The previous
lemma givesM =
(
D, (p1,q 1), (p2,q 2)
)
, and to getS3 back we must have a
Dehn ﬁllingS3 =
(
S2, (p1,q 1), (p2,q 2), (1,n )
)
. In particularK is isotopic to
a ﬁbre and hence contained in a vertical Heegaard torus forS3. Heegaard tori
are standard by Corollary 11.2.2, and henceK is a torus knot. □
The relevance of this proposition will be magniﬁed later, after introducing
geometrisation. Note that in particular all the composite knots are satellite
knots: where is the essential torus?
