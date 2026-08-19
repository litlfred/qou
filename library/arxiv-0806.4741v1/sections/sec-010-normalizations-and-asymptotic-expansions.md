---
doc_id: arxiv-0806.4741v1
doc_title: "The deformation quantizations of the hyperbolic plane P. Bieliavsky G´ eom´ etrie et Physique math´ ematique Universit´ e Catholique de Louvain 2, Chemin du Cyclotron, B-1348 Louva"
section_id: sec-010-normalizations-and-asymptotic-expansions
section_title: "Normalizations and asymptotic expansions"
section_number: null
pages: 17-22
source_pdf: 0806.4741v1.pdf
source_sha256: 5e7ad85a99fb3552
doc_brief: "The deformation quantizations of the hyperbolic plane P. Bieliavsky Géométrie et Physique mathématique Université Catholique de Louvain 2, Chemin du Cyclotron, B-1348 Louvain-la-Neuve, Belgium — We"
---
Observe that the change of variables (89) becomes singular when ℏ vanishes, while the equation (86) dege-
nenrates into
(−r∂ 2
r + 2q∂r∂q +r (k−k′q2))F (q,r ) = 0 . (103)
The general solution of this equation can be expressed as a superposition of modes
F0,σ =C 1√qeiσqr 2
2 e− i
2σ(k
q +k′q) . (104)
Let us notice that these modes can be obtained from special combinations of modes (95) and a rescaling of
the wave-numbers intos =σ/ℏ2. This rescaling is dictated by the necessity of maintaining a r dependence
in the limit ℏ→ 0 of the modes (95):
s
√
1 + ℏ2r2≈s +s ℏ2r2 = σ
ℏ2 +σr 2 (105)
while the oscillating factor can be controlled by considering the asymptotic behavior of the Hankel functions
([41], sec. 8.41)
H(2)√
k
ℏ
(
√
σ2
ℏ4 + k′
ℏ2q)≈ ℏ
√ 2
πσq e−iσq
ℏ2ei
√
kπ
2 ℏ e− i
2σ(k
q +k′q) . (106)
Thus by choosing in the coeﬃcients A and B in the linear combination (95) as :
A =−iB =C 1
ℏ
√πσ
2 e−i
√
kπ
2 ℏ (107)
we obtain modes whose limit for ℏ = 0 is well deﬁned. This explain the results of our computations below.
Note that, given an operator U, it is not straightforward to extract the inverse operator U−1 since one has
to determine how to superpose these diﬀerent modes. In section 3.7 however, we will discuss a particular
example where the superposition is known.
The operators U we consider hereafter will correspond to (97), (95) with B = 0. This special choice is
motivated by the bad behavior of the Y -Bessel function near the origin. We have :
(Usf)(a,l ) =Cℏ(s)
∫
R2×R+
drdndxJ √
k
ℏ
(
√
s2 +k′/ℏ2 x)(1 + ℏ2r2)− 1
4
eisx
√
1+ℏ2r2
eirlx e−irn f(a− 1
2 lnx,n ) . (108)
A necessary condition for Us to deﬁne a star product is that ( Us1) = 1. This leads to the condition 4
Cℏ(s) =
√
k′
2π ℏ
[√
k′−i ℏs[ℏ]√
k′ +i ℏs[ℏ]
]
√
k′
2 ℏ
. (109)
Let us notice that we allow a ℏ dependence in s; we don’t assume it a priori to be constant but leave it as a
free (regular) function of the deformation parameter.
On the other hand, the requirement
Usf−→
ℏ→ 0
f (110)
to get the right classical limit further imposes
k =k′ . (111)
4A useful relation in this derivation (see ref.[41], sec. 13.2, eq.[8]) is :
R∞
0 e(iκ−ϵ)ζJλ(βζ )dζ = β−λ[
√
β2−κ2+iκ]λ
√
β2−κ2
17
Let us now turn to the asymptotic expansion of the operator (108). To this end we introduce the following
Fourier-like transforms:
˜f−(k,p ) = 1
2π2
∫
f(a,l )e−ike−2a
e−iple−2adadl (112)
f(a,l ) =
∫
˜f−(k,p )eike−2a
eipldkdp , (113)
from which one obtains
(Usf)(a,l ) =
√
k
∫ (1 + ℏ2p2)−1/4
(k + ℏ2 (s2(ℏ)−κ2))1/2
[√
k + ℏ2 (s2(ℏ)−κ2) +i ℏκ√
k +i ℏs(ℏ)
]
√
k
ℏ
˜f−(r,p )dpdr (114)
where
κ =re−2a +pl +s(ℏ)
√
1 + ℏ2r2. (115)
Setting X =re−2a +pl , the integrand can be Taylor expanded around ℏ = 0 as
√
k (1 + ℏ2p2)−1/4
(k + ℏ2 (s2(ℏ)−κ2))1/2
[√
k + ℏ2 (s2(ℏ)−κ2) +i ℏκ√
k +i ℏs(ℏ)
]
√
k
ℏ
= eiXP (X,p 2) (116)
where (116) deﬁnes the ℏ power series P (X,p 2), which, at ﬁrst (non-trivial) order 5, reads as :
P (X,p 2) = 1 + ℏ2
(
−p2 (1− 2is )
4 + s
kX + (1 +is )
2k X2 + i
6kX3
)
+O(ℏ4) (117)
The important point in the previous expression is the structure of the expansion, and in particular the
occurrence of the factor eiX. Using this result, the expansion of the operator U follows:
(Usf)(a,l ) ≈
∫
P (X,p 2)eiX ˜f−(r,p )dpdr
=
∫
P [−i∂σ,−∂2
α]eiσXeiαp ˜f(k,p )−
⏐⏐⏐
σ=1,α=0
dpdr
= P [−i∂σ,−∂2
α]f(a− 1
2 lnσ,σl +α)
⏐⏐⏐⏐
σ=1,α=0
. (118)
It therefore appears appears that the product so-deﬁned deforms the pointwise product on the hyperbolic
plane in the direction of the SL(2 , R)-invariant Poisson bracket.
A similar computation can be performed starting from the inverse operator. One has (with x =e2(b−a))
(Vsf)(a,l ) = Dℏ(s)
2
∫
R2×R+
drdndxJ √
k
ℏ
(
√
s2 +k′/ℏ2x)(1 + ℏ2r2)− 1
4
eisx
√
1+ℏ2r2
eir(nx−l)f(a + 1
2 lnx,n ) . (119)
The requirement Vs1 = 1, imposes
Dℏ(s) =
√
k
π ℏ
(√
k′−i ℏs(ℏ)√
k′ +i ℏs(ℏ)
)
√
k
2 ℏ
(120)
while the right classical limit implies 6
k =k′, (121)
5If we assume s to be constant, instead of a function of ℏ, this expansion involves only even power of ℏ.
6A useful relation in that case is (see ref.[41], sec. 13.2, eq.(7)) :
R∞
0
e(iκ−ϵ)ζ
ζ Jλ(βζ )dζ = [
√
β2−κ2+iκ]λ
λβλ
18
in accordance with eq. (111).
Using again the expression of the Fourier transform of the Bessel function but the Fourier transform
˜f+(k,p ) = 1
2π2
∫
f(a,l )e−ike2a
e−iple2adadl (122)
f(a,l ) =
∫
˜f+(k,p )eike+2a
eipldkdp. (123)
one is led to
(Vsf)(a,l ) =
√
k
2π
∫ (1 + ℏ2p2)−1/4eipleiqn
(k + ℏ2 (s2(ℏ)−ρ2))1/2
[√
k + ℏ2 (s2(ℏ)−ρ2) +i ℏρ√
k +i ℏs(ℏ)
]
√
k
ℏ
˜f+(r,q )dpdrdndq (124)
where
ρ =re 2a−pn +s(ℏ)
√
1 + ℏ2p2 . (125)
Setting Y =re 2a−pn , we may write
√
k (1 + ℏ2p2)−1/4
(k + ℏ2 (s2(ℏ)−ρ2))1/2
[√
k + ℏ2 (s2(ℏ)−ρ2) +i ℏρ√
k +i ℏs(ℏ)
]
√
k
ℏ
=eiYP (Y,p 2), (126)
whereP has the same expression as in (116) (Let us remark that this holds only because we use the strongly
closed S-invariant star product). One successively gets
(Vsf)(a,l ) = 1
2π
∫
dpdrdndqe ipl eiqn P (Y,p 2)eiY ˜f+(r,q )
= 1
2π
∫
dpdrdndqP [−i∂σ,−∂2
l ]eiσY eipl eiqn ˜f+(k,q )
⏐⏐⏐
σ=1
= 1
2π
∫
dpdnP [−i∂σ,−∂2
l ]f(a + 1
2 lnσ,n )eip (l−nσ )
⏐⏐⏐⏐
σ=1
= P [−i∂σ,−∂2
l ] 1
σ f(a + 1
2 lnσ, l
σ )
⏐⏐⏐⏐
σ=1
. (127)
3.6 The case k = ℏ2
4 and Zagier type deformations
We now consider the case of our closed star product ⋆ := T closed(⋆0
ℏ) together with a particular derivation
Dℏ∈ Der(⋆) deﬁned as setting k = ℏ2
4 in the expression (51) and then intertwining by T closed following (59).
We then proceed as in the subsection 3.4, but use the following variables rather than (89):
ξ =q
1
2
2
ℏ sinh( ℏ
2ζ) , η =q
1
2 cosh( ℏ
2ζ) (128)
Note that in contrast with the coordinates (89), the above one are not singular in the limit ℏ→ 0. Indeed,
they become ξ0 =q
1
2ζ and η0 =q
1
2 in the limit.
Within these normalisations, the equation (91) then becomes:
∂ξ∂ηG = 4k′ηξG ; (129)
with, as before,
G(q,r ) =q1/2(1 +r2ℏ2)1/4F (q,r ). (130)
Note that from (84), the classical limit ℏ→ 0 of the latter is prescribed to equal
Fcl := δ0(a)⊗ 1r . (131)
19
One way to achieve this requirement is to allow k′ to depend on ℏ in such a way that the condition (111)
remains satisﬁed
lim
ℏ→0
k′(ℏ) = 0 . (132)
More naturally, this corresponds to considering the ℏ-independent wave equation in the case k′ = 0:
∂ξ∂ηG = 0 , (133)
which trivially admits the ξ-independent solution:
G = G(η) = G
(
ea
√
2
2
(
1 +
√
1 + ℏ2r2
) 1
2
)
; (134)
with
G(ea) := eaδ0(a). (135)
The above discussion leads us to the particular solution:
uℏ(a,𝓁 ) :=
√
2e2a
4π
∫ ∞
−∞
eir𝓁e2a
(
1 +
√
1 + ℏ2r2
√
1 + ℏ2r2
) 1
2
δ0
(
a + 1
2 log(1
2(1 +
√
1 + ℏ2r2) )
)
dr ; (136)
that admits the correct limit:
u0(a,𝓁 ) = δe(a,𝓁 ). (137)
The associated convolution operator U produces a deformation quantization that is invariant under the
inﬁnitesimal action of sl2(R) on an open S-orbit in R2 (the group S acting by special linear transformations).
The corresponding underlying geometry here being ﬂat ( k′ = 0). In particular, this class of solutions
reproduces star products of the same type as the one considered by Connes and Moscovici in [42], primarily
constructed by Zagier as a (sl)2(R)-invariant deformation of the algebra of modular forms [43].
3.7 Unterberger type solutions and Weinstein’s asymptotics
In [31, 32] an associative SL(2, R) invariant composition law, though not a star product, has been derived in
a totally diﬀerent context by A. and J. Unterberger, for the composition of symbols in the so-called Bessel
calculus. We are going to show that a slight modiﬁcation of their formula yields one of the simplest products
in the family we have found.
As a prealable, let us notice, that in their works, these authors also make use of an interwiner operator linking
an SL(2, R)- invariant composition law with an AN-invariant star product, but not the strongly closed one
we have adopted. Instead of this one, the star product they use may be expressed in our framework as the
one obtained from (56) with special weight function P(ℏξ) = cosh(ℏξ), as proven in [44].
The convolution kernel of an intertwiner between an SL(2 , R)-invariant star product # and a general AN -
invariant product, itself built from the Moyal star product twisted by an operator TP is obtained from the
operator U we constructed in section 3.4 by:
UP =U◦ (T
closed
)−1◦TP . (138)
In particular, if TP is of the form of eq. (56), the kernel of UP is then given as a superposition of modes,
uP(a,l ) =
∫
φ(s′)uP
ℏ,s′(a,l )ds′ , (139)
with
uP
ℏ,s(a,l ) =e2ahs(e2a)
∫
(1 + ℏ2r2)− 1
2P(arcsinh(ℏr))eis
√
1+ℏ2r2e2a
eirle2a
dr , (140)
where hs(x)∝J√
k/ℏ[
√
s2 +k/ℏ2 x].
20
An analog computation yields the kernel of the inverse operatorU−1
P again as a superposition of modes, each
of them being given by
vP
ℏ,s(a,l ) =e−2ahs(e−2a)
∫
P−1(arcsinh(ℏr))eis
√
1+ℏ2r2e−2a
e−irldr . (141)
Let us plug B = 0 in (95), and normalize the modes accordingly to eqs (109, 120) with k =k′ (see eqs (111,
121). The operator U considered in [31, 32] then corresponds to the value s = 0 in (97). This obviously
amounts to pick up φ(s′) = δ(s′) in eq. (139). By taking P(ℏξ) = cosh( ℏξ), and denoting by UU the
corresponding operator, one ﬁnds
(UUf)(a,l ) =
√
k
ℏ
∫
dxJ √
k
ℏ
(
√
kx/ ℏ)f(a− 1
2 lnx,lx ). (142)
The inverse operator, U−1
U corresponds to the kernel resulting from the superposition
vℏ,s(a,l ) =
∫
ψ(s)ΨU
ℏ,s(a,l )ds (143)
of modes
ΨU
ℏ,s(a,l ) =
√
k
2π ℏ
(√
k′−i ℏs(ℏ)√
k′ +i ℏs(ℏ)
)
√
k
2 ℏ
J√
k
ℏ
(
√
s2 +k′/ℏ2x)
∫ eisx
√
1+ℏ2r2
e−irl
√
(1 + ℏ2r2)
dr (144)
that is obtained by using
ψ(s) = (i−s)δ′(s) (145)
in the superposition of modes like those appearing in eq. (119), normalized according to eq. (120). Explicitly,
one gets
(U−1
U f)(a,l ) =
√
k
ℏ
∫
dxJ √
k
ℏ
(
√
kx/ ℏ)f(a + 1
2 lnx, l
x). (146)
Apart from the ℏ-dependent pre-factors, these operators are exactly the ones found in [31], see equations
(4.16) and (4.7).
Of course, the asymptotic expansions allows to buildU−1 perturbatively, as an expansion inℏ. For illustrative
purpose let us mention, that for a ﬁxed value of s we obtain at fourth order:
U−1
s =
(
Vr− i
4π
[
1−i ℏ2r (1
4 +ir )
]
∂rVr
)
r=−s
+O(ℏ5)
=
∫ [
(1 + ℏ2
16π +i ℏ2
2 r)δ[r +s] + i
4π (1−i ℏ2
4 r +π ℏ2r2)δ′(r +s)
]
Vrdr +O(ℏ5)
(147)
By a long but straightforward computation, the above explicit expressions of UU and U−1
U yield (for k = 1)
the following integral formula for the invariant star product on the hyperbolic plane D:
u♯ ℏv (x) = 1
16π3ℏ4
∫
D×D
Kℏ (Scan(x,y,z )) u(y)v(z) dy dz ;
where dy denotes the Liouville measure on D and where
Kℏ(ϖ) :=
∫ ∞
0
s2J 1
ℏ
(s/ℏ)e
i
ℏsϖ ds. (148)
Using tabulated Laplace transforms, one ﬁrst computes
Fµ(p) =
∫ ∞
0
e−ptJµ(t)dt = 1
pµ+1
[1 + (1 + 1
p2 )1/2]−µ
√
1 + 1
p2
, (149)
21
with p =ε−iϖ, ε≪ being a small real part necessary to ensure convergence. Using the following relations
1 + 1
p2 =
{
1−ϖ−2 if ϖ2 > 1,
(ϖ−2− 1)ei sign(ϖ)π if ϖ2 < 1, (150)
and
1 +
√
1 + 1
p2 =
{
1 + (1−ϖ−2)1/2∈ R if ϖ2 > 1,
1 + (ϖ−2− 1)1/2ei sign(ϖ)π/2 if ϖ2 < 1, (151)
one ﬁnally gets
Fµ(−iϖ) =
{
1√
1−ϖ2 ei µ
2fW (ϖ) if ϖ2 < 1,
|ϖ|−(µ+2)(ϖ2− 1)−1/2[1 + (1−ϖ−2)1/2]−µei π
2 (µ+1)sign(ϖ) if ϖ2 > 1 ; (152)
wherefW is the odd function (40) deﬁned by fW (Scan) :=SW . Note that, when ϖ2 < 1, the phase ofFµ is
precisely given by fW (ϖ), while when ϖ2 > 1, it is pure phase. The kernel Kµ is now simply described by
Kµ(ϖ) =− d2
dϖ2Fµ(−iϖ). (153)
The phase Sµ of the kernel Kµ can then be determined from (153). For ϖ2 < 1, one gets
Sµ(ϖ) =µfW (ϖ)
2 − arctan[ 3µ sinfW (ϖ)
µ2− 4 + (µ2 + 2) cosfW (ϖ)] . (154)
In other words, for ϖ2 < 1, which corresponds to triples of points in D for which Weinstein’s SW is well
deﬁned, the above kernel Kℏ can be expressed under the WKB oscillatory form. The expression of the
corresponding phase is then the following:
S = SW
2 − ℏ arctan[ 3ℏ sinSW
1− 4ℏ2 + (1 + 2ℏ2) cosSW
] . (155)
In particular, one has the following asymptotics:
S ∼ SW
2 ,
agreeing with A. Weinstein’s picture in [33].
Acknowledgments
P.B. and Ph.S. acknowledge partial support from the IISN-Belgium (convention 4.4511.06). P.B. acknowl-
edges partial support from the IAP grant ‘NOSY’ delivered by the Belgian Federal Government. S.D. and
Ph.S. warmly thank the IHES for its hospitality and the exceptional working conditions provided to its
guests.
