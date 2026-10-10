---
doc_id: arxiv-1905.06064v1
doc_title: "ON O’HARA KNOT ENERGIES I: REGULARITY FOR CRITICAL KNOTS"
section_id: sec-001-2-a-new-energy-e
section_title: "A new energy E"
section_number: 2
pages: 4-26
source_pdf: 1905.06064v1.pdf
source_sha256: 3ffe25c8ee62779d
doc_brief: "ON O’HARA KNOT ENERGIES I: REGULARITY FOR CRITICAL KNOTS — We develop a regularity theory for extremal knots of scale invariant knot ener- gies deﬁned by J. O’hara in 1991."
---
critical knot (parametrized by arc-length) induces a criticalS2-valued map u and vice versa.
The main result in this section is the following equivalence between an energyEα,p which
will be deﬁned below and the O’hara energyOα,p.
Theorem 2.1. Forαp = 4, p≥ 2. Letγ : R/Z→ R3 be a knot parametrized with constant
speed with ﬁnite energyOα,p(γ)<∞.
Denote with u := c−1γ′ : R/Z→ S2 its unit tangent ﬁeld, where c≡|γ′|. Then (1)⇒ (2),
where
(1) γ is a critical knot forOα,p, that isOα,p(γ)<∞ and for anyϕ∈ C∞(R/Z, R3) we
have
δOα,p(γ,ϕ ) := d
dε
⏐⏐⏐⏐ε=0
Oα,p(γ +εϕ) = 0.
(2) u is a critical map forEα,p in the class of maps u : R/Z→ S2 with ﬁnite energy
Eα,p, that is for anyϕ∈ C∞(R/Z, R3) we have
d
dε
⏐⏐⏐⏐ε=0
Eα,p
( u +εϕ
|u +εϕ|
)
= 0.
Let us remark again that for the convenience of the reader we will refer to critical knots
when referring to criticality with respect to the O’hara energy Oα,p acting on in isotopy
classes, and a critical map when we refer to criticality with respect to the energy Eα,p as
maps between the manifolds R/Z→ S2. In principle both are of course critical points of
the respective energy in a certain domain.
The important advantage of u being a critical map in the above sense for Eα,p is that the
class of permissible is independent of the topological constraints of γ, and are exactly the
variations permitted for harmonic maps into S2 – thus the regularity theory for harmonic
maps comes into play.
To deﬁne properly the energyEα,p we ﬁrst ﬁx some notation for integrating on R/Z. The
reader may decide to skip the following notation and use common sense when interpreting
the meaning of respecitve integrals.
Remark 2.2 (Technicalities on integration on segments of R/Z). (1) We denote with
ρ(x,y ) the distance on R/Z, namelyρ(x,y ) =|x−y| mod 1.
(2) For x,y ∈ R/Z there are two geodesics. If x and y are not not antipodal (i.e.
|x−y| , 1
2) let x⊿y be the shortest geodesic (with orientation x toy), and for this
O’HARA KNOT ENERGIES I 5
case we deﬁne the integral, for Z-periodic f ,
∮
x⊿y
f ds :=
˜y∫
x
f (z) dz(z),
where ˜y∈y + Z such that|x− ˜y|< 1
2. Note that this is an integral with orientation
in the sense that ∮
x⊿y
f ds =−
∮
y⊿x
f ds
(3) We deﬁne the mean value integral on a segment S⊂ R/Z
−
∫
B
f := 1
H 1(S )
∫
S
f dH 1.
(i.e. the mean value is always without taking into account the orientation). In
particular,
( f )R/Z =
∫
R/Z
f =
1∫
0
f (z) dz.
Moreover we write
−
∫
x⊿y
f≡ −
∫
|x⊿y|
f = σ(x⊿y)
ρ(x,y )
∮
x⊿y
f ds,
where
σ(x⊿y) = sgn
∮
x⊿y
1,
that is σ(x⊿y) is +1 if x⊿y from x to y is positively oriented, and −1 if it is
negatively oriented. In particular,
−
∫
x⊿y
f = −
∫
y⊿x
f,
and
−
∫
x⊿y
f≥ 0 if f ≥ 0 on x⊿y.
(4) We then have the fundamental theorem of calculus in the following form. For any
non-antipodal points x,y∈ R/Z we have
f (y)− f (x) =
∮
x⊿y
f′(z) dz,
where f′ is the derivative.
With this notation, we can deﬁne the energy Eα,p. Firstly for two maps u,u : R/Z→ R3
we denote
(2.1) ⟨δu,δu⟩(x,y ) := −
∫
x⊿y
−
∫
x⊿y
(u(z1)− u(z2))· (u(z1)−u(z2)) dz1 dz2.
For nonnegative a, b, c we set
(2.2) F(a, b, c) :=

(
b− 1
2a
)−α
2
− c−α

p
2
.
6 SIMON BLATT, PHILIPP REITER, AND ARMIN SCHIKORRA
Also for later use deﬁne
(2.3) G(a) := F(a, 1, 1) =

(
1− 1
2a
)−α
2
− 1

p
2
.
Now the energyEα,p is deﬁned as follows.
(2.4)
Eα,p(u) =
∫
R/Z
∫
R/Z
F
⟨δu,δ u⟩(x,y ),−
∫
x⊿y
|u− (u)R/Z|2,−
∫
x⊿y
|u− (u)R/Z|
|u(x)−(u)R/Z|| u(y)−(u)R/Z| dx dy
ρ(x,y )αp/2.
We will see later, see Proposition 2.6, that Eα,p is comparable to the Gagliardo-norm
[u]p
W
α
2− 1p,p
, so we are formally in the realm of Wβ,p-harmonic maps into the sphere, for
which regularity theory has been developed by the third-named author [42], see also [35].
2.1. Properties ofEα,p. Letγ : R/Z→ R3 be a constant speed parametrization of a knot.
For c :=|γ′| we set u := c−1γ′.
In [5] the ﬁrst-named author characterized the energy space of knots with ﬁnite O’hara
energies. Which imply the following properties, Lemma 2.3 and Lemma 2.4.
Lemma 2.3. Wheneverγ has ﬁnite energyOα,p,αp = 4, p≥ 2, then there existsλ =λ(u)
such that
(2.5) sup
x,y∈R/Z
⟨δu,δ u⟩(x,y )≤λ.
Proof. In [5, Lemma 2.1] the ﬁrst-named author showed that wheneverγ has ﬁnite energy
Oα,p then there exists a bilipschitz constant L = L(γ)> 0 such that
L≤ γ(x)−γ(y)
|x−y| .
Consequently, since u = c−1γ′,
⟨δu,δ u⟩(x,y ) =
∮
x⊿y
∮
x⊿y
|u(s)− u(t)|2 ds dt
=c−2
∮
x⊿y
∮
x⊿y
|γ′(s)−γ′(t)|2 ds dt
=
∮
x⊿y
∮
x⊿y
2− 2
c2⟨γ′(s),γ′(t)⟩ ds dt
=
(
2− 2c−2|γ(y)−γ(x)|2
|x−y|2
)
≤2− 2c−2L2 =:λ.
□
Lemma 2.4. For s∈ [0,λ ] for someλ< 2,
|G(s)|≈ s
p
2.
the derivative
|G′(s)|≈ s
p−2
2 .
The constants depend onλ.
Proof. Firstly, for s∈ [0,λ ] with L’hopital one obtains
(
1− 1
2 s
)−α
2
− 1≈ s.
O’HARA KNOT ENERGIES I 7
Also for all s∈ [0,λ ],
(1− 1
2 s)≈ 1.
Finally compute and conclude with
G′(s) := αp
8

(
1− 1
2 s
)−α
2
− 1

p−2
2 (
1− 1
2 s
)−α+2
2
.
□
For u : R/Z→ S2 satisfying (2.5) and
∫
R/Z u = 0, the energyEα,p(u) is comparable to the
following W
α
2− 1
p,p-seminorm ⟦ f ⟧Wβ,p(R) which for an interval B is deﬁned as
⟦ f ⟧Wβ,p(B) =

∫
B
∫
B
⟨δ f,δ f⟩(x,y )
p
2
ρ(x,y )1+βp dx dy

1
p
.
The notion Wβ,p(B) is justiﬁed, since for β suﬃciently large in terms of p we have the
following equivalence to the usual Wβ,p-norm,
[ f ]Wβ,p(B) =

∫
B
∫
B
| f (x)− f (y)|p
ρ(x,y )1+βp dx dy

1
p
.
For
Proposition 2.5. For p∈ (1,∞),β∈ (0, 1) such that 1>β> 1
p− 1
2 we have (with constants
depeding on p, β)
⟦u⟧Wβ,p(R/Z)≈ [u]Wβ,p(R/Z).
The proof is given in the appendix, see Proposition A.1.
2.2. Proof of Theorem 2.1. We introduce an auxiliary energy ˜Eα,p which is the same as
Eα,p only that the third component in F, namely −
∫
x⊿y|u− (u)R/Z|, is replaced by
du(x,y ) := min

ρ(x,y )−
∫
x⊿y
|u(z)− (u)R/Z|, (1−ρ(x,y )) −
∫
R/Z\x⊿y
|u(z)− (u)R/Z|

.
Observe that when u =γ′ then du(x,y ) simpliﬁes to
du(x,y )≡D γ(x,y ) := min

ρ(x,y )−
∫
x⊿y
|u(z)|, (1−ρ(x,y )) −
∫
R/Z\x⊿y
|u(z)|

,
i.e. the intrinsic distance ofγ(x) toγ(y) alongγ.
That is,
˜Eα,p(u) =
∫
R/Z
∫
R/Z
F
⟨δu,δ u⟩(x,y ),−
∫
x⊿y
|u− (u)R/Z|2, du(x,y )
ρ(x,y )
|u(x)−(u)R/Z|| u(y)−(u)R/Z| dx dy
ρ(x,y )αp/2.
Then we have
Lemma 2.6. For any knotγ with ﬁnite energyOα,p we have
˜Eα,p(γ′) =Oα,p(γ).
If the knotγ is moreover arclength-parametrized or more generally constant speed,
Eα,p(γ′) =Oα,p(γ).
8 SIMON BLATT, PHILIPP REITER, AND ARMIN SCHIKORRA
Proof. Firstly, (γ′)R/Z = 0. ThusDγ(x,y ) = dγ′(x,y ), and we have
˜Eα,p(γ′) =
∫
R/Z
∫
R/Z
F
⟨δγ′,δγ′⟩(x,y ),−
∫
x⊿y
|γ′|2,Dγ(x,y )
ρ(x,y )
|γ′(x)||γ′(y)| dx dy
ρ(x,y )αp/2.
We have
F
⟨δγ′,δγ′⟩(x,y ),−
∫
x⊿y
|γ′|2,Dγ(x,y )
ρ(x,y )
 =

−
∫
x⊿y
|γ′|2− 1
2⟨δγ′,δγ′⟩

−α
2
−
( ρ(x,y )
Dγ(x,y )
)α

p
2
We recall⟨δγ′,δγ′⟩ deﬁned in (2.1). Then we have (the orientation cancels),
|γ(x)−γ(y)|2
ρ(x,y )2 = −
∫
x⊿y
|γ′|2− 1
2 −
∫
x⊿y
−
∫
x⊿y
|γ′(s)−γ′(t)|2 = −
∫
x⊿y
|γ′|2− 1
2⟨δγ′,δγ′⟩(x,y ).
Thus,
F
(
⟨δγ′,δγ′⟩(x,y ),−
∫
x⊿y|γ′|2,Dγ(x,y )
)
ρ(x,y )
αp
2
=
( 1
|γ(x)−γ(y)|α− 1
Dγ(x,y )α
) p
2
This shows ˜Eα,p(γ′) = ˜Oα,p(γ′).
Ifγ is arclength-parametrized,
Dγ(x,y )
ρ(x,y ) = 1 = −
∫
x⊿y
|u− (u)R/Z|.
Thus,Eα,p(γ′) = ˜Eα,p(γ′) for arclength parametrizedγ. □
Now we are ready to show
Proof of Theorem 2.1: (1)⇒ (2). Observe for any c> 0,
Eα,p(c−1γ′) = cαp−2Eα,p(γ′),
and
˜Eα,p(c−1γ′) = cαp−2 ˜Eα,p(γ′).
Thus, we shall assume w.l.o.g. γ′ = u (i.e. c≡ 1) without changing anything about the
criticality.
Forϕ∈ C∞(R/Z, R3) let
uε := u +εϕ
|u +εϕ|,
and
γε(x) :=γ(0) +
∮
0⊿x
(uε− (uε)R/Z
).
Then, since uε−γ′
ε = (uε)R/Z is constant, we ﬁnd
˜Eα,p(uε) = ˜Eα,p(uε− (uε)R/Z) = ˜Eα,p(γ′
ε).
On the other hand, by Lemma 2.6, for all smallε (so that the energies are ﬁnite),
Oα,p(γε) = ˜Eα,p(γ′
ε).
Moreover, we observe that
(2.6) uε = u +εΠ(u)ϕ + O(ε2), f
where Π(u) is the orthogonal projection onto TuS2,
Π(u)u =u−⟨u, u⟩u
O’HARA KNOT ENERGIES I 9
and
γε(x) =γ(x) +ε
∮
0⊿x
(Π(u)ϕ− (Π(u)ϕ)R/Z
) + O(ε2).
Thusγε is a variation ofγ, so because ofγ being by (i) a critical knot ofOα,p we have
(2.7) d
dε
⏐⏐⏐⏐ε=0
˜Eα,p(uε) = d
dε
⏐⏐⏐⏐ε=0
Oα,p(γε) = 0.
In order to make the step from ˜E toE, recall that the ˜E isE only replacing duε (x,y)
ρ(x,y) by
−
∫
x⊿y|uε(z)− (uε)R/Z|. We show that this does not change the derivative d
dε
⏐⏐⏐⏐ε=0
, by Lebesgue
theorem:
Firstly, by deﬁnition
duε(x,y )
ρ(x,y ) = min

−
∫
x⊿y
|uε(z)− (uε)R/Z|, (1−ρ(x,y ))
ρ(x,y ) −
∫
R/Z\x⊿y
|uε(z)− (uε)R/Z|

.
Since|u| = 1 and (u)R/Z = 0, for any x,y not antipodal,
−
∫
x⊿y
|uε(z)− (uε)R/Z| = 1 + O(ε).
Also,ρ(x,y )≤ 1 and thus
(1−ρ(x,y ))
ρ(x,y ) −
∫
R/Z\x⊿y
|uε(z)− (uε)R/Z| = (1−ρ(x,y ))
ρ(x,y ) + O(ε)≥ 1− O(ε).
Thus we have for any x,y not antipodal.
1− O(ε)≤ duε(x,y )
ρ(x,y ) ≤ 1 + O(ε).
Moreover,
sup
δ∈(0,ε)
⏐⏐⏐⏐⏐⏐⏐⏐
duε (x,y)
ρ(x,y) −
duδ (x,y)
ρ(x,y)
δ−ε
⏐⏐⏐⏐⏐⏐⏐⏐
= O(1).
On the other hand, pointwise almost everywhere,
d
dε
⏐⏐⏐⏐ε=0
duε(x,y )
ρ(x,y ) = d
dε
⏐⏐⏐⏐ε=0
−
∫
x⊿y
|uε(z)− (uε)R/Z|
and so by the Lebesgue convergence theorem we conclude
d
dε
⏐⏐⏐⏐ε=0
Eα,p(uε) = d
dε
⏐⏐⏐⏐ε=0
˜Eα,p(uε).
With (2.7) we conclude
d
dε
⏐⏐⏐⏐ε=0
Eα,p(uε) = 0.
Thus ifγ is an arclength-parametrized critical knot ofOα,p, then c−1γ′ is a critical map of
Eα,p in the class of mapsv : R/Z→ S2. □
Remark 2.7. We found the relation betweenEα,p andOα,p quite intriguing.
For example: to us it did not seem obious that (2)⇒ (1) in Theorem 2.1. By an argument
due to He [25] anyOα,p-variation of γ (constant-speed parmetrized) into the direction of
u = γ′ is trivial even if γ is not a critical knot. Indeed, this is a consequence of the
parametrization invariance of Oα,p. Moroever, Oα,p-variations of γ in direction u∧ u′
essentially correspond to Eα,p-variations of u in direction of T uS2, and thus vanish if u
is a critical map for Eα,p. However, Oα,p-variations of γ in the direction of u′ = γ′′
seem to correspond neither to reparametrizations ofγ nor to tangential variations ofEα,p.
10 SIMON BLATT, PHILIPP REITER, AND ARMIN SCHIKORRA
However, as our arguments shows,Oα,p-criticality with respect to this class of variations is
not necessary to obtain the regularity theory for knots – so in principle one could weaken
theorem I to critical knots with variations in fewer directions.
It also seems not fully clear to us what geometrical implication it is for a mapu : R/Z→ S2
to have ﬁnite energyE, in particular with respect to the (possibly not closed!) correspond-
ing curveγ(x) :=
∫ x
0 u(z) dz. (e.g. it seems not obvious that γ is injective).
3. R egularity theory forEα,p-critical maps: Proof of Theorem I
In view of Theorem 2.1 the claim of Theorem I is a consequence of the following theorem.
Theorem 3.1. Forαp = 4, p≥ 2 considerEα,p from (2.4).
Let u is a critical map forEα,p in the class of maps u : R/Z→ S2 with ﬁnite energyEα,p,
that is for anyϕ∈ C∞(R/Z, R3) we have
d
dε
⏐⏐⏐⏐ε=0
Eα,p
( u +εϕ
|u +εϕ|
)
= 0.
Then u∈ Cσ for someσ> 0.
We prove this theorem by extending the argument in [42] whereWβ,p-harmonic maps into
spheres were considered. See also [35] for a diﬀerent proof.
Remark 3.2. It is a natural question to ask whether it is possible to extend He’s argu-
ment, [25] see also [8], which shows smoothness of critical knots of the M¨ obius energy
that have an initial C 1,σ-regularity. But this argument depends heavily on the L 2-type of
the energy. From the theory of critical harmonic map-type equations one expects that once
C1,σ-regularity is obtained as in Theorem I the best possible regularity corresponds to the
best possible regularity of solutions to the homogeneous pde of the leading order operator
(which in the L 2-case is the linear fractional Laplacian |∇|β, and thus smoothness is to
be expected). In our L p-energy setting the corresponding equation involves however the
fractional p-Laplace equation for which maximal regularity is unknown. The best current
results for that operator has been obtained by Brasco and Lindgren, see [13, 14]. Regard-
ing convergence, observe that there are suitable stability results available for the fractional
p-Laplacian [34, 43, 3] which seem to carry over to our situation.
3.1. Euler-Lagrange equations of Eα,p. To compute the Euler-Lagrange equations of
Eα,p we introduce
Q(u,ϕ ) := 2
∫
R/Z
∫
R/Z
G′(⟨δu,δ u⟩(x,y ))⟨δu,δϕ⟩(x,y ) dx dy
ρ(x,y )αp/2,
and
R1(u,ϕ ) =
∫
R/Z
∫
R/Z
H(⟨δu,δ u⟩(x,y )) −
∫
x⊿y
u· (ϕ)R/Z
dx dy
ρ(x,y )αp/2.
with
H(a) = αp
2

(
1− 1
2a
)−α
2
− 1

p−2
2

(
1− 1
2a
)−α+2
2
− 1
.
Finally we set
R2(u,ϕ ) =
∫
R/Z
∫
R/Z
G(⟨δu,δ u⟩(x,y )) (u(x) + u(y))· (ϕ)R/Z
dx dy
ρ(x,y )αp/2.
Note that in view of Lemma 2.4.
(3.1) H(a), G(a)≈ a
p
2 for 0≤ a≤λ< 2
O’HARA KNOT ENERGIES I 11
Formally the Euler-Lagrange equations ofEα,p in the class of maps from R/Z into S2 are
then
(3.2) Q(u,·) +R1(u,·)−R 2(u,·)⊥ TuS2,
Remark 3.3. We shall see thatRi(u,·) are lower order terms which belong to (L1)∗, see
Proposition 3.5. Thus, one could interpret (3.2) as a fractional, nonlinear version of the
harmonic map equation
∆u⊥ TuS2
up to a lower-order termRi(u,·).
More precisely we have the following
Lemma 3.4 (Euler-Lagrange equations). Let u be a critical point of E in the class of
maps v : R/Z→ S2 and assume
∫
R/Z u = 0 as well as (2.5). Then for any testfunction
ϕ∈ W
1
p,p(R/Z, R3), which is also tangential,ϕ∈ TuS2,
δEα,p(u,ϕ ) =Q(u,ϕ ) +R1(u,ϕ )−R 2(u,ϕ ).
Proof. Of course this only holds almost everywhere, namely whenever x,y are not antipo-
dal. With a cutoﬀ argument we can make the following computations rigorous.
Recall that G(a) = F(a, 1, 1) where
F(a, b, c) :=

(
b− 1
2a
)−α
2
− c−α

p
2
.
Set uε := u +εϕ. We need to compute
d
dε
⏐⏐⏐⏐⏐ε=0
∫
R/Z
∫
R/Z
F (a(ε), b(ε), c(ε)) d(ε) e(ε) dx dy
ρ(x,y )
αp
2
.
Here, we set
a(ε) :=⟨δuε,δ uε⟩(x,y )
b(ε) := −
∫
x⊿y
|uε− (uε)R/Z|2
c(ε) := −
∫
x⊿y
|uε− (uε)R/Z|
d(ε) :=|uε(x)− (uε)R/Z|
e(ε) :=|uε(y)− (uε)R/Z|.
We ﬁrst observe that b(0) = c(0) = d(0) = e(0) = 1 since (u)R/Z = 0 and|u|≡ 1. We ﬁnd,
a(0) =⟨δu,δ u⟩(x,y ), a′(0) = 2⟨δu,δϕ⟩(x,y )
Next, sinceϕ· u≡ 0 and (u)R/Z = 0,
(3.3) b′(0) = 2c′(0) =−2−
∫
x⊿y
u· (ϕ)R/Z
Also
d′(0) =−u(x)· (ϕ)R/Z, e′(0) =−u(y)· (ϕ)R/Z
12 SIMON BLATT, PHILIPP REITER, AND ARMIN SCHIKORRA
Thus, we ﬁnd by product rule
d
dε
⏐⏐⏐⏐⏐ε=0
∫
R/Z
∫
R/Z
F (a(ε), b(ε), c(ε)) d(ε) e(ε) dx dy
ρ(x,y )
αp
2
=2
∫
R/Z
∫
R/Z
G′(⟨δu,δ u⟩(x,y ))⟨δu,δϕ⟩(x,y ) dx dy
ρ(x,y )
αp
2
+
∫
R/Z
∫
R/Z
d
dε
⏐⏐⏐⏐⏐ε=0
F (⟨δu,δ u⟩(x,y ), b(ε), c(ε)) dx dy
ρ(x,y )
αp
2
−
∫
R/Z
∫
R/Z
G (⟨δu,δ u⟩(x,y )) ( u(x) + u(y))· (ϕ)R/Z
dx dy
ρ(x,y )
αp
2
=Q(u,ϕ ) +R1(u,ϕ )−R 2(u,ϕ ).
To ﬁnd the form ofR1 we ﬁnally observe that with (3.3),
d
dε
⏐⏐⏐ε=0F(a(0), b(ε), c(ε))
=− αp
2

(
1− 1
2a(0)
)−α
2
− 1

p−2
2

(
1− 1
2a(0)
)−α+2
2
− 1
 c′(0)
=H(a(0))−
∫
x⊿y
u· (ϕ)R/Z.
□
From (3.1) we readily obtain
Proposition 3.5. For u satisfying (2.5) we have for i = 1, 2.
|Ri(u,ϕ )|≼ C(λ)‖u‖L∞ ⟦u⟧p
Wβ,p(R/Z)‖ϕ‖L1,
Observe that by Lemma 2.3 we haveλ =λ(u) is bounded away from 2, if u = c−1γ′ where
γ has ﬁnite O’hara energy.
3.2. Regularity theory: Left-hand side estimates. Recall that
Q(u,ϕ ) := 2
∫
R/Z
∫
R/Z
G′(⟨δu,δ u⟩(x,y ))⟨δu,δϕ⟩(x,y ) dx dy
ρ(x,y )αp/2,
where
G(s) :=

(
1− 1
2 s
)−α
2
− 1

p
2
,
For some interval B we denote the version ofQ restricted to iv asQB, that is
QB(u,ϕ ) := 2
∫
B
∫
B
G′(⟨δu,δ u⟩(x,y ))⟨δu,δϕ⟩(x,y ) dx dy
ρ(x,y )αp/2,
and as in [42] deﬁne the potential Γβ,Bu as
(3.4) Γβ,Bu(z) :=QB(u,|z−·| β−1).
The reason for taking such a potential is that |z− ˙|β−1 is the kernel of the Riesz potential
|∇|−(β),
|∇|−(β) f (x) =
∫
R
|z− x|β−1 f (z) dz.
O’HARA KNOT ENERGIES I 13
The Riesz potential of orderβ,|∇|−(β), has as an inverse the fractional Laplacian of orderβ,
|∇|β:
|∇|−(β)|∇|β f =|∇|β|∇|−(β) f = f for f∈ C∞
c (R).
The fractional Laplacian|∇|β is an an elliptic operator of diﬀerential orderβ which can be
described in diﬀerent ways. For β∈ (0, 1), it can be represented as an integro-di ﬀerential
operator
|∇|β f (x) = c
∫
R
f (y)− f (x)
|x−y|1+β dy,
or its Fourier symbol is c|ξ|β,
F
(
|∇|β f
)
(ξ) = c|ξ|βF ( f )(ξ).
The kernel|z|β−1 is the fundamental solution of the operator|∇|β (just as|z|2−n is the funda-
mental solution of−∆ =|∇|2 in dimension n≥ 3), which means
|∇|β (
|z− x|β−1)
=δx,z.
That is,
QB(u,·) =|∇|βΓβ,Bu.
or, by an integration by parts,
QB(u,ϕ ) = c
∫
R
Γβ,Bu(z)|∇|βϕ.
From now on we will assume that B is a small interval inside [0, 1] and that u is extended
to R\[−1, 2] as an W
1
p,p-map.
Proposition 3.6 (Left-hand side estimate). Let Br be an interval (x0− r, x0 + r), r∈ (0, 1
2).
If u : R/Z→ S2 satisﬁes (2.5) then for anyε> 0,
[u]p
W
1p,p(Br)
≼[u]W
1p,p(B2Lr)‖χB2K rΓβ,B2Lr u‖
L
1
1−β
+ε [u]p
W
1p,p(B2Lr)
+ Cε
(
[u]p
W
1p,p(B2Lr)
− [u]p
W
1p,p(Br)
)
for any L, K∈ N large enough.
Proof. In view of Proposition A.1, it su ﬃces to prove the estimate for ⟦u⟧W
1p,p. Recall
(2.1) and
⟦u⟧p
W
1p,p(Br)
=
∫
Br
∫
Br
(⟨δu,δ u⟩(x,y ))
p
2
ρ(x,y )2 dx dy,
with Lemma 2.4 (using the condition (2.5)),
≈
∫
Br
∫
Br
G′(⟨δu,δ u⟩(x,y ))⟨δu,δ u⟩(x,y ) dx dy
ρ(x,y )
αp
2
.
Letη∈ C∞
c (B2r),η≡ 1 on Br, with|∇kη|≤ C(k)r−k. Set (u)B2r = (2r)−1 ∫
B2r
u.
ψ(x) :=η(x)(u(x)− (u)B2r),
Observe that for x,y∈ Br,
⟨δu,δ u⟩(x,y ) =⟨δψ,δψ⟩(x,y ).
Thus, for any L≥ 0,
⟦u⟧p
W
1p,p(Br)
≼
∫
B2Lr
∫
B2Lr
G′(⟨δu,δ u⟩(x,y ))⟨δψ,δψ⟩(x,y ) dx dy
ρ(x,y )
αp
2
.
14 SIMON BLATT, PHILIPP REITER, AND ARMIN SCHIKORRA
Now we write
ψ(s)−ψ(t) =(u(s)− u(t))− (1−η(s))(u(s)− u(t))
+ (η(s)−η(t))(u(t)− (u)B2r).
and thus
⟦u⟧p
W
1p,p(Br)
≼ I− II + III
where
I :=
∫
B2Lr
∫
B2Lr
G′(⟨δu,δ u⟩(x,y ))⟨δu,δψ⟩(x,y ) dx dy
ρ(x,y )
αp
2
II :=−
∫
B2Lr
∫
B2Lr
G′(⟨δu,δ u⟩(x,y ))
ρ(x,y )−2 ∫ y
x
∫ y
x⟨(1−η(s))(u(s)− u(t)),ψ (s)−ψ(t)⟩ ds dt
ρ(x,y )
αp
2
dx dy
III :=
∫
B2Lr
∫
B2Lr
G′(⟨δu,δ u⟩(x,y ))
ρ(x,y )−2 ∫ y
x
∫ y
x
⟨(η(s)−η(t))(u(t)− (u)B2r
),ψ (s)−ψ(t)⟩ ds dt
ρ(x,y )
αp
2
dx dy
As for II , we have by H¨older p−2
p + 2
p = 1, and Jensen inequality and using Fubini/Lemma A.2-
arguments
|II|≼ ⟦u⟧p−2
W
1p,p(B2Lr)
[ψ]W
1p,p(B2Lr)

∫
B2Lr
∫
B2Lr
(1−η(s))p|u(t)− u(s)|p
|s− t|2 ds dt

1
p
We conclude as in [42, Proof of Lemma 3.2., Proposition D.1, Proposition D.2]. The same
way we estimate III . Also I can be estimated as in [42, Proof of Lemma 3.2.]. □
3.3. Estimates of the right-hand side. Since|u| = 1 a.e., we have the estimate
(3.5) ‖χB2K rΓβ,B2Lr u‖
L
1
1−β
≼‖χB2K r u· Γβ,B2Lr u‖
L
1
1−β
+‖χB2K r u∧ Γβ,B2Lr u‖
L
1
1−β
,
where u∧ denotes the R3-cross product with u.
Lemma 3.7. Forβ< 1
p large enough,
‖u· Γβ,B2Lr u‖
L
1
1−β
≼ [u]p
W
1p,p(B22Lr)
+
∞∑
k=1
2−σ(L+k)[u]p
W
1p,p(B22L+kr)
.
Proof. The fact that|u| = 1, implies
u(z)·
y∫
x
y∫
x
(u(s)− u(t))(|s− z|β−1−| t− z|β−1) ds dt
=− 1
2
y∫
x
y∫
x
(u(s)− u(t))(u(s) + u(t)− 2u(z))(|s− z|β−1−| t− z|β−1) ds dt.
Thus
|u(z)· Γβ,B2Lr u(z)|
≼
∫
B2Lr
∫
B2Lr
⟨δu,δ u⟩(x,y )
p−2
2
(
ρ(x,y )−2 ∫ y
x
∫ y
x χS (s, t)|u(s)− u||u(s) + u− 2u(z)|||s− z|β−1−| t− z|β−1| ds dt
)
ρ(x,y )2 dx dy
≼⟦u⟧p−2
W
1p,p(S )

∫
B2Lr
∫
B2Lr
(
|u(s)− u||u(s) + u− 2u(z)|
⏐⏐⏐|s− z|β−1−| t− z|β−1⏐⏐⏐
) p
2
|s− t|2 ds dt

2
p
.
O’HARA KNOT ENERGIES I 15
The arguments in [42, Lemma 6.5] then imply that if β < 1
p is large enough, the claim
follows. □
Lemma 3.8. Let u : R/Z→ S2 solve the Euler-Lagrange equation from Lemma 3.4, then
for any K∈ N large enough,
‖χB2K r u∧ Γβ,B210K r u‖
L
1
1−β
≼[u]p
W
1p,p(B220K r)
+ 2−σK[u]p−1
W
1p,p(B220K r)
+ [u]W
1p,p(R)
∞∑
k=1
2−σ(K+k)[u]p−1
W
1p,p(B220K+kr)
+ (22Kr) ⟦u⟧W
1p,p(R/Z)).
Proof. We follow the strategy in [42, Lemma 3.5].
Firstly, by duality we ﬁndg∈ C∞
c (B2Kr) so that‖g‖
L
1
β
≤ 1 and
‖χB2K r u∧ Γβ,B2Lr u‖
L
1
1−β
≼
∫
R
u(z)∧ Γβ,B2Lr u(z)g(z) dz = I +
∞∑
k=1
IIk,
with
I =
∫
R
|∇|β(ηB22K|∇|−(β)g)u(z)∧ Γβ,B2Lr u(z) dz
IIk =
∫
R
|∇|2( 1
p−β) (
|∇|β (
ηB22K+k+1\B22K+k|∇|−(β)g
)
u(z)∧
)
·|∇|−
(
2( 1
p−β)
)
Γβ,B2Lr u(z) dz
for the usual choice of cutoﬀ functions on segment and annuli.
First, we treat II . Observe that (forϕ :=|∇|2( 1
p−β) (
|∇|β
(
ηB22K+k+1\B22K+k|∇|−(β)g
)
u(z)∧
)
)
∫
ϕ(z)|∇|−
(
2( 1
p−β)
)
Γβ,B2Lr u(z) dz≤
∫
B2Lr
∫
B2Lr
(⟨δu,δ u⟩(x,y ))
p−2
2
ρ(x,y )2 ⟨δu,δ|∇|−
( 2
p−β
)
ϕ⟩(x,y )
≼⟦u⟧p−1
W
1p,p(B2Lr)
[|∇|−
( 2
p−β
)
ϕ]W
1p,p(R)
≼⟦u⟧p−1
W
1p,p(B2Lr)
‖ϕ‖
L
1
2p−β
.
In the last step we used Sobolev embedding and thatβ< 1
p.
This and the estimates of the remaining term of II (see [42, Proof of Lemma 3.5]) imply
the estimate for II .
As for I, we set (some other)ϕ := (ηB22K|∇|−(β)g), and have
‖|∇|βϕ‖
L
1
β
≤ 1.
Up to a three-commutator estimate which can be treated exactly as in [42, Proof of Lemma
3.5], we have to deal with
I1 :=
∫
|∇|β(ϕu∧) Γβ,B210K r u,
I2 :=
∫
ϕ|∇|β(u∧) Γβ,B210K r u,
16 SIMON BLATT, PHILIPP REITER, AND ARMIN SCHIKORRA
Regarding I1, we have.
I1 =
∫
B2Lr
∫
B2Lr
G′(⟨δu,δ u⟩)⟨δu,δ (ϕu∧)⟩(x,y )
ρ(x,y )
αp
2
dx dy
=
∫
R/Z
∫
R/Z
G′(⟨δu,δ u⟩)⟨δu,δ (ϕu∧)⟩(x,y )
ρ(x,y )
αp
2
dx dy
+ 2
∫
[0,1]\B2Lr
∫
B2Lr
G′(⟨δu,δ u⟩)⟨δu,δ (ϕu∧)⟩(x,y )
ρ(x,y )
αp
2
dx dy
+
∫
[0,1]\B2Lr
∫
[0,1]\B2Lr
G′(⟨δu,δ u⟩)⟨δu,δ (ϕu∧)⟩(x,y )
ρ(x,y )
αp
2
dx dy.
The ﬁrst term is the Euler-Lagrange operatorQ(u,ϕ u∧). With the Euler-Lagrange equation
forEα,p, (note that u∧ϕ∈ TuS2), Lemma 3.4,
|Q(u,γ∧ϕ)| =|R(u,ϕ )|≼Eα,p(u)‖ϕ‖L1≼ (22Kr)Eα,p(u).
As for the second term of I1,
∫
B2Lr
∫
R/Z\B2Lr
(⟨δu,δ u⟩(x,y ))
p
2−2⟨δu,δ (ϕu∧)⟩(x,y ) dx dy
ρ(x,y )
αp
2
.
can be estimated with Lemma B.1. As for the third term we observe that for large enough
L≿ K, for x,y∈ [0, 1]\B2Lr, either
ρ(x,y )≿ 2Kr,
or by the support ofϕ,
⟨δu,δ (ϕu∧)⟩(x,y ) = 0.
Thus,
∫
[0,1]\B2Lr
∫
[0,1]\B2Lr
G′(⟨δu,δ u⟩)⟨δu,δ (ϕu∧)⟩(x,y )
ρ(x,y )
αp
2
dx dy≼ 2−σK[u]W
1p,p(B220K r).
This estimates I1.
To estimate I2, we use the deﬁnition of Γβ,I, (3.4), and have
I2 =
∫
B210K r
∫
B210K r
G′(⟨δu,δ u⟩(x,y ))⟨δu,δ|∇|−(β)(ϕ|∇|βu∧)⟩⟩ dx dy
ρ(x,y )
αp
2
Now, as in [42, (3.13)], since u∧ u = 0,
⟨δu,δ (|∇|−(β)(ϕ|∇|βu∧)⟩ =ρ(x,y )−2
y∫
x
y∫
x
(u(s)− u(t))·θ(s, t) ds dt,
where
θ(s, t) = (|∇|−(β)(ϕ|∇|βu∧)(s)−|∇|−(β)(ϕ|∇|βu∧)(t)− 1
2(u∧ (s)− u∧ (t))(ϕ(s) +ϕ(t))
Now we can argue as in [42, Lemma 6.6] to obtain the claim.
□
O’HARA KNOT ENERGIES I 17
3.4. Proof of Theorem 3.1. As usual for the regularity theory of harmonic maps, one
needs to obtain a decay estimate of the localized energy (or the respective norm), from
which the H¨older continuity of the solution follows from an iteration argument. The decay
estimate is the following.
Proposition 3.9 (Decay estimate). Let u be a critical point ofEα,p for p≥ 2,αp = 4.
There existε> 0 andτ< 1 and L0 > 0 such that whenever for L≥ L0 and [u]W
1p,p(B2Lr) <ε
then
[u]p
W
1p,p(Br)
≼τ[u]p
W
1p,p(B2Lr)
+
∞∑
k=1
2−σ(L+k)[u]p
W
1p,p(B220L+kr)
Proof. From Proposition 3.6 we have for anyε> 0, and all L, K large enough
[u]p
W
1p,p(Br)
≼[u]W
1p,p(B2Lr)‖χB2K rΓβ,B2Lr u‖
L
1
1−β
+ε[u]p
W
1p,p(B2Lr)
+ Cε
(
[u]p
W
1p,p(B2Lr)
− [u]p
W
1p,p(Br)
)
.
From (3.5)
‖χB2K rΓβ,B2Lr u‖
L
1
1−β
≼‖χB2K r u· ΓB2Lr u‖
L
1
1−β
+‖χB2K r u∧ Γβ,B2Lr u‖
L
1
1−β
.
For Lemma 3.7 forβ< 1
p large enough,
‖u· Γβ,B2Lr u‖
L
1
1−β
≼ [u]p
W
1p,p(B22Lr)
+
∞∑
k=1
2−σ(L+l)[u]p
W
1p,p(B22L+𝓁r)
.
From Lemma 3.8, since the energy is ﬁnite,
‖χB2K r u∧Γβ,B210K r u‖
L
1
1−β
≼ [u]p
W
1p,p(B220K r)
+2−σK[u]p−1
W
1p,p(B220K r)
+
∞∑
k=1
2−σ(K+k)[u]p−1
W
1p,p(B220K+kr)
+(22Kr).
Plugging this together, we obtain for all L large enough,
[u]p
W
1p,p(Br)
≼
(
[u]W
1p,p(B2Lr) +ε + 2−σL
)
[u]p
W
1p,p(B2Lr)
+ Cε
(
[u]p
W
1p,p(B2Lr)
− [u]p
W
1p,p(Br)
)
+
∞∑
k=1
2−σ(L+k)[u]p
W
1p,p(B220L+kr)
Using the hole-ﬁlling technique, adding Cε[u]p
W
1p,p(Br)
to both sides, for small enoughε and
large enough L, whenever [u]W
1p,p(B2Lr) <ε , for someτ< 1
[u]p
W
1p,p(Br)
≼τ[u]p
W
1p,p(B2Lr)
+
∞∑
k=1
2−σ(L+k)[u]p
W
1p,p(B220L+kr)
□
Proof of Theorem 3.1. Iterating the estimate from Proposition 3.9 on small balls, cf. [8,
Lemma A.8], we ﬁndσ> 0 such that
sup
r>0,x∈R/Z
r−σ [u]W
1p,p(Br(x))≼ C(u).
From Sobolev embedding on Morrey spaces, [2] we obtain thatu∈ C ˜σ for any ˜σ<σ . □
4. E xtremal casesα = 4 andα = 0, and no M¨obius inv ariance forp = 2
The following deﬁnition goes back to Gromov [22], see also O’hara [39].
Deﬁnition 4.1 (distortion). For any curveγ∈ C0(R/Z, Rd) let
distorγ := sup
x,y∈R/Z
x,y
Dγ(x,y )
|γ(x)−γ(y)|
ifγ is injective and distorγ :=∞ else.
18 SIMON BLATT, PHILIPP REITER, AND ARMIN SCHIKORRA
Lemma 4.2. Letγ∈ C0,1(R/Z, Rd) be parametrized by arc-length. Then
lim inf
α↘0
1
α
(
Oα,4/α(γ)
)α/4
≥ log distorγ.
Proof. We may assume thatγ is injective since otherwiseOα,4/α(γ) would be inﬁnite. We
compute
1
α
( 1
|γ(x)−γ(y)|α− 1
Dγ(x,y )α
)
= 1
α|γ(x)−γ(y)|α
(
1−|γ(x)−γ(y)|α
Dγ(x,y )α
)
= 1
|γ(x)−γ(y)|α
α−1∫
|γ(x)−γ(y)|
Dγ(x,y)
ξ−1 dξ.
On|x−y|≥ δ> 0 the integral uniformly converges,
1∫
|γ(x)−γ(y)|
Dγ(x,y)
ξα−1 dξ
α↘0
−−−→
1∫
|γ(x)−γ(y)|
Dγ(x,y)
ξ−1 dξ = log Dγ(x,y )
|γ(x)−γ(y)|,
i.e., for given ε >0 there is some α0 = α0(δ,ε) > 0 such that, for any α∈ (0,α 0), these
two quantities diﬀer at most byε.
By deﬁnition of distortion, for given ε >0 we may choose points x0,y 0∈ R/Z, x0 , y0,
such that
(distorγ≥) Dγ(x0,y 0)
|γ(x0)−γ(y0)|≥ e−ε distorγ.
Moreover, we may ﬁnd someδ =δ(ε)> 0 such that theδ-neighborhoods of x0 andy0 are
disjoint in R/Z and
Dγ(x,y )
|γ(x)−γ(y)|≥ e−2ε distorγ for all x∈ Bδ(x0),y∈ Bδ(y0).
For anyα∈ (0,α 0) we arrive at
"
(R/Z)2
[ 1
α
( 1
|γ(x)−γ(y)|α− 1
Dγ(x,y )α
)]2/α
dx dy
≥
∫
Bδ(x0)
∫
Bδ(y0)
[ 1
α
( 1
|γ(x)−γ(y)|α− 1
Dγ(x,y )α
)]2/α
dy dx
=
∫
Bδ(x0)
∫
Bδ(y0)
1
|γ(x)−γ(y)|2

1∫
|γ(x)−γ(y)|
Dγ(x,y)
ξα−1 dξ

2/α
dy dx
≥
∫
Bδ(x0)
∫
Bδ(y0)
1
|γ(x)−γ(y)|2
(
log Dγ(x,y )
|γ(x)−γ(y)|−ε
)2/α
dy dx
≥
∫
Bδ(x0)
∫
Bδ(y0)
1
|γ(x)−γ(y)|2
(log distorγ− 3ε)2/α dy dx
≥ (log distorγ− 3ε)2/α (2δ)2
(|x0−y0|R/Z + 2δ)2.
Thus we arrive at
lim inf
α↘0
1
α
(
Oα,4/α(γ)
)α/4
≥ log distorγ− 3ε.
O’HARA KNOT ENERGIES I 19
□
Lemma 4.3. Let γ∈ C1,β(R/Z, Rd) for some β∈ (0, 1] be parametrized by arc-length.
Then
lim sup
α↘0
1
α
(
Oα,4/α(γ)
)α/4
≤ log distorγ.
Proof. We may assume thatγ is injective since otherwise its distortion would be inﬁnite.
As in the preceding proof we have
1
α
( 1
|γ(x)−γ(y)|α− 1
Dγ(x,y )α
)
= 1
α|γ(x)−γ(y)|α
(
1−|γ(x)−γ(y)|α
Dγ(x,y )α
)
= 1
|γ(x)−γ(y)|α
1∫
|γ(x)−γ(y)|
Dγ(x,y)
ξα−1 dξ
≤ 1
|γ(x)−γ(y)|α
1∫
|γ(x)−γ(y)|
Dγ(x,y)
ξ−1 dξ
= 1
|γ(x)−γ(y)|α log Dγ(x,y )
|γ(x)−γ(y)|.
(4.1)
We compute for some constant C > 0 only depending onγ
1≥|γ(x)−γ(y)|2
|x−y|2
=
⏐⏐⏐⏐⏐⏐⏐⏐⏐
1∫
0
γ′(x +θ(y− x)) dθ
⏐⏐⏐⏐⏐⏐⏐⏐⏐
2
=
"
[0,1]2
⟨γ′(x +θ1(y− x)),γ′(x +θ2(y− x))⟩ dθ2 dθ1
= 1− 1
2
"
[0,1]2
⏐⏐⏐γ′(x +θ1(y− x))−γ′(x +θ2(y− x))
⏐⏐⏐2
dθ2 dθ1
≥ 1− C|x−y|2β.
This is bounded below by 1
2 provided|x−y|≤ (2C)−1/2β (we also assume|x−y|≤ 1
2). In
this case, the right-hand side of (4.1) is majorized by
1
|γ(x)−γ(y)|α log Dγ(x,y )
|γ(x)−γ(y)|
≤ 1
2|x−y|α (1− C|x−y|2β)α log Dγ(x,y )2
|γ(x)−γ(y)|2
≤ 1
21−α|x−y|α log |x−y|2
|γ(x)−γ(y)|2
≤ 1
21−α|x−y|α log 1
1− C|x−y|2β
≤ 2α−1 C|x−y|2β−α
1− C|x−y|2β
≤ 2αC|x−y|2β−α.
20 SIMON BLATT, PHILIPP REITER, AND ARMIN SCHIKORRA
On the other hand, if|x−y|≥ (2C)−1/2β we have
|γ(x)−γ(y)|≥ c> 0
by injectivity. Lettingε∈
(
0, (2C)−1/2β
)
andα< 4β we arrive at
1
α
(
Oα,4/α(γ)
)α/4
=

∫
R/Z
1/2∫
−1/2
[ 1
α
( 1
|γ(x)−γ(y)|α− 1
Dγ(x,y )α
)]2/α
dw du

α/4
≤
("
|x−y|≥(2C)−1/2β
···
)α/4
+
("
|x−y|≤(2C)−1/2β
···
)α/4
≤

"
|x−y|≥ε
1
c2
(
log |x−y|
|γ(x)−γ(y)|
)2/α
dw du

α/4
+
("
|x−y|≤(2C)−1/2β
4C2/α|x−y|4β/α−2 dw du
)α/4
≤ 1
cα log distorγ + C

8ε4β/α−1
4β
α − 1

α/4
≤ 1
cα log distorγ + C
( 8α
4β−α
)α/4
ε2β−α/4
α↘0
−−−→log distorγ + Cε2β.
□
Subsuming the past two results we obtain
Corollary 4.4. Letγ∈ C1,β(R/Z, Rd) for some β∈ (0, 1] be parametrized by arc-length.
Then
1
α
(
Oα,4/α(γ)
)α/4 α↘0
−−−→log distorγ.
Corollary 4.5. There is someα0∈ (0, 2] such thatOα,4/α is not M¨ obius invariant for any
α∈ (0,α 0).
The preceding statement immediately follows from
Example 4.6 (Distortion is not M¨obius invariant). We consider the square
Q =
{
(x,y )∈ R2 ⏐⏐⏐ max (|x|,|y|)≤ 1
}
which we identify with an arbitrary (injective) arc-length parametrization. In order to see
distor Q = 2 we consider the quotient Dγ(x,y)
|γ(x)−γ(y)| for diﬀerent conﬁgurations of x,y ∈ R/Z,
x ,y. If x,y belong to the same edge of Q it clearly amounts to1 while we arrive at
√
2 in
case of x,y belonging to neighboring edges. For opposite edges we evaluate the quotient at
points (ξ,−1) and (η, 1),ξ,η∈ [−1, 1]. Without loss of generality we may assumeξ+η≥ 0,
thus dQ(x,y)
|Q(x)−Q(y)| = 4−ξ−η√
22+(ξ−η)2
≤ 2 with equality ifξ =η = 0.
Now we perform an inversion on the unit circle x 2 +y2 = 1. It maps the edges of Q onto
segments of the circles passing to the origin and tangentially meeting the intersection of
Q with the axes, see Figure 1 (left). The points ±(1, 1) are mapped to±
( 1
2, 1
2
)
while the
length of the two arcs joining them now amounts toπ. The distortion of the inversion of Q
is therefore bounded below by π√
2 > 3√
2 > 2.
O’HARA KNOT ENERGIES I 21
1
-1
0
inverted square
1
-1 0
square
0
1
-4 - π
inverted stadion curve
-2 -1 0 1
-1
stadion curve
Figure 1. The square Q (left) and a station curve σ (right) inverted on
the unit circle.
Conjecture 1.2 means that we haveα0 = 2 in Corollary 4.5.
Rather than providing a rigorous proof of the preceding statement by suitably decomposing
the integration domain and carefully estimating based on techniques from [7], we illustrate
the situation by providing a numerical experiment that supports the latter conjecture (and
which we believe should be possible to be made rigorous with a careful, lengthy computa-
tion).
To this end, we consider the stadion curve σ depicted in Figure 1 (right) which is con-
structed by vertically cutting the unit circle into two half circles and horizontally delating
the left one byπ. This gives distorσ =π.
Now we approximate the energy values 1
α
(
Oα,4/α
)α/4
, α∈ (0, 2], for the (unit) circle, the
stadion curve σ and its inversion on the unit circle. We employ a straightforward mid-
point based quadrature. Let
(
x j
)
j=1,...,N⊂ R2 denote a set of vertices which form a polyg-
onal approximation of the curve. As it is assumed to be closed, we set x j±N = x j for all
j = 1,..., N. So the approximative length L = ∑N
𝓁=1
⏐⏐⏐x j+1− x j
⏐⏐⏐ is well-deﬁned. For any
j, k∈{ 1,..., N}, j≤ k, we let d j,k = dk, j = min
(∑k−1
𝓁= j
⏐⏐⏐x j+1− x j
⏐⏐⏐, L− ∑k−1
𝓁= j
⏐⏐⏐x j+1− x j
⏐⏐⏐
)
.
Furthermore, we set ∆ j = 1
2
(⏐⏐⏐x j+1− x j
⏐⏐⏐ +
⏐⏐⏐x j− x j−1
⏐⏐⏐
)
. In order to avoid cancellation eﬀects
forα↘ 0 which occur when evaluating the approximative energy value
1
α

N∑
j,k=1

1⏐⏐⏐x j+1− x j
⏐⏐⏐α− 1
dα
j,k

2/α
∆ j∆k

α/4
,
we use the (algebraically equal) term
logβ

N∑
j,k=1
1⏐⏐⏐x j+1− x j
⏐⏐⏐2

1−
(|x j+1−x j|
d j,k
)α
α logβ

2/α
∆ j∆k

α/4
whereβ = max j,k=1,...,N
d j,k
|x j−xk| approximates the distortion.
The results presented in Figure 2 suggest thatOα,4/α is not M¨obius invariant unlessα = 2.
In this experiment we have chosen N = 1000. We ﬁnd that our values for the circle agree
with those obtained using the integral formula derived by Abrams et al. [1, (24)] up to a
relative error of about 10−3.
Whenα→ 4 (or p→ 1) we converge to the total curvature functional.
Proposition 4.7. Ifγ : R/Z→ R3 is a constant speed, bilipschitz parametrization of a
knot then
lim
α→4−
4−α
4 Oα, 4
α (γ) = c
∫
R/Z
|γ′′|.
22 SIMON BLATT, PHILIPP REITER, AND ARMIN SCHIKORRA
3
4
0
stadion curve
0.5 1
inverted stadion curve
1.5 20
log π
2
log π
2
circle
Figure 2. Plot of α↦→ 1
α
(
Oα,4/α
)α/4
for the circle and the curves depicted
in Figure 1 (right).
Proof. We have by Lemma 2.6,
Oα, 4
α (γ) =Eα, 4
α (γ′).
From Lemma 2.4
Eα, 4
α (γ′)≈ ⟦u⟧p
W
α
4, 4α (R/Z)
In view of Proposition 2.5
⟦γ′⟧
4
α
W
α
4, 4α (R/Z)
≈ [γ′]
4
α
W
α
4, 4α (R/Z)
.
From [12] we know that
lim
α→4−
(
1− 4
α
)
[γ′]
4
α
W
α
4, 4α (R/Z)
≈
∫
R/Z
|γ′′|
The claim follows. □
Appendix A. A new norm for Wβ,p
Let
⟨δu,δv⟩(x,y ) :=
1∫
0
1∫
0
(u(x + s(y− x))− u(x + t(y− x)))· (v(x + s(y− x))−v(x + t(y− x))) ds dt
=ρ(x,y )−2
y∫
x
y∫
x
(u(s)− u)· (v(s)−v(t)) ds dt
We set
⟦u⟧Wβ,p(S ) :=

∫
B
∫
B
(⟨δu,δ u⟩(x,y ))
p
2
ρ(x,y )1+βp dx dy

1
p
.
The semi-norm ⟦u⟧Wβ,p(S ) is equivalent to the usual Wβ,p-seminorm for β large enough –
note that in particular for our situation where p = 1
s this equivalence holds. Here
[u]Wβ,p(S ) :=

∫
B
∫
B
|u(x)− u(y)|
p
2
ρ(x,y )1+βp dx dy

1
p
.
O’HARA KNOT ENERGIES I 23
Proposition A.1. For p∈ (1,∞),β∈ (0, 1) so thatβ> 1
p− 1
2 we have for any u∈ C∞
c (R),
for any interval B⊆ R,
(A.1) ⟦u⟧Wβ,p(S )≼ [u]Wβ,p(S ).
The constant is independent of u and I.
For p∈ (1,∞),β∈ (0, 1) so thatβ> 1
p− 1
2(p−1) we have for any u∈ C∞
c (R),
(A.2) [ u]Wβ,p(R)≼ ⟦u⟧Wβ,p(R).
There is a ﬁxed number L ∈ N so that for any compact interval B ρ⊂ R of sidelength ρ
denoting with B2Lρ the concentric interval with sidelength 2Lρ, we have for a ﬁxed
(A.3) [ u]Wβ,p(Bρ)≼ ⟦u⟧Wβ,p(B2Lρ).
To see this we need the following two Lemmata.
Lemma A.2. Let A(s, t)⊂ R2 be the set
(A.4) ( x,y )∈ A(s, t)⇔ min{x,y}< s, t< max{x,y}.
Then for anyµ> 0, and any s , t
(A.5)
∫
A(s,t)
ρ(x,y )−2−µd(x,y ) = 2
µ(1 +µ)|t− s|−µ.
Proof. W.l.o.g. s< t. Then by symmetry we have
∫
A(s,t)
ρ(x,y )−2−µdy dx
=2
s∫
x=−∞
∞∫
y=t
ρ(x,y )−2−µdy dx
=2
s∫
x=−∞
∞∫
y=t−x
|y|−2−µdy dx
= 2
1 +µ
s∫
x=−∞
(t− x)−1−µdx
= 2
1 +µ
∞∫
ρ=t−s
(ρ)−1−µdρ
= 2
µ(1 +µ)(t− s)−µ.
□
Lemma A.3. Let p > 0,β∈ (0, 1), q∈ (1,∞) so thatβ > 1
pq− 1
q then for any u∈ C∞
c (R)
and any interval B⊆ R,
(A.6)
∫
B
∫
B
(
ρ(x,y )−2 ∫ y
x
∫ y
x|u(s)− u(t)|q ds dt
)p
ρ(x,y )1+βpq dx dy≼ [u]pq
Wβ,pq(S ).
Also for I⊆ R an interval,
(A.7)
∫
R
∫
R
(
ρ(x,y )−2 ∫ y
x
∫ y
x χS (s, t)|u(s)− u(t)|q ds dt
)p
ρ(x,y )1+βpq dx dy≼ [u]pq
Wβ,pq(S ).
24 SIMON BLATT, PHILIPP REITER, AND ARMIN SCHIKORRA
Proof. The (A.7) follows the same way as (A.6). We just prove the latter one.
If p≥ 2, with Jensen’s inequality
(
ρ(x,y )−2 ∫ y
x
∫ y
x|u(s)− u(t)|q ds dt
)p
ρ(x,y )1+βpq ≤ρ(x,y )−3−βpq
y∫
x
y∫
x
|u(s)− u(t)|pq ds dt.
With Fubini (note that s, t∈ I if x,y∈ I), setting A(s, t) as in (A.4) and using (A.5),
∫
B
∫
B
(
ρ(x,y )−2 ∫ y
x
∫ y
x|u(s)− u(t)|q ds dt
)p
ρ(x,y )1+βpq dx dy
≼
∫
B
∫
B
|u(s)− u(t)|pq
∫
A(s,t)
ρ(x,y )−3−βpq d(x,y ) ds dt
=c
∫
B
∫
B
|u(s)− u(t)|pq|s− t|−1−βpq ds dt
=[u]pq
Wβ,pq(S ).
Now assume 0 < p < 2, then Jensen’s inequality fails. We use instead Poincar `e-Sobolev
inequality Wα,pq((x,y ))⊂ Lq((x,y )) for α∈ (0, 1) satisfying α≥ 1
pq− 1
q. More precisely
we have the estimate
ρ(x,y )−2
y∫
x
y∫
x
χS (s, t)|u(s)− u(t)|q ds dt
≼ρ(x,y )αq− 1
p

y∫
x
y∫
x
χS (s, t)|u(s)− u(t)|pq
|s− t|1+αpq ds dt

1
p
Observe that this estimate would have followed from directly H¨older’s inequality forp≥ 1.
We need it however for p> 0.
We arrive at
(
ρ(x,y )−2 ∫ y
x
∫ y
x|u(s)− u(t)|q ds dt
)p
ρ(x,y )1+βpq ≤ρ(x,y )−2−(s−α)pq
y∫
x
y∫
x
|u(s)− u(t)|pq
|s− t|1+αpq ds dt
Our assumption on s implies that we may pickα< s. Then we may employ again Fubini,
again having A(s, t) as in (A.4) and using (A.5),
∫
B
∫
B
(
ρ(x,y )−2 ∫ y
x
∫ y
x|u(s)− u(t)|q ds dt
)p
ρ(x,y )1+βpq dx dy
≼
∫
B
∫
B
|u(s)− u(t)|pq
|s− t|1+αpq
∫
A(s,t)
ρ(x,y )−2−(s−α)pq d(x,y ) ds dt
(A.5)
= c
∫
B
∫
B
|u(s)− u(t)|pq|s− t|−1−βpq ds dt = [u]pq
Wβ,pq(S ).
□
From Lemma A.3 follows Proposition A.1.
Proof of Proposition A.1. The estimate (A.1) follows directly from Proposition A.1.
O’HARA KNOT ENERGIES I 25
For (A.2) we employ a duality argument. We have
[u]p
Wβ,p(S )
=
∫
B
∫
B
|u(s)− u(t)|p−2(u(s)− u(t))· (u(s)− u(t))
|s− t|1+βp ds dt
=c
∫
B
∫
B
|u(s)− u(t)|p−2(u(s)− u(t))· (u(s)− u(t))
∫
A(s,t)
ρ(x,y )−(3+βp) d(x,y ) ds dt,
where A(s, t)⊂ R2 is deﬁned as in (A.4).
With Fubini’s theorem we then have
[u]p
Wβ,p(S )
=c
∫
R
∫
R
ρ(x,y )−2 ∫ y
x
∫ y
x χI(s, t)|u(s)− u(t)|p−2(u(s)− u(t))· (u(s)− u(t))ds dt
ρ(x,y )1+βp dx dy,
Let us for now assume that I = R, then simply with H¨older’s inequality,
≤c
∫
R
∫
R
(
ρ(x,y )−2 ∫ y
x
∫ y
x χI(s, t)|u(s)− u(t)|(p−1)2 ds dt
) 1
2
(
ρ(x,y )−2 ∫ y
x
∫ y
x χI(s, t)|u(s)− u(t)|2 ds dt
) 1
2
ρ(x,y )1+βp dx dy
≤c

∫
R
∫
R
(
ρ(x,y )−2 ∫ y
x
∫ y
x|u(s)− u(t)|(p−1)2 ds dt
) p′
2
ρ(x,y )1+βp dx dy

1
p′
⟦u⟧Wβ,p(R)
Because of s> 1
p− 1
2(p−1), from Lemma A.3 we obtain

∫
R
∫
R
(
ρ(x,y )−2 ∫ y
x
∫ y
x|u(s)− u(t)|(p−1)2 ds dt
) p′
2
ρ(x,y )1+βp dx dy

1
p′
≼ [u]
p
p′
Wβ,p(R).
This proves (A.2).
If B is a compact interval, we have by the above estimates
[u]p
Wβ,p(Bρ)
≼[u]p−1
Wβ,p(Bρ) ⟦u⟧Wβ,p(B2Lρ)
+
∫
R
∫
R
χR\B2Lρ(x,y )
ρ(x,y )−2 ∫ y
x
∫ y
x χBρ(s, t)|u(s)− u(t)|p−2(u(s)− u(t))· (u(s)− u(t))ds dt
ρ(x,y )1+βp dx dy
Since we have disjoint support, we can be rough and estimate
∫
R
∫
R
χR\B2Lρ(x,y )
ρ(x,y )−2 ∫ y
x
∫ y
x χBρ(s, t)|u(s)− u(t)|p−2(u(s)− u(t))· (u(s)− u(t))ds dt
ρ(x,y )1+βp dx dy
≼
∫
Bρ
∫
Bρ
|u(s)− u(t)|p ds dt
∫
x<Bρ
∫
y>B2Lρ
ρ(x,y )−2
ρ(x,y )1+βp dx dy
≼2L(−1−βp)[u]p
Wβ,p(Bρ).
Having L be chosen large enough, we can absorb and ﬁnished proving (A.3). □
26 SIMON BLATT, PHILIPP REITER, AND ARMIN SCHIKORRA
Appendix B. C omputations
Lemma B.1. Forϕ∈ C∞
c (Bρ), L∈ N, k∈ N, we have the estimate

∫
B2Lρ
∫
B2L+kρ\B2L+k−1
1
ρ(x,y )2
ρ(x,y )−2
y∫
x
y∫
x
|u(s)− u(t)||ϕ(s)v(s)−ϕ(t)v(t)| ds dt

p
2
dx dy

2
p
≼2−s(L+k)‖v‖∞ [u]W
1p,p(B2L+kρ)‖|∇|
1
pϕ‖Lp
.
Proof. W.l.o.g. Bρ is centered around 0.
Note that the support ofϕ tells us that whenever x,y>ρ or x,y< −ρ,
1
ρ(x,y )2
ρ(x,y )−2
y∫
x
y∫
x
|u(s)− u(t)||ϕ(s)v(s)−ϕ(t)v(t)| ds dt

p
2
≡ 0.
Thus, it suﬃces to estimate
ρ∫
−2Lρ
2L+kρ∫
2L+k−1ρ
1
ρ(x,y )1+ 1
p
ρ(x,y )−2
y∫
x
y∫
x
|u(s)− u(t)||ϕ(s)v(s)−ϕ(t)v(t)| ds dt

p
2
dx dy
≼(2L+kρ)−2−p(2Lρ)(2L+kρ)

∫
B2L+kρ
∫
B2L+kρ
|u(s)− u(t)||ϕ(s)v(s)−ϕ(t)v(t)| ds dt

p
2
≼(2L+kρ)−1−p(2Lρ)‖v‖
p
2
∞(2L+kρ)p−2
∫
B2L+kρ
∫
B2L+kρ
|u(s)− u(t)|
p
2|ϕ(s)−ϕ(t)|
p
2 ds dt
+ (2L+kρ)−1−p(2Lρ)(2L+kρ)p−2
∫
B2L+kρ
∫
B2L+kρ
|u(s)− u(t)|
p
2|ϕ(t)|
p
2|v(t)−v(s)|
p
2 ds dt
=(2L+kρ)−3(2Lρ)‖v‖
p
2
∞
∫
B2L+kρ
∫
B2L+kρ
|u(s)− u(t)|
p
2|ϕ(s)−ϕ(t)|
p
2 ds dt
+ (2L+kρ)−3(2Lρ)
∫
B2L+kρ
∫
B2L+kρ
|u(s)− u(t)|
p
2|ϕ(t)|
p
2|v(t)−v(s)|
p
2 ds dt
≼(2L+kρ)−3(2Lρ)‖v‖
p
2
∞

∫
B2L+kρ
∫
B2L+kρ
|u(s)− u(t)|p ds dt

1
2
(
2L+kρ‖ϕ‖p
Lp
) 1
2
≼(2L+kρ)− 5
2 (2Lρ)‖v‖
p
2
∞
(2L+kρ)1+1[u]p
W
1p,p(B2L+kρ)

1
2 (
ρ1‖|∇|
1
pϕ‖p
Lp
) 1
2
=(2L+k)− 3
2 (2L)‖v‖
p
2
∞
[u]p
W
1p,p(B2L+kρ)

1
2 (
‖|∇|
1
pϕ‖p
Lp
) 1
2
□
