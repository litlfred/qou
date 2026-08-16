---
doc_id: arxiv-math-0605314v1
doc_title: "A UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANT FOR INTEGRAL HOMOLOGY SPHERES KAZUO HABIRO"
section_id: sec-077-1233-expansions-at-roots-of-unity-for-every-root
section_title: "Expansions at roots of unity. For every root of unityζ,ιζ (JM )∈ Z[ζ][[q−ζ]]"
section_number: 12.3.3
pages: 42-43
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
doc_brief: "A UNIFIED WITTEN-RESHETIKHIN-TURAEV INVARIANT FOR INTEGRAL HOMOLOGY SPHERES KAZUO HABIRO — W e construct an invariant JM of integral homology spheres M with values in a completion ˆZ[q] of the"
---
may be considered as a generalization of the Ohtsuki series τ O(M ) = ι1(JM ). Deﬁne
λζ,k (M )∈ Z[ζ], k≥ 0, by
ιζ (JM ) =
∑
k≥0
λζ,k (M )(q−ζ)k.
Question 12.8. Recall that the Ohtsuki series is considered to be related to the
perturbative expansion of the Chern-Simons path integral. Are there any “physical”
interpretation of the other power series ιζ(JM )?
Let us consider the case ζ =−1. We have
ι−1(JM ) =
∑
k≥0
λ−1,k(M )(q + 1)k∈ Z[[q + 1]] (12.5)
whereλ−1,k(M )∈ Z. It follows from Lemma 10.3 that λ−1,0(M ) = 1. Thus the ﬁrst
interesting coeﬃcient is λ−1,1(M )∈ Z, which is additive under connected sum, and
satisﬁes λ−1,1(−M ) =−λ−1,1(M ) by Proposition 12.1. Some computations show
that λ−1,1 is nontrivial (i.e., non-vanishing for some M ), and linearly independent
over Q to the Casson invariant λ(M ) = 1
6λ1(M ) of M . (However, there is a
congruence relation between them, see Remark 12.22 below.) See Remarks 12.21
and 12.22 for some other properties of λ−1,k(M ). An interesting problem is to
identify the topological information carried by λ−1,1(M ).
12.3.4. Relations between two power series expansions at diﬀerent r oots of unity.
Let ζ,ξ ∈Z , where ord( ζ/ξ ) = pe is a prime power. We consider how the two
power series expansions ιζ (JM )∈ Z[ζ][[q−ζ]] and ιξ(JM )∈ Z[ξ][[q−ξ]] are related.
Note that these two formal power series rings can be regarded as subrings of
Rζ,ξ := lim←−i,jZ[ζ,ξ ][q]/((q−ζ)i, (q−ξ)j)∼
= Zp[ζ,ξ ][[q−ζ]]∼
= Zp[ζ,ξ ][[q−ξ]].
InRζ,ξ we have
ιζ (JM ) =
∑
k≥0
λζ,k (q−ζ)k
=
∑
k≥0
λζ,k ((q−ξ) + (ξ−ζ))k
=
∑
i≥0
(∑
j≥0
(i +j
i
)
(ξ−ζ)jλζ,i+j
)
(q−ξ)i
A UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANT 43
Hence, we have
λξ,k =
∑
j≥0
(k +j
k
)
(ξ−ζ)jλζ,k+j(12.6)
fork≥ 0. This formula describes how the coeﬃcients of the power ser ies expansion
atζ determines those at ξ. Note that each λξ,k is determined modulo a given power
of p by ﬁnitely many coeﬃcients in the power series expansion at ζ.
Setting k = 0 in (12.6), we have
τξ(M ) =
∑
j≥0
(ξ−ζ)jλζ,j(12.7)
Note that if ζ = 1 and ord( ξ) is an odd prime power, then (12.7) implies that
the Lawrence’s p-adic convergence conjecture mentioned in the introductio n. Thus
(12.7) generalizes Lawrence’s conjecture.
(12.7) implies the following.
Proposition 12.9. Letζ,ξ ∈Z with ord(ζ/ξ ) a prime power. Then we have
τζ (M )≡τξ(M ) (mod ( ξ−ζ))
in Z[ζ,ξ ].
Corollary 12.10. Let ζ∈Z with ord(ζ) = dpe, where d∈{ 1, 2, 3, 4, 6}, e≥ 0,
and p is a prime. Then we have τζ(M )⁄= 0.
Proof. It is well known that we have τξ(M ) ⁄= ±1 for ξ ∈ Z with ord(ξ) ∈
{1, 2, 3, 4, 6} (see Section 12.4.2). This fact and Proposition 12.9 implie s the as-
sertion, since (ξ−ζ)⁄= (1) in Z[ζ,ξ ].
The case d = 1 and p odd in Corollary 12.10 follows also from Lawrence’s
conjecture proved by Rozansky, and presumably has been well known.
Conjecture 12.11 (Non-vanishing Conjecture). For any integral homology sphere
M , we have τζ (M )⁄= 0 for every root of unity ζ.
See Conjectures 13.4 and 13.9 for stronger statements.
12.4. Divisibility properties and applications to power series i nvariants.
