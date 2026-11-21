---
doc_id: arxiv-1811.05376v4
doc_title: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres"
section_id: sec-010-412-asymptotic-expansions-of-q-series-with-perio
section_title: "Asymptotic expansions of q-series with periodic coefficients"
section_number: 4.1.2
pages: 31-33
source_pdf: 1811.05376v4.pdf
source_sha256: a486709d0a78d19c
toc_source: outline
doc_brief: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres — For a Seifert ﬁbered homology sphere X we show that the q-series invariant ˆZ0(X; q) introduced by"
---
Asymptotic expansions of q-series with periodic coeﬃcients
Let Bm(x) denote the m-th Bernoulli polynomial, i.e.
tetx
et −1 =
∞
X
m=0
Bm(x)
m!
tm.
(74)
We recall the following result.
Proposition 13 ([31, 40]). Let C : Z →C be a periodic function with period M and mean value
equal to zero
M
X
m=1
C(n) = 0.
Consider the L-series L(s, C), which for ℜ(s) > 1 is deﬁned by
L(s, C) =
∞
X
m=1
C(m)
ms .
This L-series admits an analytic extension to all of C and for r ∈N
L(−r, C) = −M r
r + 1
M
X
m=1
C(m)Br+1
 m
M

.
(75)
For any polynomial Q of degree d
Q(x) =
d
X
u=0
quxu ∈C[x]
the following asymptotic expansions hold for real and positive t
∞
X
m=1
e−tm2C(m)Q(m)
∼
t→0
d
X
u=0
∞
X
r=0
quL(−2r −u, C)(−t)r
r!
.
(76)
Proof. The existence of the analytic extension of the L-series of C, as well as the explicit evaluation
(75) are proven in [40].
In [31, 40] the following asymptotic expansions are proven
∞
X
m=1
C(m)e−tm2
∼
t→0
∞
X
r=0
L(−2r, C)(−t)r
r!
,
∞
X
m=1
mC(m)e−tm2
∼
t→0
∞
X
r=0
L(−2r −1, C)(−t)r
r!
.
(77)
We have
∞
X
m=1
e−tm2C(m)Q(m) =
∞
X
j=0
∂j
∂(−t)j
∞
X
m=0
(q2j+1m + q2j)e−tm2,
where it is understood that ql = 0 for l > d. The expansion (76) follows formally from diﬀerentiating
the expansions given in (77). This diﬀerentiation is valid because Poincare asymptotic expansions
of analytic functions which are valid on suitable sectors can be termwise diﬀerentiated. Clearly
t 7→P
m≥0 C(m)Q(m) exp(−tm2) is an analytic function of t in a small tubular neighbourhood of
(0, 1], and from the proof given in [40] it is clear that the asymptotic expansions (77) are valid on
such a small sector.
Recall the deﬁnition of the meromorphic function F given in (15). Next we prove that the
coeﬃcients of the principal part of F at poles are periodic functions with mean value equal to zero.
Proposition 14. For j = 1, 2, ..., n −2 deﬁne fj : Z →C as the coeﬁcients of the principal part
of F at 2πim for m ∈Z, e.g. for y near 2πim
F(y) =
n−2
X
j=1
fj(m)(y −2πim)−j + reg..
Then each fj is 2P-periodic and if P is even, then we have for each even k ∈Z
X
m=1,...,2P
ekg(2πim)fj(m) = 0.
(78)
Proof. The periodicity of the functions fj, j = 1, ..., n−3 follow directly from the 4πiP-periodicity
of F.
We now prove (78) assuming P is even - which is equivalent to exactly one the pj being even.
Using the deﬁnition (15) of F we obtain
F(y + 2πiP) = 1
4 sinh(y/2 + πiP)2−n
n
Y
j=1
sinh(y/pj + πiP/pj)
= (−1)nP (−1)
Pn
j=1
P
pj F(y) = −F(y).
This implies that for each j = 1, ..., n −3 and m = 1, ..., P we have
fj(m + P) = −fj(m).
On the other hand we have for integral m
g(2πi(P + m)) = i(2πi(P + m))2
8πP
= −iπm2
2P
∓iπmP −iπP
2
= g(2πi(P ∓m))
mod πiZ.
It follows that for even k we have a pairwise cancellation
2P
X
m=1
ekg(2πim)fj(m) =
P
X
m=1
ekg(2πim)fj(m) + ekg(2πi(m+P ))fj(m + P)
=
P
X
m=1
ekg(2πim)fj(m) −ekg(2πim)fj(m) = 0.
This concludes the proof.
