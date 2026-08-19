---
doc_id: arxiv-2410.14661v1
doc_title: "(r is odd). Contents 1. Introduction 2 2. Preliminaries 4 2.1. Defintion of the Reshetikhin-Turaev invariants 4 2.2. Dilogarithm and Lobachevsky functions 6 2.3. Quantum dilogrithm"
section_id: sec-009-51-preparations
section_title: "Preparations"
section_number: 5.1
pages: 20-41
source_pdf: 2410.14661v1.pdf
source_sha256: 3362fcd5e28eb1f0
doc_brief: "ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III: THE RESHETIKHIN-TURAEV INVARIANTS OF CLOSED HYPERBOLIC 3-MANIFOLDS OBTAINED BY DOING INTEGRAL SURGERY ALONG THE TWIST KNOT — This is the"
---
ˆVN(θ1,θ 2,θ 3) (5.1)
=π
√
−1
q
2− 1

θ2
1−θ1 + (2p + 1)θ2
3− (2p + 3)θ3− 2θ2 + 3
2q− 1
12
+ 2θ2
N + 1
2
+ p− 2q + 7
4
N + 1
2
− 3(p +q) + 2
6(N + 1
2)2

+ 1
N + 1
2

φN(θ2 +θ3 +
1
2
N + 1
2
− 1) +φN(θ2−θ3 +
1
2
N + 1
2
)
−φN(θ2 +θ1)−φN(θ2)−φN(θ2−θ1))
and
ˆV (θ1,θ 2,θ 3) =π
√
−1
3q
2 + (q
2− 1)θ2
1−θ1 + (2p + 1)θ2
3− (2p + 3)θ3− 2θ2

(5.2)
+ 1
2π√−1
π2
6 + Li2(e2π√−1(θ2+θ3)) + Li2(e2π√−1(θ2−θ3)))
−Li2(e2π√−1(θ2+θ1)− Li2(e2π√−1θ2)− Li2(e2π√−1(θ2−θ1))

.
Proposition 5.1. For any L> 0, in the region
{(θ1,θ 2,θ 3)∈ C3|(Re(θ1), Re(θ2), Re(θ3))∈D0,|Im(θ1)|<L,|Imθ2|<L,|Imθ3|<L},
(5.3)
ON THE ASYMPTOTIC EXPANSION OF V ARIOUS QUANTUM INV ARIANTS III 21
we have
ˆVN(θ1,θ 2,θ 3) = ˆV (θ1,θ 2,θ 3) + 1
N + 1
2

π
√
−1

2θ2 + (p− 2q + 7
4)

(5.4)
−1
2 log(1−e2π√−1(θ2+θ3))− 1
2 log(1−e2π√−1(θ2−θ3))

+ 1
(N + 1
2)2wN(θ1,θ 2,θ 3),
with|wN(θ1,θ 2,θ 3)| bounded from above by a constant independent of N.
Proof. By using Taylor expansion, together with Lemma 2.6, we have
φN

θ2 +θ3− 1 + 1
N + 1
2

(5.5)
=φN(θ2 +θ3− 1) +φ′
N(θ2 +θ3− 1) 1
N + 1
2
+ φ′′
N(θ2 +θ3− 1)
2
1
(N + 1
2)2 +O
 1
(N + 1
2)2

= N + 1
2
2π√−1Li2(e2π√−1(θ2+θ3))− π√−1
6(2N + 1)
e2π√−1(θ2+θ3)
1−e2π√−1(θ2+θ3)
− 1
2 log(1−e2π√−1(θ2+θ3)) + π√−1
2(2N + 1)
e2π√−1(θ2+θ3)
1−e2π√−1(θ2+θ3) +O
 1
(N + 1
2)2

.
ExpandingφN

θ2−θ3 + 1
N + 1
2

,φN(θ2 +θ1),φN(θ2) andφN(θ2−θ1) similarly, we obtain
1
N + 1
2

φN(θ2 +θ3 +
1
2
N + 1
2
− 1) +φN(θ2−θ3 +
1
2
N + 1
2
) (5.6)
−φN(θ2 +θ1)−φN(θ2)−φN(θ2−θ1))
= 1
2π√−1

Li2(e2π√−1(θ2+θ3)) + Li2(e2π√−1(θ2−θ3))− Li2(e2π√−1(θ2+θ1))
−Li2(e2π√−1θ2)− Li2(e2π√−1(θ2−θ1))

− 1
2 log(1−e2π√−1(θ2+θ3))
− 1
2 log(1−e2π√−1(θ2−θ3)) +w′
N(θ1,θ 2,θ 3),
where
w′
N(θ1,θ 2,θ 3) (5.7)
= π√−1
12
 
2 e2π√−1(θ2+θ3)
1−e2π√−1(θ2+θ3) + 2 e2π√−1(θ2−θ3)
1−e2π√−1(θ2−θ3) + e2π√−1(θ2+θ1)
1−e2π√−1(θ2+θ1)
+ e2π√−1(θ2+θ1)
1−e2π√−1(θ2+θ1) + e2π√−1θ2
1−e2π√−1θ2
+O
 1
N + 1
2
!
.
Let
wN(θ1,θ 2,θ 3) =w′
N(θ1,θ 2,θ 3)− 3(p +q) + 2
6 ,(5.8)
22 QINGTAO CHEN AND SHENGMAO ZHU
then we obtain the formula (5.4). □
We consider the critical point of ˆV (θ1,θ 2,θ 3) which is given by the solution of the
following equations
ˆVθ1 =π
√
−1((q− 2)θ1 + 1) + log(1−e2π√−1(θ2+θ1))− log(1−e2π√−1(θ2−θ1)) = 0,(5.9)
ˆVθ2 =−2π
√
−1− log(1−e2π√−1(θ2+θ3))− log(1−e2π√−1(θ2−θ3)) (5.10)
+ log(1−e2π√−1(θ2+θ1)) + log(1−e2π√−1θ2) + log(1−e2π√−1(θ2−θ1)) = 0,
ˆVθ3 =π
√
−1((4p + 2)θ3− (2p + 3))− log(1−e2π√−1(θ2+θ3)) (5.11)
+ log(1−e2π√−1(θ2−θ3)) = 0.
Proposition 5.2. The critical point equations (5.9), (5.10) and (5.11) has a unique
solution (θ0
1,θ 0
2,θ 0
3) in the region D0C ={(θ1,θ 2,θ 3)∈ C3|(Re(θ1), Re(θ2), Re(θ3))∈D0}.
Proof. See Appendix 6.3 for a proof. □
Now we set ζ(p,q ) to be the critical value of the potential function ˆV (p,q ;θ1,θ 2,θ 3),
i.e.
ζ(p,q ) =V (p,q,θ 0
1,θ 0
2,θ 0
3),(5.12)
and set
ζR(p,q ) = Reζ(p,q ) = Re ˆV (p,q,θ 0
1,θ 0
2,θ 0
3).(5.13)
Lemma 5.3. When (p,q )∈S, we have the following estimation for ζR(p,q )
2πζR(p,q )≥ 3.56337.(5.14)
Proof. See Appendix 6.1 for a proof. □
Set z1 = e2π√−1θ1,z 2 = e2π√−1θ2, and z3 = e2π√−1θ3, by straightforward computations,
we have
ˆVθ1θ1 = (q− 2)π
√
−1− 2π√−1e2π√−1(θ2+θ1)
1−e2π√−1(θ2+θ1) − 2π√−1e2π√−1(θ2−θ1)
1−e2π√−1(θ2−θ1)(5.15)
= 2π
√
−1
q
2− 1− 1
z1/z2− 1− 1
1/(z1z2)− 1

ˆVθ1θ2 =−2π√−1e2π√−1(θ2+θ1)
1−e2π√−1(θ2+θ1) + 2π√−1e2π√−1(θ2−θ1)
1−e2π√−1(θ2−θ1)(5.16)
= 2π
√
−1
 1
z1/z2− 1− 1
1/(z1z2)− 1

,
ˆVθ1θ3 = 0.(5.17)
ON THE ASYMPTOTIC EXPANSION OF V ARIOUS QUANTUM INV ARIANTS III 23
ˆVθ2θ2 = 2π√−1e2π√−1(θ2+θ3)
1−e2π√−1(θ2+θ3) + 2π√−1e2π√−1(θ2−θ3)
1−e2π√−1(θ2−θ3) − 2π√−1e2π√−1(θ2+θ1)
1−e2π√−1(θ2+θ1)(5.18)
− 2π√−1e2π√−1θ2
1−e2π√−1θ2
− 2π√−1e2π√−1(θ2−θ1)
1−e2π√−1(θ2−θ1)
= 2π
√
−1

− 1
z1/z2− 1− 1
1/z2− 1− 1
1/(z1z2)− 1
+ 1
1/(z2z3)− 1 + 1
z3/z2− 1

.
ˆVθ2θ3 = 2π√−1e2π√−1(θ2+θ3)
1−e2π√−1(θ2+θ3) − 2π√−1e2π√−1(θ2−θ3)
1−e2π√−1(θ2−θ3)(5.19)
= 2π
√
−1
 1
1/(z2z3)− 1− 1
z3/z2− 1

.
ˆVθ3θ3 =π
√
−1(4p + 2) + 2π√−1e2π√−1(θ2+θ3)
1−e2π√−1(θ2+θ3) + 2π√−1e2π√−1(θ2−θ3)
1−e2π√−1(θ2−θ3)(5.20)
= 2π
√
−1

(2p + 1) + 1
1/(z2z3)− 1 + 1
z3/z2− 1

.
We let
ˆf(θ1,X 1,θ 2,X 2,θ 3,X 3) = Re ˆV (p,q,θ 1 +
√
−1X1,θ 2 +
√
−1X2,θ 3 +
√
−1X3),(5.21)
then for i∈{ 1, 2, 3},
ˆfXi = Re(
√
−1 ˆV (p,q,θ 1 +
√
−1X1,θ 2 +
√
−1Xi,θ 3 +
√
−1X3) (5.22)
=−Im ˆVθi(p,q,θ 1 +
√
−1X1,θ 2 +
√
−1X2,θ 3 +
√
−1X3)
and
ˆfXiXi =−Im
√
−1 ˆVθiθi(p,q,θ 1 +
√
−1X,θ 2 +
√
−1X2,θ 3 +
√
−1X3)

.(5.23)
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
(5.24)
= 2πIm


a +c −a +c 0
−a +c a +b +c +d +e d−e
0 d−e d +e


24 QINGTAO CHEN AND SHENGMAO ZHU
where
a =−Im 1
1−z2/z1
=− sin(2π(θ2−θ1))
e2π(X2−X1) +e−2π(X2−X1)− 2 cos(2π(θ2−θ1))(5.25)
b =−Im 1
1−z2
=− sin(2πθ2)
e2πX2 +e−2πX2− 2 cos(2πθ2)
c =−Im 1
1−z1z2
=− sin(2π(θ2 +θ1))
e2π(X2+X1) +e−2π(X2+X1)− 2 cos(2π(θ2 +θ1))
d = Im 1
1−z2z3
= sin(2π(θ2 +θ3))
e2π(X2+X3) +e−2π(X2+X3)− 2 cos(2π(θ2 +θ3))
e = Im 1
1−z2/z3
= sin(2π(θ2−θ3))
e2π(X2−X3) +e−2π(X2−X3)− 2 cos(2π(θ2−θ3)).
Obviously, when 1
2 < θ2−θ1,θ 2,θ 2 +θ1 < 1, 1 < θ2 +θ3 < 3
2 and 0 < θ2−θ3 < 1
2, we
have that a,b,c,d,e> 0.
Set
DH ={(θ1,θ 2,θ 3)∈D0|1
2 <θ 2±θ1,θ 2 < 1, 1<θ 2 +θ3 < 3
2, 0<θ 2−θ3 < 1
2}.(5.26)
We obtain
Proposition 5.4. For (θ1,θ 2,θ 3)∈DH, the Hessian matrix
Hess( ˆf) (5.27)
is positive definite.
Proof. Since

a +c −a +c 0
−a +c a +b +c +d +e d−e
0 d−e d +e

(5.28)
=abd +abe + 4acd + 4ace + 4ade +cbd +cbe + 4cde> 0,

a +c −a +c
−a +c a +b +c +d +e

(5.29)
=ab + 4ac +ad +ae +cb +cd +ce> 0
and a +c> 0 by a,b,c,d,e> 0 when (θ1,θ 2,θ 3)∈DH. □
5.2. The casem2̸= 0. We say that a Fourier coefficientˆhN(m1,m 2,m 3) can be neglected
if exists some ϵ> 0, such that
ˆhN(m1,m 2,m 3) =O(e(N + 1
2 )(ζR(p,q)−ϵ)).(5.30)
ON THE ASYMPTOTIC EXPANSION OF V ARIOUS QUANTUM INV ARIANTS III 25
We introduce
ˆV (θ1,θ 2,θ 3,m 1,m 2,m 3) = ˆV (θ1,θ 2,θ 3)− 2π
√
−1
3X
i=1
miθi
(5.31)
=π
√
−1
3q
2 +
q
2− 1

θ2
1− (2m1 + 1)θ1 + 2(m2 + 1)θ2 + (2p + 1)θ2
3− (2p + 3 + 2m3)θ3

+ 1
2π√−1
π2
6 + Li2(e2π√−1(θ2+θ3)) + Li2(e2π√−1(θ2−θ3))− Li2(e2π√−1(θ2+θ1))
−Li2(e2π√−1θ2)− Li2(e2π√−1(θ2−θ1))

.
First, when m2 =−1, it is easy to see that
lim
X2→+∞
Re ˆV (θ1 +
√
−1X1,θ 2 +
√
−1X2,θ 3 +
√
−1X3;m1,m 2,m 3)|X3=X1=0(5.32)
= lim
X2→+∞
Re
 1
2π√−1

Li2(e2π√−1(θ2+θ3+√−1X2)) + Li2(e2π√−1(θ2−θ3+√−1X2))
−Li2(e2π√−1(θ2−θ1+√−1X2))− Li2(e2π√−1(θ2+√−1X2))− Li2(e2π√−1(θ2+θ1+√−1X2))

= 0.
It follows that the term ˆhN(m1,−1,m 3) can be neglected for any m1,m 3∈ Z.
Next, we consider the case m2̸=−1. Motivated by Lemma 2.4, for ( θ1,θ 2,θ 3)∈ D0,
we introduce the following function
(5.33) F (X1,X 2,X 3;m1,m 2,m 3) =



0 (if X2 +X3≥ 0)

θ2 +θ3− 3
2

(X2 +X3) (if X2 +X3 < 0)
+



0 (if X2−X3≥ 0)

θ2−θ3− 1
2

(X2−X3) (if X2−X3 < 0)
−



0 (if X2≥ 0)

θ2− 1
2

X2 (if X2 < 0)
−



0 (if X2 +X1≥ 0)

θ2 +θ1− 1
2

(X2 +X1) (if X2 +X1 < 0)
−



0 (if X2−X1≥ 0)

θ2−θ1− 1
2

(X2−X1) (if X2−X1 < 0)
+

−
q
2− 1

θ1 +m1 + 1
2

X1 + (m2 + 1)X2 +

p + 3
2 +m3− (2p + 1)θ3

X3
26 QINGTAO CHEN AND SHENGMAO ZHU
where we useθ2 +θ3− 3
2 instead ofθ2 +θ3− 1
2 in the first summation since in our situation
1<θ 2 +θ3 < 2.
The following simple observation is useful.
Lemma 5.5. Given a linear function on F (X1,X 2,X 3) = AX1 +BX2 +CX 3 over R3
with X1≥X2≥X3≥ 0, we have
(1) If A < 0 or A +B < 0 or A +B +C < 0, then we can find a direction with
X 2
1 +X 2
2 +X 2
3→∞ , such that F (X1,X 2,X 3)→−∞ ;
(2) If A> 0 and A +B >0 and A +B +C >0, then we have F (X1,X 2,X 3)→ +∞
as X 2
1 +X 2
2 +X 2
3→ +∞.
Then we have
Proposition 5.6. If (θ1,θ 2,θ 3)∈D0 satisfies the following 26 inequalities:
(1) :m2 + 1> 0
(2) : (2p + 1)θ3 <p +m2 +m3 + 5
2
(3) : 2pθ3 +θ2 <p +m3 + 2
(4) : (2p− 1)θ3−θ2 <p −m2 +m3
(5) :θ2 >m 2 + 1
2
(6) : (2p− 1)θ3 +θ2 >p +m2 +m3 + 1
(7) : 2pθ3−θ2 >p +m3
(8) : (2p + 1)θ3 >p −m2 +m3 + 1
2
(9) : (2p + 1)θ3 + (q
2− 1)θ1 <p +m2 +m3 +m1 + 3
(10) : (q
2− 1)θ1 <m 2 +m1 + 3
2
(11) :θ2− q
2θ1 >−m1
(12) : (2p + 1)θ3− (q
2− 1)θ1 <p +m2 +m3−m1 + 2
(13) : (q
2− 1)θ1 >−m2 +m1− 1
2
(14) :θ2 + q
2θ1 >m 1 + 1
(15) : 2pθ3 + q
2θ1 <p +m3 +m1 + 2
(16) : 2pθ3− q
2θ1 <p +m3−m1 + 1
(17) : (2p− 1)θ3−θ2 + (q
2 + 1)θ1 <p −m2 +m3 +m1 + 1
2
(18) : (2p− 1)θ3−θ2− (q
2 + 1)θ1 <p −m2 +m2−m1− 1
2
ON THE ASYMPTOTIC EXPANSION OF V ARIOUS QUANTUM INV ARIANTS III 27
(19) :θ2− (q
2 + 1)θ1 >m 2−m1
(20) :θ2 + (q
2 + 1)θ1 >m 2 +m1 + 1
(21) : (2p− 1)θ3 +θ2− (q
2 + 1)θ1 >p +m2 +m3−m1 + 1
2
(22) : (2p− 1)θ3 +θ2 + (q
2 + 1)θ1 >p +m2 +m3 +m1 + 3
2
(23) : 2pθ3− q
2θ1 >p +m3−m1
(24) : 2pθ3 + q
2θ1 >p +m3 +m1 + 1
(25) : (2p + 1)θ3− (q
2− 1)θ1 >p −m1 +m3−m1
(26) : (2p + 1)θ3 + (q
2− 1)θ1 >p −m2 +m3 +m1 + 1
then we have F (X1,X 2,X 3,m 1,m 2,m 3)→ +∞ as X 2
1 +X 2
2 +X 2
3→ +∞.
We prove the proposition by subdividing (X1,X 2,X 3)∈ R3 into 48 regions.
Case I: X2≥X3≥ 0,
I-A: X2≥X3≥X1≥ 0, then
F (X1,X 2,X 3;m1,m 2,m 3) (5.34)
= (m2 + 1)X2 + (p +m3 + 3
2− (2p + 1)θ3)X3 + (m1 + 1
2− (q
2− 1)θ1)X1
By Lemma 5.5, if
m1 + 1> 0, (2p + 1)θ3 <p +m2 +m3 + 5
2,(5.35)
and
(2p + 1)θ3 + (q
2− 1)θ1 <p +m2 +m3 +m1 + 3 (5.36)
then we have F (X1,X 2,X 3)→ +∞ as X 2
1 +X 2
2 +X 2
3→ +∞.
I-B: X2≥X1≥X3≥ 0,
F (X1,X 2,X 3;m1,m 2,m 3) (5.37)
= (m2 + 1)X2 + (m1 + 1
2− (q
2− 1)θ1)X1 + (p +m3 + 3
2− (2p + 1)θ3)X3
By Lemma 5.5, if
m2 + 1> 0, (q
2− 1)θ1 <m 2 +m1 + 3
2(5.38)
and
(2p + 1)θ3 + (q
2− 1)θ1 <p +m2 +m3 +m1 + 3 (5.39)
then we have F (X1,X 2,X 3)→ +∞ as X 2
1 +X 2
2 +X 2
3→ +∞.
28 QINGTAO CHEN AND SHENGMAO ZHU
I-C: X2≥X1≥X3≥ 0,
F (X1,X 2,X 3;m1,m 2,m 3) (5.40)
= (m1 +θ2− q
2θ1)X1 + (m2 + 3
2−θ2 +θ1)X2 + (p +m3 + 3
2− (2p + 1)θ3)X3
By Lemma 5.5, if
m1 +θ2− q
2θ1 > 0, (q
2− 1)θ1 <m 2 +m1 + 3
2(5.41)
and
(2p + 1)θ3 + (q
2− 1)θ1 <p +m2 +m3 +m1 + 3 (5.42)
then we have F (X1,X 2,X 3)→ +∞ as X 2
1 +X 2
2 +X 2
3→ +∞.
I-D: X2≥X3≥−X1≥ 0,
F (X1,X 2,X 3;m1,m 2,m 3) (5.43)
= (m2 + 1)X2 + (p +m3 + 3
2− (2p + 1)θ3)X3 + (−m1− 1
2 + (q
2− 1)θ1)(−X1)
By Lemma 5.5, if
m2 + 1> 0, (2p + 1)θ3 <p +m2 +m3 + 5
2(5.44)
and
(2p + 1)θ3− (q
2− 1)θ1 <p +m2 +m3−m1 + 2 (5.45)
then we have F (X1,X 2,X 3)→ +∞ as X 2
1 +X 2
2 +X 2
3→ +∞.
I-E: X2≥−X1≥X3≥ 0,
F (X1,X 2,X 3;m1,m 2,m 3) (5.46)
= (m2 + 1)X2 + (−m1− 1
2 + (q
2− 1)θ1)(−X1) + (p +m3 + 3
2− (2p + 1)θ3)X3
By Lemma 5.5, if
m2 + 1> 0, (q
2− 1)θ1 >−m2 +m1− 1
2(5.47)
and
(2p + 1)θ3− (q
2− 1)θ1 <p +m2 +m3−m1 + 2 (5.48)
then we have F (X1,X 2,X 3)→ +∞ as X 2
1 +X 2
2 +X 2
3→ +∞.
I-F:−X1≥X2≥X3≥ 0,
F (X1,X 2,X 3;m1,m 2,m 3)
(5.49)
= (−m1− 1 +θ2 + q
2θ1)(−X1) + (m2 + 3
2−θ2−θ1)X2 + (p +m3 + 3
2− (2p + 1)θ3)X3
By Lemma 5.5, if
θ2 + q
2θ1 >m 1 + 1, (q
2− 1)θ1 >−m2 +m1− 1
2(5.50)
ON THE ASYMPTOTIC EXPANSION OF V ARIOUS QUANTUM INV ARIANTS III 29
and
(2p + 1)θ3− (q
2− 1)θ1 <p +m2 +m3−m1 + 2 (5.51)
then we have F (X1,X 2,X 3)→ +∞ as X 2
1 +X 2
2 +X 2
3→ +∞.
Hence from the above 6 cases I-A,B,C,D, E and F, we obtain 8 inequalities:
m1 + 1> 0,(5.52)
(2p + 1)θ3 <p +m2 +m3 + 5
2
(2p + 1)θ3 + (q
2− 1)θ1 <p +m2 +m3 +m1 + 3
(q
2− 1)θ1 <m 2 +m1 + 3
2
θ2− q
2θ1 >−m1
(2p + 1)θ1− (q
2− 1)θ2 <p +m1 +m3−m1 + 2
(q
2− 1)θ1 >−m2 +m1− 1
2
θ2 + q
2θ1 >m 1 + 1
Similarly, by considering the other 7 cases II: Y ≥ X ≥ 0, III: Y ≥ −X ≥ 0, IV:
−X≥ Y ≥ 0, V: −X≥− Y ≥ 0, VI: −Y ≥− X≥ 0, VII:−Y ≥ X≥ 0, and VIII:
X≥−Y≥ 0, we finally obtain the 26 inequalities in Proposition 5.6.
From the inequalities (1) and (5), we have
−1<m 2 <θ 2− 1
2 < 1
2(5.53)
sinceθ2 < 1. Hence for any (θ1,θ 2,θ 3)∈D0, whenm2 <−1 orm2≥ 1,F (X1,X 2,X 3;m1,m 2,m 3)
goes to−∞ in some direction of X 2
1 +X 2
2 +X 2
3→ +∞.
In conclusion, when m2̸= 0, the Fourier coefficients ˆhN(m1,m 2,m 3) can be neglected.
In the following, we consider the Fourier coefficient ˆhN(m1,m 2,m 3) with m2 = 0.
5.3. The case m2 = 0 but (m1,m 3)̸= (0, 0).
Theorem 5.7. When m1 = 0 and m3≥ 1, then
ˆhN(0, 0,m 3) (5.54)
can be neglected.
30 QINGTAO CHEN AND SHENGMAO ZHU
Proof. Forc3≥ 1
2 + 7
8p, then ˜c3≥ 7
8p, by Lemmas 6.6 and 6.7, we have
2πRe ˆV (p,q ;θ1,θ 2,c 3 = 1
2 + ˜c3; 0, 0,m 3) (5.55)
≤ 2πRe ˆV

p,q,θ 1
1
2

,θ 2
1
2

, 1
2

−π2˜c2
3
≤ 2πRe ˆV

p,q,θ 1
1
2

,θ 2
1
2

, 1
2

−π2 49
64
1
p2
<Vol (Mp,q).
Then the integral over the region{(θ1,θ 2,θ 3)∈D0|θ3≤ 1
2 + 7
8p} can be neglected by using
Theorem 6.11.
Moreover, when m3≥ 1, from the inequalities (6) and (7), we obtain
(4p− 1)θ3 > 2p + 2m3 + 1 (5.56)
Hence
θ3 > 1
2 + 4m3 + 3
2(4p− 1) > 1
2 + 7
8p.(5.57)
Therefore, over the region {(θ1,θ 2,θ 3)∈ D0|θ3≤ 1
2 + 7
8p}, we can find a direction of
X 2
1 +X 2
2 +X 2
3→ +∞ such that
Re ˆV (p,q ; 0, 0,m 3,θ 1,θ 2,θ 3)→−∞.(5.58)
It follows that the integral over this region can be neglected. Therefore, the whole integral
can be neglected. □
Theorem 5.8. When m1≥ 1 and m3 = 0, then
ˆhN(m1, 0, 0) (5.59)
can be neglected.
Proof. For 2
q≤c1 < 1
4, by Lemmas 6.8 and 6.9, we have
2πRe ˆV (p,q ;c1,θ 2,θ 3;m1, 0, 0)≤Vol
 
S3\Kp

− 3
2π2c2
1(5.60)
≤Vol
 
S3\Kp

− 6π2 1
q2
<Vol (Mp,q).
Then the integral over the region {(θ1,θ 2,θ 3)∈ D0|θ1 > 2
q} can be neglected by using
Theorem 6.12.
Moreover, when m1≥ 1, from the inequalities (14), we obtain
θ1 > 2(2−θ2)
q > 2
q,(5.61)
Therefore, over the region {(θ1,θ 2,θ 3)∈ D0|θ1≤ 2
q}, we can find a direction of X 2
1 +
X 2
2 +X 2
3→ +∞ such that
Re ˆV (p,q ;θ1,θ 2,θ 3;m1, 0, 0)→−∞.(5.62)
ON THE ASYMPTOTIC EXPANSION OF V ARIOUS QUANTUM INV ARIANTS III 31
It follows that the integral over this region can be neglected.
Therefore, the whole integral can be neglected. □
Theorem 5.9. When m1≥ 1 and m3≥ 1, then
ˆhN(m1, 0,m 3) (5.63)
can be neglected.
Proof. First, when m1≥ 1, from the inequalities (14), we obtain
θ1 > 2(2−θ2)
q > 2
q,(5.64)
Therefore, over the region whenθ1 < 2
q, we can find a direction ofX 2
1 +X 2
2 +X 2
3→ +∞
such that
Re ˆV (p,q ;θ1,θ 2,θ 3;m1, 0,m 3)→−∞.(5.65)
It follows that the integral over the region {θ1 < 2
q} can be neglected.
For 2
q≤c1≤ 1
4, on the region D0(c1) ={θ1 =c1}∩ D0, we estimate the integral
Z
D0(c1)
sin(πc1) sin(2πθ3)e(N + 1
2 ) ˆVN (c1,θ2,θ3;m1,0,m3)dθ2dθ3(5.66)
as follows.
Forθ3 < 1
2 + 7
8p, thenθ3 < 1
2 + 7
2(4p−1), in this case, we can find a direction ofX 2
2 +X 2
3→
+∞ such that
Re ˆV (p,q ;c1,θ 2,θ 3;m1, 0,m 3)→−∞.(5.67)
So the integral over θ3 < 1
2 + 7
8p can be neglected.
For θ3≥ 1
2 + 7
8p, we use the one-dimensional saddle point method. Let θ3 = c3, for
c3≥ 1
2 + 7
8p, then by Lemma 6.13 and formula (5.60), we have
2πRe ˆV (p,q ;m1, 0,m 3,c 1,T 2(c1, 1
2 + ˜c3),c 3 = 1
2 + ˜c3) (5.68)
< 2πRe ˆV (p,q ;m1, 0, 0,c 1,θ 2(c1),θ 3(c1))
<Vol (Mp,q).
By using the one-dimensional saddle method, see Appendix 6.6, we can show that integral
over the region θ3≥ 1
2 + 7
8p can also be neglected.
Hence the whole integral can be neglected. □
Therefore,
Proposition 5.10. There exists ϵ> 0, such that
RTr(Mp,q) = 4ˆhN(0, 0, 0) +O(e(N + 1
2 )(ζR(p,q)−ϵ)).(5.69)
Finally, we only need to estimate the integral ˆhN(0, 0, 0).
32 QINGTAO CHEN AND SHENGMAO ZHU
5.4. The contribution of ˆhN(0, 0, 0). We letU′
0 be the region determined by inequalities
illustrated in Proposition 5.6 when m1 = m2 = m3 = 0. Let U0 = U′
0∩ D0, as a
consequence of Proposition 5.6,
Corollary 5.11. For any (θ1,θ 2,θ 3)∈D0,
(i) when (θ1,θ 2,θ 3)∈U0, we have
f(X1,X 2,X 3)→ +∞ as X 2
1 +X 2
2 +X 2
3→ +∞.(5.70)
(ii) when (θ1,θ 2,θ 3) /∈U0,
f(X1,X 2,X 3)→−∞ in some directions of X 2
1 +X 2
2 +X 2
3→ +∞.(5.71)
We introduce the cube MCB as shown in figure 5.4, the integrand is symmetric with
respect to θ3 = 1
2, θ1 = 0 and by Lemma 4.2, we have
.
Figure 5.1. The cube MCB
Z
D0
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3)dθ1dθ2dθ3(5.72)
= 4
Z
MCB
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3)dθ1dθ2dθ3 +O(e
N + 1
2
2π (3.56337−ϵ))
ON THE ASYMPTOTIC EXPANSION OF V ARIOUS QUANTUM INV ARIANTS III 33
So we only need to consider the integral over the cube MCBZ
MCB
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3)dθ1dθ2dθ3.(5.73)
Consider the function
v(θ1,θ 3,θ 3) = Re ˆV (p,q,θ 1,θ 2,θ 3) (5.74)
= Λ(θ2 +θ3) + Λ(θ2−θ3)− Λ(θ2 +θ1)− Λ(θ2)− Λ(θ2−θ1).
we have
dv(θ1,θ 2,θ 3)
dθ1
= Λ′(θ2−θ1)− Λ′(θ2 +θ1) = 2 log| sinπ(θ2 +θ1)|
| sinπ(θ2−θ1)| < 0(5.75)
and
dv(θ1,θ 2,θ 3)
dθ3
= Λ′(θ2 +θ3)− Λ′(θ2−θ3) = 2 log| sinπ(θ2−θ3)|
| sinπ(θ2 +θ3)| < 0(5.76)
for 0 <θ 1 < 1
2, 1
2 <θ 2 < 1 and 1
2 <θ 3 < 1.
Therefore, on the cube CB 1 :I21J2J3I31−E21F2F3E31, for (θ1,θ 2,θ 3)∈CB 1, we have
2πv(θ1,θ 3,θ 3)≤ 2π max
θ2∈( 1
2,1)
v
1
4,θ 2, 3
4

(5.77)
= 2πv
1
4, 5
6, 3
4

=v3 < 3.56337.
On the cube CB 2 :A21B2B3A31−I21J2J3I31, for (θ1,θ 2,θ 3)∈CB 2, we have
2πv(θ1,θ 3,θ 3)≤ 2π max
θ2∈( 1
2,1)
v

0,θ 2, 3
4

(5.78)
= 2πv

0, 5
6, 3
4

= 3.552296< 3.56337.
On the cube CB 3 :I01J0J2I21−E01F0F2E21, for (θ1,θ 2,θ 3)∈CB 3, we have
2πv(θ1,θ 3,θ 3)≤ 2π max
θ2∈( 1
2,1)
v
1
4,θ 2, 1
2

(5.79)
= 2πv
1
4, 0.688635, 1
2

= 3.252728< 3.56337.
Now we consider the cube SPM 1 :A01B0B2A21−I01J0J2I21 as shown in Figure 5.4, it
is obvious that
MCB =SPM 1∪CB 1∪CB 2∪CB 3.(5.80)
By the formulas (5.77), (5.78) and (5.79), we obtain
Z
MCB
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3)(5.81)
=
Z
SPM 1
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3) +O(e
N + 1
2
2π (3.56337−ϵ)).
Now we consider the integral overSPM 1. For the cubeCB 4 :M11N1N2M21−I11J1J2I21.
34 QINGTAO CHEN AND SHENGMAO ZHU
.
Figure 5.2. The cube SPM 1
For any fixed (c1,c 3)∈ M11M21J21I11, i.e. c10≤ c1 < 1
4 and c20≤ c3 < 3
4, the critical
point equation ˆVθ2(p,q,c 1,θ,c 3) = 0 has a unique solution θ2(c1,c 3) with Re(θ2(c1,c 3))∈
( 1
2, 1), see Appendix 6.6. By Proposition 6.16, we obtain
2πRe ˆV (p,q,c 1,θ 2(c1,c 3),c 3) (5.82)
≤ 2πRe ˆV (p,q,c 10,θ 2(c10,c 30),c 30))
= 2πRe ˆV (p,q, 0.1225320, 0.808058− 0.111315
√
−1, 0.600484))
= 3.25806< 3.56337
By using the one-dimensional saddle point method, see Appendix 6.6 for checking the
condition, we estimate the integral
Z 1
1
2
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (c1,θ2,c3)dθ2 =O(e
N + 1
2
2π (3.56337−ϵ)) (5.83)
ON THE ASYMPTOTIC EXPANSION OF V ARIOUS QUANTUM INV ARIANTS III 35
for some ϵ> 0. Therefore,
Z
CB 4
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3)(5.84)
=
Z
(θ1,θ3)∈M11M21J21I11
 Z 1
1
2
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3)dθ2
!
dθ1dθ3
=O(e
N + 1
2
2π (3.55337−ϵ)).
On the Triangular Prism TPL 1 :A01M03M01−A2M23M21, for (θ1,θ 2,θ 3)∈TPL 1, by
formula (5.76), we have
2π max
(θ1,θ2,θ3)∈TPL 1
v(θ1,θ 2,θ 3) (5.85)
= 2π max
(θ1,θ2)∈A01M03M01
v(θ1,θ 2, 1
2)
= 2π max
0≤c≤c10
v

c,c + 1
2, 1
2

= 2πv

c10,c 10 + 1
2, 1
2

= 3.37448< 3.56337.
Similarly, on the Triangular Prism TPR 1 :B0M06N0−B2M25N2, we have
2π max
(θ1,θ2,θ3)∈TPR 1
v(θ1,θ 2,θ 3) (5.86)
= 2π max
(θ1,θ3)∈B0M05N0
v

θ1,θ 2, 1
2

= 2π max
0≤c≤c10
v(c, 1−c, 1
2)
= 2πv

c10, 1−c10, 1
2

= 2.93274< 3.56337.
On the Triangular Prism TPL 2 :A01A12A11−I01I12I11, we have
2π max
(θ1,θ2,θ3)∈TPL 2
v(θ1,θ 2,θ 3) (5.87)
= 2π max
(θ2,θ3)∈A01A12A11
v(0,θ 2,θ 3)
= 2π max
0≤c≤c30
v(0,c,c )
= 2πv(0,c 30,c 30) = 2.27746< 3.56337.
36 QINGTAO CHEN AND SHENGMAO ZHU
On the Triangular Prism TPR 2 :B0B1A16−J0J1I16, we have
2π max
(θ1,θ2,θ3)∈TPR 2
v(θ1,θ 2,θ 3) (5.88)
= 2π max
(θ2,θ3)∈B0B1A16
v(0,θ 2,θ 3)
= 2π max
0≤c≤c30
v

0, 3
2−c,c

= 2πv

0, 3
2−c30,c 30

= 3.56337.
Note that the intersections ofTPL 1 andTPL 2 is a truncated triangular prism TTPL :
A01Q12A11−M01M12M11, and the intersections of TPR 1 andTPR 2 is a truncated trian-
gular prisim TTPR :B0Q16B1−N01M16N1.
Now, we let SPM 2 =SPM 1−TPL 1−TPR 1− (TPL 2\TTPL )− (TPR 2\TTPR ),
by previous formulas, we have
Z
SPM 1
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3)(5.89)
=
Z
SPM 2
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3) +O(e
N + 1
2
2π (3.55337−ϵ)).
For the Trapezoidal Prism TZP 1 : A11B1M15M13−A21B2M25M23, first, we add two
triangular prismsA11M13M11−A21M23M21 andB1M15N1−B2M25N2 toTZP 1, we obtain
a cube CB 5 :A11B1B2A21−M11N1N2M21,
By formulas (5.85) and (5.86), we obtain that
Z
TZP 1
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3)(5.90)
=
Z
CB5
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3) +O(e
N + 1
2
2π (3.55337−ϵ))
For any fixed (c1,c 3)∈A11A21M21M11, i.e. 0 ≤c1≤c10 and c20≤c3 < 3
4, the critical
point equation ˆVθ2(p,q,c 1,θ,c 3) = 0 has a unique solution θ2(c1,c 3) with Re(θ2(c1,c 3))∈
( 1
2, 1), see Appendix 6.6. By Proposition 6.16 we obtain
2πRe ˆV (p,q,c 1,θ 2(c1,c 3),c 3) (5.91)
≤ 2πRe ˆV (p,q,c 10,θ 2(c10,c 30),c 30))
= 2πRe ˆV (p,q, 0, 0.8270666460− 0.1216893136
√
−1, 0.600484))
= 3.563367< 3.56337.
By using the one-dimensional saddle point method, see Appendix 6.6 for checking the
condition, we estimate the integral
Z 1
1
2
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (c1,θ2,c3)dθ2 =O(e
N + 1
2
2π (3.56337−ϵ)) (5.92)
ON THE ASYMPTOTIC EXPANSION OF V ARIOUS QUANTUM INV ARIANTS III 37
for some ϵ> 0. Therefore,
Z
CB5
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3)(5.93)
=
Z
(θ1,θ3)∈A11A21M21M11
 Z 1
1
2
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3)dθ2
!
dθ1dθ3
=O(e
N + 1
2
2π (3.56337−ϵ)).
For the Trapezoidal Prism TZP 2 : M01N0M16M12−I01J0I16I12, we can estimates its
integral similarly as the computation for TZP 1.
Finally, we obtain a polyhedron SPM 2 =MCB−∪ 6
i=1CBi−∪ 2
i=1TPL i−∪ 2
i=1TPR i.
Then we use the polyhedron SPM 2 to do the reflection along the plane θ3 = 1
2 and
θ1 = 0 to obtain a new polyhedron denoted by P , the key point is that P ⊂ DH. Let
D′′
0 =P∩D0, the above analysis tell us that
Z
D0
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3)dθ1dθ2dθ3(5.94)
=
Z
D′′
0
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3)dθ1dθ2dθ3 +O(e(N + 1
2 )ζR(p,q)−ϵ).
Proposition 5.12. For (p,q ) satisfies the condition (1.3), we have
ˆhN(0, 0, 0) =−κ′′
r
Z
D0
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3)dθ1dθ2dθ3(5.95)
=κ′′
rω(p,q )e(N + 1
2 )ζR(p,q)
·
 
1 +
dX
i=1
κi(p,q )
2π√−1
N + 1
2
i
+O
 1
(N + 1
2)d+1
!
,
for d≥ 1, where ω(p,q ) and κi(p,q ) are constants determined by Mp,q.
Proof. We need to estimate the following integral
Z
D0
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3)dθ1dθ2dθ3.(5.96)
According to formula (5.95), we only need to estimate the integral
Z
D′′
0
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3)dθ1dθ2dθ3.(5.97)
We will verify the conditions of Proposition 2.8 for saddle point method in Proposition
5.13. By Proposition 5.1 and Remark 2.9, we can apply the Proposition 2.8 to the above
integral (5.97). Let (θ0
1,θ 0
2,θ 0
3) be the critical point of ˆV (p,q,θ 1,θ 2,θ 3), we obtain that
38 QINGTAO CHEN AND SHENGMAO ZHU
Z
D′′
0
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3)dθ1dθ2dθ3(5.98)
=
 π
N + 1
2
 3
2 α(θ0
1,θ 0
2,θ 0
3)r
det

− 1
2Hess( ˆV )(θ0
1,θ 0
2,θ 0
3)
e(N + 1
2 )ζ(p,q)
 
1 +
dX
i=1
κi(p,q )
2π√−1
N + 1
2
i
+O
 1
(N + 1
2)d+1
!
where the function
α(θ0
1,θ 0
2,θ 0
3) (5.99)
= sin(πθ0
1) sin(2πθ0
3)eπ√−1(2θ0
2+(p−2q+ 7
4 ))− 1
2 log(1−e2π√−1(θ0
2 +θ0
3 ))− 1
2 log(1−e2π√−1(θ0
2−θ0
3 ))
=
(−1)p− 1
4z0
2(z0
3− 1
z0
3
)(
p
z0
1− 1√
z0
1
)
4
q
(1−z0
2z0
3)(1−z0
2
1
z0
3
)
.
the determinant of the Hessian matrix at ( θ0
1,θ 0
2,θ 0
3) is given by
det

−1
2Hess( ˆV )(θ0
1,θ 0
2,θ 0
3)

= (−1
2)3(2π
√
−1)3H(p,q ;z0
1,z 0
2,z 0
3)(5.100)
where
H(p,q ;z0
1,z 0
2,z 0
3) = 4 z0
2
z0
1−z0
2
· z0
1z0
2
1−z0
1z0
2
 z0
2z0
3
1−z0
2z0
3
+ z0
2
z0
3−z0
2
(5.101)
− 4
 z0
2
z0
1−z0
2
+ z0
1z0
2
1−z0
1z0
2
 z0
2z0
3
1−z0
2z0
3
· z0
2
z0
3−z0
2
+
 z0
2
z0
1−z0
2
+ z0
1z0
2
1−z0
1z0
2
 z0
2
1−z0
2
 z0
2z0
3
1−z0
2z0
3
+ z0
2
z0
3−z0
2

+ (8p + 4) z0
2
z0
1−z0
2
· z0
1z0
2
1−z0
1z0
2
+ (2p + 1)
 z0
2
z0
1−z0
2
+ z0
1z0
2
1−z0
1z0
2
 z0
2
1−z0
2
− (2p + q
2)
 z0
2
z0
1−z0
2
+ z0
1z0
2
1−z0
1z0
2
 z0
2z0
3
1−z0
2z0
3
+ z0
2
z0
3−z0
2

− (q
2− 1) z0
2
1−z0
2
 z0
2z0
3
1−z0
2z0
3
+ z0
2
z0
3−z0
2

+ 4(q
2− 1) z0
2z0
3
1−z0
2z0
3
· z0
2
z0
3−z0
2
− (2p + 1)(q
2− 1)
 z0
2
z0
1−z0
2
+ z0
1z0
2
1−z0
1z0
2
+ z0
2
1−z0
2
− z0
2z0
3
1−z0
2z0
3
− z0
2
z0
3−z0
2

.
Therefore, we have
ON THE ASYMPTOTIC EXPANSION OF V ARIOUS QUANTUM INV ARIANTS III 39
Z
D′′
0
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3)dθ1dθ2dθ3(5.102)
=
(−1)p√−1z2(z3−z−1
3 )(√z1− 1√z1
)
4(N + 1
2)
3
2
p
(1−z2z3)(1−z2z−1
3 )
p
H(p,q ;z0
1,z 0
2,z 0
3)
e(N + 1
2 )ζ(p,q)
·
 
1 +
dX
i=1
κi(p,q )
2π√−1
N + 1
2
i
+O
 1
(N + 1
2)d+1
!
.
Hence
ˆhN(0, 0, 0) =−κ′′
r
Z
D0
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3)dθ1dθ2dθ3(5.103)
= (−1)p+1
√−1
4 eσ((Kp)q)( 3
2N +1 +N +1
2 )π√−1ω(p,q )e(N + 1
2 )ζ(p,q)
·
 
1 +
dX
i=1
κi(p,q )
2π√−1
N + 1
2
i
+O
 1
(N + 1
2)d+1
!
where
ω(p,q ) =
z0
2(z0
3− (z0
3)−1)(
p
z0
1− 1√
z0
1
)
p
(1−z0
2z0
3)(1−z0
2(z0
3)−1)
p
H(p,q ;z0
1,z 0
2,z 0
3)
.(5.104)
□
Proposition 5.13. When we apply Proposition 2.8 (saddle point method) to the integral
(5.97), the assumptions of Proposition 2.8 holds.
Proof. We note that, by Lemma 2.7,ˆVN(p,q ;θ1,θ 2,θ 3) uniformly converges to theˆV (p,q ;θ1,θ 2,θ 3)
on D′′
0 as N→∞ . Hence, we only need to verify the assumptions of the saddle point
method for ˆV (p,q ;θ1,θ 2,θ 3). We show that there exists a homotopy D′′
δ (0≤ δ≤ 1)
betweenD′′
0 and D′′
1 such that
(θ0
1,θ 0
2,θ 0
3)∈D′′
1,(5.105)
D′′
1−{ (θ0
1,θ 0
2,θ 0
3)}⊂{ (θ1,θ 2,θ 3)∈ C3|ReV (p,q ;θ1,θ 2,θ 3)<ζ R(p,q )},(5.106) Z
∂D′′
δ
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3)dθ1dθ2dθ3 =O

e(N + 1
2 )(ζR(p,q)−ϵ)

.(5.107)
In the fiber of the projection C3→ R3 at (θ1R,θ 2R,θ 3R)∈ D′′
0, we consider the flow
from (X1,X 2,X 3) = (0, 0, 0) determined by the vector field (− ∂ ˆf
∂X1
,− ∂ ˆf
∂X2
,− ∂ ˆf
∂X3
). By the
construction of the region D′′
0⊂ DH, together with Corollary 5.11 and Proposition 5.4,
the convex neighborhood U0 of (θ0
1R,θ 0
2R,θ 0
3R) satisfies the following holds.
(1) If (θ1R,θ 2R,θ 3R)∈U0, then ˆf has a unique minimal point, and the flow goes there.
(2) If (θ1R,θ 2R,θ 3R)∈D′′
0\U0, then the flow goes to infinity.
We put g(θ1R,θ 2R,θ 3R) = ( g1(θ1R,θ 2R,θ 3R),g 2(θ1R,θ 2R,θ 3R),g 2(θ1R,θ 2R,θ 3R) to be the
minimal point of (1). In particular, |g(θ1R,θ 2R,θ 3R)|→∞ as (θ1R,θ 2R,θ 3R) goes to ∂U0.
Further, for a sufficiently large R >0, we stop the flow when |g(θ1R,θ 2R,θ 3R)| =R. We
40 QINGTAO CHEN AND SHENGMAO ZHU
construct the revised flowˆg(θ1R,θ 2R,θ 3R), by putting ˆg(θ1R,θ 2R,θ 3R) = g(θ1R,θ 2R,θ 3R) for
(θ1R,θ 2R,θ 3R)∈U0 with|g(θ1R,θ 2R,θ 3R)|< R, otherwise, by putting |ˆg(θ1R,θ 2R,θ 3R)| =
(R,R,R ).
We define the ending of the homotopy by
D′′
1 ={(θ1R,θ 2R,θ 3R) + ˆg(θ1R,θ 2R,θ 3R)
√
−1|(θ1R,θ 2R,θ 3R)∈D′′
0}.(5.108)
Further, we define the internal part of the homotopy by setting it along the flow from
(θ1R,θ 2R,θ 3R) determined by the vector field

− ∂ ˆf
∂X1
,− ∂ ˆf
∂X2
,− ∂ ˆf
∂X3

.
We show (5.105) and (5.106) as follows. We consider the function
h(θ1R,θ 2R,θ 3R) = ReV (θ1R +
√
−1ˆg1,θ 2R +
√
−1ˆg2,θ 3R +
√
−1ˆg3).(5.109)
If (θ1R,θ 2R,θ 3R) /∈U0, by (2),−h(θ1R,θ 2R,θ 3R) is sufficiently large (because we let R be
sufficiently large), hence (5.106) holds in this case. Otherwise, (θ1R,θ 2R,θ 3R)∈U0, in this
case, ˆg(θ1R,θ 2R,θ 3R) = g(θ1R,θ 2R,θ 3R). It is shown from the definition of ˆg(θ1R,θ 2R,θ 3R)
that
∂Re ˆV
∂X1
= ∂Re ˆV
∂X2
= ∂Re ˆV
∂X3
= 0 at (X1,X 2,X 3) = g(θ1R,θ 2R,θ 3R),(5.110)
which implies
Im∂ ˆV
∂θ1
= Im∂ ˆV
∂θ2
= Im∂ ˆV
∂θ3
= 0 at (θ1R,θ 2R,θ 3R) + g(θ1R,θ 2R,θ 3R)
√
−1.(5.111)
On the other hand, for i = 1, 2, 3,
∂h
∂θiR
= Re∂ ˆV
∂θi
, at (θ1R,θ 2R,θ 3R) + g(θ1R,θ 2R,θ 3R)
√
−1.(5.112)
Therefore, when (θ1R,θ 2R,θ 3R)+g(θ1R,θ 2R,θ 3R)√−1 is a critical point of ˆV , (θ1R,θ 2R,θ 3R)
is a critical point of h(θ1R,θ 2R,θ 3R). Hence by Proposition 5.2, h(θ1R,θ 2R,θ 3R) has a
unique maximal point at (θ0
1R,θ 0
2R,θ 0
3R) which is equal to ζR(p,q ). Therefore, (5.105) and
(5.106) holds.
We show (5.107) as follows. Note that the boundary of∂D′′
0 consists ofD0(c10),D0(c30)
and the partial boundaries of D0 denoted by D0b. Hence ∂D′′
δ consists of three parts
denoted by
∂D′′
δ =A1∪A2∪B,(5.113)
whereA1 andA2 comes from the flows start at (θ1R,θ 2R,θ 3R)∈D0(c10) and (θ1R,θ 2R,θ 3R)∈
D0(c30) respectively, while B comes from the flows start at (θ1R,θ 2R,θ 3R)∈D0b.
By its definition, D0b⊂ ∂D0⊂{ (θ1,θ 2,θ 3)∈ C3|Re ˆV (p,q ;θ1,θ 2,θ 3) < ζR(p,q )−ϵ},
and the function Re ˆV (p,q ;θ1,θ 2,θ 3) decreases under the flow, so we have
Z
B
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3)dθ1dθ2dθ3 =O

e(N + 1
2 )(ζR(p,q)−ϵ)

.(5.114)
By Theorems 6.11 and 6.12, the integrals on D0(c10) and D0(c30) is also of order
O(e(N + 1
2 )(ζR(p,q)−ϵ)). By applying the saddle point method to the slices of the region
ON THE ASYMPTOTIC EXPANSION OF V ARIOUS QUANTUM INV ARIANTS III 41
A1∪A2 as shown in Appendix 6.5, we can prove that
Z
A1∪A2
sin(πθ1) sin(2πθ3)e(N + 1
2 ) ˆVN (θ1,θ2,θ3)dθ1dθ2dθ3 =O

e(N + 1
2 )(ζR(p,q)−ϵ)

.(5.115)
Combining formulas (5.114) and (5.115) together, we prove (5.107).
By (5.105) (5.106) and (5.107), the required homotopy exists. Hence the assumptions
of Proposition 2.8 holds when we apply the saddle point method to the integral (5.97). □
