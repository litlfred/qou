---
doc_id: arxiv-2012.12159v3
doc_title: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME"
section_id: sec-016-9-regularizing-the-total-funk-volume
section_title: "Regularizing the total Funk volume"
section_number: 9
pages: 34-41
source_pdf: 2012.12159v3.pdf
source_sha256: 473ec6959e82cd98
---
We use the notation of subsection 3.2. Recall that we use the standard Euclidean
structure on V = Rn+1, and identify the double cover of P and P∨ with the unit
sphere. Let x0∈ x be a unit vector, well-deﬁned up to sign. We write σx,σξ for
the standard Euclidean measure on the corresponding copy of S2.
Lemma 9.1. Forg∈ PGL(V ), set χg(x,ξ ) =|gx0||g−∗ξ0|. Then
g∗(σxσξ) =χ−n−1
g−1 σxσξ
Proof. Denote by Stab+(x,ξ )⊂ Stab(x,ξ ) the subgroup of the stabilzer in PGL(V )
that has sign detg|x = sign detg∗|ξ. Then Stab +(x,ξ )-equivariantly we have
Dens(Tx,ξ(P× P∨)) = Dens∗(x)n+1⊗ Dens∗(ξ)n+1 =xn+1⊗ξn+1,
and so
g∗(σxσξ)(gx,g−∗ξ) = (|gx0||g−∗ξ0|)n+1σxξ =χg(x,ξ )n+1σxσξ.
Hence
g∗(σxσξ)(x,ξ ) =χg(g−1x,g∗ξ)n+1σxσξ =χ−n−1
g−1 (x,ξ )σxσξ,
as claimed. □
35 A Funk perspective on billiards, projective geometry and Mahler volume
Deﬁne f0∈C(P× P∨) by f0(x,ξ ) =|⟨x0,ξ 0⟩|. It is easy to check that
g∗f0 =χ−1
g f0.
Deﬁne µz(x,ξ ) =f0(x,ξ )zσxσξ∈M (P× P∨\Z ). For Rez >−1, it extends as an
absolutely continuous measure on P× P∨.
Lemma 9.2. g∗µz =χ−(n+1)−z
g−1 µz.
Proof. It is easy to check that g∗µz = (g−1)∗fz
0·g∗(σxσξ). It remains to put the
previous computations together. □
As expected from Proposition 3.9, we see that z =−(n + 1) corresponds to the
invariant measureµ.
Henceforth we use the same notation for a point on Sn and the corresponding
line in RPn. The action of GL( V ) on Sn is g(x) = gx
|gx|.
Let K⊂ Sn⊂ V = Rn+1 be a proper convex compact set, and K∨⊂ Sn its
polar body, namely K∨ ={ξ∈ Sn :∀x∈ K,⟨x,ξ⟩≥ 0}. They correspond to a
dual pair of convex sets in P and P∨, also denoted K,K∨.
Deﬁne the Beta function of K⊂Sn by
C∋z↦→BK(z) =
∫
K×K∨
⟨x,ξ⟩zσxσξ =⟨1 K×K∨,µz⟩.
Clearly,BK(z) = BK∨(z). Assume henceforth that K is smooth and strictly con-
vex.
Lemma 9.3. The integral BK(z) is convergent if and only if Rez >−n+3
2 .
Proof. The zeros of⟨x,ξ⟩ onK×K∨ areZ∩K×K∨, which is an (n−1)-dimensional
submanifold in ∂K×∂K∨. Let x1,...,x n−1 be local coordinates on ∂K, and
ξ1,...,ξ n−1 the Legendre-dual coordinates on ∂K∨, that isZ∩ (K×K∨) ={ξj =
xj}. Let xn be the remaining coordinate near ∂K, so that locally K ={xn≥ 0},
and K∨ ={ξn≥ 0}. We put ξ =x +y, and use the notation vj = (vi)j
i=1. When
restricted to{xn =ξn = 0},f0((xn−1, 0), (ξn−1, 0)) =⟨Axyn−1,yn−1⟩+O(|yn−1|3),
for some Ax > 0. It follows that in general,
f0(x,ξ ) =⟨Axyn−1,yn−1⟩ +bxxn +cxξn +O(|yn−1|3 +|yn−1|(xn +ξn) +x2
n +ξ2
n),
where Ax,bx,cx > 0 are uniformly bounded from above and below by strict con-
vexity.
Thus
∫
K×K∨f0(x,ξ )z converges if and only if
∫
y2
1+···+y2
n−1<1
∫ 1
xn,ξn=0
(y2
1 +··· +y2
n−1 +xn +ξn)z <∞,
which immediately reduces to 2(Rez + 2) + (n− 2)>−1 ⇐⇒ Rez >−n+3
2 . □
In all the following we assume n = 2, as already this case appears to be inter-
esting and involved. We proceed to prove Theorem F.
Denote D+ ={(x,ξ );⟨x,ξ⟩ > 0}⊂ S2×S2. The group SO(3) acts diagonally
onS2×S2, leavingD+ invariant. By Ωi,j(S2×S2) we denote the diﬀerential forms
of bidegree (i,j ). We will use the function Rz(t) = 1−tz
1−t2 , which is smooth in t> 0
and analytic in z∈ C.
36 A Funk perspective on billiards, projective geometry and Mahler volume
Proposition 9.4. Forz∈ C, z⁄=−1, deﬁne ωz∈ Ω1,1(D+)SO(3) by
ωz := 1
z + 1Rz+1(⟨x,ξ⟩)⟨dx,ξ⟩∧⟨ x,dξ⟩.
Then dxdξωz =⟨x,ξ⟩zσxσξ.
Proof. Rather than verify the claimed equality, we will construct from scratch the
formωz with the required derivative. We write S2
x,S2
ξ for the corresponding copies
of the sphere.
Fix ξ and use it as the North Pole with associated polar coordinates θ,φ of
x∈ S2, where cos θ =⟨x,ξ⟩, and φ is the azimuth. We have σx = sinθdθdφ. It
holds that dφ(u) =− 1
sinθdθ(x×u), and diﬀerentiating cosθ =⟨x,ξ⟩ we ﬁnd
− sinθdθ =⟨dx,ξ⟩⇒ dφ = 1
sin2θ⟨x×dx,ξ⟩ =⟨x×dx,ξ⟩
1−⟨x,ξ⟩2 (14)
The forms dθ,⟨x×dx,ξ⟩ = sin 2θdφ are linearly independent in S2\{±ξ}, and
vanish at±ξ. Assume a 1-form ζz on S2
x of the form ζz = bz(θ)dφ is given, such
that dξωz =ζzσξ. Then
dζz =b′
z(θ)dθdφ +c0bz(0)δξ,
where c0 = 2π and δξ is the delta measure at ξ. Thus if bz(0) = 0, and b′
z(θ) =
sinθ coszθ, the desired equation would be satisﬁed. For this we take
bz(θ) = 1− cosz+1θ
z + 1
Now ﬁx x. We should ﬁnd an R3-valued Stab(x) = SO(2)-equivariant 1-formηz
on S2
ξ with
dξηz = 1−⟨x,ξ⟩z+1
1−⟨x,ξ⟩2 σξξ, (15)
whence we may take ωz = 1
z+1⟨x×dx,ηz⟩. It is easy to verify that
ηz =az(θ)dφ·x +cz(θ)dθ·x×ξ,
wherecz(θ) = 1−cosz+1θ
sinθ andaz(θ) =
∫θ
0 cz(τ) cosτdτ satisﬁes (15). The veriﬁcation
boils down to the equality
1− cosz+1θ
sinθ cosθdθdφ·x− 1− cosz+1θ
sinθ dθ·x×dξ = 1− cosz+1θ
sinθ dθdφ·ξ,
which in turn follows from (14) applied to S2
ξ , by taking scalar products with x,ξ
and x×ξ.
We ﬁnd that
ωz =− 1
z + 1⟨x×dx,ηz⟩ = 1
z + 1
1−⟨x,ξ⟩z+1
1−⟨x,ξ⟩2 ⟨dx,ξ⟩∧⟨ x,dξ⟩.
□
It follows by the Stokes theorem and using continuity to pass to the boundary
of D+, that for Rez≥ 0,
BK(z) =
∫
K×K∨
⟨x,ξ⟩z =
∫
∂K×∂K∨
ωz. (16)
37 A Funk perspective on billiards, projective geometry and Mahler volume
Example 9.1. Let us compute BK(z) for the spherical disc K = {x3 ≥ 1√
2},
satisfying K = K∨. Parametrize ∂K by x(α) = 1√
2(cosα, sinα, 1), and ∂Ko by
ξ(β) =L(x(β)) = 1√
2(− cosβ,− sinβ, 1), 0≤α,β ≤ 2π. Then:
⟨x,ξ⟩ = 1
2(1− cos(α−β)) = sin2 α−β
2
dx = 1√
2(− sinα, cosα, 0)dα, dξ = 1√
2(sinβ,− cosβ, 0)dβ
⟨dx,ξ⟩ = 1
2 sin(α−β)dα, ⟨dξ,x⟩ = 1
2 sin(β−α)dβ
Thus
BK(z) =− 1
4(z + 1)
∫ 2π
0
∫ 2π
0
1− (sin2 α−β
2 )z+1
1− sin4 α−β
2
sin2(α−β)dαdβ
=− 1
2(z + 1)
∫ π
−π
(2π− 2|γ|)1− (sin2γ)z+1
1− sin4γ sin2 2γdγ
=− 8
z + 1
∫ π
0
(π−γ)1− (sin2γ)z+1
1 + sin2γ sin2γdγ
=− 8
z + 1
∫ π
0
π
2
1− (sin2γ)z+1
1 + sin2γ sin2γdγ
=− 8π
z + 1
∫ π
2
0
1− (sin2γ)z+1
1 + sin2γ sin2γdγ,
where the penultimate equality is by symmetrizing the integrand around π
2 .
Putting t = sin2γ we get
BK(z) =− 4π
z + 1
∫ 1
0
1−tz+1
1 +t
√
t√1−tdt =− 4π
z + 1(π(1− 1√
2)−
∫ 1
0
tz+ 3
2dt
(1 +t)√1−t)
=− 4π
z + 1
(
π(1− 1√
2)−√π Γ(z + 5
2)
Γ(z + 3) 2F1(1,z + 5
2,z + 3;−1)
)
.
In particular, BK(−3) = 2π2.
Proposition 9.5. For K⊂ S2 smooth and strictly convex, BK(z) extends as a
meromorphic function with simple poles that are contained in {− 5
2,− 7
2,− 9
2,... }.
Proof. LetL :∂K→∂K∨ be the Legendre transform, deﬁned byLx =∂K∨∩x⊥.
It points in the unique direction perpendicular to both x and Tx∂K: since ⟨x,ξ⟩ :
∂K×∂K∨→ R is smooth and non-negative, its zeros are all minima and hence
critical points. That is, for ﬁxed ξ =Lx, we have⟨dx,ξ⟩ = 0. Parametrize ∂K by
arc-length, denoted x(α), and ∂K∨ byξ(β) =L(x(β)). It then holds that
⟨x(α),ξ (β)⟩ = (β−α)2u(α,β )
with u smooth, and by strict convexity u> 0. Similarly we have
⟨x′(α),ξ (β)⟩ = (β−α)v1(α,β ), ⟨ξ′(β),x (α)⟩ = (β−α)v2(α,β ),
withv1,v 2 smooth and non-zero when|α−β|≤ ϵ. Here ϵ> 0 is ﬁxed, and depends
on the lower bound on the curvatures of K,K∨.
38 A Funk perspective on billiards, projective geometry and Mahler volume
Recall eq. (16):
BK(z) =− 1
z + 1
∫
∂K×∂K∨
1−⟨x,ξ⟩z+1
1−⟨x,ξ⟩2 ⟨dx,ξ⟩∧⟨ dξ,x⟩.
Writingβ =α +φ, it follows that up to an addition of an entire function of z and
the factor 1
z+1, BK(z) equals
Bϵ
K(z) :=
∫ ϵ
−ϵ
dφ
∫ 2π
α=0
1−⟨x(α),ξ (α +φ)⟩z+1
1−⟨x(α),ξ (α +φ)⟩2 ⟨x′(α),ξ (α +φ)⟩⟨ξ′(α +φ),x (α)⟩dα
=hϵ(K)−
∫ ϵ
−ϵ
|φ|2z+4dφ
∫ 2π
α=0
u(α,α +φ)z+1˜v(α,φ )dα,
where hϵ(K) is a constant depending only on K, and ˜v is a smooth non-zero func-
tion.
The inner integral, denoted fz(φ), is an analytic family of smooth functions as
z∈ C. The function
∫ϵ
−ϵ|φ|2z+4fz(φ)dφ is then meromorphic in C, with simple
poles that are contained in a subset of {− 5
2,− 7
2,... }, corresponding to the simple
poles of the meromorphic family {|φ|2z+4} of even homogeneous distributions on
R. Also by Lemma 9.3, z =−1 is an analytic point of BK(z). This completes the
proof of the meromorphic extendibility of BK(z) with poles as stated. □
Proposition 9.6. The value BK(−3) is a projective invariant of K⊂ RP2.
Proof. Recall the symbolχg(x,ξ ) deﬁned in Lemma 9.1. For any ﬁxedg∈ PGL(V ),
we have by Lemma 9.2 the following equality for Re z >−1:
⟨1 g−1K×(g−1K)∨,µz⟩ =⟨g∗1 K×K∨,µz⟩ =⟨1 K×K∨,g∗µz⟩ (17)
=⟨χ−3−z
g−1 1 K×K∨,µz⟩.
We already established that one end (and hence both) of this equation admits a
meromorphic extension in z∈ C, which is analytic at z =−3. Let us verify that
the value of the right hand side at z =−3 equals BK(−3), implying projective
invariance.
Fix g∈ PGL(3), and consider h(z) =⟨χ−3−z
g−1 1 K×K∨,µz⟩ =
∫
K×K∨χ−3−z
g−1 dµz.
Writeψ(x,ξ ) = χg−1(x,ξ ), and note ψ is a smooth positive function. We now use
Proposition 9.4 and the Stokes theorem to write
h(z) =
∫
K×K∨
ψ(x,ξ )−z−3dxdξωz
=
∫
∂K×K∨
ψ−z−3dξωz + (z + 3)
∫
K×K∨
ψ−z−4dxψ∧dξωz
=
∫
∂K×∂K∨
ψ−z−3ωz− (z + 3)
∫
K×K∨
dξ(ψ−z−4dxψ)∧ωz
+ (z + 3)
∫
∂K×K∨
ψ−z−4dξψ∧ωz + (z + 3)
∫
K×∂K∨
ψ−z−4dxψ∧ωz
The ﬁrst summand admits a meromorphic extension by the same proof as that
for BK, and its value at z =−3 is
∫
∂K×∂K∨ω−3 = BK(−3). Consider next the
39 A Funk perspective on billiards, projective geometry and Mahler volume
second summand; by Lemma 9.3, the form ωz is L1 in K×K∨ for Rez >− 7
2,
implying the second summand is analytic in this range, and vanishes at z =−3.
The last two summands are treated similarly, so let us focus on the ﬁrst one.
Written explicitly, it is
z + 3
z + 1
∫
∂K×K∨
1−⟨x,ξ⟩z+1
1−⟨x,ξ⟩2 ⟨dx,ξ⟩∧⟨ x,dξ⟩∧ ψ−z−4dξψ.
It is easy to see that up to a summand that is analytic near, and vanishes at,
z =−3, the integral equals
I = z + 3
z + 1
∫
∂K×K∨
⟨x,ξ⟩z+1⟨x,dξ⟩∧⟨ dx,ξ⟩∧ ψ−z−4dξψ.
It holds that
1
z + 2d(⟨x,ξ⟩z+2)∧⟨dx,ξ⟩∧ ψ−z−4dξψ =⟨x,ξ⟩z+1⟨x,dξ⟩∧⟨ dx,ξ⟩∧ ψ−z−4dξψ.
Consequently we can integrate by parts to obtain
I =I1 +I2 = z + 3
(z + 1)(z + 2)
∫
∂K×∂K∨
⟨x,ξ⟩z+2⟨dx,ξ⟩∧ ψ−z−4dξψ
− z + 3
(z + 1)(z + 2)
∫
∂K×K∨
⟨x,ξ⟩z+2d(⟨dx,ξ⟩∧ ψ−z−4dξψ).
Let us rewrite the ﬁrst summand as
I1 = 1
(z + 1)(z + 2)
∫
∂K×∂K∨
dx(⟨x,ξ⟩z+3)∧ψ−z−4dξψ
=− 1
(z + 1)(z + 2)
∫
∂K×∂K∨
⟨x,ξ⟩z+3dx(ψ−z−4dξψ) (18)
We use the arc-length parametrization x(α), 0 ≤ α≤ L for ∂K, and ξ(β) =
L(x(β)), 0 ≤ β ≤ L for ∂K∨. Recall that by strict convexity, ⟨x(α),ξ (β)⟩ =
|β−α|2u(α,β ) with u >0 smooth. We will use C to denote a positive constant
that only depends on K and g, which may diﬀer between occurrences.
Consider the integral in (18). As z → −3, the integrand is majorized by
C|⟨x,ξ⟩|−1/4, which is integrable on ∂K×∂K∨. Thus by Lebesgue’s dominated
convergence theorem,
lim
z→−3
I1 =−1
2
∫
∂K×∂K∨
dx(ψ−1dξψ) = 0.
Next we consider I2. Let P : S2 → ∂K∨ be the nearest-point projection,
well-deﬁned in some open neighborhood U of ∂K∨. Deﬁne K∨
ϵ = {ξ ∈ U :
⟨ξ,L(Pξ )⟩≤ ϵ}, which is a one-sided tube around ∂K∨. We parametrize ∂K×K∨
ϵ
by (x(α),ξ (β,s )), 0≤α,β ≤L, 0≤s≤ϵ, where ξ =ξ(β,s ) is the point that has
P (ξ) =ξ(β),⟨ξ,L(P (ξ))⟩ =s.
Writeη =d(⟨dx,ξ⟩∧ ψ−z−4dξψ). We claim that the integral
∫
∂K×K∨
⟨x,ξ⟩z+2η (19)
converges for Rez >− 7
2.
40 A Funk perspective on billiards, projective geometry and Mahler volume
It is enough to consider the integral (19) in the smaller domain {|α−β|≤ ϵ, 0≤
s≤ ϵ}. There ⟨x(α),ξ (β,s )⟩≥ C max((β−α)2,s )≥ C((β−α)2 +s). It remains
to check that for Rez >− 7
2,
∫ ϵ
0
∫ ϵ
0
dsdφ
(s +φ2)−z−2 <∞,
which is clear. Consequently, lim z→−3I2 = 0 due to the ( z + 3) factor. This
concludes the proof of the statement.
□
Let us derive some equivalent expressions for BK(−3), working towards an ex-
plicit geometric formula. One has
BK(−3) =−1
2
∫
∂K×∂K∨
1−⟨x,ξ⟩z+1
1−⟨x,ξ⟩2 ⟨dx,ξ⟩∧⟨ x,dξ⟩
⏐⏐⏐⏐
z=−3
= 1
2
∫
∂K×∂K∨
⟨x,ξ⟩z+1 1−⟨x,ξ⟩−z−1
1−⟨x,ξ⟩2 ⟨dx,ξ⟩∧⟨ x,dξ⟩
⏐⏐⏐⏐
z=−3
= 1
2
∫
∂K×∂K∨
⟨x,ξ⟩z+1⟨dx,ξ⟩∧⟨ x,dξ⟩
⏐⏐⏐⏐
z=−3
= 1
2(z + 2)
∫
∂K×∂K∨
⟨dx,ξ⟩∧ d(⟨x,ξ⟩z+2)
⏐⏐⏐⏐
z=−3
= 1
2
∫
∂K×∂K∨
⟨x,ξ⟩z+2⟨dx,dξ⟩
⏐⏐⏐⏐
z=−3
.
BK(−3) = 1
2
∫
∂K×∂K∨
⟨dx,dξ⟩
⟨x,ξ⟩z
⏐⏐⏐⏐
z=1
(20)
= 1
2
∫
∂K×∂K∨
⟨dx,ξ⟩∧⟨ x,dξ⟩
⟨x,ξ⟩z
⏐⏐⏐⏐
z=2
(21)
Proposition 9.7. Let ∂K be parametrized by arc-length as x(α). The geodesic
curvature of ∂K is κ(α) = det(x(α),x′(α),x′′(α)). Then
BK(−3) = 1
2 lim
ϵ→0
∫
x∈∂K,ξ∈∂K∨,⟨x,ξ⟩≥ϵ2
⟨dx,ξ⟩∧⟨ x,dξ⟩
⟨x,ξ⟩2 + 2
√
2
ϵ
∫
∂K
√
κ(α)dα.
Proof. We carry out the regularization explicitly, using formula (21). Put L =
Length(x(α)), ξ(β) = L(x(β)) = x(β)×x′(β), and let α,β ∈ R be L-periodic
parameters.
We will write x(α)>ξ (β) if β <α<β + L
2 . Deﬁne for small values |t|≤ ϵ
gK(t) =
{ ∫
⟨x,ξ⟩=t2,x>ξ⟨dx,ξ⟩ , t ≥ 0∫
⟨x,ξ⟩=t2,x<ξ⟨dx,ξ⟩ , t< 0
Clearly gK is smooth in [−ϵ,ϵ ], and gK(0) = 0.
Let S(x,ξ ) =
√
⟨x,ξ⟩ be a signed square root deﬁned on ∂K×∂K∨ , which is
non-negative for x≥L (ξ), and non-positive for x≤L(ξ). Put t =S(x,ξ ), so t2 =
f0(x,ξ ) =⟨x,ξ⟩ and 2tdt =⟨dx,ξ⟩ +⟨x,dξ⟩, and⟨dx,ξ⟩∧⟨ x,dξ⟩ =−2tdt⟨dx,ξ⟩.
41 A Funk perspective on billiards, projective geometry and Mahler volume
It then holds that
BK(−3) = 1
2
∫
⟨x,ξ⟩≥ϵ2
⟨dx,ξ⟩∧⟨ x,dξ⟩
⟨x,ξ⟩2 −
∫ ϵ
0
gK(t)−gK(−t)− 2g′
K(0)t
t3 dt + 2
ϵg′
K(0),
and the middle summand approaches 0 as ϵ→ 0.
It remains to compute g′
K(0). Note that
gK(−t) =
∫
S(x,ξ)=−t
⟨dx,ξ⟩ =−
∫
S(ξ,x)=t
⟨dξ,x⟩ =−gK∨(t).
Parametrizingα =β +st(β), we have
t2 =⟨x(α),ξ (β)⟩ = 1
2st(β)2κ(β) +O(s3
t ).
Thus
st(β) =
√
2√
κ(β)
t +O(t2),
and writing
gK(t) =
∫ L
0
⟨x′(β +st(β)),x (β)×x′(β)⟩dβ,
⟨x′(β +st(β)),x (β)×x′(β)⟩ =
√
2κ(β)t +O(t2),
we ﬁnd
g′
K(0) =g′
K∨(0) =
√
2
∫ L
0
√
κ(β)dβ.
□
