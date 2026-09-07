---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-065-154-volumes
section_title: "Volumes"
section_number: 15.4
pages: 476-487
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
We have discovered that “most” Dehn ﬁllings of a cusped ﬁnite-volume
hyperbolic manifold are hyperbolic, and we now discuss their volumes.
Let M be a complete orientable ﬁnite-volume cusped hyperbolic three-
manifold. We say that a Dehn ﬁlling ofM is non-trivial if it ﬁlls at least one
boundarytorus; inotherwords, itisdeterminedbysomeDehnﬁllingparameter
s diﬀerent from(∞,..., ∞), after ﬁxing some arbitrary homology bases for
the boundary tori. We prove in this section the following theorem.
Theorem 15.4.1.If a non-trivial Dehn ﬁllingMﬁll ofM admits a complete
ﬁnite-volume hyperbolic metric, then
Vol(Mﬁll)< Vol(M).
If si is any sequence of non-trivial Dehn ﬁlling parameters converging to
(∞,..., ∞), andMi is the manifold obtained by ﬁllingM along si, thenMi
is eventually hyperbolic and
Vol(Mi )↗ Vol(M).
The cores of the ﬁlling solid tori are eventually simple closed geodesics and
their lengths tend to zero.
We already know that ifsi→ (∞,..., ∞) then Vol(Mi )→ Vol(M) and
the cores of the solid tori are closed geodesics whose length tend to zero:
this follows from the construction of the metric onMi via geometric ideal
triangulations. In some sense (that we will not make precise), the metric on
Mi converges to that ofM, and the core geodesics become so short that they
disappear in the limit opening the ﬁlling solid torus to a cusp.
The only new fact to prove is that the volume strictly decreases under
any Dehn ﬁllingMﬁll, not only those that are close to(∞,..., ∞): this is
rather subtle, because the hyperbolic metric onMﬁll might not be obtained by
completing ideal triangulations ofM. (For instance, the core tori inMﬁll may
not be isotopic to closed geodesics.)
15.4. VOLUMES 469
We prove the theorem as follows. We ﬁrst consider the case whereM has
an ideal geometric triangulationT: in that caseDef(M,T ) is a nice smooth
complex manifold and we investigate the volume function
Vol : Def(M,T )−→ R>0
that computes the volume of each hyperbolic structure onM. We show that
the volume function makes sense in a bigger convex set containingDef(M,T )
and is also easier to study there. This bigger convex set is the set ofangle
structures onT. We prove that the volume function is strictly concave there,
and the complete solution is a global maximum.
We conclude with a couple of ﬁnite-covering tricks to pass from local (near
(∞,..., ∞)) to global, and to deal with more general manifoldsM that do
not decompose into hyperbolic ideal tetrahedra.
15.4.1. Anglestructures. LetM = int(N)whereN isanorientablecom-
pact three-manifold bounded byc > 0 tori, equipped with an oriented ideal
triangulationT withn tetrahedra ∆1,..., ∆n andn edgese1,...,e n. We iden-
tify orientation-preservingly each∆i with the one shown in Figure 15.5, and
we label the edge pairs of type 1, 2, 3, with the numbersi,i +n, andi + 2n
respectively.
An angle structureθ on M is the assignment of anangle 0< θj < πto
thej-th edge pair inT, with the following requirements:
(1) at each tetrahedron∆i we haveθi +θi+n +θi+2n =π,
(2) at each edgeei, the sum of the incident angles is2π.
The set of angle structures is thus a subsetA⊂ R3n
>0. It is the intersection
of the aﬃne subspace inR3n determined by the conditions (1) and (2) with
the cone R3n
>0, so in particular it is convex. By deﬁnition this aﬃne subspace
is the solution space of the linear system
Aθ =
(π
2π
)
where A is the incidence 2n× 3n deﬁned in Section 15.2.2 and depicted in
Figure 15.6-(left), andθ = (θ1,...,θ 3n)∈ R3n.
What is the geometric meaning of an angle structureθ onT? Thanks
to condition (1), every∆i is realised by a unique ideal hyperbolic tetrahedron
with dihedral anglesθi,θi+n, andθi+2n whose complex modulus is
(31) zi = sinθi+n
sinθi+2n
eiθi.
Angle structures are then in natural 1-1 correspondence with the realisations
of the tetrahedra ∆1,..., ∆n as ideal hyperbolic tetrahedra, with the mild
condition (2) that their dihedral angles around each edgeei must sum to2π.
Condition (2) is only “half” of the consistency equation at eachei, which
requires the product of the complex moduli to be 1: condition (2) alone does
470 15. HYPERBOLIC DEHN FILLING
not guarantee that by gluing these tetrahedra we get a hyperbolic structure
onM: some “shearing” may arise when you turn around an edgeei.
With this geometric description, the deformation spaceDef(M,T ) is nat-
urally a smooth submanifold ofA.
15.4.2. Dimensions. We will henceforth suppose thatDef(M,T ) is non-
empty and contains a complete solutionz 0, that isT can be realised as a
geometric ideal triangulation. This implies in particular thatA is also non-
empty and has dimension dim kerA = 3n− (2n−c) = n +c by Corollary
15.2.8. The spaceDef(M,T ) is a real smooth submanifold of dimension2c.
The tangent spaceTθA at any pointθ∈A is of coursekerA. We now
construct an explicit set of generators forkerA. Recall from Section 15.2.6
that every simplicial closed oriented curveγ in a triangulated boundary torus
Ti deﬁnes an integer vectorvγ∈ R3n.
Recall the alternating formω on R3n from Section 15.2.3: we consider it
as a matrix and writev∗ = ωv for allv ∈ R3n, so thatω(v,w ) = ⟨v,w ∗⟩
where⟨,⟩ is the Euclidean scalar product. We denote byAi thei-th row ofA,
considered as a vector inR3n.
We ﬁx two arbitrary generatorsmi,li ofπ1(Ti ) for alli = 1,...,c .
Proposition 15.4.2. The tangent spaceTθA = kerA is generated by the
(not independent)n + 2c vectorsA∗
n+1,...,A ∗
2n,v∗
m1,v∗
l1,...,v ∗
mc,v∗
lc.
Proof. Propositions 15.2.9 and 15.2.14 say that the rows ofA are ω-
orthogonal to themselves and tovγ for anyγ, hence they are⟨,⟩-orthogonal
to all vectorsA∗
i andv∗
γ, in other wordsA∗
i,v∗
γ∈ kerA.
To prove that then + 2c listed vectors generatekerA it suﬃces to show
that they span a subspace of dimensionn +c. Proposition 15.2.15 says that
if we add the rowsvm1,...,v mc to A we get a rank-2n matrix. The same
proof shows that by further adding the rowsvl1,...,v lc we get a rank-(2n +c)
matrix.
The vectorsA1,...,A 2n,vm1,vl1,...,v mc,vlc span a dimension-(2n +c)
space. Since dim kerω =n, the vectorsA∗
1,...,A ∗
2n,v∗
m1,v∗
l1,...,v ∗
mc,v∗
lc span
a space of dimension at least2n +c−n =n +c. SinceA∗
1 =... =A∗
n = 0,
we are done. □
15.4.3. The volume function. The volume function onDef(M,T ) ex-
tends naturally to a function
Vol :A−→ R>0
which assigns to each angle structureθ the sum of the volumes of the ideal
hyperbolic realisations of ∆1,..., ∆n determined byθ. Recall from Section
13.1 that the volume of∆i is
Vol(∆i ) = Λ(θi ) + Λ(θi+n) + Λ(θi+2n)
15.4. VOLUMES 471
where Λ is the Lobachevsky function
Λ(α) =−
∫ α
0
log|2 sint|dt.
We therefore get a simple-looking formula
Vol(θ) =
3n∑
j=1
Λ(θj )
which implies immediately the following important fact.
Proposition 15.4.3. For everyθ∈A andv∈TθA we have
∂Vol
∂v =
3n∑
j=1
−vj log sinθj, ∂2Vol
∂v 2 < 0.
Proof. We consider a single addendumΛ(θj ) of Vol(θ). We have
∂Λ(θj )
∂v = Λ′(θj )∂θj
∂v =− log|2 sinθj|vj =−vj log 2−vj log sinθj.
Sincev∈TθA we havevi +vi+n +vi+2n = 0 for alli and hence∑
jvj sin 2 = 0.
This proves the ﬁrst equality. To estimate the second derivative, we may
suppose up to symmetries thatθi,θi+n< π
2 and we get
−∂2Vol(∆i )
∂v 2 =v 2
i cotθi +v 2
i+n cotθi+n +v 2
i+2n cotθi+2n
=v 2
i cotθi +v 2
i+n cotθi+n + (vi +vi+n)2 1− cotθi cotθi+n
cotθi + cotθi+n
= (vi +vi+n)2 + (vi cotθi−vi+n cotθi+n)2
cotθi + cotθi+n
> 0.
Indeed the denominator is positive sinceθi,θi+n < π
2, and if the numerator is
zero we getvi =−vi+n and hence cotθi =− cotθi+n, a contradiction. □
We have discovered thatVol is a smooth strictly concave function onA.
15.4.4. Thecompletesolution. Wenowrememberthat Def(M,T )con-
tains a complete solutionz 0 by assumption.
Proposition 15.4.4.The functionVol :A→ R>0 has a unique global max-
imum at the complete solutionz 0.
Proof. The complete solutionz 0 has an angle structureθ. Proposition
15.4.3 says that
∂Vol
∂v =
3n∑
j=1
−vj log sinθj
472 15. HYPERBOLIC DEHN FILLING
for all v ∈ TθA. At every edge ei, the consistency equation is of type∑
j logwj = 2πi where w1,...,w k are the moduli of the incident tetrahe-
dra. The imaginary part of this equation is satisﬁed at every point ofA, so
we look at the real part and using (31) we discover that
0 =ℜ
∑
j
logwj =
∑
j
log|wj| =
∑
j
(
log sinα1
j− log sinα2
j
)
where α1
j and α2
j are the other two angles in the tetrahedron with modulus
wj, in counterclockwise order. The latter expression is in fact equivalent to
−
3n∑
j=1
(A∗
n+i )j log sinθj = ∂Vol
∂A∗
n+i
which is hence zero for alli = 1,...,n .
We make some analogous considerations for the completeness equations.
Sincez 0 iscomplete, foreverysimplicialboundarycurve γ wehave ∑
j logwj =
|γ|πi wherew1,...,w k are the moduli encountered byγ at its right, and the
real part of this equation implies that∂Vol
∂v∗γ
= 0.
Proposition 15.4.2 shows that vectors of typeA∗
n+i andv∗
γ generateTθA,
hence the gradient of Vol vanishes atθ. Since Vol is strictly concave, this
critical point is the unique global maximum. □
Corollary 15.4.5. The space Def(M,T ) contains at most one complete
solution.
15.4.5. Volumes and Dehn ﬁlling.We can now prove Theorem 15.4.1
on manifolds having a geometric ideal triangulation. We start with a “local”
version which also considers generalised Dehn ﬁllings, see Section 15.1.1.
Lemma 15.4.6.IfM has a geometric ideal triangulation, there is a neigh-
bourhoodU of (∞,..., ∞) such thatVol(Mﬁll)< Vol(M) for every non-trivial
generalised Dehn ﬁlling parameters∈U. Moreover Vol(Mﬁll)↗ Vol(M) ass
tends to (∞,..., ∞).
Proof. The Dehn Filling Theorem 15.1.1 says that all Dehn ﬁllings in an
open neighbourhoodU of (∞,..., ∞) are hyperbolic and constructed by com-
pleting solutions inDef(M,T ), and they have smaller volume thanM in virtue
of Proposition 15.4.4. (The completion adds a circle toM which does not
contribute to the volume.)
The volume ofMﬁll depends smoothly ons∈U and has a global maximum
at (∞,..., ∞). In particular, when s → (∞,..., ∞) we get Vol(Mﬁll)→
Vol(M) from below. □
We now need to drop the open setU and prove that volume decreases
under any Dehn ﬁlling ofM.
15.4. VOLUMES 473
Lemma 15.4.7. Let M have a geometric ideal triangulation. If a non-
trivial Dehn ﬁllingMﬁll admits a complete ﬁnite-volume hyperbolic metric,
then Vol(Mﬁll)< Vol(M).
Proof. Lets = (s1,...,s c) be the Dehn ﬁlling parameter givingMﬁll and
letU be the open neighbourhood of(∞,..., ∞) furnished by Lemma 15.4.6.
For suﬃciently big integerk >0 we haveks∈U and henceMﬁll also admits a
hyperbolic metric with cone angles2π
k on the core geodesics of the ﬁlling solid
tori, with volume strictly smaller thanVol(M). We may interpret this metric
as a hyperbolic orbifoldO, and we haveVol(O)< Vol(M).
IfMﬁll is closed Proposition 13.3.8 givesVol(M)> Vol(O)>v3‖Mﬁll‖ =
Vol(Mﬁll) and we are done.
If Mﬁll is not closed, we can ﬁnd some closed ﬁllings ofMﬁll with vol-
ume arbitrarily close toVol(O) that can be interpreted as orbifolds, and get
Vol(O)> Vol(Mﬁll) as a limit. □
The proof of Lemma 15.4.7 shows also the following.
Lemma 15.4.8. Let M have a geometric ideal triangulation. We have
v3‖Mﬁll‖< Vol(M) for every closed Dehn ﬁllingMﬁll ofM.
We prove a lemma that will be useful below.
Lemma 15.4.9. Let M have a geometric ideal triangulation. IfMi is a
hyperbolic Dehn ﬁlling ofM with parametersi and Vol(Mi )→ Vol(M), then
si→ (∞,..., ∞).
Proof. We may suppose that theMi are closed, since every sequence of
Dehn ﬁllings can be approximated by a sequence of closed ones. Ifsi lies
deﬁnitely in the open setU furnished by Theorem 15.1.1, the assertion follows
because the volume function there hasVol(M) as a unique maximum (thanks
to Proposition 15.4.4).
Otherwise, there is a ﬁxed bigk ∈ N such that ksi ∈ U for alli, but
ksi does not converge to (∞,..., ∞). Therefore Mi admits a hyperbolic
orbifold structureOi with Vol(M)−ε> Vol(Oi ) and Proposition 13.3.8 gives
Vol(M)−ε> Vol(O)>v3‖Mi‖ = Vol(Mi ) for alli. □
Again, the proof shows also the following.
Lemma 15.4.10. Let M have a geometric ideal triangulation. If Mi is
a closed Dehn ﬁlling ofM with parametersi and v3‖Mi‖→ Vol(M), then
si→ (∞,..., ∞).
To conclude the proof of Theorem 15.4.1 we only need to consider the
unlucky case whereM has no geodesic ideal triangulations. We prove that
geometric triangulations exist on some ﬁnite cover ofM, and this will suﬃce.
474 15. HYPERBOLIC DEHN FILLING
15.4.6. Geometric triangulations exist virtually.We prove here the fol-
lowing.
Theorem 15.4.11.Every cusped complete ﬁnite-volume three-manifoldM
has a ﬁnite-sheeted cover˜M that has a geometric ideal triangulationT.
Proof. The Epstein-Penner decomposition subdividesM into ideal polyhe-
draP1,...,P k. If distinct vertices ofPi lie in distinct cusps ofM for alli, then
the decomposition can be easily subdivided into an ideal triangulation: we or-
der the cusps, so the vertices of eachPi inherit an ordering which is preserved
along the matching faces; we subdivide eachPi as in the proof of Proposition
15.3.2 by coning on the smallest vertex at each step: the triangulations on
the paired faces match and we get a geometric ideal triangulation forM itself.
We now show that some cover˜M has a decomposition of this type. The
decomposition ofM intoP1,...,P k lifts in any degree-d cover ˜M to a decom-
position of ˜M into Pi
1,...,P i
k with i = 1,...,d . We now prove that there is
a ˜M such that distinct vertices ofPi
j lie in distinct cusps, for alli,j .
To do so, we prove that for every pair of verticesv⁄=v′ of somePi there
is a covering where the lifts˜v, ˜v′ in Pj
i for somej lie in distinct cusps. This
is enough to conclude: pick aregular covering ˜M that covers all these ﬁnitely
many coverings; since its desk transformation group acts transitively on lifts,
all distinct vertices on everyPj
i lie in distinct cusps.
We haveM = H3/Γ. We ﬁx an arbitrary lift˜Pi⊂ H3 ofPi. Two vertices
v⁄=v′ ofPi lie in the same cuspT⇔ there is aγ∈ Γ such thatγ(˜v ) = ˜v′,
where ˜v, ˜v′∈ ˜Pi are the lifts ofv,v ′. The subgroup StabΓ(˜v ) = π1(T ) is
separable by Corollary 4.3.13 and hence there is a ﬁnite-indexH < Γ that
contains StabΓ(˜v ) but avoidsγ.
No element ϕ ∈ H is such that ϕ(˜v ) = ˜v′, otherwise we would have
γ−1ϕ∈ StabΓ(v ) < Hand hence γ ∈ H, a contradiction. We have con-
structed a ﬁnite-coverH3/H where in some liftPj
i ofPi the two lifted vertices
˜v, ˜v′ lie in distinct cusps. □
15.4.7. Conclusion of the proof.We can ﬁnally prove Theorem 15.4.1.
Proof of 15.4.1. Some degree-d cover ˜M ofM has an ideal geometric trian-
gulation, hence the theorem holds for˜M.
For every Dehn ﬁllingMﬁll of M, there is a Dehn ﬁlling˜Mﬁll of ˜M such
that the cover ˜M→M extends to a degree-d map ˜Mﬁll→Mﬁll.
IfMﬁll is closed hyperbolic, we have
dVol(M) = Vol( ˜M)>v 3‖( ˜Mﬁll)‖>dv 3‖Mﬁll‖ =dVol(Mﬁll)
using Lemma 15.4.8, henceVol(M)> Vol(Mﬁll).
If Mﬁll is cusped hyperbolic, it can be approximated by closed hyperbolic
ﬁllingsMﬁll
i , and there are closed ﬁllings˜Mﬁll
i of ˜Mﬁll with degree-d maps
15.4. VOLUMES 475
˜Mﬁll
i →Mﬁll
i . By Lemma 15.4.10 there is anε> 0 such that
Vol( ˜M)−ε>v 3‖ ˜Mﬁll
i ‖>dv 3‖Mﬁll
i ‖ =dVol(Mﬁll
i )
for alli, hencedVol(M)−ε = Vol( ˜M)−ε>dVol(Mﬁll). □
15.4.8. Boundedvolume. Howmanyhyperbolicmanifoldsaretherewith
bounded volume? In general, inﬁnitely many.
We have just discovered that there are inﬁnitely many hyperbolic manifolds
with volume smaller than 2v3 = 2.0298832128... because the ﬁgure-eight
knot complementM has Vol(M) = 2v3 and every hyperbolic Dehn ﬁlling ofM
has volume smaller thanVol(M). Moreover, the volumes of the Dehn ﬁllings
ofM form an indiscrete set that tends to2v3 from below.
Theorem 15.4.1 shows that this is the typical situation: the hyperbolic
Dehn ﬁlling produces inﬁnite sequences of manifolds with bounded volume.
Despite this variety of manifolds, we can still control topologically the hyper-
bolic manifolds having bounded volume, at least in principle.
Theorem 15.4.12. For every V > 0 there is a compact 3-manifold N
bounded by tori, such that every complete ﬁnite-volume orientable hyperbolic
3-manifoldM with Vol(M)<V is diﬀeomorphic to the interior of some Dehn
ﬁlling ofN.
Proof. This is a consequence of the thick-thin decomposition. Letε> 0
be a ﬁxed Margulis constant: every complete ﬁnite-volumeM decomposes
along disjoint embedded tori asM =Mthick∪Mthin where Mthick is compact
and has injectivity radius>ε , andMthin consists of truncated cusps and tube
neighbourhoods of short geodesics. In particularM is a Dehn ﬁlling ofMthick.
We now show that there are only ﬁnitely many possible diﬀeomorphism
types forMthick with volume<V . This concludes the proof: by Proposition
11.3.18 every such diﬀeomorphism type is realised from a linkL∪C⊂S3 by
surgerying alongL and drilling alongC; we take a disjoint union of all these
links inS3, and the complement of the resulting link inS3 is ourN.
Let X ⊂ Mthick be a maximal ε
2-net, that is a ﬁnite set of points that
stay at pairwise distance> ε
2, such that every other point inMthick stays
at distance< ε
2 from X (X exists becauseMthick is compact). The ε
4-balls
centred at the points inX are embedded and disjoint: henceX has cardinality
at mostC(V ) =V/ Vol
(
B(x, ε
4)
)
.
The set X determines a cellularisation ofMthick as follows. Lift X to
˜X⊂ H3, taketheVoronoitessellation(seeSection3.3.4)determinedby ˜X and
projectitbackto M: thisfurnishesasubdivisionof Mthick intopolyhedra. Since
X is maximal, every polyhedron has at mostC′(ε) faces withC′ depending
only onε. Hence there are ﬁnitely many combinatorial types of polyhedra,
depending only onε. With at mostC(V ) of them we obtain only ﬁnitely many
476 15. HYPERBOLIC DEHN FILLING
manifolds. (The proof of Proposition 11.1.6 applies to polyhedra and shows
that the combinatorial subdivision determines the smooth manifold.) □
15.4.9. Volumes of hyperbolic three-manifolds.We ﬁnish this chapter
by furnishing some qualitative information on the set of volumes of hyperbolic
three-manifolds. We start with the following.
Proposition 15.4.13. LetMi be a sequence of pairwise non-diﬀeomorphic
complete orientable hyperbolic three-manifolds of uniformly bounded volume.
After passing to a subsequence, we may suppose that there is a hyperbolic
manifold M such that eachMi is a Dehn ﬁlling ofM with parametersi →
(∞,..., ∞) .
Proof using geometrisation. We know from Theorem 15.4.12 that there
is a manifoldN such that eachMi is a Dehn ﬁlling ofN with parametersi.
After passing to a subsequence, we may suppose that at each boundary torus
Tj ofN the slopesi
j is either constant or goes to inﬁnity. LetM be obtained
fromN by Dehn ﬁlling the slopes that stay constant.
IfM is hyperbolic, we are done. Unfortunately, this may not be the case,
and we use geometrisation to solve this annoying possibility (the original proof
of Jørgensen and Thurston [56] does not need geometrisation and follows
from a discussion on the geometric convergence of hyperbolic manifolds: we
employ geometrisation only for simplicity). If M is not prime, it contains
some essential spheres that always bound balls in the ﬁlledMi and hence we
may cutM along them and cup oﬀ with balls (reducing the components of
∂M). Now M is prime and its geometric decomposition must contain some
hyperbolic block, otherwiseM would be a graph manifold and no Dehn ﬁlling
of M would be hyperbolic (it would be a graph manifold again). The tori
of the decomposition ofM become compressible inMi, so up to passing to
a subsequence we may suppose that eachMi is a Dehn ﬁlling of one ﬁxed
hyperbolic block ofM. Ifsi does not tend to(∞,..., ∞) in this new setting,
we restart from the beginning and proceed by induction on the number of
boundary components ofM. □
Corollary 15.4.14.The set of volumes of all complete orientable hyperbolic
three-manifolds is well-ordered. For every valueV there are only ﬁnitely many
such manifolds with volumeV.
Proof. Suppose that there is a sequence of manifoldsMi with Vol(M1)>
Vol(M2) > ... By the previous proposition these are all obtained by Dehn
ﬁlling the same hyperbolicM with si → (∞,..., ∞), and Theorem 15.4.1
says they should converge toVol(M) from below, a contradiction. The same
argument show that there are ﬁnitely many manifolds of any ﬁxed volume.□
We deduce that the volumes of all the complete orientable hyperbolic
three-manifoldsareindexedbycountableordinals. Thevolumes v1<v 2<...,
15.4. VOLUMES 477
Figure 15.14. The volumes of all the complete orientable hyperbolic
three-manifolds form a well-ordered subset ofR of typeωω.
of the smallest closed manifolds converge to the volumevω of the smallest
1-cusped manifold; the volumes vω < v2ω < ... of the smallest 1-cusped
manifolds converge to the volumevω2 of the smallest 2-cusped manifold, and
so on. The set of all volumes has order typeωω, see Figure 15.14.
We can also deduce the following.
Corollary 15.4.15.For everyV > 0 andR> 0 there are only ﬁnite many
closed hyperbolic three-manifoldsM with Vol(M)<V and inj(M)>R .
Proof. On a sequence of closed hyperbolic three-manifolds with bounded
volume, the length of some core geodesic tends to zero. □
15.4.10. References. To furnish a complete proof of Thurston’s Dehn
ﬁlling Theorem we have patched together a number of diﬀerent sources. The
most relevant ones are as usual Thurston’s notes [56], Benedetti – Petronio
[4], and Ratcliﬀe [49], together with Neumann – Zagier [42].
Some arguments have been updated here in light of some new results that
were discovered more recently by some authors. The list of non-exceptional
slopes for the ﬁgure-eight knot and the Whitehead link can be found in Martelli
– Petronio [38]. The smoothness of the deformation space stated in Corollary
15.2.13 has been proved by Choi [13] in 2004. Many of the arguments of this
chapter, including all the discussion on angle structures, have been taken from
a nice paper of Futer – Guéritaud [21]. The ﬁrst complete proof of Thurson’s
Dehn ﬁlling Theorem, that takes care of the annoying case of triangulations
withﬂattetrahedra,isduetoPetronio–Porti[ 48]. Wedivergefromthatproof
478 15. HYPERBOLIC DEHN FILLING
in the last arguments, where we extend Choi’s smoothness theorem to this
partially ﬂat context in Proposition 15.3.4 (this proposition is probably the only
original result of this book). The virtual existence of geometric triangulations
was proved by Luo – Schleimer – Tillmann [37] in 2008.
