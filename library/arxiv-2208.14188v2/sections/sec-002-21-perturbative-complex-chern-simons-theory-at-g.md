---
doc_id: arxiv-2208.14188v2
doc_title: "Resurgence in complex Chern-Simons theory at generic levels"
section_id: sec-002-21-perturbative-complex-chern-simons-theory-at-g
section_title: "Perturbative complex Chern-Simons theory at generic level"
section_number: 2.1
pages: 4-10
source_pdf: 2208.14188v2.pdf
source_sha256: 92a7651c81b799b3
doc_brief: "Resurgence in complex Chern-Simons theory at generic levels — In this note we study the resurgent structure of sl(2, C) Chern-Simons state integral model on knot complements S3\41,S 3\52 with generic"
---
The sl(2, C) Chern-Simons theory on a three manifold M has action
Ik,s =tSCS(A) + ˜tSCS(A) (2.1)
where SCS(A) is the three dimensional Chern-Simons action
SCS(A) = 1
4π
∫
M
Tr(A∧ dA + 2
3A∧A∧A), (2.2)
A is a connection of the sl(2, C) bundle over M, and A its complex conjugation. The
couplings t, ˜t can be split as
t = 1
2(k + is), ˜t = 1
2(k− is). (2.3)
In a consistent quantum theory, the levelk must be an integer so that the partition function
of the Chern-Simons theory is invariant under large gauge transformations. The other level
s is constrained to be either real or imaginary in order for the CS theory to be unitary,
which, however, we do not impose in this work.
Suppose the 3-manifoldM is a knot complementM =S3\K with torus boundary. The
sl(2, C) connection on the boundary torus is parametrised by the holonomies x,y along the
meridian and the longitude. The condition that the sl(2, C) connection can be extended to
the interior of M constrains that x,y are not independent but are related by a polynomial
equation
A(x,y ) = 0 (2.4)
called the A-polynomial. Furthermore, in a quantum theory, the holonomy x should be
parametrised as
x = exp
(2πbµ
k − 2πin
k
)
, (2.5)
– 3 –
where µ∈ C, n∈ Zk, and the parameter b is related to the levels k,s by
b2 = k− is
k + is. (2.6)
By the 3d-3d correspondence, the sl(2, C) Chern-Simons theory at discrete level k≥ 1
on M is dual to a 3d N = 2 SCFT denoted by T2[M] put on an orbifold of the squashed
3-sphere S3
b/Zk [15],
S3
b/Zk =
{
(z,w )∈ C2| b2|z|2 + b−2|w|2 = 1
}
/(z,w )∼ (e2πi/kz, e−2πi/kw). (2.7)
Here b has the geometric meaning of the squashing parameter. When M is a knot com-
plement, the T2[M] theory has a u(1) ﬂavor symmetry. The parameters µ,n are then
respectively the ﬂavor mass, and the holonomy of the ﬂavor vector ﬁeld. The latter takes
value in π1(S3
b/Zk) = Zk.
WhenM =S3\K is a hyperbolic manifold, it can be triangulated, namely decomposed
to N ideal tetrahedra glued along their faces. In [4], the T2[M] theory was constructed
based on the triangulation data from the T2[∆] associated with an ideal tetrahedron ∆,
which is well understood. Based on this construction, the partition function of T2[M] on
S3
b/Zk was computed [15], and it was used to give the state integral model for the sl(2, C)
Chern-Simons theory at level k.
It is important to note that, as ﬁrst pointed out in [18], the construction in [4] misses
an entire sector related to the Abelian ﬂat connection, and thus the partition function
computed in [15] is also not complete. Rather, the state integral model should be regarded
as the reduced partition function of thesl(2, C) Chern-Simons theory that does not include
the contribution from the Abelian ﬂat connection.
Let us discuss in a bit detail the state integral model. The triangulation of M in terms
ofN tetrahedra is described by the small Neumann-Zagier data 1 that can be encoded in a
tupleγ = (AAA,BBB,ν ) consisting of two matricesAAA,BBB∈GL(N, Z) and a vectorν∈ ZN. They
encode the coeﬃcients of Thurston’s gluing equations for the triangulation including N−1
independent equations imposing condition on internal edges, and one equation describing
holonomy on external edges. We order rows of AAA,BBB and elements of ν so that the ﬁrst
rows ofAAA,BBB and the ﬁrst element of ν corresponds to the external edge.
It was shown in [36] that ( AAA BBB) forms the top half of a symplectic matrix, so that
AAABBBT is symmetric and (AAABBB) is of full rank. On the other hand, giving a triangulation of
M, the choice of Neumann-Zagier data is not unique. Following [34, 35] we always choose
a set of Neumann-Zagier data where BBB is invertible over integers, and thenBBB−1AAA must be
symmetric.
Let us introduce in addition σ = (σ1,...,σ N)∈ CN, mmm = (m1,...,m N)∈ (Zk)N as
well as µ = (µ, 0,..., 0)∈ C× 0N−1, nnn = (n, 0,..., 0)∈ Zk× 0N−1. By following the
procedure in [15] and extending slightly the formulas in [34], the state integral model can
1The complete Neumann-Zagier data introduced in [34, 35] also includes a choice of the solution to the
Neumann-Zagier equation.
– 4 –
be written as
Z(k)
γ (µ,n ; b) = 1
kN√
detBBB
∑
m∈(Zk)N
∫
dN σe
2πi
k (−σBBB−1µ+mmmBBB−1nnn)e
πi
k (−σBBB−1AAAσ+mmmBBB−1AAAmmm+2cbσBBB−1ν)
(−1)mmmBBB−1AAAmmm
N∏
i=1
Z(k)
b [∆](σi,mi). (2.8)
The part in blue is due to non-vanishing boundary holonomy and thus new compared to the
results in [34]. HereZ(k)
b [∆](σi,mi) is the partition function of the Chern-Simons theory on
a tetrahedron, which can be expressed in terms of Faddeev’s quantum dilogarithm Φ b(x)
Z(k)
b [∆](µ,n ) =
∏
(r,s)∈Γ(k;n)
Φb(cb− 1
k (µ + ibr + ib−1s)) (2.9)
where
Γ(k;n) ={(r,s )∈ Z2| 0≤r,s<k,r −s≡n(modk)} (2.10)
and cb = i
2(b + b−1). This deﬁnes a meromorphic function of µ∈ C for each n∈ Zk, and
it is deﬁned for all values of b with b2 in the cut plane C′ = C\R≤0. When Im b > 0 or
Im b< 0, it has the factorisation form
Z(k)
b [∆](µ,n ) = (qx−1;q)∞(˜q−1˜x−1; ˜q−1)∞ (2.11)
where we use the notation
q = exp 2πi
k (b2 + 1), ˜q = exp−2πi
k (b−2 + 1),
x = exp
(2πbµ
k − 2πin
k
)
, ˜x = exp
(2πb−1µ
k + 2πin
k
)
,
(2.12)
and (a,q )∞ is the q-Pochhammer symbol deﬁned to be ∏∞
j=1(1− aqj) if |q| < 1 or
1/(q−1a;q−1)∞ if|q|> 1.
One can give explicitly the contour of integral to make the N dimensional integral
convergent [15]. But it is a bit complicated and we specify the contours in individual
examples in Sections 3, 4.
We are interested in the double scaling limit
b→ 0, µ →∞, bµ ﬁxed, (2.13)
where the last condition guarantees that the holonomy parameter x remains ﬁnite. Let us
introduce
ζ = e2πi/k, τ = b2 (2.14)
By scaling the variables
Zi = 2πbσi, u i = 2πbµi =
{
2πbµ, i = 1
0, i ≥ 2
(2.15)
– 5 –
and using the asymptotic expansion (A.15) of the tetrahedron partition function, the inte-
gral (2.8) can be written as
Z(N)
γ (µ,n ;τ) = 1
kN√
detBBB(4π2τ)N/2
∑
mmm∈(Zk)N
(−1)mmmBBB−1AAAmmmζ
1
2mmmBBB−1AAAmmm+mmmBBB−1nnn
∫
dNZZZ exp
∞∑
𝓁=0
(2πiτ)𝓁−1U (mmm)
𝓁 (uuu,ZZZ)
(2.16)
where the coeﬃcient functions are
U0(uuu,ZZZ) = 1
kZZZBBB−1uuu+ 1
2kZZZBBB−1AAAZZZ− πi
kZZZBBB−1ν + 1
k
N∑
i=1
Li2(e−Zi), (2.17a)
U (mmm)
𝓁≥1(uuu,ZZZ) =− 1
2kZZZBBB−1νδ𝓁,1 +
N∑
i=1
k∑
s=1
B𝓁(s/k)
𝓁! Li2−𝓁(e
2πi
k (s+mi)e−Zi
k ). (2.17b)
We drop the superscript (mmm) forU0 since it does not depend on the index mmm. We have also
simpliﬁed the expression of U0 using the identity
k∑
s=1
Li2(e2πis/kx) = 1
k Li2(xk), (2.18)
which can be easily proved by the series expansion of Li 2(x). The saddle point equations,
i.e. the critical point equations for U0 are
uj +
N∑
i=1
AjiZi +
N∑
i=1
Bji log(1− e−Zi) =πiνj, j = 1,...,N, (2.19)
or equivalently with
zi = eZi, w i = eui (2.20)
we ﬁnd
wj
N∏
i=1
zAji
i (1−z−1
i )Bji = (−1)νj, j = 1,...,N. (2.21)
Note that at the end of the day, we must setuj = 0 or equivalentlywj = 1 forj = 2,...,N .
Since
x = exp 2πi
k (−ibµ−n) = exp
(u
k− 2πin
k
)
=ζ−nw1/k
1 , (2.22)
the critical equations can also be written as
xk
N∏
i=1
zAji
i (1−z−1
i )Bji = (−1)νj, j = 1, (2.23a)
N∏
i=1
zAji
i (1−z−1
i )Bji = (−1)νj, j = 2,...,N. (2.23b)
– 6 –
They can be regarded as a deformation of the Neumann-Zagier equations. Each solution
zzz∗ = expZZZ∗ to the critical equations corresponds to a non-Abelian sl(2, C) ﬂat connection
σ∗ overM.
We can choose one of the critical points (saddle points) ZZZ∗ = (Z∗
i ) and expand around
the critical point by Zj =Z∗
j + (2πiτ)1/2δZj. By an expansion ﬁrst in terms of τ and then
performing Gaussian integral order by order, we obtain a trans-series Φ (k,σ∗)
γ (µ,n ;τ). This
was worked out in [34] whenµ = 0 andn = 0. In the generic case the calculation is similar,
and we present the results here.
Let us introduce z = eZ, as well as
z′ = (1−z)−1, z ′′ = 1−z−1 (2.24)
so that
zz′z′′ =−1. (2.25)
From (2.17b) it is necessary to choose a k-th root of Z∗. We introduce θi such that
(θi)k =z∗
i. (2.26)
Let us also deﬁne the Average and Vev of a function g
Av(g(mmm)) =
∑
mmm∈(Zk)Nammm(x,θ )g(mmm)
∑
mmm∈(Zk)Nammm(x,θ ) (2.27)
with
ammm(x,θ ) =x−mmmBBB−1
(−1)mmmBBB−1AAAmmmζ
1
2 (mmmBBB−1AAAmmm+mmmBBB−1ν)θ−BBB−1AAAmmm
N∏
i=1
(ζθ−1
i ;ζ)−1
mi. (2.28)
and
⟨g(δZZZ)⟩ =
∫
dNδZZZ e− 1
2δZZZTHHHδZZZg(δZZZ)
∫
dNδZZZ e− 1
2δZZZTHHHδZZZ (2.29)
with
HHH = 1
k
(
−BBB−1AAA + ∆z∗′
)
, (2.30)
and
∆z = diag(z1,...,z N). (2.31)
The perturbative expansion of the state integral (2.8) near the critical point ZZZ∗ then
reads
Φ(k,σ∗)
γ (u,n ;τ) = eU (k)
0,0 (σ∗)/(2πiτ)ω(k,σ∗)
γ ϕ(k,σ∗)
γ (u,n ;τ). (2.32)
The 1-loop contribution is
ω(k,σ∗)
γ = 1
(ik)N/2
√
det(A∆z∗′′ +B∆−1
z∗ )zzz∗BBB−1ννν/k
N∏
i=1
D∗
k(θ−1
i )1/k ∑
mmm∈(Zk)N
ammm(x,θ ). (2.33)
– 7 –
Here recall the cyclic quantum dilogarithms are deﬁned by
Dk(z) =
k−1∏
s=1
(1−ζsz)s, D ∗
k(z) =
k−1∏
s=1
(1−ζ−sz)s. (2.34)
Higher loop contributions are given in
ϕ(k,σ∗)
γ (u,n ;τ) = Av (⟨g(δZZZ,mmm;x,θ )⟩) = 1 +τ C[[τ]] (2.35)
and
g(δZZZ,mmm;x,θ ) = exp

∑
𝓁≥0
(2πiτ)𝓁+d/2−1∑
d≥0
′
U (𝓁,mmm)
k,(id)δZd
i

, (2.36)
where∑
d≥0
′ means d≥ 3 for 𝓁 = 0, d≥ 1 for 𝓁 = 1, and d≥ 0 for 𝓁≥ 2. Besides, in each
sum a summation over i = 1,...,N is implicit. The coeﬃcients are
U (k)
0,0 =1
kZZZ∗BBB−1uuu− πi
kZZZ∗BBB−1ν + 1
2kZZZ∗BBB−1AAAZZZ∗ + 1
k
N∑
j=1
Li2(e−Z∗
j ), (2.37a)
U (k)
0,(id) =(−1)d
kd! Li2−d(e−Z∗
i ), d ≥ 3, (2.37b)
U (k,mmm)
𝓁≥1,(id) =δ𝓁,1δd,0
(
− 1
2kZZZ∗BBB−1ν
)
+δ𝓁,1δd,1
(
− 1
2k (BBB−1ν)i
)
+(−1)d
kdd!𝓁!
N∑
j=1
k∑
s=1
B𝓁(s/k) Li2−𝓁−d(e
2πi
k (s+mj)e−
Z∗
j
k )(δij)d. (2.37c)
The trans-series Φ(k,σ∗)
γ (u,n ;τ) has some very important properties. First of all, unlike
the other coeﬃcients, U0,0(σ∗) in (2.37a) depends on the level k only as an overall factor
1/k,
U (k)
0,0 (σ∗) = 1
kU0,0(σ∗). (2.38)
And U0,0(σ∗) only depends on the Neumann-Zagier data γ, the choice of solution σ∗, and
the holonomy parameteru = log(xk) (but not on the other holonomy parameter n). When
|u|≪ 1, U0,0(σ∗) is the deformed complexiﬁed hyperbolic volume of the knot complement
S3\K [37].
Next, even though the expression of the trans-series Φ (k,σ∗)
γ (u,n ;τ) depends explicitly
on θ∗
i , a choice of the k-th root of z∗
i , one can show that a diﬀerent choice of θ∗
i merely
amounts to an overall constant factor. The exponential expU0,0/(2πiτ) manifestly depends
onz∗
i instead ofθ∗
i . Besides, one can prove that both (ω(k,σ∗)
γ )2k andϕ(k,σ∗)
γ (τ) are invariant
under the transformation θi→ζθi. This has already been proved when the holonomy x is
turned oﬀ in [34], and the coeﬃcients of the power series ϕ(k,σ∗)
γ (τ) are said to live in the
trace ﬁeld of the knot. When the holonomy x is turned on, a similar proof following closely
[34] can be written down with all the necessary ingredients provided in (2.33),(2.35), and
we do not repeat the proof here.
– 8 –
In addition, the dependence on the holonomy of the trans-series Φ(k,σ∗)
γ (u,n ;τ) is quite
elegant. Both (ω(k,σ∗)
γ )2k and ϕ(k,σ∗)
γ (τ) depend on the combination x = exp(u/k− 2πin/k)
but not on u and n individually. This is because the NZ solution z∗ depends on u and
n implicitly through the modiﬁed NZ equations (2.23a), (2.23b), which only depend on
xk. On top of that, ( ω(k,σ∗)
γ )2k and ϕ(k,σ∗)
γ (τ) depend on u,n through the NZ solution
z∗ as well as ammm(x,θ ), which is also a function of x. Combining the discussion of these
two paragraphs, we thus claim that the coeﬃcients of the power series ϕ(k,σ∗)
γ (u,n ;τ) are
understood to live in Fk,x, the trace ﬁeld of the knot extended by holonomy x, deﬁned by
Fk,x =Fk(x), F k =F (ζ), F = Q(z1,...,z N). (2.39)
Finally, although a universal expression (2.33) of the one-loop contribution ω(k,σ∗)
γ at
any level is possible, the power seriesϕ(k,σ∗)
γ depend on the level in a very complicated way,
as we will see in example sections 3.1,4.1.
We also comment that the trans-series (2.32) can be computed from radial asymptotics
ofq-series that come from the evaluation of the state integral model forq at complex roots of
unity, similar to the discussion in [38]. Examples of theq-series, also known as holomorphic
blocks, are shown in Sections 3.2 and 4.2. They can be regarded as x-feformation of the
Nahm sums.
Even though the form of trans-series (2.32) is elegant and it allows us to infer the
above universal properties, it is computationally ineﬃcient as it involves anN-dimensional
integral. Often the state integral (2.8) can be simpliﬁed. For example in the case of
complements of knots 41 and 52, in Thurston’s scheme of triangulation the number N of
ideal tetrahedra is respectively 2 and 3, and their state integral models involve a two- and a
three-dimensional integral respectively. However using integral identities of the tetrahedron
partition functionZ(k)
b [∆](σ,m ), both of them can be reduced to one-dimensional integrals
[13, 15], and their perturbative expansion in terms of Gaussian integral is much simpler.
This will be demonstrated in Sections 3, 4. Nevertheless the universal properties of the
asymptotic series discussed in this section still hold.
