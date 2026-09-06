---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-053-125-nil-geometry
section_title: "Nil geometry"
section_number: 12.5
pages: 394-404
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
Therearestillthreenon-isotropicgeometriestoanalyse. Thesegeometries
are not products, but they have a reasonable bundle structure, so that many of
the arguments of the previous section can be extended with not much eﬀort.
We start with the geometryNil, which is aR-bundle overR2. This geom-
etry is fully carried by a Lie group called theHeisenberg group.
12.5.1. The Heisenberg group. The Heisenberg group consists of all
matrices 

1 x z
0 1 y
0 0 1


with x,y,z ∈ R, with the multiplication operation. This is a nilpotent (but
non-abelian) Lie group (see Exercise 1.4.4) and is hence also called Nil. It is
clearly diﬀeomorphic toR3. There is a Lie groups exact sequence
0−→ R−→Nil−→ R2−→0
where R = [Nil, Nil] is the centre of Nil and consists of all matrices with
x =y = 0. Therefore Nil is naturally a line bundle overR2. We identify Nil
with R3 using the coordinates(x,y,z ). The product operation becomes
(x,y,z )· (x′,y′,z′) = (x +x′,y +y′,z +z′ +xy′).
Exercise 12.5.1. The commutator of two elements is
[
(x,y,z ), (x′,y′,z′)
]
= (0, 0,xy′−x′y ).
12.5. NIL GEOMETRY 387
x
y
z
Figure 12.4. The planes orthogonal to thez axis in Nil form the stan-
dard contact structure onR3.
12.5.2. The geometry of Nil.Every left-invariant Riemannian structure
on a Lie groupG is constructed by ﬁxing a scalar product at the tangent space
TeG of e∈G and then extending it by left-multiplication. Heree = (0, 0, 0)
and we giveTeNil = R3 the Euclidean scalar product. This deﬁnes a left-
invariant Riemannian structure onNil.
Exercise 12.5.2. The metric tensor at(x,y,z ) is


1 0 0
0 x 2 + 1 −x
0 −x 1

.
The following triple is an orthonormal basis at(x,y,z ):
(16) (1, 0, 0), (0, 1,x ), (0, 0, 1).
The planes spanned by the ﬁrst two vectors form the standardcontact
structure in R3 shown in Figure 12.4. It is a non-integrable distribution of
planes: no surface is tangent to it at every point.
We remark that the metric tensor has unit determinant at every point:
therefore the volume form onNil is the standard one onR3.
We can calculate the Christoﬀel symbolsΓk
ij by hand or using a computer
code; these are all zero except the following:
Γ1
22 =−x, Γ1
23 = Γ1
32 = 1
2,
Γ2
12 = Γ2
21 = x
2, Γ2
13 = Γ2
31 =−1
2,
Γ3
12 = Γ3
21 = x 2− 1
2 , Γ3
13 = Γ3
31 =−x
2.
388 12. THE EIGHT GEOMETRIES
The Ricci tensor at(x,y,z ) is
Rij = 1
2·


−1 0 0
0 x 2− 1 −x
0 −x 1

.
Whenx = 0 the Ricci tensor is a diagonal matrix with entries− 1
2,− 1
2, 1
2. For
a unit vectorv∈TpNil, recall thatRijvivj equals twice the average value of
the sectional curvatures of the planes containingv: this average value ranges
here from− 1
4 to 1
4 and is maximal whenv = (0, 0,±1). This holds when
x = 0 and hence at all pointsp∈ Nil by left-multiplication.
12.5.3. The isometry group of Nil.The group Nil acts on itself iso-
metrically by left-multiplication. Left-multiplication by(a,b,c ) preserves the
bundle Nil→ R2 and induces onR2 a translation by the vector(a,b ).
There are also more complicate isometries ofNil that preserve the bundle
structure but induce rotations onR2: one such isometryϕ sends (x,y,z ) to
(
x cosθ−y sinθ, xsinθ +y cosθ, z + 1
2(x 2−y 2) sinθ cosθ−xy sin2θ
)
.
This map preserves the bundle and induces a rotation onR2.
Proposition 12.5.3. The mapϕ is an isometry ofNil.
Proof. Set (x′,y′,z′) =ϕ(x,y,z ). The diﬀerentialdϕ at (x,y,z ) is


cosθ − sinθ 0
sinθ cosθ 0
x sinθ cosθ−y sin2θ −y sinθ cosθ−x sin2θ 1


and may be rewritten as


cosθ − sinθ 0
sinθ cosθ 0
x′ sinθ x′ cosθ−x 1.


The diﬀerentialdϕ sends the orthonormal basis (16) to
(cosθ, sinθ,x′ sinθ), (− sinθ, cosθ,x′ cosθ), (0, 0, 1).
These vectors at(x′,y′,z′) are also orthonormal. □
We deduce the following.
Proposition 12.5.4. Every isometry of Nil preserves the line bundle and
induces an isometry ofR2. We have
0−→ R−→Isom+(Nil)
p
−→Isom(R2)−→0
where R is the centre ofNil. The groupIsom+(Nil) has two components.
12.5. NIL GEOMETRY 389
L
x
z
y
L
F
F
Figure 12.5. The Nil manifoldM = Nil/Γ is obtained by identifying the
faces of this unit cube as follows: the triangular faces are glued via the
aﬃne maps as shown by the labels, and the pairs of unlabelled opposite
square faces are identiﬁed by translations. The cube is a fundamental
domain for Γ.
Proof. The rotational isometriesϕ with angleθ introduced above form a
S1-subgroup of Isom+(Nil). The subgroups S1 and Nil belong to the com-
ponent Isom+
◦ (Nil) < Isom+(Nil) containing the identity, which hence has
dimension at least 1 + 3 = 4 and acts transitively on Nil. Stabilisers have
dimension at least4− 3 = 1 and cannot have bigger dimension by Proposi-
tion 6.2.15, otherwiseNil would have constant sectional curvature: therefore
dim(Isom+
◦ (Nil)) = 4 and Isom+
◦ (Nil) is generated byS1 and Nil, and it pre-
serves the line bundle sinceS1 and Nil do.
The subgroupIsom+
◦ (Nil) preserves the orientation of the ﬁbres and ofR2.
We leave as an exercise the existence of another component ofIsom+(Nil)
which inverts the orientation of the ﬁbres and ofR2. □
Example 12.5.5. A manifoldM = Nil/Γ modelled on Nil is described in
Figure 12.5. The ﬁgure shows a fundamental domain for the groupΓ <
Isom+(Nil) generated by the isometries
(x,y,z )↦−→(x + 1,y,z +y ),
(x,y,z )↦−→(x,y + 1,z ), (x,y,z )↦−→(x,y,z + 1).
obtained by left-multiplication with the canonical basis ofR3. Both the unit
cube andM have volume one. The manifoldM is clearly a torus bundle with
monodromy
(1 1
0 1
)
and is hence diﬀeomorphic to the Seifert manifold
(
T, (1, 1)
)
by Exercise 11.4.11.
A group Γ < Isom(X) is cocompact if X/Γ is compact. We prove that
cocompact groups inIsom(R2) do not lift.
Proposition 12.5.6. Let Γ< Isom(R2) be discrete and cocompact. There
is no homomorphismf : Γ→ Isom+(Nil) such thatp◦f = id.
Proof. Up to taking a ﬁnite-index subgroup we may suppose thatΓ is gen-
erated by two translations along independent vectors(x,y ) and (x′,y′). We
390 12. THE EIGHT GEOMETRIES
prove that two liftsϕ,ϕ′∈ Isom+(Nil) of these translations never commute,
thus forbidding the existence of a homomorphismf.
If ϕ, ϕ′ ∈ Nil, Exercise 12.5.1 gives [ϕ,ϕ′] = xy′−x′y ⁄= 0. All the
other lifts are of typegϕ,g′ϕ′ for someg,g′∈ R, hence we get the same
commutator. □
Let Isom+
0 (Nil) be the connected component ofIsom+(Nil) containinge.
Exercise 12.5.7. We have
[
Isom+
0 (Nil), Isom+
0 (Nil)
]
= R.
Therefore Isom+
0 (Nil) is nilpotent.
Corollary 12.5.8.If a three-manifoldM has aNil geometry, thenπ1(M) is
virtually nilpotent.
Proof. It has a nilpotent subgroup of index at most two, because the
subgroup Isom+
0 (Nil)< Isom+(Nil) is nilpotent and has index two. □
12.5.4. Nil geometry. We now classify the manifolds modelled onNil.
Proposition 12.5.9.A discrete groupΓ< Isom+(Nil) is coﬁnite if and only
if bothp(Γ) and Γ∩ kerp are discrete and coﬁnite.
Proof. We follow the proof of Proposition 12.4.4. Up to taking ﬁnite-
index subgroups we may suppose thatΓ< Isom+
0 (Nil). Ifp(Γ) is discrete the
proof of Proposition 12.4.4 applies also here; note that the formula (15) holds
because the volume form inNil is the standard one onR3.
Ifp(Γ) is not discrete then that proof shows that there is a neighbourhood
U⊂ Isom+(Nil) ofe such that every two elementsf,g ∈ Γ projecting inp(U)
commute. (It is still true that [f,g ] depends only onp(f ) and p(g) since
kerp = R is central.) We deduce again that the isometries inp(Γ) commute:
hence they are either rotations ﬁxing the same point or translations.
In the former caseΓ is not coﬁnite. In the latter, we getΓ< Nil acting
as left-multiplication. Every two f,g ∈ Γ projecting top(U) commute and
hence project to parallel translations by Exercise 12.5.1. As in the proof of
Proposition 12.4.4 we deduce thatp(Γ) preserves a line, and hence it is not
coﬁnite. □
Corollary 12.5.10.If the interior of a compact orientable manifoldM ad-
mits a ﬁnite-volume completeNilgeometry thenM is a closed Seifert manifold
withχ = 0 ande⁄= 0.
Proof. We have int(M) = Nil /Γ with Γ coﬁnite and Proposition 12.5.9
provides a Seifert ﬁbrationM→ S over a ﬁnite-area orbifoldS = R2/p(Γ).
Finite-area ﬂat orbifolds haveχ(S) = 0 and are closed (there are no cusps in
ﬂat geometry), henceM is closed.
12.5. NIL GEOMETRY 391
We havee⁄= 0, otherwise up to ﬁnite-index we would getM = T×S1
contradicting Proposition 12.5.6. □
We prove the converse.
Proposition 12.5.11. If M is a closed Seifert manifold withχ = 0 and
e⁄= 0, thenM admits a Nil geometry.
Proof. We have
M =
(
S, (p1,q 1),..., (pk,qk)
)
.
Suppose S is a closed orientable surface of genusg > 0. In the following
π1(S) is the orbifold fundamental group. We have:
π1(S) =⟨a1,b 1,...,a g,bg,c 1,...,c k| [a1,b 1]··· [ag,bg]c1··· ck,cpi
i ⟩,
π1(M) =⟨a1,b 1,...,a g,bg,c 1,...,c k,l | [a1,b 1]··· [ag,bg]c1··· ck,cpi
i lqi,
[ai,l ], [bi,l ]⟩.
We ﬁx any ﬂat structure on the orbifoldS and get an injectionπ1(S)→
Isom+(R2). Wenowwanttoliftthismaptoaninjection π1(M)→ Isom+(Nil),
so that the resulting diagram commutes:
π1(M) //

Isom+(Nil)

π1(S) // Isom+(R2)
Recall that Isom+
0 (Nil) contains the groupR of vertical translations: we use
the multiplicative notation and indicate it asR>0. We note thatR>0 is cen-
tral in Isom+
0 (Nil) because it commutes withNil and the isometriesϕ from
Proposition 12.5.3, which altogether generateIsom+
0 (Nil).
We identifyπ1(S) with its image inIsom+(R2). We lift arbitrarilyai,bi,ci
inside Isom+(Nil) and pickl∈ R>0. We get
[a1,b 1]··· [ag,bg]c1··· ck =eµ,
cpi
i lqi =eλi
for someµ,λi∈ R. To get a homomorphismπ1(M)→ Isom+(Nil) we need
µ =λi = 0. To obtain that we change the lifts asc′
i =etici,l′ =eul to get
[a1,b 1]··· [ag,bg]c′
1··· c′
k =et1+...+tk +µ,
(c′
i )pi (l′)qi =etipi +uqi +λi.
We want
t1 +... +tk =−µ,
tipi +uqi =−λi.
392 12. THE EIGHT GEOMETRIES
The determinant of thek×k coeﬃcient matrix was already calculated in the
proof of Proposition 10.3.15, and is
±
∑qi
pi
(p1··· pk) =±e·p1··· pk⁄= 0.
Therefore the linear system has a unique solution(t1,...,t k,u ). The liftl′ is
necessarily non-trivial, otherwise we would get a liftπ1(S)→ Isom+(Nil) that
is excluded by Proposition 12.5.6. Therefore the lift is injective.
IfS is non-orientable the proof is similar and left as an exercise. □
12.6. ~SL2 geometry
The~SL2 geometry is similar toNil, but it is now aR-bundle overH2. The
geometry is again fully carried by the Lie group~SL2, which is the universal
cover of bothSL2(R) and PSL2(R). It is convenient to identifyPSL2(R) with
the unit tangent bundle ofH2.
12.6.1. The unit tangent bundle. The tangent bundleTM of a Rie-
mannian n-manifold M has a natural Riemannian structure, which we brieﬂy
introduce.
The tangent space at any pointx∈ TM splits into avertical subspace
Vx = kerdpx wherep :TM→M is the projection, and ahorizontal subspace
Hx determined by the metric tensor onM as follows: use the parallel transport
to move the tangent vectorx along all geodesics exiting fromp(x); the result
is a smalln-surface inTM containingx and we setHx to be its tangent space
atx.
To deﬁne a metric onTM we impose thatVx andHx be orthogonal and we
give to each space the metric ofTxM, via the natural identiﬁcationVx =TxM
and via the isomorphismdpx :Hx→TxM.
The unit tangent bundleUM⊂TM consists of all unitary tangent vectors
and inherits a Riemannian structure. Every isometryf : M→ M induces an
isometrydf :UM→UM.
12.6.2. The space UH2. We now focus on the caseM = H2 we are
interested in. Parallel transport was deﬁned explicitly in Section 2.4.4. We
represent H2 using the upper half-plane model H2 = {ℑz > 0}, so that
TH 2 = H2× C and UH 2 = H2×S1 has coordinates (z,θ ). The tangent
spaceT(z,θ )UH 2 is naturally identiﬁed withC× R = R3.
Lemma 12.6.1. The metric tensor ofUH 2 at (z,θ ) is


2y−2 0 y−1
0 y−2 0
y−1 0 1


wherez =x +iy.
12.6. ~SL2 GEOMETRY 393
Proof. We ﬁrst consider the disc modelD2 of H2 with TD 2 = D2× C
and T(z,v )TD 2 = C× C. We focus at a point (0,v ) and determine the
decomposition
T(0,v) =H(0,v)⊕V(0,v).
We haveV(0,v) = 0× C and we now determineH(0,v). Every geodesic through
0 is a Euclidean linel and the parallel transport ofv∈T0D2 alongl forms a
constant angle withl: the parallel transport ofv atz∈l is just the rescaled
vector (1−|z|2)v. Parallel transports ofv along lines passing through0form a
surface, which is the graph of the functionf (z) = (1−|z|2)v, whose tangent
plane at 0 isH(0,v) = C× 0 since ∂f
∂x = ∂f
∂y = 0 at 0.
We have discovered that the horizontal and vertical planes at(0,v ) are
just the coordinate ones ofT(0,v) = C× C. By deﬁnition these are orthogonal
and inherit a metric tensor from that ofT0D2, which is4 times the Euclidean
one. Therefore the metric tensor atT(0,v) = C2 is 4 times the Euclidean one.
We now turn to the unitary sub-bundleUD 2 = D2×S1. We use the
natural identiﬁcationsT(0,θ)UD 2 = C× R = R3 and we deduce that the
vectors (1, 0, 0), (0, 1, 0), (0, 0, 1) ∈ T(0,θ) are orthogonal and have norm
2, 2, 1 respectively.
The Möbius transformation
f (z) = z−i
iz− 1
is an isometry between the two modelsD2 and H2 that sends 0 to i. It is
holomorphic and its complex derivative is
f′(z) = −2
(iz− 1)2.
The isometry f : D2 → H2 induces an isometry f∗ : UD 2 → UH 2, that is
f∗ :D2×S1→H2×S1, which is as follows:
f∗(z,θ ) =
( z−i
iz− 1,θ + arg(f′(z))
)
=
( z−i
iz− 1,θ +π− 2arg(iz− 1)
)
=
( z−i
iz− 1,θ +π− 2ℑ log(iz− 1)
)
.
In particularf∗(0,θ ) = (i,θ +π). Recall that the Jacobians of a holomorphic
g and of logg are
Jg =
(ℜg′ −ℑg′
ℑg′ ℜg′
)
, J (logg) =
(
ℜg′
g −ℑg′
g
ℑg′
g ℜg′
g
)
.
394 12. THE EIGHT GEOMETRIES
The diﬀerential off∗ at the point(z,θ ) is hence
(df∗)(z,θ ) =


ℜ −2
(iz−1)2 −ℑ −2
(iz−1)2 0
ℑ −2
(iz−1)2 ℜ −2
(iz−1)2 0
−2ℑ 1
z+i −2ℜ 1
z+i 1

.
In particular atz = 0 we get
(df∗)(0,θ) =


−2 0 0
0 −2 0
2 0 1

.
Since this is an isometry, the three image vectors(−2, 0, 2), (0,−2, 0), and
(0, 0, 1)areorthogonalwithnorm 2, 2, 1,hence (1, 0,−1), (0, 1, 0),and (0, 0, 1)
form an orthonormal basis atT(i,θ +π)UH 2 and the metric tensor there is


2 0 1
0 1 0
1 0 1

.
The tensor is independent ofθ. To ﬁnd its value at(z,θ ) for a genericz∈
H2 it suﬃces to transport it via an isometry that sendsi to z. Every such
isometry is a composition of a horizontal translation (which does not change
the tensor) and a dilationg(z) = λz with λ >0. We have g′(z) = λ and
g∗(z,θ ) = (λz,θ ), thereforedg∗ sends the above orthonormal basis atT(i,θ )
tothebasis (λ, 0,−1), (0,λ, 0), (0, 0, 1). Themetrictensorat (λi,θ )ishence


2λ−2 0 λ−1
0 λ−2 0
λ−1 0 1

.
The proof is complete. □
At a point(x,y,θ )∈UH 2, an orthonormal basis is
(17) (y, 0,−1), (0,y, 0), (0, 0, 1).
The planes orthogonal to(0, 0, 1) form a contact structure similar to the one
drawn in Figure 12.4.
We remark that the metric tensor at(x,y,θ ) has determinanty−4, like in
the product metricH2×S1: therefore the volume form inUH 2 is the same
as in the product metric (although the metric tensor is not).
The non-zero Christoﬀel symbols at(x,y,θ ) are:
Γ1
12 = Γ1
21 =− 3
2y, Γ1
23 = Γ1
32 =−1
2,
Γ2
11 = 2
y, Γ2
13 = Γ2
31 = 1
2, Γ2
22 =− 1
y,
Γ3
12 = Γ3
21 = 1
y 2, Γ3
23 = Γ3
32 = 1
2y.
12.6. ~SL2 GEOMETRY 395
The Ricci tensor is
Rij = 1
2·


−2y−2 0 y−1
0 −3y−2 0
y−1 0 1

.
When y = 1 we can represent the Ricci tensor in the orthonormal basis (17)
and get a diagonal matrix with values− 3
2,− 3
2, 1
2. For a vectorv∈T(z,θ )UH2,
recall thatRijvivj is twice the average value of the sectional curvatures of the
planes containingv: this average value ranges from− 3
4 to 1
4 and is maximal
when v = (0, 0,±1). This holds wheny = 1 and hence for anyz∈UH2 by
acting via isometries ofH2.
12.6.3. ~SL2 geometry. Let~SL2 be the universal cover ofSL2 = SL2(R).
As a universal cover of a Lie group, it is also a Lie group. We have coverings
~SL2−→SL2−→ PSL2(R) = Isom +(H2).
The group PSL2(R) acts freely and transitively onUH2 and hence we can
identify PSL2(R) with UH2. With this identiﬁcationPSL2(R) inherits a left-
invariant Riemannian metric that lifts to a left-invariant Riemannian metric on
the Lie group~SL2.
In the previous section we have identiﬁedUH2 with H2×S1 and we can
likewiseidentify ~SL2 withH2×R, andgetanexplicitmetrictensorfromLemma
12.6.1.
SinceUH2 is a circle bundle overH2, likewise~SL2 is a line bundle overH2.
The group R acts isometrically on~SL2 by translating every ﬁbre.
Proposition 12.6.2. Every isometry of~SL2 preserves the line bundle and
induces an isometry ofH2. We have
0−→ R−→Isom+(~SL2)
p
−→Isom(H2)−→0.
The group Isom+(~SL2) has two components.
Proof. The groupsR and~SL2 belong to the componentIsom+
◦ (~SL2) con-
taininge which has dimension at least1 + 3 = 4. We conclude as in the proof
of Proposition 12.5.4. □
Exercise 12.6.3. The unit tangent bundle of a ﬁnite-area complete hyper-
bolic surface is naturally a manifold modelled on~SL2.
As for Nil, cocompact groups do no lift.
Proposition 12.6.4.Let Γ< Isom(H2) be discrete and cocompact. There
is no homomorphismf : Γ→ Isom+(~SL2) such thatp◦f = id.
Proof. Up to taking a ﬁnite index subgroup we may suppose thatΓ acts
freely and henceS = H2/Γ is a closed hyperbolic surface. IfΓ lifts, consider
the groupG < Isom+(~SL2) generated byf (Γ) and 2π∈ R, isomorphic to
396 12. THE EIGHT GEOMETRIES
Γ× Z. The quotient~SL2/G is naturally the unit tangent bundle ofS and is
hence the Seifert manifold
(
S, (1,χ (S))
)
by Remark 10.2.8. Its fundamental
group is however not a productΓ× Z by Exercise 10.2.9. □
Proposition 12.6.5. A discrete group Γ < Isom+(~SL2) is coﬁnite if and
only if bothp(Γ) and Γ∩ kerp are discrete and coﬁnite.
Proof. Same proof as Proposition 12.4.4, with a minor variation: ifp(Γ)
is not discrete, up to taking an index-two subgroup we suppose thatp(Γ)<
Isom+(H2); the R-action commutes with Γ and [f,g ] depends only onp(f )
andp(g), so that proof applies. □
We now classify the manifolds having a~SL2 geometry.
Corollary 12.6.6.If the interior of a compact orientable manifoldM admits
a ﬁnite-volume complete~SL2 geometry then M is a Seifert manifold with
χ< 0. IfM is closed thene⁄= 0.
Proof. We haveint(M) = ~SL2/Γ with Γ coﬁnite. Proposition 12.6.5 fur-
nishes a Seifert ﬁbrationM→ S over the ﬁnite-area orbifoldS = H2/p(Γ).
If M is closed we gete⁄= 0: if not, up to taking a ﬁnite index subgroup we
would getM =S×S1 contradicting Proposition 12.6.4. □
We now prove the converse.
Proposition 12.6.7. If M is a Seifert manifold with χ < 0 and either
∂M⁄= ∅ ore⁄= 0, the interior ofM admits a ﬁnite-volume~SL2 geometry.
Proof. IfM isclosedweapplytheproofofProposition12.5.11. If ∂M⁄= ∅
the presentations ofπ1(S) andπ1(M) are as described there, except that they
do not contain the relatorcpi
i whenever ci represents a boundary component
of M. So we have less constraints and we easily see that a solution to the
ﬁnal linear problem exists also in this case. □
