---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-020-61-convergence-of-polynomial-functions
section_title: "Convergence of polynomial functions"
section_number: 6.1
pages: 38-40
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 39
6.1. Convergence of polynomial functions. Let us recall equation (8), which
gives us the expectation of Jack characters with respect to Jack measure:
EP(α)
n
(Ch(α)
µ ) =
{
n(n − 1) · · · (n − k + 1) if µ = 1 k for some k ≤ n,
0 otherwise.
As Chµ is a linear basis of Λ (α)
⋆ , it implies the following lemma (which is an
analogue of [Ols10, Theorem 5.5] with another gradation).
Lemma 6.1. Let F be an α-polynomial function. Then EP(α)
n
(F ) is a polynomial
in n of degree at most deg1(F )/2.
Proof. It is enough to verify this lemma on the basis Chµ because of the remark in
Section 3.8. But in this case EP(α)
n
(F ) is explicit (see formula (8)) and the lemma
is obvious (recall that deg1(Chµ) = |µ| + ℓ(µ), see Section 3.4). □
Informally, smaller terms for deg1 are asymptotically negligible. We can now
prove the following weak convergence result:
Proposition 6.2. Let (λ(n))n≥1 be a sequence of random partitions distributed
with Jack measure. For any 1-polynomial function F ∈ Λ (1)
⋆ , when n → ∞ , one
has
F
(
D1/√
n
(
Aα(λ(n))
) )
P(α)
n
− − →F (Ω) ,
where
P(α)
n
− − →means convergence in probability and Ω is given by (3).
Proof. As (R(1)
k )k≥2 is an algebraic basis of Λ (1)
⋆ , it is enough to prove the propo-
sition for any R(1)
k .
Let µ be partition. By Corollary 3.8
(20)
∏
i≤ℓ(µ)
Rµi+1 = Ch µ + terms of degree at most
|µ| + ℓ(µ) − 1 with respect to deg1 .
Together with Lemma 6.1 and the formula (8) for EP(α)
n
(Chµ), this implies:
EP(α)
n

 ∏
i≤ℓ(µ)
Rµi+1

 =
{
n(n − 1) · · · (n − k + 1) + O(nk−1) if µ = 1 k for some k;
o(n
|µ|+ℓ(µ)
2 ) otherwise.
In particular
EP(α)
n
(Rk(D1/√n(λ(n)))) = 1
nk/2 EP(α)
n
(Rk) = δk,2 + O
( 1√n
)
,
VarP(α)
n
(Rk(D1/√n(λ(n)))) = 1
nk
(
EP(α)
n
(
(Rk)2)
− EP(α)
n
(Rk)2
)
= O
(1
n
)
.
40 M. DOŁ ˛ EGA AND V . FÉRAY
Thus, for each k, Rk(D1/√
n(λ(n))) converges in probability towards δk,2. But, by
deﬁnition
Rk(D1/√n(λ(n))) = R(1)
k
(
D1/√n
(
Aα(λ(n))
) )
and (δk,2)k≥2 is the sequence of free cumulants of the continuous diagram Ω (see
[Bia01, Section 3.1]), i.e.
δk,2 = R(1)
k (Ω) . □
