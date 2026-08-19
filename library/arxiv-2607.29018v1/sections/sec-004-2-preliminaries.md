---
doc_id: arxiv-2607.29018v1
doc_title: "The Aldous property for normal Cayley graphs on symmetric groups"
section_id: sec-004-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 7-8
source_pdf: 2607.29018v1.pdf
source_sha256: 789faa122dd32290
doc_brief: "The Aldous property for normal Cayley graphs on symmetric groups — Aldous’ spectral gap conjecture states that the random walk and the interchange process on any connected graph have the same"
---
and Corollary 1.5 in Section 4. To prove Theorem 1.6, we first need to determine all normal
Cayley graphs onS n that are line graphs (see Theorem 5.1). Using this and the classifica-
tion [31] of connected regular graphs with second largest eigenvalue at most 1, we obtain a
classification of all normal Cayley graphs onS n whose strictly second largest eigenvalue is
at most 1 (see Theorem 5.5). With the help of this classification, which is of interest for its
own sake, we prove Theorem 1.6 and Corollary 1.7 in Section 6.
2 Preliminaries
The reader is referred to [18, 19, 29, 32] for general representation theory and [28] for sym-
metric groups and their representations. Apartitionof a positive integernis a sequence of
positive integersγ= (γ 1,γ 2,...,γ m) such thatγ 1≥γ 2≥···≥γ m andn=γ 1 +γ 2 +···+γ m.
We writeγ⊢nto indicate this partition ofn, and letc i(γ) denote the number of parts of
γwhich are equal toi. Thesignof a permutationσ∈S n, denoted by sgn(σ), is defined
to be 1 ifσis an even permutation and−1 ifσis an odd permutation. Every permutation
σ∈S n decomposes into disjoint cycles; thecycle typeofσis the partition ofnwhose parts
are the lengths of these cycles. It is well known that two elements ofS n are conjugate if and
only if they have the same cycle type. Thus, the conjugacy classes ofS n are determined by
their cycle types and thus correspond to the partitions ofn. For a partitionγ⊢n, denote by
C(Sn,γ) the corresponding conjugacy class ofS n. Note thatc 1(γ) =|fix(σ)|is the number
of fixed points of eachσ∈C(S n,γ). Define sgn(γ) = 1 if the permutations inC(S n,γ) are
even, and sgn(γ) =−1 otherwise.
For each partitionζ⊢n, letρ ζ denote the corresponding Specht module in ˆSn. The
Specht modulesρ (n),ρ (1n) andρ (n−1,1) are called thetrivial representation,sign representation
andstandard representationofS n, respectively. We denote the character and normalized
character ofρ ζ byχ ζ(·) and ˜χζ(·), respectively. Since they are class functions onS n, we
writeχ ζ(γ) and ˜χζ(γ) for their values on the conjugacy classC(S n,γ). It is well known
thatχ (n)(σ) = ˜χ(n)(σ) = 1 andχ (1n)(σ) = ˜χ(1n)(σ) = sgn(σ) for everyσ∈S n. Note that
χζ(e) = dimρζ is the dimension ofρ ζ∈ ˆSn for anyζ⊢n.
In view of (1), for a normal Cayley graph Cay(S n,S) and a partitionζ⊢n, we use
λζ(Cay(Sn,S)), orλ ζ for short, to denote its eigenvalue corresponding to the Specht module
7
ρζ. That is,
λζ(Cay(Sn,S)) =
∑
σ∈S
˜χζ(σ).(6)
It is known [13] that the character of everyρζ∈ ˆSn on every conjugacy class ofSn is an integer
whose absolute value is at most the dimension ofρ ζ. Hence ˜χζ(γ) is a rational number in
the interval [−1,1] for allζ,γ⊢n. The following table, which is extracted from [27, Table
1], gives the dimensions and characters of some irreducible representations ofS n.
ζ⊢ndimρ ζ =χ ζ(e)χ ζ(γ) withc i(γ) =c i
(n) 1 1
(n−1,1)n−1c 1−1
(n−2,2) n(n−3)
2
c1(c1−3)
2 +c 2
(n−2,1,1) (n−1)(n−2)
2
(c1−1)(c1−2)
2 −c 2
(n−3,3) n(n−1)(n−5)
6
c1(c1−1)(c1−5)
6 + (c1−1)c 2 +c 3
(n−3,2,1) n(n−2)(n−4)
3
c1(c1−2)(c1−4)
3 −c 3
Table 1: Dimensions and characters of some irreducible representations ofS n
The following lemma will play a crucial role in our proof of Theorem 1.3.
Lemma 2.1(cf. [27, Proposition 2.3]).There exists a positive integerN 0 such that for every
n≥N 0 and anyγ⊢nwith|fix(γ)|≥2, we have
max
ζ⊢n
ζ/∈{(n),(1n)}
˜χζ(γ) = ˜χ(n−1,1)(γ).
