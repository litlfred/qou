---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-011-31-the-41-knot-when-u0
section_title: "The 41 knot when u=0"
section_number: 3.1
pages: 12-17
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
toc_source: outline
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
Z41(0; τ) =
Z
R+i0
Φb(v)2 e−πiv2dv .
(37)
The critical points of the integrand are the logarithms of the solutions ξ1 = e2πi/6 and
ξ2 = e−2πi/6 of the polynomial equation
(1 −y)(1 −y−1) = 1 .
(38)
The labeling set P = {σ1, σ2}, where σ1 corresponds to the geometric representation of the
41 and σ2 to the complex conjugate of the geometric representation. Observe that ξ1 (resp.,
ξ2) lie in the trace ﬁeld Q(√−3) (resp., its complex conjugate) of the 41 knot, where Q(√−3)
is a subﬁeld of the complex numbers with √−3 taken to have positive imaginary part.
The ﬁrst ingredient is a vector of formal power series
Φ(τ) =

Φσ1(τ)
Φσ2(τ)

(39)
deﬁned by the asymptotic expansion of the state-integral (37) at each of the two critical
points, and which has the form
Φσ(τ) = exp
V (σ)
2πiτ

ϕσ(τ),
(40)
satisﬁes the symmetry Φσ2(τ) = iΦσ1(−τ), where
V (σ1) = iVol(41) = i 2Im Li2(eiπ/3) = i 2.029883 . . . .
(41)
with Vol(41) being the hyperbolic volume of 41 and the ﬁrst few terms of ϕσ1(τ/(2πi)) ∈
3−1/4Q(√−3)[[τ]] are given by
ϕσ1
 τ
2πi

=
1
4√
3

1 +
11τ
72√−3 +
697τ 2
2 (72√−3)2 +
724351τ 3
30 (72√−3)3 + · · ·

.
(42)
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY
13
The second ingredient is a vector G(q) =

G0(q)
G1(q)

of q-series deﬁned for |q| < 1 by
G0(q) =
∞
X
n=0
(−1)nqn(n+1)/2
(q; q)2
n
(43a)
G1(q) =
∞
X
n=0
(−1)nqn(n+1)/2
(q; q)2
n
 
E1(q) + 2
n
X
j=1
1 + qj
1 −qj
!
,
(43b)
where E1(q) = 1 −4 P∞
n=1 qn/(1 −qn) is the Eisenstein series, and extended to |q| > 1 by
G0(q−1) = G0(q) and G1(q−1) = −G1(q). These series are motivated by, and appear in, the
factorization of the state-integral of the 41 knot given in [GK17, Cor.1.7]
Z41(0; τ) = −i
2
q
˜q
 1
24 √τG0(˜q)G1(q) −1
√τ G0(q)G1(˜q)

,
(τ ∈C \ R)
(44)
where
q = e2πiτ,
˜q = e−2πi/τ .
(45)
The above factorization follows by applying the residue theorem to the integrand of (37),
a meromorphic function of v with prescribed zeros and poles. In particular, the integrand
of (37) determines the q-hypergeometric formula for the vector G(q) of q-series.
Below,
given a q-series H(q) deﬁned on |q|̸ = 1, we denote by h(τ) = H(e2πiτ) the corresponding
holomorphic function in C \ R.
The vector G(q) of q-series and the vector of asymptotic series Φ(τ) come together when
we consider the asymptotics of diag( 1
√τ , √τ)g(τ) in the τ-plane (as was studied in [GZa]) and
compare them with the Borel summed vector Φ. Recall that when the Borel transform of an
asymptotic series has singular points ιi in the Borel plane, the rays (Stokes rays) emanating
from the origin with angle θ = arg ιi divide the complex plane into diﬀerent sectors. When
one crosses into neighboring sectors, the Borel sum of the asymptotic series undergoes Stokes
automorphism. In the case of the vector of asymptotic series Φ(τ), the singularities of the
Borel transforms of its two component asymptotic series are located at
ιi,j = V (σi) −V (σj)
2πi
,
i, j = 1, 2, i̸ = j,
(46)
as well as
2πik, ιi,j + 2πik ,
k ∈Z̸=0,
(47)
forming vertical towers as illustrated in Figure 2. In particular, the two singularities ι1,2, ι2,1
are on the positive and the negative real axis. We pick out four sectors which separate the
two singularities on the real axis and all the others, and label them by I, II, III, IV , as
illustrated in Figure 3. The relation between the vector G(q) and the Borel summed vector
Φ(τ) depend on the sector R. In [GGMn], we found out that we do not get an agreement,
but rather both sides agree up to powers of the exponentially small quantity ˜q, and what
is more, several coeﬃcients of those powers were numerically recognized to be integers. In
other words, we found that
diag( 1
√τ , √τ)g(τ) = MR(˜q) sR(Φ)(τ) .
(48)
14
STAVROS GAROUFALIDIS, JIE GU, AND MARCOS MARIÑO
where diag(v) denotes the diagonal matrix with diagonal given by v and MR(q) is a matrix
of q-series with integer coeﬃcients.
ι1,2 = Vol(41)/π
ϕσ1(τ)
ι2,1 = −Vol(41)/π
ϕσ2(τ)
Figure 2. The singularities in the Borel plane for the series ϕσj(0; τ) for
j = 1, 2 of knot 41.
I
II
IV
III
L
Figure 3. Four diﬀerent sectors in the τ-plane for Φ(0; τ) of knot 41.
To identify the matrices MR, we used the third ingredient, namely the linear q-diﬀerence
equation
ym+1(q) −(2 −qm)ym(q) + ym−1(q) = 0
(m ∈Z) .
(49)
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY
15
It has a fundamental solution set given by the columns of the following matrix
Wm(q) =

G0
m(q)
G1
m(q)
G0
m+1(q)
G1
m+1(q)

,
(|q|̸ = 1)
(50)
where Gm(q) =

G0
m(q)
G1
m(q)

, and G0
m(q) and G1
m(q) are deﬁned by
G0
m(q) =
∞
X
n=0
(−1)nqn(n+1)/2+mn
(q; q)2
n
(51a)
G1
m(q) =
∞
X
n=0
(−1)nqn(n+1)/2+mn
(q; q)2
n
 
2m + E1(q) + 2
n
X
j=1
1 + qj
1 −qj
!
,
(51b)
for |q| < 1 and extended to |q| > 1 by Gj
m(q−1) = (−1)jGj
m(q). Observe that G0(q) = G(q),
the vector that appears in the factorization (44) of the state-integral Z41(0; τ). The matrix
Wm(q) of holomorphic functions in |q|̸ = 1 satisﬁes several properties summarized in the
following theorem.
Theorem 9. Wm(q) is a fundamental solution of the linear q-diﬀerence equation (49) that
has constant determinant
det(Wm(q)) = 2 ,
(52)
satisﬁes the symmetry
Wm(q−1) = W−m(q)

1
0
0
−1

,
(53)
the orthogonality property
1
2Wm(q)

0
1
−1
0

Wm(q)T =

0
1
−1
0

(54)
as well as
1
2Wm(q)

0
1
−1
0

Wℓ(q)T ∈SL(2, Z[q±])
(55)
for all integers m, ℓand for |q|̸ = 1.
Conjecture 10. Equation (48) holds where the matrices MR(q) are given in terms of W−1(q)
as follows
MI(q) = W−1(q)T

0
−1
1
−1

,
|q| < 1 ,
(56a)
MII(q) =

1
0
0
−1

W−1(q)T

1
0
1
−1

,
|q| < 1 ,
(56b)
MIII(q) = W−1(q−1)T

1
0
1
1

,
|q| > 1 ,
(56c)
MIV (q) =

1
0
0
−1

W−1(q−1)T

0
1
1
1

,
|q| > 1 .
(56d)
16
STAVROS GAROUFALIDIS, JIE GU, AND MARCOS MARIÑO
Assuming the above conjecture, we can now describe completely the resurgent structure
of Φ(τ). The Stokes matrices are given by
S+(q) = SI→II(q)SIV →I,
S−(q) = SIII→IV (q)SII→III ,
(57)
where
SI→II(q) = MII(q)−1MI(q)
SIII→IV (q) = MIV (q−1)−1MIII(q−1)
(58a)
SIV →I = MI(q)−1MIV (q)
SII→III = MIII(q)−1MII(q) .
(58b)
(Compare with Equations (33) and (34) after we set ˜x = 1 and replace ˜q by q). Note that
since MI(q), MII(q) and MIII(q), MIV (q) are given respectively as q-series and q−1-series in
(56a),(56b) and (56c),(56d), analytic continuation as discussed below (51b) is needed when
one computes SIV →I, SII→II in (58b). Using (52)–(55) we can express the answer in terms
of W−1(q). Explicitly, the Stokes matrices are given by
S+(q) = 1
2

0
−1
1
1

W−1(q)

0
1
1
0

W−1(q)T

0
−1
1
2

,
|q| < 1 ,
(59a)
S−(q) = 1
2

−1
−1
0
1

W−1(q)

0
1
1
0

W−1(q)T

1
0
−2
1

,
|q| < 1 .
(59b)
In the q →0 limit,
S+(0) =

1
3
0
1

,
S−(0) =

1
0
−3
1

(60)
whose oﬀ-diagonal entries −3, +3 are Stokes constants associated to the singularities ι2,1
and ι1,2 on the negative and positive real axis respectively, and they agree with the matrix
of integers obtained numerically in [GH18, GZb]. In addition, we can assemble the Stokes
constants into the matrix S of Equation (36) (after we set ˜x = 1 and replace ˜q by q). The
resulting matrix S+(q) has entries in qZ[[q]], and we ﬁnd
S+
σ1,σ1(q) =S+(q)1,1 −1
= −8q −9q2 + 18q3 + 46q4 + 90q5 + 62q6 + O(q7),
(61)
S+
σ1,σ2(q) =S+(q)1,2/S+(q)1,1 −S(0)
σ1,σ2
=9q + 75q2 + 642q3 + 5580q4 + 48558q5 + 422865q6 + O(q7),
(62)
S+
σ2,σ1(q) =S+(q)2,1/S+(q)1,1
= −9q −75q2 −642q3 −5580q4 −48558q5 −422865q6 + O(q7),
(63)
S+
σ2,σ2(q) =S+(q)2,2 −1 −S+(q)1,2S+(q)2,1/S+(q)1,1
=8q + 73q2 + 638q3 + 5571q4 + 48538q5 + 422819q6 + O(q7).
(64)
We notice the symmetry
S(k)
1,2 = −S(k)
2,1,
for k ∈Z>0 ,
(65)
which is due to the reﬂection property ϕσ1(−τ ∗) = ϕσ2(τ)∗of the asymptotic series. Also
experimentally it appears that the entries of the matrix S+(q) = (S+
σi,σj(q)) (except the
upper-left one) are (up to a sign) in N[[q]]. Similarly we can extract the Stokes constants
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY
17
S(−k)
σi,σj associated to the singularities in the lower half planes and collect them in q−1-series
S−
σi,σj(q−1) accordingly, and we ﬁnd
S(−k)
σi,σj = −S(+k)
σj,σi, i̸ = j ,
and
S(−k)
σ1,σ1 = S(+k)
σ2,σ2, S(−k)
σ2,σ2 = S(+k)
σ1,σ1,
for k ∈Z>0.
(66)
A nontrivial consistency check in the above calculation is that the matrices SIV →I(q) and
SII→III(q) should come out to be independent of q, and coincide with S−(0) and S+(0).
That is exactly what we ﬁnd.
The fourth and last ingredient, which makes a full circle of ideas, is the descendant state-
integral of the 41 knot
Z41,m,µ(0; τ) =
Z
D
Φb(v)2 e−πiv2+2π(mb−µb−1)v dv
(m, µ ∈Z) .
(67)
The integration contour D asymptotes at inﬁnity to the horizontal line Imv = v0 with
v0 > |Re(mb −µb−1)| but is deformed near the origin so that all the poles of the quantum
dilogarithm located at
cb + ibr + ib−1s,
r, s ∈Z≥0,
(68)
are above the contour. The integral Z41,m,µ(0; τ) is a holomorphic function of τ ∈C′ that
coincides with Z41(0; τ) when m = µ = 0 and can be expressed bilinearly in Gm(q) and
Gµ(˜q) as follows
Z41,m,µ(0; τ) = (−1)m−µ+1iq
m
2 ˜q
µ
2
q
˜q
 1
24 1
2
√τ G0
µ(˜q)G1
m(q) −1
√τ G1
µ(˜q)G0
m(q)

.
(69)
It follows that the matrix-valued function
Wm,µ(τ) = (Wµ(˜q)T)−1

1/√τ
0
0
√τ

Wm(q)T
(70)
deﬁned for τ = C\R, has entries given by the descendant state-integrals (up to multiplication
by a prefactor of (69)) and hence extends to a holomorphic function of τ ∈C′ for all integers
m and µ. Using this for m = −1 and µ = 0 and the orthogonality relation (54), it follows that
we can express the Borel sums of Φ(τ) in a region R in terms of descendant state-integrals
and hence, as holomorphic functions of τ ∈C′ as follows. For instance, in the region I we
have
sI(Φ)(τ) = MI(˜q)−1
 1
√τ g0
0(τ)
√τg1
0(τ)

= i
q
˜q
−1
24 
Z41,0,0(0; τ) −˜q1/2Z41,0,−1(0; τ)
Z41,0,0(0; τ)

(71)
This completes the discussion of u = 0 for the 41 knot.
