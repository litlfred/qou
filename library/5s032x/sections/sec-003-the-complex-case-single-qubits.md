---
doc_id: 5s032x
doc_title: "The Standard Model Symmetry and Qubit Entanglement"
section_id: sec-003-the-complex-case-single-qubits
section_title: "The Complex Case: Single Qubits"
section_number: null
pages: 5-5
source_pdf: 5S032X.pdf
source_sha256: 17761383781f7bdc
toc_source: outline
doc_brief: "The Standard Model Symmetry and Qubit Entanglement — quantum description."
---
THE COMPLEX CASE: SINGLE QUBITS
We start by treating the simplest case, that of single qubits in ordinary, complex quantum mechanics. Any pure
qubit state can be written as
|ψ⟩= c0 |0⟩+ c1 |1⟩,
(5)
where c0, c1 ∈C, |c0|2 + |c1|2 = 1, and {|0⟩, |1⟩} denotes a standard basis of the two-qubit Hilbert space C2.
It will be useful to represent qubit states in terms of the Pauli matrices
σ1 =

0 1
1 0

σ2 =

0 −i
i
0

σ3 =

1
0
0 −1

,
yielding
ρψ = |ψ⟩⟨ψ| =

c0c∗
0 c1c∗
0
c0c∗
1 c1c∗
1

= 1
2

1 + x3
x1 −ix2
x1 + ix2
1 −x3

(6)
= 1
2 (1 + rψ · σ) ,
with x1 = c1c∗
0 + c0c∗
1, x2 = i(c0c∗
1 −c1c∗
0), and x3 = |c0|2 −|c1|2. This yields the parametrization of the Bloch sphere
and introduces the Bloch vector rψ = (x1, x2, x3), whose components are given by the expectation values of the Pauli
matrices for the given quantum state, xi = ⟨σi⟩ψ.
A.
