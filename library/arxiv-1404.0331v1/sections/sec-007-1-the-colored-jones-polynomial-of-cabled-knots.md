---
doc_id: arxiv-1404.0331v1
doc_title: "THE STRONG AJ CONJECTURE FOR CABLES OF TORUS KNOTS ANH T. TRAN"
section_id: sec-007-1-the-colored-jones-polynomial-of-cabled-knots
section_title: "The Colored Jones polynomial of cabled knots"
section_number: 1
pages: 3-4
source_pdf: 1404.0331v1.pdf
source_sha256: 53d7ce3afaf405e1
doc_brief: "THE STRONG AJ CONJECTURE FOR CABLES OF TORUS KNOTS ANH T. TRAN — The AJ conjecture, formulated by Garoufalidis, relates the A-poly nomial and the colored Jones polynomial of a knot in the 3-sphere."
---
By [Mo], the formula for the colored Jones polynomial of the ( r, s)-cabled knot K (r,s )
over a knot K is given by
(1.1) JK (r,s)(n) = t− rs(n2− 1)
n− 1
2∑
j=− n− 1
2
t4rj (js+1)JK(2sj + 1).
Lemma 1.1. One has
JK (r,s)(n + 2) − t− 4rs(n+1)JK (r,s)(n)
= t− 2rs(n+1) (
t2r(n+1)JK(s(n + 1) + 1) − t− 2r(n+1)JK(s(n + 1) − 1)
)
.
4 ANH T. TRAN
Proof. From Eq. (1.1) we have
JK (r,s)(n + 2) − t− 4rs(n+1)JK (r,s)(n)
= t− rs((n+2)2− 1)
n+1
2∑
j=− n+1
2
t4rj (sj+1)JK(2sj + 1) − t− 4rs(n+1)t− rs(n2− 1)
n− 1
2∑
j=− n− 1
2
t4rj (js+1)JK(2sj + 1)
= t− rs((n+2)2− 1) (
tr(n+1)(s(n+1)+2)JK(s(n + 1) + 1) + tr(n+1)(s(n+1)− 2)JK(−s(n + 1) + 1)
)
.
The lemma follows since JK(−s(n + 1) + 1) = −JK(s(n + 1) − 1). □
Lemma 1.2. One has
JK (r,2)(n + 1) + t− 2r(2n+1)JK (r,2)(n) = t− 2rnJK(2n + 1).
Proof. By Eq. (1.1) we have
JK (r,2)(n + 1) = t− 2r((n+1)2− 1)
n
2∑
k=− n
2
t4rk(2k+1)JK(4k + 1).
Set k = −(j + 1
2). Then
JK (r,2)(n + 1) = t− 2r((n+1)2− 1)
− n+1
2∑
j= n− 1
2
t4rj (2j+1)JK(−(4j + 1))
= t− 2r((n+1)2− 1)
(
−
n− 1
2∑
j=− n− 1
2
t4rj (2j+1)JK(4j + 1) + t2rn(n+1)JK(2n + 1)
)
= −t− 2r(2n+1)JK (r,2)(n) + t− 2rnJK(2n + 1).
This proves Lemma 1.2. □
Remark 1.3. The proofs of Lemmas 1.1 and 1.2 are similar to those of Lemmas 1.1 and
1.5 in [Tr]. See also Propositions 3 and 5 in [Hi], and Lemma 3.1 and Section 6 .1 in [RZ].
