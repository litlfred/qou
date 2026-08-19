---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-015-37-yet-another-gradation-and-bound-on-degrees
section_title: "Yet another gradation and bound on degrees"
section_number: 3.7
pages: 27-30
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
Section 3.5 is suitable for some purposes (as we have seen in t he previous sec-
tion), but it has the unpleasant aspect that all homogeneous spaces have an inﬁnite
dimension. In particular, Proposition 3.10 does not give an y information on the
maximal power of M2 which can appear in Lµ. In this section we propose a way
to avoid this difﬁculty. It is technical but will be useful in the next section.
We deﬁne a new algebraic basis of Λ (α)
⋆ by:
M ′
2 = M2,
M ′
k = Mk − (−γ)k−2M2 for k ≥ 3.
28 M. DOŁ ˛ EGA AND V . FÉRAY
We also consider the gradation deﬁned by:
deg3(M ′
2) = 1 , deg3(M ′
k) = k − 2 for k ≥ 3,
so that deg3(M ′
ρ) = |ρ| − 2ℓ(ρ) + m2(ρ). Obviously, there exists a polynomial L′
µ
such that
Chµ = L′
µ(M ′
2, M′
3, . . .).
For example, one has:
L′
(2,2) = (M ′
3)2 + 6(M ′
2)2 − 4M ′
4 − 10γM ′
3 − 2M ′
2.
We denote by(a′)µ
ρ the coefﬁcient of M ′
ρ in L′
µ. Then, one has the following result.
Proposition 3.13. The coefﬁcient (a′)µ
ρ is a polynomial in γ of degree at most
|µ| − ℓ(µ) + m1(µ) − (|ρ| − 2ℓ(ρ) + m2(ρ)).
Remark. The analogous result is not true for aµ
ρ, as it can be seen on the case
µ = (2, 2).
The algorithm to compute the coefﬁcient (a′)µ
ρ is the same as for aµ
ρ and the
proof of the bound on degrees is similar to those of Propositions 3.7 and 3.10. Let
us give some details.
First, one can rewrite Proposition 3.1 in terms of the quantities M ′
k:
(16) M ′
k(λ(i)) − M ′
k(λ) = Mk(λ(i)) − Mk(λ) − (−γ)k−2
=
∑
r≥1,s,t≥0,
2r+s+t≤k
(r,s,t )⁄=(1,k −2, 0)
[
zk−2r−s−t
i
( k − t − 1
2r + s − 1
)( r + s − 1
s
)
· (−γ)s(M ′
t(λ) + (−γ)t−2M ′
2(λ))
]
.
Please note that the term (−γ)k−2 corresponding to (r, s, t) = (1 , k − 2, 0) does
not belong to the sum any more. By multiplication, there exis t some polynomials
(b′)ρ
g,π (γ) such that
M ′
ρ(λ(i)) = M ′
ρ(λ) +
∑
g,π
(b′)ρ
g,π (γ) zg
i M ′
π(λ).
Using Equation (11) and Proposition 3.3, we obtain the following equalities:
∑
ρ
(a′)µ
ρ



∑
g,h≥0,
π⊢h
(b′)ρ
g,π (γ)M ′
πMg


 = m1(µ) Chµ\1,(A′)
∑
ρ
(a′)µ
ρ



∑
g,h≥0,
π⊢h
(b′)ρ
g,π (γ)M ′
πMg+1


 =
∑
r≥2
r · mr(µ) Chµ↓r .(B′)
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 29
Plugging Mg = M ′
g + (−γ)g−2M ′
2 in these equations and identifying the coefﬁ-
cient of M ′
τ on both sides, we obtain the following system:
(A′
τ )
∑
ρ
(a′)µ
ρ




∑
g,π,
π∪(g)=τ
(b′)ρ
g,π (γ) +
∑
g>2,π,
π∪(2)=τ
(−γ)g−2(b′)ρ
g,π (γ)




= m1(µ)(a′)µ\1
τ ,
(B′
τ )
∑
ρ
(a′)µ
ρ




∑
g,π,
π∪(g+1)=τ
(b′)ρ
g,π (γ) +
∑
g≥2,π,
π∪(2)=τ
(−γ)g−1(b′)ρ
g,π (γ)




=
∑
r≥2
r · mr(µ)(a′)µ↓r
τ ,
It is easy to check that Lemma 3.4 still holds for this system.
The next step is to give a bound on the degree of (b′)ρ
g,π (γ).
Lemma 3.14.
degγ(bρ
g,π (γ)) ≤ deg3(M ′
ρ) − deg3(M ′
π) − max(g, 1).
Proof. Let us call pre-degree (with respect to deg3) of an expression of the form
b(γ) M ′
π zg
i the quantity degγ(b) + deg 3(M ′
π) + g. It is multiplicative. Clearly,
M ′
k(λ(i)) has pre-degree max(k − 2, 1) (see Equation (16)), thus M ′
ρ(λ(i)) has pre-
degree deg3(M ′
ρ), which ﬁnishes the proof of the case g ≥ 1. For g = 0, one has
to look at the term which does not involve zi. It is easy to check on Equation (16)
(here, it is crucial to use M ′ and not M) that
M ′
k(λ(i))|zi=0 = M ′
k(λ)|zi=0 + (terms of pre-degree k − 3) .
Hence by multiplication,
M ′
ρ(λ(i))|zi=0 = M ′
ρ(λ)|zi=0 +
(
terms of pre-degree deg3(M ′
ρ) − 1
)
,
which ﬁnishes the proof of the lemma. □
We have now all the tools to prove Proposition 3.13 by induction. As usual, we
ﬁrst consider the case where ρ = τ ∪ (2) has the smallest part equal to 2. Then
Equation (Aτ ) can be written as:
m2(ρ) · (a′)µ
ρ = m1(µ)(a′)µ\1
τ −
∑
π,g,
π∪(g)=τ
∑
ρ′>1ρ
(b′)ρ′
g,π (γ)(a′)µ
ρ′
−
∑
g>2,π,
π∪(2)=τ
∑
ρ′>1ρ
(−γ)g−2(b′)ρ
g,π (γ)(a′)µ
ρ′.
30 M. DOŁ ˛ EGA AND V . FÉRAY
With arguments similar to the ones used previously, the ﬁrst two terms are poly-
nomials in γ of degree at most |µ| − ℓ(µ) + m1(µ) − deg3(M ′
ρ). Let us focus
on the last summand. By induction hypothesis (a′)µ
ρ′ is a polynomial of degree
|µ| − ℓ(µ) + m1(µ) − deg3(M ′
ρ′). By Lemma 3.14, (b′)ρ
g,π (γ) has degree equal to
deg3(M ′
ρ) − deg3(M ′
π) − g. Hence the product of these two terms with (−γ)g−2
has degree at most
|µ| − ℓ(µ) + m1(µ) − (deg3(M ′
π) − 2) = |µ| − ℓ(µ) + m1(µ) − deg3(M ′
ρ).
The equality comes from the fact that ρ = τ ∪ (2) = π ∪ (2, 2).
Finally one obtains that(a′)µ
ρ has degree at most|µ|−ℓ(µ)+m1(µ)−deg3(M ′
ρ).
The case when ρ has no parts equal to 2 is similar. □
Corollary 3.15. For any partition µ one has:
deg3(Chµ) = |µ| − ℓ(µ) + m1(µ),
and the top degree part does not depend on α.
Remark. The top degree part of Chµ for deg3 has, as far as we know, no close
expression.
