---
doc_id: maximal-hoermander-q-var-revised-v03
doc_title: "q-variational Hörmander functional calculus and Schrödinger and wave maximal estimates"
section_id: sec-007-schrödinger-and-wave-maximal-estimates
section_title: "Schrödinger and wave maximal estimates"
section_number: null
pages: 21-28
source_pdf: Maximal-Hoermander-q-Var-revised-v03.pdf
source_sha256: 135332c04a1b3bb8
toc_source: outline
doc_brief: "q-variational Hörmander functional calculus and Schrödinger and wave maximal estimates — 12 sections: Front matter; Introduction; R-boundedness"
---
Schrödinger and wave maximal estimates
In the next two sections, we will prove maximal estimates for the operator exp(itA), where A
is as before a semigroup generator acting on Lp(Y ) with a Hörmander functional calculus. As
an application, we shall obtain pointwise continuity of the function t 7→exp(itA)f(x, ω) with
f belonging to the domain of a fractional power of A inside Lp(Y ). The guiding example is
Carleson’s problem [Car, Theorem p.24] on the pointwise convergence of the solution of the free
Schrödinger equation to the initial data,
exp(it∆)f(x) →f(x) as t →0, a.e. x ∈Rd.
Carleson asked what is the optimal parameter s > 0 such that f belonging to the Sobolev space
Hs(Rd) = {f ∈L2(Rd) : ˆf(ξ)(1+|ξ|2)s/2 ∈L2(Rd)} guarantees that this pointwise convergence
holds true. A key point to prove pointwise convergence in Carleson’s problem is the maximal
estimate

 sup
0<t<1
| exp(it∆)f|

L2(B(0,1))
⩽Cs ∥f∥Hs(Rd) .
Later on, variants of this problem and the maximal estimate, also for the wave equation with
A =
√
−∆were studied by many authors, see e.g. [RV1, RV2, Rog, BeGo, DeGu]. Carleson
found for his problem that in the one-dimensional case, s > 1
4 is suﬃcient and no s < 1
8 can be
20
suﬃcient. Later on, in particular in the last 10 years, many mathematicians contributed to the
solution of Carleson’s problem [DaKe, Sjo, Veg, TVV, Lee, Bou13, Bou16, DGL, LuRo, DGLZ]
(the parameter s >
d
2(d+1) is now known to be suﬃcient and no s <
d
2(d+1) is suﬃcient).
This has also opened the way to new problems such as to describe the Hausdorﬀdimen-
sion of the set of divergence in case of small values of s, which is beyond the scope of the
present article. In the following two sections we will contribute to both the maximal estimate
∥supt | exp(itA)f|∥Lp(Y ) < ∞and the pointwise convergence of exp(itA)f(x) →f(x) as t →0,
in the quite general setting of operators A as in Section 3 before.
First, in this section, we show that Theorem 5.1 below, which is a variant of Theorem
3.3 gives to some extent maximal estimates for Schrödinger and wave operators, under rather
general conditions on A, see Corollary 5.3. The underlying question is the following. Suppose
that A = −∆is the usual Laplacian operator on Lp(Rd) or that A =
√
−∆. Then t 7→u(t) =
exp(it∆)f is the solution of the Schrödinger equation with initial data f ∈Lp(Rd), so
(
i ∂
∂tu(t)
= −∆u(t)
u(0)
= f
.
In the same way, t 7→u(t) = exp(it
√
−∆)f is the solution of the wave equation with initial
data u(0) = f ∈Lp(Rd) and u′(0) = i
√
−∆f, so





∂2
∂t2 u(t)
= ∆u(t)
u(0)
= f
u′(0)
= i
√
−∆f
.
In [RV1], the authors investigate the boundedness of the associated Schrödinger maximal oper-
ators
S∗f = sup
0<t<1
|exp(it∆)f|
and
S∗∗f = sup
t∈R
|exp(it∆)f| .
Moreover, in [RV2, (4),(5)], these authors study the boundedness of the wave maximal operators
S∗f = sup
0<t<1

exp(±it
√
−∆)f

and
S∗∗f = sup
t∈R

exp(it
√
−∆)f

 .
Here, typical bounds are between spaces S∗, S∗∗: Hs(Rd) →Lp(Rd) [RV1, RV2]. For further
results on maximal estimates of Schrödinger and wave operators, we refer to [Rog, BeGo, DeGu].
Moreover, the Sobolev space admits a description Hs(Rd) = {f ∈L2(Rd), (1−∆)
s
2 f ∈L2(Rd)},
so that the above maximal operator estimates read as follows

 sup
0<t<1
| exp(±itA)f|

Lp(Rd)
≲∥(1 + A)sf∥L2(Rd)
(5.1)

sup
t∈R
| exp(itA)f|

Lp(Rd)
≲∥(1 + A)sf∥L2(Rd),
(5.2)
for A = −∆and A =
√
−∆, the right choices of s and p depending on the dimension d. In this
section, we shall prove an analogue of (5.1) and (5.2) for semigroup generators A = A0 ⊗IdY
such that the semigroup of exp(−tA0) is positive and contractive on Lp, and such that A has
a Hörmander calculus on Lp(Y ). See Corollary 5.3. Note that it is well-known that A = −∆
and thus also A =
√
−∆do generate a positive contractive semigroup on Lp(Rd) and do have
a Hörmander Hα
2 functional calculus on Lp(Rd) for α >
d
2 [Hor].
Thus our quite general
21
assumptions on A are in particular satisﬁed in the above examples from [RV1, RV2]. In our
framework, the norm on the left hand side of (5.1) and (5.2) will be in Lp(Y ). Also it appears
more natural that the L2 space on the right hand side is replaced by Lp(Y ). Our Sobolev space
will be abstractly modelled as a domain of a power of A as the right hand sides of (5.1) and
(5.2) indicate. The price we have to pay for this generality is that instead of suprema over
0 < t < 1 or t ∈R as in (5.1) or (5.2), we can only handle t ∈[a, b] ⊆(0, ∞) compactly (via
a test function ψ0 ∈C∞
c (R+)). Also our parameter δ in (5.3) below will be higher (that is,
worse) than the parameter s that obtained [RV1, RV2] in (5.1) and (5.2). We then shall get in
Corollary 5.3
(5.3)

sup
t>0
|ψ0(t) exp(itA)f|

Lp(Y )
≲ψ0

(1 + A)δf

Lp(Y )
(f ∈D(Aδ))
for the correct choice of δ depending on the Hörmander calculus order of A and the geometry
of Y . The constant of the estimate depends on ψ0, in particular its support.
The following Theorem is a variant of [DK, Theorem 3.1], where elements f ∈Lp(Y ) are
replaced by functions ft ∈Lp(Y (Λβ)). Compared to [DK, Theorem 3.1], it has a diﬀerent value
for the derivation exponent c and involves the W c
1(R) norm in place of the W c
2(R) norm.
Theorem 5.1 Let Y be a UMD lattice, 1 < p < ∞and (Ω, µ) a σ-ﬁnite measure space. Let
β ⩾0. Let A be a 0-sectorial operator on Lp(Y ). Assume that A has a Hα
2 calculus on Lp(Y )
for some α > 1
2. Consider
c > α + max
1
2,
1
type Lp(Y ) −
1
cotype Lp(Y )

+ 1 + β.
Let m be a spectral multiplier such that
1. m ∈W c
1(R) and supp(m) ⊆[ 1
2, 2] or, more generally,
2. m(0) = 0, m(2n·)ϕ0 ∈W c
1(R) for all n ∈Z and P
n∈Z ∥m(2n·)ϕ0∥W c
1 (R) < ∞, where
(ϕn)n∈Z is a partition of unity of R+.
Then for ft ∈Lp(Y (Λβ
2,2(R+))), we have
(5.4)
∥t 7→m(tA)ft∥Lp(Y (Λβ
2,2(R+))) ⩽Cm∥t 7→ft∥Lp(Y (Λβ
2,2(R+))),
where
1. Cm ⩽C∥m∥W c
1 (R),
2. Cm ⩽C P
n∈Z ∥m(2n·)ϕ0∥W c
1 (R).
Proof : The proof is a variant of that of Theorem 3.3. We indicate the changements.
1. Let ψ ∈C∞
c (R+) as before and let also eψ = P
k∈F ϕk ∈C∞
c (R+), where F ⊆Z is ﬁnite,
such that eψ(t) = 1 for t ∈supp(ψ). Indeed, since supp(ψ) stays away from 0 and ∞, such a
22
funcion eψ exists. As in the proof of Theorem 3.3, we obtain for t 7→ft ∈Lp(Y (Λβ)), with,
∥t 7→m(tA)ft∥Lp(Y (Λβ)) ∼=

 X
n∈Z
∥t 7→m(tA)ϕn(A)ft∥2
Λβ
! 1
2 

Lp(Y )
=

 X
n∈Z
∥t 7→ψ(t) eψ(t)m(2−ntA)ϕn(A)f2−nt∥2
Λβ
! 1
2 

Lp(Y )
≲R

t 7→ψ(t)m(2−ntA) : n ∈Z
	
Lp(Y (Λβ))→Lp(Y (Λβ))


 X
n∈Z
∥t 7→eψ(t)ϕn(A)f2−nt∥2
Λβ
! 1
2 

Lp(Y )
.
(5.5)
Note that the operator family subject to R-boundedness is now in B(Lp(Y (Λβ))). Moreover,
since {ϕn(A) : n ∈Z}Lp(Y (Λβ))→Lp(Y (Λβ)) is R-bounded (since ∥ϕn∥Hγ
2 ⩽C and A ⊗IdΛβ has
an R-bounded Hγ
2 calculus), the square function in (5.5) above estimates further to
. . . ⩽

 X
n∈Z
∥t 7→eψ(t)f2−nt∥2
Λβ
! 1
2 

Lp(Y )
=

 X
n∈Z
∥t 7→eψ(2nt)ft∥2
Λβ
! 1
2 

Lp(Y )
⩽
X
k∈F

 X
n∈Z
∥t 7→ϕk(2nt)ft∥2
Λβ
! 1
2 

Lp(Y )
∼=

 X
n∈Z
∥t 7→ϕn(t)ft∥2
Λβ
! 1
2 

Lp(Y )
.
Now for ﬁxed (x, ω) ∈Ω× Ω′, we have
X
n∈Z
∥t 7→ϕn(t)ft(x, ω)∥2
Λβ ∼= E

X
n∈Z
εn · (t 7→ϕn(t)ft(x, ω))

2
Λβ
∼= ∥t 7→ft(x, ω)∥2
Λβ,
where the last step follows from the Paley-Littlewood equivalence [KrW2, Theorem 4.1] for the
0-sectorial operator A(t 7→ft) = t 7→t · ft on the space X = Λβ which indeed has a Mihlin
calculus as needed in this source. We infer that
(5.6)

 X
n∈Z
∥t 7→eψ(t)ϕn(A)f2−nt∥2
Λβ
! 1
2 

Lp(Y )
≲∥t 7→ft∥Lp(Y (Λβ)).
It remains to estimate the R-bound of
(5.7)

t 7→ψ(t)m(2−ntA) : n ∈Z
	
Lp(Y (Λβ))→Lp(Y (Λβ)) .
23
Develop ψ(t)m(2ntA)f as in (??). Note that Λβ is a Hilbert space (isometric to ℓ2). Note also
that Rademacher sums in Lp(Y ) are equivalent to square sums in the sense of (2.1). Then
use that by Lemma 2.9, A ⊗IdΛβ has an R-bounded Hγ
2 calculus on Lp(Y (Λβ)) to get the
R-bounded operator family {(1 + 2nA)γφ(2nA) : n ∈Z}Lp(Y (Λβ))→Lp(Y (Λβ)). Then as in the
proof of Theorem 3.3, we are left to show that
 1
2π
Z
R
hs⟨s⟩−(γ+δ)(1 + 2nA)−γ exp(i2nsA)ds : n ∈Z

Lp(Y (Λβ))→Lp(Y (Λβ))
is an R-bounded operator family, but this time as operators Lp(Y (Λβ)) →Lp(Y (Λβ)). Here
hs ∈Λβ is the function from (??). Write in short T n
s =
1
2π⟨s⟩−(γ+δ)(1 + 2nA)−γ exp(i2nsA).
Then for f1, . . . , fN ∈Lp(Y (Λβ)) and any n1, . . . , nN ∈Z,

 N
X
k=1

Z
R
hs(t)T nk
s fk(t)ds

2
Λβ
! 1
2 

Lp(Y )
⩽

 N
X
k=1
Z
R
∥hs(t)T nk
s fk(t)∥Λβds
2! 1
2 

Lp(Y )
⩽sup
s∈R
∥hs∥M(Λβ)

 N
X
k=1
Z
R
∥T nk
s fk(t)∥Λβds
2! 1
2 

Lp(Y )
⩽sup
s∈R
∥hs∥M(Λβ)
Z
R

 N
X
k=1
∥T nk
s fk(t)∥2
Λβ
! 1
2 

Lp(Y )
ds
≲sup
s∈R
∥hs∥M(Λβ)
Z
R
R

{T n
s : n ∈Z}Lp(Y (Λβ))→Lp(Y (Λβ))

ds

 N
X
k=1
∥fk(t)∥2
Λβ
! 1
2 

Lp(Y )
.
(5.8)
Here, M(Λβ) stands for the Banach algebra of pointwise multipliers of Λβ. According to
[Tri, p. 140], we have for the classical Sobolev space, M(W β
2 (R)) ⊇Cβ′ for β′ > β. Note that
since ψ has compact support in R+, similarly to Remark 2.7, we have ∥hs,e∥Cβ′ ∼= ∥hs∥Cβ′,
so that ∥hs∥M(Λβ) ≲∥hs∥Cβ′. Let us estimate ∥hs∥Cβ′ = supα⩽β′ ∥∂αhs∥∞. We have with
ξ(t) = tψ
  1
t

∈C∞
c (R+),
∥hs∥L∞(R) =

∂β′ξ(t) ˆm
s
t


L∞
t (R) ⟨s⟩γ+δ ≲
sup
t∈[ 1
8 ,8]

 ˆm
s
t


 ⟨s⟩γ+δ
(5.9)
⩽sup
s∈R
sup
t∈[ 1
8 ,8]
| ˆm(s)| ⟨st⟩γ+δ
≲

 ˆm(s)⟨s⟩γ+δ

L∞
s (R) ≲∥m∥W γ+δ
1
(R).
Moreover

ξ(t)∂β′ ˆm
s
t


L∞
t (R) ⟨s⟩γ+δ ≲

∂β′ ( ˆm) (s)sβ′⟨s⟩γ+δ

L∞
s (R)
≲

xβ′m(x)

W γ+δ+β′
1
(R) ≲∥m∥W γ+δ+β′
1
(R),
where the last step follows from the fact that m has compact support in R+, similarly to Remark
2.7. Thus,
sup
s∈R
∥hs∥M(Λβ) ≲sup
s∈R
∥hs∥Cβ′ ≲∥m∥W γ+δ+β′
1
(R) < ∞.
24
To obtain the bound in (5.8), it suﬃces to note that according to Lemma 2.9,
Z
R
R

{T n
s : n ∈Z}Lp(Y (Λβ))→Lp(Y (Λβ))

ds =
Z
R
R

{T n
s : n ∈Z}Lp(Y )→Lp(Y )

ds < ∞.
This shows with the calculation (5.8) that the set in (5.7) is R-bounded. With the square
function estimate (5.6), we conclude the bound in (5.5), and thus the proof of the ﬁrst case.
2.
Do as in the proof of Theorem 3.3, exploiting that ∥t 7→f2nt∥Lp(Y (Λβ)) = ∥t 7→
ft∥Lp(Y (Λβ)).
In the case that m(0)̸ = 0, we have the following variant of Theorem 5.1 in which we obtain
an estimate of the pointwise supremum of t 7→m(tA)ft. Here the norm ∥m∥Hα
1 is deﬁned in a
similar manner to ∥m∥Hα
2 in Deﬁnition 2.11, namely, ∥m∥Hα
1 = |m(0)|+supR>0 ∥φm(R ·)∥W α
1 (R)
for any C∞
c (0, ∞) function φ diﬀerent from the constant 0 function. Also, χ0 is as in Theorem
3.3, namely, χ0 ∈C∞(R+) with support in (0, 4] and equal to 1 on (0, 2].
Proposition 5.2 Let Y be a UMD lattice, 1 < p < ∞and (Ω, µ) a σ-ﬁnite measure space. Let
β > 1
2. Let A be a 0-sectorial operator on Lp(Y ). Assume that A has a Hα
2 calculus on Lp(Y )
for some α > 1
2. In this Proposition, we assume that A is of the form A = A0 ⊗IdY and that
exp(−tA0) is lattice positive and contractive on Lp(Ω). Let m be a spectral multiplier such that
m|[0,1] ∈C1[0, 1], ∥m′χ0∥Hc−1
1
< ∞,
X
n⩾0
∥m(2n·)ϕ0∥W c
1 (R) < ∞,
where
c > α + max
1
2,
1
type Lp(Y ) −
1
cotype Lp(Y )

+ 1 + β.
Then for ft ∈Lp(Y (Λβ
2,2(R+))), we have
∥t 7→m(tA)ft∥Lp(Y (L∞(R+))) ⩽
(5.10)
C

|m(0)| + ∥m′χ0∥Hc−1
1
+
X
n⩾0
∥m(2n·)ϕ0∥W c
1 (R)

∥t 7→ft∥Lp(Y (Λβ
2,2(R+))).
Proof
: The proof is a variant of the proof of case 3 in Theorem 3.3.
We put m1(t) =
m(t) −m(0) exp(−t). In particular, we note that

sup
t>0

e−tAft

Lp(Y )
⩽

sup
t>0
e−tA sup
s>0
|fs|

Lp(Y )
≲

sup
s>0
|fs|

Lp(Y )
Lemma 3.2
≲
∥f∥Lp(Y (Λβ)) .
The rest of the proof is identical to that of case 3 in Theorem 3.3, replacing the integration
exponent 2 by 1 everywhere.
The main result of this section then reads as follows.
Corollary 5.3 Let Y be a UMD lattice, 1 < p < ∞and (Ω, µ) a σ-ﬁnite measure space. Let
A be a 0-sectorial operator on Lp(Y ). Assume that A has a Hα
2 calculus on Lp(Y ) for some
α > 1
2. In this corollary, we assume that A is of the form A = A0 ⊗IdY and that exp(−tA0)
is lattice positive and contractive on Lp(Ω). Let
δ > α + max
1
2,
1
type Lp(Y ) −
1
cotype Lp(Y )

+ 3
2.
25
Let ψ0 ∈C∞
c (R+), i.e. with support included in a compact interval ⊆(0, ∞). Then, with
implied constants depending on ψ0 and its support, we have
∥sup
t>0
|ψ0(t) exp(itA)f| ∥Lp(Y ) ≲

(1 + A)δf

Lp(Y )
(f ∈D(Aδ)).
Proof
: We shall apply Proposition 5.2 to the spectral multiplier m(λ) = (1 + λ)−δ exp(iλ)
and the element ft = ψ0(t)(1 + tA)δf for some f ∈D(Aδ) ⊆Lp(Y ). Let β > 1
2 such that
δ > α + max

1
2,
1
type Lp(Y ) −
1
cotype Lp(Y )

+ 1 + β.
Note that according to [DK, Corollary
3.11], m satisﬁes the hypotheses of Proposition 5.2 for our choice of β and δ, since in general
∥m′χ0∥Hc−1
1
≲∥m′χ0∥Hc−1
2
and ∥m(2n·)ϕ0∥W c
1 (R) ≲ϕ0 ∥m(2n·)ϕ0∥W c
2 (R). Then we obtain

sup
t>0
|ψ0(t) exp(itA)f|

Lp(Y )
=

sup
t>0

(1 + tA)−δ exp(itA)
 1 + tA)δψ0(t)f


Lp(Y )
=

sup
t>0
|m(tA)ft|

Lp(Y )
Proposition 5.2
≲
∥ft∥Lp(Y (Λβ))
=

t 7→ψ0(t)(1 + tA)δf

Lp(Y (Λβ)) .
We estimate this further. Since ψ0 has compact support in R+, by Remark 2.7, we have

t 7→ψ0(t)(1 + tA)δf

Lp(Y (Λβ)) ≲

t 7→ψ0(t)(1 + tA)δf

Lp(Y (W ⌈β⌉
2
(R)))
≲

t 7→ψ0(t)(1 + tA)δf

Lp(Y (L2(R))) +
⌈β⌉
X
k=1

t 7→dk
dtk
 ψ0(t)(1 + tA)δf


Lp(Y (L2(R)))
≲ψ0

sup
t∈supp(ψ0)

(1 + tA)δf

Lp(Y )
+
max
k=0,...,⌈β⌉

sup
t∈supp(ψ0)

Ak(1 + tA)δ−kf

Lp(Y )
.
We ﬁx a k ∈{0, 1, . . . , ⌈β⌉}. Then
Ak(1 + zA)δ−kf = Ak(1 + A)−δ(1 + zA)δ−k(1 + A)δf = φz(A)f1
with φz(λ) = λk(1 + λ)−δ(1 + zλ)δ−k and f1 = (1 + A)δf ∈Lp(Y ) since f ∈D(Aδ). Then φz is
holomorphic and bounded on C+, thus φz(A) is a bounded operator thanks to the Hörmander
calculus, thus H∞calculus of A. Moreover, the function z 7→φz(A)f1 is analytic in some
neighborhood of supp(ψ0) ⊆(0, ∞). Thus, by the Cauchy integral formula,
φt(A)f1 =
1
2πi
Z
Γ
(z −t)−1φz(A)f1dz,
where Γ is some simple contour surrounding supp(ψ0). We obtain
sup
t∈supp(ψ0)
|Ak(1 + tA)δ−kf| ⩽1
2π
 
sup
t∈supp(ψ0),z∈Γ
|(z −t)−1|
! Z
Γ
|φz(A)f1| |dz|
and thus,

sup
t∈supp(ψ0)
|Ak(1 + tA)δ−kf|

Lp(Y )
≲
Z
Γ
∥φz(A)f1∥Lp(Y ) |dz|
≲∥f1∥Lp(Y ) =

(1 + A)δf

Lp(Y ) < ∞,
where ∥φz(A)f1∥≲∥f1∥thanks to bounded H∞calculus.
26
