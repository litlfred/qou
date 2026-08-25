---
doc_id: cjdoubletwistfinal
doc_title: "THE COLORED JONES POL YNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: sec-004-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 6-7
source_pdf: cJdoubletwistfinal.pdf
source_sha256: a1e18db5232b39f4
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
---
a discussion of the generalized Kontsevich-Zagier functions and the generalized U-functions for
the torus knots T(2,2t+1), along with some related questions.
2. Preliminaries
We begin by recalling the setup from [28]. Let l andt be coprime odd integers with l>t ≥ 1
and p′ := l−1
2 . For 1 ≤ j≤ p′, deﬁne integers r(j) such that r(j)≡ (2j− 1)t (mod 2l) and
−l < r(j) < l. We put σj := (−1)⌊ (2j−1)t
l ⌋, r′(j) := |r(j)|+1
2 and ir′(j) = j (and thus ik = j if
and only if r′(j) = k). For an integer i, sgn(i) denotes the sign of i. Let n = (n1,...,n p′) and
ns = 0 for s≤ 0. Finally, deﬁne
κ(p′) =
{
−Nnp′ if σp′ =−1,
0 if σp′ = 1 (2.1)
and
τ(j) =
{
(−1)nj−nj−1 if σj =−1,
q(
nj−nj−1+1
2 ) if σj = 1. (2.2)
THE COLORED JONES POLYNOMIAL FOR DOUBLE TWIST KNOTS 7
Consider the family of 2-bridge knots b(l,t ) [5]. The main result in [28] is an explicit formula
for the colored Jones polynomial of b(l,t )∗.
Theorem 2.1. We have
JN(b(l,t )∗;q) =
∑
N−1≥np′≥...≥n1≥0
qa(n)N+b1(n)+b2(n)X(n) (2.3)
where2
a(n) =−1
2
p′
∑
j=1
( p′
∑
k=r′(j)
(σik +σip′+1−k)
)
(nj−nj−1)− 1
2
p′−1∑
j=1
(σj+1 +σp′+1−j)nj
− 1
2(σp′ + 1)np′−
p′
∑
j=1
σj,
b1(n) =−a(n) +
l−t
2∑
k=1
1−σik
2 nik−1−
p′
∑
k= l−t
2 +1
nik−1 +
p′
∑
k= l−t
2 +1
1 +σik
2 nik− (1 +σp′)np′
+ 1
2
p′−1∑
j=1
(σj+1−σj)nj
− 1
2
p′−1∑
k=1
p′
∑
k′=k+1
1 + sgn(ik−ik′)
