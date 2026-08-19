---
doc_id: arxiv-2111.06645
doc_title: ""
section_id: sec-019-a1-q-series-identities
section_title: "A.1 q-series identities"
section_number: null
pages: 26-27
source_pdf: 2304.09377v2.pdf
source_sha256: 76ae6c6058f4a9f9
doc_brief: "Knots and Their Related q-Series — We discuss a matrix of periodic holomorphic functions in the upper and lower half-plane which can be obtained from a factorization of an Andersen–Kashaev state"
---
We begin by giving the proof of the two identities of equation (2.6), as communicated to us by
Sander Zwegers. We will use the identity (A.17) and
1
(q)m(q)n
=
X
r,s,t≥0
r+s=m,s+t=n
qrt
(q)r(q)s(q)t
, (A.1)
which may be found for instance in [53], where we abbreviate ( q)n = (q;q)n. If we sum over m
using (A.17) we find
X
m,n≥0
(−1)m+nq
1
2m2+mn+ 1
2n2+ 1
2m+ 1
2n
(q)m(q)n
=
X
n≥0
(−1)nq
1
2n2+ 1
2n
(q)n
(qn+1)∞ = (q;q)∞
X
n≥0
(−1)nq
1
2n2+ 1
2n
(q)2n
.
Knots and Their Related q-Series 27
Equation (A.1) with m =n gives
1
(q)2n
=
X
r,s,t≥0
r+s=n,s+t=n
qrt
(q)r(q)s(q)t
=
X
r,s≥0
r+s=n
qr2
(q)2r(q)s
,
and so
X
m,n≥0
(−1)m+nq
1
2m2+mn+ 1
2n2+ 1
2m+ 1
2n
(q)m(q)n
= (q;q)∞
X
n≥0
(−1)nq
1
2n2+ 1
2n X
r,s≥0
r+s=n
qr2
(q)2r(q)s
which we can also write as
(q;q)∞
X
r,s≥0
(−1)r+sq
3
2r2+rs+ 1
2s2+ 1
2r+ 1
2s
(q)2r(q)s
.
Summing over s and using (A.17) with x =qr, we get that this equals to
(q;q)∞
X
r≥0
(−1)rq
3
2r2+ 1
2r
(q)2r
(qr+1)∞ = (q;q)2
∞
X
r≥0
(−1)rq
3
2r2+ 1
2r
(q)3r
.
This concludes the proof of (2.6). ■
