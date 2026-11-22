---
doc_id: arxiv-1603.07827v1
doc_title: "Braiding With Majorana Fermions"
section_id: sec-007-4-braiding-operators-and-universal-quantum-gates
section_title: "BRAIDING OPERATORS AND UNIVERSAL QUANTUM GATES"
section_number: 4
pages: 8-9
source_pdf: arxiv-1603.07827v1.pdf
source_sha256: 8f4959c11d26c8c2
toc_source: inferred
doc_brief: "Braiding with Majorana fermions (Kauffman–Lomonaco, Proc. SPIE 9873 (2016), arXiv:1603.07827) — Clifford Braiding Theorem; SU(2) representations of B₃ from quaternions; Fibonacci model"
---
A key concept in the construction of quantum link invariants is the association of a Yang-Baxter operator R to
each elementary crossing in a link diagram. The operator R is a linear mapping
R: V ⊗V −→V ⊗V
deﬁned on the 2-fold tensor product of a vector space V, generalizing the permutation of the factors (i.e.,
generalizing a swap gate when V represents one qubit). Such transformations are not necessarily unitary in
topological applications. It is useful to understand when they can be replaced by unitary transformations for
the purpose of quantum computing. Such unitary R-matrices can be used to make unitary representations of
the Artin braid group.
A solution to the Yang-Baxter equation, as described in the last paragraph is a matrix R, regarded as a
mapping of a two-fold tensor product of a vector space V ⊗V to itself that satisﬁes the equation
(R ⊗I)(I ⊗R)(R ⊗I) = (I ⊗R)(R ⊗I)(I ⊗R).
=
R
I
R
I
R
I
R
I
R
I
R
I
R
I
R
I
Figure 5. The Yang-Baxter equation
From the point of view of topology, the matrix R is regarded as representing an elementary bit of braiding
represented by one string crossing over another.
In Figure 5 we have illustrated the braiding identity that
corresponds to the Yang-Baxter equation. Each braiding picture with its three input lines (below) and output
lines (above) corresponds to a mapping of the three fold tensor product of the vector space V to itself, as required
by the algebraic equation quoted above. The pattern of placement of the crossings in the diagram corresponds
to the factors R ⊗I and I ⊗R. This crucial topological move has an algebraic expression in terms of such a
matrix R. We need to study solutions of the Yang-Baxter equation that are unitary. Then the R matrix can be
seen either as a braiding matrix or as a quantum gate in a quantum computer.
