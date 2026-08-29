---
doc_id: hal-01215114
doc_title: "FPSAC 2011, Reykjavík, Iceland DMTCS proc. AO, 2011, 317–328 Dual combinatorics of zonal polynomials"
section_id: sec-012-orthogonality
section_title: "Orthogonality"
section_number: null
pages: 8-9
source_pdf: hal-01215114.pdf
source_sha256: c70f8b04a5542a1f
doc_brief: "FPSAC 2011, Reykjavík, Iceland DMTCS proc. AO, 2011, 317–328 Dual combinatorics of zonal polynomials — In this paper we establish a new combinatorial formula for zonal polynomials in terms of"
---
In this section we prove that the functionsYλ satisfy property OR.
As the deﬁnition of Yλ does not depend on the choice of the bijective ﬁlling T ∈ F (λ) (F (λ) is by
deﬁnition the set of bijective ﬁllings of 2λ), one can write:
(2n)!Yλ =
∑
T∈F(λ)
∑
(S1,S2)T -admissible
(−1)(S(T),S1)pL(S1,S2)
=
∑
S1,S2
pair-partitions
∑
T∈F(λ) s.t.
(S1,S2) T -admissible
(−1)(S(T),S1)pL(S1,S2). (4)
Letν be a partition ofn. A consequence of Lemma 5 is that each of the (2n)!
zν2𝓁(ν) couples of pair-partitions
(S1,S 2) such that µ(L(S1,S 2)) = ν has the same contribution to the right-hand side of the previous
equation. Therefore, if we ﬁx such a couple (S1,S 2), the coefﬁcient ofpν inYλ is given by:
(2n)! [pν]Yλ = (2n)!
zν2𝓁(ν)
∑
T∈F(λ) s.t.
(S1,S2) T -admissible
(−1)(S(T),S1). (5)
But, using equation (4) forYλ, one has the following expression for the scalar product:
(2n)!⟨Yλ,Yλ′⟩2 =
∑
S1,S2
pair-partitions
∑
T∈F(λ) s.t.
(S1,S2) T -admissible
(−1)(S(T),S1)zν 2𝓁(ν) [pν]Yλ′,
whereν =µ
(
L(S1,S 2)
)
depends on the summation index. Now, [pν]Yλ′ can be evaluated via equation
(5) and we obtain:
(2n)!⟨Yλ,Yλ′⟩2 =
∑
S1,S2
pair-partitions
∑
T∈F(λ) s.t.
(S1,S2) T -admissible
∑
T′∈F(λ′) s.t.
(S1,S2) T′-admissible
(−1)(S(T),S1) (−1)(S(T′),S1). (6)
Let us assumeλ⁄=λ′. One can assume without loss of generality thatλ is not dominated byλ′; otherwise
we swapλ andλ′. By Lemma 4 there exist two elements i andj which are in the same row of T′ and in
the same column of T . We choose the smallest ones in the lexicographic order. We denote by τT,T′ the
transposition (ij ) and we consider the function:
ϕ : (S1,S 2,T,T ′)↦→ (τT,T′(S1),S 2,T,T ′◦τT,T′),
whereT′◦τT,T′ is the tableauT′ with the locations ofi andj interchanged. It is easy to check that:
Dual combinatorics of zonal polynomials 325
• ϕ is an involution (becauseT′◦τT,T′ andT′ have the same rows and, therefore, the unordered pair
{i,j} is the same for the two pairs of ﬁllings);
• (S1,S 2) isT -admissible if and only if (τT,T′(S1),S 2) isT -admissible;
• (S1,S 2) isT′-admissible if and only if (τT,T′(S1),S 2) isT′◦τT,T′-admissible;
• (−1)(S(T),τT,T′(S1)) = (−1)(S(T),S1)+1 (see Lemma 6);
• (−1)
(
S(T′◦τT,T′),τT,T′(S1)
)
= (−1)(S(T′),S1) (becauseS(T′◦τT,T′) =τT,T′(S(T′))).
The contributions of the quadruplets (S1,S 2,T,T ′) andϕ(S1,S 2,T,T ′) in equation (6) cancel, which
proves that the functionsYλ are orthogonal with respect to the deformed Hall scalar product⟨·,·⟩2.
