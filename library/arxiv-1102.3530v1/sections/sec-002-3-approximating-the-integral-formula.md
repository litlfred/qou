---
doc_id: arxiv-1102.3530v1
doc_title: "THE COLORED JONES POL YNOMIAL, THE CHERN–SIMONS"
section_id: sec-002-3-approximating-the-integral-formula
section_title: "Approximating the integral formula"
section_number: 3
pages: 6-10
source_pdf: 1102.3530v1.pdf
source_sha256: ad3edab19f3dc404
doc_brief: "THE COLORED JONES POLYNOMIAL, THE CHERN–SIMONS — W e show that from the asymptotic behavior of an evaluation of the colored Jones polynomial of the ﬁgure-eight knot we can extr act the Chern– Simons"
---
In this section we approximate the integral formula for the colored Jones poly-
nomial obtained in the previous section.
Since tan(Nπw ) is close to √−1 ( −√−1, respectively) when Im( w) is posi-
tive and large (negative and | Im(w)| is large, respectively), we can approximate
G±(N,ε ) by the integral of gN (w) on C±(ε). In fact if we write
G±(N,ε ) = ±
√
−1
∫
C±(ε)
gN (w)dw +
∫
C±(ε)
(tan(Nπw ) ∓
√
−1)gN (w)dw,
then we have the following lemma.
Proposition 3.1 (see Equation (4.7) in [1]) . There exists a positive constant K1, ±
independent of N and ε such that the following inequality holds:
⏐
⏐
⏐
⏐
⏐
∫
C±(ε)
(tan(Nπw ) ∓
√
−1)gN (w)dw
⏐
⏐
⏐
⏐
⏐< K1, ±
N .
A proof is given in Section 6.
Now we approximate the integral of gN (w) along C±(ε). Deﬁne
Φ(w) := 1
ξ
(
Li2
(
eu−ξw)
− Li2
(
eu+ξw))
−uw.
Since Li 2 is analytic in the region C \ (1, ∞), the function Φ is analytic in the region
{w ∈ C | − 2π
u Re(w)< Im(w)< − 2π
u (Re(w) − 1)} (Figure 1).
Proposition 3.2 (see Equation (4.9) in [1]) . Let p(ε) be any contour in the par-
allelogram bounded by C(ε) connecting ε and 1 −ε, then there exists a positive
constantK2 independent of N and ε such that the following inequality holds.
⏐
⏐
⏐
⏐
⏐
∫
p(ε)
gN (w)dw −
∫
p(ε)
exp(N Φ(w))dw
⏐
⏐
⏐
⏐
⏐ ≤ K2 log(N )
N max
w∈p(ε)
{
exp
(
N Re Φ(w)
)}
.
A proof is given in Section 7.
We will study the asymptotic behavior of
∫
C±(ε) exp
(
N Φ(w)
)
dw for large N .
Since Φ( w) is analytic in the region {w ∈ C | − 2π
u Re(w) < Im(w) <
− 2π
u (Re(w) − 1)}, we have
∫
C+(ε)
exp
(
N Φ(w)
)
dw =
∫
C−(ε)
exp
(
N Φ(w)
)
dw
by Cauchy’s integral theorem.
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 7
We will apply the saddle point method (see for example [16, § 7.2]) to approxi-
mate the integral
∫
C−(ε) exp(N Φ(w))dw.
First we ﬁnd a solution to the equation d Φ(w)/dw = 0. Since we have
d Φ(w)
dw = log(1 −eu−ξw ) + log(1 −eu+ξw ) −u,
a solution to the equation
eξw +e−ξw =eu +e−u − 1
can be a saddle point that we need. Put
ϕ(u) := arccosh(cosh(u) − 1/2)
= log
( 1
2
(
eu +e−u − 1 −
√
(eu +e−u + 1)(eu +e−u − 3)
) )
,(3.1)
˜ϕ(u) := ϕ(u) + 2π
√
−1,
and
w0 := ˜ϕ(u)
ξ ,
where we choose the square root of ( eu +e−u +1)(eu +e−u −3) as a positive multiple
of √−1 and the branch of log so that −π/3< Imϕ(u)< 0.
Remark 3.3. Note that ϕ(u) and ˜ ϕ(u) are purely imaginary since⏐
⏐
⏐eu +e−u − 1 −
√
(eu +e−u + 1)(eu +e−u − 3)
⏐
⏐
⏐ = 4.
It is easy to see that d Φ(w0)/dw = 0. Since we have
Im(w0) + 2π
u Re(w0) = Im ˜ϕ(u)
u ,
w0 is in the domain of Φ.
We choose a pathP fromε to 1−ε that passes throughw0 so that nearw0 it keeps
Im Φ(w) constant and that Re Φ( w) takes its maximum (over all w on P ) at w0 as
indicated in the thick curve in Figures 2. Then the integral
∫
C−(ε) exp(N Φ(w))dw
is approximated by the integral near w0 along the path we choose. More precisely
we have
(3.2)
∫
C−(ε)
exp(N Φ(w))dw ∼
N →∞
√
2π exp(N Φ(w0))√
N
√
−d2 Φ(w0)/dw 2
from [16, Theorem 7.2.8], where the sign of the square root of −d2 Φ(w0)/dw 2 is
chosen so that
(3.3)
√
−d2 Φ(w0)/dw 2 × (tangent of P at w0)> 0.
Note that
(3.4) Φ( w0) = 1
ξ
(
Li2
(
eu−ϕ (u)
)
− Li2
(
eu+ϕ (u)
)
−u ˜ϕ(u)
)
.
From Propositions 3.1 and 3.2, choosing P as a contour in Proposition 3.2 we
have⏐
⏐
⏐
⏐
⏐G±(N,ε ) ∓
√
−1
∫
C±(ε)
exp
(
N Φ(w)
)
dw
⏐
⏐
⏐
⏐
⏐
≤
⏐
⏐
⏐
⏐
⏐
∫
C±(ε)
(tan(Nπw ) ∓
√
−1)gN (w)dw ±
√
−1
∫
C±(ε)
(
gN (w) − exp
(
N Φ(w)
))
dw
⏐
⏐
⏐
⏐
⏐
≤K1, ±
N + K2 log(N )
N exp
(
N Re Φ(w0)
)
.
8 HITOSHI MURAKAMI
1
0.5 
-0.5 
-1 
0
0 0.2 0.4 0.6 0.8 1
Figure 2. A contour plot of Re Φ( w) on the complex plane for
u = 0.9. A brighter part is higher than a darker part. The path P
is indicated by a thick curve and the saddle point w0 is marked by
a circle.
From (3.2) we have
lim
N →∞
⏐
⏐
⏐
⏐
⏐
G±(N,ε )
±√−1∫
C±(ε) exp
(
N Φ(w)
)
dw − 1
⏐
⏐
⏐
⏐
⏐
≤ K1, ±
N
⏐
⏐
⏐
∫
C±(ε) exp
(
N Φ(w)
)
dw
⏐
⏐
⏐
+ K2 log(N )
N × exp
(
N Re Φ(w0)
)
⏐
⏐
⏐
∫
C±(ε) exp
(
N Φ(w)
)
dw
⏐
⏐
⏐
− →
N →∞
0.
Here we use the following lemma which will be proved in Section 3.4.
Lemma 3.4. The real part of Φ(w0) is positive for 0 < u < log
(
(3 +
√
5)/2
)
.
Therefore from (3.2) we see that
∫
C±(ε) exp
(
N Φ(w)
)
dw grows exponentially.
So we have
G±(N,ε ) ∼
N →∞
±
√
−1
∫
C±(ε)
exp
(
N Φ(w)
)
dw.
Therefore from (2.4) we have
JN
(
K; exp(ξ/N )
)
∼
N →∞
e2π √−1uN/ξ
eu − 1
Ne u/ 2
2
( ∫
C−(ε)
exp(N Φ(w))dw −
∫
C+(ε)
exp(N Φ(w))dw
)
=Ne 2π √−1uN/ξ
2 sinh(u/2)
( ∫
C−(ε)
exp(N Φ(w))dw
)
from the lemma below.
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 9
Lemma 3.5. Forγ = (2π − √−1u)/(2N ) with positive u, we have
Sγ (−π − √−1u +γ)
Sγ (π − √−1u −γ) = eπu/γ − 1
eu − 1 .
Therefore we have the following asymptotic equivalence:
Sγ (−π − √−1u +γ)
Sγ (π − √−1u −γ) ∼
N →∞
e2π √−1uN/ξ
eu − 1 .
A proof of the lemma is given in Section 5.
Remark 3.6. When u = 0, we have
Sγ (−π +γ)
Sγ (π −γ) =N
from [1, P. 492].
Since
d2 Φ(w0)
dw 2 =ξ
√
(eu +e−u + 1)(eu +e−u − 3),
we have the following asymptotic equivalence from (3.2):
∫
C−(ε)
exp(N Φ(w))dw ∼
N →∞
√
2π exp(N Φ(w0))
√
N
√
−ξ
√
(eu +e−u + 1)(eu +e−u − 3)
,
where we choose the square root of
√
−ξ
√
(eu +e−u + 1)(eu +e−u − 3) so that it
is in the fourth quadrant from (3.3).
Therefore we ﬁnally have
JN
(
E; exp(ξ/N )
)
∼
N →∞
Ne 2π √−1uN/ξ
2 sinh(u/2)
√
2π
√
N
√
−ξ
√
(eu +e−u + 1)(eu +e−u − 3)
× exp
( N
ξ
(
Li2
(
eu−ϕ (u)
)
− Li2
(
eu+ϕ (u)
)
−u ˜ϕ(u)
) )
=
√π
2 sinh(u/2)
√
−2√
(eu +e−u + 1)(eu +e−u − 3)
√
N
ξ exp
( N
ξ S(u)
)
.
Here we put
S(u) := Li 2
(
eu−ϕ (u)
)
− Li2
(
eu+ϕ (u)
)
−uϕ(u).
Remark 3.7. When u = 0, we have
∫
C−(ε)
exp(N Φ(w))dw ∼
N →∞
exp(N Φ(w0))√
N 31/ 4 .
Since w0 = 5/6 in this case we have
Φ(w0) = 1
2π√−1
(
Li2(e−5π √−1/ 3) − Li2(e5π √−1/ 3)
)
= 6√−1Λ(π/3)
2π√−1 = Vol(E)
2π .
Therefore from Remark 3.6, we have Theorem 1.3.
4. Topological interpretations of S(u) and T (u)
In this section we describe topological interpretations of S(u) and T (u).
10 HITOSHI MURAKAMI
