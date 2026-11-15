---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-015
section_title: "Page 15"
section_number: null
pages: 15-15
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
§3. The elements p#
k
Let Sn be the symmetric group of degree n. Recall that both irreducible charac-
ters and conjugacy classes of Sn are indexed by the same set, the set of partitions
of n or, equivalently, of Young diagrams with n boxes. We denote this set by Yn .
For λ, ρ ∈Yn , we denote by χλ the irreducible character of Sn indexed by λ, and
by χλ
ρ the value of χλ on the conjugacy class indexed by ρ.
In particular, the partition ρ = (1n) = (1, . . ., 1) corresponds to the trivial
conjugacy class {e} ⊂Sn , so that χλ
(1n) equals the dimension of χλ; we denote this
number by dim λ.
Deﬁnition 3.1. For k = 1, 2, . . ., let p#
k be following function on Y:
p#
k (λ) =



n↓k ·
χλ
(k,1n−k)
dim λ
,
n := |λ| ≥k,
0,
n < k,
where
n↓k = n(n −1) . . .(n −k + 1)
and
(k, 1n−k) = (k, 1, . . ., 1) ∈Yn .
Proposition 3.2. For any k = 1, 2, . . . and any λ ∈Y, p#
k (λ) equals the coeﬃcient
of z−1 in the expansion of the function
−1
k (z −1
2)↓k
Φ(z; λ)
Φ(z −k; λ)
(3.1)
in descending powers of z about the point z = ∞.
Proof. First, assume n < k. Then, by the deﬁnition, p#
k (λ) = 0, and we have to
prove that the coeﬃcient in question equals 0, too. It suﬃces to prove that (3.1) is
a polynomial in z. By Proposition 1.2, (3.1) equals
−1
k (z −1
2)↓k
d
Y
i=1
z + bi
z −ai
·
d
Y
j=1
z −aj −k
z + bj −k .
Note that ai̸ = k −bj for any i, j = 1, . . ., d, because ai + bj ≤n < k. Therefore,
all the factors z −ai and z + bj −k = z −(k −bj) are pairwise distinct. Each of
them cancels with one of the factors in the product (z −1
2)↓k, because
ai, k −bj ∈{ 1
2, 3
2, . . ., k −1
2}.
This concludes the proof in the case n < k.
Now we shall assume n ≥k. Then we use a formula due to Frobenius (see [Ma,
Ex. I.7.7]) which says that p#
k (λ) equals the coeﬃcient of z−1 in the expansion of
the function
F(z) = −1
k z↓k
n
Y
i=1
z −λi −n + i −k
z −λi −n + i
15
