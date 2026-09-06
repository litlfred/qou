---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-042-103-seifert-manifolds
section_title: "Seifert manifolds"
section_number: 10.3
pages: 320-339
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
Exercise 10.2.4. Prove this corollary using Proposition 9.1.4.
10.2.3. Closed circle bundles.We now turn to closed circle bundles. In
this section we prove that the oriented circle bundles over a closed surface are
parameterised by an integer called theEuler numberof the ﬁbering.
WeprefertoseethebundlesoverclosedsurfacesasDehnﬁllingsofbundles
over surfaces with boundary. Here are the details.
LetS be a compact surface with non-empty boundary. PickM =S×
(∼)
S1
and ﬁx an orientation forM. Recall that we denote byS the zero-section of
M. Every boundary componentT of M is an oriented torus, which contains
two natural unoriented simple closed curves: the boundarym =T∩∂S of the
sectionS and the ﬁbrel of the bundle. If oriented, the curvesm andl form a
basis (m,l ) forH1(T, Z). We choose orientations form andl such that(m,l )
form a positively oriented basis: there is a unique choice up to reversing both
m andl.
A Dehn ﬁlling onT is determined as usual by a pair(p,q ) of coprime
integers that indicate the slope±(pm +ql ) to be killed.
Suppose now thatS has only one boundary component and letMﬁll be
obtained by Dehn ﬁllingM along the slope(1,q ). Let ˆS be the closed surface
obtained by cappingS with a disc.
Proposition 10.2.5. The circle bundleM→S extends to a circle bundle
Mﬁll → ˆS. Every oriented circle bundle on ˆS is obtained in this way, and
distinct values ofq yield vector bundles that are not orientation-preservingly
isomorphic.
Proof. Themeridianoftheﬁllingsolidtorusis m′ =m+ql. Theﬁbrel has
geometric intersection 1 withm′ and is hence a longitude for the ﬁlling solid
torus. We may represent the ﬁlling solid torus asD×S1 withm′ =S1×{y}
and l ={x}× S1. The circle bundle M→ S extends naturally to a circle
bundleMﬁll→ ˆS with ˆS =S∪D.
Every closed circle bundleN→ ˆS arises in this way: the bundle above a
disc D⊂ ˆS is the trivialD×S1, and if we remove it we getM→ S back.
The numberq is intrinsically determined: the meridianm does not depend
on the section ofM→S by Corollary 10.2.3, and the equalitym′ =m +ql
determinesq. Therefore distinct values ofq yield non-isomorphic bundles. □
The integer q is the Euler number of the circle bundle and is usually
denoted with the lettere. We summarise our discovery:
Corollary 10.2.6. For everye∈ Z and every closed surfaceS there is a
unique oriented circle bundle overS with Euler numbere.
A change of orientation forM transforms e into−e. Recall that every
closed surfaceS has a trivial circle bundleS×
(∼)
S1 constructed by doubling the
unique oriented line bundle onS.
10.3. SEIFERT MANIFOLDS 313
Exercise 10.2.7. An oriented circle bundle over a closed surface is trivial
⇐⇒e = 0⇐⇒the bundle has a section.
We may see the Euler number of a bundleM→S over a closedS as an
obstruction for the existence of a section.
Remark 10.2.8. Every orientedn-dimensional vector bundleE→S over a
closed orientedn-manifoldS has aEuler numberdeﬁned by taking two generic
sections and counting their signed intersections. We brieﬂy explain how this
number is closely related to the one we deﬁned here.
Each vector bundleE→ S induces a sphere bundleM→ S: it suﬃces
to ﬁx a Riemannian metric onE and take the sub-bundle consisting of unit
tangent vectors. Whenn = 2 we get a circle bundleM→ S and the Euler
number ofE→S coincides with that ofM→S that we deﬁned above.
WhenE is the tangent bundle ofS, the Euler number is the Euler charac-
teristic χ(S). For instance, the unit tangent bundle ofS2 has Euler number
e =χ(S2) = 2 and hence it is diﬀeomorphic toL(2, 1) = RP3.
Exercise 10.2.9. LetM be a circle bundle over the genus-g surfaceSg with
Euler numbere. We haveH1(M, Z) = Z2g× Z/eZ.
Corollary 10.2.10.LetM→Sg andM′→Sg′ be circle bundles with Euler
numbers e and e′. The manifolds M and M′ are diﬀeomorphic⇐⇒g = g′
and|e| =|e′|.
Exercise 10.2.11. The circle bundleM over S2 with Euler numbere is
diﬀeomorphic to the lens spaceL(|e|, 1).
Hint. The base sphereS2 decomposes into two discs, and the ﬁbration
over each disc is a solid torus. ThereforeM is the union of two solid tori.□
We end the discussion by deﬁning explicitly a famous non-trivial circle
bundle overS2.
10.2.4. The Hopf ﬁbration.The quotient map
(C2)∗−→ CP1
(z,w )↦−→[z,w ]
restricts to a circle bundleS3→ CP1 = S2 called the Hopf ﬁbration. The
ﬁbre over[z,w ] is the circle(ωz,ωw ) asω∈S1 varies. See Figure 10.9.
Exercise 10.2.11 implies that the Euler number of the Hopf ﬁbrationS3→
S2 is±1, and hence it has no section by Exercise 10.2.7.
10.3. Seifert manifolds
We now enlarge the class of circle bundles over surfaces by admitting
some kind of singular ﬁbres. We introduce theSeifert ﬁbrations, whose total
314 10. SEIFERT MANIFOLDS
Figure 10.9. The ﬁbre of every point in the Hopf ﬁbrationS3→S2 is a
circle, and the counterimage of a circle inS2 is a torus inS3. The picture
shows the counterimage of three circle arcs: each is a portion of standard
torus inS3 = R3∪∞, foliated by circles of type(1, 1).
spaces are calledSeifert manifolds. These manifolds were introduced by Her-
bert Seifert in 1933 and ﬁt perfectly in the much more recent geometrisation
perspective: in the next chapter we will introduce the eight three-dimensional
geometries, and prove that six of them are realised precisely by the Seifert
manifolds.
10.3.1. Deﬁnition.We deﬁne the Seifert manifolds as Dehn ﬁllings of
trivial bundles over surfaces with boundary. Here are the details.
LetM be the (unique) oriented bundleS×
(∼)
S1 over a compact connected
(possibly non-orientable) surfaceS with boundary. We denote byS the zero-
section.
Let T1,...,T k be the boundary tori ofM. On each Ti we choose an
orientation for the meridianmi =Ti∩∂S and for the ﬁbreli of the bundle so
that the basis(mi,li ) forH1(Ti, Z) be positively oriented.
A (pi,qi )-Dehn ﬁlling onTi kills the slopepimi +qili. We say that the
Dehn ﬁlling isﬁbre-parallelifpi = 0, i.e. if it kills a ﬁbre.
Deﬁnition 10.3.1. ASeifert manifold is any 3-manifoldN obtained from
M by Dehn ﬁlling someh⩽k boundary tori in a non-ﬁbre-parallel way, that is
withpi⁄= 0 for alli.
10.3. SEIFERT MANIFOLDS 315
The Seifert manifold is closed ifh = k, and has k−h boundary tori
otherwise. It is not important to know whichh tori are ﬁlled, in virtue of the
following.
Proposition 10.3.2. Every permutation of the boundary tori is realised by
a self-diﬀeomorphism ofM that preserves the pairs±(mi,li ).
Proof. Every permutation of the boundary circles ofS is realised by a self-
diﬀeomorphism ofS, that extends orientation-preservingly to the orientable
I-bundle and its doubleM. □
The pair(pi,qi ) is determined up to sign, so we can always supposepi > 0
and we fully encode the Seifert manifoldN using the following notation:
(6) N =
( ˆS, (p1,q 1),..., (ph,qh)
)
where ˆS is S with h boundary components capped. The reason for usingˆS
instead ofS is thatN has a particular ﬁbration ontoˆS, as we will soon see.
Before constructing this ﬁbration we list some simple examples that should
hopefully help the reader to familiarise with the notation (6), that will be used
extensively in the whole chapter.
Example 10.3.3. The Seifert manifold
(
Sg, (1,e )
)
is the circle bundle over
the orientable genus-g surface Sg with Euler numbere, by construction. In
particular
(
Sg, (1, 0)
)
=Sg×S1.
Example 10.3.4. The Seifert manifold
(
S2, (p,q )
)
is diﬀeomorphic to the
lens spaceL(q,p ).
The following facts follow from Exercise 10.1.7.
Exercise 10.3.5. The Seifert manifold
(
D2, (p,q )
)
is a solid torus.
In the following exercise, it should be clear that the resulting manifold is
a lens space (by Exercise 10.1.7) and the hard part is to check carefully that
the proposed lens space parameters are correct.
Exercise 10.3.6. The Seifert manifold
(
S2, (p1,q 1), (p2,q 2)
)
is the lens
spaceL(p1q2 +q1p2,rq 2 +sp2) wherer,s are such thatp1s−q1r =±1. In
particular, this Seifert manifold isS3 whenp1q2 +q1p2 =±1.
10.3.2. Seifert ﬁbrations.As we anticipated, a Seifert manifoldN as in
(6) possesses some kind of singular ﬁbration over the ﬁlled surfaceˆS. We
clarify this point here by deﬁning the notion ofSeifert ﬁbration.
Let (p,q ) be two coprime integers withp >0. A standard ﬁbered solid
torus with coeﬃcients(p,q ) is the solid torus
D× [0, 1]/ψ
whereψ :D×0→D×1 is a rotation of angle2πq
p. The ﬁbration into vertical
segments{pt}× [0, 1] extends to a ﬁbration into circles of the solid torus. The
316 10. SEIFERT MANIFOLDS
Figure 10.10. A standard ﬁbered solid torus. We identify the top and
bottom discs by a2πq
p rotation, for someq coprime withp. Herep = 5.
Every non-central ﬁbre (green) windsp times along the central ﬁbre (red).
central ﬁbre obtained by identifying the endpoints of0× [0, 1] is the core of
the solid torus, and every non-central ﬁbre windsp times around the core of
M: see Figure 10.10.
The positive numberp is themultiplicity of the central ﬁbre. Ifp = 1 the
ﬁbered solid torus is diﬀeomorphic to the usual product ﬁbrationD×S1 and
the central ﬁbre isregular. Ifp> 1 the central ﬁbre issingular.
Deﬁnition10.3.7. ASeifertﬁbrationisapartitionofacompactoriented3-
manifoldN with (possibly empty) boundary into circles, such that every circle
has a ﬁbered neighbourhood diﬀeomorphic to a standard ﬁbered solid torus.
LetS be the topological space obtained fromN by quotienting circles to
points.
Proposition 10.3.8. The space S is a compact connected surface with
(possibly empty) boundary.
Proof. Every standard ﬁbered solid torus quotients to a disc: a sector
z = ρeiθ with 0 ⩽ ρ ⩽ 1 and 0 ⩽ θ ⩽ 2π
p with two edgesθ = 0 and
θ = 2π
p identiﬁed by a rotation. This disc actually looks like a “cone”, and this
motivates the following discussion. □
The mapN→S is in fact what we call a Seifert ﬁbration. The surfaceS
may have boundary and may be non-orientable, and its interior has a natural
orbifold structure: if the preimage ofx∈S is a ﬁbre of orderp, we seex as a
cone point of orderp, see Section 6.2.4. IfN has boundary, thenS also has,
and we say thatS itself is an orbifold for simplicity although we actually mean
only its interior. Morally, we should consider the ﬁbrationN→S as a circle
bundle over the orbifoldS.
10.3. SEIFERT MANIFOLDS 317
A Seifert ﬁbration without singular ﬁbres is just an ordinary circle bundle.
We now show that Seifert manifolds and Seifert ﬁbrations are more or less the
same thing.
Proposition 10.3.9. The Seifert manifold
N =
(
S, (p1,q 1),..., (ph,qh)
)
has a Seifert ﬁbrationN→S over the orbifold
(S,p 1,...,p h).
Every Seifert ﬁbration arises in this way.
Proof. The Seifert manifoldN is obtained by ﬁllingh components of a
bundle M = S′×
(∼)
S1. The bundle M → S′ extends to a Seifert ﬁbration
N→ S where the orbifoldS is obtained fromS′ by attachingh discs with
cone pointsp1,...,p h.
Moreprecisely, weﬁlleachboundarytorus Ti ofM withasolidtorushaving
meridianµi =pimi +qili. We ﬁx a longitudeλi =rimi +sili for this solid torus
by choosingri,si withpisi−qiri = 1. We getli =piλi−riµi. By hypothesis
the Dehn ﬁlling is not ﬁbre-parallel, hencepi⁄= 0 and the ﬁbrationM→ S′
extends to a standard ﬁbration of the solid torus with coeﬃcients(pi,−ri ).
Every Seifert ﬁbrationN→S arises in this way: if we remove the singular
ﬁbres (or a regular one, if there are not) we get an ordinary circle bundle over
a surface with boundary, which is trivial. ThereforeN is a Dehn ﬁlling of this
trivial bundle, hence a Seifert manifold. □
We have seen that the notation
(7) N =
(
S, (p1,q 1),..., (ph,qh)
)
deﬁnes a Seifert ﬁbrationN→S and a Seifert manifoldN.
Example 10.3.10. If the orbifoldS is a disc with at most one singular point
then N is a standard ﬁbered solid torus. IfS is S2 with at most 2 singular
points thenN is a lens space: see Exercises 10.3.5 and 10.3.6.
10.3.3. Classiﬁcation of Seifert ﬁbrations.We say that two Seifert ﬁ-
brationsπ1 :N1→S,π2 :N2→S areisomorphic if there is a diﬀeomorphism
ψ :N1→ N2 such thatπ1 = π2◦ψ. Two diﬀerent notations as in (7) may
describe isomorphic ﬁbrations, but this phenomenon is completely understood.
Proposition 10.3.11. Two notations as in (7) describe two orientation-
preservingly isomorphic Seifert ﬁbrations if and only if they are related by a
ﬁnite sequence of the following moves and their inverses:
(pi,qi ), (pi+1,qi+1)↦−→(pi,qi +pi ), (pi+1,qi+1−pi+1),(8)
(p1,q 1),..., (ph,qh)↦−→(p1,q 1),..., (ph,qh), (1, 0),(9)
(pi,qi )↦−→(pi,qi +pi ) if ∂N⁄= ∅,(10)
318 10. SEIFERT MANIFOLDS
and permutations of the pairs(pi,qi )’s.
Proof. Recall thatN is a Dehn ﬁlling ofM =S′×
(∼)
S1. Move (8) is the
result of twistingM along a ﬁbered annulusA connecting the toriTi andTi+1
in ∂M: this self-diﬀeomorphism ofM acts onTi and Ti+1 like two opposite
Dehn twists and extends to an isomorphism of the two ﬁbrations. In (10) we
twist along an annulus connectingTi and ∂N. The move (9) corresponds to
drilling a nonsingular ﬁbered torus and reﬁlling it back.
We now prove that these moves suﬃce to connect two isomorphic Seifert
ﬁbrations. Suppose that two distinct notations as in (7) describe isomorphic
ﬁbrations. We use the moves (8), (9), and (10) to eliminate the parameters
pi = 1 as much as possible from both notations. If there are no singular ﬁbres,
we end up with a single parameter(1,e ) ifS is closed, and no parameters at
all if∂S⁄= ∅. We conclude by Corollary 10.2.6.
If the ﬁbration has at least one singular ﬁbre, we can eliminate allpi = 1
and the(pi,qi ) correspond to singular ﬁbres. An isomorphism of Seifert ﬁbra-
tions sends singular ﬁbres to singular ﬁbres and hence induces an isomorphism
of their complement S′×
(∼)
S1. The parameters (pi,qi ) are determined by
the choice of a section inS′×
(∼)
S1. Diﬀerent sections are related by Dehn
twist along annuli and hence the parameters are related by the moves (8) and
(10). □
Proposition 10.3.11 classiﬁes all the Seifert ﬁbrations up to isomorphism.
A classiﬁcation of Seifert manifolds up todiﬀeomorphismwould also be de-
sirable, but it is much harder to obtain because a three-manifold may admit
many non-isomorphic Seifert ﬁbrations. For instance, Exercise 10.3.6 shows
that the lens spaces may ﬁbre in many diﬀerent ways; a manifold as familiar as
S3 ﬁbres over the orbifold(S2,p 1,p 2) ifp1 andp2 are coprime and hence has
inﬁnitely many non-isomorphic ﬁbrations. It is a stimulating exercise to try to
visualise these Seifert ﬁbrations ofS3.
We now start a long journey in Seifert manifolds theory, whose ultimate
goal is to classify them completely up to diﬀeomorphism. We will see at the
end that the only Seifert manifolds admitting non-isomorphic ﬁbrations are the
“smallest” ones, likeS3, the lens spaces, and few more that will be classiﬁed
using somead hocargument.
Exercise 10.3.12. The number of non-isomorphic Seifert ﬁbrations over a
ﬁxed orbifoldS is ﬁnite⇐⇒∂S⁄= ∅.
10.3.4. Euler number. We now extend the notion of Euler number from
ordinary to Seifert ﬁbrations. We deﬁne theEuler numberof the ﬁbration (7)
to be the rational number
e(N) =
h∑
i=1
qi
pi
.
10.3. SEIFERT MANIFOLDS 319
The Euler number is only deﬁned moduloZ whenN has boundary. The good
deﬁnition follows from Proposition 10.3.11 (the moves do not aﬀecte, except
(10) that modiﬁese intoe + 1 and applies only whenN has boundary) and is
coherent with the circle bundle case. The Euler number depends on the ﬁbra-
tion and not only onN, but we writee(N) anyway for simplicity. Proposition
10.3.11 easily implies the following.
Corollary 10.3.13.Two Seifert ﬁbrations
(
S, (p1,q 1),..., (ph,qh)
)
,
(
S′, (p′
1,q′
1),..., (p′
h′,q′
h′)
)
with pi,p′
i> 2 are orientation-preservingly isomorphic if and only ifS = S′,
h =h′,e =e′, and up to reorderingpi =p′
i andqi≡q′
i (modpi) for alli.
The numberse and e′ indicate the Euler numbers of the two ﬁbrations,
and recall that they are only deﬁned moduloZ when∂S⁄= ∅.
Remark 10.3.14. The move
(
S, (p1,q 1),..., (ph,qh)
)
↦−→
(
S, (p1,−q1),..., (ph,−qh)
)
corresponds to a change of orientation for the three-manifold and transforms
e into−e.
10.3.5. Homology. We now characterise the Seifert manifolds that have
ﬁnite homology groups, and in particular the homology spheres.
Proposition 10.3.15. The homology groupH1(M, Z) of
M =
(
S, (p1,q 1),..., (ph,qh)
)
is ﬁnite⇐⇒one of the following holds:
• S =S2 ande⁄= 0, and we get|H1(M, Z)| =|e|p1··· ph;
• S = RP2, and we get|H1(M, Z)| = 4p1··· ph.
Proof. IfM is not closed thenH1(M, Z) is inﬁnite becauseH1(∂M, Z) is.
If S⁄= S2, RP2 then H1(S) is inﬁnite. It is easy to check that the ﬁbration
M→S inducesasurjection H1(M)→H1(S)andhence H1(M)isalsoinﬁnite.
Suppose S = S2. The manifoldM is a (pi,qi )-Dehn ﬁlling ofS0,h×S1
whereS0,h is the sphere withh holes. The homology ofS0,h×S1 is generated
bym1,...,m h,l with the relationm1 +... +mh = 0. The i-th Dehn ﬁlling
adds the relationpimi +qili = 0. The relations form a square(h + 1)-matrix


1 p1 0 ··· 0
1 0 p2
... ...
... ... ... ... 0
1 0 0 ··· ph
0 q1 q2 ··· qh


∼


1 p1 0 ··· 0
1 0 p2
... ...
... ... ... ... 0
1 0 0 ··· ph
−e 0 0 ··· 0


.
320 10. SEIFERT MANIFOLDS
We have used Gauss moves to simplify the last row. The determinant of
this matrix is±ep1··· ph. The order|H1(M, Z)| is the absolute value of the
determinant if it is non-zero, and is inﬁnite if it is zero.
Suppose S = RP2 and letSno
1,h be RP2 with h holes. The homology of
Sno
1,h×∼ S1 is generated bya,m 1,...,m h,l , wherea is an orientation-reversing
curve inSno
1,h, with the relations2a +m1 +... +mh = 0 and 2l = 0. The
relations now form a square(h + 2)-matrix with determinant
det


2 0 0 ... 0
1 0 p1
... 0
... ... ... ... ...
1 0 0 ··· ph
0 2 q1 ··· qh


=±2 det


2 0 ··· 0
1 p1
... ...
... ... ... ...
1 0 ··· ph


=±4p1··· ph.
The proof is complete. □
We deduce an elegant description of all the Seifert homology spheres.
Corollary 10.3.16. For every setp1,...,p h of pairwise coprime integers
pi> 2 there is a unique homology sphereΣ(p1,...,p h) Seifert-ﬁbering over
(S2,p 1,...,p h). Every homology sphere Seifert manifold arises in this way.
Proof. By the previous proposition a Seifert manifold
M =
(
S, (p1,q 1),..., (ph,qh)
)
is a homology sphere if and only ifS =S2 and|ep1··· ph| = 1. We have
ep1··· ph =
h∑
i=1
qi
pi
p1··· ph =
h∑
i=1
qip1··· ˆpi··· ph =
h∑
i=1
qip′
i
where we setp′
i =p1··· ˆpi··· ph. The integersp1,...,p h arepairwise coprime
if and only ifp′
1,...,p ′
h are globally coprime (no prime number divides all of
them). The equation ∑
i=1qip′
i = 1 is satisﬁed by someq1,...,q h ⇐⇒
they are globally coprime. Diﬀerent solutionsqi are related by moves as in
Proposition 10.3.11 (exercise) and produce the same Seifert ﬁbration.□
For instance, the homology spheresΣ(p1) and Σ(p1,p 2) are justS3 by
Example 10.3.10. The simplest homology sphere with three singular ﬁbres
is Σ(2, 3, 5). This manifold is called thePoincaré homology sphereand we
will soon see that its fundamental group has order 120. All the other Seifert
homology spheres have inﬁnite fundamental group: this is related to the fact
that∑ 1
pi
> 1 for all choices of(p1,...,p h) with h> 3 except (2, 3, 5), as
we will soon see. A Seifert homology sphere of typeΣ(p1,p 2,p 3) is called a
Brieskorn homology sphere.
10.3. SEIFERT MANIFOLDS 321
10.3.6. Coverings. We now start to investigate the coverings of Seifert
ﬁbered spaces. Our main goal will be to subdivide the Seifert manifolds into
nine classes: this will be done in Section 10.3.9.
Like ordinary ﬁbrations, Seifert ﬁbrations behave well with respect to cov-
erings. Let M → S be a Seifert ﬁbration and˜M → M a covering. The
foliation into circles ofM lifts to a foliation into circles or lines in˜M, with
some quotient space ˜S.
Proposition 10.3.17. The quotient ˜S is an orbifold covering ofS.
• If ˜M foliates in circles then˜M→ ˜S is a Seifert ﬁbration,
• If ˜M foliates in lines then˜M→ ˜S is a line bundle.
In the second case˜S has no singular points.
Proof. This holds on all coverings of a standard ﬁbered solid torus and
hence holds everywhere. □
We now concentrate ourselves on the ﬁnite-degree case.
10.3.7. Finite-degree coverings. We deﬁne aﬁnite-degree coveringof
a Seifert ﬁbrationM→S to be a commutative diagram
˜M //

M

˜S //S
where ˜M→ ˜S is a Seifert ﬁbration,˜M→M is a ﬁnite-degree covering, and
˜S→S is an orbifold covering. Proposition 10.3.17 implies the following.
Corollary 10.3.18. Let M→S be a Seifert ﬁbration. Every ﬁnite-degree
covering ˜M→M induces a ﬁnite-degree covering of Seifert ﬁbrations:
˜M //

M

˜S //S
The dotted arrows indicate the maps that are induced. The degreed of
such a covering ˜M→M splits into two parts:
• the horizontal degreedh is the degree of the covering˜S→S,
• the vertical degree dv is the degree with which a regular ﬁbre of˜M
covers a regular ﬁbre ofM.
The vertical degree is well-deﬁned since regular ﬁbres in˜M form a connected
set. The pre-image of a regular ﬁbre inM consists ofdh regular ﬁbres in˜M,
each ﬁbering with degreedv. Therefore
d =dh·dv.
322 10. SEIFERT MANIFOLDS
A covering ˜M→M is horizontal or vertical if respectivelydv = 1 ordh = 1.
Proposition 10.3.19 (Pull-back).LetM→S be a Seifert ﬁbration. Every
ﬁnite-degreeorbifoldcovering ˜S→S isinducedbyauniquehorizontalcovering
of Seifert ﬁbrations:
˜M //

M

˜S //S
Proof. Like for ordinary bundles, there is a unique way to deﬁne˜M by
pulling back the Seifert ﬁbration on ﬁbered solid tori. □
Recall that an orbifold isvery goodwhen it is ﬁnitely covered by a surface.
Every locally orientable 2-orbifold is very good except the bad orbifoldsS2(p1)
andS2(p1,p 2) withp1⁄=p2, see Theorem 6.2.10 and Corollary 6.2.11.
Corollary 10.3.20. If S is good, every Seifert ﬁbrationM→ S is ﬁnitely
covered by a circle bundle over a surface.
Proof. Pull-back the ﬁbration along the surface cover˜S→S. □
Proposition 10.3.21. Every ﬁnite-degree covering between Seifert ﬁbra-
tions is a composition of one vertical and one horizontal covering.
Proof. Letp : ˜M→M be a covering of Seifert ﬁbrations, with base spaces
˜S→ S. If we pull-backM to ˜S we get a horizontal coveringph :Mh→ M.
There is a natural verticalpv : ˜M→Mh such thatp =ph◦pv. □
10.3.8. Circle bundle coverings.The Euler number of the ﬁbration and
the Euler characteristic of the base orbifold behave well with coverings.
Proposition 10.3.22.Letp : ˜M→M be a ﬁnite covering of closed Seifert
ﬁbrations with base orbifolds˜S andS, with degrees(dh,d v). We have
χ( ˜S) =dh·χ(S),
e( ˜M) = dh
dv
·e(M).
Proof. The ﬁrst equality holds for every orbifold covering˜S→ S. Con-
cerning the second one, by Proposition 10.3.21 we may supposep is either
vertical or horizontal. Write
M =
(
S, (p1,q 1),... (ph,qh)
)
and recall that M is obtained from a circle bundleN by (pi,qi )-ﬁlling the
boundary torusTi for alli = 1,...,h . Set ˜Ti =p−1(Ti ) and ˜N =p−1(N).
Ifp is vertical, we ﬁx a section of˜N and note that it projects to a section
ofN: these sections induce meridians on˜Ti andTi. Here ˜Ti is a single torus
10.3. SEIFERT MANIFOLDS 323
and ˜Ti→Ti wraps the ﬁbre with degreed =dv. Since the covering extends
to the ﬁlled solid tori, we haved|qi and ˜Ti is ﬁlled with parameters(pi,qi/d).
Thereforee( ˜M) =e(M)/d.
Ifp is horizontal, we ﬁx a section ofN, and its counterimage is a section
of ˜N: these sections induce meridians onTi and ˜Ti. Now ˜Ti consists of some
tori ˜Ti = ˜Ti,1⊔... ⊔ ˜Ti,ki and ˜Ti,j → Ti wraps the meridians with some
degree di,j. The total sum of these local degrees isdi,1 +... +di,ki = d =
dh. Similarly as above we havedi,j|pi and the ﬁlling solid torus at˜Ti,j has
parameters (pi/di,j,qi ). Therefore
e( ˜M) =
h∑
i=1
ki∑
j=1
di,jqi
pi
=
h∑
i=1
d·qi
pi
=d·e(M).
This concludes the proof. □
An important consequence is that the signs ofχ(S)ande(M)are invariant
under ﬁnite coverings.
10.3.9. Commensurability classes. We now would like to subdivide the
Seifert manifolds into few classes, and to this purpose we introduce a general
equivalence relation between manifolds.
Deﬁnition 10.3.23. Two manifoldsM and N are commensurable if there
is a manifold that covers bothM andN with ﬁnite degrees.
Proposition 10.3.24. Commensurability is an equivalence relation.
Proof. IfM is commensurable withN1 and N2, it has ﬁnite-sheeted cov-
erings M1,M 2 that coverN1 and N2 corresponding to ﬁnite-index subgroups
Γ1, Γ2 < π1(M). The subgroup Γ = Γ 1∩ Γ2 has also ﬁnite index and deter-
mines a manifold that covers bothN1 andN2. □
Exercise 10.3.25. There are three commensurable classes of closed sur-
faces, determined by their Euler characteristic being positive, null, or negative.
We now classify the commensurability classes of Seifert manifolds. The
3-torus is of courseT×S1 =S1×S1×S1.
Proposition 10.3.26. A closed Seifert ﬁbrationM→S has:
• χ(S)> 0 ande = 0⇐⇒M is covered byS2×S1,
• χ(S)> 0 ande⁄= 0⇐⇒M is covered byS3,
• χ(S) = 0 ande = 0⇐⇒M is covered by the 3-torus,
• χ(S) = 0 ande⁄= 0⇐⇒M is covered by a twisted bundle overT,
• χ(S)< 0 ande = 0⇐⇒M is covered bySg×S1 for someg> 1,
• χ(S)< 0 ande⁄= 0⇐⇒M is covered by a twisted bundle overSg
for someg> 1.
324 10. SEIFERT MANIFOLDS
χ> 0 χ = 0 χ< 0
e = 0 S2×S1 S1×S1×S1 S2×S1
e⁄= 0 S3 (
T, (1, 1)
) (
S2, (1, 1)
)
∂M⁄= ∅ D×S1 T× [0, 1] P×S1
Table 10.1. There are 9 commensurability classes of Seifert manifolds:
6 closed and 3 with boundary. Every Seifert manifoldM is commensurable
with one (and only one) of these 9 manifolds. The commensurability class
ofM is easily detected by looking at its invariantsχ ande (the latter only
in the closed case). The surfacesT,S 2,D,P are the torus, the genus-2
surface, the disc, and the pair-of-pants. Note thatS3 =
(
S2, (1, 1)
)
.
Proof. IfS is a bad orbifold, thenS =S2(p) orS2(p1,p 2) with p1⁄=p2
and hence we gete⁄= 0 and χ(S) > 0. The manifoldM is a lens space by
Example 10.3.10 and is hence covered byS3.
IfS is good, the ﬁbrationM→S is covered by a circle bundle˜M→ ˜S over
anorientableclosedsurface ˜S byCorollary10.3.20. ByProposition10.3.22the
numbers χ( ˜S) and e( ˜M) have the same signs ofχ(S) and e(M). Therefore
˜S = S2,T , orSg with g > 1, depending on whetherχ(S) is positive, null,
or negative. Exercise 10.2.7 says that the circle bundle ˜M → ˜S is trivial
⇐⇒e( ˜M) = 0 ⇐⇒e(M) = 0 . Note that a non-trivial bundle overS2 is a
lens spaceL(e, 1) withe⁄= 0 and is hence covered byS3.
We have proved thatM is covered (according to the signs ofχ ande) by a
manifold belonging to one of the six types:S3,S2×S1, the 3-torus, a twisted
bundle overT, Sg×S1, and a twisted bundle overSg. It remains to prove
thatM cannot be covered by two manifoldsM1,M 2 belonging to two diﬀerent
types: this holds because manifolds of distinct types are not commensurable.
To prove that, note that the ﬁnite cover of a manifold of one of the six types
is a manifold of the same type, and Corollary 10.2.10 implies that a manifold
cannot belong to two diﬀerent types. If two manifolds of distinct types were
commensurable they would be covered by a manifold belonging to both types,
yielding a contradiction. □
We can now easily classify all closed Seifert manifolds up to commensura-
bility. To conclude we just need to solve the following exercise.
Exercise 10.3.27. PickS =Sg ande >0. Construct:
• a degree-e vertical covering
(
S, (1, 1)
)
→
(
S, (1,e )
)
,
• a degree-e horizontal covering
( ˜S, (1,e )
)
→
(
S, (1, 1)
)
ifg> 1.
Hint. Ifg> 1 thenS has covers of any degreee. To construct them, pick
surjective homomorphismsπ1(S)→H1(S)→ Z/eZ. □
10.3. SEIFERT MANIFOLDS 325
Corollary 10.3.28.There are six commensurability classes of closed Seifert
manifolds, depending onχ ande as shown in Table 10.1.
Proof. By the previous exercise the non-trivial (or trivial) bundles over
closed surfaces withχ< 0 (orχ = 0,χ> 0) are all commensurable. □
Corollary 10.3.29. A closed Seifert ﬁbrationM→S has e = 0⇐⇒it is
ﬁnitely covered by a trivial circle bundle.
We recall that a Seifert manifoldM may have non-isomorphic Seifert ﬁ-
brations M→ S and M→ S′, and the invariantsχ,χ′ and e,e′ of the two
ﬁbrations are not necessarily equal; howeverχ is positive, null, or negative if
and only ifχ′ is, ande vanishes if and only ife′ does (in the closed case).
This holds because the commensurability class ofM does not depend on its
ﬁbration. For instance, Exercise 10.3.6 shows that a lens spaceM =L(p,q )
withp> 0 has many ﬁbrations, but each withχ> 0 ande⁄= 0.
Wenowconsidertheboundarycase, whichissimplerbecausecirclebundles
over orientable surfaces with boundary are always trivial. LetA denote the
annulus andSg,b be the surface of genusg withb open discs removed.
Proposition 10.3.30. A Seifert ﬁbrationM→S with boundary has
• χ(S)> 0⇐⇒M =D×S1,
• χ(S) = 0⇐⇒M is covered byA×S1 =T× [0, 1],
• χ(S)< 0⇐⇒M is covered bySg,b×S1 for someg +b> 2.
Proof. Every Seifert manifold with boundary is covered by a circle bundle
over an orientable surface, and such a bundle is trivial here. Ifχ > 0 the
base surface is a disc with at most one cone point and henceM is a standard
ﬁbered solid torus. □
Corollary 10.3.31. There are three commensurability classes of Seifert
manifolds with boundary, depending onχ as shown in Table 10.1.
Proof. Thesurfaces Sg,b withg+b> 2arecommensurable(exercise). □
We now characterise some commensurability classes by looking at the
fundamental groups.
10.3.10. Virtually abelian fundamental groups.A groupG is virtually
abelian of rankh if it containsZh as a ﬁnite-index subgroup.
This is a ﬁnite-index-independent property: ifG′ < G has ﬁnite index,
the group G′ is virtually abelian of rankh if and only ifG is. Therefore a
manifold M has a virtually abelian fundamental group of rankh⇐⇒ every
manifoldN commensurable withM also has⇐⇒there is a manifoldN in the
commensurability class withπ1(N) = Zh.
Proposition 10.3.32. There are ﬁve commensurability classes of Seifert
manifolds with virtually abelian fundamental groups, shown in Table 10.2.
326 10. SEIFERT MANIFOLDS
χ> 0 χ = 0 χ< 0
e = 0 Z Z 3
e⁄= 0 {e}
∂M⁄= ∅ Z Z 2
Table 10.2. There are ﬁve Seifert manifoldsM with π1(M) = Zh and
they belong to distinct commensurability classes. The fundamental group
π1(N) of every other manifoldN in these ﬁve classes is virtually abelian:
it contains Zh as a ﬁnite-index subgroup.
Proof. These ﬁve classes containS2×S1, S1×S1×S1, S3, D×S1,
andA×S1. The remaining four classes do not contain manifolds with abelian
fundamental group: every manifold in these classes is covered by someS×S1
with χ(S)< 0 or
(
Sg, (1,e )
)
with g> 1 and e> 1 (use Exercise 10.3.27).
The fundamental group of such manifolds is notZh: the former becauseπ1(S)
is not abelian, and the latter because its abelianization contains torsion, see
Exercise 10.2.9. □
Itcouldbereasonabletoexpecttheseﬁvecommensurabilityclassestocon-
tain manifolds of some simpler topological nature, which are easier to study
and classify. We will see however in Section 10.4.7 that the Seifert mani-
folds covered byS3 are quite interesting and their topological classiﬁcation is
certainly not immediate: we already experienced that for lens spaces in The-
orem 10.1.12, whose classiﬁcation is quite involved. The other four classes
are indeed of a simpler nature: we now prove that each contains ﬁnitely many
manifolds, and we classify them completely.
10.3.11. Finite commensurability classes.We now completely identify
the commensurability classes of Seifert manifolds that contain only ﬁnitely
many manifolds.
We start by considering manifoldsM with boundary. We have already
seen that the classχ> 0 contains only the solid torus. The classχ = 0 also
contains few manifolds:
Proposition 10.3.33. Every Seifert ﬁbration with boundary andχ = 0 is
isomorphic to one of the following:
A×S1, S ×∼ S1,
(
D, (2, 1), (2,−1)
)
.
The Seifert manifold is correspondingly diﬀeomorphic to the interval bundles
T×I,K×∼ I, andK×∼ I again. HereA,S, andK are the annulus, the Möbius
strip, and the Klein bottle.
Proof. The orbifolds with boundary andχ = 0 are A, S, and (D, 2, 2).
Every Seifert ﬁbration over(D, 2, 2) is isomorphic to
(
D, (2, 2n + 1), (2, 2m +
10.3. SEIFERT MANIFOLDS 327
Figure 10.11. Draw the orientable line bundle over the Klein bottle as
S1× [−1, 1]× [−1, 1]/ψ where ψ identiﬁes the lower and upper (yellow)
annuliS1×[−1, 1]×{±1}by gluing(eiθ,t )to (e−iθ,−t). The Klein bottle
is drawn in green (left). This manifold has two ﬁbrations: a horizontal one
with ﬁbresS1×x×y and base surface the green Möbius strip (centre),
and a vertical one with ﬁbresx×y× [−1, 1] and base surface the green
disc with two cone points of order two (the green annulus becomes a disc
after identifying the points(eiθ, 0) and (e−iθ, 0)). The two singular ﬁbres
of order two lie above(±1, 0) and are drawn in red (right).
1)
)
and does not depend onn,m ∈ Z by Proposition 10.3.11. Hence there
is only one Seifert ﬁbration over the orbifold(D, 2, 2), which we write as(
D, (2, 1), (2,−1)
)
only for aesthetic reasons (to gete = 0).
We get three manifolds and we now prove that they are all diﬀeomorphic
to some interval bundle. The diﬀeomorphismA×S1 ∼= T×I is obvious.
DrawK×∼ I asS1× [−1, 1]× [−1, 1]/ψ as in Figure 10.11. The manifold has
two ﬁbrations: a horizontal one by circlesS1×x×y, and a vertical one by
segments x×y× [−1, 1]. The horizontal one givesS×∼ S1 and the vertical
one closes to a Seifert ﬁbration over the disc with two singular ﬁbres of order
two, and hence is(D, (2, 1), (2,−1)). □
Corollary 10.3.34. Every Seifert manifold with boundary andχ > 0 is
diﬀeomorphic toD×S1,T×I, orK×∼ I.
We now turn to closed Seifert manifolds. We have seen thatK×∼ I ﬁbres
in two non-isomorphic ways, and this has some consequences.
Corollary 10.3.35.The following diﬀeomorphisms hold:
(
S2, (2, 1), (2,−1), (p,q )
)∼=
(
RP2, (q,p )
)
,
(
S2, (2, 1), (2, 1), (2,−1), (2,−1)
)∼=K×∼ S1.
Proof. Both equalities follow from
(
D, (2, 1), (2,−1)
)∼=S×∼ S1. In the
ﬁrst we look at Figure 10.11 to check that a(p,q )curve in
(
D, (2, 1), (2,−1)
)
328 10. SEIFERT MANIFOLDS
M H1(M, Z)
T×S1 Z3
K×∼ S1 Z× Z/2Z× Z/2Z(
S2, (2, 1), (2, 1), (2,−1), (2,−1)
)
Z× Z/2Z× Z/2Z(
S2, (3, 1), (3, 1), (3,−2)
)
Z× Z/3Z(
S2, (2, 1), (4,−1), (4,−1)
)
Z× Z/2Z(
S2, (2, 1), (3, 1), (6,−5)
)
Z(
RP2, (2, 1), (2,−1)
)
Z/4Z× Z/4Z
Table 10.3. The seven closed Seifert ﬁbrations withχ = 0 and e = 0.
Two of these manifolds are actually diﬀeomorphic, so we get six closed
Seifert manifolds up to diﬀeomorphism, distinguished by their homology.
becomes a(q,p )curve inS×∼ S1. The second equality is obtained by doubling
the line bundleK×∼ I. □
We want to classify the closed Seifert manifolds withχ> 0 and e = 0.
We start with the caseχ> 0.
Proposition 10.3.36. Every closed Seifert ﬁbration withχ> 0 and e = 0
is isomorphic to one of the following:
S2×S1, RP2×∼ S1,
(
S2, (p,q ), (p,−q)
)
.
The manifolds of the last type are all diﬀeomorphic toS2×S1.
Proof. If the base surfaceS is a sphere with⩽ 2 singular ﬁbres, we use
Exercise 10.3.6. OtherwiseS is one of the following orbifolds (see Table 6.1):
(S2, 2, 2,p ), (S2, 2, 3, 3), (S2, 2, 3, 4), (S2, 2, 3, 5), RP2, (RP2,p )
with p> 2. In all cases except RP2, we gete⁄= 0 for any choice of Dehn
ﬁlling parameters: for instance
e
(
S2, (2,q 1), (2,q 2), (p,q 3)
)
= q1 +q2
2 +q3
p ⁄= 0.
The other cases are analogous. □
The manifold RP2×∼ S1 is not diﬀeomorphic toS2×S1, because they
have non-isomorphic fundamental groups. Moreover,RP2×∼ S1 is not prime:
Exercise 10.3.37. The two manifoldsRP2×∼ S1 and RP3#RP3 are diﬀeo-
morphic.
We will soon see thatRP2×∼ S1 is the unique non-prime Seifert manifold.
We now turn to theχ = 0 case.
10.3. SEIFERT MANIFOLDS 329
χ> 0 χ = 0 χ< 0
e = 0 2 6 ∞
e⁄= 0 ∞ ∞ ∞
∂M⁄= ∅ 1 2 ∞
Table 10.4. The number of Seifert manifolds in each commensurability class.
χ> 0 χ = 0 χ< 0
e = 0 S2× R R 3 R3
e⁄= 0 S3 R3 R3
Table 10.5. The universal cover of a closed Seifert manifold depends
on its invariantse andχ.
Proposition 10.3.38. Every closed Seifert ﬁbration withχ = 0 and e = 0
is isomorphic to one of the seven listed in Table 10.3. These seven manifolds
are all pairwise non-diﬀeomorphic, except
(
S2, (2, 1), (2, 1), (2,−1), (2,−1)
)∼=K×∼ S1.
Proof. The closed orbifolds withχ = 0 are
T, K, (RP2, 2, 2), (S2, 2, 2, 2, 2), (S2, 2, 3, 6), (S2, 3, 3, 3), (S2, 2, 4, 4).
It is easy to show that by imposinge = 0 we get the ﬁbrations listed. The ho-
mology calculation is an easy exercise and luckily distinguishes all the manifolds
except (of course) the two diﬀeomorphic ones (see Corollary 10.3.35).□
Summing up, there are four commensurability classes containing ﬁnitely
many manifolds, and their number is shown in Table 10.4.
10.3.12. Universal cover. We now determine the universal cover of all
the closed Seifert manifolds. Nothing strange happens: we either get S3,
S2× R, or R3.
Proposition 10.3.39. The universal cover of a closed Seifert manifold is
shown in Table 10.5.
Proof. The universal cover of a circle bundle over a surfaceS withχ(S)⩽
0 is a line bundle over the universal coverR2 of S. The line bundle is trivial
since R2 is contractible and we getR2× R = R3. □
Corollary 10.3.40.Every Seifert manifoldM is either irreducible or covered
byS2× R. In the latter caseM is diﬀeomorphic toS2×S1 or RP2×∼ S1.
330 10. SEIFERT MANIFOLDS
Proof. If the universal cover isS3 or R3, it is irreducible and hence alsoM
is. When M has boundary, we apply the proof of Proposition 10.3.39 to the
interior ofM and ﬁnd that its universal cover isR3. □
Therefore every Seifert manifold is prime exceptRP2×∼ S1 = RP3#RP3.
10.3.13. Fibre-Parallel Dehn ﬁlling.We have investigated various topo-
logical properties of Seifert manifolds, and we are now curious: what happens
if we perform a forbidden ﬁbre-parallel Dehn ﬁlling? We start by looking at
the basic blockP×S1, whereP is a pair-of-pants.
Proposition 10.3.41. A ﬁbre-parallel Dehn ﬁlling onP×S1 produces the
connected sum of two solid tori; the ﬁbres ofP×S1 become the meridians of
the solid tori.
Proof. Letγ⊂∂P be the component whose torusγ×S1 is ﬁlled. Pick an
essential arcα inP with both endpoints inγ: the ﬁbered annulusA =α×S1
closes up to a two-sphereS in the Dehn ﬁlling.
The sphereS separates the ﬁlled manifold into two portions, each diﬀeo-
morphic toT× [0, 1] with a two-handle attached along a non-trivial curve:
this is a holed solid torus. Every ﬁbre now bounds a disc there. □
We now turn to arbitrary bundles.
Exercise 10.3.42. LetS be a compact surface withb> 1 boundary com-
ponents. The ﬁbre-parallel Dehn ﬁlling ofS×∼ S1 is diﬀeomorphic to the
connected sum ofb− 1 solid tori and−χ(S) + 2−b copies ofS2×S1.
Wenowdeduceamoregeneralfact: aﬁbre-parallelDehnﬁllingofaSeifert
manifold is a connected sum of lens spaces and solid tori.
Corollary 10.3.43.The ﬁber-parallel Dehn ﬁlling of
(
S, (p1,q 1),..., (ph,qh)
)
is diﬀeomorphic to the connected sum
L(p1,q 1)#... #L(ph,qh)#k(S2×S1)#b−1(D2×S1)
whereS hasb boundary components andk =−χ(S) + 2−b.
IfS is orientable thenk is twice the genus ofS.
Corollary 10.3.44.Every Dehn ﬁlling of a Seifert manifold is a connected
sum of Seifert manifolds.
If we have a Seifert manifoldM with many boundary components and we
Dehn ﬁll some of them, we are guaranteed to produce a new Seifert manifold,
unless one of the Dehn ﬁlling kills a ﬁber-parallel slope: in that case the
manifold “degenerates” to a connected sum of lens spaces and solid tori. This
is an interesting phenomenon to keep in mind, because it will reproduce in
