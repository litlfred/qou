---
doc_id: cjdoubletwistfinal
doc_title: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: page-007
section_title: "Page 7"
section_number: null
pages: 7-7
source_pdf: cJdoubletwistfinal.pdf
source_sha256: a1e18db5232b39f4
toc_source: undetermined
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
---
THE COLORED JONES POLYNOMIAL FOR DOUBLE TWIST KNOTS
7
Consider the family of 2-bridge knots b(l, t) [5]. The main result in [28] is an explicit formula
for the colored Jones polynomial of b(l, t)∗.
Theorem 2.1. We have
JN(b(l, t)∗; q) =
X
N−1≥np′≥...≥n1≥0
qa(n)N+b1(n)+b2(n)X(n)
(2.3)
where2
a(n) = −1
2
p′
X
j=1
 
p′
X
k=r′(j)
(σik + σip′+1−k)
!
(nj −nj−1) −1
2
p′−1
X
j=1
(σj+1 + σp′+1−j)nj
−1
2(σp′ + 1)np′ −
p′
X
j=1
σj,
b1(n) = −a(n) +
l−t
2
X
k=1
1 −σik
2
nik−1 −
p′
X
k= l−t
2 +1
nik−1 +
p′
X
k= l−t
2 +1
1 + σik
2
nik −(1 + σp′)np′
+ 1
2
p′−1
X
j=1
(σj+1 −σj)nj
−1
2
p′−1
X
k=1
p′
X
k′=k+1
1 + sgn(ik −ik′)
2
(σik −σik′)(nik −nik−1)(nik′ −nik′−1)
+
p′
X
j=1
σj
r′(j)
X
k=1
(nik −nik−1)

nj−1,
b2(n) =

















t−1
2
X
k= l−t
2 +1
1 + σik
2
nik−1
if l < 2t
−
l−t
2
X
k= t+1
2 +1
1 + σik
2
nik−1
if l > 2t,
X(n) = (−1)np′qκ(p′) (q)N−1(q)np′
(q)N−np′−1
p′
Y
j=1
τ(j)
(q)nj−nj−1
.
As the mirror image of the torus knots T(2,2t+1) is b(2t + 1, 1) (cf.
[5, 26, 29]), one can
check that Theorem 2.1 recovers the q-hypergeometric expression for JN(T(2,2t+1); q) given in
[14, 15].
Our interest will be to apply Theorem 2.1 to the case of the double twist knots
K(m,p) = b(4mp −1, 4mp −2p −1) and K(m,−p) = b(4mp + 1, 4mp −2p + 1) (cf. [29]). In order
to facilitate these computations, we need the following results concerning σj, ik and σik. We
omit the proofs as they are straightforward generalizations of Lemmas 6–9 in [28].
2Note that there is a misprint in the deﬁnition of X(n) in [28]. Each q in the prefactor should be q.
