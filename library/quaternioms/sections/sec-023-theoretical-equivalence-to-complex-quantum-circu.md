---
doc_id: quaternioms
doc_title: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations"
section_id: sec-023-theoretical-equivalence-to-complex-quantum-circu
section_title: "Theoretical Equivalence to Complex Quantum Circuits"
section_number: null
pages: 20-21
source_pdf: quaternioms.pdf
source_sha256: becedcbc858611dd
toc_source: outline
doc_brief: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations — 45 sections: Front matter; Introduction; Extended Related Work"
---
The equivalence between the quaternionic and complex models is formally established
by showing that any computation in one framework can be efﬁciently simulated by the
other. Seminal works in the ﬁeld have demonstrated that any quantum circuit operating
on a register of n quaternionic qubits can be simulated by a standard complex quantum
computer with at most a polynomial increase in resources [6,7]. The core of this argument
lies in constructing an explicit mapping (an isomorphism) between the quaternionic state
space and a larger complex Hilbert space.
Mapping Quaternionic States to Complex States
The key to the simulation is to represent the four real degrees of freedom of a single
quaternion using the four real degrees of freedom available in a pair of complex numbers.
As shown in the Cayley–Dickson construction, any quaternion q ∈H can be uniquely
written as follows:
q = z1 + z2j
(9)
where z1 = a + bi and z2 = c + di are complex numbers. This allows us to map a single
quaternionic qubit state to a state of two complex qubits. A quaternionic qubit state
|ψ⟩= q1|0⟩+ q2|1⟩can be expanded as follows:
|ψ⟩= (z11 + z12j)|0⟩+ (z21 + z22j)|1⟩
(10)
This state can be mapped to a vector in the four-dimensional complex Hilbert space C4,
which is the state space of two complex qubits, via the following isomorphism:
|ψ⟩7→|ψC⟩= z11|00⟩+ z21|01⟩+ z12|10⟩+ z22|11⟩.
(11)
This provides a dictionary for translating any quaternionic qubit state into an equivalent
two-qubit complex state. The mapping for an n-quaternionic qubit system follows directly,
requiring 2n complex qubits for a full simulation.
Mapping Quaternionic Gates to Complex Gates
This equivalence must also hold for the operators. A single-quaternionic qubit gate is a
2 × 2 unitary matrix with quaternionic entries. Using the same decomposition (q = z1 + z2j),
any 2 × 2 quaternionic matrix U can be written as U = A + Bj, where A and B are 2 × 2
complex matrices. When this operator acts on a state vector, the non-commutativity of j
with complex numbers must be handled carefully (speciﬁcally, zj = j¯z for any z ∈C).
The action of U on |ψ⟩can be shown to be equivalent to the action of a 4 × 4 complex
unitary matrix UC on the corresponding complex state |ψC⟩. This complex matrix has a
speciﬁc block structure:
U = A + Bj
7→
UC =
 
A
B
−¯B
¯A
!
.
(12)
This provides a constructive method for converting any single-quaternionic qubit gate into
an equivalent two-qubit complex gate. The procedure can be generalized to n-quaternionic
qubit gates, which map to 2n-qubit complex gates. Because this mapping from states
and gates can be performed efﬁciently, it proves that the two models are polynomially
equivalent. An alternative simulation proposed by [6] uses a single ancilla qubit to manage
the non-commutative phases, achieving a simulation of an n-quaternionic qubit system on
just n + 1 complex qubits, further cementing the efﬁciency of the equivalence.
Therefore, quaternionic quantum computing does not offer a hyper-computational
advantage that would expand the class of solvable problems. Instead, it should be viewed
as an alternative, and in some cases, a more physically intuitive language for describing the
SU(2) operations that govern quantum bits. The true potential of the formalism, as we will
explore next, may lie not in its computational power, but in its representational efﬁciency.
