---
doc_id: arxiv-0905.0591v3
doc_title: "A SUR VEY OF TWISTED ALEXANDER POL YNOMIALS"
section_id: sec-010-34-duality-for-twisted-invariants
section_title: "Duality for twisted invariants"
section_number: 3.4
pages: 9-11
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
doc_brief: "A SUR VEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexand er polynomials of a 3–manifold associated to a representation of its fundam ental group."
---
r ↦→
r. Let F be a free abelian group, with its natural involution. We exte nd the involution
on R to the group ring R[F ] and the quotient ﬁeld Q(R[F ]) in the usual way. We equip
R[F ]k with the standard hermitian inner product ⟨v,w ⟩ =vtw (where we view elements in
R[F ]k as column vectors).
LetN be a 3–manifold with empty or toroidal boundary and let α :π1(N ) → GL(k,R [F ])
a representation. We denote by α :π1(N ) → GL(k,R [F ]) the representation given by
⟨α(g−1)v,w ⟩ = ⟨v,α(g)w⟩
for all v,w ∈R[F ]k,g ∈π1(N ). Put diﬀerently, for any g ∈π1(N ) we have
α(g) = (α(g)−1)t ∈ GL(k,R [F ]).
We say that a representation is unitary if α =α.
Note that if ψ : π1(N ) → F is a non–trivial homomorphism to a free abelian group F
and γ :π1(N ) → GL(k,R ) a representation, then
γ ⊗ψ =γ ⊗ψ.
The following duality theorem can be proved using the ideas o f [Ki96] and [KL99a,
Corollary 5.2].
10 STEF AN FRIEDL AND STEF ANO VIDUSSI
Proposition 3.6. Let N be a 3–manifold with empty or toroidal boundary and let α :
π1(N ) → GL(k,R [F ]) a representation. Then
τ (N,α ) .=τ (N,a) ∈R[F ].
In particular if ψ : π1(N ) → F is a non–trivial homomorphism to a free abelian group F
and γ :π1(N ) → GL(k,R ) is a unitary representation, then τ (N,γ ⊗ψ) is reciprocal, i.e.
τ (N,γ ⊗ψ) = τ (N,γ ⊗ψ) ∈R[F ].
It is easy to see that in general the twisted Reidemeister tor sion is not reciprocal if one
considers representations α such that α(g) ⁄= α(g) for some g ∈ π1(N ). Hillman, Silver
and Williams [HSW09] give much more subtle examples which sh ow that there also exist
knots K together with special linear representations such that the corresponding twisted
Reidemeister torsion is not reciprocal.
The following proposition follows from the discussion in [F K06].
Proposition 3.7. Let N be a closed 3–manifold and let α : π1(N ) → GL(k,R [F ]) a
representation withR a Noetherian UFD. Assume that ∆ α
N,i ⁄= 0 for all i. Then the following
equalities hold:
∆ α
N,2
.= ∆
a
N,0 and
∆ α
N
.= ∆
a
N.
3.5. Shapiro’s lemma for twisted invariants. Let N be a 3–manifold with empty or
toroidal boundary. Let p : ˆN → N be a ﬁnite cover of degree d. Let F be a free abelian
group and let ˆα :π1( ˆN ) → GL(k,R [F ]) a representation.
Now consider the R[F ]k–module
Z[π1(N )] ⊗Z[π1( ˆN )]R[F ]k.
If g1,...,g d are representatives of π1(N )/π1( ˆN ) and if e1,...,e k is the canonical basis of
R[F ]k, then it is straightforward to see that the above R[F ]–module is a free R[F ]–module
with basis gi ⊗ej,i = 1,...,d,j = 1,...,k . The group π1(N ) acts on
Z[π1(N )] ⊗Z[π1( ˆN )]R[F ]k =R[F ]kd
via left multiplication which deﬁnes a representation π1(N ) → GL(kd,R [F ]) which we
denote by α.
Remark. (1) Let ˆγ : π1( ˆN ) → GL(k,R ) be a representation. Let ψ : π1(N ) → F be a
non–trivial homomorphism to a free abelian group F . We write ˆψ =ψ ◦p∗ and we
denote by γ the representation given by left multiplication by π1(N ) on
Z[π1(N )] ⊗Z[π1( ˆN )]Rk =Rkd.
Given ˆα = ˆγ ⊗ ˆψ we have in that case α =γ ⊗ψ.
(2) If ˆγ is the trivial one–dimensional representation, and ˆN the cover of N correspond-
ing to an epimorphism ϕ :π1(N ) →G to a ﬁnite group, then we have γ =ϕ.
The following is now a variation on Shapiro’s lemma (cf. [FV0 8a, Lemma 3.3] and
[HKL08, Section 3]).
A SUR VEY OF TWISTED ALEXANDER POLYNOMIALS 11
Theorem 3.8. We have
τ ( ˆN, ˆα) .=τ (N,α ).
If R is furthermore a Noetherian UFD, then
∆ ˆα
ˆN,i
.= ∆ α
N,i.
In its simplest form Theorem 3.8 says that given an epimorphi sm γ : π1(N ) → G to
a ﬁnite group the corresponding twisted Alexander polynomi als of N are just untwisted
Alexander polynomials of the corresponding ﬁnite cover.
