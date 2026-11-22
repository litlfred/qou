---
doc_id: arxiv-2105.09342v1
doc_title: "A Unitary Matrix Model for q-deformed Plancherel Growth"
section_id: sec-003-31-solution-class-1-no-gap-solution
section_title: "Solution class 1: No-gap solution"
section_number: 3.1
pages: 10-12
source_pdf: 2105.09342v1.pdf
source_sha256: 57ae12327da7b9a1
toc_source: outline
doc_brief: "A Unitary Matrix Model for q-deformed Plancherel Growth — In this paper we construct a unitary matrix model that captures the asymptotic growth of Young diagrams under q-deformed Plancherel measure."
---
Taking the ansatz u(h) = 1 for 0 ≤h ≤a and u(h) = ˜u(h) for a ≤h ≤b in h-plane, we
have
u(w) =
(
1
1−λw
for 0 ≤w ≤wa
˜u(w)
for wa ≤w ≤wb
(3.18)
where wa = 1−e−λa
λ
and wb = 1−e−λb
λ
. Putting this ansatz in the saddle point equation (3.17),
we get
−
Z wb
wa
dw′ ˜u(w′)
w −w′ =
1
1 −λw log

w −wa
ξ(1 −λwa)

.
(3.19)
We deﬁne a resolvent function
H(w) =
Z
dw′ u(w′)
w −w′,
(3.20)
to solve the integral equation. H(w) is analytic in the whole complex plane except at the
support of u(w), where it has a branch cut. The Young diagram density is given by the
discontinuity of H(w) about the branch cut. Following the standard technique [19], we can
write
H(w) =
1
1 −λw log w(1 −λwa)
w −wa
−
p
(w −wa)(w −wb)
I
C
ds
2πi
log
h
s−wa
ξ(1−λwa)
i
(s −w)(1 −λs)
p
(s −wa)(s −wb)
(3.21)
where the contour C encloses the branch cut between wa and wb. To evaluate the integral
in (3.21), we deform the contour as depicted in ﬁg 3. The resolvent is ﬁnally given by
H(w) =
1
1 −λw

log w
ξ + 2 tanh−1
rw −wb
w −wa

+
λ
1 −λw
s
(w −wa)(w −wb)
(1 −λwa)(1 −λwb)
"
log λξ + 2 tanh−1
r
1 −λwb
1 −λwa
#
.
(3.22)
10
Figure 3: The deformed contour of integration for (3.21) has a logarithmic branch cut extending from wa
to −∞. There are ﬁrst order poles at the points s = w, 1
λ
From the asymptotic behaviour of the resolvent, one can ﬁnd that the support of ˜u(w) is
given by
wa = 1 −e−λ(1 + λξ)2
λ
,
wb = 1 −e−λ(1 −λξ)2
λ
(3.23)
For w inside the support, the discontinuity of H(w) gives
˜u(w) =
2
π(1 −λw) tan−1
rwb −w
w −wa
.
(3.24)
In terms of our original variables h(x),
˜u(h)
=
(1 −λw) ˜u(w)
=
1
π cos−1 h1 + λ2ξ2 −e−λ(h−1)
2λξ
i
(3.25)
with support between a and b given by
a = 1 −2
λ log (1 + λξ) ,
and
b = 1 −2
λ log (1 −λξ) .
(3.26)
Since a ≥0, the solution (3.25) is valid for
ξ ≤1
λ(eλ/2 −1).
(3.27)
11
