---
doc_id: arxiv-math-0501112v3
doc_title: "GAUSSIAN FLUCTUATIONS OF CHARACTERS OF"
section_id: sec-039-22-piotr-sniady
section_title: "PIOTR ´SNIADY"
section_number: 22
pages: 22-24
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
doc_brief: "GAUSSIAN FLUCTUATIONS OF CHARACTERS OF — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
is the maximal partition with only one block.
Corollary 4.5. Let permutations σ 1, . . . , σ n be disjoint cycles of length
l1, . . . , l n. Then
(4.9) k•(Σ l1 , . . . , Σ ln ) =
∑
π (1),π (2)
kπ (1) (σ 1, . . . , σ n) k•
π (2) (Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
l1 times
, . . . , Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
ln times
),
where the sum runs over all partitions π (1), π (2) of the set {1, . . . , n }such
that π (1) ∨ π (2) =
{
{1, . . . , n }
}
.
Proof. We consider the algebra C(Sq ) ⊗ A• with the usual product on the
ﬁrst factor and the disjoint product on the second one:(a1⊗b1)(a2⊗b2) =
(a1a2) ⊗ (b1 • b2).
For all integers l1, . . . , l n ≥ 1 and disjoint cycles σ 1, . . . , σ n with appro-
priate lengths we clearly have
E
(
Σ l1 • · · · • Σ ln
)
= E
[
(σ 1 ⊗ Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
l1 times
) · · ·(σ n ⊗ Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
ln times
)
]
,
where the product on the left-hand side is taken inA• and the product on the
right-hand side is taken in C(Sq ) ⊗ A•. In other words: the mixed moments
of the family of random variables (Σ li ) coincide with the mixed moments
of the family (σ i ⊗ Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
li times
). It follows that corresponding cumulants are
equal:
k•(
Σ l1 , . . . , Σ ln
)
= k(σ 1 ⊗ Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
l1 times
, . . . , σ n ⊗ Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
ln times
).
We use now Theorem 4.4 to compute the right-hand side which ﬁnishes the
proof. □
In applications of this result we will ﬁnd useful the following lemma.
Lemma 4.6. Let π = {π 1, . . . , π m }be a partition which contributes to the
right-hand side of (4.8). Then
∑
i
(
|π i|− 1
)
≥ n − 1.
Let π (k) = {π (k)
1 , . . . , π (k)
m (k)}for k ∈ {1, 2 }be partitions which contribute
to the right-hand side of (4.9). Then
∑
i
(
|π (1)
i |− 1
)
+
∑
i
(
|π (2)
i |− 1
)
≥ n − 1.
GAUSSIAN FLUCTUATIONS OF CHARACTERS OF SYMMETRIC GROUPS 23
Proof. Partition π can be obtained from the trivial partition (every block
consists of exactly one element) by performing ∑
i
(
|π i|− 1
)
times the
following operation: we select two blocks and merge them int o a single
one. Clearly, the number of blocks of partition
π ∨
{
{i1 + 1, i 1 + 2, . . . , i 2}, . . . , {in + 1, i n + 2, . . . , i n+1}
}
either decreases by one or stays the same in each step. The ini tial number
of blocks is equal to n and the ﬁnal number of blocks is equal to 1, which
ﬁnishes the proof.
The proof of the second statement is analogous and we skip it. □
Corollary 4.7. Let X be a set of generators of the algebra of conjugacy
classes A. Suppose that
(4.10) k(a1, . . . , a n)q− deg a1 +···+deg an − 2(n− 1)
2 = O(1)
holds true for all n ≥ 1 and a1, . . . , a n ∈ X. Then (4.10) holds true for all
n ≥ 1 and a1, . . . , a n ∈ A.
Proof. Clearly, it is enough to consider the case whena1, . . . , a n are mono-
mials in elements ofX. In order to estimate each summand on the right-hand
side of (4.8) we apply Lemma 4.6. □
Remark. Note that the above Corollary holds true also when the cumulants
k are replaced by k•. In particular, this Corollary can be applied for (3.2)
and (3.3).
4.6. Proof of the main theorem: equivalence (3.2) ⇐ ⇒(3.3).
Proof of the implication (3.2) =⇒ (3.3). Our goal is to use Proposition 4.1
in order to express k•(Σ l1 , . . . , Σ ln ) in terms of the cumulants kid and k•.
To estimate a summand on the right-hand side of (4.4) corresp onding to a
partition π = {π 1, . . . , π m }of {1, . . . , n }we use Theorem 4.3 and get
deg kid(xi : i ∈ π j) ≤
( ∑
i∈π j
deg xi
)
− 2(|π j|− 1).
Thus
(4.11)( ∑
1≤j≤m 
deg kid(xi : i ∈ π j)
)
− 2(m − 1) ≤
( ∑
i
deg xi
)
− 2(n − 1).
Assumption (3.2) and Corollary 4.7 show that
k•[
kid(xi : i ∈ π j) : j = 1, 2, . . .
]
q
−
∑ 
j deg kid(xi :i∈π j )+ 2(m− 1)
2 = O(1).
Now (4.11) ﬁnishes the proof. □
