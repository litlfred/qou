---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-004-15-second-main-result-polynomiality-of-structure
section_title: "Second main result: polynomiality of structure constants of Jack characters"
section_number: 1.5
pages: 10-12
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
ters. It follows from the work of Lassalle – see Proposition 2.9 – that the functions
Ch(α)
µ span linearly the algebra of α-polynomial functions denoted by Λ (α)
⋆ (when
µ runs over integer partitions of all sizes). Hence, there exi st some rational num-
bers g(α)
µ,ν;π, depending on α such that
(9) Ch(α)
µ · Ch(α)
ν =
∑
π partition
of any size
g(α)
µ,ν;π Ch(α)
π .
These numbers are often called structure constants of the basis (Ch(α)
µ ). It is a
worthy goal to understand them, because they describe the multiplicative structure
of the algebra.
Our second main result is a polynomiality result for these st ructure constants
with precise bounds on the degree: let
n1(µ) = |µ| + ℓ(µ),
n2(µ) = |µ| − ℓ(µ),
n3(µ) = |µ| − ℓ(µ) + m1(µ).
Then we have:
Theorem 1.4. Fix three partitions µ, ν and π. The structure constant g(α)
µ,ν;π is a
polynomial in γ = √
α−1 − √α with rational coefﬁcients and of degree at most
min
i=1,2,3
ni(µ) + ni(ν) − ni(π).
Moreover, if n1(µ) + n1(ν) − n1(π) is even (respectively, odd), it is an even (re-
spectively, odd) polynomial.
1.5.1. Other applications of the second main result. In addition of the main pur-
pose of this paper, Theorem 1.4 can be applied to several diff erent problems from
the literature.
• It contains a ﬁfty-year old result from Farahat and Higman, stating that the
structure constants of the center of the symmetric group alg ebra behave
polynomially in n [FH59].
• A natural analog of the center of the symmetric group algebrais the Hecke
algebra of the pair (S2n, Hn), see e.g. [Mac95, Section 7.2] for an intro-
duction to it. Theorem 1.4 implies also an analog of Farahat and Higman’s
result in this context: up to some explicit normalization fa ctor, structure
constants also behave polynomially inn1. The same result has been proved
independently by Tout [Tou13].
1Let us also mention the work of Aker and Can [AC12] in this dire ction. Unfortunately, a factor
2nn! is missing in the main result and the authors are not able to correct this [Can12]
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 11
• Goulden and Jackson [GJ96a], have deﬁned, using Jack polyno mials, an
interpolation between the structure constants of both alge bras. By con-
struction, these quantities are rational functions in α but they were conjec-
tured to be in fact polynomials in α − 1 with non-negative integer coefﬁ-
cients having some combinatorial interpretation [GJ96a, Section 4]. Here,
we prove that they are polynomials in α (or equivalently in α − 1) with
rational coefﬁcients. Unfortunately, we are not able to pro ve either the
integrity or the positivity of the coefﬁcients.
• We are also able to prove two conjectures of Matsumoto [Mat10 , Section
9], arising in the context of matrix integrals (Section B.3).
• We can give a short proof of a recent result of Vassilieva [Vas 13] which
generalizes a famous result of Dénes [Dén59] for the number o f minimal
factorizations of a cycle in the symmetric group.
The link between our main result and the ﬁrst two items is pres ented in Section
5, while the connection with the last three items is explained in Appendix B.
1.5.2. Tool: Kerov’s polynomial for Jack characters.Let us now say a word about
the proof of our second main result.
The algebra Λ (α)
⋆ , linearly spanned by the functions Ch(α)
µ , admits also some
interesting algebraic basis: for example the basis of free cumulants (R(α)
k )k≥2 –
see Section 2. Thus Ch(α)
µ writes uniquely as a polynomial in free cumulants. As
it was ﬁrst considered by Kerov in the case α = 1 , it is usually termed Kerov’s
polynomial (or Kerov’s expansionto avoid repetition of the word polynomial).
In [Las09], Lassalle has described an inductive algorithm to compute the coefﬁ-
cients of this expansion. In this paper, by a careful analysis of Lassalle’s algorithm,
we obtain some polynomiality results (with several bounds on the degree) for these
coefﬁcients: see Propositions 3.7, 3.10 and 3.13.
Clearly, writing some functions in a multiplicative basis m ay help to under-
stand how to multiply them and we can deduce Theorem 1.4 from these results on
Kerov’s polynomials.
While inappropriate to obtain close formulas, this way of st udying structure
constants is, as far as we know, original. Usually, results of structure constants are
obtained using their combinatorial description of via representation theory tools
[FH59, GJ96b, IK99, GS98, Tou13].
To ﬁnish this paragraph, let us mention that there is an appealing positivity con-
jecture on Kerov’s polynomials for Jack characters [Las09,Conjecture 1.2]. While
we can not solve this conjecture, our analysis of Lassalle’s algorithm gives some
partial results: we prove in general the polynomiality of th e coefﬁcients and we
compute a few speciﬁc values that were conjectured by Lassalle (see Appendix A).
Another interesting application of our result on Kerov’s po lynomials is a new
proof of the polynomial dependence of Jack polynomials in term of Jack parameter
α, which was an important open problem in the early nineties. This is presented in
Section 3.6.
12 M. DOŁ ˛ EGA AND V . FÉRAY
1.6. An open problem: edge ﬂuctuations of Jack measure. Another natural
question on asymptotics of Jack measure is the behavior of th e ﬁrst few rows of
the Young diagrams. This kind of results, orthogonal to the o nes in this paper, is
called edge ﬂuctuations. Our law of large number on the bulk on Young diagrams
implies that, for any ﬁxed positive integer k and real number C < 1,
P
[ (λ(n))k
√n ≤ 2 C√α
]
→ 0,
while Lemma 6.3 tells us that (λ(n))k/√n exceeds (2e)/√α with exponentially
small probability.
A natural conjecture, considering the caseα = 1 where the edge ﬂuctuations are
well described (see [Oko00, BOO00] and references therein) and the link with β-
ensemble, would be the following: for each integerk ≥ 1, the quantity (λ(n))k/√n
converges in probability towards 2/√α and the joint vector
[
n1/3
((λ(n))j
√n − 2√α
)]
1≤j≤k
converges in law towards the β-Tracy-Widom distribution, which has been intro-
duced and studied in [RRV11] to study edge ﬂuctuations ofβ-ensemble. Naturally,
a similar conjecture can be formulated for the lengths of the ﬁrst columns of the
Young diagram λ(n).
These conjectures hold true for the ﬁrst row/column in the ca se α = 1 /2 and
α = 2 . The proof uses the combinatorial interpretation of Jack me asure at these
particular values of α, using Robinson-Schensted on random ﬁxed point free invo-
lutions: see [BR01].
We have not made computer experiments to conﬁrm this conjecture and let this
problem wide open for future research.
