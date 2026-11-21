---
doc_id: quaternioms
doc_title: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations"
section_id: sec-018-quaternionic-model-structural-universality-and-s
section_title: "Quaternionic Model: Structural, Universality, and Simulation Results"
section_number: null
pages: 16-17
source_pdf: quaternioms.pdf
source_sha256: becedcbc858611dd
toc_source: outline
doc_brief: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations — 45 sections: Front matter; Introduction; Extended Related Work"
---
We begin by securing the structural backbone over H: A well-deﬁned multipartite
composition. This provides the substrate on which universality and simulation statements
are built.
Theorem 1 (Canonical tensor structure over H). Let (Hi, ⟨·, ·⟩i), i = 1, 2, 3, be right H-Hilbert
modules. Then
(H1 ⊗H2) ⊗H3 ∼= H1 ⊗(H2 ⊗H3)
canonically and isometrically, with inner product on simple tensors ⟨u1 ⊗u2, v1 ⊗v2⟩:=
⟨u1, v1⟩1 ⟨u2, v2⟩2. Proof: Appendix A. Signiﬁcance: Guarantees parenthesization-independent
multipartite composition and entanglement over H.
With a canonical tensor product in place, we can lift the standard “single-qubit +
entangler” recipe to the quaternionic setting.
Proposition 1 (Quaternionic universality via SU(2) + entangler). Let G1 be any dense family
of single-quaternionic qubit gates (identiﬁed with SU(2) via the embedding ι in Appendix A), and let
G2 contain one ﬁxed entangling two-quaternionic qubit gate (e.g., CNOT/CZ). Then G = G1 ∪G2
is universal over H. Proof: Appendix A. Signiﬁcance: The standard “single-qubit + entangler”
paradigm lifts intact to H.
Having established universality, we next compare computational power by explicit
simulations between the quaternionic and complex models.
Theorem 2 (Polynomial simulation equivalence H ↔C). Any n-quaternionic qubit circuit of
depth D compiles to a complex circuit on O(n) qubits with depth poly(D) via ι : H֒ →M2(C);
conversely, complex circuits embed into quaternionic circuits with polynomial overhead. Proof
sketch: Appendix A. Signiﬁcance: Computation over H captures the same complexity class as the
standard model.
This equivalence immediately transfers standard complexity-theoretic guarantees and
fault-tolerance to H.
Corollary 1 (Complexity and fault-tolerance transfer). By Theorem 2, BQP-level algorithms
and threshold-theorem constructions transfer between the complex and quaternionic models with
polynomial overhead; noise models and compilation pipelines port through the embedding up to
constant-factor rescalings in gadgetization. Justiﬁcation: Appendix A.
At the control layer, the embedding is compatible with native SU(2) implementations,
aligning theory with practice.
Lemma 1 (Alignment with native SU(2) control). If a platform implements U ∈SU(2)
natively on an encoded pair, then for any unit quaternion q, ι(q) is realized by the same calibrated
SU(2) pulse on that pair. Proof idea: Appendix A. Signiﬁcance: Single-quaternionic qubit gates
inherit the ﬁdelity of native single-qubit SU(2) control (≳99% in reported designs).
Finally, we account for the resources of the embedded synthesis itself to close the
quaternionic story.
Proposition 2 (Overhead accounting for embedded synthesis). Let
GH = {SU(2) on an encoded pair} ∪{CNOT between pairs}.
A k-quaternionic qubit circuit with G elementary gates compiles to O(G) elementary complex gates
with constant-size gadgets per elementary operation; depth scales by at most a polylogarithmic
factor under Solovay–Kitaev-type reﬁnements. Proof idea: Standard complex synthesis on ι(U);
see Appendix A. Signiﬁcance: Embedded implementations are asymptotically efﬁcient.
