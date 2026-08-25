---
doc_id: arxiv-0905.0228v4
doc_title: "A CURIOUS q-ANALOGUE OF HERMITE POL YNOMIALS"
section_id: sec-004-51-some-well-known-facts
section_title: "Some well-known facts"
section_number: 5.1
pages: 16-17
source_pdf: 0905.0228v4.pdf
source_sha256: 1744545d0f210949
doc_brief: "A CURIOUS q-ANALOGUE OF HERMITE POLYNOMIALS — Two well-known q-Hermite polynomials are the continuous and discrete q-Hermite polynomials."
---
onal polynomials (see [2, 18, 17]). Let pn(x) be a sequence of polynomials which satisﬁes the
three term recurrence relation
pn+1(x) = ( x − bn)pn(x) − λ npn−1(x) (5.1)
with initial values p0(x) = 1 and p−1(x) = 0.
Deﬁne the coeﬃcients a(n, k ) (0 ≤ k ≤ n) by
n∑
k=0
a(n, k )pk(x) = xn. (5.2)
These are characterized by the Stieltjes tableau :
a(0, k ) = δk, 0,
a(n, 0) = b0a(n − 1, 0) + λ 1a(n − 1, 1),
a(n, k ) = a(n − 1, k − 1) + bka(n − 1, k ) + λ k+1a(n − 1, k + 1).
(5.3)
If F is the linear functional such that F(pn(x)) = δn, 0, then
F(xn) = a(n, 0). (5.4)
The generating function of the moments has the continued fra ction expansion
∑
n≥0
F(xn)zn = 1
1 − b0z − λ 1z2
1 − b1z − λ 2z2
1 − · · ·
. (5.5)
The Hankel determinants for the moments are
d(n, 0) = det( F(zi+j))n−1
i,j =0 =
n−1∏
i=1
i∏
k=1
λ k, (5.6)
and
d(n, 1) = det( F(zi+j+1))n−1
i,j =0 = d(n, 0)(−1)npn(0). (5.7)
As an example we want to give another simple proof of (1.10).
Proposition 16. The continuous q-Hermite polynomials ˜Hn(x, s |q) deﬁned by (1.9), i.e.,
˜Hn+1(x, s |q) = x ˜Hn(x, s |q) − s[n]q ˜Hn−1(x, s |q), (5.8)
are the moments of the measure of the orthogonal polynomials pn(z) := Pn(z; x, −s, 0) deﬁned
by the recurrence
pn+1(z) = ( z − xqn)pn(z) + sqn−1[n]qpn−1(z). (5.9)
16
Proof. Let bn = qnx and λ n+1 = (−s)qn[n + 1]q for n ≥ 0. It is suﬃcient to verify that in this
case (5.3) is satisﬁed with
a(n, k ) =
[ n
k
]
˜Hn−k(z, s |q). (5.10)
This is clearly equivalent to (5.8).
We derive immediately the Hankel determinants
d(n, 0) = ( −s)(n
2)q(n
3)
n−1∏
j=0
[j]q!, (5.11)
and
d(n, 1) = d(n, 0)r(n), (5.12)
where r(n) = ( −1)npn(0; x, −s, 0).
Note that the polynomials r(n) satisfy
r(n) = qn−1xr(n − 1) + qn−2s[n − 1]qr(n − 2).
This implies that
r(n) = q
n(n−2)
2 ˜Hn
(
x√q, −s| 1
q
)
. (5.13)
The ﬁrst terms of the sequence ˜Hn(x, s |q) are
1, x, −s + x2, x (−(2 + q)s + x2), (1 + q + q2)s2 − (3 + 2q + q2)sx2 + x4,
x((3 + 4q + 4q2 + 3q3 + q4)s2 − (4 + 3q + 2q2 + q3)sx2 + x4).
From their recurrence relation we see that
˜H2n(0, s |q) = ( −s)n[2n − 1]q!! and ˜H2n+1(0, s |q) = 0 .
