---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-023-52-extensions-of-homotopies
section_title: "Extensions of homotopies"
section_number: 5.2
pages: 151-163
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
Figure 5.4. Diﬀerent choices of truncated cusps may lead to distinct
decompositions into ideal polyhedra.
A way to get a truly canonical decomposition ofM, which depends on no
choice, consists of takingV1 = ... = Vc > 0. Note that when c = 1 any
choice leads to the same canonical decomposition.
5.2. Extensions of homotopies
This section is entirely devoted to the proof of the following theorem.
Recall that every mapf : M → N between connected manifolds lifts to a
(non-unique) map ˜f : ˜M→ ˜N between their universal covers.
Theorem 5.2.1. Let f : M→ N be a smooth homotopy equivalence be-
tween closed hyperbolicn-manifolds. Every lift ˜f : Hn → Hn extends to a
continuous map ˜f : Hn→ Hn whose restriction ˜f|∂Hn :∂Hn→∂Hn is a home-
omorphism.
Every smooth homotopy equivalence extends to a homeomorphism of the
boundaries of the universal coverings. This theorem will have important con-
sequences in the Chapters 8 and 13. To prove it, we need to deﬁne a weaker
notion of isometry.
5.2.1. Quasi-isometries. We introduce the following.
Deﬁnition 5.2.2. A mapF : X → Y between metric spaces is aquasi-
isometry if there are two constantsC1> 0,C2> 0 such that
1
C1
d(x1,x 2)−C2⩽d(F (x1),F (x2))⩽C1d(x1,x 2) +C2
for allx1,x 2∈X andd(F (X),y )⩽C2 for ally∈Y.
A quasi-isometry is an isometry up to some error: note thatF might
neither be continuous nor injective. Two metric spaces arequasi-isometric if
there is a quasi-isometryF :X→Y (which implies the existence of a quasi-
isometry G : Y → X, exercise) and quasi-isometry is an equivalence relation
between metric spaces. Intuitively, looking at a space up to quasi-isometries
144 5. THE SPHERE AT INFINITY
is like watching it from some distance. Compact metric spaces are obviously
quasi-isometric to a point.
This notion is an important ingredient ingeometric group theory: one may
for instance give every ﬁnitely-presented groupG a canonical metric (through
its Cayley graph), uniquely determined up to quasi-isometries.
5.2.2. Pseudo-isometries. Let f : M→ N be a homotopic equivalence
between closed hyperbolicn-manifolds. Every continuous function is homo-
topic to a smooth one, hence we suppose thatf is smooth. The map lifts to
a map ˜f : Hn→ Hn. We will prove that˜f is a quasi-isometry. Actually, the
map ˜f is also continuous and (as we soon see) Lipschitz: it will be useful for
us to retain this information on˜f to simplify some arguments, so we introduce
a diﬀerent (more restrictive but less natural) version of a quasi-isometry.
Deﬁnition 5.2.3. A mapF : X→ Y between metric spaces is apseudo-
isometry if there are two positive constantsC1,C 2> 0 such that
1
C1
d(x1,x 2)−C2⩽d(F (x1),F (x2))⩽C1d(x1,x 2)
for allx1,x 2∈X.
In particular a pseudo-isometry isC1-Lipschitz and hence continuous. Let
f :M→N be a smooth map between Riemanniann-manifolds; themaximum
dilatation off at a pointx∈M is the maximum ratio‖dfx (v)‖
‖v‖ wherev varies
among all the unitary vectors inTx. The maximum dilatation of f is the
supremum of all maximum dilatations asx∈M varies.
Exercise 5.2.4. If f : M → N has maximum dilatationC the map f is
C-Lipschitz.
Proposition 5.2.5. Let f :M→N be a smooth homotopy equivalence of
closed hyperbolicn-manifolds. The lift ˜f : Hn→ Hn is a pseudo-isometry.
Proof. SinceM iscompact, themap f hassomeﬁnitemaximumdilatation
C. Since ˜f is locally likef, it also has maximum dilatationC and is henceC-
Lipschitz. The same holds for the homotopic inverseg :N→M. Therefore
there is aC1> 0 such that
d
( ˜f (x1), ˜f (x2)
)
⩽C1·d(x1,x 2) ∀x1,x 2∈ Hn,
d
(
˜g(y1), ˜g(y2)
)
⩽C1·d(y1,y 2) ∀y1,y 2∈ Hn.
We haveM = Hn/Γ. Being a composition of lifts, the map˜g◦ ˜f commutes
with Γ and has maximum displacement bounded by someK >0 equal to the
maximum displacement of the points in a (compact) Dirichlet domain. Hence
d(x1,x 2)− 2K⩽d
(
˜g( ˜f (x1)), ˜g( ˜f (x2))
)
⩽C1·d
( ˜f (x1), ˜f (x2)
)
for allx1,x 2∈ Hn. Therefore ˜f is a pseudo-isometry withC2 = 2K/C1. □
5.2. EXTENSIONS OF HOMOTOPIES 145
Figure 5.5. We use the half-space model. The hyperbolic cosine of the
distance betweenx and π(x) is the inverse of the cosine ofθ (left). To
determine the maximum dilatation we decompose the tangent spaceTx
orthogonally asU⊕V (right).
5.2.3. Boundary extension of a pseudo-isometry.We now prove that
not only pseudo-isometries Hn→ Hn extend at inﬁnity, but their extensions
at∂Hn eliminate the “errors” and behave nicely.
Theorem 5.2.6.Every pseudo-isometryF : Hn→ Hn extends to a contin-
uous mapF : Hn→ Hn that injects∂Hn into itself.
We separate the proof in some lemmas.
Lemma 5.2.7. Consider the picture in Figure 5.5. We have
coshd(x,π (x)) = 1
cosθ.
Proof. We can work with the half-plane modelH2⊂ C and up to trans-
lations and dilations suppose thatπ(x) = i. The geodesicr is parametrized
asiet. The Möbius transformationz↦→ z+1
−z+1 sendsr toγ and ﬁxesi, hence
γ(t) = iet +1
−iet +1. Sets =d(x,π (x)). We getx = ies +1
−ies +1 and
cosθ =ℑx =ℑ(ies + 1)2
e2s + 1 = 2es
e2s + 1 = 2
es +e−s = 1
coshs.
The proof is complete. □
Lemma 5.2.8. Let r ⊂ Hn be a line andπ : Hn→ r be the orthogonal
projection tor. The maximum dilatation ofπ atx∈ Hn is
d = 1
coshs
wheres =d(x,r ).
Proof. We use the half-space model withr and x as in Figure 5.5-(left):
we know thatcoshs = 1
cosθ. We haveTx = U⊕V as in Figure 5.5-(right)
withV = kerdπx. A generatoru ofU is just rotated bydπx with respect to
the Euclidean metric; with respect to the hyperbolic metric we have
‖dπx (u)‖
‖u‖ = xn
π(x)n
= cosθ = 1
coshs.
146 5. THE SPHERE AT INFINITY
Figure 5.6. We use the red paths to estimate the distance between
F (r ) and F (s). On the left: sinceF is C1-Lipschitz, the blue path has
length at most C1d(r,s ). Its projection onto l has dilatation at most
1/coshR by Lemma 5.2.8, hence the red path inl has length at most
C1d(r,s )/ coshR. Therefore d(F (r ),F (s)) ⩽ C1
d(r,s )
coshR + 2R. On the
right we getd(F (r ),F (s))⩽ 2R.
The proof is complete. □
We writepq for the segment with endpointsp and q and we denote by
Nr (A) ther-neighbourhood ofA.
Lemma 5.2.9. Let F : Hn→ Hn be a pseudo-isometry. There is aR> 0
such that
F (pq)⊂NR
(
F (p)F (q)
)
for all distinct pointsp,q ∈ Hn.
Proof. LetC1,C 2 bethepseudo-isometryconstantsof F. Fixasuﬃciently
bigR so that coshR> 2C2
1. Letl be the line containingF (p) andF (q). We
show thatF (pq) can exit fromNR(l) only for a limited amount of time. Let
rs ⊂ pq be a maximal segment whereF (rs ) is disjoint from the interior of
NR(l), as the blue arc in Figure 5.6-(left). We have
1
C1
d(r,s )−C2⩽d(F (r ),F (s))⩽C1d(r,s ).
We can improve the right inequality as shown in Figure 5.6-(left) and write
1
C1
d(r,s )−C2⩽d(F (r ),F (s))⩽C1
d(r,s )
coshR + 2R.
Therefore ( 1
C1
− C1
coshR
)
d(r,s )⩽ 2R +C2.
Since coshR >2C2
1 we deduce thatd(r,s ) < Mfor some constantM that
depends only onC1 andC2.
5.2. EXTENSIONS OF HOMOTOPIES 147
F(p)
F(l(u))
F(l(t))atu <R
Figure 5.7. For every 0<u <t , the pointF (l(u)) is contained in the
(yellow)R-neighbourhood ofF (p)F (l(t)). If u is big, the blue segment
F (p)F (l(u)) is long, while the red one is bounded byR: hence the angle
αtu betweenvt andvu is small. Thereforevt is a Cauchy sequence.
We have proved thatF (pq) may exit fromNR(l) only on subsegments of
pq with length< M. Since F is C1-Lipchitz the curveF (pq) lies entirely in
NR+C1M(l), and we replaceR withR +C1M.
It remains to prove thatF (pq) lies entirely (up to taking a biggerR) in the
bounded setNR(F (p)F (q)): the proof is analogous and easier, since Figure
5.6-(right) shows thatd(F (r ),F (s))⩽ 2R. □
In the previous and following lemmas, the constantR depends only on the
pseudo-isometry constantsC1 andC2.
Lemma 5.2.10.LetF : Hn→ Hn be a pseudo-isometry. There is aR> 0
such that for allp∈ Hn and every half-linel starting fromp there is a unique
half-linel′ starting fromF (p) such that
F (l)⊂NR(l′).
Proof. We parametrizel as a geodesicl : [0, +∞)→ Hn with unit speed.
We havel(0) =p. SinceF is a pseudo-isometry we get
lim
t→∞
d
(
F (p),F (l(t))
)
=∞.
Letvt∈TF (p) be the unitary tangent vector pointing towardsF (l(t)): Figure
5.7 shows that{vt}t∈N is a Cauchy sequence, hence it converges to a unitary
vectorv∈TF (p). Let l′ be the half-line starting fromF (p) with directionv.
It is easy to check thatF (l)⊂NR(l′) andl′ is the unique half-line fromp with
this property. □
The previous lemma gives a recipe to transform every half-linel into a
half-line l′ that approximatesF (l). Since ∂Hn is an equivalence relation of
half-lines, we deﬁne the extensionF :∂Hn→∂Hn by sendingl tol′.
Lemma 5.2.11. The boundary extensionF : ∂Hn→ ∂Hn is well-deﬁned
and injective.
Proof. Letl1,l 2 be two half-lines at bounded distanced(l1(t),l 2(t))<M
for all t. If d(l′
1(t),l′
2(t)) → ∞we get d
(
F (l1(t)),F (l2(t))
)
→ +∞, a
148 5. THE SPHERE AT INFINITY
Figure 5.8. Let l and H be a line and an orthogonal hyperplane. The
orthogonal projection ofH onto l is obviously a pointl∩H; the pseudo-
isometry F mildly distorts this picture: the image F (H) projects to a
bounded segment inl′.
contradiction since F is Lipschitz. Therefore l′
1,l′
2 are at bounded distance
andF is well-deﬁned.
Injectivity is proved analogously: ifl1 and l2 are divergent thenl′
1 and l′
2
also are becauseF is a pseudo-isometry. □
It remains to prove that the extensionF : Hn→ Hn is continuous. We
start by extending Lemma 5.2.10 from half-lines to lines.
Lemma 5.2.12.LetF : Hn→ Hn be a pseudo-isometry. There is aR> 0
such that for every linel there is a unique linel′ withF (l)⊂NR(l′).
Proof. Parametrizel asl : (−∞, +∞)→ Hn with unit speed. By cutting
l into two half-lines we know thatF (l(t)) is a curve that tends to two distinct
points x±∈∂Hn as t→±∞ . Let l′ be the line with endpointsx±. For any
t >0 we have
F
(
l([−t,t ])
)
⊂NR
(
F (l(−t))F (l(t))
)
and by sendingt→ +∞ we deduce thatF (l)⊂NR(l′). □
The next lemma says that a pseudo-isometry does not distort much lines
and orthogonal hyperplanes. We will need it to prove continuity.
Lemma 5.2.13.LetF : Hn→ Hn be a pseudo-isometry. There is aR> 0
such that for any linel and hyperplaneH orthogonal tol, the imageF (H)
projects orthogonally tol′ onto a bounded segment length smaller thanR.
Proof. See Figure 5.8. Consider a generic lines ⊂ H passing through
p = l∩H. By the previous lemmas F (s)⊂ NR(s′) with s′⁄= l′, and the
orthogonal projection onl′ sends any other lines′ onto a segment, bounded
by the images of the endpoints ofs′.
5.2. EXTENSIONS OF HOMOTOPIES 149
l
H
l'
s
dd
s1
s2
s'1
s'2
p
∞s
∞F(s )
F(p)
f
F
q
Figure 5.9. The liness1 ands2 have a distanced fromp which depends
on nothing (in fact,coshd =
√
2). The linesl′, s′
1, ands′
2 approximate
up to an errorR the images ofl,s1, ands2 alongF. The projectionq of
F (p) on l′ is henceR-close toF (p), which is in turn(C1d)-close to the
lines s′
i. Therefore q is (C1d + 2R)-close to boths′
1 and s′
2. This easily
implies thatf is (C1d + 2R)-close toq.
Consider as in Figure 5.9 the lines, with one endpoints∞ and the cor-
responding endpointF (s∞) of s′. The ﬁgure shows that the projectionf of
F (s∞) tol′ is at bounded distance from a pointq which does not depend on
s. □
Finally, we prove that the extendedF is continuous.
Lemma 5.2.14. The extensionF : Hn→ Hn is continuous.
Proof. Consider x ∈ ∂Hn and its imageF (x)∈ ∂Hn. Let l be a half-
line pointing tox: hencel′ points toF (x). The half-spaces orthogonal tol′
determine a neighbourhood system forF (x): consider one such half-spaceS.
Let R >0 be as in the previous lemmas. The imageF (l) is R-close to
l′, hence for suﬃciently bigt the pointF (l(t)) and its projection intol′ lie in
S at distance> Rfrom ∂S. By the previous lemma the imageF (H(t)) of
the hyperplaneH(t) orthogonal tol inl(t) is also contained inS. Hence the
entire half-space bounded by one suchH(t) goes insideS through F. This
shows thatF is continuous at every pointx∈∂Hn. □
With some eﬀort, we have proved that every pseudo-isometry ofHn ex-
tends continuously to the boundary. Theorem 5.2.1 now follows easily.
Proof of Theorem 5.2.1. We know that˜f is a pseudo-isometry and hence
extends to a map˜f : Hn→ Hn that sends injectively∂Hn to itself. It remains
to prove that˜f|∂Hn is a homeomorphism.
Pick a smooth homotopic inverseg forf. The homotopyidM∼g◦f lifts
to a homotopyidHn∼ ˜g◦ ˜f for some lift˜g. Since M is compact, the latter
homotopy moves every point at uniformly bounded distance and hence˜g◦ ˜f
150 5. THE SPHERE AT INFINITY
extends continuously to the identity on∂Hn, and the same holds for˜f◦ ˜g.
Therefore ˜g|∂Hn istheinverseof ˜f|∂Hn andtheyarebothhomeomorphisms. □
5.2.4. References. Asinthepreviouschapters, wehavemostlyconsulted
Benedetti – Petronio [4], Ratcliﬀe [49], and Thurston’s notes [56]. The Ep-
stein – Penner decomposition is taken from their 1988 paper [17].
Part 2
Surfaces
CHAPTER 6
Surfaces
A surface is a diﬀerentiable manifold of dimensionn = 2, possibly with
boundary. The closed orientable surfaces are classiﬁed topologically by their
Euler characteristic, a complete invariant that also determines their possible
geometries: a closed surface has a hyperbolic, ﬂat, or spherical structure if
and only if its Euler characteristic is negative, null, or positive.
We devote some time here to expose the topological classiﬁcation and the
geometrisation of closed surfaces. Then we describe some of the beautiful
features of geometrisation: the geometry of a surface (typically, hyperbolic
geometry)canbeusedtoproveinanelegantwayvariousnon-trivialtopological
facts.
We end this chapter by deﬁning and studying themapping class group, a
group that encodes the topological symmetries of a surface.
6.1. Topological classiﬁcation
A surface can be topologically quite complicated: think for instance ofR2
with a Cantor set removed. We decide to restrict our investigation to the sur-
faces of ﬁnite type, i.e. obtained from a closed one by removing points and/or
open discs: these include all the compact surfaces with or without boundary.
We introduce here these surfaces and classify them up to diﬀeomorphism.
We manipulate surfaces using various cut-and-paste tools: boundary glu-
ings, removal of discs or points, handle decompositions, connected sums. See
Section 1.1 to refresh these notions.
6.1.1. Gluing surfaces. A simple way to construct a surface is by gluing
simpler surfaces along their boundaries. We show here that the glued surface
depends only on the orientation classes of the gluing maps.
Two self-diﬀeomorphisms ofS1 are co-oriented if they both preserve or
both invert the orientation ofS1.
Lemma 6.1.1. Two co-oriented self-diﬀeomorphisms ofS1 are isotopic.
Proof. Letf0,f 1 :S1→S1 be two co-oriented self-diﬀeomorphisms. Their
lifts ˜f0, ˜f1 : R→ R are periodic and monotone, hence˜ft = (1−t) ˜f0 +t ˜f1 also
is and descends to an isotopyft connectingf0 andf1. □
153
154 6. SURFACES
Figure 6.1. A surface of genus3 may be represented in various ways.
Corollary 6.1.2.If we glue two oriented surfaces along their boundaries via
orientation-reversing diﬀeomorphisms, the resulting oriented surface does not
depend on the diﬀeomorphisms chosen.
Proof. All the orientation-reversing gluing maps are isotopic by Lemma
6.1.1, and isotopic gluing maps produce diﬀeomorphic manifolds, as stated in
Proposition 1.1.15. □
In a non-oriented context, we have two possible maps for every glued
boundary component.
Corollary 6.1.3.If we glue two discs we get a sphere.
Proof. The two discs are copies ofD2⊂ C and are glued along a diﬀeo-
morphism ϕ:S1→ S1. Up to mirroring one disc we may suppose thatϕ is
orientation-reversing, and by Corollary 6.1.2 we may suppose thatϕ(z) = ¯z.
The resulting surface is diﬀeomorphic to a sphere (exercise). □
Warning 6.1.4. In dimensionn> 7, by gluing two discs we may get a
manifold homeomorphic butnot diﬀeomorphic to a sphere! See Section 6.4.2.
6.1.2. Classiﬁcation of surfaces.In Section 1.1.13 we introduced the
connected sum, a two-steps operation which consists of ﬁrst removing balls
and then gluing the new sphere boundaries. LetSg be the connected sum
Sg =T #... #T| {z }
g
of g toriT =S1×S1. By conventionS0 =S2 is the sphere andS1 =T is
the torus. The numberg is thegenus of the closed surfaceSg. The surface
Sg may be represented inR3 in various ways, see Figure 6.1.
Proposition 6.1.5. We haveχ(Sg) = 2− 2g.
Proof. LetS,S′ be surfaces andD⊂ int(S),D′⊂ int(S′) be discs. Then
χ(S#S′) =χ(S\D) +χ(S′\D′)−χ(S1) =χ(S) +χ(S′)− 2.
Thereforeχ(Sg) = 2− 2g by induction ong. □
