---
doc_id: arxiv-2104.06067v1
doc_title: "ON IRREDUCIBLE CHARACTERS OF THE IW AHORI-HECKE ALGEBRA IN TYPE A"
section_id: sec-002-4-determinant-type-murnaghan-nakayama-rule
section_title: "Determinant type Murnaghan-Nakayama rule"
section_number: 4
pages: 12-17
source_pdf: 2104.06067v1.pdf
source_sha256: 750303181ca019ba
doc_brief: "ON IRREDUCIBLE CHARACTERS OF THE IWAHORI-HECKE ALGEBRA IN TYPE A — We use vertex operators to compute irreducible characters o f the Iwahori-Hecke algebra of type A."
---
The Murnaghan-Nakayama rule is an iterative formula to comp ute the Hecke algebra characters.
The combinatorial rule was proved by Ram [18] using the Frobe nius formula and the Hall-Littlewood
symmetric functions. In this section, we formulate a determ inant type Murnaghan-Nakayama rule and
use it to compute the characters and also give a new proof of th e Murnaghan-Nakayama rule.
For two partitions µ ⊂ λ, the set-theoretic diﬀerence θ = λ − µ is called a skew diagram denoted by
λ/µ. A subset ξ of θ is connected if any two squares in θ are connected by a path in ξ. The connected
12
components, themselves skew diagrams, are by deﬁnition the maximal connected subsets of θ. A skew
diagram λ/µ is a vertical (resp. horizontal) strip if each row (resp. col umn) contains at most one box.
A skew diagram θ is a border strip if it contains no 2 × 2 blocks of squares and is connected (see [15]).
If the border strip θ = λ − µ has m connected components ( ξ1, ξ2, . . . , ξm), we deﬁne the weight of θ
by
wt(θ; t) = ( t − 1)m−1
m∏
i=1
(−1)r(ξi)−1tc(ξi)−1.
where the r(ξi) (resp. c(ξi)) means the number of rows (resp. columns) in the border stri p ξi. Usually
we refer θ as a broken border strip to emphasize the non-connectedness of θ.
Let λ ⊢ n. A Young tableau of shape λ is an assignment of numbers 1 , 2, . . . , n into the dots of the
Young diagram. A tableau is standard if its rows and columns are increasing sequences. Let f λ be
the number of standard tableau of shape λ and let λ− be a partition obtained by removing an inner
corner of λ, then [20]
f λ =
∑
λ −
f λ −
.(4.1)
Recall from (2.19), for a ﬁxed partition λ with l = l(λ) we have that
q∗
kSλ .1 =
∑
τ1, . . . , τ l ≥ 0
|τ | = k
(1 − t)l−∑ δτi, 0Sλ −τ .1.(4.2)
For any composition τ ⊨ k, Sλ −τ .1 = sg(σ)Sµ .1 if λ − τ + δ is strict and µ = σ(λ − τ + δ) − δ for
some permutation σ ∈ Sl, otherwise Sλ −τ .1 = 0. Note that µ must be a partition ⊂ λ with weight
|λ| − k if Sλ −τ .1 ⁄= 0. In fact, note that µi = λσ (i) − τσ (i) + i − σ(i) for some permutation σ that sends
λ − τ + δ into partition µ. If j = σ(i) ≥ i, then λi − µi = λi − λj + τj − i + j ≥ 0. If j = σ(i) < i, we
claim that λi − µi ≥ 0 otherwise λi − µi = λi − λj + τj − i + j < 0, then
(λj − τj, λj+1 − τj+1, . . . , λi − τi) + (i − j, . . . ,1, 0) = ( λj − τj + i − j, . . . , λi − τi).
Observe that ( λi − τi) − (λj − τj + i − j) < 0 so σ cannot send i to j, which is a contradiction!
Conversely, for any µ ⊢ |λ| − k and any σ ∈ Sl, the l-tuple
(λ1 − µσ (1) − 1 + σ(1), λ2 − µσ (2) − 2 + σ(2), · · · , λl − µσ (l) − l + σ(l))
13
is a composition of k provided that λi − µσ (i) + i − σ(i) ≥ 0. Then sg(σ)Sµ .1 = Sλ −τ .1 for τi =
λi − µσ (i) − i + σ(i). Therefore (4.2) can be rewritten as:
q∗
kSλ .1 =
∑
µ
∑
σ ∈ Sl
λ i − i − µ σ (i) + σ (i) ≥ 0
sgn(σ)(1 − t)
l−∑ δλ i−i−µ σ (i)+σ (i), 0
Sµ .1
= (1 − t)l∑
µ
det(δλ i−i≥µ j −j(1 − t)−δλ i−i,µ j −j )Sµ .1
where the sum is over all partitions µ ⊂ λ such that | λ/µ |= k.
For partitions µ ⊂ λ and |λ/µ| = k, consider the l(λ) × l(λ)-matrix
M (λ/µ; t) = ( δλ i−i≥µ j−j(1 − t)−δλ i−i,µ j −j )
where δa≥b = 1 if a ≥ b and δa≥b = 0 otherwise. Then we have proven the following theorem.
Theorem 4.1. Let λ = (λ1, . . . , λl) be a partition and k be a positive integer. Then one has
q∗
kSλ .1 =
∑
µ
(1 − t)l det M (λ/µ; t)Sµ .1(4.3)
where the sum is over all partitions µ ⊂ λ such that | λ/µ |= k.
The matrix M (λ/µ; t) has the following properties: (i) if M (λ/µ; t)ij = 1
1−t , then all entries in
the southwest region to the ( i, j)-entry are zero; (ii) if M (λ/µ; t)ij = 0, then all entries down the
jth column are also zero; and (iii) if M (λ/µ; t)ij = 1, then all entries in the northeast region to the
(i, j)-entry are also 1. et’s divide λ/µ into several cases:
Case 1 : If λ/µ is a k-border strip with the initial box at the rth row, then M (λ/µ; t) has the
following form:




















1
1−t · · · 1 1 1 · · · 1 1
.
.
. . . . .
.
. .
.
. .
.
. · · · .
.
. .
.
.
0 · · · 1
1−t 1 1 · · · 1 1
0 · · · 0 1 1 · · · 1 1
0 · · · 0 1
1−t 1 · · · 1 1
0 · · · 0 0 1
1−t · · · 1 1
.
.
. .
.
. .
.
. .
.
. .
.
. . . . .
.
. .
.
.
0 · · · 0 0 0 · · · 1
1−t 1




















l×l
=

M0 ∗
0 M1

 ,
det(λ/µ; k) = (1 − t)−r+1( −t
1 − t )l−r
14
where M0 is an ( r − 1) × (r − 1) upper-triangular matrix with 1
1−t on the diagonal and M1 is a
(l − r + 1) × (l − r + 1) quasi upper-triangular matrix with 1 on the diagonal and 1
1−t on the (lower)
secondary diagonal. For simplicity we denote M1 by M (ξ; t), where ξ is the border strip obtained from
λ/µ by removing the initial empty boxes.
Case 2 : If λ/µ is connected and contains a 2 × 2 block of boxes, then det( λ/µ; t) = 0. This can be
seen as follows. Without loss of generality, suppose ht(λ/µ) = l(λ) − 1 and the 2 × 2 block appear at
the r-th and ( r + 1)-th rows (1 ≤ r ≤ l − 1), then M (λ/µ; t) has the following form:
M (λ/µ; t) =


























r − 1 r
1 1 · · · 1 1 · · · 1 1
1
1−t 1 · · · 1 1 · · · 1 1
0 1
1−t · · · 1 1 · · · 1 1
.
.
. .
.
. . . . .
.
. .
.
. . . . .
.
. .
.
.
r 0 0 · · · 1
1−t 1 · · · 1 1
r + 1 0 0 · · · 0 1 · · · 1 1
.
.
. .
.
. . . . .
.
. .
.
. . . . .
.
. .
.
.
0 0 0 0 0 · · · 1
1−t 1


























, det(λ/µ; t) = 0 .
Case 3 : If λ/µ has two connected components ξ1, ξ2, then M (λ/µ; t) is a 2 × 2 upper-triangular
block matrix with the diagonal blocks corresponding to ξ1, ξ2. If one of the components contains a
2×2-block of boxes, then det( λ/µ; t) = 0. Suppose each ξi is a border strip and there are ri unoccupied
rows immediately above ξi on the border of λ, then M (λ/µ; t) has the following form:
M (λ/µ; t) =

M1 ∗
0 M2

 , det Mi = (1 − t)−ri+1( −t
1 − t )ht(ξi)−1,
where each Mi is a 2 × 2 block diagonal matrices speciﬁed in case one.
In general, if λ/µ has m connected components ξ1, ξ2, · · · , ξm, then det M (λ/µ; t) = 0 unless each
ξi is a border strip. Then
M (λ/µ; t) =








M1 ∗ · · · ∗
0 M2 · · · ∗
0 .
.
. · · · .
.
.
0 0 .
.
. Ms








15
where the diagonal blocks are either 1
1−t or the quasi upper-triangular matrix M (ξj; t), i = 1, 2, . . . , s; j =
1, 2 . . . , m. It is clear that the number of 1
1−t on the diagonal is equal to Card {λi = µi | i = 1, . . . , l} =
l −∑
j
r(ξj) and the order of M (ξj; k) is equal to r(ξj), j = 1, 2, . . . , m. Therefore,
det(λ/µ; t) = ( 1
1 − t )l−∑ r(ξi)
m∏
i=1
det(ξi; t)
= ( 1
1 − t )l−∑ r(ξi)
m∏
i=1
( −t
1 − t )r(ξi)−1
= (1 − t)m−l
m∏
i=1
(−t)r(ξi)−1.
Thus we have proved the following result.
Corollary 4.2. Let λ be a partition and k a positive integer. Then one has that
q∗
kSλ .1 =
∑
µ
(1 − t)C(λ/µ )
C(λ/µ )∏
i=1
(−t)r(ξi)−1Sµ .1(4.4)
where the sum runs through all partitions µ ⊂ λ such that λ/µ is a k-broken border strip. Here
ξ1, . . . , ξC(λ/µ ) are the connected components of λ/µ.
Remark 4.3. If k = |λ| = n in Corollary 4.2, then q∗
kSλ .1 = 0 unless λ is a hook. In this case,
q∗
nS(m, 1n−m).1 = (1 − t)(−t)n−m. So for all λ ⊢ n ≥ 1,
gλ
(n)(t) =





0, if λ is not a hook
(1 − t)(−t)n−m, if λ = (m, 1n−m).
Similarly, when k = 1 , then q∗
1Sλ .1 = (1 − t)∑
λ −
Sλ −.1, where λ− runs through all partitions obtained
from λ by removing an inner corner. Therefore,
gλ
(1n)(t) = (1 − t)
∑
λ −
gλ −
(1n−1)(t).
By (4.1) it follows that,
gλ
(1n)(t) = (1 − t)nf λ
where f λ is the number of standard tableau of shape λ.
We now present a new proof of the Murnaghan-Nakayama rule for Hn(q) [18] (cf. [7, 8]).
16
Theorem 4.4. (The Murnaghan-Nakayama rule for Hn(q)) Let µ be a partition and k a positive
integer. Then one has that
˜qkSµ .1 =
∑
λ
wt(λ/µ; q)Sλ .1,(4.5)
where the sum is over all partitions λ ⊃ µ such that λ/µ is a k-broken border strip.
Proof. By Corollary 4.2 and duality, it is enough to check that
(1 − t)m
m∏
i=1
(−t)r(ξi)−1 = tk−1(1 − t)wt(λ/µ; t)
where λ/µ is a k-broken border strip with m connected components ξ1, . . . , ξm. Suppose | ξi |= ki,
then∑
i ki = k. Since ξi is a border strip, r(ξi) + c(ξi) = ki + 1, i = 1, 2, . . . , m. Therefore,
tk−1(1 − t)wt(λ/µ; t) = (1 − t)mtk−m
m∏
i=1
(−1)r(ξi)−1t1−c(ξi)
= (1 − t)m
m∏
i=1
(−1)r(ξi)−1tki−c(ξi)
= (1 − t)m
m∏
i=1
(−t)r(ξi)−1.
□
