---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-030-83-informal-reformulation-of-theorem-81
section_title: "Informal reformulation of Theorem 8.1"
section_number: 8.3
pages: 58-60
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
independent standard Gaussian random variables(Ξ k)k=2,3,... and consider the ran-
dom series
∆ (α)
∞ (2 cos(θ)) := 1
π
∞∑
k=2
( Ξ k√
k
− γ
k [k is even]
)
sin(kθ)
= 1
π
∞∑
k=2
Ξ k√
k
sin(kθ) − γ/4 + γθ/2π.
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 59
This series is nowhere convergent (almost surely), but it makes sense as a general-
ized Gaussian process with values in the space of generalized functions (C∞(R))′,
that is the dual of the space of inﬁnitely differentiable functions; see [IO02, Section
9] for details.
For polynomials uℓ(x), one has
⟨uℓ, ∆ (α)
∞ ⟩ =
∫ 2
−2
uℓ(x)∆ (α)
∞ (x)dx = 2
∫ π
0
uℓ(2 cos(θ)∆ (α)
∞ (2 cos(θ)) sin(θ)dθ
= 2
π
∞∑
k=2
( Ξ k√
k
− γ
k [k is even]
) ∫ π
0
sin
(
(ℓ + 1)θ
)
sin(kθ)dθ.
Only the integral for k = ℓ + 1 is non-zero (it is equal to 2/π). Thus we get
⟨uℓ, ∆ (α)
∞ ⟩ = Ξ ℓ+1√
ℓ + 1 − γ
ℓ + 1 [ℓ is odd],
which, from Theorem 8.1, is exactly the limit in distribution of
⟨uℓ, ∆ (α)(λ(n))⟩.
As this limit in distribution holds jointly for different values of ℓ, by linearity, one
can replace uℓ by any polynomial P . Hence, ∆ (α)
∞ can be informally seen as the
limit of the random functions ∆ (α)(λ(n)), which justiﬁes equation (5).
APPENDIX A. K EROV POLYNOMIALS
In this Section, we answer some questions of Lassalle concerning Kerov polyno-
mials [Las09]. The results are consequences of the methods or results from Section
3 and thus ﬁt in the scope of this paper. However, as Kerov poly nomials are used
in this paper only as a tool, we decided to present them in Appendix.
A.1. Comparison with Lassalle’s normalizations. Recall that our normalization
is different than the one used by Lassalle. As in Section 3.2, we use boldface font
for quantities deﬁned in Lassalle’s paper [Las09]. Our second bound on the degree
of coefﬁcients of Kµ, implies the following result.
Proposition A.1. The coefﬁcient cµ
ρ of Rρ in Kµ with Lassalle’s normalization is
a polynomial in α divisible by α|ρ|−ℓ(ρ).
Proof. Let us start by a comparison of Lassalle’s conventions with ours. If µ does
not contain a part equal to 1 then
ϑ λ
µ (α ) = zµθ(α)
µ,1|λ|−|µ|(λ),
so that
Chµ(λ) = α− |µ|−ℓ(µ)
2 ϑ λ
µ (α ).
Besides,
Rk(λ ) = α−k/2Rk(λ)
60 M. DOŁ ˛ EGA AND V . FÉRAY
and
ϑ λ
µ (α ) = Kµ (R2, R3, · · · ).
Finally, the coefﬁcient cµ
ρ of Rρ in Kµ with Lassalle’s normalization is related to
the coefﬁcient dµ
ρ of Rρ in Kµ with our conventions by:
cµ
ρ = α
|µ|−ℓ(µ)
2 + |ρ|
2 dµ
ρ .
But we have shown that dµ
ρ is a polynomial in γ = 1−α
√α of degree less than |µ| −
ℓ(µ) − (|ρ| − 2ℓ(ρ)). Thus cµ
ρ is a polynomial in √
α divisible by α|ρ|−ℓ(ρ). Our
parity result for dµ
ρ (second part of Proposition 3.7) implies that cµ
ρ is in fact a
polynomial in α. □
Lassalle had only proved in his article that these quantitie s were rational func-
tions in α. He conjectured that they are polynomials with integer coef ﬁcients
[Las09, Conjecture 1.1]. Our result is weaker than this conj ecture as we are not
able to prove the integrity of the coefﬁcients. However, we a lso proved that the
polynomials are divisible by α|ρ|−ℓ(ρ), which ﬁts with Lassalle’s data [Las09, Sec-
tion 1], but was not mentioned by him.
