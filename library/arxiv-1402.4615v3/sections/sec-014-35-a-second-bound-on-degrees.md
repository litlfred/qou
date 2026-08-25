---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-014-35-a-second-bound-on-degrees
section_title: "A second bound on degrees"
section_number: 3.5
pages: 26-27
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
aµ
ρ given by Proposition 3.7 is not strong enough. In this sectio n we give another
bound which is related to another gradation of Λ (α)
⋆ deﬁned by:
deg2(Mk) = k − 2 for k ≥ 2.
One has the following analogue of Lemma 3.6:
Lemma 3.9. Let ρ and π be two partitions and g ≥ 0 an integer. Then
degγ(bρ
g,π (γ)) ≤ deg2(Mρ) − deg2(Mπ∪(g)),
degγ(bρ
g,π (γ)) ≤ deg2(Mρ) − deg2(Mπ∪(g+1)) − 1.
Proof. The proof is similar to the one of Lemma 3.6. We deﬁne the pre-degree
(with respect to deg2) of an expression of the form b(γ) Mπ zg
i to be degγ(b) +
deg2(Mπ) + g. By Proposition 3.1, the pre-degree of Mk(λ(i)) is equal to k − 2.
Note that this pre-degree is multiplicative. Then Mρ(λ(i)) has pre-degree |ρ| −
2ℓ(ρ) = deg 2(Mρ). The lemma follows from the following inequalities: forg ≥ 0,
deg2(Mπ∪(g)) ≤ deg2(Mπ) + g;
deg2(Mπ∪(g+1)) ≤ deg2(Mπ) + g − 1.
Note that in the ﬁrst inequality the difference between the r ight hand side and the
left hand side is equal to 2, unless g = 0 ; in that case we have an equality. In the
second inequality, the case g = 0 is obvious as Mπ∪(1) = 0 and hence its degree is
−∞ by convention. In all other cases, we have an equality. □
We deduce from this lemma a new bound on the degree of aµ
ρ.
Proposition 3.10. The coefﬁcient aµ
ρ of Mρ in Jack character polynomial Lµ is a
polynomial in γ of degree smaller or equal to |µ| − ℓ(µ) − (|ρ| − 2ℓ(ρ)).
The same is true for Kµ.
Proof. It is a straightforward exercise to adapt the proof of Proposition 3.7. We use
Lemma 3.9 instead of Lemma 3.6 and |ρ| has to be replaced by |ρ| − 2ℓ(ρ). □
As an immediate consequence we have
Corollary 3.11. For any partition µ one has:
deg2(Chµ) = |µ| − ℓ(µ),
and the top degree part does not depend on α.
Note that Proposition 3.10 is neither weaker nor stronger th an Proposition 3.7.
But it is sometimes more appropriate, as we shall see in the next section.
Remark. The top degree part ofChµ for deg2 does not admit an explicit expression
as for deg1. One can however compute its linear terms in free cumulants, see
[FG13, Section 3].
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 27
3.6. Polynomiality of θµ(λ). In this section we prove that θµ(λ) is a polynomial
with rational coefﬁcients in α. This simple statement does not follow directly from
the deﬁnition of Jack polynomials and had been open for twent y years. It was
then proved by Lapointe and Vinet [LV95], who also proved the integrality of the
coefﬁcients in the monomial basis. Short after that, this re sult was completed by a
positivity result from Knop and Sahi [KS97].
Using the material of this Section, we can ﬁnd a new proof of th e polynomial-
ity in α. Integrity and positivity seem unfortunately impossible t o obtain via this
method.
First, we consider the dependence of Mk(λ) on α.
Lemma 3.12. Let k ≥ 2 be an integer and λ a partition. Then √αk−2Mk(λ) is a
polynomial in α with integer coefﬁcients.
Proof. We use induction over |λ| and k. Proposition 3.1 can be rewritten as
√αk−2Mk(λ(i)) − √αk−2Mk(λ) =
∑
r≥1,s,t≥0,
2r+s+t≤k
αr(√αzi)k−2r−s−t
( k − t − 1
2r + s − 1
)( r + s − 1
s
)
(α − 1)s √αt−2Mt(λ).
Note that √αzi = αx − y is a polynomial in α with integer coefﬁcients. Hence the
induction is immediate. □
Now we write, for µ, λ ⊢ n,
zµθµ(λ) = α
|µ|−ℓ(µ)
2 Chµ(λ) = α
|µ|−ℓ(µ)
2
∑
ρ
aµ
ρ Mρ(λ)
=
∑
ρ
α
|µ|−ℓ(µ)−(|ρ|−2ℓ(ρ))
2 aµ
ρ

 ∏
i≤ℓ(ρ)
√
αρi−2Mρi(λ)

 .
The quantities α
|µ|−ℓ(µ)−(|ρ|−2ℓ(ρ))
2 aµ
ρ and √
αρi−2Mρi(λ) are polynomials in α (by
Proposition 3.10 and Lemma 3.12), hence θµ(λ) is a polynomial in α.
