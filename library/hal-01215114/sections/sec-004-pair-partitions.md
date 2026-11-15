---
doc_id: hal-01215114
doc_title: "FPSAC 2011, Reykjavík, Iceland"
section_id: sec-004-pair-partitions
section_title: "Pair partitions"
section_number: null
pages: 3-4
source_pdf: hal-01215114.pdf
source_sha256: c70f8b04a5542a1f
toc_source: outline
doc_brief: "FPSAC 2011, Reykjavík, Iceland — In this paper we establish a new combinatorial formula for zonal polynomials in terms of power-sums. The proof relies on the sign-reversing involution principle."
---
Pair partitions
Deﬁnition 2 A pair-partition of [2n] = {1, . . . , 2n} is a set of pairwise disjoint two-element sets, such
that their (disjoint) union is equal to [2n].
A pair-partition S can be also seen as an involution as the set [2n]. Therefore, we use the notation S(i)
for the partner of i, i.e. the other element in the same set of S.
For two pair-partitions S1, S2 of the same set [2n] we consider the edge-bicolored graph GS1,S2 deﬁned
as follows: its vertex set is [2n], its red (resp. blue) edges are the pairs in S1 (resp. S2). As every vertex
has degree 2, this graph is a disjoint union of loops. We denote L(S1, S2) the corresponding set-partition
of [2n]. Note that the length of each loop (or equivalently the size of each block of L(S1, S2)) is an even
number because of the edge bicoloration.
It is common to associate to a set-partition the integer partition formed by the non-increasing sequence
of the part sizes. Here, as we deal only with set partitions Π with parts of even length, we will rather
320
Valentin Féray and Piotr ´Sniady
consider the non-increasing sequence of the half-sizes of the parts. This integer partition is called the type
of the set partition Π and is denoted µ(Π).
In other words, the type of L(S1, S2) is the partition ℓ1, ℓ2, . . . where (2ℓi)i≥1 is the non-increasing
sequence of the lengths of the loops of GS1,S2. We also deﬁne the sign of a couple of pair-partitions as
follows:
(−1)(S1,S2) = (−1)(ℓ1−1)+(ℓ2−1)+··· = (−1)n−| L(S1,S2)|.
Finally we use the short notations pΠ = pµ(Π) and mΠ = mµ(Π) for symmetric functions.
Example. We consider
S1 =

{1, 2}, {3, 4}, {5, 6}
	
;
S2 =

{1, 3}, {2, 4}, {5, 6}
	
.
Then GS1,S2 = .
.
.
.
.
.
1
2
3
4
5
6
.
In this case, L(S1, S2) =

{1, 2, 3, 4}, {5, 6}
	
and µ(L(S1, S2)) = (2, 1).
