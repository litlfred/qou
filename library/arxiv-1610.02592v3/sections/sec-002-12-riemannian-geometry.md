---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-002-12-riemannian-geometry
section_title: "Riemannian geometry"
section_number: 1.2
pages: 23-31
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
M M'
M#M'
Figure 1.3. A connected sum of closed surfaces.
ϕ:N→∂Dn. By cuttingM along N we get two new boundary components
diﬀeomorphic toN and we glue two discs to them via the mapϕ. We get two
manifoldsN1,N 2 such thatM =N1#N2.
1.1.14. Transversality. Letf :M→N be a smooth map between man-
ifolds andX⊂N be a submanifold. We say thatf is transverse to X if for
anyp∈f−1X the following condition holds:
Im (dfp) +Tf (p)X =Tf (p)N.
The maps transverse to a ﬁxedX are generic, that is they form an open dense
subset in the space of all smooth maps fromX to Y, with respect to an
appropriate topology. In particular the following holds.
Theorem 1.1.17. Let f :M→ N be a continuous map andd a distance
on N compatible with the topology ofN. For everyε> 0 there is a smooth
mapg transverse toX, homotopic tof, withd(f (p),g (p))<ε for allp∈M.
1.2. Riemannian geometry
We brieﬂy introduce Riemannian manifolds and their geometric properties:
distance, geodesics, volume, exponential map, injectivity radius, completeness,
curvature, and isometries. These notions are carefully explained in do Carmo’s
Riemannian Geometry [16].
1.2.1. Metric tensor. A diﬀerentiable manifold lacks many natural geo-
metric notions, such as distance between points, angle between vectors, path
lengths, geodesics, volumes, etc. It is a quite remarkable fact that the intro-
duction of a single additional mathematical entity suﬃces to recover all these
geometric notions: this miraculous object is the metric tensor.
A metric tensor for a diﬀerentiable manifoldM is the datum of a scalar
product on each tangent spaceTp of M, which varies smoothly onp. More
speciﬁcally, on a chart the scalar product may be expressed as a matrix, and
we require that its coeﬃcients vary smoothly onp.
16 1. PRELIMINARIES
Deﬁnition 1.2.1. ARiemannian manifold is a diﬀerentiable manifold with
a metric tensor that is positive deﬁnite at every point.
A Riemannian manifold is usually denoted as a pair(M,g ), whereM is the
manifold andg is the metric tensor.
Example 1.2.2. TheEuclidean spaceis the manifoldRn equipped with the
Euclidean metric tensorg(x,y ) =∑n
i=1xiyi at every tangent spaceTp = Rn.
Example 1.2.3. Every diﬀerential submanifoldN in a Riemannian manifold
M is also Riemannian: it suﬃces to restrict at everyp∈N the metric tensor
onTpM to the linear subspaceTpN.
In particular, thesphere
Sn =
{
x∈ Rn+1⏐⏐‖x‖ = 1
}
is a submanifold ofRn+1 and is hence Riemannian.
The metric tensorg deﬁnes in particular a norm for every tangent vector,
and an angle between tangent vectors with the same basepoint. The velocity
γ′(t) of a curveγ :I→M at timet∈I now has a norm‖γ′(t)‖> 0 called
speed, and two curves that meet at a point with non-zero velocities form a
well-deﬁned angle. Thelength ofγ may be deﬁned as
L(γ) =
∫
I
‖γ′(t)‖dt
and can be ﬁnite or inﬁnite. Areparametrisation ofγ is the curveη :J→M
obtained asη =γ◦ϕ where ϕ:J→I is a diﬀeomorphism of intervals. The
length is invariant under reparametrisations, that isL(γ) =L(η).
1.2.2. Distance and geodesics.Let (M,g ) be a connected Riemannian
manifold. The curves inM now have a length and hence may be used to deﬁne
a distance onM.
Deﬁnition 1.2.4. Thedistance d(p,q ) between two pointsp,q ∈M is
d(p,q ) = inf
γ
L(γ)
whereγ varies among all curvesγ : [0, 1]→M withγ(0) =p andγ(1) =q.
Themanifold M equippedwiththedistance d isametricspace(compatible
with the initial topology ofM).
Deﬁnition 1.2.5. Ageodesic is a curveγ :I→M having constant speed
k that realises locally the distance. This means that everyt∈I has a closed
neighbourhood [t0,t 1]⊂I suchthat d(γ(t0),γ (t1)) =L(γ|[t0,t1]) =k(t1−t0).
Note that with this deﬁnition the constant curveγ(t) = p0 is a geodesic
with constant speedk = 0. Such a geodesic is calledtrivial. A curve that
realises the distance locally may not realise it globally.
1.2. RIEMANNIAN GEOMETRY 17
Example 1.2.6. The non-trivial geodesics in Euclidean spaceRn are aﬃne
lines run at constant speed. The non-trivial geodesics in the sphereSn are
portions of great circles, run at constant speed.
A geodesicγ :I→M is maximal if it cannot be extended to a geodesic
on a strictly larger intervalJ⊃I. Maximal geodesics are determined by some
ﬁrst-order conditions:
Theorem 1.2.7. Let p∈ M be a point andv ∈ TpM a tangent vector.
There exists a unique maximal geodesicγ :I→M withγ(0) =p andγ′(0) =
v. The intervalI is open and contains0.
1.2.3. Volume. If the diﬀerentiable manifoldM is oriented, the metric
tensor also induces avolume form.
The best method to deﬁne volumes on an-manifoldM is to construct an
appropriaten-form. An-formω is an alternating multilinear form
ωp :Tp×... ×Tp| {z }
n
−→ R
at each pointp∈M, which varies smoothly withp. The alternating condition
means that if we swap two vectors the result changes by a sign. Then-forms
are designed to be integrated: it makes sense to write∫
D
ω
on any open setD. A volume form on an oriented manifoldM is an-form
ω such thatωp(v1,...,v n) > 0 for every positive basisv1,...,v n of Tp and
everyp∈M.
The metric tensor deﬁnes a volume form as follows: it suﬃces to set
ωp(e1,...,e n) = 1 on every positive orthonormal basise1,...,e n. With this
deﬁnition every open setD ofM has a well-deﬁnedvolume
Vol(D) =
∫
D
ω
which is a positive number or inﬁnity. IfD has compact closure the volume is
necessarily ﬁnite; in particular, a compact Riemannian manifoldM has ﬁnite
volume Vol(M).
On a chart, the volume form can be calculated from the metric tensorg
via the following formula:
ω =
√
detg·dx 1··· dxn.
1.2.4. Completeness. A Riemannian manifold(M,g ) is a metric space,
and as such it may be complete or not. For instance, a compact Riemannian
manifold is always complete; on the other hand, by removing a point from
a Riemannian manifold we always get a non-complete space. Non-compact
manifolds likeRn typically admit both complete and non-complete Riemannian
18 1. PRELIMINARIES
structures. The completeness of a Riemannian manifold may be expressed in
various ways:
Theorem 1.2.8 (Hopf – Rinow).Let (M,g ) be a connected Riemannian
manifold. The following are equivalent:
(1) M is complete,
(2) a subset ofM is compact if and only if it is closed and bounded,
(3) every geodesic can be extended on the wholeR.
IfM is complete, any two pointsp,q ∈M are joined by aminimising geodesic
γ, i.e. a curve such thatL(γ) =d(p,q ).
1.2.5. Exponential map. Let M be a complete Riemannian manifold.
The fact that geodesics are determined by ﬁrst-order conditions allows us to
introduce the following.
Deﬁnition 1.2.9. Letp∈M be a point. Theexponential map
expp :TpM−→M
is deﬁned as follows. A vectorv ∈ TpM determines a maximal geodesic
γv : R→M withγv (0) =p andγ′
v (0) =v. We setexpp(v ) =γv (1).
Theorem 1.2.10.The diﬀerential of the exponential mapexpp at the origin
is the identity and henceexpp is a local diﬀeomorphism at the origin.
Via the exponential map, a small neighborhood of the origin inTpM can
be used as a chart nearp: we recover here the intuitive idea that the tangent
space approximates the manifold nearp.
When M is not complete, the exponential map is only deﬁned in some
open star-shaped neighbourhoodVp⊂TpM of the origin, and Theorem 1.2.10
holds also in this case.
1.2.6. Injectivityradius. LetM beacompleteRiemannianmanifold. We
introduce the following.
Deﬁnition 1.2.11. Theinjectivity radius injpM >0 ofM at a pointp∈M
is the supremum of allr >0 such thatexpp|B0(r) is a diﬀeomorphism onto its
image.
HereB0(r ) is the open ball with centre0 and radiusr in the tangent space
TpM. The injectivity radius is always positive by Theorem 1.2.10. For every
r <injpM the exponential map transforms the ball of radiusr in Tp(M) into
the metric ball of radiusr inM. That is, the following equality holds:
expp(B0(r )) =Bp(r )
and the metric ballBp(r ) is indeed diﬀeomorphic to an open ball inRn. When
r≥ injpM this may not be true: for instance ifM is compact there is aR> 0
such thatBp(R) =M.
1.2. RIEMANNIAN GEOMETRY 19
The injectivity radiusinjp(M) varies continuously with respect top∈M;
the injectivity radiusinj(M) ofM is deﬁned as
inj(M) = inf
p∈M
injpM.
Proposition 1.2.12.A compact Riemannian manifold has positive injectiv-
ity radius.
Proof. The injectivity radiusinjpM is positive and varies continuously with
p, hence it has a positive minimum on the compactM. □
Finally we note the following. A loop is a curve γ : [a,b ] → M with
γ(a) =γ(b).
Proposition 1.2.13. Let M be a complete Riemannian manifold. Every
loopγ inM shorter than 2· inj(M) is homotopically trivial.
Proof. Setp =γ(a) =γ(b). Sinceγ is shorter than2· inj(M), it cannot
escape the ballBp(r ) for somer <inj(M)⩽ injpM. This ball is diﬀeomorphic
to a ball in Rn, hence in particular it is contractible, soγ is homotopically
trivial. □
A proof of the continuity ofinjp(M) can be found in [35].
1.2.7. Curvature. The curvature of a Riemannian manifold (M,g ) is
some mathematical entity that measures how distortedg is when compared to
the familiar Euclidean structure onRn. The curvature is encoded by various
kinds of mathematical objects, and some of them may be frustratingly compli-
cated whenn = dimM> 3. Luckily, most of the Riemannian manifolds that
we will encounter in this book have “constant curvature” and therefore these
objects will simplify dramatically. We brieﬂy recall them here.
The metric tensorg induces theLevi-Civita connection∇, which can be
used to diﬀerentiate any vector ﬁeld with respect to a tangent vector at any
point ofM. We concentrate on an open chart and hence suppose thatM =U
is an open set ofRn; lete1,...,e n be the coordinate vector ﬁelds onU and
∇i be the Levi-Civita diﬀerentiation with respect toei. We have
∇iej = Γk
ijek
for some smooth functionsΓk
ij :U→ R called theChistoﬀel symbols. Here we
use the Einstein notation: repeated indices should be added from1 ton. The
Christoﬀel symbols are determined byg via the formula:
Γk
ij = 1
2gk𝓁
(∂g𝓁i
∂xj +∂g𝓁j
∂xi −∂gij
∂x𝓁
)
.
Here gk𝓁 is just the inverse matrix ofg = gk𝓁. Christoﬀel symbols are very
useful but depend heavily on the chosen chart; a more intrinsic object is the
20 1. PRELIMINARIES
Riemann tensorthat may be deﬁned (quite obscurely) as
Rijk𝓁 =∂kΓi
𝓁j−∂𝓁Γi
kj + Γi
km Γm
𝓁j− Γi
𝓁mΓm
kj.
By contracting two indices we get theRicci tensor
Rij =Rkikj =∂kΓk
ji−∂j Γk
ki + Γk
km Γm
ji − Γk
jm Γm
ki.
The Ricci tensor is symmetric, and by further contracting we get thescalar
curvature
R =gijRij.
1.2.8. Scalar curvature. What kind of geometric information is con-
tained in the tensors introduced above? The scalar curvatureR is the simplest
curvature detector, and it measures the local discrepancy between volumes in
M and inRn. LetBp(ε)⊂M be theε-ball inM centred atp andB0(ε)⊂ Rn
be theε-ball in the EuclideanRn. We have
Vol
(
Bp(ε)
)
= Vol
(
B0(ε)
)
·
(
1− R
6(n + 2)ε2
)
+ O(ε4).
We note in particular thatR is positive (negative) ifBp(ε)has smaller (bigger)
volume than the usual Euclidean volume.
IfM has dimension 2, that is it is a surface, the Riemann and Ricci tensors
simplify dramatically and are fully determined by the scalar curvatureR, which
is in turn equal to twice thegaussian curvatureK: ifM is contained inR3 the
gaussian curvature is deﬁned as the product of its two principal curvatures,
but whenM is abstract principal curvatures make no sense. On surfaces, the
formula above reads as
Area(Bp(ε)) =πε2−πε4
12 K + O(ε4).
1.2.9. Sectional curvature.If (M,g )has dimensionn> 3the scalar cur-
vature is a weak curvature detector when compared to the Ricci and Riemann
tensors. Moreover, there is yet another curvature detector which encodes
the same amount of information of the full Riemann tensor, but in a more
geometric way: this is thesectional curvatureand is deﬁned as follows.
Deﬁnition 1.2.14. Let(M,g ) be a Riemannian manifold. Letp∈ M be
a point andW ⊂ TpM be a 2-dimensional vector subspace. By Theorem
1.2.10 there exists an open setUp⊂ TpM containing the origin whereexpp
is a diﬀeomorphism onto its image. In particularS = exp p(Up∩W ) is a
small smooth surface inM passing throughp, with tangent planeW. As a
submanifold ofM, the surfaceS has a Riemannian structure induced byg.
The sectional curvature of (M,g ) along W is deﬁned as the gaussian
curvature ofS inp.
1.2. RIEMANNIAN GEOMETRY 21
Figure 1.4. Three surfaces in space (hyperboloid with one sheet, cylin-
der, sphere) whose gaussian curvature is respectively negative, null, and
positive at each point. The curvature on the sphere is constant, while the
curvature on the hyperboloid varies: a complete surface inR3 cannot have
constant negative curvature.
We can use the sectional curvature to unveil the geometric nature of the
Riccitensor: theRiccitensor Rij inp measurestheaveragesectionalcurvature
alongaxes,thatisforeveryunitvector v∈Tp(M)thenumber Rijvivj is (n−1)
times the average sectional curvature of the planesW⊂Tp(M) containingv.
The Riemann tensor is determined by the sectional curvatures and vice-
versa. In dimension n = 3 the Ricci tensor fully determines the sectional
curvatures and hence also the Riemann tensor. This is not true in dimension
n> 4.
1.2.10. Constant sectional curvature. A Riemannian manifold (M,g )
has constant sectional curvature K if the sectional curvature of every 2-
dimensional vector spaceW⊂TpM at every pointp∈M is alwaysK.
Remark 1.2.15. On a Riemannian manifold(M,g ) one may rescale the
metric by some factorλ > 0 substituting g with the tensorλg. At every
point the scalar product is rescaled byλ. Consequently, lengths of curves are
rescaled by
√
λ and volumes are rescaled byλ
n
2. The sectional curvature is
rescaled by 1/λ.
By rescaling the metric we may transform every Riemannian manifold with
constant sectional curvatureK into one with constant sectional curvature−1,
0, or1.
Example 1.2.16. Euclidean space Rn has constant curvature zero. A
sphere of radiusR has constant curvature1/R2.
1.2.11. Isometries. Every honest category has its morphisms. Riemann-
ian manifolds are so rigid, that in fact one typically introduces only isomor-
phisms: these are calledisometries.
22 1. PRELIMINARIES
Deﬁnition 1.2.17. A diﬀeomorphismf :M→N between two Riemannian
manifolds (M,g ) and (N,h ) is anisometry if it preserves the scalar product.
That is, the equality
⟨v,w⟩ =⟨dfp(v ),dfp(w )⟩
holds for allp∈ M and every pair of vectorsv,w ∈ TpM. The symbols⟨,⟩
indicate the scalar products inTpM andTf (p)N.
As we said, isometries are extremely rigid. These are determined by their
ﬁrst-order behaviour at any single point.
Theorem 1.2.18. Let f,g : M→ N be two isometries between two con-
nected Riemannian manifolds. If there is a pointp∈M such thatf (p) =g(p)
anddfp =dgp, thenf =g everywhere.
Proof. Let us show that the subsetS ⊂ M of the pointsp such that
f (p) =g(p) anddfp =dgp is open and closed.
The locus where two functions coincide is typically closed, and this holds
also here (to prove it, take a chart). We prove that it is open: pickp∈ S.
By Theorem 1.2.10 there is an open neighbourhoodUp⊂TpM of the origin
where the exponential map is a diﬀeomorphism onto its image. We show that
the open setexpp(Up) is entirely contained inS.
A pointq∈ expp(Up) is the imageq = exp(v ) of a vectorv ∈ Up and
henceq =γ(1)forthegeodesic γ determinedbythedata γ(0) =p,γ′(0) =v.
The mapsf andg are isometries and hence send geodesics to geodesics: here
f◦γ andg◦γ are geodesics starting fromf (p) = g(p) with the same initial
velocities and thus they coincide. This implies thatf (q) =g(q). Sincef and
g coincide on the open setexpp(Up), also their diﬀerentials do. □
1.2.12. Local isometries. A local isometry f : M → N between Rie-
mannian manifolds is a map where everyp∈M has an open neighbourhood
U such thatf|U is an isometry onto its image. Theorem 1.2.18 applies with
the same proof to local isometries.
The following proposition relates nicely the notions of local isometry, topo-
logical covering, and completeness.
Proposition 1.2.19. Letf :M→N be a local isometry.
(1) IfM is complete, the mapf is a covering.
(2) Iff is a covering, thenM is complete⇐⇒N is complete.
Proof. Sincef is a local isometry, every geodesic inM projects to a ge-
odesic inN. If f is also a covering, the converse holds: every geodesic inN
lifts to a geodesic inM (at any starting point).
If f is a covering we can thus project and lift geodesics viaf: therefore
every geodesic inM can be extended toR if and only if every geodesic inN
can; this proves (2) using the Hopf – Rinow Theorem 1.2.8.
