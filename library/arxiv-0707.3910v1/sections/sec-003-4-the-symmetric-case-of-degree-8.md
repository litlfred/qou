---
doc_id: arxiv-0707.3910v1
doc_title: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS"
section_id: sec-003-4-the-symmetric-case-of-degree-8
section_title: "The symmetric case of degree 8"
section_number: 4
pages: 7-8
source_pdf: 0707.3910v1.pdf
source_sha256: ad31f3cba16c4ea4
doc_brief: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS — We present a rational version of the classical Landen transfor- mation for elliptic integrals."
---
In this section we prove the computability of the set Em,s
8
of symmetric rational
functions with denominator of degree 8 and establish an explicit formula for the
integral
Nn,8(a1, a2; m)
=
Z ∞
0
z2n dz
(z8 + a2z6 + 2a1z4 + a2z2 + 1)m+1
where 0 ≤n ≤4m + 3 is required for convergence. Observe that (2.4) reduces the
discussion to the case 0 ≤n ≤2m + 1. The expression (2.2), with p = 2, produces
E2(a1, a2; z) = (1 + a1 + a2)z4 + 2(a2 + 4)z2 + 8.
Theorem 4.1. Every function in Em,s
8
is computable. More speciﬁcally, deﬁne
c1 := a2 + 4, c2 := 1 + a1 + a2, and
tk,j(m, n; a1, a2)
:=
π2−(3m+2+k+j)/2c(m−k−j)/2
2
(c1 + √8c2)j−m−1/2 ×
×
4m −n −k + 2
k −n
2m −2j
m −j
m −k + j
2j
2j
j
m
j
−1
.
Then for m + 1 ≤n ≤2m + 1, 1 + a1 + a2 > 0 and a2 + 4 > −8
p
8(1 + a1 + a2),
Z ∞
0
z2n dz
(z8 + a2z6 + 2a1z4 + a2z2 + 1)m+1
=
2m+1
X
k=n
k−m−1
X
j=0
tk,j(m, n; a1, a2),
and for 0 ≤n ≤m,
Z ∞
0
z2n dz
(z8 + a2z6 + 2a1z4 + a2z2 + 1)m+1 =
m
X
k=n
m−k
X
j=0
tk,j(m, n; a1, a2) +
2m+1
X
k=m+1
k−m−1
X
j=0
tk,j(m, n; a1, a2).
Proof. The reduction formula yields
Z ∞
0
z2n dz
(z8 + a2z6 + 2a1z4 + a2z2 + 1)m+1 =
23m+2
2m+1
X
k=n
2−2k
4m −n −k + 2
k −n
 Z ∞
0
z2k dz
(c2z4 + 2c1z2 + 8)m+1 .
(4.1)
8
GEORGE BOROS AND VICTOR H. MOLL
We then use Corollary 3.2 to evaluate (4.1).
□
