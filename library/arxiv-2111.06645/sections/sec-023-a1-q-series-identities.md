---
doc_id: arxiv-2111.06645
doc_title: "Knots and Their Related $q$-Series"
section_id: sec-023-a1-q-series-identities
section_title: "A.1 q-series identities"
section_number: null
pages: 26-27
source_pdf: 2304.09377v2.pdf
source_sha256: 76ae6c6058f4a9f9
toc_source: outline
doc_brief: "Knots and Their Related $q$-Series — We discuss a matrix of periodic holomorphic functions in the upper and lower half-plane which can be obtained from a factorization of an Andersen–Kashaev state"
---
q-series identities
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
,
(A.1)
which may be found for instance in [53], where we abbreviate (q)n = (q; q)n. If we sum over m
using (A.17) we find
X
m,n≥0
(−1)m+n q
1
2 m2+mn+ 1
2 n2+ 1
2 m+ 1
2 n
(q)m(q)n
=
X
n≥0
(−1)n q
1
2 n2+ 1
2 n
(q)n
(qn+1)∞= (q; q)∞
X
n≥0
(−1)n q
1
2 n2+ 1
2 n
(q)2n
.
Equation (A.1) with m = n gives
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
(−1)m+n q
1
2 m2+mn+ 1
2 n2+ 1
2 m+ 1
2 n
(q)m(q)n
= (q; q)∞
X
n≥0
(−1)nq
1
2 n2+ 1
2 n X
r,s≥0
r+s=n
qr2
(q)2r(q)s
which we can also write as
(q; q)∞
X
r,s≥0
(−1)r+s q
3
2 r2+rs+ 1
2 s2+ 1
2 r+ 1
2 s
(q)2r(q)s
.
Summing over s and using (A.17) with x = qr, we get that this equals to
(q; q)∞
X
r≥0
(−1)r q
3
2 r2+ 1
2 r
(q)2r
(qr+1)∞= (q; q)2
∞
X
r≥0
(−1)r q
3
2 r2+ 1
2 r
(q)3r
.
This concludes the proof of (2.6).
■
