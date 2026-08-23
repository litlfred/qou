---
doc_id: motivicperiodsandp1minus3pointsv3
doc_title: "Motivic periods and P^1 minus 3 points"
section_id: sec-063-61-eichler-shimura-integrals-denote-the-space-of
section_title: "Eichler-Shimura integrals. Denote the space of homogenous poly-"
section_number: 6.1
pages: 20-21
source_pdf: MotivicPeriodsandP1minus3pointsv3.pdf
source_sha256: 7870572b8cc316d0
doc_brief: "Motivic periods and P^1 minus 3 points — This is a review of the theory of the motivic fundamental grou p of the projective line minus three points, and its relation to mult iple zeta values."
---
nomials of degree n ≥ 0 with rational coeﬃcients by
Vn =
⨁
i+j=n
QX iY j
It admits a right action of Γ via the formula ( X, Y )|γ = (aX + bY, cX + dY ), where
γ =
(a b
c d
)
. Let f (τ ) be a modular form of weight k for Γ. Deﬁne
f (τ ) = (2 πi)k−1f (τ )(X − τ Y )k−2dτ ∈ Γ( H, Ω 1
H ⊗ Vk−2)
It satisﬁes the invariance property f
(γ(τ ))
⏐
⏐
γ = f
(τ ) for all γ ∈ Γ. For f a cusp
form, the classical Eichler-Shimura integral (see, e.g., [ 29]) is
∫ ∞
0
f (τ ) =
k−1∑
n=1
cnL(f, n)X k−n−1Y n−1 (6.1)
where cn are certain explicit constants (rational multiples of a pow er of π) and
L(f, s) is the analytic continuation of the L-function L(f, s) = ∑
n≥1
an
ns of f ,
where f (τ ) = ∑
n≥1 anqn and q = e2πiτ . Manin showed that if f is a Hecke
eigenform, there exist ω+
f , ω−
f ∈ R such that
∫ ∞
0
f (τ ) = ω+
f P +
f (X, Y ) + ω−
f P −
f (X, Y )
where P ±
f (X, Y ) ∈ Vk−2 ⊗ Q are polynomials with algebraic coeﬃcients which are
invariant (resp. anti-invariant) with respect to ( X, Y ) ↦→(−X, Y ).
Recall that the Eisenstein series of weight 2 k, for k ≥ 2, is deﬁned by
e2k(q) = − B2k
4k +
∑
n≥1
σ2k−1(n)qn , q = e2πiτ
where B2k is the 2 kth Bernoulli number, and σ denotes the divisor function. The
corresponding integrals for Eisenstein series diverges. Z agier showed how to extend
the deﬁnition of the Eichler-Shimura integrals to the case e2k, giving [29]
(2k − 2)!
2 ζ(2k−1)(Y 2k−2−X 2k−2)− (2πi)2k−1
4k(2k − 1)
∑
a+b=2k,a,b ≥1
(2k
a
)
BaBbX a−1Y b−1
(6.2)
Manipulating this formula leads to expressions for the odd R iemann zeta values
in terms of Lambert series similar to the following formula d ue to Ramanujan:
ζ(3) = 7
180 π3 − 2
∑
n≥1
1
n3(e2nπ − 1) .
It converges very rapidy. One wants to think of (6 .2) as pointing towards a modular
construction of ζm(2k − 1).
Motivic periods and P1\{ 0, 1, ∞} 21
