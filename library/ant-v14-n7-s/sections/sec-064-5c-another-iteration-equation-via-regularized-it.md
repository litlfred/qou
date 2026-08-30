---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-064-5c-another-iteration-equation-via-regularized-it
section_title: "5C. Another iteration equation via regularized iterated integrals"
section_number: null
pages: 77-78
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
p-adic multiple polylogarithms in [Jarossay 2019], which was centered around a notion of regularization
of iterated integrals, gives us another point of view on how they depend on α. Below, for a power series
S∈ K[[z]], we denote by S[zm] the coefﬁcient of zm in S for all m∈ N. Again we restrict the statement
to positive numbers of iteration of the Frobenius for simplicity, but a similar statement holds for negative
number of iterations.
Proposition 5C.1. For any wordw on e0∪µN and any m0∈ N, there exists a sequence
(c(l,ξ,n)[w](m0)) l∈N
ξ∈µN(K)
n∈N
of elements of K such that, for any˜α∈ N such that q˜α> m0 and m∈ N∗ satisfying|m− m0|p⩽ q−˜α, we
have
Li†
q,˜α[w][zm]=
∞∑
n=0
(q˜α)n
(∑
l∈N
∑
ξ
c(l,ξ,n)[w](m0)ξ−m(m− m0)l
)
.
Proof. In [Jarossay 2019, Section 3], we have deﬁned a notion of regularized iterated integrals attached
to any sequence of differential forms among pα dz
z , pαdz
z−ξ ,ξ∈µN(K), d(z pα
)
z pα−ξ pα ,ξ∈µN(K). We have
computed these regularized iterated integrals by induction on the depth, and this gives us information
on how they depend on α. Namely, each regularized iterated integral is a rigid analytic function on
P1,an\⋃
ξ∈µN(K) B(ξ, 1) which has a power series expansion∑∞
m=0 cmzm satisfying the following property:
for any m0∈{ 0,..., pα− 1}, there exists a sequence (c(l,ξ)(m0)) l∈N
ξ∈µN(K)
of elements of K such that, for
all m∈ N with|m− m0|p⩽ p−α, we have cm=∑∞
l=0
∑
ξ c(l,ξ)(m0)ξ−m(m− m0)l.
In [Jarossay 2019, Appendix B], we have showed that the numbers c(l,ξ)(m0) have an expression
as certain sums of series involving multiple harmonic sums, and particularly prime weighted multiple
harmonic sums.
1744 David Jarossay
In [Jarossay 2019, Section 4], we have showed an expression of each Li†
p,α[w] as a linear combination
of regularized p-adic iterated integrals over the ring of p-adic cyclotomic multiple zeta valuesζp,α(w′).
Combining these facts with the results of Sections 1 and 2 on how ζq,˜α and harq˜α depend on˜α, we
deduce the result. □
