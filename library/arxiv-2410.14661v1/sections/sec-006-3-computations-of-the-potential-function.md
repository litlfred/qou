---
doc_id: arxiv-2410.14661v1
doc_title: "(r is odd). Contents 1. Introduction 2 2. Preliminaries 4 2.1. Defintion of the Reshetikhin-Turaev invariants 4 2.2. Dilogarithm and Lobachevsky functions 6 2.3. Quantum dilogrithm"
section_id: sec-006-3-computations-of-the-potential-function
section_title: "Computations of the potential function"
section_number: 3
pages: 8-15
source_pdf: 2410.14661v1.pdf
source_sha256: 3362fcd5e28eb1f0
doc_brief: "ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III: THE RESHETIKHIN-TURAEV INVARIANTS OF CLOSED HYPERBOLIC 3-MANIFOLDS OBTAINED BY DOING INTEGRAL SURGERY ALONG THE TWIST KNOT — This is the"
---
LetMp,q be the 3-manifold obtained by the doingq-surgery along the twist knotKp, (see
Figure 3) where the index p represents 2p crossings (half-twists). For example,K−1 = 41,
K1 = 31,K2 = 52.
ON THE ASYMPTOTIC EXPANSION OF V ARIOUS QUANTUM INV ARIANTS III 9
.
Figure 3.1. Twist knotKp
Denoted by (Kp)q the twist knotKp with framingq, andD(Kp)q be its link diagram. By
formula (2.7), the r-th Reshetikhin-Turaev invariant ofMp,q is given by
RTr(M) =µr⟨Ωr⟩D(Kp)q⟨Ωr⟩−σ((Kp)q)
U+ .(3.1)
A direct computation shows that ⟨Ωr⟩U+ =e(− 3
r−r+1
4 )π√−1. Let σp,q =σ((Kp)q) and
κr =µ2
r⟨Ωr⟩−σp,q
U+ =
sin 2π
r√r
2
eσp,q( 3
r +r+1
4 )π√−1.(3.2)
Then we have
RTr(Mp,q) =κr⟨ωr⟩D(Kp)q =κr
r−2X
m=0
[m + 1](−1)qm+1tqm(m+2)
4 ⟨em⟩D(Kp)0
.(3.3)
Recall the definition of colored Jones polynomial [4], for a knot K with zero-framing,
we have
[m + 1]Jm+1(K;t) =⟨(−1)mem⟩DK,(3.4)
then we get
RTr(M) =κr
r−2X
m=0
[m + 1]2(−1)qmtqm(m+2)
4 Jm+1(Kp;t) (3.5)
= κr
sin2

π
N + 1
2

2N−1X
m=0
(−1)qm sin2
(m + 1)π
N + 1
2

e
qm(m+2)π√−1
2(N + 1
2 ) Jm+1(Kp;t)
And at the root of unity t =e
2π√−1
N + 1
2 , we have
Jm(Kp;t) =
m−1X
k=0
kX
l=0
(−1)k+l sin π(2l+1)
N + 1
2
sin mπ
N + 1
2
t(p+ 1
2 )l(l+1)−m(k+ 1
2 )+ 1
2k2+ 3
2k+ 1
2(3.6)
· (t)k(t)m+k
(t)k+l+1(t)k−l(t)m−k−1
.
10 QINGTAO CHEN AND SHENGMAO ZHU
Therefore, let a =N− 1−m, we obtain
RTr(Mp,q) =κ′
r
N−1X
a=−N
N−a−1X
k=0
kX
l=0
(−1)q(N−1−a)+k+l sin
(a + 1
2)π
N + 1
2

sin
2π(l + 1
2)
N + 1
2

(3.7)
·tq (N−1−a)(N +1−a)
4 +(p+ 1
2 )l(l+1)−(N−a)(k+ 1
2 )+ 1
2k2+ 3
2k+ 1
2
(t)k(t)N−a+k
(t)k+l+1(t)k−l(t)N−a−k−1
,
where
κ′
r = κr
sin2

π
N + 1
2
.(3.8)
Let
θ1 = a + 1
2
N + 1
2
, θ2 = k + 1
2
N + 1
2
, θ3 = l + 1
2
N + 1
2
.(3.9)
Then we have
tq (N−1−a)(N +1−a)
4 +(p+ 1
2 )l(l+1)−(N−a)(k+ 1
2 )+ 1
2k2+ 3
2k+ 1
2(3.10)
=e
(N + 1
2 )2π√−1

q
4 (1+θ2
1−2θ1− 1
(N + 1
2 )2 )+(p+ 1
2 )(θ2
3− 1
4(N + 1
2 )2 )−θ2+θ2θ1+ 1
2θ2
2+ θ2
(N + 1
2 )− 1
8(N + 1
2 )2

.
Moreover, by using Lemma 2.5, we have
(t)k(t)N−a+k
(t)k+l+1(t)k−l(t)N−a−k−1
(3.11)
= exp

φN
(k +l + 1) + 1
2
N + 1
2

+φN
(k−l) + 1
2
N + 1
2

−φN
 1
2
N + 1
2

−φN
k + 1
2
N + 1
2

−φN
(N−a +k) + 1
2
N + 1
2

+φN
(N−a−k− 1) + 1
2
N + 1
2

=e
φN (θ2+θ3+
1
2
N + 1
2
)+φN (θ2−θ3+
1
2
N + 1
2
)+φN (−θ1−θ2+1)−φN (θ2)−φN (1+θ2−θ1)
·e
(N + 1
2 )(π√−1
12 − π√−1
4(N + 1
2 ) + π√−1
12(N + 1
2 )2 )
(N + 1
2)− 1
2
for 0 <k +l + 1≤N and 0 <N −a +k <N,
ON THE ASYMPTOTIC EXPANSION OF V ARIOUS QUANTUM INV ARIANTS III 11
(t)k(t)N−a+k
(t)k+l+1(t)k−l(t)N−a−k−1
(3.12)
= exp

φN
(k +l + 1) + 1
2
N + 1
2

+φN
(k−l) + 1
2
N + 1
2

+φN
(N−a−k− 1) + 1
2
N + 1
2

−φN
k + 1
2
N + 1
2

−φN
(N−a +k) + 1
2
N + 1
2
− 1

−φN
 1
2
N + 1
2

+ log 2

= 2e
φN (θ2+θ3+
1
2
N + 1
2
)+φN (θ2−θ3+
1
2
N + 1
2
)+φN (−θ1−θ2+1)−φN (θ2)−φN (θ2−θ1)
·e
(N + 1
2 )(π√−1
12 − π√−1
4(N + 1
2 ) + π√−1
12(N + 1
2 )2 )
(N + 1
2)− 1
2
for 0 <k +l + 1≤N and N <N−a +k <2N,
(t)k(t)N−a+k
(t)k+l+1(t)k−l(t)N−a−k−1
(3.13)
= exp

φN
(k +l + 1) + 1
2
N + 1
2
− 1

+φN
(k−l) + 1
2
N + 1
2

+φN
(N−a−k− 1) + 1
2
N + 1
2

−φN
k + 1
2
N + 1
2

−φN
(N−a +k) + 1
2
N + 1
2

−φN
 1
2
N + 1
2

− log 2

= 1
2e
φN (θ2+θ3+
1
2
N + 1
2
−1)+φN (θ2−θ3+
1
2
N + 1
2
)+φN (−θ1−θ2+1)−φN (θ2)−φN (1+θ2−θ1)
·e
(N + 1
2 )(π√−1
12 − π√−1
4(N + 1
2 ) + π√−1
12(N + 1
2 )2 )
(N + 1
2)− 1
2
for N <k +l + 1≤ 2N and 0 <N −a +k <N,
(t)k(t)N−a+k
(t)k+l+1(t)k−l(t)N−a−k−1
(3.14)
= exp

φN
(k +l + 1) + 1
2
N + 1
2
− 1

+φN
(k−l) + 1
2
N + 1
2

+φN
(N−a−k− 1) + 1
2
N + 1
2

−φN
k + 1
2
N + 1
2

−φN
(N−a +k) + 1
2
N + 1
2
− 1

−φN
 1
2
N + 1
2

=e
φN (θ2+θ3+
1
2
N + 1
2
−1)+φN (θ2−θ3+
1
2
N + 1
2
)+φN (−θ1−θ2+1)−φN (θ2)−φN (θ2−θ1)
·e
(N + 1
2 )(π√−1
12 − π√−1
4(N + 1
2 ) + π√−1
12(N + 1
2 )2 )
(N + 1
2)− 1
2
for N <k +l + 1≤ 2N and N <N−a +k <2N.
12 QINGTAO CHEN AND SHENGMAO ZHU
Since
e
(N + 1
2 )2π√−1

q
2 (1−θ1− 1
N + 1
2
)+θ2+θ3
2 − 1
2(N + 1
2 )
(3.15)
·e
(N + 1
2 )2π√−1

q
4 (1+θ2
1−2θ1− 1
(N + 1
2 )2 )+(p+ 1
2 )(θ2
3− 1
4(N + 1
2 )2 )+θ2−θ2θ1+ 1
2θ2
2+ θ2
(N + 1
2 )− 1
8(N + 1
2 )2

·e
φN (θ2+θ3+
1
2
N + 1
2
−1)+φN (θ2−θ3+
1
2
N + 1
2
)+φN (−θ1−θ2+1)−φN (θ2)−φN (θ2−θ1)
·e
(N + 1
2 )(π√−1
12 − π√−1
4(N + 1
2 ) + π√−1
12(N + 1
2 )2 )
(N + 1
2)− 1
2
= (N + 1
2)− 1
2e
(N + 1
2 )π√−1

q( 3
2−2θ1+
θ2
1
2− 1
N + 1
2
− 1
2(N + 1
2 )2 )+(2p+1)(θ2
3− 1
4(N + 1
2 )2 )−θ1+2θ2θ1+θ2
2+θ3+ 2θ2
(N + 1
2 )

·e
(N + 1
2 )π√−1(− 5
4(N + 1
2 )− 1
6(N + 1
2 )2 + 1
12 )
,
finally, combining above formulas together, we obtain
RTr(Mp,q)
(3.16)
=κ′
r(N + 1
2)− 1
2
N−1X
a=−N
N−a−1X
k=0
kX
l=0
(−1)q(N−1−a)+k+l sin
(a + 1
2)π
N + 1
2

sin
2π(l + 1
2)
N + 1
2

·tq (N−1−a)(N +1−a)
4 +(p+ 1
2 )l(l+1)−(N−a)(k+ 1
2 )+ 1
2k2+ 3
2k+ 1
2
(t)k(t)N−a+k
(t)k+l+1(t)k−l(t)N−a−k−1
=κ′
r(N + 1
2)− 1
2
N−1X
a=−N
N−a−1X
k=0
kX
l=0
sin
(a + 1
2)π
N + 1
2

sin
2π(l + 1
2)
N + 1
2

e
(N + 1
2 ) ˜VN (
a+ 1
2
N + 1
2
,
k+ 1
2
N + 1
2
,
l+ 1
2
N + 1
2
)
,
where ˜VN(θ1,θ 2,θ 3) is given by
•
π
√
−1

q
3
2− 2θ1 + θ2
1
2 − 1
N + 1
2
− 1
2(N + 1
2)2

+ (2p + 1)

θ2
3− 1
4(N + 1
2)2

−θ2 + 2θ2θ1 +θ2
2 +θ3 + 2θ2
N + 1
2
− 5
4(N + 1
2)− 1
6(N + 1
2)2 + 1
12
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
) +φN(θ2−θ3 +
1
2
N + 1
2
) +φN(−θ1−θ2 + 1)
−φN(θ2)−φN(1 +θ2−θ1)),
when 0 <θ 2 +θ3 < 1 and 0 < 1−θ1 +θ2 < 1;
ON THE ASYMPTOTIC EXPANSION OF V ARIOUS QUANTUM INV ARIANTS III 13
•
π
√
−1

q
3
2− 2θ1 + θ2
1
2 − 1
N + 1
2
− 1
2(N + 1
2)2

+ (2p + 1)

θ2
3− 1
4(N + 1
2)2

−θ2 + 2θ2θ1 +θ2
2 +θ3 + 2θ2
N + 1
2
− 5
4(N + 1
2)− 1
6(N + 1
2)2 + 1
12
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
) +φN(θ2−θ3 +
1
2
N + 1
2
) +φN(−θ1−θ2 + 1)−φN(θ2)
−φN(θ2−θ1)),
when 0 <θ 2 +θ3 < 1 and 1 < 1−θ1 +θ2 < 2;
•
π
√
−1

q
3
2− 2θ1 + θ2
1
2 − 1
N + 1
2
− 1
2(N + 1
2)2

+ (2p + 1)

θ2
3− 1
4(N + 1
2)2

−θ2 + 2θ2θ1 +θ2
2 +θ3 + 2θ2
N + 1
2
− 5
4(N + 1
2)− 1
6(N + 1
2)2 + 1
12
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
) +φN(−θ1−θ2 + 1)
−φN(θ2)−φN(1 +θ2−θ1)),
when 1 <θ 2 +θ3 < 2 and 0 < 1−θ1 +θ2 < 1;
•
π
√
−1

q
3
2− 2θ1 + θ2
1
2 − 1
N + 1
2
− 1
2(N + 1
2)2

+ (2p + 1)

θ2
3− 1
4(N + 1
2)2

−θ2 + 2θ2θ1 +θ2
2 +θ3 + 2θ2
N + 1
2
− 5
4(N + 1
2)− 1
6(N + 1
2)2 + 1
12

+ 1
N + 1
2

φN(t +u +
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
+φN(−θ1−θ2 + 1)−φN(θ2)−φN(θ2−θ1)),
when 1 <θ 2 +θ3 < 2 and 1 < 1−θ1 +θ2 < 2.
By Lemma 2.6, we have
φN(1−θ1−θ2) =−φ(θ1 +θ2) (3.17)
+ 2π
√
−1

−2N + 1
4

(θ1 +θ2)2− (θ2 +θ1) + 1
6

+ 1
12(2N + 1)

since θ1 +θ2 < 1.
14 QINGTAO CHEN AND SHENGMAO ZHU
Hence
˜VN(θ1,θ 2,θ 3)
(3.18)
=π
√
−1

q
3
2− 2θ1 + θ2
1
2 − 1
N + 1
2
− 1
2(N + 1
2)2

+ (2p + 1)

θ2
3− 1
4(N + 1
2)2

−θ2
1 +θ1 +θ3 + 2θ2
N + 1
2
− 5
4(N + 1
2)− 1
12(N + 1
2)2− 1
12
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
−φN(θ2 +θ1)−φN(θ2)−φN(θ2−θ1)),
for 1 < θ2 +θ3 < 2 and 1 < 1−θ1 +θ2 < 2, and we can write the expression for ˜VN for
other cases similarly.
Then we introduce the functions
ˆVN(θ1,θ 2,θ 3) (3.19)
= ˜VN(θ1,θ 2,θ 3) + 2(q− 1)π
√
−1

θ1−
1
2
N + 1
2

− 2π
√
−1

θ2−
1
2
N + 1
2

− 2(p + 2)π
√
−1

θ3−
1
2
N + 1
2

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
+ p− 2q + 9
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
ˆV (θ1,θ 2,θ 3) (3.20)
= lim
N→∞
VN(θ1,θ 2,θ 3)
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

+ 1
2π√−1

Li2(e2π√−1(θ2+θ3)) + Li2(e2π√−1(θ2−θ3))− Li2(e2π√−1(θ2+θ1))
−Li2(e2π√−1θ2)− Li2(e2π√−1(θ2−θ1))

for 1 <θ 2 +θ3 < 2 and 1 < 1−θ1 +θ2 < 2, and one can write the expression for VN and
V for other cases similarly.
ON THE ASYMPTOTIC EXPANSION OF V ARIOUS QUANTUM INV ARIANTS III 15
Proposition 3.1. Letr = 2N + 1 with N≥ 1, the r-th Reshetikhin-Turaev invariant of
Mp,q can be written as
RTr(Mp,q) =κ′
r(N + 1
2)− 1
2
N−1X
a=0
N−a−1X
k=0
kX
l=0
gN(a,k,l ) (3.21)
with
gN(a,k,l ) = sin
(a + 1
2)π
N + 1
2

sin
2π(l + 1
2)
N + 1
2

e
(N + 1
2 ) ˆVN

a+ 1
2
N + 1
2
,
k+ 1
2
N + 1
2
,
l+ 1
2
N + 1
2

,(3.22)
where the function ˆVN(θ1,θ 2,θ 3) is given by formula (3.19), and κ′
r is given by (3.8).
