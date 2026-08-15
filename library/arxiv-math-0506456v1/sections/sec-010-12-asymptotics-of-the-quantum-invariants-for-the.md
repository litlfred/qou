---
doc_id: arxiv-math-0506456v1
doc_title: "Journal of Knot Theory and Its Ramiﬁcations c© W orld Scientiﬁc Publishing Company ASYMPTOTICS OF THE QUANTUM INV ARIANTS FOR SURGERIES ON THE FIGURE 8 KNOT JØRGEN ELLEGAARD ANDERS"
section_id: sec-010-12-asymptotics-of-the-quantum-invariants-for-the
section_title: "Asymptotics of the quantum invariants for the ﬁgure 8 knot"
section_number: 12
pages: 11-12
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
where Φ is the Rademacher Phi function, see [26], and ˜· is the unitary representation
of P SL(2, Z) given by
˜Bj,k =
√
−1 sign(q)√
2r|q|
e−
√−1π
4 Φ(B)
×
∑
µ=±1
∑
n∈Z/|q|Z
µ exp
(√−1π
2rq [pj2 − 2µj(k + 2rnµ) +d(k + 2rnµ)2]
)
.
By evaluating the sum over µ we get
τr(Np/q) = a(r)
∑
n∈Z/|q|Z
exp
(
2πirdn2
q
)
(2.13)
×
r−1∑
k=1
sin
(π
q
[
2nd − k
r
])
exp
(
πir
2q
[
p
(k
r
) 2
− 4nk
r
])
[k]J ′
K(k),
where
a(r) = − 2sign(q)
r
√
|q|
sin
(π
r
)
e− 3πi
4 sign(pq) exp
(πi
2r
[
3sign(pq) − p
q + S
(p
q
)])
.
Here S is the Dedekind symbol, see e.g. [17]. We note that the quantum invariant
τr is independent of the colored Jones polynomial J ′
K(k) for the top-color k =r.
In the remaining part of this paper K will denote the ﬁgure 8 knot unless
explicitly stated otherwise. Recall that Mp/q denotes the 3–manifold obtained by
surgery onS3 alongK with surgery coeﬃcient p/q ∈ Q. By an R–matrix calculation
(see e.g. [11]) we ﬁnd that
J ′
K(λ) =
λ−1∑
m=0
ξ−mλ
m∏
l=1
(1 −ξλ−l)(1 −ξλ+l) (2.14)
for λ = 1, 2,...,r , where ∏ m
l=1(1 −ξk−l)(1 −ξk+l) = 1 for m = 0. Le and Habiro
have obtained a similar formula, cf. [20].
Remark 1. Unitarity of the TQFT associated to Ut implies that
τr(−M ) =
τr(M ) (2.15)
for any 3–manifold M , where · means complex conjugation. This formula also
follows directly from [16] and the remarks concerning normalization f ollowing (2.12).
Since the ﬁgure 8 knot is amphicheiral, M−p/q andMp/q are orientation reversing
homeomorphic. By (2.15) we therefore have
τr(Mp/q) = τr(M−p/q). (2.16)
This formula also follows directly by (2.13) and the facts that J ′
K(λ) is real and
S(−p/q) = −S(p/q). That J ′
K(λ) is real follows by amphicheirality of K but can
12 Asymptotics of the quantum invariants for the ﬁgure 8 knot
also be seen directly from (2.14) by
J ′
K(λ) =
λ−1∑
m=0
m∏
l=1
ξ−λ/2ξl/2(1 −ξλ−l)ξ−λ/2ξ−l/2(1 −ξλ+l)
=
λ−1∑
m=0
m∏
l=1
(ξ(λ−l)/2 −ξ−(λ−l)/2)(ξ(λ+l)/2 −ξ−(λ+l)/2)
=
λ−1∑
m=0
(−4)m
m∏
l=1
sin(π(λ −l)/r) sin(π(λ +l)/r).
By (2.13) and (2.14) we get the following preliminary formula for the RT –invariants
of the manifolds Mp/q:
τr(Mp/q) = ia(r)
2 sin(π/r)
∑
n∈Z/|q|Z
exp
(
2πirdn2
q
)
×
r−1∑
k=1
exp
(
πir
2q
[
p
(k
r
) 2
− 4nk
r
])
sin
(π
q
[
2nd − k
r
])
×
r−1∑
m=0
ξ−(m+1/2)k
(1 −ξk)
m∏
l=0
(1 −ξk−l)(1 −ξk+l). (2.17)
