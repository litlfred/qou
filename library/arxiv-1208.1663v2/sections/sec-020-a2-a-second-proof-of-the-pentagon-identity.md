---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES STAVROS GAROUFALIDIS With an appendix by Sander Zwegers"
section_id: sec-020-a2-a-second-proof-of-the-pentagon-identity
section_title: "A.2. A second proof of the pentagon identity"
section_number: null
pages: 26-27
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES STAVROS GAROUFALIDIS With an appendix by Sander Zwegers — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of"
---
of the pentagon identity using
1
(q)m(q)n
=
∑
r,s,t
r+s=m
s+t=n
qrt
(q)r(q)s(q)t
,
qmn
(q)m(q)n
=
∑
r,s,t
r+s=m
s+t=n
(−1)sq
1
2s2− 1
2s
(q)r(q)s(q)t
=
∑
s
(−1)sq
1
2s2− 1
2s
(q)m−s(q)n−s(q)s
.
(A.3)
The ﬁrst identity is well-known [29, Eqn.(13)], and the second follows from the ﬁrst by
replacing q byq−1 and multiplying both sides by (−1)m+nq− 1
2 (m−n)2− 1
2 (m+n).
Using these equations, we will show here that
qe1e2 (−1)n1+n2q
1
2n2
1+ 1
2n2
2+ 1
2n1+ 1
2n2+e2n1+e1n2
(q)n1(q)n2(q)n1+e1(q)n2+e2
=
∑
r1,r2,r3,e3
r1+r3+e3=n1
r2+r3+e3=n2
(−1)r1+r2+r3q
1
2r2
1+ 1
2r2
2+ 1
2r2
3+ 1
2r1+ 1
2r2+ 1
2r3+e3
(q)r1(q)r1+e1+e3(q)r2(q)r2+e2+e3(q)r3(q)r3+e3
.(A.4)
The sum on the right actually only has a ﬁnite number of non-zero terms, so there is no
issue with convergence. If we multiply both sides with xn1
1 xn2
2 and sum over all n1 and n2,
then we again ﬁnd
qe1e2Fe1(qe2x1)Fe2(qe1x2) =
∑
e3
(x1x2q)e3Fe1+e3(x1)Fe2+e3(x2)Fe3(x1x2).
To prove (A.4) we use Equations (A.3) which give
q(n1+e1)(n2+e2)
(q)n1(q)n2(q)n1+e1(q)n2+e2
=
∑
r1,r2,r3,e3
r1+e3=n1
r2+e3=n2
(−1)r3q
1
2r2
3− 1
2r3+r1r2
(q)r1(q)r2(q)n1+e1−r3(q)n2+e2−r3(q)r3(q)e3
.
THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES 27
Replacing e3 bye3 +r3 in this sum we get
q(n1+e1)(n2+e2)
(q)n1(q)n2(q)n1+e1(q)n2+e2
=
∑
r1,r2,r3,e3
r1+r3+e3=n1
r2+r3+e3=n2
(−1)r3q
1
2r2
3− 1
2r3+r1r2
(q)r1(q)r2(q)n1+e1−r3(q)n2+e2−r3(q)r3(q)r3+e3
=
∑
r1,r2,r3,e3
r1+r3+e3=n1
r2+r3+e3=n2
(−1)r3q
1
2r2
3− 1
2r3+r1r2
(q)r1(q)r2(q)r1+e1+e3(q)r2+e2+e3(q)r3(q)r3+e3
.
Now multiplying both sides by (−1)n1+n2q
1
2 (n1−n2)2+ 1
2n1+ 1
2n2 gives Equation (A.4).
