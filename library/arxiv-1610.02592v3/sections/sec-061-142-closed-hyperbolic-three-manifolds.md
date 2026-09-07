---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-061-142-closed-hyperbolic-three-manifolds
section_title: "Closed hyperbolic three-manifolds"
section_number: 14.2
pages: 441-451
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
14.2. Closed hyperbolic three-manifolds
We have described in Section 14.1 a method to construct cusped ﬁnite-
volume hyperbolic three-manifolds. How can we now build someclosed hyper-
bolic three-manifolds?
Following the same path, we could try to parametrizecompact hyperbolic
tetrahedra via some variables, and then encode the isometric gluings of their
faces via some equations. However, it is really hard to parametrize compact
tetrahedra and their gluings, and nobody has ever constructed any closed
hyperbolic three-manifold in this way!
The usual procedure for building closed hyperbolic three-manifolds consists
of using (again) ideal tetrahedra: we start with a cusped manifold, and then we
slightly modify the completeness equations to allow some appropriate Dehn-
ﬁlling of some (or all) cusps.
14.2.1. Dehn ﬁlling parameters.We now consider an orientable three-
manifold M = int(N) where N is compact and∂N = T1⊔... ⊔Tc consists
of tori. For simplicity we will always assume that eachTi is incompressible, so
thatπ1(Ti ) = Z× Z injects inπ1(N) =π1(M) for alli.
We ﬁx once for all two generatorsmi,li ofπ1(Ti ) for eachi = 1,...,c . A
Dehn ﬁlling parameters = (s1,...,s c) is a sequence where eachsi is either a
pair (p,q ) of coprime integers or the symbol∞. It is useful to think ofsi as
a point in the two-sphereS2 = R2∪{∞}.
A Dehn ﬁlling parameters determines a Dehn ﬁlling ofN as follows: for
everyi, ifsi = (p,q ) we ﬁllTi by killing the slopepmi +qli, while ifsi =∞ we
do nothing. The result is a new compact manifold, whose interior we denote
by Mﬁll, that may be closed (if there are no∞ in s) or may be bounded by
some tori.
We now ﬁx a Dehn ﬁlling parameters, producing a ﬁlled manifoldMﬁll.
14.2.2. The modiﬁed equations.LetT be an oriented ideal triangula-
tion forM. We now describe some equations similar to that of Section 14.1,
whose solutions now identify hyperbolic structures onMﬁll instead ofM. The
equations of course will depend on the Dehn ﬁlling parameters, since the
manifoldMﬁll does.
The triangulationT consists of somen tetrahedra ∆1,..., ∆n; we choose
an edge in each∆i and we assign it the variablezi∈ C withℑzi > 0 as we
did in Section 14.1.
The edges of all tetrahedra are now coloured with modulizi, 1
1−zi
, zi−1
zi
that lie in the upper half-plane and as such may be written in polar coordinates
asρeiθ withθ∈ (0,π ). It is convenient to consider these variables as elements
of the multiplicative group
~C∗ =
{
ρeiθ ⏐⏐ρ∈ R>0, θ∈ R
}
434 14. HYPERBOLIC THREE-MANIFOLDS
that covers C∗ and is isomorphic toC via the mapexp : C→~C∗.
Every edge ofT furnishes a consistency equation in ~C∗ as described in
Section 14.1, of the form
w1··· wh =e2πi.
Note thate2πi⁄= 1 in ~C∗, so by interpreting the consistency equations in~C∗
we have also incorporated the request that all angles sum to2π.
Letz = (z1,...,z n) be a solution to the consistency equations. We have
deﬁned in Proposition 14.1.4 a homomorphismµ: π1(Ti ) → C∗ for every
boundary torusTi, and we now lift it to~C∗.
Deﬁnition 14.2.1. Represent each non-trivialγ ∈ π1(Ti ) as a simplicial
path that lifts to an embedded path in the universal cover ofTi. Deﬁne˜µ(γ)
to bee−|γ|πi times the product of all the moduli thatγ encounters at its right
side, considered now as elements in the group~C∗. Ifγ is trivial, set˜µ(γ) = 1.
Exercise 14.2.2. The element˜µ(γ)∈~C∗ is well-deﬁned and
˜µ:π1(Ti )→~C∗
is a homomorphism.
We now deﬁne some newcompleteness equations at Ti for each i =
1,...,c that depend on the Dehn ﬁlling parametersi. There are two cases to
consider for eachi = 1,...,c . Ifsi =∞, the completeness equations relative
toTi are the two equations
µ(mi ) =µ(li ) = 1
already considered in Section 14.1.5. (If we wish, we can substitute them with
the equations ˜µ(mi ) = ˜µ(li ) = 1. Both choices will work.)
Ifsi = (p,q ) we deﬁne one new completeness equation
˜µ(mi )p· ˜µ(li )q =e2πi.
The total number of completeness equations therefore varies fromc to 2c,
depending on the number of cusps that are left unﬁlled. The main goal of this
section is to prove the following.
Theorem 14.2.3.A solutionz = (z1,...,z n) to the consistency and com-
pleteness equations determines a hyperbolic structure onM whose completion
M is a complete hyperbolic manifold diﬀeomorphic toMﬁll.
If s ⁄= (∞,..., ∞) the solution z determines an incomplete hyperbolic
metric onM, and the miracle here is that the completionM is another hyper-
bolic manifold!
We note that both the consistency and completeness equations are of type
w1··· wh = 1 ore2πi. The rest of this section is mainly devoted to the proof of
Theorem 14.2.3. We start with a short discussion that introduces (truncated)
14.2. CLOSED HYPERBOLIC THREE-MANIFOLDS 435
solid tori with cone angles: these objects will be crucial in the proof of the
theorem.
14.2.3. The inﬁnite branched covering.Let l ⊂ H3 be any line and
recall the universal cover
π :X−→ H3\l
already considered in Section 3.5.4 when we introduced manifolds with cone
singularities. The manifoldX is incomplete and its completionX is obtained
by adding a copy˜l ofl.
We use the half-space model and representl as the vertical axis, so that
H3\l = C∗× R>0 and we can write
X =~C∗× R>0.
We note that~C∗ acts onX via isometries: the elementw∈~C∗ acts as
(z,t )↦−→(wz,|w|t).
Whenw =eαi thisistherotationofangle αthatwasusedtodeﬁnehyperbolic
cone manifolds. When|w|⁄ = 1 the map projects to a hyperbolic isometry of
H3 with axisl and translation distancelog|w|.
14.2.4. Tubes with cone angles.A non-trivial discrete groupΓ<~C∗∼=
C is either isomorphic toZ or toZ× Z; it acts freely onX and (not necessarily
freely!) on the line˜l. Concerning Z× Z, there are two cases to consider.
If Γ = Z× Z contains a non-trivial rotation, it is generated by some maps
(z,t )↦→ (eαiz,t ), (z,t )↦→eλ(eβiz,t )
with λ⁄= 0, and it acts on˜l as translations whose step is an integer multiple
ofλ. The quotientX/Γ is naturally a complete hyperbolic manifold with cone
angles: it is an open solid torus with singular locus a closed geodesic of length
|λ| and with cone angleα. We call it atube with cone angleα. Whenα = 2π
we get an ordinary tube as in Section 4.1.2, with no singular points.
If Γ = Z×Z does not contain a rotation, it acts on˜l as an indiscrete group
of translations and henceX/Γ is not a hyperbolic manifold with cone angles
(it is not even Hausdorﬀ). We also note thatX/Γ is not the completion of
the hyperbolic manifoldX/Γ in that case, but it only maps surjectively onto it:
the completion adds a single point toX/Γ.
Tubes have natural truncations. For everyR > 0 the R-neighbourhood
NR(˜l)⊂X of the singular line˜l projects onto theR-neighbourhoodNR(l) of
l, which is a Euclidean cone with axisl. The group Γ preservesNR(˜l) and in
the ﬁrst case its quotient is a truncated tube with cone angles.
436 14. HYPERBOLIC THREE-MANIFOLDS
14.2.5. Incomplete solutions. We now go back to our triangulationT,
and we letz = (z1,...,z n) be a solution to the consistency equations for
T. The solution z furnishes a hyperbolic metric onM, which might not be
complete: we want to understand the metric completionM ofM. Recall that
M is diﬀeomorphic to the interior of a compactN whose boundary consists of
c tori.
We pick a boundary torusT ⊂ ∂N and deﬁne acollar C(T )⊂ M of
T to be the intersection of a closed collar ofT in N with M. We know
from Proposition 14.1.5 that whenµ:π1(T )→ C∗ is trivial there is a collar
C(T ) isometric to a truncated cusp, that is the truncated quotient ofH3 by
a discrete Z× Z of parabolic elements.
When µ is not trivial, we now show that a similar (but diﬀerent) con-
ﬁguration arises: there is a collarC(T ) isometric to a truncated quotient of
the hyperbolic manifoldX considered above by a discreteZ× Z. The crucial
diﬀerence is thatC(T ) now is incomplete, becauseX is. To prove this fact
we use developing maps and holonomies.
The hyperbolic ideal triangulationT of M determined byz lifts to a hy-
perbolic ideal triangulation ˜T for the universal cover ˜M→ M with inﬁnitely
many tetrahedra. The triangulated torusT is the link of a vertexv ofT. We
ﬁx a lift˜v ofv in ˜T, and the link of˜v is a triangulated surface˜T that covers
T. SinceT is incompressible,π1(T ) injects inπ1(M) and hence ˜T is a plane.
Recall from Section 3.5.3 that there is a developing mapD : ˜M→ H3 and
a holonomyρ:π1(M)→ Isom+(H3), and both are determined once we deﬁne
D on an ideal tetrahedron in ˜T. We choose for our convenience one ideal
tetrahedron incident to˜v and we map it to the half-space modelH3 with an
isometryD that sends ˜v to∞.
The developing mapD sends all tetrahedra of˜T incident to ˜v to vertical
ideal tetrahedra inH3 with one vertex at∞. Ifγ∈π1(T ), thenρ(γ)permutes
these tetrahedra and ﬁxes∞. Therefore the holonomyρ sendsπ1(T ) = Z×Z
to a group of commuting elements inPSL2(C) ﬁxing∞. Every such element
may be written asz↦→az +b, and there are two possibilities:
• the group consists of translationsz↦→z +b,
• the group ﬁxes a pointp∈ C.
In the second case we may supposep = 0 up to translating everything, so
the maps are all of typez↦→az. Not surprisingly, the holonomyρ is tightly
connected with the homomorphismµ:π1(T )→ C∗.
Exercise 14.2.4. The derivativeρ(γ)′, that is the coeﬃcient1 ora in the
above examples, equalsµ(γ).
We now suppose thatµ is non-trivial and hence the ﬁrst possibility is
excluded: the groupρ(π1(T )) consists of mapsz↦→az and we can identifyρ
withµ. The mapD induces a developing mapD : ˜T→ C with holonomyµ.
14.2. CLOSED HYPERBOLIC THREE-MANIFOLDS 437
0 0
l l
Figure 14.11. For suﬃciently smallR > 0 the cone neighbourhood
NR(˜l) of ˜l does not intersect the lower faces of the developed images of
˜∆i1,..., ˜∆ih (left). These tetrahedra intersect∂NR(˜l) into triangles that
glue up to determine a torusTR inC(T ) (right).
Proposition 14.2.5. The imageD( ˜T ) misses the origin.
Proof. The vector ﬁeldv (z) = z on C is µ(π1(T ))-invariant and hence
pulls-back viaD to a vector ﬁeld onT. If 0∈D( ˜T ) then this vector ﬁeld on
T has some zeroes, all with index1: a contradiction sinceχ(T ) = 0. □
Let St˜v⊂ ˜M be the open star of˜v, that is the union of all ideal tetrahedra
incident to ˜v, with the faces not incident to˜v removed: it is homeomorphic
to ˜T× [0, +∞) and hence simply connected. The proposition implies that the
restriction D|St˜v of the developing map misses the entire vertical linel⊂ H3
above the origin and hence lifts to a map
˜D : St ˜v−→X.
Likewise the holonomyρ atπ1(T ) lifts to a holonomy
˜ρ:π1(T )−→~C∗< Isom+(X)
which is of course related to the homomorphism˜µ:π1(T )→~C∗.
Exercise 14.2.6. We have˜ρ = ˜µ.
After this long discussion, we can ﬁnally discover how a collarC(T ) ofT
looks like.
Proposition 14.2.7. If µ is non-trivial then ˜µ is injective and has discrete
image. There is a collarC(T ) that is isometric to a truncation ofX/Im ˜µ.
Proof. We have deﬁned a lifted developing map˜D : St ˜v→X with holo-
nomy ˜ρ = ˜µ.
438 14. HYPERBOLIC THREE-MANIFOLDS
Let ∆i1,..., ∆ih be the tetrahedra incident tov (with multiplicities), and
let ˜∆i1,..., ˜∆ih be any lifts in ˜T incident to ˜v. We ﬁx a suﬃciently small
R0 > 0 such that the coneNR0(˜l)⊂ X does not intersect the lower faces
of the tetrahedra˜D(˜∆i1),..., ˜D(˜∆ih), see Figure 14.11-(left). SinceNR0(˜l) is
ρ(π1(T ))-invariant, it does not intersect the lower faces of any ideal tetrahe-
dron in the image of˜D, and hence it intersects every ideal tetrahedron in a
curved triangle as in Figure 14.11-(right).
We deﬁne~C(T )⊂ ˜M as the preimage ofNR0(˜l) along ˜D. By construction
it is aπ1(T )-invariant submanifold that projects to a submanifoldC(T )⊂
M. This submanifold intersects every tetrahedron incident tov into a cone
neighbourhood ofv and is hence a collar forT. We want to prove that the
map
˜D : ~C(T )−→NR0(˜l)\ ˜l
is an isometry. Being a local isometry, it suﬃces to prove that it is injective
and surjective. We prove this using the natural foliation ofNR0(˜l)\ ˜l into the
sheets∂NR(˜l) withR⩽R0.
For everyR⩽R0 the map ˜D restricts to a local isometry of surfaces
˜DR : ˜TR→∂NR(˜l)
where ˜TR = ˜D−1(∂NR(˜l)) is π1(T )-invariant and covers a torusTR ⊂ M
parallel toT. SinceTR is compact, the cover˜TR is complete. Therefore ˜DR
is a covering by Proposition 1.2.19 and is hence an isometry since∂NR(˜l) is
simply-connected. In particular it is a bijection for allR<R 0, and hence˜D is
a bijection.
Since ˜D is an isometry, its holonomy˜ρ is discrete and injective and
C(T )∼=
(
NR0(˜l)\ ˜l
)
/˜ρ(π1(T )).
The proof is complete. □
14.2.6. The completion. We now have an isometric model for the collar
C(T ) of T and we study its completion. This analysis will lead to a proof of
Theorem 14.2.3.
We suppose thatµ is non-trivial and henceC(T ) is not complete. By
Proposition 14.2.7, the completionC(T ) ofC(T ) depends on theZ× Z group
Im ˜µ< ~C∗ acting onX: see Section 14.2.4 where we deﬁned in particular the
(truncated) tubes with cone angles.
Proposition 14.2.8. If Im ˜µ contains a non-trivial rotation thenC(T ) is a
truncated tube with some cone angle; otherwise it is a one-point compactiﬁ-
cation ofC(T ).
In the ﬁrst case, there are generatorsγ,η forπ1(T ) such that
˜µ(γ) =eαi, ˜µ(η) =eλ+βi
14.2. CLOSED HYPERBOLIC THREE-MANIFOLDS 439
and the core geodesic ofC(T ) has cone angleα and length|λ|. The curveγ
is a meridian of the truncated tube.
Proof. We know thatC(T ) is isometric to a truncation ofX/Im ˜µ and we
apply the discussion of Section 14.2.4. □
We now look atM globally: every boundary torusTi ⊂ ∂N has its own
homomorphismsµ and ˜µ.
Corollary 14.2.9. Suppose that at every boundary torusTi⊂ ∂N one of
the following holds:
(1) µ is trivial, or
(2) there is a primitiveγi∈π1(Ti ) such that ˜µ(γi ) =eαii.
The completionM is a complete hyperbolic cone manifold obtained by Dehn
ﬁlling the slopesγi. The core of thei-th Dehn ﬁlling is a closed geodesic with
cone angleαi.
Theorem 14.2.3 now follows immediately.
Proof of 14.2.3. The equation ˜µ(mi )p ˜µ(li )q = e2πi implies that ˜µ(pmi +
qli ) = e2πi and therefore the completion is a hyperbolic manifold (with no
cone angles sinceα = 2π) diﬀeomorphic toMﬁll. □
14.2.7. Generalised Dehn ﬁlling invariants.We have proved Theorem
14.2.3 and we now make some comments that will be useful in the next chap-
ter. Letz be a solution of the consistency equations and consider a boundary
torusTi⊂∂N with ﬁxed generatorsmi,li forπ1(T ).
Proposition 14.2.10. Ifµ is non-trivial, there is a unique(p,q )∈ R2 such
that ˜µ(mi )p ˜µ(li )q =e2πi.
Proof. We know from Proposition 14.2.7 that˜µ is injective and has dis-
crete image. Therefore ˜µ(mi ) and ˜µ(li ) form a basis of~C∗ considered as a
R-vector space. □
We now deﬁne thegeneralised Dehn ﬁlling invariant(p,q )∈S2 = R2∪
{∞} of the solutionz at the torusTi to be:
• (p,q ) =∞ ifµ is trivial,
• the (p,q )∈ R2 from Proposition 14.2.10 ifµ is non-trivial.
If (p,q ) = ∞ there is a complete collarC(Ti ) of Ti that is a truncated
cusp; if (p,q )∈ R2 then Proposition 14.2.7 provides a nice incomplete collar
C(Ti ) and Proposition 14.2.8 tells us everything about its completionC(Ti ).
Namely, the following holds:
• if p
q∈ Q∪{∞} then (p,q ) =k(r,s ) for a unique real numberk >0
and coprime integers(r,s ), andC(Ti ) is a solid torus with meridian
rm +sl, isometric to a truncated tube with cone angle2π
k ;
440 14. HYPERBOLIC THREE-MANIFOLDS
• if p
q ⁄∈ Q∪{∞} then C(Ti ) is the much less interesting one-point
compactiﬁcation.
We deduce the following:
• if (p,q )are coprime integers thenC(Ti )is a standard truncated tube;
if this holds at all boundary toriTi thenM is a hyperbolic manifold;
• if (p,q ) are integers thenk is a natural number and the cone an-
gle divides 2π; if this holds at all boundary toriTi then M may be
interpreted as an orbifold thanks to Proposition 3.6.18;
• if p
q∈ Q∪{∞} at all boundary toriTi then M is a hyperbolic cone
manifold.
Corollary 14.2.11.If the generalised Dehn ﬁlling invariants(p,q ) at each
Ti are either∞or coprime integers, the completionM is a complete hyperbolic
manifold obtained by(p,q )-Dehn ﬁlling the cusps of the second type.
We end this discussion by calculating(p,q ) explicitly. We deﬁne
ui = log ˜µ(mi ), v i = log ˜µ(li )
and ﬁnd the following.
Proposition 14.2.12. Ifµ is non trivial we have
p =−2π ℜvi
ℑ( ¯uivi ), q = 2π ℜui
ℑ( ¯uivi ).
Proof. The pair(p,q ) is the unique solution of
(20) pui +qvi = 2πi
whenui,vi⁄= 0, or is∞ otherwise. Note thatui = 0⇔vi = 0. The relation
iℑ( ¯uiv ) =−(ℜvi )ui + (ℜui )vi
implies easily that the pair(p,q ) stated above is a solution to (20). □
14.2.8. Closed census. The Lickorish-Wallace Theorem 11.3.15 states
that every closed orientable three-manifoldM is the result of a Dehn surgery
along some linkL⊂S3, and as such it can be easily presented to SnapPea.
Theprogramtriestosolvenumericallytheconsistencyandcompletenessequa-
tions forM, based on some ideal triangulation for the complement ofL.
If it succeeds to ﬁnd a solutionz, the closed manifoldM is hyperbolic and
SnapPea calculates numerically various geometric invariants ofM: the volume
(which is just the sum of the volumes of the ideal tetrahedra), the length of
the core geodesics of the ﬁlling solid tori (using Proposition 14.2.8), a segment
of the geodesic spectrum, a Dirichlet domain, etc.
Various closed manifoldsM have been tested and listed, and the ten closed
hyperbolic three-manifolds of smallest volume known today are in Table 14.5,
taken from Hodgson – Weeks [28].
14.2. CLOSED HYPERBOLIC THREE-MANIFOLDS 441
Name Volume Homology Symmetry SG C
Vol1 0.94270736 Z5 + Z5 D12 0.5846 c
Vol2 0.98136883 Z5 D4 0.5780 c
Vol3 1.01494161 Z3 + Z6 S16 0.8314 a
Vol4 1.26370924 Z5 + Z5 D8 0.5750 c
Vol5 1.28448530 Z6 D4 0.4803 c
Vol6 1.39850888 {e} D4 0.3661 c
Vol7 1.41406104 Z6 D4 0.7941 c
Vol8 1.41406104 Z10 D4 0.3648 c
Vol9 1.42361190 Z35 D4 0.3523 c
Vol10 1.44069901 Z3 D4 0.3615 c
Table 14.5. The ten closed hyperbolic three-manifolds with smallest
volume known. HereS16 is the semidihedral group of order 16 with pre-
sentation⟨x,y |x 8 =y 2 = 1,y−1xy =x 3⟩, SG indicates the length of the
shortest geodesics (volume and SG values are truncated after few digits),
and C indicates whether the manifold is achiral (a) or chiral (c), that is
whether it admits an orientation-reversing isometry or not.
14.2.9. References. The material contained in this chapter originated
from Thurston’s notes [56] and Neumann – Zagier [42], see also Benedetti –
Petronio [4]. The program SnapPea is freely available and can now be used via
a Python interface [15]. We have used the computer censuses of Callahan –
Hildebrand – Weeks [10], Hoste – Thistlethwaite – Weeks [29], and Hodgson
– Weeks [28].
It is conjectured in [1] that each link in Figure 14.10 withc = 1,..., 5
cusps has minimum volume among orientable hyperbolic manifolds with c
cusps. This has been proved forc = 1 by Cao and Meyerhoﬀ [11], forc = 2 by
Agol [1], and forc = 4 by Yoshida [61]. The manifold Vol1 from Table 14.5 is
called theFomenko – Matveev – Weeks manifoldand has indeed smallest vol-
ume among all complete hyperbolic three-manifolds by Gabai – R. Meyerhoﬀ
– P. Milley [22].
CHAPTER 15
Hyperbolic Dehn ﬁlling
We have completely classiﬁed in Chapter 10 the closed three-manifolds
that belong to the six Seifert geometries, and now we long for a similar cata-
loguethatdisplaysalltheclosedhyperbolicthree-manifoldsthatexistinnature.
Is there something like a “name” to assign to each closed hyperbolic three-
manifold, together with some reasonable tables that list all possible names?
There is not yet one such thing, and we do not know if there will ever
be one: we still do not understand hyperbolic three-manifolds globally. The
main diﬃculty is that there are really many hyperbolic three-manifolds around,
so many that topologists often say informally that “most three-manifolds are
hyperbolic.”
This folk sentence is supported by a fundamental theorem that we prove
in this chapter, theHyperbolic Dehn ﬁlling Theorem, which says roughly that
by Dehn-ﬁlling generically a cusped hyperbolic three-manifold we still get a
hyperbolic manifold.
