---
doc_id: quaternioms
doc_title: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations"
section_id: sec-006-quaternionic-and-octonionic-preliminaries
section_title: "Quaternionic and Octonionic Preliminaries"
section_number: null
pages: 6-7
source_pdf: quaternioms.pdf
source_sha256: becedcbc858611dd
toc_source: outline
doc_brief: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations — 45 sections: Front matter; Introduction; Extended Related Work"
---
The hypercomplex extensions considered here replace the complex scalar ﬁeld by
either H or O, together with compatible notions of inner product, adjoint, dynamics,
and composition.
Notation on SU(2) and context.
Unless explicitly stated otherwise, SU(2) denotes the standard group of 2 × 2 complex
special unitaries acting on a single complex qubit. When we speak of “quaternionic gates
realised as SU(2) operations” or of “native SU(2) control” on hardware, we always mean
the image of quaternionic unitaries under the embedding ι : H֒ →M2(C), acting on an
encoded complex qubit.
Quaternionic Hilbert modules.
A (right) quaternionic Hilbert module (HH, ⟨·, ·⟩) is a right H-module endowed with
an H-valued inner product satisfying the following:
1.
⟨ψ, φa + χb⟩= ⟨ψ, φ⟩a + ⟨ψ, χ⟩b
(right linearity);
2.
⟨φ, ψ⟩= ⟨ψ, φ⟩
(quaternionic Hermiticity);
3.
⟨ψ, ψ⟩∈R≥0 and vanishes iff ψ = 0
(positivity).
States (quaternionic qubits) have the form |φ⟩= q1|0⟩+ q2|1⟩with qi ∈H and
∥q1∥2 + ∥q2∥2 = 1. Born probabilities are real: P(ψ|φ) = ∥⟨ψ, φ⟩∥2 ∈R≥0. Linear
operators are right H-linear maps A : HH →HH with an adjoint A† determined by
⟨ψ, Aφ⟩= ⟨A†ψ, φ⟩. Unitary dynamics U†U = I is well-deﬁned, and—crucially—tensor
products over H are associative:
(H1 ⊗H2) ⊗H3 ∼= H1 ⊗(H2 ⊗H3),
with inner product on simple tensors ⟨u1⊗u2, v1⊗v2⟩= ⟨u1, v1⟩⟨u2, v2⟩. This guaran-
tees a canonical multipartite structure and permits the usual notions of separability and
entanglement (Theorem 1 in the main text).
Matrix embedding H֒ →M2(C).
The multiplicative embedding ι : H →M2(C), sends unit quaternions to SU(2) and
preserves norms up to a factor (∥ι(q)∥2
F = 2∥q∥2). It allows one to simulate quaternionic
circuits in the complex model with polynomial overhead (and conversely embed complex
circuits into the quaternionic setting), and implies that native SU(2) control translates
directly into single-quaternionic qubit gate synthesis (see Appendix A).
Octonionic modules and the associator.
Attempting to transplant the above structure to O runs into foundational obstacles
controlled by the associator [x, y, z]:
•
Adjoint/inner product ambiguity: Without associativity, the deﬁning relation ⟨ψ, Aφ⟩=
⟨A†ψ, φ⟩becomes parenthesization-dependent unless dynamics and observables are
conﬁned to associative subalgebras.
•
Non-associative tensor products: For right O-modules HA, HB, HC, the identiﬁcation
(HA ⊗HB) ⊗HC ∼= HA ⊗(HB ⊗HC) is not canonical in general; different parenthe-
sizations yield inequivalent scalar actions. Thus, there is no canonical multipartite
structure unless one restricts to an associative (quaternionic) sector.
•
Path dependence in evolution: For H(t) ∈O, the propagator U(t) = P exp
h
−i
¯h
R t
0 H(τ)dτ
i
acquires higher-order terms involving associators in Magnus-like expansions. Reordering
control slices can change U(t) even for the same time-averaged H, leading to intrinsic
path dependence outside associative sectors.
These features motivate the mitigation palette developed later (associative conﬁne-
ment, G2-invariant coding, associator-aware decoupling, and seven-factor synthesis).
