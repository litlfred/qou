---
doc_id: quaternioms
doc_title: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations"
section_id: sec-028-quaternion-to-complex-embedding-and-proof-detail
section_title: "Quaternion-to-Complex Embedding and Proof Details"
section_number: null
pages: 26-27
source_pdf: quaternioms.pdf
source_sha256: becedcbc858611dd
doc_brief: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations — 40 sections: Introduction; Extended Related Work; Introduction: Bridging"
---
Appendix A.1. Explicit Embedding H֒→M2(C)
A powerful tool for connecting quaternions to standard quantum mechanics is their
representation as 2 × 2 complex matrices. The algebra of quaternions is isomorphic to a
subalgebra of the 2 × 2 complex matrices M2(C). A general quaternion q = a + bi + cj + dk
can be represented as the matrix:
q ↦→
(
a + bi c + di
−c + di a − bi
)
. (A1)
Under this mapping, the quaternion basis units {1, i, j, k} have a direct correspondence
with the identity matrix I and the Pauli matrices ( σ x, σ y, σ z), up to a factor of −i:
1 ↦→
(
1 0
0 1
)
= I (A2)
i ↦→
(
i 0
0 −i
)
= iσ z (A3)
j ↦→
(
0 1
−1 0
)
= −iσ y (A4)
k ↦→
(
0 i
i 0
)
= iσ x (A5)
This isomorphism is profound. It shows that the non-commutative algebra of quaternions
is the same algebra as that of the spin operators for a spin-1/2 particle. This is why
quaternions naturally appear in the description of spin and rotations in quantum mechanics.
q = z1 + z2j (A6)
|ψ ⟩ = ( z11 + z12j)|0⟩ + (z21 + z22j)|1⟩ (A7)
|ψ ⟩ ↦→|ψ C⟩ = z11|00⟩ + z21|01⟩ + z12|10⟩ + z22|11⟩. (A8)
Quantum Rep. 2025, 7, 55 26 of 40
A single-quaternionic qubit gate is a 2 × 2 unitary matrix with quaternionic entries.
Using the same decomposition ( q = z1 + z2j), any 2 × 2 quaternionic matrix U can be
written as U = A + Bj, where A and B are 2 × 2 complex matrices. When this operator
acts on a state vector, the non-commutativity of j with complex numbers must be handled
carefully (speciﬁcally , zj = j ¯z for any z ∈ C).
U = A + Bj ↦→ UC =
(
A B
− ¯B ¯A
)
. (A9)
This provides a constructive method for converting any single-quaternionic qubit gate into
an equivalent two-qubit complex gate. The procedure can be generalized to n-quaternionic
qubit gates, which map to 2 n-qubit complex gates.
