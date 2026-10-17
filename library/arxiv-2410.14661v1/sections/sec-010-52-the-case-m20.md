---
doc_id: arxiv-2410.14661v1
doc_title: "ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III: THE RESHETIKHIN-TURAEV INVARIANTS OF CLOSED HYPERBOLIC 3-MANIFOLDS OBTAINED BY DOING INTEGRAL SURGERY ALONG THE TWIST"
section_id: sec-010-52-the-case-m20
section_title: "The case m2=0"
section_number: 5.2
pages: 24-29
source_pdf: 2410.14661v1.pdf
source_sha256: 3362fcd5e28eb1f0
toc_source: outline
doc_brief: "ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III: THE RESHETIKHIN-TURAEV INVARIANTS OF CLOSED HYPERBOLIC 3-MANIFOLDS OBTAINED BY DOING INTEGRAL SURGERY ALONG THE TWIST KNOT — This is the"
---
if exists some ϵ > 0, such that
ˆhN(m1, m2, m3) = O(e(N+ 1
2 )(ζR(p,q)−ϵ)).
(5.30)
ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III
25
We introduce
ˆV (θ1, θ2, θ3, m1, m2, m3) = ˆV (θ1, θ2, θ3) −2π
√
−1
3
X
i=1
miθi
(5.31)
= π
√
−1
3q
2 +
q
2 −1

θ2
1 −(2m1 + 1)θ1 + 2(m2 + 1)θ2 + (2p + 1)θ2
3 −(2p + 3 + 2m3)θ3

+
1
2π√−1
π2
6 + Li2(e2π√−1(θ2+θ3)) + Li2(e2π√−1(θ2−θ3)) −Li2(e2π√−1(θ2+θ1))
−Li2(e2π√−1θ2) −Li2(e2π√−1(θ2−θ1))

.
First, when m2 = −1, it is easy to see that
lim
X2→+∞ReˆV (θ1 +
√
−1X1, θ2 +
√
−1X2, θ3 +
√
−1X3; m1, m2, m3)|X3=X1=0
(5.32)
=
lim
X2→+∞Re

1
2π√−1

Li2(e2π√−1(θ2+θ3+√−1X2)) + Li2(e2π√−1(θ2−θ3+√−1X2))
−Li2(e2π√−1(θ2−θ1+√−1X2)) −Li2(e2π√−1(θ2+√−1X2)) −Li2(e2π√−1(θ2+θ1+√−1X2))

= 0.
It follows that the term ˆhN(m1, −1, m3) can be neglected for any m1, m3 ∈Z.
Next, we consider the case m2̸ = −1. Motivated by Lemma 2.4, for (θ1, θ2, θ3) ∈D0,
we introduce the following function
(5.33)
F(X1, X2, X3; m1, m2, m3) =



0
(if X2 + X3 ≥0)

θ2 + θ3 −3
2

(X2 + X3)
(if X2 + X3 < 0)
+



0
(if X2 −X3 ≥0)

θ2 −θ3 −1
2

(X2 −X3)
(if X2 −X3 < 0)
−



0
(if X2 ≥0)

θ2 −1
2

X2
(if X2 < 0)
−



0
(if X2 + X1 ≥0)

θ2 + θ1 −1
2

(X2 + X1)
(if X2 + X1 < 0)
−



0
(if X2 −X1 ≥0)

θ2 −θ1 −1
2

(X2 −X1)
(if X2 −X1 < 0)
+

−
q
2 −1

θ1 + m1 + 1
2

X1 + (m2 + 1)X2 +

p + 3
2 + m3 −(2p + 1)θ3

X3
26
QINGTAO CHEN AND SHENGMAO ZHU
where we use θ2 +θ3 −3
2 instead of θ2 +θ3 −1
2 in the first summation since in our situation
1 < θ2 + θ3 < 2.
The following simple observation is useful.
Lemma 5.5. Given a linear function on F(X1, X2, X3) = AX1 + BX2 + CX3 over R3
with X1 ≥X2 ≥X3 ≥0, we have
(1) If A < 0 or A + B < 0 or A + B + C < 0, then we can find a direction with
X2
1 + X2
2 + X2
3 →∞, such that F(X1, X2, X3) →−∞;
(2) If A > 0 and A + B > 0 and A + B + C > 0, then we have F(X1, X2, X3) →+∞
as X2
1 + X2
2 + X2
3 →+∞.
Then we have
Proposition 5.6. If (θ1, θ2, θ3) ∈D0 satisfies the following 26 inequalities:
(1) : m2 + 1 > 0
(2) : (2p + 1)θ3 < p + m2 + m3 + 5
2
(3) : 2pθ3 + θ2 < p + m3 + 2
(4) : (2p −1)θ3 −θ2 < p −m2 + m3
(5) : θ2 > m2 + 1
2
(6) : (2p −1)θ3 + θ2 > p + m2 + m3 + 1
(7) : 2pθ3 −θ2 > p + m3
(8) : (2p + 1)θ3 > p −m2 + m3 + 1
2
(9) : (2p + 1)θ3 + (q
2 −1)θ1 < p + m2 + m3 + m1 + 3
(10) : (q
2 −1)θ1 < m2 + m1 + 3
2
(11) : θ2 −q
2θ1 > −m1
(12) : (2p + 1)θ3 −(q
2 −1)θ1 < p + m2 + m3 −m1 + 2
(13) : (q
2 −1)θ1 > −m2 + m1 −1
2
(14) : θ2 + q
2θ1 > m1 + 1
(15) : 2pθ3 + q
2θ1 < p + m3 + m1 + 2
(16) : 2pθ3 −q
2θ1 < p + m3 −m1 + 1
(17) : (2p −1)θ3 −θ2 + (q
2 + 1)θ1 < p −m2 + m3 + m1 + 1
2
(18) : (2p −1)θ3 −θ2 −(q
2 + 1)θ1 < p −m2 + m2 −m1 −1
2
ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III
27
(19) : θ2 −(q
2 + 1)θ1 > m2 −m1
(20) : θ2 + (q
2 + 1)θ1 > m2 + m1 + 1
(21) : (2p −1)θ3 + θ2 −(q
2 + 1)θ1 > p + m2 + m3 −m1 + 1
2
(22) : (2p −1)θ3 + θ2 + (q
2 + 1)θ1 > p + m2 + m3 + m1 + 3
2
(23) : 2pθ3 −q
2θ1 > p + m3 −m1
(24) : 2pθ3 + q
2θ1 > p + m3 + m1 + 1
(25) : (2p + 1)θ3 −(q
2 −1)θ1 > p −m1 + m3 −m1
(26) : (2p + 1)θ3 + (q
2 −1)θ1 > p −m2 + m3 + m1 + 1
then we have F(X1, X2, X3, m1, m2, m3) →+∞as X2
1 + X2
2 + X2
3 →+∞.
We prove the proposition by subdividing (X1, X2, X3) ∈R3 into 48 regions.
Case I: X2 ≥X3 ≥0,
I-A: X2 ≥X3 ≥X1 ≥0, then
F(X1, X2, X3; m1, m2, m3)
(5.34)
= (m2 + 1)X2 + (p + m3 + 3
2 −(2p + 1)θ3)X3 + (m1 + 1
2 −(q
2 −1)θ1)X1
By Lemma 5.5, if
m1 + 1 > 0,
(2p + 1)θ3 < p + m2 + m3 + 5
2,
(5.35)
and
(2p + 1)θ3 + (q
2 −1)θ1 < p + m2 + m3 + m1 + 3
(5.36)
then we have F(X1, X2, X3) →+∞as X2
1 + X2
2 + X2
3 →+∞.
I-B: X2 ≥X1 ≥X3 ≥0,
F(X1, X2, X3; m1, m2, m3)
(5.37)
= (m2 + 1)X2 + (m1 + 1
2 −(q
2 −1)θ1)X1 + (p + m3 + 3
2 −(2p + 1)θ3)X3
By Lemma 5.5, if
m2 + 1 > 0, (q
2 −1)θ1 < m2 + m1 + 3
2
(5.38)
and
(2p + 1)θ3 + (q
2 −1)θ1 < p + m2 + m3 + m1 + 3
(5.39)
then we have F(X1, X2, X3) →+∞as X2
1 + X2
2 + X2
3 →+∞.
28
QINGTAO CHEN AND SHENGMAO ZHU
I-C: X2 ≥X1 ≥X3 ≥0,
F(X1, X2, X3; m1, m2, m3)
(5.40)
= (m1 + θ2 −q
2θ1)X1 + (m2 + 3
2 −θ2 + θ1)X2 + (p + m3 + 3
2 −(2p + 1)θ3)X3
By Lemma 5.5, if
m1 + θ2 −q
2θ1 > 0, (q
2 −1)θ1 < m2 + m1 + 3
2
(5.41)
and
(2p + 1)θ3 + (q
2 −1)θ1 < p + m2 + m3 + m1 + 3
(5.42)
then we have F(X1, X2, X3) →+∞as X2
1 + X2
2 + X2
3 →+∞.
I-D: X2 ≥X3 ≥−X1 ≥0,
F(X1, X2, X3; m1, m2, m3)
(5.43)
= (m2 + 1)X2 + (p + m3 + 3
2 −(2p + 1)θ3)X3 + (−m1 −1
2 + (q
2 −1)θ1)(−X1)
By Lemma 5.5, if
m2 + 1 > 0, (2p + 1)θ3 < p + m2 + m3 + 5
2
(5.44)
and
(2p + 1)θ3 −(q
2 −1)θ1 < p + m2 + m3 −m1 + 2
(5.45)
then we have F(X1, X2, X3) →+∞as X2
1 + X2
2 + X2
3 →+∞.
I-E: X2 ≥−X1 ≥X3 ≥0,
F(X1, X2, X3; m1, m2, m3)
(5.46)
= (m2 + 1)X2 + (−m1 −1
2 + (q
2 −1)θ1)(−X1) + (p + m3 + 3
2 −(2p + 1)θ3)X3
By Lemma 5.5, if
m2 + 1 > 0, (q
2 −1)θ1 > −m2 + m1 −1
2
(5.47)
and
(2p + 1)θ3 −(q
2 −1)θ1 < p + m2 + m3 −m1 + 2
(5.48)
then we have F(X1, X2, X3) →+∞as X2
1 + X2
2 + X2
3 →+∞.
I-F: −X1 ≥X2 ≥X3 ≥0,
F(X1, X2, X3; m1, m2, m3)
(5.49)
= (−m1 −1 + θ2 + q
2θ1)(−X1) + (m2 + 3
2 −θ2 −θ1)X2 + (p + m3 + 3
2 −(2p + 1)θ3)X3
By Lemma 5.5, if
θ2 + q
2θ1 > m1 + 1, (q
2 −1)θ1 > −m2 + m1 −1
2
(5.50)
ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III
29
and
(2p + 1)θ3 −(q
2 −1)θ1 < p + m2 + m3 −m1 + 2
(5.51)
then we have F(X1, X2, X3) →+∞as X2
1 + X2
2 + X2
3 →+∞.
Hence from the above 6 cases I-A,B,C,D, E and F, we obtain 8 inequalities:
m1 + 1 > 0,
(5.52)
(2p + 1)θ3 < p + m2 + m3 + 5
2
(2p + 1)θ3 + (q
2 −1)θ1 < p + m2 + m3 + m1 + 3
(q
2 −1)θ1 < m2 + m1 + 3
2
θ2 −q
2θ1 > −m1
(2p + 1)θ1 −(q
2 −1)θ2 < p + m1 + m3 −m1 + 2
(q
2 −1)θ1 > −m2 + m1 −1
2
θ2 + q
2θ1 > m1 + 1
Similarly, by considering the other 7 cases II:Y ≥X ≥0, III: Y ≥−X ≥0, IV:
−X ≥Y ≥0, V: −X ≥−Y ≥0, VI: −Y ≥−X ≥0, VII:−Y ≥X ≥0, and VIII:
X ≥−Y ≥0, we finally obtain the 26 inequalities in Proposition 5.6.
From the inequalities (1) and (5), we have
−1 < m2 < θ2 −1
2 < 1
2
(5.53)
since θ2 < 1. Hence for any (θ1, θ2, θ3) ∈D0, when m2 < −1 or m2 ≥1, F(X1, X2, X3; m1, m2, m3)
goes to −∞in some direction of X2
1 + X2
2 + X2
3 →+∞.
In conclusion, when m2̸ = 0, the Fourier coefficients ˆhN(m1, m2, m3) can be neglected.
In the following, we consider the Fourier coefficient ˆhN(m1, m2, m3) with m2 = 0.
