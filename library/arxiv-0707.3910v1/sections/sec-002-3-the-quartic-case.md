---
doc_id: arxiv-0707.3910v1
doc_title: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS"
section_id: sec-002-3-the-quartic-case
section_title: "The quartic case"
section_number: 3
pages: 5-7
source_pdf: 0707.3910v1.pdf
source_sha256: ad31f3cba16c4ea4
doc_brief: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS — We present a rational version of the classical Landen transfor- mation for elliptic integrals."
---
In this section we describe the computability of rational functions R ∈Em
4 .
These are functions of the form
R(z)
=
P(z)
(z4 + 2az2 + 1)m+1
where P(z) is an even polynomial of degree 4m+2. Observe that the normalization
a0 = a2 = 1 makes the denominator of R automatically symmetric. It suﬃces to
evaluate
Nn,4(d1; m)
:=
Z ∞
0
z2n dz
(z4 + 2d1z2 + 1)m+1
(3.1)
6
GEORGE BOROS AND VICTOR H. MOLL
where 0 ≤n ≤2m+1 is required for convergence. From (2.4) we have Nn,4(d1; m) =
N2m−1−n,4(d1; m), so we may assume 0 ≤n ≤m. We now employ Theorem 2.1 to
obtain a closed form expression for Nn,4(d1; m).
Theorem 3.1. Let m ∈N and assume 0 ≤n ≤m. Then
Nn,4(d1; m) :=
Z ∞
0
z2n dz
(z4 + 2d1z2 + 1)m+1
=
(3.2)
π
23m+3/2(1 + a)m+1/2 ×
m−n
X
j=0
2j(1 + d1)j ×
2m −2j −1
m −j
m −n + j
2j
2j
j
m
j
−1
.
For m + 1 ≤n ≤2m + 1 we have
Z ∞
0
z2n dz
(z4 + 2d1z2 + 1)m+1
=
(3.3)
π
23m+3/2(1 + d1)m+1/2 ×
n−m−1
X
j=0
2j(1 + d1)j ×
2m −2j −1
m −j
m −n + j
2j
2j
j
m
j
−1
.
Proof. We apply the result of the Theorem 2.1 with D1(d1; z) = z4 + 2d1z2 + 1 and
E1(d1; z) = (1 + d1)z2 + 2, so that
Z ∞
0
z2n dz
(z4 + 2d1z2 + 1)m+1
=
2−m
m−n
X
j=0
4j
m −n + j
2j
 Z ∞
0
z2(m−j) dz
((1 + d1)z2 + 2)m+1 .
The change of variable u = (1 + d1)z2/2 then yields
Z ∞
0
z2(m−j) dz
( (1 + d1)z2 + 2 )m+1
=
2−(j+3/2)(1 + d1)−m+j−1/2
Z ∞
0
um−j−1/2 du
(1 + u)m+1
=
π
2m −2j
m −j
2j
j
m
j
−1
2−(2m+j+3/2)(1 + d1)−(m−j+1/2),
where we have used
Z ∞
0
ur−1/2
(1 + u)s du
=
π
22(s−1)
2r
r
2(s −r −1)
s −r −1
s −1
r
−1
.
□
The algorithm also requires a scaled version of N0,4(d1; m).
Corollary 3.2. Let b > 0, c > 0, a > −
√
bc, m ∈N, and 0 ≤n ≤m. Deﬁne
Nn,4(a, b, c; m)
:=
Z ∞
0
z2n dz
(bz4 + 2az2 + c)m+1 .
Then for 0 ≤n ≤m,
Nn,4(a, b, c; m)
=
π

c(c/b)m−n n
8(a +
√
bc)
o2m+1−1/2
×
×
m−n
X
k=0
2k
2m −2k
m −k
m −n + k
2k
2k
k
m
k
−1  a
√
bc
+ 1
k
,
(3.4)
LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS
7
and for m + 1 ≤n ≤2m + 1,
Nn,4(a, b, c; m)
=
π

c(c/b)m−n n
8(a +
√
bc)
o2m+1−1/2
×
×
n−m−1
X
k=0
2k
2m −2k
m −k
m −n + k
2k
2k
k
m
k
−1  a
√
bc
+ 1
k
.
(3.5)
Proof. Let 0 ≤n ≤m. The substitution u = z(b/c)1/4 yields
Nn,4(a, b, c; m)
=
1
cm−n/2+3/4bn/2+1/4 Nn,4
 a
√
bc
; m

,
(3.6)
so (3.4) then follows from Theorem 3.1.
From (2.4) we have Nn,4(a, b, c; m) =
N2m+1−n,4(c, b, a; m) for m + 1 ≤n ≤2m + 1, giving (3.5).
□
