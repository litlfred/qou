---
doc_id: arxiv-q-alg-9608020v2
doc_title: "Shifted Jack polynomials, binomial formula, and applications"
section_id: sec-008-5-f-ormula-for-θ-dimension-of-a-skew-diagram-λµ
section_title: "F ormula for θ-dimension of a skew diagram λ/µ . Deﬁne the θ-dimension"
section_number: 5
pages: 6-7
source_pdf: 9608020v2.pdf
source_sha256: 727268098db7f23d
doc_brief: "Shifted Jack polynomials, binomial formula, and applications — In this note we prove an explicit binomial formula for Jack poly nomials and discuss some applications of it. 1."
---
θ-dimλ/µ of a skew diagram λ/µ as the following coeﬃcient
(5.1) (
∑
xi)kPµ (x;θ) =
∑
|λ |=|µ |+k
θ-dimλ/µ P λ (x;θ), k = 1, 2,....
If θ = 1 then θ-dimλ/µ equals the number of the standard tableaux on λ/µ ; for
generalθ each tableauT is counted with a certain weight ψ ′
T (θ) given in [M], section
VI.6. In particular, if µ = ∅ then (see (5.6) below for a proof using shifted Jack
polynomials)
θ-dimλ = |λ|!/H (λ).
We have
Proposition.
(5.2) θ-dimλ/µ
θ-dimλ = P ∗
µ (λ;θ)
|λ|(|λ| − 1) · · ·(|λ| − |µ | + 1).
This proposition can be deduced from (3.8) and [La,K] (see th e remark above),
but it easier to give a direct proof, which uses the very same a rgument as in [OO],
section 9.
First one proves that
SHIFTED JACK POLYNOMIALS, BINOMIAL FORMULA, AND APPLICATI ONS 7
Lemma.
(5.3) (
∑
xi − |µ |)P ∗
µ (x;θ) =
∑
|λ |=|µ |+1
θ-dimλ/µ P ∗
λ (x;θ).
Proof. Letf be the diﬀerence of the LHS and RHS in (5.3). By (2.3) and (5.1) we
have degf ≤ |µ |. One easily checks that f (ν) = 0 for all |ν| ≤ |µ |. It follows that
f = 0. □
Applying this lemma k times, where k = |λ| − |µ |, we obtain
(5.4) (
∑
xi − |µ |) · · · (
∑
xi − |µ | −k + 1)P ∗
µ (x;θ) =
∑
|ν |=|µ |+k
θ-dimν/µ P ∗
ν (x;θ).
Evaluation of (5.4) at x =λ gives
(5.5) ( |λ| − |µ |)!P ∗
µ (λ) = θ-dimλ/µ P ∗
λ (λ).
In particular, for µ = ∅ one has
(5.6) |λ|! = θ-dimλP ∗
λ (λ).
Dividing (5.5) by (5.6) we obtain (5.2). □
