---
doc_id: arxiv-2410.14661v1
doc_title: "ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III: THE RESHETIKHIN-TURAEV INVARIANTS OF CLOSED HYPERBOLIC 3-MANIFOLDS OBTAINED BY DOING INTEGRAL SURGERY ALONG THE TWIST"
section_id: sec-009-51-preparations
section_title: "Preparations"
section_number: 5.1
pages: 20-24
source_pdf: 2410.14661v1.pdf
source_sha256: 3362fcd5e28eb1f0
toc_source: outline
doc_brief: "ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III: THE RESHETIKHIN-TURAEV INVARIANTS OF CLOSED HYPERBOLIC 3-MANIFOLDS OBTAINED BY DOING INTEGRAL SURGERY ALONG THE TWIST KNOT — This is the"
---
ˆVN(θ1, θ2, θ3)
(5.1)
= π
√
−1
q
2 −1

θ2
1 −θ1 + (2p + 1)θ2
3 −(2p + 3)θ3 −2θ2 + 3
2q −1
12
+ 2θ2
N + 1
2
+ p −2q + 7
4
N + 1
2
−3(p + q) + 2
6(N + 1
2)2

+
1
N + 1
2

φN(θ2 + θ3 +
1
2
N + 1
2
−1) + φN(θ2 −θ3 +
1
2
N + 1
2
)
−φN(θ2 + θ1) −φN(θ2) −φN(θ2 −θ1))
and
ˆV (θ1, θ2, θ3) = π
√
−1
3q
2 + (q
2 −1)θ2
1 −θ1 + (2p + 1)θ2
3 −(2p + 3)θ3 −2θ2

(5.2)
+
1
2π√−1
π2
6 + Li2(e2π√−1(θ2+θ3)) + Li2(e2π√−1(θ2−θ3)))
−Li2(e2π√−1(θ2+θ1) −Li2(e2π√−1θ2) −Li2(e2π√−1(θ2−θ1))

.
Proposition 5.1. For any L > 0, in the region
{(θ1, θ2, θ3) ∈C3|(Re(θ1), Re(θ2), Re(θ3)) ∈D0, |Im(θ1)| < L, |Imθ2| < L, |Imθ3| < L},
(5.3)
ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III
21
we have
ˆVN(θ1, θ2, θ3) = ˆV (θ1, θ2, θ3) +
1
N + 1
2

π
√
−1

2θ2 + (p −2q + 7
4)

(5.4)
−1
2 log(1 −e2π√−1(θ2+θ3)) −1
2 log(1 −e2π√−1(θ2−θ3))

+
1
(N + 1
2)2wN(θ1, θ2, θ3),
with |wN(θ1, θ2, θ3)| bounded from above by a constant independent of N.
Proof. By using Taylor expansion, together with Lemma 2.6, we have
φN

θ2 + θ3 −1 +
1
N + 1
2

(5.5)
= φN(θ2 + θ3 −1) + φ′
N(θ2 + θ3 −1)
1
N + 1
2
+ φ′′
N(θ2 + θ3 −1)
2
1
(N + 1
2)2 + O

1
(N + 1
2)2

= N + 1
2
2π√−1Li2(e2π√−1(θ2+θ3)) −
π√−1
6(2N + 1)
e2π√−1(θ2+θ3)
1 −e2π√−1(θ2+θ3)
−1
2 log(1 −e2π√−1(θ2+θ3)) +
π√−1
2(2N + 1)
e2π√−1(θ2+θ3)
1 −e2π√−1(θ2+θ3) + O

1
(N + 1
2)2

.
Expanding φN

θ2 −θ3 +
1
N+ 1
2

, φN(θ2 +θ1), φN(θ2) and φN(θ2 −θ1) similarly, we obtain
1
N + 1
2

φN(θ2 + θ3 +
1
2
N + 1
2
−1) + φN(θ2 −θ3 +
1
2
N + 1
2
)
(5.6)
−φN(θ2 + θ1) −φN(θ2) −φN(θ2 −θ1))
=
1
2π√−1

Li2(e2π√−1(θ2+θ3)) + Li2(e2π√−1(θ2−θ3)) −Li2(e2π√−1(θ2+θ1))
−Li2(e2π√−1θ2) −Li2(e2π√−1(θ2−θ1))

−1
2 log(1 −e2π√−1(θ2+θ3))
−1
2 log(1 −e2π√−1(θ2−θ3)) + w′
N(θ1, θ2, θ3),
where
w′
N(θ1, θ2, θ3)
(5.7)
= π√−1
12
 
2
e2π√−1(θ2+θ3)
1 −e2π√−1(θ2+θ3) + 2
e2π√−1(θ2−θ3)
1 −e2π√−1(θ2−θ3) +
e2π√−1(θ2+θ1)
1 −e2π√−1(θ2+θ1)
+
e2π√−1(θ2+θ1)
1 −e2π√−1(θ2+θ1) +
e2π√−1θ2
1 −e2π√−1θ2 + O

1
N + 1
2
!
.
Let
wN(θ1, θ2, θ3) = w′
N(θ1, θ2, θ3) −3(p + q) + 2
6
,
(5.8)
22
QINGTAO CHEN AND SHENGMAO ZHU
then we obtain the formula (5.4).
□
We consider the critical point of ˆV (θ1, θ2, θ3) which is given by the solution of the
following equations
ˆVθ1 = π
√
−1((q −2)θ1 + 1) + log(1 −e2π√−1(θ2+θ1)) −log(1 −e2π√−1(θ2−θ1)) = 0,
(5.9)
ˆVθ2 = −2π
√
−1 −log(1 −e2π√−1(θ2+θ3)) −log(1 −e2π√−1(θ2−θ3))
(5.10)
+ log(1 −e2π√−1(θ2+θ1)) + log(1 −e2π√−1θ2) + log(1 −e2π√−1(θ2−θ1)) = 0,
ˆVθ3 = π
√
−1((4p + 2)θ3 −(2p + 3)) −log(1 −e2π√−1(θ2+θ3))
(5.11)
+ log(1 −e2π√−1(θ2−θ3)) = 0.
Proposition 5.2. The critical point equations (5.9), (5.10) and (5.11) has a unique
solution (θ0
1, θ0
2, θ0
3) in the region D0C = {(θ1, θ2, θ3) ∈C3|(Re(θ1), Re(θ2), Re(θ3)) ∈D0}.
Proof. See Appendix 6.3 for a proof.
□
Now we set ζ(p, q) to be the critical value of the potential function ˆV (p, q; θ1, θ2, θ3),
i.e.
ζ(p, q) = V (p, q, θ0
1, θ0
2, θ0
3),
(5.12)
and set
ζR(p, q) = Reζ(p, q) = ReˆV (p, q, θ0
1, θ0
2, θ0
3).
(5.13)
Lemma 5.3. When (p, q) ∈S, we have the following estimation for ζR(p, q)
2πζR(p, q) ≥3.56337.
(5.14)
Proof. See Appendix 6.1 for a proof.
□
Set z1 = e2π√−1θ1, z2 = e2π√−1θ2, and z3 = e2π√−1θ3, by straightforward computations,
we have
ˆVθ1θ1 = (q −2)π
√
−1 −2π√−1e2π√−1(θ2+θ1)
1 −e2π√−1(θ2+θ1)
−2π√−1e2π√−1(θ2−θ1)
1 −e2π√−1(θ2−θ1)
(5.15)
= 2π
√
−1
q
2 −1 −
1
z1/z2 −1 −
1
1/(z1z2) −1

ˆVθ1θ2 = −2π√−1e2π√−1(θ2+θ1)
1 −e2π√−1(θ2+θ1)
+ 2π√−1e2π√−1(θ2−θ1)
1 −e2π√−1(θ2−θ1)
(5.16)
= 2π
√
−1

1
z1/z2 −1 −
1
1/(z1z2) −1

,
ˆVθ1θ3 = 0.
(5.17)
ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III
23
ˆVθ2θ2 = 2π√−1e2π√−1(θ2+θ3)
1 −e2π√−1(θ2+θ3)
+ 2π√−1e2π√−1(θ2−θ3)
1 −e2π√−1(θ2−θ3)
−2π√−1e2π√−1(θ2+θ1)
1 −e2π√−1(θ2+θ1)
(5.18)
−2π√−1e2π√−1θ2
1 −e2π√−1θ2
−2π√−1e2π√−1(θ2−θ1)
1 −e2π√−1(θ2−θ1)
= 2π
√
−1

−
1
z1/z2 −1 −
1
1/z2 −1 −
1
1/(z1z2) −1
+
1
1/(z2z3) −1 +
1
z3/z2 −1

.
ˆVθ2θ3 = 2π√−1e2π√−1(θ2+θ3)
1 −e2π√−1(θ2+θ3)
−2π√−1e2π√−1(θ2−θ3)
1 −e2π√−1(θ2−θ3)
(5.19)
= 2π
√
−1

1
1/(z2z3) −1 −
1
z3/z2 −1

.
ˆVθ3θ3 = π
√
−1(4p + 2) + 2π√−1e2π√−1(θ2+θ3)
1 −e2π√−1(θ2+θ3)
+ 2π√−1e2π√−1(θ2−θ3)
1 −e2π√−1(θ2−θ3)
(5.20)
= 2π
√
−1

(2p + 1) +
1
1/(z2z3) −1 +
1
z3/z2 −1

.
We let
ˆf(θ1, X1, θ2, X2, θ3, X3) = ReˆV (p, q, θ1 +
√
−1X1, θ2 +
√
−1X2, θ3 +
√
−1X3),
(5.21)
then for i ∈{1, 2, 3},
ˆfXi = Re(
√
−1ˆV (p, q, θ1 +
√
−1X1, θ2 +
√
−1Xi, θ3 +
√
−1X3)
(5.22)
= −ImˆVθi(p, q, θ1 +
√
−1X1, θ2 +
√
−1X2, θ3 +
√
−1X3)
and
ˆfXiXi = −Im
√
−1ˆVθiθi(p, q, θ1 +
√
−1X, θ2 +
√
−1X2, θ3 +
√
−1X3)

.
(5.23)
Hence the Hessian matrix of ˆf is given by
Hess( ˆf) =


ˆfX1X1
ˆfX1X2
ˆfX1X3
ˆfX2X1
ˆfX2X2
ˆfX2X3
ˆfX3X1
ˆfX2X2
ˆfX3X3


(5.24)
= 2πIm


a + c
−a + c
0
−a + c
a + b + c + d + e
d −e
0
d −e
d + e


24
QINGTAO CHEN AND SHENGMAO ZHU
where
a = −Im
1
1 −z2/z1
= −
sin(2π(θ2 −θ1))
e2π(X2−X1) + e−2π(X2−X1) −2 cos(2π(θ2 −θ1))
(5.25)
b = −Im
1
1 −z2
= −
sin(2πθ2)
e2πX2 + e−2πX2 −2 cos(2πθ2)
c = −Im
1
1 −z1z2
= −
sin(2π(θ2 + θ1))
e2π(X2+X1) + e−2π(X2+X1) −2 cos(2π(θ2 + θ1))
d = Im
1
1 −z2z3
=
sin(2π(θ2 + θ3))
e2π(X2+X3) + e−2π(X2+X3) −2 cos(2π(θ2 + θ3))
e = Im
1
1 −z2/z3
=
sin(2π(θ2 −θ3))
e2π(X2−X3) + e−2π(X2−X3) −2 cos(2π(θ2 −θ3)).
Obviously, when 1
2 < θ2 −θ1, θ2, θ2 + θ1 < 1, 1 < θ2 + θ3 < 3
2 and 0 < θ2 −θ3 < 1
2, we
have that a, b, c, d, e > 0.
Set
DH = {(θ1, θ2, θ3) ∈D0|1
2 < θ2 ± θ1, θ2 < 1, 1 < θ2 + θ3 < 3
2, 0 < θ2 −θ3 < 1
2}.
(5.26)
We obtain
Proposition 5.4. For (θ1, θ2, θ3) ∈DH, the Hessian matrix
Hess( ˆf)
(5.27)
is positive definite.
Proof. Since

a + c
−a + c
0
−a + c
a + b + c + d + e
d −e
0
d −e
d + e

(5.28)
= abd + abe + 4acd + 4ace + 4ade + cbd + cbe + 4cde > 0,

a + c
−a + c
−a + c
a + b + c + d + e

(5.29)
= ab + 4ac + ad + ae + cb + cd + ce > 0
and a + c > 0 by a, b, c, d, e > 0 when (θ1, θ2, θ3) ∈DH.
□
