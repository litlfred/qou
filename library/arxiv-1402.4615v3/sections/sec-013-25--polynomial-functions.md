---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-013-25--polynomial-functions
section_title: "-polynomial functions"
section_number: 2.5
pages: 17-19
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
Deﬁnition 2.8. We say that F is an α-polynomial function on the set of (continuous)
Young diagrams if
λ 7→F(Tα−1,1(λ))
is a polynomial function. The set of α-polynomial functions is an algebra which
will be denoted by Λ(α)
⋆.
Using Deﬁnition 2.1, this means that the polynomial F(α−1λ1, · · · , α−1λh) is
symmetric in λ1 −1, . . . , λh −h. Equivalently (by a change of variables), F is
symmetric in αλ1 −1, . . . , αλh −h or in
λ1 −1
α, . . . , λh −h
α.
The last characterization is the deﬁnition of what is usually called an α-shifted
symmetric function [OO97, Las08].
It would be equivalent to ask in the deﬁnition of α-polynomial functions that
λ 7→F(Aα−1(λ))
18
M. DOŁ ˛EGA AND V. FÉRAY
is a polynomial function, where Aα−1(λ) = T√α−1,√α(λ) is an α-anisotropic
Young diagram. Indeed, T√α−1,√α(λ) is a dilatation of Tα−1,1(λ) and the property
of being polynomial is invariant by dilatation of the argument.
Therefore, the α-anisotropic moments and free cumulants deﬁned by
M(α)
k
(λ) := M(1)
k
(Aα(λ)) ,
R(α)
k (λ) := R(1)
k
(Aα(λ)) ,
are α-polynomial. Moreover, the families (M(α)
k
)k≥2 and (R(α)
k )k≥2 are algebraic
bases of the algebra Λ(α)
⋆
of α-polynomial functions.
The following property is due to Lassalle (under a slightly different form).
Proposition 2.9. When µ runs over all partitions, Jack characters

Ch(α)
µ

µ form
a linear basis of the algebra of α-polynomial functions.
Proof. In [Las08, Section 3], Lassalle builds a linear isomorphism λ 7→λ# be-
tween symmetric functions and α-shifted symmetric functions. Then he shows
[Las08, Proposition 2] that, for any two partitions λ and µ with |λ| ≥|µ|,
α(|µ|−ℓ(µ))/2p#
µ (λ) = Ch(α)
µ (λ).
It is straight-forward to check that, for |λ| < |µ|, both sides of equality above are
equal to 0. Hence, as functions on all Young diagrams, Ch(α)
µ
is equal, up to a
scalar multiple, to p#
µ . The facts that pµ is a basis of the symmetric function ring
and f 7→f # a linear isomorphism conclude the proof.
□
In particular, they are α-polynomial functions and can be expressed in terms of
the algebraic bases above.
Proposition 2.10. Let µ be a partition and α > 0 a ﬁxed real number. There exist
unique polynomials L(α)
µ
and K(α)
µ
such that, for every λ,
Ch(α)
µ (λ) = L(α)
µ

M(α)
2
(λ), M(α)
3
(λ), · · ·

;
Ch(α)
µ (λ) = K(α)
µ

R(α)
2 (λ), R(α)
3 (λ), · · ·

.
The polynomials K(α)
µ
have been introduced by Kerov in the case α = 1 [Ker00b,
Bia03] and by Lassalle in the general case [Las09] and they are called Kerov poly-
nomials. Once again, our normalizations are different from his. We will explain
this choice later.
From now on, when it does not create any confusion, we suppress the superscript
(α).
We present a few examples of polynomials Lµ and Kµ (in particular the case of
a one-part partition µ of length lower than 6). This data has been computed using
LARGE DIAGRAMS AND STRUCTURE CONSTANTS
19
the one given in [Las09, page 2230]. Recall that we set γ := 1−α
√α .
L(1) = M2,
L(2) = M3 + γM2,
L(3) = M4 −2M2
2 + 3γM3 + (1 + 2γ2)M2,
L(4) = M5 −5M3M2 + 6γM4 −11γM2
2 + (5 + 11γ2)M3 + (7γ + 6γ3)M2,
L(5) = M6 −6M4M2 −3M2
3 + 7M3
2 + 10γM5 −45γM3M2
+ (15 + 35γ2)M4 −(25 + 60γ2)M2
2
+ (55γ + 50γ3)M3 + (8 + 46γ2 + 24γ4)M2,
L(2,2) = M2
3 + 2γM3M2 −4M4 + (γ2 + 6)M2
2 −10γM3 −(6γ2 + 2)M2.
Similarly,
K(1) = R2,
K(2) = R3 + γR2,
K(3) = R4 + 3γR3 + (1 + 2γ2)R2,
K(4) = R5 + 6γR4 + γR2
2 + (5 + 11γ2)R3 + (7γ + 6γ3)R2,
K(5) = R6 + 10γR5 + 5γR3R2 + (15 + 35γ2)R4 + (5 + 10γ2)R2
2
+ (55γ + 50γ3)R3 + (8 + 46γ2 + 24γ4)R2,
K(2,2) = R2
3 + 2γR3R2 −4R4 + (γ2 −2)R2
2 −10γR3 −(6γ2 + 2)R2.
A few striking facts appear on these examples. First, all coefﬁcients are poly-
nomials in the auxiliary parameter γ: we prove this fact in the next section with
explicit bounds on the degrees. Besides, for one part partition, polynomials K(r)
have non-negative coefﬁcients. We are unfortunately unable to prove this state-
ment, which is a slightly more precise version of [Las09, Conjecture 1.2]. A similar
conjecture holds for several part partitions, see also [Las09, Conjecture 1.2].
