---
doc_id: arxiv-1603.07827v1
doc_title: "Braiding With Majorana Fermions"
section_id: sec-008-41-universal-gates
section_title: "Universal Gates"
section_number: 4.1
pages: 9-10
source_pdf: arxiv-1603.07827v1.pdf
source_sha256: 8f4959c11d26c8c2
toc_source: inferred
doc_brief: "Braiding with Majorana fermions (Kauffman–Lomonaco, Proc. SPIE 9873 (2016), arXiv:1603.07827) — Clifford Braiding Theorem; SU(2) representations of B₃ from quaternions; Fibonacci model"
---
A two-qubit gate G is a unitary linear mapping G : V ⊗V −→V where V is a two complex dimensional vector
space. We say that the gate G is universal for quantum computation (or just universal) if G together with
local unitary transformations (unitary transformations from V to V ) generates all unitary transformations of
the complex vector space of dimension 2n to itself. It is well-known29 that CNOT is a universal gate. (On the
standard basis, CNOT is the identity when the ﬁrst qubit is |0⟩, and it ﬂips the second qbit, leaving the ﬁrst
alone, when the ﬁrst qubit is |1⟩.)
A gate G, as above, is said to be entangling if there is a vector
|αβ⟩= |α⟩⊗|β⟩∈V ⊗V
such that G|αβ⟩is not decomposable as a tensor product of two qubits. Under these circumstances, one says
that G|αβ⟩is entangled.
In,5 the Brylinskis give a general criterion of G to be universal. They prove that a two-qubit gate G is universal
if and only if it is entangling.
Remark. A two-qubit pure state
|φ⟩= a|00⟩+ b|01⟩+ c|10⟩+ d|11⟩
is entangled exactly when (ad −bc)̸ = 0. It is easy to use this fact to check when a speciﬁc matrix is, or is not,
entangling.
Remark. There are many gates other than CNOT that can be used as universal gates in the presence of
local unitary transformations. Some of these are themselves topological (unitary solutions to the Yang-Baxter
equation, see1, 20) and themselves generate representations of the Artin braid group. Replacing CNOT by a
solution to the Yang-Baxter equation does not place the local unitary transformations as part of the corresponding
representation of the braid group. Thus such substitutions give only a partial solution to creating topological
quantum computation.
