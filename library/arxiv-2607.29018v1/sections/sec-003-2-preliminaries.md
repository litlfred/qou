---
doc_id: arxiv-2607.29018v1
doc_title: "The Aldous property for normal Cayley graphs on symmetric groups"
section_id: sec-003-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 7-8
source_pdf: 2607.29018v1.pdf
source_sha256: 789faa122dd32290
toc_source: inferred
doc_brief: "The Aldous property for normal Cayley graphs on symmetric groups — Aldous’ spectral gap conjecture states that the random walk and the interchange process on any connected graph have the same"
---
and Corollary 1.5 in Section 4. To prove Theorem 1.6, we first need to determine all normal
Cayley graphs on Sn that are line graphs (see Theorem 5.1). Using this and the classifica-
tion [31] of connected regular graphs with second largest eigenvalue at most 1, we obtain a
classification of all normal Cayley graphs on Sn whose strictly second largest eigenvalue is
at most 1 (see Theorem 5.5). With the help of this classification, which is of interest for its
own sake, we prove Theorem 1.6 and Corollary 1.7 in Section 6.
2
Preliminaries
The reader is referred to [18, 19, 29, 32] for general representation theory and [28] for sym-
metric groups and their representations. A partition of a positive integer n is a sequence of
positive integers γ = (γ1, γ2, . . . , γm) such that γ1 ≥γ2 ≥· · · ≥γm and n = γ1+γ2+· · ·+γm.
We write γ ⊢n to indicate this partition of n, and let ci(γ) denote the number of parts of
γ which are equal to i. The sign of a permutation σ ∈Sn, denoted by sgn(σ), is defined
to be 1 if σ is an even permutation and −1 if σ is an odd permutation. Every permutation
σ ∈Sn decomposes into disjoint cycles; the cycle type of σ is the partition of n whose parts
are the lengths of these cycles. It is well known that two elements of Sn are conjugate if and
only if they have the same cycle type. Thus, the conjugacy classes of Sn are determined by
their cycle types and thus correspond to the partitions of n. For a partition γ ⊢n, denote by
C(Sn, γ) the corresponding conjugacy class of Sn. Note that c1(γ) = |fix(σ)| is the number
of fixed points of each σ ∈C(Sn, γ). Define sgn(γ) = 1 if the permutations in C(Sn, γ) are
even, and sgn(γ) = −1 otherwise.
For each partition ζ ⊢n, let ρζ denote the corresponding Specht module in c
Sn. The
Specht modules ρ(n), ρ(1n) and ρ(n−1,1) are called the trivial representation, sign representation
and standard representation of Sn, respectively. We denote the character and normalized
character of ρζ by χζ(·) and ˜χζ(·), respectively. Since they are class functions on Sn, we
write χζ(γ) and ˜χζ(γ) for their values on the conjugacy class C(Sn, γ). It is well known
that χ(n)(σ) = ˜χ(n)(σ) = 1 and χ(1n)(σ) = ˜χ(1n)(σ) = sgn(σ) for every σ ∈Sn. Note that
χζ(e) = dim ρζ is the dimension of ρζ ∈c
Sn for any ζ ⊢n.
In view of (1), for a normal Cayley graph Cay(Sn, S) and a partition ζ ⊢n, we use
λζ(Cay(Sn, S)), or λζ for short, to denote its eigenvalue corresponding to the Specht module
7
ρζ. That is,
λζ(Cay(Sn, S)) =
X
σ∈S
˜χζ(σ).
(6)
It is known [13] that the character of every ρζ ∈c
Sn on every conjugacy class of Sn is an integer
whose absolute value is at most the dimension of ρζ. Hence ˜χζ(γ) is a rational number in
the interval [−1, 1] for all ζ, γ ⊢n. The following table, which is extracted from [27, Table
1], gives the dimensions and characters of some irreducible representations of Sn.
ζ ⊢n
dim ρζ = χζ(e)
χζ(γ) with ci(γ) = ci
(n)
1
1
(n −1, 1)
n −1
c1 −1
(n −2, 2)
n(n−3)
2
c1(c1−3)
2
+ c2
(n −2, 1, 1)
(n−1)(n−2)
2
(c1−1)(c1−2)
2
−c2
(n −3, 3)
n(n−1)(n−5)
6
c1(c1−1)(c1−5)
6
+ (c1 −1)c2 + c3
(n −3, 2, 1)
n(n−2)(n−4)
3
c1(c1−2)(c1−4)
3
−c3
Table 1: Dimensions and characters of some irreducible representations of Sn
