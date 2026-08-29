---
doc_id: hal-01215114
doc_title: "FPSAC 2011, Reykjavík, Iceland DMTCS proc. AO, 2011, 317–328 Dual combinatorics of zonal polynomials"
section_id: sec-011-combinatorial-lemmas
section_title: "Combinatorial lemmas"
section_number: null
pages: 6-8
source_pdf: hal-01215114.pdf
source_sha256: c70f8b04a5542a1f
doc_brief: "FPSAC 2011, Reykjavík, Iceland DMTCS proc. AO, 2011, 317–328 Dual combinatorics of zonal polynomials — In this paper we establish a new combinatorial formula for zonal polynomials in terms of"
---
The proof relies on three simple combinatorial lemmas.
Lemma 4 Letλ andµ be two partitions of the same integer n. If λ does not dominate µ then for any
bijective ﬁllingsTλ andTµ of the diagramsλ andµ with integers in [n] there exist two elementsi andj
which are in the same row ofTµ and in the same column of Tλ.
Proof: Let us replace in the tableau Tλ each number i by the index of the row of Tµ containingi. We
have now a ﬁlling T′
λ ofλ in which any number k appearsµk times and we have to prove the existence
of a column with some number appearing (at least) twice. Of course, reordering each column ofT′
λ in the
increasing order does not change anything. Asλ does not dominateµ, there exists an integeri such that:
µ1 +··· +µi >λ 1 +··· +λi.
Butµ1 +··· +µi is exactly the number of integers smaller than i + 1 inT′
λ. There is not enough room
to ﬁt all these numbers in the ﬁrst i rows ofλ, therefore there exists a box 2 in the other rows ofλ which
contains a number which is smaller or equal thani. The column containing 2 has therefore at leasti + 1
boxes with entries smaller or equal toi. The pigeon-hole principle shows that this column must contain a
repeated entry. 2
Consider the following action of S2n on the pair-partitions of [2n]: if σ is a permutation in S2n andS
a pair-partition of [2n], we denote by σ(S) the pair partition such that {σ(i),σ (j)} is a part of σ(S) if
and only if{i,j} is a part of S. Of course, the graphs GS1,S2 andGσ(S1),σ(S2) are isomorphic thus the
corresponding set of loops have the same type. Conversely:
Lemma 5 The couples (S1,S 2) such thatµ(L(S1,S 2)) = ν form exactly one orbit under the diagonal
action of the symmetric groupS2n. Moreover, there are exactly (2n)!
zν2𝓁(ν) of them.
Proof: Let us consider two couples (S1,S 2) and (S′
1,S′
2), such that both graphs G := GS1,S2 and
G′ :=GS′
1,S′
2 are collections of loops of lengths 2ν1, 2ν2... . These two graphs are isomorphic as edge-
bicolored graphs. Letϕ be any isomorphism of them. As it sends vertices ofG on vertices ofG′, it can be
seen as a permutation inS2n. As it sends red (resp. blue) edges of G on red (resp. blue) edges ofG′, one
has:ϕ(S1) =S′
1 (resp.ϕ(S2) =S′
2). Thus all couples of pair-partitions of typeν are in the same orbit.
We will prove now that the size of the centralizer of a ﬁxed couple (S1,S 2) is equal to zν2𝓁(ν) =∏
imi(ν)!(2i)mi(ν). Indeed, an element in the centralizer is entirely determined by the image of one
given point in each loop of L(S1,S 2). Moreover, the image of an element in a loop of length 2𝓁 must
be in a loop of the same length 2𝓁 and the images of two elements in two different loops must be in two
different loops. 2
Dual combinatorics of zonal polynomials 323
Lemma 6 Let λ be a partition of n, let T be a bijective ﬁlling of 2λ and let S1 be a pair-partition
matching elements of the 2j− 1-th column of T with elements in its 2j-th column. Ifτ = (ij ) withi and
j in the same column of T , andS =S(T ) then
(−1)(S,τ(S1)) = (−1)(S,S1)+1.
Proof: Let us ﬁrst remark thatGS,τ(S1) can be obtained fromGS,S1 by replacing the blue edges{S1(i),i}
and{S1(j),j} by{S1(i),j} and{S1(j),i}. We distinguish two cases:
• ifi andj are in different loops inGS,S1 then these loops are uniﬁed into one new loop inGS,τ(S1).
Thus
⏐⏐L(S,τ (S1))
⏐⏐ =
⏐⏐L(S,S 1)
⏐⏐− 1 and the lemma holds in this case;
• supposei andj are in the same loop in GS,S1. As i andj are in the same column of T and bothS
andS1 match elements of the 2j−1-th column ofT with elements of its 2j-th column, the distance
betweeni andj is even, where the distance is regarded as the number of steps within one loop. It
is easy to check in this case that the loop containing i andj inGS,S1 is split into two in GS,τ(S1).
Therefore,
⏐⏐L(S,τ (S1))
⏐⏐ =
⏐⏐L(S,S 1)
⏐⏐ + 1 and the lemma also holds in this case. 2
4.2 T riangularity
In this paragraph we prove that the functionsYλ satisfy property TR.
Let us ﬁx a bijective ﬁllingT of 2λ and setS =S(T ). The ﬁrst step of the proof consist of writing
Yλ =
∑
(S1,S2)T -admissible
(−1)(S,S1)pL(S1,S2)
in the monomial basis. In order to do that we will write eachpL(S1,S2) on this basis.
Recall that, if Π and Π′ are two set partitions, we say that Π is ﬁner than Π′ (and write Π≤ Π′) if each
part of Π′ is the union of some parts of Π.
Lemma 7 LetS1,S 2 be two pair partitions of{1,..., 2n}. Then
pL(S1,S2) =
∑
Π≥L(S1,S2)
aut
(
µ(Π)
)
mΠ.
Proof: It is a consequence of [Mac95, Chapter I, equation (6.9)]. 2
Using this lemma, one can writeYλ in the monomial basis:
Yλ =
∑
(S1,S2)T -admissible
∑
Π≥L(S1,S2)
(−1)(S,S1) aut
(
µ(Π)
)
mΠ
=
∑
Πset-
partition of [2n]


∑
(S1,S2) T -admissible
L(S1,S2)≤Π
(−1)(S,S1)

 aut
(
µ(Π)
)
mΠ. (3)
Remark. The inequalityL(S1,S 2)≤ Π is equivalent to the following local condition: the partners of any
integeri in the pair-partitionsS1 andS2 are in the same part of Π asi.
Let us assume now that µ(Π) is not dominated by λ. By Lemma 4, there exist i andj in [2n], which
are in the same part of Π and in the same column ofT . Let us denoteτ = (ij )∈S2n. Then:
324 Valentin Féray and Piotr ´Sniady
• (τ(S1),S 2) isT -admissible ⇐⇒ (S1,S 2) isT -admissible;
• L(τ(S1),S 2)≤ Π ⇐⇒ L(S1,S 2)≤ Π (because of the remark above);
• (−1)(S,τ(S1)) = (−1)(S,S1)+1 (see Lemma 6).
Thus, (S1,S 2)↦→ (τ(S1),S 2) is a sign reversing involution proving that the expression in the bracket in
the right-hand side of (3) is equal to zero as soon asµ(Π) is not dominated byλ.
This ends the proof of property TR.
