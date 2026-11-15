---
doc_id: hal-01215114
doc_title: "FPSAC 2011, Reykjavík, Iceland"
section_id: sec-006-zonal-polynomials-in-terms-of-pair-partition
section_title: "Zonal polynomials in terms of pair-partition"
section_number: null
pages: 4-5
source_pdf: hal-01215114.pdf
source_sha256: c70f8b04a5542a1f
toc_source: outline
doc_brief: "FPSAC 2011, Reykjavík, Iceland — In this paper we establish a new combinatorial formula for zonal polynomials in terms of power-sums. The proof relies on the sign-reversing involution principle."
---
Zonal polynomials in terms of pair-partition
Let λ = (λ1, λ2, . . . ) be a partition of n and T be a bijective ﬁlling of the Young diagram 2λ =
(2λ1, 2λ2, . . . ) with the elements of [2n]. Any pair-partition of [2n] can be viewed as a pairings of
the boxes of T. We denote S(T) the pair partition which matches the boxes (i, 2j −1) and (i, 2j) of T
for all values of i and 1 ≤j ≤λi. Besides, a couple of pair-partitions (S1, S2) is called T-admissible if
each pair of boxes matched by S2 is in the same row and if S1 matches elements of the 2j −1-th column
of T with elements of its 2j-th column.
Theorem 3 Let λ be a partition and T be a bijective ﬁlling of 2λ. One has:
Zλ =
X
(S1,S2) T -admissible
(−1)(S(T ),S1) pL(S1,S2).
Example.
Let λ = (2, 1) and T =
1 2 3 4
5 6
.
Then (S1, S2) is T-admissible if and only if:
S1 ∈

{1, 2}, {3, 4}, {5, 6}
	
,

{1, 6}, {3, 4}, {2, 5}
	
and
S2 ∈

{1, 2}, {3, 4}, {5, 6}
	
,

{1, 3}, {2, 4}, {5, 6}
	
,

{1, 4}, {2, 3}, {5, 6}
	
.
The ﬁrst possible value of S1 gives (−1)(S(T ),S1) = 1 and the types of L(S1, S2) for the three pos-
sible values of S2 are, respectively, (1, 1, 1), (2, 1) and (2, 1). For the second value of S1 one has
(−1)(S(T ),S1) = −1 and the types of the corresponding set-partitions L(S1, S2) are, respectively, (2, 1),
(3) and (3).
Finally, one obtains Z(2,1) = p(1,1,1) + p(2,1) −2p(3).
Remark. This theorem is an analogue of a known result on Schur symmetric functions:
n! · sλ
dim(λ) =
X
(−1)|σ1| ptype(σ1◦σ2),
(1)
Dual combinatorics of zonal polynomials
321
where the sum runs over pairs of permutations (σ1, σ2) of the boxes of the diagram λ such that σ1
(resp. σ2) preserves the columns (resp. the rows) of λ and type(σ1 ◦σ2) denotes the partition describing
the lengths of the cycles of σ1 ◦σ2. This formula is a consequence of the explicit construction of the
representation associated to λ via the Young symmetrizer. For a detailed proof, see [F´S11a, Theorem
4]. In [Han88], the authors tries unsuccessfully to generalize it to Jack polynomials by introducing some
statistics on couples of permutations. Our result shows, that, at least for α = 2, a natural way to generalize
it consists in using other combinatorial objects than permutations.
