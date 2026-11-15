---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-030-74-skein-polynomial
section_title: "Skein polynomial"
section_number: 7.4
pages: 52-53
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
table1 in [J].) For 4-braids several new 14 crossing knots can be ruled out, for example 1421199.
Remark 7.3 The use of P to restrict the possible values of e is usually most effective, but not indispensable. There
are other conditions on e, originating from Bennequin’s work [Be], that can be more applicable in certain cases where
the calculation of P is tedious. Also, when t is a root of unity of order n, the tests depend only on e mod 2n.
Remark 7.4 Note that the quantity χ in (24) is equal to utr ψ2, where u = √−t +
1
√−t and ψ2 is the Burau matrix of
B3 (see the explanation in [K]). Thus one can obtain similar estimates for values of Q on 3-braids.
7.4.
Skein polynomial
Now it is natural to look at the full 2-variable skein polynomial X. We have, as in (47), for β ∈B4 of exponent sum e,
Xˆβ(q,λ) = −
√
λ
e−3 ∑
Y⊢4
tr πY(q) eWY(q,λ),
where the weights eWY are given in λ-coefﬁcients by table 3. (They are all polynomials in λ of degree 3, with coefﬁcients
being rational expressions in q.) Now, with given e and P, we have 4 equations (the coefﬁcients in λ) in 3 unknowns
(the traces of π211, π31 and π22; we use here the partition notation for the subscripts). However, the restriction of
the matrix in table 3 to the columns of π211, π31 and π22 has rank 2. This means that two of the Xi = [X]λi+(e−3)/2
for 0 ≤i ≤3 determine the other two. One could believe now to use this as a 4-braid test. However, these two
relations result from the general substitutions λ = 1 and λ = 1/q2 that turn X into the component parity count or 1.
These substitutions kill all trace weights except of the trivial or parity representation, and for these representations the
weights become also independent on the braid group. Thus the relations between the Xi will hold whenever MWF ≤4,
and are useless as a 4-braid test. In a similar vein, one has
Proposition 7.3 If a braid β has MWF(β) ≤4, then V(ˆβ) and ∆(ˆβ) together with the exponent sum [β] = e, determine
P(ˆβ).
1The second duplication was noted in the remarks after Jones’s table, but not referred to correctly in its last column.
