---
doc_id: arxiv-1707.00196v3
doc_title: "Yang-Baxter representations of the inﬁnite symmetric group"
section_id: sec-003-22-faithfulness
section_title: "Faithfulness"
section_number: 2.2
pages: 8-8
source_pdf: 1707.00196v3.pdf
source_sha256: 9908b71521275b17
toc_source: outline
doc_brief: "Yang-Baxter representations of the inﬁnite symmetric group — Every unitary involutive solution of the quantum Yang-Baxter equation (R- matrix) deﬁnes an extremal character and a representation of the"
---
Faithfulness
Given an R-matrix R ∈R0 of dimension d, the homomorphism ρR restricts to a
representation ρ(n)
R
of Sn on V ⊗n, which has dimension dn. This observation expresses
that Yang-Baxter representations are small in comparison to the group algebra C[Sn],
and leads to restrictions on the Thoma parameters of Yang-Baxter characters.
Proposition 2.4. Let R ∈R0.
i) As a group homomorphism, ρR is injective if and only if R̸ = ±1.
ii) As an algebra homomorphism, ρR : C[S∞] →E0 is not injective.
Proof. i) This is a general property of S∞. Clearly, if R = ±1 then ρR is not injective.
Conversely, assume that ρR is not injective and σ ∈S∞lies in the kernel, then σ also
lies in the kernel of ρR|Sn for n suﬃciently large. But for n ≥5, the only non-trivial
proper normal subgroup of Sn is the alternating group An. Thus ker ρR|Sn contains
at least An. This implies that the image of ρR is either trivial or Z2. In the case at
hand, this means that ρR is injective if and only if R̸ = ±1.
ii) ρR restricts to an algebra homomorphism ρ(n)
R
: C[Sn] →End V ⊗n. As the
dimensions of C[Sn] and End(V ⊗n) are n! and d2n, respectively, and n! > d2n for n
suﬃciently large, it follows that ρ(n)
R
cannot be injective.
The second part of this proposition implies that Yang-Baxter characters are never
faithful.
This observation allows us to make use of the following theorem due to
Wassermann [26, Thm. III.6.5].
Theorem 2.5. [26] Let χ be an extremal character of S∞with Thoma parameters
(α, β) ∈T. Then χ is faithful as a state of the group C∗-algebra C∗S∞if and only
if either P
i αi + P
i βi < 1, or P
i αi + P
i βi = 1 and inﬁnitely many αi or βi are
non-zero.
In combination with Prop. 2.4 ii), this immediately implies the following result.
Corollary 2.6. Let (α, β) ∈T be the Thoma parameters of a Yang-Baxter character
χR. Then P
i αi + P
i βi = 1, and only ﬁnitely many αi or βi are non-zero.
We can now give a ﬁrst example of an extremal non-Yang-Baxter character, namely
the Plancherel trace χ(σ) = δσ,e. By (2.6), the Plancherel trace has Thoma parameters
α = β = 0 and therefore violates the condition P
i αi + P
i βi = 1. Its GNS repre-
sentation is the left regular representation, which is too large to be of Yang-Baxter
form.
