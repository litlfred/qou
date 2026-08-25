---
doc_id: arxiv-2401.04019v1
doc_title: "TRUNCA TED THET A SERIES RELA TED TO THE JACOBI TRIPLE PRODUCT IDENTITY"
section_id: sec-001-2-preliminaries-and-notation
section_title: "Preliminaries and notation"
section_number: 2
pages: 5-6
source_pdf: 2401.04019v1.pdf
source_sha256: 1a29e52a81639640
doc_brief: "TRUNCATED THETA SERIES RELATED TO THE JACOBI TRIPLE PRODUCT IDENTITY — The work of Andrews and Merca on the truncated Euler’s pen- tagonal number theorem led to a resurgence in research on tru ncated"
---
In this section we discuss some background on partitions and set th e notation
used frequently in the article.
We writeλ ⊢n to mean that λ is a partition of n. We say that λ has size n if the
parts of λ add up to n and write |λ| for the size of λ. The length of λ, denoted ℓ(λ),
is the number of parts in λ. We denote by ℓe(λ) (respectively ℓo(λ)) the number
of even (respectively odd) parts in λ. We also work with vectors of partitions and
write (λ(1),λ (2),...,λ (t)) ⊢ n to mean that λ(1),λ (2),...,λ (t) are partitions with
|λ(1)| + |λ(2)| + · · · + |λ(t)| =n.
We denote by P(n) the set of all partitions of n. In general, if A(n) denotes a set
of partitions of n satisfying certain conditions, we set A := ⋃
n≥0 A(n). Moreover,
iff is a partition counting function, say f (n) = |A(n)|, we use the convention that
f (x) = 0 if x ⁄∈N0. We use the notation N0 for the set of non-negative integers.
The Ferrers diagram of a partition λ = (λ1,λ 2,...,λ ℓ) is an array of left justiﬁed
boxes such that the ith row from the top contains λi boxes. For example, the Ferrers
diagram of λ = (5, 3, 2, 2, 1) is shown below
We abuse notation and write λ to mean a partition, its Ferrers diagram, or its
multiset of parts. We write a ∈ λ to mean the positive integer a is a part of
λ. The number of times a > 0 appears in λ is denoted by mλ(a) and is called
the multiplicity of a in λ. When convenient, we use the frequency notation for
6 CRISTINA BALLANTINE AND BROOKE FEIGON
partitions: the exponent of a part is the multiplicity of the part. For example,
λ = (5 2, 34, 1) is the partitions (5 , 5, 3, 3, 3, 3, 1). We also use the convention that
λj = 0 for all j >ℓ(λ) and set λ0 := ∞.
We deﬁne the following operations on partitions. If λ and µ are partitions, by
λ ∪µ and λ \µ we mean the corresponding operations on the multisets of parts of
λ and µ. Moreover λ \µ is only deﬁned if µ ⊆λ as multisets.
Given an integer R ≥ 2, and a partition λ, the R-modular diagram of λ is a
Ferrers diagram withℓ(λ) rows such that, if λi =qiR+Si forqi ≥ 0 and 0 <S i ≤R,
then the ith row from the top has qi + 1 boxes: the ﬁrst qi boxes are ﬁlled with R
and the last box is ﬁlled with Si. For example, if R = 3 and λ = (10, 9, 8, 8, 7, 3, 2),
the 3-modular diagram of λ is
3 3 3 1
3 3 3
3 3 2
3 3 2
3 3 1
3
2
Given integersR ≥ 2 and 0 <S <R , we denote by P±S,R(n) the set of partitions
of n with parts congruent to ±S modulo R. For j ≥ 1, we denote by δS,R,j the
partition in P±S,R with distinct parts equal to iR +S for 0 ≤i ≤j − 1. If j = 0,
we set δS,R,0 := ∅. The R-modular Ferrers diagram of δS,R,j is a staircase shaped
diagram with j rows, each having S in the last box. For example, the 5-modular
diagram of δ3,5,4 is
5 5 5 3
5 5 3
5 3
3
Moreover, |δS,R,j| = j(j − 1)R/2 +jS . If R is clear from the context, we drop
the subscript R from δS,R,j to write δS,j.
For a partition λ, we write λℓ−i for the (i + 1)st part counted from the last: λℓ
is the last part, λℓ−1 is the second to last part, etc.
Ifr ≥ 2 and 0 ≤s<r we write λs,r for the partitions whose parts are the parts
of λ that are congruent to s modulo r (with the same multiplicity as in λ) and we
set λ±s,r :=λs,r ∪λr−s,r.
We use the customary shorthand notation
(a1,a 2,...,a j;q)∞ := (a1;q)∞(a2;q)∞ · · ·(aj ;q)∞.
