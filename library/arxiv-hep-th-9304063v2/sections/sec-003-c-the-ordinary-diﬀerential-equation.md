---
doc_id: arxiv-hep-th-9304063v2
doc_title: "Level Spacing Distributions and the Bessel Kernel Craig A. Tracy∗"
section_id: sec-003-c-the-ordinary-diﬀerential-equation
section_title: "The ordinary diﬀerential equation"
section_number: C
pages: 3-6
source_pdf: 9304063v2.pdf
source_sha256: 14a82437462eae23
doc_brief: "Level Spacing Distributions and the Bessel Kernel Craig A. Tracy∗ — 26 sections: INTRODUCTION AND STATEMENT OF RESU; KN(; (α2 −aj + 2v)q2"
---
For the special case J = (0, s) the above equations can be used to show that q(s; λ), the quantity q of the last
section corresponding to the endpoint s, satisﬁes
s(q2 −1)(s q′)′ = q(sq′)2 + 1
4(s −α2)q + 1
4sq3(q2 −2)
(′= d
ds).
(1.16)
with boundary condition
3
q(s; λ) ∼
√
λ
2αΓ(1 + α) sα/2 ,
s →0.
(1.17)
This equation is reducible to a special case of the PV diﬀerential equation;3 explicitly, if q(s) = (1 + y(x))/(1 −y(x))
with s = x2, then y(x) satisﬁes PV with α′ = −β′ = α2/8, γ′ = 0 and δ′ = −2. (We have primed the usual PV
parameters to avoid confusion with the α in our kernel. We mention that this special PV can be expressed algebraically
in terms of a third Painlev´e transcendent and its ﬁrst derivative [13]. We mention also that an argument can be given
that (1.16) must be reducible to one of the 50 canonical types of diﬀerential equations found by Painlev´e, without an
explicit veriﬁcation being necessary. This will be discussed at the end of section II B.) It is sometimes convenient to
transform (1.16) by making the substitution
q(s) = cos ψ(s),
so that ψ satisﬁes
ψ′′ + 1
sψ′ = 1
8s sin (2ψ) −α2
4s2
cos ψ
sin3 ψ .
(1.18)
The Fredholm determinant is expressible in terms of q by the formula
D(J; λ) = exp

−1
4
Z s
0
log s
t q(t)2 dt

.
(1.19)
Denoting by R(s) minus the logarithmic derivative of D(J; λ) with respect to s, we have also the representation
R(s) = 1
4 cos2 ψ(s) + s
dψ
ds
2
−α2
4s cot2 ψ(s) .
(1.20)
Furthermore, R(s) itself satisﬁes a diﬀerential equation which in the Jimbo-Miwa-Okamoto σ notation for Painlev´e
III (see, in particular, (3.13) in [14]) is
(sσ′′)2 + σ′ (σ −sσ′) (4σ′ −1) −α2 (σ′)2 = 0
(1.21)
where σ(s) = sR(s); it has small s expansion
σ(s; λ) = cα s1+α

1 −
1
2(2 + α)s +
3 + 2α
16(1 + α)(2 + α)(3 + α)s2 + · · ·

+
1
1 + αc2
α s2+2α

1 −
3 + 2α
2(2 + α)2 s + · · ·

+
1
(1 + α)2 c3
α s3+3α [1 + · · ·] + · · ·
(1.22)
where
cα =
λ
22α+2
1
Γ(1 + α)Γ(2 + α) .
We mention that in the special case α = 0 and λ = 1 we have D(J; 1) = e−s/4, q(s; 1) = 1, ψ(s, 1) = 0, and
σ(s, 1) = s/4 exactly [7,8,11].
3The Painlev´e V diﬀerential equation is
d2y
dx2 =

1
2y +
1
y −1
 dy
dx
2
−1
x
dy
dx + (y −1)2
x2

α′y + β′
y

+ γ′y
x + δ′y(y + 1)
y −1
where α′, β′, γ′, and δ′ are constants.
4
D. Asymptotics
Again we take J = (0, s) and consider asymptotics as s →∞. From the random matrix point of view the interesting
quantities are
E(n; s) := (−1)n
n!
∂n
∂λn D(J; λ)

λ=1.
(1.23)
This is the probability that exactly n eigenvalues lie in J. The asymptotics of E(0, s) = D(J; 1) are obtained from
(1.19) using the asymptotics of q(s; 1) or equivalently σ(s; 1) obtained from (1.16) or (1.21), respectively.
(Our
derivation is heuristic since as far as we are aware the corresponding Painlev´e connection problem has not been
rigorously solved.) We ﬁnd that as s →∞,
E(0; s) = τα
e−s/4+α√s
sα2/4
(1.24)
×

1 + α
8 s−1
2 + 9α2
128 s−1 + ( 3α
128 + 51α3
1024 )s−3
2 + (75α2
1024 + 1275α4
32768 )s−2 + · · ·

,
where τα is a constant which cannot be determined from the asymptotics of q (or σ) alone. However, as we mentioned
above, when α = ∓1
2 this expansion must agree with those obtained from formulas (12.2.6) of [18] (see also (12.6.17)–
(12.6.19) in [18]) after replacing s by π2t2. This leads to the conjecture
τα = G(1 + α)
(2π)α/2
where G is the Barnes G-function [1]. This conjecture is further supported by numerical work similar to that described
for the analogous conjecture in [28].
As in [28], there are two approaches to the asymptotics of E(n; s) for general n. We use the notation
r(n; s) := E(n; s)
E(0; s) .
(1.25)
In the ﬁrst approach (see also [2,27]) one diﬀerentiates (1.21) successively with respect to λ. Using the known
asymptotics of σ(s; 1) and the diﬀerential equation (1.21) satisﬁed by σ(s; λ) for all λ, one can ﬁnd asymptotic
expansions for the quantities
σn(s) := ∂nσ
∂λn

λ=1
,
and these in turn can be used to ﬁnd expansions for the r(n; s).
This approach is inherently incomplete since
yet another undetermined constant enters the picture. And there are also computational problems since when one
expresses the r(n, s) in terms of the σn(s) a large amount of cancellation occurs, with the result that even the ﬁrst-order
asymptotics of r(n; s) are out of reach by this method when n is large.
The second approach uses the easily-established identity
r(n; s) =
X
i1<...<in
λi1 · · · λin
(1 −λi1) · · · (1 −λin)
(1.26)
where λ0 > λ1 > · · · are the eigenvalues of the integral operator K with λ = 1 acting on (0, s). It turns out that this
operator, rescaled so that it acts on (0, 1), commutes with the diﬀerential operator L deﬁned by
Lf(x) = (x(1 −x)f ′(x))′ −(α2
4x + sx
4 ) f(x),
with appropriate boundary conditions on f. Applying the WKB method to the equation, and a simple relationship
between the eigenvalues of K (as functions of s) and its eigenfunctions, we are able to derive the following asymptotic
formula for the eigenvalues as s →∞:
1 −λi ∼
2π
Γ(α + i + 1) i! si+ α+1
2
e−2√s 24i+2α+2.
(1.27)
5
From this and (1.26) we deduce
r(n; s) ∼
(n−1
Y
k=0
Γ(α + k + 1) k!
)
π−n 2−n(2n+2α+1) s−n2
2 −α
2 n e2n√s.
(1.28)
For the special case α = 0, the quantity r(1; s) can be expressed exactly in terms of Bessel functions (see (2.30)
below).
