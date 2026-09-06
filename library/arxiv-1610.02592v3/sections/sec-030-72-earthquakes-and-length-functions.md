---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-030-72-earthquakes-and-length-functions
section_title: "Earthquakes and length functions"
section_number: 7.2
pages: 202-210
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
Simple closed geodesics are a formidable tool to study Teich(Sg): we
can use a simple closed geodesic totwist a metric (the operation is called an
earthquake), and by simply looking at the lengths of the other closed geodesics
we can measure how the metric varies along this transformation. We introduce
these operations here; later on, we will use them to parametrizeTeich(Sg).
7.2.1. Earthquakes. The hyperbolic, ﬂat, and spherical metrics on sur-
faces may be twisted along simple closed geodesics: this operation is called an
earthquake.
Let m be a complete hyperbolic, ﬂat, or elliptic metric on an oriented
surface S and γ be a simple closed geodesic inS. Recall that γ is a map
γ :S1→S. Fix an angleθ∈ R. Informally, a new complete hyperbolic, ﬂat,
or elliptic metricmθ on S is constructed by cuttingS along γ and regluing
with a counterclockwise twist of angleθ. Formally, the new metric is deﬁned
as follows.
In the hyperbolic case, recall from Proposition 4.1.16 thatγ has a R-
neighbourhood isometric to a R-tube for some R > 0. A R-tube in di-
mension two is aR-annulus as in Figure 7.2, deﬁned by quotienting aR-
neighbourhood of a linel by a hyperbolic transformation. TheR-annulus is
naturally parametrized asS1× [−R,R ], where{eit}× [−R,R ] is the geodesic
segment orthogonal toγ in γ(eit ) parametrized by arc length. The ﬂat and
elliptic cases are analogous.
We choose a diﬀeomorphismϕ ofS1× [−R,R ] that curves the segments
left-wise with stepθ as in Figure 7.3-(right). More precisely, letf : [−R,R ]→
R be a smooth function which is zero on
[
−R,−R
2
]
and is constantlyθ on[R
2,R
]
. We setϕ(eit,s ) = (ei(t+f (s)),s ).
7.2. EARTHQUAKES AND LENGTH FUNCTIONS 195
Figure 7.3. To deﬁne the earthquake we pick a diﬀeomorphism of the
R-annulus that modiﬁes the orthogonal segments as shown here.
Wedeﬁneanewmetric mθ onSg asfollows: themetrictensor mθ coincides
with ϕ∗m on theR-annulus and coincides withm on the complement of the
R
2-annulusS1×
[
−R
2, R
2
]
.
Proposition 7.2.1. The metric tensormθ is well-deﬁned and gives a com-
plete hyperbolic, ﬂat, or elliptic metric toSg.
Proof. It is well-deﬁned becausem andmθ coincide onS1×
[R
2,R
]
, since
(eit,s )↦→ (ei(t+θ),s ) is an isometry of theR-annulus. It is hyperbolic, ﬂat, or
elliptic because both patchesm andϕ∗m are. □
Remark 7.2.2. In the new metricmθ the curveγ is still a simple closed
geodesic of the same length as before, and itsR-neighbourhood is also un-
changed.
Of course by deforming an elliptic metric in this way we get nothing new,
because all the elliptic metrics onS2 are isometric. Earthquakes are interesting
only in the ﬂat and hyperbolic geometries.
7.2.2. The earthquake map.We consider the surfaceSg withg> 1 and
show that earthquakes deﬁne nice actions on the Teichmüller spaceTeich(Sg).
If m is any ﬂat or hyperbolic metric andγ is a non-trivial simple closed
curve inSg, we deﬁnemγ
θ to be the ﬂat or hyperbolic metric obtained fromm
via an earthquake of angleθ performed along the unique (up to translations if
g = 1) simple closed geodesic homotopic toγ in the metricm.
Proposition 7.2.3. The earthquake map
Eγ : R× Teich(Sg)−→Teich(Sg)
(θ,m )↦−→mγ
θ
is a well-deﬁned action ofR on Teich(Sg). The mapEγ depends only on the
homotopy class ofγ.
Proof. The only ambiguity in the deﬁnition ofmγ
θ is the choice of the
function f : [−R,R ]→ R. If we use another functionf′ the resulting metric
(mγ
θ )′ changes only by an isotopy: the diﬀeomorphism ofSg which is the
196 7. TEICHMÜLLER SPACE
identity outside theR-annulus and sends (eit,s ) to (ei(t+f (s)−f′(s)),s ) is an
isometry betweenmγ
θ and (mγ
θ )′, and is clearly isotopic to the identity.
To prove thatEγ is an action we need to check that
mγ
θ+θ′ =
(
mγ
θ′
)γ
θ.
ByRemark7.2.2wecantakethesame R-annulustocomposetwoearthquakes
and the equality follows. □
Like the Dehn twistsTγ deﬁned in Section 6.5.3, the actionEγ depends
on the orientation ofSg but not on the orientation ofγ. There is indeed a
strong relation between earthquakes and Dehn twists onγ: as objects acting
on Theichmüller space, the ﬁrst generalise the second.
Proposition 7.2.4. We haveTγ(m) =Eγ(2π,m ).
Proof. It follows directly from the deﬁnitions. □
We now want to study the Teichmüller space and the action ofEγ on it. In
mathematics a space is often beautifully described by some natural functions
deﬁned on it: this role is played here by the length functions of closed curves.
7.2.3. Length functions. A homotopically nontrivial (possibly non sim-
ple) closed curveγ inSg deﬁnes alength function
𝓁γ : Teich(Sg)→ R>0
which assigns to a metricm∈ Teich(Sg)the length𝓁γ(m)of the unique closed
geodesic homotopic toγ.
Wheng = 1 we must actually specify a couple of things in the deﬁnition:
the closed geodesicγ is unique only up to translations, which do not aﬀect its
length; ontheotherhandrescaling does aﬀectlengths, sotogetawell-deﬁned
length function we always rescale the metricm to have unit area.
Wewanttostudytheselengthfunctions, andasusualwestartbyanalysing
the simpler torus ﬂat world, where everything can be described explicitly.
7.2.4. Length functions on the torus.We denote every (isotopy class
of) non-trivial simple closed curve onT with a coprime pair(p,q ) of integers
and we identify the Teichmüller spaceTeich(T ) withH2⊂ C, see Propositions
6.3.2 and 7.1.2. The length functions may be written explicitly.
Proposition 7.2.5. The formula holds:
𝓁(p,q)(z) =|p +qz|√
ℑz
for every simple closed curve(p,q ) and every metricz∈H2.
7.2. EARTHQUAKES AND LENGTH FUNCTIONS 197
1
z
1
z
g
u
a
Figure 7.4. A torus with metricz (left) twisted along the horizontal
curveγ (right). The curveα is a closed geodesic in the new metric.
Proof. Up to rescaling we haveT = R2/Γ with Γ =⟨1,z⟩. The translation
in Γ corresponding to(p,q ) isp· 1 +q·z and the closed geodesic it produces
has length|p +qz|. The area of the torusT isℑz (see a fundamental domain
in Figure 7.1) and hence we must rescale it by1/
√
ℑz. □
We can also write the earthquake action on the meridianm = (1, 0) ofT.
Exercise 7.2.6. We have:
Em(θ,z ) =z + θ
2π.
Hint. Look at the closed geodesicα in Figure 7.4. □
We have discovered in particular thatEm is a parabolic isometry ofH2,
and we can now consider the earthquake action along a generic curve(p,q ).
Corollary 7.2.7.The earthquake actionE(p,q) is the 1-parameter family of
parabolic transformations with ﬁxed point−p
q∈∂H 2.
Proof. We know this when(p,q ) = (1, 0) =m. In general, we send(1, 0)
to (p,q ) via some element of the mapping class group: this element acts by
isometries ofH2 by Proposition 7.1.5 and sends∞ to−p
q. □
The orbits ofE(p,q) are the horospheres centred at−p
q. We have discov-
ered that, quite unexpectedly, the hyperbolic geometry of the planeH2 is well
designed to model the Teichmüller space of the ﬂat torusT.
It is now natural to identify theunoriented simple closed curve±(p,q )
with the rational point−p
q in R∪{∞}⊂ ∂H 2. We get the following convexity
property.
Corollary 7.2.8.Letγ andη be two simple closed curves onT. Ifi(γ,η )>
0 then the length function𝓁η is strictly convex on the orbits ofEγ.
Proof. We may supposeγ = m = (1, 0) and note that the condition
i(γ,η )> 0 translates intoη = (p,q )⁄= (±1, 0). The function in Proposition
7.2.5 is strictly convex on the horospheresℑz =k when (p,q )⁄= (±1, 0). □
198 7. TEICHMÜLLER SPACE
Summing up, the torus picture is the following:
• the mapping class group acts on the Teichmüller space roughly like
PSL2(Z) acts isometrically on the hyperbolic planeH2,
• the unoriented simple closed curves are in 1-1 correspondence with
the rational points in∂H 2 = R∪∞,
• earthquakes act like parabolic transformations centred at these ra-
tional points,
• the length function𝓁γ is constant at the horospheres centred atγ
but strictly convex at the horospheres centred at all the other curves.
The main goal of Chapters 7 and 8 is to draw a similar picture for surfaces
Sg of higher genusg> 2. Everything is more diﬃcult in the hyperbolic world,
because there are no nice explicit formulas describing the length functions,
the action of the mapping class group, the simple closed curves, and the
earthquakes. We now start by generalising the last point: the strict convexity
of length functions.
7.2.5. Convexity of the length functions.We considerSg with g> 2.
Our aim now is to generalise Corollary 7.2.8 to the hyperbolic setting and
then later use this convexity property to parametrizeTeich(Sg). We need a
preliminary result.
Exercise 7.2.9. Letf : Rm× Rn→ R>0 be strictly convex and proper. The
function
F : Rn−→ R>0
y↦−→min
{
f (x,y )
⏐⏐x∈ Rm}
is well-deﬁned, strictly convex, and proper.
The following generalisation of Corollary 7.2.8 says that length functions
are convex on the earthquakes orbits, and very often they are strictly convex
and proper.
Proposition 7.2.10. Let η and γ be two homotopically non-trivial simple
closed curves inSg andm be a hyperbolic metric onSg. The function
R−→ R>0
θ↦−→𝓁η(mγ
θ )
is
• constant ifi(η,γ ) = 0,
• strictly convex and proper ifi(η,γ )> 0.
Proof. The metricmγ
θ is obtained by twistingm of an angleθ along the
simple closed geodesic γ. If i(η,γ ) = 0 the curves η and γ are disjoint
geodesics inm andη is not aﬀected by the earthquakes that we perform near
γ, hence the function𝓁η(mγ
θ ) is constant.
7.2. EARTHQUAKES AND LENGTH FUNCTIONS 199
Figure 7.5. A geodesic inmγ
θ can be seen on the original metricm as
follows: it is a geodesic outside the annulus and deviates on the left by an
angle θ every time it crosses it (centre). We may simplify the picture by
describing it as a broken geodesic line that makes a leftθ-jump each time
that it crossesγ (right).
Consider the casen =i(η,γ )> 0. Denote by ¯ηθ the geodesic represen-
tative ofη in the twisted metricmγ
θ: it intersectsγ transversely inn points.
Fix a suﬃciently smallR-annulus aroundγ and note that the geodesics
in mγ
θ can be seen in the original metricm as follows: these are curves that
are geodesic outside theR-annulus and deviate smoothly on the left each
time they cross it as in Figure 7.5-(centre). We may substitute each smooth
deviation with a broken jump as shown in Figure 7.5-(right) and get a bijection
{ closed geodesics
with respect to mγ
θ
}
←→
{ broken geodesics
with respect to m
}
where a broken geodesic is a geodesic that at every crossing ofγ jumps to
the left at distanceθL(γ)
2π and then keeps going on, leavingγ with the same
incidence angle (hereL(γ) is the length ofγ). This correspondence is useful
because it preserves the lengths: the length of the closed geodesic formγ
θ is
equal to the length of the corresponding broken geodesic (which is the sum of
the lengths of its components), because the segments in Figure 7.5-(left) and
(right) are isometric.
We lift this description to the universal coverH2. We ﬁx a liftl of ¯η = ¯η0
and pickn + 1 consecutive intersectionsr1,...,r n+1 ofl with the lifts ofγ as
in Figure 7.6. The hyperbolic transformationτ with axisl corresponding toη
sendsr1 torn+1. We parametrise eachri with R via arc length.
The closed geodesic¯ηθ, represented as a broken geodesic, lifts to a broken
geodesic which starts at some pointx1−θL(γ)/2π∈r1 and arrives at some
other pointx2∈r2, then jumps on the left at distanceθL(γ)/2π and starts
again fromx2−θL(γ)/2π, and so on until it reaches the pointτ(x1)∈τ(r1) =
rn+1. If we make the pointsx1∈ r1,...,x n∈ rn vary we get various broken
paths in this way, but only one arrives and exits from each lineri with the same
incidence angles and thus represents¯ηθ. The other broken paths represent
piecewise-geodesic curves homotopic to¯ηθ and are therefore longer than¯ηθ.
200 7. TEICHMÜLLER SPACE
x -  '
'
x -  '
Figure 7.6. The (blue) line l is a lift of ¯η. Consider n consecutive
intersections with liftsr1,...,r n+1 of γ (in red), withτ(r1) = rn+1, and
parametrize eachri with R via arc-length. We setθ′ =θL(γ)/2pi.
Hence
𝓁η(mγ
θ ) = min
{ n∑
i=1
d
(
xi−θL(γ)
2π ,xi+1
)⏐⏐⏐⏐⏐ (x1,...,x n)∈ Rn
}
where xn+1 = τ(x1). We can now prove that the functionθ↦→ 𝓁η(mγ
θ ) is
proper and strictly convex. The function
ψ : R2n−→ R
(x1,y 1,...,x n,yn)↦−→
n∑
i=1
d(yi,xi+1)
where xn+1 = τ(x1) is strictly convex and proper by Proposition 2.4.4. The
auxiliary function
φ: R2n× R−→ R
(x,θ )↦−→ψ(x)
is only convex, but its restriction to the subspace
H =
{
yi =xi−θl (γ)
2π
}
is strictly convex and proper, because the subspaceH is not parallel to the
direction (0,..., 0, 1). The coordinatesxi andθ identifyH with Rn× R. The
restrictionf =φ|H is hence a functionf : Rn× R→ R and we obtain
𝓁η(mγ
θ ) = min
{
f (x,θ )
⏐⏐x∈ Rn}
.
By Exercise 7.2.9 the functionθ↦→𝓁η(mγ
θ ) is strictly convex and proper.□
7.2. EARTHQUAKES AND LENGTH FUNCTIONS 201
Figure 7.7. Choose for each componentγi of a pants decompositionµ
a curveγ′
i that intersectsγi in one or two points and is disjoint from the
other components ofµ. There are two cases to consider, depending on
whether the two pants adjacent toγi are distinct (left) or not (right).
We now employ this convexity property to prove some facts on the earth-
quakes and the Teichmüller space.
7.2.6. Earthquakes on essential multicurves.We use the convexity of
the length functions to prove the following. We suppose again thatg> 2.
Corollary 7.2.11. For every simple closed curveγ, the earthquake action
Eγ on Teich(Sg) is free.
Proof. Suppose by contradiction thatm = mγ
θ0 for someθ0 > 0. Then
m =mγ
nθ0 for everyn∈ Z. Let η be a simple closed curve withi(η,γ )> 0,
which exists by Exercise 6.3.13; the functionθ↦→ 𝓁η(mγ
θ ) is strictly convex
and constant on{nθ0,n∈ Z}, a contradiction. □
The earthquake action is deﬁned more generally for essential multicurves.
An essential multicurveµ =γ1⊔···⊔ γk ofSg determines an action
Eµ : Rk× Teich(Sg)−→Teich(Sg)
(θ,m )↦−→mµ
θ
where θ = (θ1,...,θ k) and mµ
θ =mγ1
θ1◦···◦ mγk
θk
. Note that the actions on
disjoint curves commute.
Corollary 7.2.12. For every essential multicurveµ, the earthquake action
Eµ on Teich(Sg) is free.
Proof. We may completeµto a pants-decompositionµ =γ1⊔...⊔γ3g−3.
Pick for everyi = 1,..., 3g−3a curveγ′
i as in Figure 7.7 such thati(γi,γ′
i )>
0 for alli andi(γi,γ′
j ) = 0 for alli⁄=j.
Suppose by contradiction thatm =mµ
θ for someθ⁄= 0: hencemµ
nθ =m
for alln∈ Z. There is ani such thatθi⁄= 0. The length function𝓁γ′
i (mµ
θ )
depends only onθi and not on the other coordinates ofθ: therefore it equals
𝓁γ′
i (mγi
θi
) which is strictly convex, a contradiction. □
202 7. TEICHMÜLLER SPACE
Figure 7.8. A frame for the Fenchel-Nielsen coordinates consists of a
(red) pants decompositionµ and a (blue) transverse multicurveν that
cuts each pair of pants into two hexagons. The number of components of
µ is 3g− 3, that ofν can vary.
