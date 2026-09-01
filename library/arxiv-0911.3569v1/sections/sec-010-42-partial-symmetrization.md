---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-010-42-partial-symmetrization
section_title: "Partial symmetrization."
section_number: 4.2
pages: 13-13
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
---
acts on C[x] by the rule σ(f)(x1,...,x m) =f(xσ(1),...,x σ(m)). Notice that
σ(xα) =
m∏
i=1
xα(i)
σ(i) =
m∏
i=1
xα◦σ−1(i)
i = xα◦σ−1
.
For{i,j}⊆ [m], let τij be the transposition that exchanges i and j and ﬁxes all
other elements of [m].
Lemma 4.3. Let 0≤ λ≤ 1 and{i,j}⊆ [m], and let T (λ)
ij = (1−λ) +λτij. If
f∈ S[x]MA is stable and multiaﬃne then T (λ)
ij f∈ S[x]MA is stable and multiaﬃne.
Proof. If f is multiaﬃne then (1 −λ)f +λτij(f) is also multiaﬃne. We apply
Theorem 3.4 to show that T =T (λ)
ij preserves stability of multiaﬃne polynomials.
By permutation we can assume that {i,j} ={1, 2}. The algebraic symbol of T is
T ((x + y)[m]) =T ((x1 +y1)(x2 +y2))·
m∏
i=3
(xi +yi).
Clearly, this is stable if and only if the same is true ofT ((x1+y1)(x2+y2)). Exercise
4.4 completes the proof. □
Exercise 4.4. Use the results of Sections 2.4 or 3.1 to show that for 0 ≤ λ≤ 1,
the polynomial
x1x2 + ((1−λ)x1 +λx2)y2 + (λx1 + (1−λ)x2)y1 +y1y2
is real stable.
