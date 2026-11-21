---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-005-5-dual-role-of-unitaries
section_title: "Dual Role of Unitaries"
section_number: 5
pages: 9-10
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
toc_source: outline
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
Dual Role of Unitaries
Complexity can be deﬁned for states2, but in many ways it is more natural to start with
the complexity of operations that you can do to a system. That means the complexity
of unitary operators. Unitary matrices have a dual role in quantum information theory.
First of all they are the matrix representation of unitary operators,
U =
X
Uij|i⟩⟨j|
(5.9)
1There are still details associated with how precisely a product of gates must approximate a target
state.
2We continue to work with systems of K qubits. The space of states is 2K dimensional.
8
Secondly they can be used to represent maximally entangled states of 2K qubits,
|Ψ⟩=
X
Uij|i⟩|¯j⟩
(5.10)
3 In asking about the complexity of unitary operators we are also asking about the com-
plexity of maximally entangled states4,
The space of (special ) unitary operators is SU(2K). It is much bigger than the space
of states CP(2K −1). Let’s begin with a crude estimate of its size. A unitary matrix in
SU(N) has (N 2 −1) real parameters. If each parameter can take on m values the number
of unitary operators is
#unitaries = m(N2−1)
Setting N = 2K,
#unitaries
=
m(4K−1)
log (#unitaries)
≈
4K log m
(5.11)
This is the same pattern that we saw for states except that 2K is replaced by 4K.
