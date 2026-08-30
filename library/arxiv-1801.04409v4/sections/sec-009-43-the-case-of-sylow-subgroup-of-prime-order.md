---
doc_id: arxiv-1801.04409v4
doc_title: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES"
section_id: sec-009-43-the-case-of-sylow-subgroup-of-prime-order
section_title: "The case of Sylow subgroup of prime order"
section_number: 4.3
pages: 17-18
source_pdf: 1801.04409v4.pdf
source_sha256: db61d011e3775aca
doc_brief: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES — We develop the theory of semisimpliﬁcations of ten- sor categories deﬁned by Barrett and Westbury."
---
consider the simplest nontrivial special case of Theorem 4.2, when t he
p-Sylow subgroup of G has order p.
Corollary 4.9. If P = Z/p then RepkG = (Verp)L, where Verp is the
Verlinde category (see Example 2.7(2)).
17
Note that if p = 2 then Verp = Vec. Thus, if P = Z/2 then Corollary
4.9 says that RepkG = Rep kL.
So let us consider the case p> 2 and compute the category (Ver p)L
more explicitly. Note that Ver p = Ver +
p ⊠ Supervec, and Ver p has no
nontrivial symmetric tensor autoequivalences ([O]), while Ver +
p has no
nontrivial tensor automorphisms of the identity functor. Thus, f rom
Corollary 4.9 we get
RepkG = Ver+
p ⊠ SupervecL.
The group of tensor automorphisms of the identity functor of Sup ervec
is Z/2. Hence, actions of L on Supervec correspond to elementsH 2(L, Z/2).
Let c ∈ H 2(L, Z/2) be the element corresponding to the action as
above, and let us compute c. Since the action of L on Z/p factors
through an action of Z/(p − 1), the element c is pulled back from a
canonical element ¯c ∈H 2(Z/(p − 1), Z/2) = Z/2.
Proposition 4.10. The element ¯c is nontrivial.
Proof. It suﬃces to show that the pullback of ¯ c to Z/2 ⊂ Z/(p − 1)
is nontrivial. For this purpose, it suﬃces to consider the semisimpliﬁ-
cation of Rep kDp, where Dp := Z/2 ⋉ Z/p is the dihedral group. In
RepkDp we have an invertible object X of vector space dimension p−1,
which has composition series k+, k−,..., k+, k−, where k+ is the trivial
representation of Z/2 and k− is the sign representation, and it suﬃces
to show that X has order > 2. But we have X = X ∗ ⊗ k−. Thus, X
cannot have order 2, as desired. □
Let ~L be the central extension of L by Z/2 deﬁned by the cocycle c,
and let z be the generator of the central subgroup Z/2 ⊂ ~L.
Corollary 4.11. If p is odd and P = Z/p then
RepkG ∼= Ver+
p ⊠ Repk(~L,z ),
where Repk(~L,z ) is the category of representations of ~L on supervector
spaces, so that z acts by the parity operator.
