---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-037-92-prime-decomposition
section_title: "Prime decomposition"
section_number: 9.2
pages: 280-295
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
In this section we study spheres and discs in three-manifolds. We prove
that every sphere inR3 bounds a disc, and we callirreducible a three-manifold
that has this property. Then we study the connected sum of three-manifolds,
and we show that it behaves like multiplication of natural numbers: every
closed oriented three-manifold decomposes uniquely into someprime factors.
9.2.1. Balls. In general dimensionn, we have used the termdisc to de-
note the closed Euclidean discDn, and the termball for its open interior.
Speaking about three-dimensional spaces, we will henceforth use a more intu-
itive terminology and calldisc and ball respectively the closed discsD2 and
D3, and we will use the symbolsD andB for them.
LetM be a connected 3-manifold. Theorem 1.1.14 says that all the closed
balls B⊂ int(M) in M are isotopic and hence the removal of the interior of
B fromM produces a new manifoldN with boundary, which does not depend
onB. The sphere∂B is a new boundary component ofN.
9.2. PRIME DECOMPOSITION 273
The inverse operation consists ofcapping oﬀa boundary component of
N diﬀeomorphic toS2 by attaching a ballB to it, via some diﬀeomorphism.
This operation depends only on the boundary component that is capped oﬀ.
Proposition 9.2.1. The manifold M obtained by capping oﬀ a spherical
boundary component ofN does not depend on the diﬀeomorphism chosen.
Proof. There are only two diﬀeomorphisms up to isotopy, see Theorem
6.4.5, and they are related by a reﬂection ofB, so they produce diﬀeomorphic
manifolds. □
In dimension 3 we can therefore freely remove and add balls without aﬀect-
ing much the topology of the manifold. In particular, by removing the interior
of a ball fromS3 we get another ballB, and by attaching a ball toB we get
S3 back. We must thank Smale’s Theorem 6.4.1 for that: the situation in
higher dimensions is more complicated.
9.2.2. Connected sums. Connected sums exist in any dimensionn, but
whenn⩽ 3 they may be redeﬁned in slightly simpler terms:
Deﬁnition 9.2.2. Theconnected sumM =M1#M2 of two oriented con-
nected 3-manifolds M1, M2 is constructed by removing the interiors of two
closed balls fromM1 and M2, and then gluing the two resulting spheres via
any orientation-reversing diﬀeomorphism.
In dimensionn⩽ 3 these diﬀeomorphisms are all isotopic, see Theorem
6.4.5, hence this is a good deﬁnition (in arbitrary dimension we require the
diﬀeomorphismtoextendtotheremoveddiscs). Weusuallyworkwithoriented
3-manifolds to have a uniquely deﬁned connected sum, but in some cases
this is not necessary. An orientable manifoldM is mirrorable if it admits an
orientation-reversing self-diﬀeomorphism.
Exercise 9.2.3. IfM1 is mirrorable, the manifoldM = M1#M2 does not
depend (up to diﬀeomorphisms) on the orientations ofM1 andM2.
If bothM1 and M2 are oriented and not mirrorable, it may happen that
M1#M2 andM1#M2 are not diﬀeomorphic (hereM2 isM2 with the reverse
orientation). There is also a boundary-version of connected sum:
Deﬁnition 9.2.4. The∂-connected sum M = M1#∂M2 of two oriented
3-manifolds with boundary is constructed by gluing two discsD1⊂∂M1 and
D2⊂∂M2 via an orientation-reversing diﬀeomorphism.
The operation depends only on the components of∂M1,∂M 2 containing
D1,D 2, because of Theorem 1.1.14. The following holds:
M#S3 =M, M #∂B =M, ∂ (M1#∂M2) = (∂M1)#(∂M2).
In the latter equality we suppose that∂M1 and∂M2 are connected.
274 9. TOPOLOGY OF THREE-MANIFOLDS
Figure 9.1. Non-degenerate points of index 0, 1, and 2.
Figure 9.2. The height function on this torus is a Morse function. It
has four critical points of index (from bottom to top) 0, 1, 1, 2.
Exercise 9.2.5. LetM =M1#M2 orM =M1#∂M2. We have
π1(M) =π1(M1)∗π2(M2).
Hint. Use Van Kampen. □
Corollary 9.2.6.We haveH1(M, Z) =H1(M1, Z)⊕H1(M2, Z).
9.2.3. Irreducible 3-manifolds. We introduce an important deﬁnition.
LetM be a connected, oriented 3-manifold with (possibly empty) boundary.
Deﬁnition 9.2.7. The manifoldM is irreducible if every sphereS⊂ int(M)
bounds a ball.
It is important to recall here that the sphere must be a smooth surface.
If we admitted also topological spheres, no 3-manifold would be irreducible:
there are “wild” topological spheres inside every ball, as shown in Figure 1.1.
9.2.4. Alexander theorem. The ﬁrst 3-manifold to look at is of course
R3. We prove here thatR3 is irreducible.
We need some Morse theory. Let S ⊂ R3 be a closed surface and
f (x,y,z ) = z be the height function. The functionf is a Morse function
for S if f|S has ﬁnitely many critical points, and at each critical point the
Hessian off|S is non-singular (the Hessian is read on a chart forS, but this
deﬁnition is chart-independent). The critical point is a local minimum, a sad-
dle, or a local maximum, according to the signature of the Hessian, see Figure
9.1. These critical points haveindex 0, 1, and 2, respectively.
9.2. PRIME DECOMPOSITION 275
P P
Figure 9.3. The planeP intersects S into circles. Starting from the
innermost ones, we cutS along the circles and cap them oﬀ by adding
pairs of discs. The resulting surface does not intersectP anymore.
Figure 9.4. After capping oﬀ at eachui we end up with many spheres
of these basic types, which clearly bound balls.
Exercise 9.2.8. A critical pointp forf|S is non-degenerate if and only ifp
is a regular (i.e. non-critical) point for the Gauss mapS→S2.
Lemma 9.2.9. Let S⊂ R3 be a closed surface. After rotatingS of an
arbitrarily small angle, the height functionf is a Morse function forS.
Proof. Consider the Gauss mapψ : S→ S2. By Sard lemma there are
regular values arbitrarily close tov = (0, 0, 1). RotateS so thatv is a regular
value. Now ψ−1(v ) is the set of critical points forf and they are all non-
degenerate. □
We are now ready to prove the following.
Theorem 9.2.10 (Alexander’s Theorem).The space R3 is irreducible.
Proof. LetS⊂ R3 be a 2-sphere. Up to a small rotation we suppose that
the height functionf|S is a Morse function, and after a further small rotation
we may suppose that thek critical points off|S stay at distinct heightsz1<
...<z k. Pick a regular valueui∈ (zi,zi+1) for everyi = 1,...,k − 1. The
horizontal planeP at heightui intersectsS transversely into circles. Starting
from the innermost ones, we cutS along these circles and cap them oﬀ by
adding pairs of discs as in Figure 9.3. The resulting surface is disjoint fromP.
276 9. TOPOLOGY OF THREE-MANIFOLDS
S
a
N
Figure 9.5. IfS⊂M is non-separating, there is a simple closed curveα
intersecting S transversely in one point: hereS is drawn as a disc whose
boundary should be collapsed to a point, andα is a line whose endpoints
should be identiﬁed (left). Pick two tubular neighbourhoods ofS and α
and consider their unionN (right).
At every cut a sphere decomposes into two spheres. If we do this for every
i = 1,...,k − 1 we end up with many spheres of the types shown in Figure
9.4, that clearly bound balls inR3.
Now we reverse the process and undo all the cuts: we prove inductively
that at each backward step we have a set of spheres bounding balls (note that
the balls are not disjoint!). At each backward step we replace two spheres
S1,S 2 bounding ballsB1,B 2 with one sphereS. Isotope S1 and S2, so that
they intersect in a discD. If the interiors ofB1 and B2 are disjoint, thenS
bounds the ballB1∪B2. If they are not disjoint, then one is contained in the
other, sayB1⊂B2 andS bounds the ballB2\ int(B1). □
Corollary 9.2.11. Every sphere contained in a sub-ballB ⊂ M of a 3-
manifoldM bounds a ballB′⊂B.
Corollary 9.2.12.Every sphere inS3 bounds a ball on both sides.
Proof. Choose two pointsp,q ⁄∈ S on opposite sides with respect toS.
We haveS3\p =S3\q = R3 hence S is contained inR3 in two ways and
bounds a ball in each. □
Alexander’s Theorem generalises the smooth Jordan curve Theorem to
dimension 3. The situation in higher dimensions is much more problematic: it
is still unknown whether every smooth 3-sphere inR4 bounds a smooth 4-disc
(this is usually called theSchönﬂies problem).
9.2.5. Prime manifolds. A connected sumM1#M2 is trivial if eitherM1
orM2 is a sphere.
Deﬁnition 9.2.13. A connected, oriented 3-manifoldM is prime if every
connected sumM =M1#M2 is trivial.
Being prime is equivalent to be irreducible, with a single exception.
Proposition 9.2.14. Every oriented 3-manifoldM⁄= S2×S1 is prime if
and only if it is irreducible.
9.2. PRIME DECOMPOSITION 277
Proof. The inverse operation of a connected sumM =M1#M2 consists
of cutting along a separating sphereS⊂ M and then capping oﬀ the two
resulting manifoldsN1,N 2 with balls. The cappedNi isS3 if and only ifNi is
a ball. Therefore the connected sum is trivial if and only ifS bounds a ball on
one side. ThereforeM is prime if and only if every separating sphereS⊂M
bounds a ball.
IfM is irreducible, then it is clearly prime. IfM is prime and not irreducible,
there is a non-separating sphereS⊂M. There is a simple closed curveα⊂M
intersectingS transverselyinonepointasinFigure9.5-(left). Picktwotubular
neighbourhoods ofS andα as in Figure 9.5-(right): their union is a manifold
N with a boundary sphere∂N = S′. The sphere S′ is separating andM is
prime, henceS′ bounds a ballB on the other side andM =N∪B.
We now prove thatM =S2×S1. We embedS∪α naturally inS2×S1
as S =S2×y and α =x×S1. Decompose S2 =D∪D′ in two discs and
S1 =I∪I′ in two intervals. The manifoldN also embeds asS2×I∪D×S1
and its complementB =D′×I′ is a ball. ThereforeM =S2×S1. □
9.2.6. Some irreducible manifolds. The Alexander theorem generates
many more examples of irreducible 3-manifolds.
Proposition9.2.15. Everycompactthree-dimensionalsubmanifold M⊂S3
with connected boundary is irreducible.
Proof. Every sphereS⊂ M bounds two balls inS3. Since ∂M is con-
nected, it is contained in one of them, so the other is contained inM. □
We turn to coverings.
Proposition 9.2.16. Let p :M→N be a covering of 3-manifolds. IfM is
irreducible thenN also is.
Proof. A sphereS⊂N lifts to many spheres inM, each bounding at least
one ball. Pick an innermost such ballB. We prove thatp(B) is a ball with
boundaryS and we are done.
To do this, note thatp|∂B is a diﬀeomorphism ontoS and p(int(B)) is
disjoint fromS since B is innermost. This implies thatp|B :B→ p(B) is a
covering and since it has degree one onS it is a diﬀeomorphism. □
Corollary 9.2.17.Elliptic, ﬂat, hyperbolic 3-manifolds are irreducible.
Proof. Their universal covering is diﬀeomorphic toS3 or R3. □
Finally, we consider the exceptionS2×S1. It is not irreducible since it
contains a non-separating sphere, but it is prime.
Proposition 9.2.18. The manifoldS2×S1 is prime.
278 9. TOPOLOGY OF THREE-MANIFOLDS
Figure 9.6. A handlebody of genus3.
Proof. Let S ⊂ S2×S1 be a separating sphere: we must prove that
it bounds a ball. It separatesS2×S1 into two manifoldsM and N, and on
fundamental groups we getZ =π1(M)∗π1(N). This implies easily that either
π1(M) orπ1(N) must be trivial: suppose the ﬁrst.
Since M is simply connected, a copyM′ of M lifts to the universal cover
S2× R of S2×S1. We identifyS2× R = R3\ 0. This copyM′ now lies in
R3, and∂M′ =S2 implies thatM′ is a ball by Alexander theorem. □
9.2.7. Handlebodies and line bundles.We now introduce some basic,
but important, compact 3-manifolds with boundary. Ahandlebody is a con-
nected orientable 3-manifold that decomposes into 0- and 1- handles.
Proposition 9.2.19. The boundary of a handlebody isSg for someg> 0.
Two handlebodies are diﬀeomorphic if and only if they have the sameg.
Proof. By simplifying handles we may decompose the handlebody into one
0-handle and someg 1-handles, so that the boundary is a genus-g surface, see
Figure 9.6. Each 1-handle is attached along a pair of discs; the orientability
assumption together with Theorem 1.1.14 easily imply that the result of at-
taching a 1-handle depends on nothing and the handlebody depends only ong
up to diﬀeomorphisms. □
The genus of a handlebodyHg is the genusg of its boundary surface.
Proposition 9.2.15 implies the following.
Corollary 9.2.20.Handlebodies are irreducible.
Some other simple manifolds are irreducible.
Proposition 9.2.21. Ifg> 1 thenSg× [0, 1] is irreducible.
Proof. Its universal coverR2× [0, 1] is irreducible, because its interior is
diﬀeomorphic toR3. □
Exercise 9.2.22. Ifb> 1 the manifoldSg,b× [0, 1] is homeomorphic to a
handlebody of genus2g +b− 1 =−χ(Sg,b) + 1.
9.2. PRIME DECOMPOSITION 279
Figure 9.7. A normal surface intersects every tetrahedron in triangles or squares.
D
S S'
Figure 9.8. We cansurger a surfaceS along a discD with∂D =D∩S.
The operation consists of removing an annular tubular neighbourhood of
∂D inS and adding two parallel copies ofD. We get a new surfaceS′.
9.2.8. Normal surfaces. Let M be a compact 3-manifold with (possibly
empty) boundary. As every smooth compact manifold,M has a triangulation
T, made of a certain numbert of tetrahedra. We now show thatT can be
used to treat combinatorially many interesting surfaces inM.
A properly embedded surfaceS⊂M is transverse toT if it is transverse
to all its simplexes. In particularS does not intersect the vertices ofT, and it
intersects every edge, face, and tetrahedron respectively into a ﬁnite number
of points, curves, and surfaces. Every properly embedded surfaceS⊂M can
be perturbed to be transverse toT.
Deﬁnition 9.2.23. Anormal surface is a properly embedded surface S
transverse toT that intersects every tetrahedron into triangles or squares as
in Figure 9.7.
Example 9.2.24. For every vertexv of T lying in int(M) we may take a
small sphere centred atv that intersects every incident tetrahedron in a small
triangle: we get a normal sphere. Ifv lies in∂M we get similarly a normal
disc. A surface of this type is calledvertex-linking. Vertex-linking spheres are
not very interesting since they bound balls.
Exercise 9.2.25. A connected normal surface is vertex-linking if and only
if it consists of triangles only (no squares).
LetS⊂M be a properly embedded, possibly disconnected, compact sur-
face. Anelementary transformationonS is one of the following moves:
• the removal of a connected component ofS contained in some ball;
280 9. TOPOLOGY OF THREE-MANIFOLDS
D
S
S'a
b
∂M ∂M
Figure 9.9. We can also surger a surfaceS along a discD touching the
boundary in a segment. The result is a new properly embedded surfaceS′.
Figure 9.10. Starting from the innermost curves in∂∆∩S we surger
along discs so thatS∩ ∆ consists only of discs and closed components,
which we then remove.
Figure 9.11. The closed curves contained in a triangle are the inter-
sections of small spherical components ofS with that triangle. We just
remove them.
• letD⊂ int(M) be a disc with∂D =D∩S: wesurger S alongD as
shown in Figure 9.8;
• letD⊂M be a disc withD∩ (S∪∂M ) = ∂D =α∪β, whereα is
an arc inS andβ an arc in∂M as in Figure 9.9-(left): wesurger S
as shown in the ﬁgure.
Every elementary transformation is local,i.e. it takes place in a ball. It trans-
formsS into a new surfaceS′. We ﬁx a triangulationT forM.
Proposition 9.2.26. Every properly embedded surfaceS ⊂ M becomes
normal after ﬁnitely many isotopies and elementary transformations.
9.2. PRIME DECOMPOSITION 281
Figure 9.12. If the boundary of a (yellow) discD intersects an edgee
of∂∆ twice, we pick two innermost intersections, that must be in opposite
directions. There must be a red disc as shown here (exercise: use Alexan-
der’s theorem), which can be used to pushS in the direction indicated by
the arrow. The resulting surface is shown in the right. Ife⊂ ∂M, we
cannot pushS outside∂M: instead, we surger along the red disc.
Proof. PutS transverse toT. It intersects every tetrahedron∆ into sur-
faces as in Figure 9.10-(left). The intersection S∩∂∆ consists of closed
curves: the innermost ones bound discs in∂∆, which may be pushed a bit
inside ∆ and then used to surgerS. We do this with all curves (starting with
the innermost ones) to transformS as in Figure 9.10, so that at the end
S∩ ∆ consists only of discs and closed surfaces. Then we remove the closed
surfaces: this is an elementary transformation since∆ is a ball. We do this for
every tetrahedron ∆.
Now S intersects every tetrahedron ∆ in discs. Consider the boundary
curve of one such disc: if it is contained in a face as in Figure 9.11-(left), it
belongs to one or two discs (depending on whether the face belongs to∂M or
not), which form a component ofS contained in a ball that can be removed.
Suppose the boundary curve crosses twice an edge of∆: if the edge lies
in the interior ofM, we isotopeS as shown in Figure 9.12 to decrease the
number of intersections ofS with the 1-skeleton ofT; if the edge lies in∂M
we simplify analogously by surgerying along the red disc shown in the ﬁgure.
In all cases then we go back to the ﬁrst step of the algorithm.
After ﬁnitely many steps we get a surfaceS intersecting every tetrahedron
∆ in discs, whose boundary curves intersect every edge of∆ at most once.
One such disc is either a triangle or a square. □
9.2.9. Interesting surfaces cannot have too many components.We
know from Proposition 9.1.7 that a compact orientableM cannot contain too
many disjoint non-orientable surfaces. It can however contain arbitrarily many
orientable surfaces: for instance, small surfaces contained in disjoint balls. A
crucial aspect of 3-manifolds theory is thatM cannot contain arbitrarily many
“interesting” surfaces, as we now see.
282 9. TOPOLOGY OF THREE-MANIFOLDS
Figure 9.13. If we cut a tetrahedron∆ along triangles and squares we
get arbitrarily many prisms with triangular or quadrilateral basis, and at
most 6 other pieces (here we get4 pyramids and two esahedra).
Two disjoint connected diﬀeomorphic surfacesΣ, Σ′⊂ M are parallel if
they cobound a region diﬀeomorphic toΣ× [0, 1] with Σ = Σ× 0 and Σ′ =
Σ× 1. Two parallel surfaces are obviously isotopic.
LetT be a triangulation of a compactM with (possibly empty) boundary.
Lett be the number of tetrahedra inT and setb2 = dimH2(M,∂M, Z2).
Lemma 9.2.27. Let S be an orientable normal surface. If S has more
than 10t +b2 components, then two componentsΣ, Σ′ ofS are parallel and
cobound a Σ× [0, 1] which is disjoint from the other components.
Proof. The complementM\S intersects every tetrahedron∆ into poly-
hedra: there are many prisms lying between parallel triangles or squares, and
at most 6 other pieces, see Figure 9.13. These at most 6 pieces are adjacent
to at most 1+1+1+1+3+3 = 10 triangles and squares.
This implies that, except at most10t of them, the components ofS are
only adjacent (on both sides) to prisms. These prisms glue to formI-bundles.
Therefore at leastb2 + 1 components ofS are adjacent toI-bundles on both
sides. The twistedI-bundles are at mostb2 by Proposition 9.1.7, and each
is adjacent to one surface. Therefore at least one surface is adjacent to a
productI-bundle Σ× [0, 1]. □
We get a topological corollary. Aball with holesis a 3-manifold obtained
by removing somek> 0 disjoint small open balls from a ball. Asphere system
for a 3-manifoldM is a surfaceS⊂ int(M) consisting of disjoint spheres, such
that no component ofM\S is a ball with holes disjoint from∂M. (Balls with
holes adjacent to spherical components of∂M are allowed.)
Corollary 9.2.28.LetM be a compact orientable 3-manifold that does not
contain any non-separating sphere. There is aK >0 such that every sphere
system inM contains less thanK spheres.
9.2. PRIME DECOMPOSITION 283
B
N1
N2
Figure 9.14. A reducing set of spheres (red) forM =M1#M2#(S2×
S1). HereB is a ball with four holes andNi isMi with one hole.
Proof. Pick a triangulationT of M with some t tetrahedra: we prove
that K = 10t +b2 + 1 works, withb2 = dim H2(M,∂M ; Z2). Suppose by
contradiction that there is a sphere systemS with>K spheres. Via isotopies
and elementary transformations we transformS into a normal surfaceS′.
We now examine the eﬀect of elementary transformations in detail. No
component of S is contained in a ball, otherwise by Alexander theorem an
innermost component ofM\S would be a ball. Therefore an elementary
transformation cannot cancel a component ofS.
A surgery along a disc splits a sphereS0 into two spheresS1,S 2. We now
prove that by substitutingS0 with eitherS1 orS2 we still get a sphere system.
If we pushS1 and S2 away fromS0 the surfacesS0,S 1,S 2 altogether bound
a ball with two holesB.
By our hypothesis onM the spheresS0,S 1, andS2 are separating. Let
Ni be the component ofM\ (S0∪S1∪S2) adjacent toSi distinct fromB,
for i = 0, 1, 2. If both N1,N 2 are balls with holes disjoint from∂M, then
N1∪N2∪B also is, which is excluded. Therefore one, sayN1, is not a ball
with holes disjoint from∂M. On the other side, ifN2∪B∪N0 were a ball
with holes disjoint from∂M, thenN0 would also be (by Alexander’s theorem),
which is excluded. Therefore by substitutingS0 with S1 we still get a sphere
system.
This proves that the ﬁnal normal surfaceS′ contains a sphere system
with the same number> K of components as S. Lemma 9.2.27 gives a
contradiction. □
9.2.10. Prime decomposition. We now show that the connected sum
operation on oriented three-manifolds behaves like the product of natural num-
bers: every object decomposes uniquely into prime factors.
284 9. TOPOLOGY OF THREE-MANIFOLDS
Theorem 9.2.29. Every compact oriented 3-manifold M with (possibly
empty) boundary decomposes into prime manifolds:
M =M1#... #Mk
This list of prime factors is unique up to permutations and adding/removing
copies ofS3.
Proof. We ﬁrst show the existence of a decomposition. IfM contains a
non-separating sphere, then the proof of Proposition 9.2.14 shows thatM =
M′#(S2×S1). Since H1(M) = H1(M′)⊕ Z, up to factoring ﬁnitely many
copies ofS2×S1 we may suppose that every sphere inM is separating.
If M is prime we are done. If not, it decomposes asM = M1#M2. We
keep decomposing each factor until all factors are prime: this process must
end, because a decompositionM = M1#... #Mk gives rise to a system of
k− 1 spheres, andk cannot be arbitrarily big by Corollary 9.2.28.
We turn to uniqueness. Let
M =M1#... #Mk#h(S2×S1), M =M′
1#... #M′
k′#h′(S2×S1)
be two prime decompositions withMi,M′
j⁄=S2×S1, soMi,M′
j are irreducible
for alli,j . We say that a setS⊂ M of disjoint spheres is areducing set
of spheres for the decompositionM = M1#... #Mk#h(S2×S1) if M\S
consists of precisely oneMi with some holes for eachi, and some balls with
holes disjoint from∂M. An example is drawn in Figure 9.14. In general, we
may constructS by taking the spheres of the prime decomposition, plus one
non-separating sphere inside eachS2×S1 summand. Similarly, let S′ be a
reducing set of spheres for the other decomposition.
The ﬁrst observation we make is that if we add toS any sphereΣ disjoint
fromS, then we still get a reducing set of spheres for the same decomposition
as before. This is becauseΣ is contained in a holedMi orS3, and sinceMi
is irreducible Σ bounds a ballB there. Therefore by addingΣ we still get the
same holedMi, plus a possibly holed (ifB∩S⁄= ∅) ballB.
We assumeS andS′ intersect transversely in circles and pick an innermost
circle in a component ofS bounding a discD⊂S. We surgerS′ alongD, thus
substituting a componentS′
0 ofS′ with two spheresS′
1⊔S′
2. We check that
the result is another sphere system for the same decomposition. We isotope
the spheresS′
0,S′
1,S′
2 so that they are disjoint and cobound a ball with two
holes B2: the systemS′⊔S′
1⊔S′
2 is still reducing by the observation above.
The removal ofS′
0 then addsB2 to the outside ofS′
0, and this is equivalent
to making one more hole there.
After ﬁnitely many surgeries we getS∩S′ = ∅. By the same observation
above S∪S′ is a reducing set of spheres for both decompositions: therefore
the piecesMi andM′
j of the decompositions are pairwise diﬀeomorphic.
Finally we must haveh =h′ sinceM =N#h(S2×S1) =N#h′(S2×S1)
andH1(M) =H1(N)⊕ Zh =H1(N)⊕ Zh′
. □
9.2. PRIME DECOMPOSITION 285
This important result is known as thePrime decomposition Theoremfor
3-manifolds: the existence of a decomposition was proved by Kneser [33]
in 1929, and its uniqueness by Milnor [41] in 1962. In light of this result,
topologists have since long restricted their attention to prime 3-manifolds, or
almost equivalently to irreducible 3-manifolds.
The strategy of cutting canonically a three-manifold along surfaces has
proved successful with spheres, so we now try to do the same with other
surfaces. We start by studying properly embedded discs, which of course
occur only in manifolds with boundary. It is tempting to guess that discs
should behave roughly like spheres, because by doubling a 3-manifold along its
boundarywetransformproperlyembeddeddiscsintospheres. Wenowseethat
this is indeed the case. As for spheres, we need to distinguish the interesting
ones, that we callessential, from the others.
9.2.11. Essential discs. Let M be a compact 3-manifold with (possibly
empty) boundary. A properly embedded surface S ⊂ M is ∂-parallel if it
is obtained by slightly pushing insideM the interior of a compact surface
S′⊂∂M, possibly with boundary.
In what followsD andS are properly embedded. We say that:
• a sphereS⊂M is essential if it does not bound a ball,
• a discD⊂M is essential if it is not∂-parallel.
Now, the manifoldM is:
• irreducible if it does not contain essential spheres, and
• ∂-irreducible if it does not contain essential discs.
To warm up, we show the following. Asolid torusis a handlebody of genus
1, that is a three-manifold diﬀeomorphic toD×S1.
Proposition9.2.30. LetM beacompact, irreducible, orientable3-manifold
with boundary, and letD⊂ M be an essential disc. Let Σ⊂ ∂M be the
boundary component containing∂D. Then:
• the curve∂D is non-trivial inΣ;
• if Σ is a torus thenM is a solid torus.
Proof. If∂D bounds a discD′⊂ Σ thenD∪D′ is a sphere, which bounds
a ball becauseM is irreducible; this ball furnishes a parallelism betweenD and
D′ and henceD is∂-parallel, a contradiction.
If Σ is a torus, by surgeryingΣ alongD we get a sphere which must bound
a ballB. ThereforeM is obtained by adding a one-handle toB, that is it is a
solid torus. □
9.2.12. Decomposition along discs. We now show that essential discs
behave roughly like essential spheres, in the sense that there is a kind of prime
decomposition theorem also for discs. After stating and proving this theorem,
286 9. TOPOLOGY OF THREE-MANIFOLDS
we will essentially forget about essential spheres and discs and focus on the
3-manifolds that do not contain them.
Let M be a compact 3-manifold with (possibly empty) boundary. Adisc
system inM is a set of pairwise disjoint and non-parallel essential discs.
Proposition 9.2.31. There is aK >0 such that every disc system inM
cannot contain more thanK discs.
Proof. The proof is analogous to that of Corollary 9.2.28 □
We now want to cut irreducible manifolds along essential discs.
Remark 9.2.32. The opposite operation of cutting a manifold along a
properly embedded disc is a 1-handle addition.
We now state the analogue of Theorem 9.2.29 in this context. Note
that M is irreducible by hypothesis: we have already eliminated the essential
spheres, and we now remove the essential discs.
Theorem 9.2.33.Every compact oriented irreducible 3-manifoldM is ob-
tained by adding 1-handles to a ﬁnite list
M1,...,M k
of connected irreducible and∂-irreducible 3-manifolds. The list is unique up
to permutations and adding/removing balls.
Proof. The proof is similar to Theorem 9.2.29. If we cut M along a
maximal disc system we get some connected manifoldsM1,...,M k. Each
Mi is ∂-irreducible because the disc system is maximal, and it is irreducible
because every sphere inMi⊂M bounds a ballB in M, andB is necessarily
contained inMi.
We prove uniqueness. Pick two sets of discsS,S′ ⊂ M such that by
cutting along each we get irreducible and∂-irreducible components. We prove
that these components are the same up to adding/removing balls. We assume
thatS andS′ intersect transversely.
A circleS∩S′ which is innermost with respect toS is bounded by two
sub-discs D⊂ S and D′⊂ S′, which together form a sphere: this sphere in
turn bounds a ball (becauseM is irreducible) as in Figure 9.15. We can use
the ball to isotopeS′ away fromS and reduce the intersections inS∩S′.
After ﬁnitely many isotopies there are no circles inS∩S′.
We are left to consider the arcs inS∩S′. We end precisely as in Theorem
9.2.29. We observe that by adding more discs toS orS′ we get a set of discs
that∂-reducesM into the same list ofMi’s, plus possibly some balls.
Thanks to an innermost argument, we may surger some discD0⊂S along
an arc inD0∩S′ and transform it into two discsD1⊔D2, both disjoint from
S and with less intersections withS′. The setS⊔D1⊔D2 is still a reducing
set for theMi’s. If we removeD0 from this new system, in the complement
