---
doc_id: hal-01215114
doc_title: "FPSAC 2011, Reykjavík, Iceland DMTCS proc. AO, 2011, 317–328 Dual combinatorics of zonal polynomials"
section_id: sec-015-via-numbers-of-embeddings
section_title: "Via numbers of embeddings"
section_number: null
pages: 9-10
source_pdf: hal-01215114.pdf
source_sha256: c70f8b04a5542a1f
doc_brief: "FPSAC 2011, Reykjavík, Iceland DMTCS proc. AO, 2011, 317–328 Dual combinatorics of zonal polynomials — In this paper we establish a new combinatorial formula for zonal polynomials in terms of"
---
LetS0,S1,S2 be three pair-partitions of the set [2k]. We consider the following function on the set of
Young diagrams:
Deﬁnition 8 N(1)
S0,S1,S2(λ) is the number of functions f from [2k] to the boxes of the Young diagram λ
such that for everyl∈ [2k]:
(Q0) f(l) =f(S0(l)), in other wordsf can be viewed as a function on the set of pairs constitutingS0;
(Q1) f(l) andf(S1(l)) are in the same column;
(Q2) f(l) andf(S2(l)) are in the same row.
Theorem 9 Letν be a partition of the integer k andS1, S2 be two ﬁxed pair-partitions of the set [2k]
such thatµ
(
L(S1,S 2)
)
=ν. Then one has the following equality between functions on the set of Young
diagrams:
Σ(2)
ν = 1
2𝓁(ν)
∑
S0
(−1)(S0,S1) 2|L (S0,S1)|N(1)
S0,S1,S2, (7)
where the sum runs over pair-partitions of [2k].
326 Valentin Féray and Piotr ´Sniady
5.2 In terms of Stanley’s coordinates
The notion of Stanley’s coordinates was introduced by Stanley [Sta04] who found a nice formula for
normalized irreducible character values of the symmetric group corresponding to rectangular Young dia-
grams. In order to generalize this result, he deﬁned, given two sequences p and q of positive integers of
same size (q being non-increasing), the partition:
p× q = (q1,...,q 1| {z }
p1 times
,...,q l,...,q l| {z }
pl times
).
Then he suggested to consider the quantity Σ(1)
ν (p× q) as a polynomial in p and q. An explicit combi-
natorial interpretation of the coefﬁcients was conjectured in [Sta06] and proved in [Fér10].
It is easy to deduce from the above expansion of Σ(2)
ν in terms of the N functions a combinatorial
description of the polynomial Σ(2)
ν (p× q).
Theorem 10 Letν be a partition of the integerk andS1,S2 be two ﬁxed pair-partitions of [2k] such that
µ
(
L(S1,S 2)
)
=ν. Then, one has:
Σ(2)
ν (p× q) = (−1)k
2𝓁(ν)
∑
S0

 ∑
φ:L(S1,S0)→N⋆
∏
l∈L(S1,S0)
(pϕ(l))·
∏
l′∈L(S2,S0)
(−2qψ(l′))

 (8)
whereψ(l′) := max lϕ(w) with l running over the loops of L(S0,S 1) having at least one element in
common withl′.
