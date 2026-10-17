---
doc_id: arxiv-math-0501112v3
doc_title: "arXiv:math/0501112v3 [math.CO] 31 May 2005"
section_id: sec-027-5-proof-of-theorem
section_title: "Proof of Theorem"
section_number: 5
pages: 26-27
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
toc_source: inferred
---
This section is devoted to the proof of Theorem 4.3 which is the only
missing component in the proof of the main theorem. We will use some
tools presented in our recent work [´Sni03].
5.1. Cumulants. If µ = {µ1, . . ., µk} is a partition of the set {1, . . ., n}
with blocks µi = {µi,1, . . ., µi,m(i)} we deﬁne partition–indexed cumulants
given by a multiplicative extension of the usual cumulants:
(5.1)
kµ(X1, . . ., Xn) =
Y
i
k(Xµi,1, Xµi,2, . . ., Xµi,m(i));
for example
k{1,3,4},{2,5}(X1, X2, X3, X4, X5) = k(X1, X3, X4) k(X2, X5).
In this article we will use the following property of cumulants: it turns out
that the cumulants are implicitly determined by a sequence of relations
(5.2)
E(X1 · · · Xn) =
X
µ
kµ(X1, . . ., Xn),
where the sum runs over all partitions µ of the set {1, . . ., n}.
5.2. Partition–indexed conjugacy classes. In the following we present
some constructions on partitions of the set X = {1, 2, . . ., N}. However,
it should be understood that by a change of labels these constructions can
be performed for any ﬁnite ordered set X.
We consider a matrix J, the entries of which belong to C(Sq), the sym-
metric group algebra:
J =


0
(1, 2)
. . .
(1, q)
1
(2, 1)
0
. . .
(2, q)
1
...
...
...
...
...
(q, 1)
(q, 2)
. . .
0
1
1
1
. . .
1
0


∈Mq+1(C) ⊗C(Sq).
Except for the last row, the last column and the diagonal, the entry in the
i-th row and the j-th column is equal to the transposition interchanging i
and j.
GAUSSIAN FLUCTUATIONS OF CHARACTERS OF SYMMETRIC GROUPS
27
Let p = (p1, . . ., pl) be a sequence with p1, . . ., pl ∈{1, . . ., q + 1}
and let π be a partition of the set {1, . . ., l}. We say that p ∼π if for any
1 ≤i, j ≤l the equality pi = pj holds if and only if i and j belong to the
same block of the partition π. We deﬁne
(5.3)
Σπ =
X
p∼π
pl=q+1
Jp1p2Jp2p3 · · · Jpl−1plJplp1 ∈C(Sq).
We will treat each summand as a partial permutation with a support
{p1, . . ., pl} \ {q + 1}.
Some partial results concerning expressions of
this form were obtained by Biane [Bia98].
We can show [´Sni03] that
Σπ = Σk1,...,kt for some integers k1, . . ., kt ≥1 which will be presented
explicitly in Section 5.7. For this reason we call Σπ a partition-indexed
conjugacy class.
