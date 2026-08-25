---
doc_id: arxiv-2208.14188v2
doc_title: "Resurgence in complex Chern-Simons theory at generic levels"
section_id: sec-006-31-asymptotic-series
section_title: "Asymptotic series"
section_number: 3.1
pages: 16-19
source_pdf: 2208.14188v2.pdf
source_sha256: 92a7651c81b799b3
doc_brief: "Resurgence in complex Chern-Simons theory at generic levels — In this note we study the resurgent structure of sl(2, C) Chern-Simons state integral model on knot complements S3\41,S 3\52 with generic"
---
The state integral of ﬁgure eight knot at level k is already given as a one-dimensional
integral in [13]
χ(k)
41 (µ,n ;τ) =ηk
k
∑
m∈Zk
∫
R+i Im(cb)−i|µ|−i0
dσZ(k)
b [∆](σ−µ,m−n)Z(k)
b [∆](σ,m )
× (−1)me
πi
k ((σ−cb)2−2(µ−σ+cb)2−m2+2(n−m)2), (3.1)
whereηk = exp πi
6 (k + 2c2
b/k). This can be derived from the generic formula (2.8). We can
choose the Neumann-Zagier data
AAA =
(
1 0
1 1
)
, BBB =
(
0 −1
−1−1
)
, ν =
(
0
0
)
, (3.2)
with which (2.8) yields
Z(k)
γ (µ,n ; b)
= 1
ik2
∑
m∈(Zk)2
∫
d2σe
2πi
k (−σ1µ1+σ2µ1+m1n1−m2n1)e
πi
k (2σ1σ2−2m1m2)Z(k)
b [∆](σ1,m 1)Z(k)
b [∆](σ2,m 2)
=e
πi
12 (k+
8c2
b
k )
ik
∑
m∈Zk
∫
dσZ(k)
b [∆](σ,m )Z(k)
b [∆](σ +µ,m +n)
(−1)m+n expπi
k
(
−(σ−cb)2− 4µσ−µ2 + 2cbµ +m2 + 4mn +n2)
.
(3.3)
In the last step, we have integrated over σ2 and summed over m2 using the Fourier trans-
formation (A.13). We then relabeled ( σ1,m 1) to (σ,m ) as well as (µ1,n 1) to (µ,n ). After
4There are missing BPS states concerning the Abelian ﬂat connection σ0. But they are related to the
Stokes automorphisms of the asymptotic series associated to σ0, which is invisible in the state integral
model. See some discussion in Section 5.
– 15 –
changing the signs of µ,n we ﬁnd the same expression as (3.1) up to an overall irrelevant
factor
χ(k)
41 (µ,n ;τ) = ie
πi
12 (k−
4c2
b
k )(−1)ne
πi
k (−µ2−2cbµ+n2)Z(k)
γ (−µ,−n; ℏ). (3.4)
As a one-dimensional integral, it is much easier to perform saddle point analysis on
(3.1). We ﬁrst introduce an alternative representation of the tetrahedron partition func-
tion5
D(k)
b (u,m ) =Z(k)
b [∆](cb−
√
ku,m ), (3.5)
in terms of which, the state integral (3.1) reads
χ(k)
41 (µ,n ;τ) =ηk
k
∑
m∈Zk
(−1)me
πi
k (2n2−4nm+m2)
×
∫
R+i0
dσ D(k)
b ( 1√
k
(σ +µ),m−n) D(k)
b ( 1√
k
σ,m )e
πi
k (−2µ2−4µσ−σ2). (3.6)
We scale the variables
Z = 2πbσ, u = 2πbµ (3.7)
and then perform asymptotic expansion of the tetrahedron partition functions in the small
b limit using (A.15),
χ(k)
41 (µ,n ; b)∼ ηk
2πbk
∑
m∈Zk
(−1)me
πi
k (2n2−4nm+m2)
∫
dZ exp
∑
𝓁≥0
(2πib2)𝓁−1U𝓁(u,Z ) (3.8)
where the potential functions are
U0(u,Z ) =1
k
(
u2 + 2uZ + Z2
2 + Li2(−eZ) + Li2(−eu+Z)
)
, (3.9a)
U𝓁≥1(u,Z ) = 1
𝓁!
∑
j∈Zk
B𝓁(1− 1/(2k)−j/k)
(
Li2−𝓁(ζm−j−1/2eZ/k) + Li2−𝓁(ζm−j−1/2eZ/kx)
)
.
(3.9b)
The critical equation of the leading order potential function reads
0 = ∂
∂ZU0(u,Z ) = 1
k
(
2u +Z− log(1 + eZ)− log(1 + eu+Z)
)
, (3.10)
which can be simpliﬁed to the algebraic equation
−X2Y = (1−XY )(1−Y ), (3.11)
with
X = eu =xk, Y =−eZ. (3.12)
We also introduce the variable θ such that
Y =−θk. (3.13)
5This version of tetrahedron partition function was introduced in [13].
– 16 –
The critical point equation (3.11) has two solutions in terms ofY , corresponding to the
geometric and conjugate ﬂat connectionsσ1,σ 2 on the knot complement. Numerically, they
are the ones that in the limit X→ 1 reduce respectively to the solutions e πi/3 and e−πi/3
of (3.11). Near each critical point σj, the integrand is approximated by the exponential
exp
(
V (k)(σj)
2πiτ
)
, (3.14)
where
V (k)(σj) =U0(log(X), log(−Yj)) +π2
6k. (3.15)
The extra factorπ2/(6k) comes from the factorηk. Note the interesting relationV (k)(X,Y ) =
V (1)(X,Y )/k.
In addition, by expanding near the critical point and performing the Gaussian inte-
gration order by order, for each critical point σj we can ﬁnd an asymptotic power series
ϕ(k,σj)(x;τ), which, together with the exponential factor (4.13), forms the trans-series
Φ(k,σj)
41 (x;τ) = eV (k)(σj)/(2πiτ)ϕ(k,σj)
41 (x;τ), j = 1, 2. (3.16)
The one-loop contribution ϕ(k,σj)
41 (x; 0) =ω(k,σj)
41 (x) has a universal expression
ω(k,σj)
41 (x) =e
πi
4 +πik
6 + 2πi
k (n2−1/12)
√
k(xkθ2k− 1)
θ1/2xD∗
k(ζ−1/2θ)1/kD∗
k(ζ−1/2θx)1/k
×
∑
m∈Zk
(−1)mζm2/2θmx2m(ζ1/2θ;ζ)−1
m (ζ1/2θx;ζ)−1
m . (3.17)
The power series ϕ(k,σj)
41 (x;τ)/ω(k,σj)
41 (x) on the other hand, depends in a very complicated
way on the level k.
The case of k = 1 is particularly simple. The dependence on n∈ Z1 is trivial, and the
state integral reduces to [31]
χ41(µ;τ) =χ(1)
41 (µ;τ) = Φb(0)−2
∫
R+i0
dvΦb(µ +v)Φb(v)eπi(v2−2(µ+v)2). (3.18)
where we have used η1 = Φb(0)−2. The power series ϕ(σi)
41 (x;τ) =ϕ(k=1,σi)
41 (x;τ) are given
by [31]
(ω(σ1)
41 )−1ϕ(σ1)
41 (x; τ
2πi) =1− 1
24γ(x)3
(
x−3−x−2− 2x−1 + 15− 2x−x2 +x3)
τ
+ 1
1152γ6(x)
(
x−6− 2x−5− 3x−4 + 610x−3− 606x−2− 1210x−1
+ 3117− 1210x− 606x2 + 610x3− 3x4− 2x5 +x6)
τ 2 +O(τ 3).
(3.19)
with
γ(x) =
√
x−2− 2x−1− 1− 2x +x2. (3.20)
– 17 –
while ϕ(σ2)
2 (x;τ) = iϕ(σ2)
1 (x;−τ). At level k = 2, the power series are
(ω(k=2,σj)
41 )−1ϕ(k=2,σj)
41 (x;τ)
=1− ((1 + 6x + 5x2− 30x3 + 10x4 + 30x5− 3x6 + 30x7 + 10x8− 30x9 + 5x10 + 6x11 +x12)
(−1−x2 +x4 + 2x2Yj))/(48(−1−x +x2)2(1−x +x2)2(−1 +x +x2)2(1 +x +x2)2)τ +O(τ 2).
(3.21)
Additional terms as well as ﬁrst few terms of the power series at level k = 3 can be found
in Appendix B.1.
Several conclusions can be drawn from these data. It is clear that the coeﬃcients of
the power series depend only on the solution Yj to the NZ equation, but not on a k-th
root of Yj. Furthermore, they depend on the deformation parameters u,n only through
the holonomy parameter x. Finally, it is evident that the power series become increasingly
more complicated at higher levels k.
