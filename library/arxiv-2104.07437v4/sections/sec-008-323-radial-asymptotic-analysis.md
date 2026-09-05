---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-008-323-radial-asymptotic-analysis
section_title: "Radial asymptotic analysis"
section_number: 3.2.3
pages: 24-27
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
---
One of the important lessons we learned from [11, 12] is that it is often helpful to study the
asymptotic behavior of the anti-holomorphic blocks 8 in the limit gs∝− b−2→ 0 along a ray
eiθR+, which depends crucially on the angle θ. Oftentimes, it is possible to promote these radial
asymptotic behavior of anti-holomorphic blocks to exact representations of them in terms of the
Borel resummation of the asymptotic series Φ σ(gs), together with non-perturbative corrections
parametrised by q-series. This turns out to be an extremely powerful method to compute the
Stokes automorphism of the asymptotic series Φ σ(gs).
In the case of the anti-holomorphic blocks ˜ g(˜q), ˜G(˜q) uncovered from evaluating the ﬁrst
trace of local F0, we ﬁnd that they can be expressed in terms of Borel resummations of Φ( gs) in
the following way ( 1√πgs ˜g(˜q)
−8√πgs ˜G(˜q)
)
= 2−3/2MR(q)sR(Φ)(gs), (3.72)
where MR(q) is a 2 × 2 matrix of q-series that encodes non-perturbative corrections. We
parametrise it by
MR(q) =
(gR
+(q) −gR
−(q)
GR
+(q) GR
−(q)
)
. (3.73)
Note that it depends on the sector R. We will focus on the two sectors I,II , as shown in Fig. 4.
When gs is in the sector I, we ﬁnd that
gI
+(q) = 1 +q1/2−q + 2q3/2− 2q2 +..., (3.74a)
GI
+(q) = 1 + 5q1/2−q + 10q3/2− 2q2 +..., (3.74b)
gI
−(q) = 1 + 3q1/2− 2q + 3q3/2 +..., (3.74c)
GI
−(q) = 1− 9q1/2− 2q− 9q3/2 +.... (3.74d)
it is easy to identify that
gI
+(q) =g0(q), G I
+(q) =G0(q), (3.75)
and we will denote them by g(q),G (q). In addition, these four q-series satisfy the “Wronskian”-
like identity
gI
+(q)GI
−(q) +GI
+(q)gI
−(q) = 2. (3.76)
8In [11, 12] one studies the asymptotics of holomorphic blocks in the opposite limit b2→ 0, which corresponds
to the semiclassical regime.
– 23 –
With the help of (3.71), we are able to identify
gI
−(q) =−1−q1/2
q1/4 g1(q) + 2g0(q), (3.77a)
GI
−(q) = 1−q1/2
2q1/4 (G1(q) +H1(q))− 2G0(q), (3.77b)
which we will denote by g′(q),G′(q). Similarly in sector II , we ﬁnd in fact
gII
− (q) =g(q), G II
− (q) =G(q),
gII
+ (q) =g′(q), G II
+ (q) =G′(q). (3.78)
Once MI,II (q) are known, the Stokes automorphism SI↦→II (q) can be computed by
SI↦→II (q) =MII (q)−1MI(q), (3.79)
which yields (3.34).
This calculation illustrates that the additional analytic structures provided by the TS/ST
correspondence makes it possible to calculate the Stokes constants associated to the series Φ0,1(gs)
and to express it in closed form, in terms of the q-series appearing in the factorization of the
spectral trace (3.71) and their descendants (3.64).
We close this subsection by commenting that the radial asymptotic formula (3.72) together
with the factorisation formula (3.70) allows us to express the trace in terms of Borel sum of
asymptotic series:
• When gs is in sector I
TrρF0 =−i√πgs
23/2
(
g(q)G(q)sI(Φ0)(gs) + 1
2(g(q)G′(q)−G(q)g′(q))sI(Φ1)(gs)
)
. (3.80)
Note that here Φ 0(gs) is the dominant series.
• When gs is in sector II
TrρF0 =−i√πgs
23/2 sII (Φ0)(gs). (3.81)
In both sectors in the leading order we have
Z1(ℏ) = TrρF0∼− i√πgs
23/2 Φ0(gs), |gs|≪ 1, (3.82)
which is consistent with the prediction (3.5) from the TS/ST correspondence.
3.2.4 Relation to q-Painlev´ e
In [79], it has been conjectured that the spectral determinant of local F0 satisﬁes a q-deformed
Painlev´ e equation, which is a diﬀerence equation involving the mass parameterξ. This leads to
q-diﬀerence equations for the spectral traces. Since we have an explicit expression for the ﬁrst
trace in terms of q-hypergeometric functions given by (3.55), it is natural that the q-Painlev´ e
equation maps to the q-diﬀerence equation satisﬁed by the q-hypergeometric function. We will
now explicitly show that this is the case.
– 24 –
In the notation used above, the q-diﬀerence equation found in [79] reads
2 tanh(ξ)Z(ξ) +Z(ξ +πib−2) +Z(ξ−πib−2) = 0. (3.83)
First of all, we note that this relation does not aﬀect the “holomorphic” part of the trace, since
the above shifts leave invariant e2b2ξ. In terms of the dual mass parameter
ξD =−b2ξ (3.84)
and the exponentiated variables
z = e−2ξ, z D = e−2ξD, (3.85)
we can write down the factorization
(q;q)2
∞(−˜qe2ξ; ˜q)∞(−˜qe−2ξ; ˜q)∞
(q1/2;q)2∞(˜qe2ξ; ˜q)∞(˜qe−2ξ; ˜q)∞
coth(ξ)I(ξ, b) =H(q,zD)~H(˜q,z ), (3.86)
where
H(q,zD) = eb2ξ/2 (qe2b2ξ;q)∞(q;q)∞
(q1/2;q)∞(q1/2e2b2ξ;q)∞
2φ1
(
q1/2,q 1/2e2b2ξ
qe2b2ξ ;q,q 1/2
)
,
~H(˜q,z ) = coth(ξ)(−˜qe2ξ; ˜q)∞(−˜qe−2ξ; ˜q)∞
(˜qe2ξ; ˜q)∞(˜qe−2ξ; ˜q)∞
2φ1
(−1,−1
˜q ; ˜q,−˜qe−2ξ
)
.
(3.87)
We can write
Z(ξ) =−z−1/4
D q1/8
2
(
H(q,zD)~H(˜q,z )−H (q,z−1
D )~H(˜q,z−1)
)
. (3.88)
We note that
Z(ξ±πib−2) =−z−1/4
D q1/8
2
(
H(q,zD)~H(˜q,z ˜q∓1) +H(q,z−1
D )~H(˜q,z−1˜q±1)
)
. (3.89)
The diﬀerence equation (3.83) implies then two equations,
−2~H(˜q,z ) = ˜q +z
˜q−z
~H(˜q,z/q ) + 1 + ˜qz
1− ˜qz
~H(˜q,zq ),
2~H(˜q, 1/z) = ˜q +z
˜q−z
~H(˜q,q/z ) + 1 + ˜qz
1− ˜qz
~H(˜q, 1/zq),
(3.90)
which are simply exchanged by z↔ 1/z. Let us then focus on the ﬁrst one. By plugging in
the explicit expression for H(˜q,z ), and changing the sign z→−z, we ﬁnd the simple diﬀerence
equation
2φ(˜qz) = 1−z
1 +z
(
φ(z) +φ(z˜q2)
)
, (3.91)
where
φ(z) = 2φ1
(−1,−1
˜q ; ˜q,z
)
. (3.92)
On the other hand, a generic q-hypergeometric function
Φ = 2φ1
(a,b
c ;q,z
)
(3.93)
– 25 –
u
