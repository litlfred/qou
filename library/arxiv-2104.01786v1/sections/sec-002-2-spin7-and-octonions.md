---
doc_id: arxiv-2104.01786v1
doc_title: "Spin(11, 3), particles and octonions"
section_id: sec-002-2-spin7-and-octonions
section_title: "Spin(7) and octonions"
section_number: 2
pages: 6-7
source_pdf: 2104.01786v1.pdf
source_sha256: 34087d5063ef5507
toc_source: outline
doc_brief: "Spin(11, 3), particles and octonions — The fermionic ﬁelds of one generation of the Standard Model, including the Lorentz spinor degrees of freedom, can be identiﬁed with components of a single real"
---
Spin(7) and octonions
2.1
Octonions
Octonions, see e.g., [23], are objects that can be represented as linear combinations of the unit
octonions 1, e1, . . . , e7
x = x0 + x1e1 + . . . + x7e7,
x0, x1, . . . , x7 ∈R.
(4)
The conjugation is again the operation that ﬂips the signs of all the imaginary coeﬃcients
x = x0 −x1e1 −. . . −x7e7,
(5)
and we have
|x|2 = xx = (x0)2 + (x1)2 + . . . + (x7)2 ≡|x|2.
(6)
For later purposes, we note that if we represent an octonion as an 8-component column with
entries x0, x1, . . . , x7, denoted by the same symbol x, we can write the norm as |x|2 = xTx.
Octonions O form a normed division algebra that satisﬁes the composition property |xy|2 =
|x|2|y|2. The cross-products of the imaginary octonions e1, . . . , e7 is most conveniently encoded
into a 3-form in R7 that arises as
C(x, y, z) = ⟨xy, z⟩,
x, y, z ∈Im(O),
(7)
where the inner product ⟨·, ·⟩in O comes by polarising the squared norm
⟨x, y⟩= Re(xy),
x, y ∈O.
(8)
6
One convenient form of C is
C = e567 + e5 ∧(e41 −e23) + e6 ∧(e42 −e31) + e7 ∧(e43 −e12),
(9)
where the notation is eijk = ei ∧ej ∧ek. It is then easy to read oﬀthe products of distinct
imaginary octonions from (9). For example, e5e6 = e7, which is captured by the ﬁrst term in
(9). The particular form (9) of the cross-product on Im(O) is convenient because it manifests
the Spin(3)×Spin(4) subgroups of Spin(7), and also one of the two maximal subgroups Spin(4)
of the group of automorphisms of the octonions G2 ⊂Spin(7) that preserves (9).
Octonions are non-commutative and non-associative, but alternative. The last property
is equivalent to saying that any two imaginary octonions (as well as the identity) generate a
subalgebra that is associative, and is a copy of the quaternion algebra H.
