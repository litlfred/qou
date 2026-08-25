---
doc_id: arxiv-2104.01786v1
doc_title: "Spin(11, 3), particles and octonions"
section_id: sec-002-2-spin7-and-octonions
section_title: "Spin(7) and octonions"
section_number: 2
pages: 6-8
source_pdf: 2104.01786v1.pdf
source_sha256: 34087d5063ef5507
doc_brief: "Spin(11, 3), particles and octonions — The fermionic ﬁelds of one generation of the Standard Model, including the Lorentz spinor degrees of freedom, can be identiﬁed with components of a sin gle real"
---
2.1 Octonions
Octonions, see e.g., [23], are objects that can be represented as lin ear combinations of the unit
octonions 1,e 1,...,e 7
x =x0 +x1e1 +... +x7e7, x 0,x 1,...,x 7 ∈ R. (4)
The conjugation is again the operation that ﬂips the signs of all the im aginary coeﬃcients
x =x0 −x1e1 −... −x7e7, (5)
and we have
|x|2 =xx = (x0)2 + (x1)2 +... + (x7)2 ≡ |x|2. (6)
For later purposes, we note that if we represent an octonion as an 8-component column with
entriesx0,x 1,...,x 7, denoted by the same symbol x, we can write the norm as |x|2 =xTx.
Octonions O form a normed division algebra that satisﬁes the composition proper ty |xy|2 =
|x|2|y|2. The cross-products of the imaginary octonions e1,...,e 7 is most conveniently encoded
into a 3-form in R7 that arises as
C(x,y,z ) = ⟨xy,z ⟩, x,y,z ∈ Im(O), (7)
where the inner product ⟨·, ·⟩ in O comes by polarising the squared norm
⟨x,y ⟩ = Re(xy), x,y ∈ O. (8)
6
One convenient form of C is
C =e567 +e5 ∧ (e41 −e23) +e6 ∧ (e42 −e31) +e7 ∧ (e43 −e12), (9)
where the notation is eijk = ei ∧ej ∧ek. It is then easy to read oﬀ the products of distinct
imaginary octonions from (9). For example, e5e6 = e7, which is captured by the ﬁrst term in
(9). The particular form (9) of the cross-product on Im( O) is convenient because it manifests
the Spin(3) × Spin(4) subgroups of Spin(7), and also one of the two maximal subg roups Spin(4)
of the group of automorphisms of the octonions G2 ⊂ Spin(7) that preserves (9).
Octonions are non-commutative and non-associative, but alterna tive. The last property
is equivalent to saying that any two imaginary octonions (as well as th e identity) generate a
subalgebra that is associative, and is a copy of the quaternion algeb ra H.
2.2 Cliﬀord algebra Cliﬀ 7
Octonions give rise to a very convenient model for the Cliﬀord algebr a Cliﬀ 7. Indeed, we can
identify
Cliﬀ 7 = Im(O). (10)
To realise this identiﬁcation, we consider the endomorphisms of O given by the operators
Ei :=Lei (11)
of left multiplication by an imaginary octonion. These operators anti- commute and square to
minus the identity
EiEj +EjEi = −2δij. (12)
Thus, the generate the Cliﬀord algebra Cliﬀ 7.
The Cliﬀord generators can be described very explicitly as 8 × 8 anti-symmetric matrices
acting on 8-dimensional columns that represent elements of O. Using the octonion product
encoded in (9) we get
E1 = −E12 +E38 −E47 +E56 (13)
E2 = −E13 −E28 +E46 +E57
E3 = −E14 +E27 −E36 +E58
E4 = −E15 −E26 −E37 −E48
E5 = −E16 +E25 +E34 −E78
E6 = −E17 −E24 +E35 +E68
E7 = −E18 +E23 +E45 −E67.
These are all 8 × 8 real (anti-symmetric) matrices, and the octonions in the column a re ordered
as I,e 1,...,e 7. They also have the property EiI =ei, where both I,e i are 8-component columns.
7
