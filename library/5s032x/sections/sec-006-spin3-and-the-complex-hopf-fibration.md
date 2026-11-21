---
doc_id: 5s032x
doc_title: "The Standard Model Symmetry and Qubit Entanglement"
section_id: sec-006-spin3-and-the-complex-hopf-fibration
section_title: "Spin(3) and the Complex Hopf Fibration"
section_number: null
pages: 7-7
source_pdf: 5S032X.pdf
source_sha256: 17761383781f7bdc
toc_source: outline
doc_brief: "The Standard Model Symmetry and Qubit Entanglement — quantum description."
---
Spin(3) and the Complex Hopf Fibration
We will now connect the story so far with the formalism in Ref. [28]. Thus, consider matrices of the form
X(r, c) =

r
Lc
Lc∗−r

, r ∈R, c ∈C,
(15)
where by Lc we mean left-multiplication by c (for the commutative complex numbers, this is obviously not a salient
distinction, but it will become important in the generalization to higher division algebras). This is just the matrix
rψ · σ from Eq. (6) with r = x3 and c = x1 −ix2.
These matrices generate the Clifford algebra Cℓ3, as they fulfill the relation
X(r, c)X(r, c) = (r2 + |c|2)1.
(16)
Furthermore, these matrices generate the group Spin(3) in the case of r2 + |c|2 = 1: a rotation along an axis in R3
can be realized by an even number of reflections, and conjugating a matrix of the form given in Eq. (16) by another,
yielding
X(r, c) −→−X(r′, c′)X(r, c)X(r′, c′), r′2 + |c|′2 = 1,
(17)
produces a reflection along (r′, c′) ∈R3 [28].
The group Spin(3) here can also be understood as the equivariance group of the complex Hopf fibration, that is,
the Hopf map is equivariant with respect to the action of Spin(3). This becomes explicit by noting that the map can
be written in terms of coset spaces [57]:
S3
S1
−→S2 ≡Spin(3)
Spin(1)
Spin(2)
Spin(1)
−→
Spin(3)
Spin(2).
(18)
Here, the action of Spin(3) on S2 is induced by its action on R3, with S2 just being the set of unit-length vectors
of R3, and the action of Spin(3) on S3 is given by the isomorphism Spin(3) ≃Sp(1) ≃U(1, H), which acts by left
multiplication on (unit) quaternions, i. e. S3.
