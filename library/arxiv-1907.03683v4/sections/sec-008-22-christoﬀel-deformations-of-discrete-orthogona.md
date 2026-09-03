---
doc_id: arxiv-1907.03683v4
doc_title: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND"
section_id: sec-008-22-christoﬀel-deformations-of-discrete-orthogona
section_title: "Christoﬀel deformations of discrete orthogonal polynomials. Let ω be a discrete"
section_number: 2.2
pages: 6-8
source_pdf: 1907.03683v4.pdf
source_sha256: eb8cc2ddfc8c0739
doc_brief: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND — Christoﬀel deformation of a measure on the real line consists of multipying this measure by a squared polynomial having its roots in R."
---
measure on R with inﬁnite support and ﬁnite moments of all orders:
Z
R
|x|ndω(x) < +∞
for all n ∈N.
We denote by {pn}n∈N a family of orthogonal polynomials with respect to ω. The number
cn stands for the leading coeﬃcient of pn, and its squared norm will be denoted by hn:
pn(x) = cnxn + terms of degree less than n,
Z
R
pn(x)pm(x)dω(x) =
(
0
if n̸ = m,
hn
if n = m
.
Let k be a non-negative integer and let u1,...,uk be pairwise distinct real numbers.
Deﬁnition 2.1. The Christoﬀel deformation ωk of ω of order k at points u1,...,uk is the
discrete measure on R deﬁned by:
dωk(x) =
k
Y
j=1
(x −uj)2dω(x)
Let {pk
n}n∈N be the family of monic orthogonal polynomials with respect to ωk. We have
the following
Proposition 2.1. The following explicit formula holds:
pk
n(x) =
 k
Y
i=1
(x −ui)2.δk
n.cn+2k
!−1
Dk
n(x)
6
where
Dk
n(x) =

pn(u1)
pn+1(u1)
. . .
pn+2k(u1)
...
...
...
...
pn(uk)
. . .
. . .
pn+2k(uk)
p′
n(u1)
p′
n+1(u1)
. . .
p′
n+2k(u1)
...
...
...
...
p′
n(uk)
. . .
. . .
p′
n+2k(uk)
pn(x)
pn+1(x)
. . .
pn+2k(x)

;
δk
n =

pn(u1)
pn+1(u1)
. . .
pn+2k−1(u1)
...
...
...
...
pn(uk)
. . .
. . .
pn+2k−1(uk)
p′
n(u1)
p′
n+1(u1)
. . .
p′
n+2k−1(u1)
...
...
...
...
p′
n(uk)
p′
n+1(uk)
. . .
p′
n+2k−1(uk)

.
Its squared l2(ωk)-norm is given by
hk
n =
hnδk
n+1
δkn.cn+2k.cn
Proof. We slightly adapt the proof from [23], where it is assumed that the ui are outside the
support of the measure ω, to the case when the measure ω has inﬁnite support, see also [34]
and [2]. We ﬁrst prove that δk
n̸ = 0. Let α1, . . . , α2k ∈R be 2k real numbers such that the
polynomial
P(x) :=
2k
X
i=1
αipn+i−1(x)
and its derivative vanish for x ∈{u1, . . . , uk}. Then there exists a polynomial Q of degree
at most or equal to n −1 such that
P(x) = Q(x)
k
Y
i=1
(x −ui)2.
Since the polynomials pn+i−1, i = 1, . . . , 2k are orthogonal to any polynomial of degree less
than or equal to n −1 with respect to ω, we have
Z
R
Q(x)P(x)dω(x) =
Z
R
Q2(x)dωk(x) = 0.
(2)
Since the support of the measure ω is inﬁnite, so is the support of the measure ωk, and thus
Equation (2) implies Q = 0 and so P = 0 i.e. α1 = · · · = α2k = 0. This implies that δk
n̸ = 0.
The fact that δk
n̸ = 0 tells us that Dk
n(x) is a polynomial of degree n + 2k. Since Dk
n(x)
and its derivative vanish for x ∈{u1, . . . , uk}, the rational function pk
n(x) is in facts a monic
polynomial of degree n.
7
Let q(x) be a polynomial of degree strictly less than n. From the orthogonality of the
polynomials pn with respect to ω, we have
Z
R
pk
n(x)q(x)dωk(x) =
1
cn+2kδkn
Z
R
Dk
n(x)q(x)dω(x) = 0,
and the polynomials pk
n are thus orthogonal with respect to ωk. The squared norm hk
n is
computed in [16, Prop. 4.2.].
□
