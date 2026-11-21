---
doc_id: quaternioms
doc_title: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations"
section_id: sec-035-state-space-overhead-the-cost-of-complex-embeddi
section_title: "State-Space Overhead: The Cost of Complex Embedding"
section_number: null
pages: 31-32
source_pdf: quaternioms.pdf
source_sha256: becedcbc858611dd
toc_source: outline
doc_brief: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations — 45 sections: Front matter; Introduction; Extended Related Work"
---
Dimensionality Analysis of a Single Octo-Qubit
Let us begin by analyzing the resource cost for a single octo-qubit. As established in
Chapter 2 [5], an octonion is an element of an 8-dimensional real vector space. A single
octo-qubit state, |ψ⟩= o1|0⟩+ o2|1⟩, is described by two such octonions, meaning its state
vector lives in a 16-dimensional real vector space before normalization.
To represent this information within the standard model, we must ﬁnd a complex
Hilbert space of at least this dimension. A system of m complex qubits has a state space
C2m, which corresponds to a 2 · 2m = 2m+1-dimensional real vector space. To embed the
16 real parameters of an unnormalized octo-qubit, we require the following:
2m+1 ≥16 =⇒2m+1 ≥24 =⇒m + 1 ≥4 =⇒m ≥3.
(A10)
This provides a rigorous lower bound: a minimum of three complex qubits is required to
represent the full state space of a single octo-qubit.
This can be understood more directly. The algebra of octonions O is an 8-dimensional
real space. To embed this algebraic structure into a quantum system, we need a Hilbert
space of at least dimension 8. The smallest standard quantum system that provides this
is a 3-qubit system, whose Hilbert space H = (C2)⊗3 has dimension 23 = 8. Under this
embedding, the eight basis vectors of the octonion algebra {1, e1, . . . , e7} are mapped to the
eight computational basis vectors of the 3-qubit system {|000⟩, |001⟩, . . . , |111⟩}.
Exponential Overhead for N-Qubit Systems
This signiﬁcant overhead for a single logical unit scales up for multi-particle systems.
To simulate a register of n octo-qubits, where each logical octo-qubit requires an embedding
into a 3-qubit physical register, a total of 3n complex qubits would be required.
The consequence of this scaling on the Hilbert space dimension is severe. While
a standard n-qubit quantum computer has a state space of dimension 2n, the complex
quantum computer required to simulate an n-octo-qubit system would need a state space
of dimension:
dim(Hsimulation) = 23n = (23)n = 8n.
(A11)
This represents an exponential increase in the size of the state space that must be physically
controlled and manipulated. This “state-space overhead” completely negates any perceived
advantage of the “information density” of an octo-qubit. While it is true that a single octo-
qubit contains more classical information (8 real numbers) than a single complex qubit
(4 real numbers), the physical resources required to represent and operate on it scale
exponentially worse.
This contrasts sharply with the quaternionic case, where the simulation requires 2n
complex qubits. The dimensionality of the corresponding simulation space is 22n = 4n.
While this is still larger than the standard model, the constant factor in the exponent
(2 vs. 3) is signiﬁcantly smaller.
