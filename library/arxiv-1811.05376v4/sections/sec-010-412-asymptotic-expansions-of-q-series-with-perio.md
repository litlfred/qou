---
doc_id: arxiv-1811.05376v4
doc_title: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres"
section_id: sec-010-412-asymptotic-expansions-of-q-series-with-perio
section_title: "Asymptotic expansions of q-series with periodic coefficients"
section_number: 4.1.2
pages: 31-33
source_pdf: 1811.05376v4.pdf
source_sha256: a486709d0a78d19c
doc_brief: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres — For a Seifert ﬁbered homology sphereX we show that the q-series invariant ˆZ0(X;q) introduced by Gukov-Pei-Putrov-Vafa"
---
Let Bm(x) denote them-th Bernoulli polynomial, i.e.
tetx
et− 1 =
∞∑
m=0
Bm(x)
m! tm. (74)
We recall the following result.
Proposition 13 ([31, 40]). LetC : Z→ C be a periodic function with periodM and mean value
equal to zero
M∑
m=1
C(n) = 0.
Consider theL-series L(s,C ), which forℜ(s)> 1 is deﬁned by
L(s,C ) =
∞∑
m=1
C(m)
ms .
This L-series admits an analytic extension to all ofC and forr∈ N
L(−r,C ) =− Mr
r + 1
M∑
m=1
C(m)Br+1
(m
M
)
. (75)
For any polynomialQ of degreed
Q(x) =
d∑
u=0
quxu∈ C[x]
the following asymptotic expansions hold for real and positivet
∞∑
m=1
e−tm2
C(m)Q(m) ∼
t→0
d∑
u=0
∞∑
r=0
quL(−2r−u,C )(−t)r
r! . (76)
Proof. The existence of the analytic extension of theL-series ofC, as well as the explicit evaluation
(75) are proven in [40].
In [31, 40] the following asymptotic expansions are proven
∞∑
m=1
C(m)e−tm2
∼
t→0
∞∑
r=0
L(−2r,C )(−t)r
r! ,
∞∑
m=1
mC(m)e−tm2
∼
t→0
∞∑
r=0
L(−2r− 1,C )(−t)r
r! .
(77)
Resurgence Analysis of Quantum Invariants 32
We have ∞∑
m=1
e−tm2
C(m)Q(m) =
∞∑
j=0
∂j
∂(−t)j
∞∑
m=0
(q2j+1m +q2j)e−tm2
,
whereitisunderstoodthat ql = 0forl>d . Theexpansion(76)followsformallyfromdiﬀerentiating
the expansions given in (77). This diﬀerentiation is valid because Poincare asymptotic expansions
of analytic functions which are valid on suitable sectors can be termwise diﬀerentiated. Clearly
t↦→∑
m≥0C(m)Q(m) exp(−tm2) is an analytic function oft in a small tubular neighbourhood of
(0, 1], and from the proof given in [40] it is clear that the asymptotic expansions (77) are valid on
such a small sector.
Recall the deﬁnition of the meromorphic functionF given in (15). Next we prove that the
coeﬃcients of the principal part ofF at poles are periodic functions with mean value equal to zero.
Proposition 14. Forj = 1, 2,...,n − 2 deﬁnefj : Z→ C as the coeﬁcients of the principal part
of F at 2πim for m∈ Z, e.g. fory near 2πim
F (y) =
n−2∑
j=1
fj(m)(y− 2πim)−j + reg..
Then eachfj is 2P-periodic and ifP is even, then we have for each evenk∈ Z
∑
m=1,...,2P
ekg(2πim)fj(m) = 0. (78)
Proof. The periodicity of the functionsfj,j = 1,...,n− 3 follow directly from the4πiP-periodicity
of F.
We now prove (78) assumingP is even - which is equivalent to exactly one thepj being even.
Using the deﬁnition (15) ofF we obtain
F (y + 2πiP ) = 1
4 sinh(y/2 +πiP )2−n
n∏
j=1
sinh(y/pj +πiP/pj)
= (−1)nP (−1)
∑n
j=1
P
pjF (y) =−F (y).
This implies that for eachj = 1,...,n − 3 and m = 1,...,P we have
fj(m +P ) =−fj(m).
On the other hand we have for integralm
g(2πi(P +m)) = i(2πi(P +m))2
8πP =−iπm2
2P ∓iπmP− iπP
2
=g(2πi(P∓m)) mod πiZ.
It follows that for evenk we have a pairwise cancellation
2P∑
m=1
ekg(2πim)fj(m) =
P∑
m=1
ekg(2πim)fj(m) +ekg(2πi(m+P))fj(m +P )
=
P∑
m=1
ekg(2πim)fj(m)−ekg(2πim)fj(m) = 0.
This concludes the proof.
Resurgence Analysis of Quantum Invariants 33
