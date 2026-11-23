---
doc_id: arxiv-quant-ph-0606114v3
doc_title: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation"
section_id: sec-010-22-universal-gates
section_title: "Universal Gates"
section_number: 2.2
pages: 14-15
source_pdf: 0606114v3.pdf
source_sha256: a8e08c457b65c728
toc_source: inferred
doc_brief: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation — We review the q-deformed spin network approach to Topological Quantum Field Theory and apply these methods"
---
Universal Gates
A two-qubit gate G is a unitary linear mapping G : V ⊗V −→V where V is
a two complex dimensional vector space. We say that the gate G is universal
for quantum computation (or just universal) if G together with local unitary
transformations (unitary transformations from V to V ) generates all unitary
transformations of the complex vector space of dimension 2n to itself. It is well-
known [65] that CNOT is a universal gate. (On the standard basis, CNOT is
the identity when the ﬁrst qubit is 0, and it ﬂips the second qbit, leaving the
ﬁrst alone, when the ﬁrst qubit is 1.)
A gate G, as above, is said to be entangling if there is a vector
|αβ⟩= |α⟩⊗|β⟩∈V ⊗V
such that G|αβ⟩is not decomposable as a tensor product of two qubits. Under
these circumstances, one says that G|αβ⟩is entangled.
In [16], the Brylinskis give a general criterion of G to be universal. They prove
that a two-qubit gate G is universal if and only if it is entangling.
Remark. A two-qubit pure state
|φ⟩= a|00⟩+ b|01⟩+ c|10⟩+ d|11⟩
is entangled exactly when (ad −bc)̸ = 0. It is easy to use this fact to check
when a speciﬁc matrix is, or is not, entangling.
Remark.
There are many gates other than CNOT that can be used as
universal gates in the presence of local unitary transformations. Some of these
are themselves topological (unitary solutions to the Yang-Baxter equation, see
[52, 81]) and themselves generate representations of the Artin Braid Group.
Replacing CNOT by a solution to the Yang-Baxter equation does not place
the local unitary transformations as part of the corresponding representation
of the braid group. Thus such substitutions connote only a partial solution
to creating topological quantum computation. In this paper we are concerned
with braid group representations that include all aspects of the unitary group.
Accordingly, in the next section we shall ﬁrst examine, how the braid group
on three strands can be represented as local unitary transformations.
3
