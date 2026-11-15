---
doc_id: hal-01215114
doc_title: "FPSAC 2011, Reykjavík, Iceland"
section_id: sec-011-combinatorial-lemmas
section_title: "Combinatorial lemmas"
section_number: null
pages: 6-7
source_pdf: hal-01215114.pdf
source_sha256: c70f8b04a5542a1f
toc_source: outline
doc_brief: "FPSAC 2011, Reykjavík, Iceland — In this paper we establish a new combinatorial formula for zonal polynomials in terms of power-sums. The proof relies on the sign-reversing involution principle."
---
Combinatorial lemmas
The proof relies on three simple combinatorial lemmas.
Lemma 4 Let λ and µ be two partitions of the same integer n. If λ does not dominate µ then for any
bijective ﬁllings Tλ and Tµ of the diagrams λ and µ with integers in [n] there exist two elements i and j
which are in the same row of Tµ and in the same column of Tλ.
Proof: Let us replace in the tableau Tλ each number i by the index of the row of Tµ containing i. We
have now a ﬁlling T ′
λ of λ in which any number k appears µk times and we have to prove the existence
of a column with some number appearing (at least) twice. Of course, reordering each column of T ′
λ in the
increasing order does not change anything. As λ does not dominate µ, there exists an integer i such that:
µ1 + · · · + µi > λ1 + · · · + λi.
But µ1 + · · · + µi is exactly the number of integers smaller than i + 1 in T ′
λ. There is not enough room
to ﬁt all these numbers in the ﬁrst i rows of λ, therefore there exists a box 2 in the other rows of λ which
contains a number which is smaller or equal than i. The column containing 2 has therefore at least i + 1
boxes with entries smaller or equal to i. The pigeon-hole principle shows that this column must contain a
repeated entry.
2
Consider the following action of S2n on the pair-partitions of [2n]: if σ is a permutation in S2n and S
a pair-partition of [2n], we denote by σ(S) the pair partition such that {σ(i), σ(j)} is a part of σ(S) if
and only if {i, j} is a part of S. Of course, the graphs GS1,S2 and Gσ(S1),σ(S2) are isomorphic thus the
corresponding set of loops have the same type. Conversely:
Lemma 5 The couples (S1, S2) such that µ(L(S1, S2)) = ν form exactly one orbit under the diagonal
action of the symmetric group S2n. Moreover, there are exactly
(2n)!
zν2ℓ(ν) of them.
Proof: Let us consider two couples (S1, S2) and (S′
1, S′
2), such that both graphs G := GS1,S2 and
G′ := GS′
1,S′
2 are collections of loops of lengths 2ν1, 2ν2 . . . . These two graphs are isomorphic as edge-
bicolored graphs. Let ϕ be any isomorphism of them. As it sends vertices of G on vertices of G′, it can be
seen as a permutation in S2n. As it sends red (resp. blue) edges of G on red (resp. blue) edges of G′, one
has: ϕ(S1) = S′
1 (resp. ϕ(S2) = S′
2). Thus all couples of pair-partitions of type ν are in the same orbit.
We will prove now that the size of the centralizer of a ﬁxed couple (S1, S2) is equal to zν2ℓ(ν) =
Q
i mi(ν)!(2i)mi(ν). Indeed, an element in the centralizer is entirely determined by the image of one
given point in each loop of L(S1, S2). Moreover, the image of an element in a loop of length 2ℓmust
be in a loop of the same length 2ℓand the images of two elements in two different loops must be in two
different loops.
2
Dual combinatorics of zonal polynomials
323
Lemma 6 Let λ be a partition of n, let T be a bijective ﬁlling of 2λ and let S1 be a pair-partition
matching elements of the 2j −1-th column of T with elements in its 2j-th column. If τ = (i j) with i and
j in the same column of T, and S = S(T) then
(−1)(S,τ(S1)) = (−1)(S,S1)+1.
Proof: Let us ﬁrst remark that GS,τ(S1) can be obtained from GS,S1 by replacing the blue edges {S1(i), i}
and {S1(j), j} by {S1(i), j} and {S1(j), i}. We distinguish two cases:
• if i and j are in different loops in GS,S1 then these loops are uniﬁed into one new loop in GS,τ(S1).
Thus

 L(S, τ(S1))

 =

 L(S, S1)

 −1 and the lemma holds in this case;
• suppose i and j are in the same loop in GS,S1. As i and j are in the same column of T and both S
and S1 match elements of the 2j −1-th column of T with elements of its 2j-th column, the distance
between i and j is even, where the distance is regarded as the number of steps within one loop. It
is easy to check in this case that the loop containing i and j in GS,S1 is split into two in GS,τ(S1).
Therefore,

 L(S, τ(S1))

 =

 L(S, S1)

 + 1 and the lemma also holds in this case.
2
