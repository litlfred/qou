---
doc_id: arxiv-1912.10638v2
doc_title: "Asymptotics of some quantum invariants of the Whitehead chains Ka Ho WONG"
section_id: sec-008-23-the-asymptotics-expansion-formula-for-jm1m2wl
section_title: "The asymptotics expansion formula for JM1,M2(WL,e2iN+12)"
section_number: 2.3
pages: 13-16
source_pdf: 1912.10638v2.pdf
source_sha256: 612e44871d91d2e2
doc_brief: "Asymptotics of some quantum invariants of the Whitehead chains Ka Ho WONG — In this paper, we study the asymptotics of the colored Jones polynomials of the Whitehead chains with one belt colored by"
---
2πi
N + 1
2 )
In this section, we generalize the previous argument to study the asymptotics expansion formula for
JM1,M2(WL,e
2πi
N + 1
2 ). Recall that the potential functions Φ ±(s1,s2)(z1,z 2) are given by
Φ±(s1,s2)(z1,z 2) = 1
2πi
[
± (2πi (s1− 1))
(
2πi
(
z1− 1
2
))
− (2πi(s2− 1))(2πiz1 + 2πiz2)
+ Li2
(
e2πi(s2−1)−2πiz1−2πiz2
)
− Li2
(
e2πi(s2−1)−2πiz2
)
+ Li2
(
e2πiz2
)
− Li2
(
e2πiz1+2πiz2
)
+ Li2
(
e2πiz1
)]
13
From now on, for simiplicity we consider the potential function Φ+(s1,s2)(z1,z 2). The same arguement
works for the potential function Φ −(s1,s2)(z1,z 2). The following lemma gaurantees the existence of the
critical points for the potential functions.
Lemma 3. There exists a neighborhood U ⊂ C2 of (1, 1)∈ C2 and two holomorphic families of non-
degenerate critical points{z±(s1,s2)}(s1,s2)∈U for the families of potential functions Φ±(s1,s2)(z1,z 2) such
that z±(1,1) =
( 1
2, 1
4
)
.
Proof. First of all, we pick a small enough neighborhood U⊂ C2 of the point (1, 1)∈ C2 such that the
function F :U×BR→ C deﬁned by
F (s1,s 2,z 1,z 2) = Φ+(s1,s2)(z1,z 2)
is well-deﬁned and holomorphic. Consider the function G :U×BR→ C2 given by
G(s1,s 2,z 1,z 2) =
( ∂
∂z1
F (s1,s 2,z 1,z 2), ∂
∂z2
F (s1,s 2,z 1,z 2)
)
By direct computation, we have
∂
∂z1
F (s1,s 2,z 1,z 2) = 2πi [(s1− 1)− (s2− 1)] + log(1−e2πi(s2−1)e−2πiz1−2πiz2)
+ log(1−e2πiz1+2πiz2)− log(1−e2πiz1) (34)
∂
∂z2
F (s1,s 2,z 1,z 2) =−2πi(s2− 1) + log(1−e2πi(s2−1)e−2πiz1−2πiz2)
+ log(1−e2πiz1+2πiz2)− log(1−e2πi(s2−1)−2πiz2)
− log(1−e2πiz2) (35)
Moreover,
∂
∂s1
( ∂
∂z1
F (s1,s 2,z 1,z 2)
)
= 2πi (36)
∂
∂s2
( ∂
∂z1
F (s1,s 2,z 1,z 2)
)
= 0 (37)
∂
∂s2
( ∂
∂z2
F (s1,s 2,z 1,z 2)
)
=−2πi− 2πie2πi(s2−1)e−2πiz1−2πiz2
1−e2πi(s2−1)e−2πiz1−2πiz2
+ 2πie2πi(s2−1)e−2πiz2
1−e2πi(s2−1)e−2πiz2
(38)
As a result, we have
⏐⏐⏐⏐⏐⏐
∂
∂s1
(
∂
∂z1
F
)
∂
∂s2
(
∂
∂z1
F
)
∂
∂s1
(
∂
∂z2
F
)
∂
∂s2
(
∂
∂z2
F
)
⏐⏐⏐⏐⏐⏐
(
1, 1, 1
2, 1
4
)
=−2πi(1 +i)⁄= 0 (39)
The result follows from the implicit function theorem.
Note that on the surfaces S+
1 , from (28) we have
Re Φ(1,1)(x1±ηi,x 2)− Re Φ(1,1)(z(1,1))< 2πη (40)
Since S+
1 is a compact set, by continuity, we may choose δ small enough such that
Re Φ(s1,s2)(x1 +ηi,x 2)− Re Φ(s1,s2)(z+(s1,s2))< 2πη
for any 1−δ <s1,s 2≤ 1. The same argument works for S−
1 ,S +
2 and S−
2 .
As a result, the assumptions for applying the Poisson Summation formula are satisﬁed. Finally, for
the same reason, we can chooseδ >0 small enough such that the conditions for applying the saddle point
approximation are automatically satisﬁed. Together with Lemma 2, the asymptotic expansion formula
of JM1,M2(WL,e
2πi
N + 1
2 ) is given by
14
JM1,M2(WL,e
2πi
N + 1
2 )
= (−1)(M1−N)e
2πi
N + 1
2
(M 2
2−M2
2 − 1
2 )
2 sin( π
N+ 1
2
) exp
(
−ϕr
( π
2(N + 1
2)
))
[
e
πi
(
M1
N + 1
2
−1
)M2−1∑
n=0
M2−1−n∑
l=0
exp
((
N + 1
2
)
Φ+(s1,s2)
M1,M2
( n
N + 1
2
, l
N + 1
2
))
+e
−πi
(
M1
N + 1
2
−1
)M2−1∑
n=0
M2−1−n∑
l=0
exp
((
N + 1
2
)
Φ−(s1,s2)
M1,M2
( n
N + 1
2
, l
N + 1
2
))]
∼
N→∞
e−πi
4 (−1)(M1−N)e
2πi
N + 1
2
(M 2
2−M2
2 − 1
2 )
2π
(
N + 1
2
) 1
2
exp
(N + 1
2
2π
π2i
6
)(
N + 1
2
)2
[
e
πi( M1
N + 1
2
−1)
∫ ∫
BR∩∆
EM2(z1,z 2) exp
((
N + 1
2
)
Φ
+
(
M1
N + 1
2
, M2
N + 1
2
)
(z1,z 2)
)
dz1dz2
+e
−πi( M1
N + 1
2
−1)
∫ ∫
BR∩∆
EM2(z1,z 2) exp
((
N + 1
2
)
Φ
−
(
M1
N + 1
2
, M2
N + 1
2
)
(z1,z 2)
)
dz1dz2
]
∼
N→∞
e−πi
4 (−1)(M1−N)e
2πi
N + 1
2
(M 2
2−M2
2 − 1
2 )
2 exp
(N + 1
2
2π
π2i
6
)(
N + 1
2
) 3
2


e
πi
(
M1
N + 1
2
−1
)
EM2(z+(s1,s2)
M1,M2 )
exp
(
(
N + 1
2
)
Φ
+
(
M1
N + 1
2
, M2
N + 1
2
)(
z
+
(
M1
N + 1
2
, M2
N + 1
2
)))
vuu√− det Hess Φ
+
(
M1
N + 1
2
, M2
N + 1
2
)(
z
+
(
M1
N + 1
2
, M2
N + 1
2
))
+e
−πi
(
M1
N + 1
2
−1
)
EM2(z−(s1,s2)
M1,M2 )
exp
(
(
N + 1
2
)
Φ
−
(
M1
N + 1
2
, M2
N + 1
2
)(
z
−
(
M1
N + 1
2
, M2
N + 1
2
)))
vuu√− det Hess Φ
−
(
M1
N + 1
2
, M2
N + 1
2
)(
z
−
(
M1
N + 1
2
, M2
N + 1
2
))


,
(41)
where the last line holds because those terms do not cancel out with each other. In fact, at the end of
Section 2.5, we will show that for s1,s 2 suﬃciently close to 1,
Φ+(s1,s2)(z+(z1,z2)) = Φ−(s1,s2)(z−(z1,z2))
and
Re Φ+(s1,s2)(z+(z1,z2)) = Re Φ−(s1,s2)(z−(z1,z2)) = Vol
(
S3\WL,u 1 = 2πi(1−s1),v 2 = 4πi(1−s2)
)
,
where Vol
(
S3\WL,u 1 = 2πi(1−s1),v 2 = 4πi(1−s2)
)
is the hyperbolic volume of the Whitehead link
complement equipped with the incomplete hyperbolic structure such that the logarithm of the holonomy
of the meridian of the belt and the logarithm of the holonomy of the longitude of the clasp are u1 =
2πi(1−s1) and v2 = 4πi(1−s2) respectively. As a result, by choosing δ >0 suﬃciently small, for any
1−δ <s1,s 2≤ 1, we have
15
JM1,M2(WL,e
2πi
N + 1
2 ) ∼
N→∞
e−πi
4 (−1)(M1−N)e
2πi
N + 1
2
(M 2
2−M2
2 − 1
2 )
2 exp
(N + 1
2
2π
π2i
6
)(
N + 1
2
) 3
2


e
πi
(
M1
N + 1
2
−1
)
EM2(z+(s1,s2)
M1,M2 )vuu√− det Hess Φ
+
(
M1
N + 1
2
, M2
N + 1
2
)(
z
+
(
M1
N + 1
2
, M2
N + 1
2
))
+
e
−πi
(
M1
N + 1
2
−1
)
EM2(z−(s1,s2)
M1,M2 )vuu√− det Hess Φ
−
(
M1
N + 1
2
, M2
N + 1
2
)(
z
−
(
M1
N + 1
2
, M2
N + 1
2
))


exp
((
N + 1
2
)
Φ
+
(
M1
N + 1
2
, M2
N + 1
2
)(
z
+
(
M1
N + 1
2
, M2
N + 1
2
)))
(42)
