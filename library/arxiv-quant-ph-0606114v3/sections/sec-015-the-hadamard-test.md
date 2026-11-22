---
doc_id: arxiv-quant-ph-0606114v3
doc_title: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation"
section_id: sec-015-the-hadamard-test
section_title: "The Hadamard Test"
section_number: null
pages: 28-29
source_pdf: 0606114v3.pdf
source_sha256: a8e08c457b65c728
toc_source: inferred
doc_brief: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation — We review the q-deformed spin network approach to Topological Quantum Field Theory and apply these methods"
---
In order to (quantum) compute the trace of a unitary matrix U, one can use
the Hadamard test to obtain the diagonal matrix elements ⟨ψ|U|ψ⟩of U. The
trace is then the sum of these matrix elements as |ψ⟩runs over an orthonormal
basis for the vector space. We ﬁrst obtain
1
2 + 1
2Re⟨ψ|U|ψ⟩
as an expectation by applying the Hadamard gate H
H|0⟩= 1
√
2(|0⟩+ |1⟩)
H|1⟩= 1
√
2(|0⟩−|1⟩)
to the ﬁrst qubit of
CU ◦(H ⊗1)|0⟩|ψ⟩= 1
√
2(|0⟩⊗|ψ⟩+ |1⟩⊗U|ψ⟩.
Here CU denotes controlled U, acting as U when the control bit is |1⟩and the
identity mapping when the control bit is |0⟩. We measure the expectation for
the ﬁrst qubit |0⟩of the resulting state
1
2(H|0⟩⊗|ψ⟩+ H|1⟩⊗U|ψ⟩) = 1
2((|0⟩+ |1⟩) ⊗|ψ⟩+ (|0⟩−|1⟩) ⊗U|ψ⟩)
= 1
2(|0⟩⊗(|ψ⟩+ U|ψ⟩) + |1⟩⊗(|ψ⟩−U|ψ⟩)).
This expectation is
1
2(⟨ψ| + ⟨ψ|U†)(|ψ⟩+ U|ψ⟩) = 1
2 + 1
2Re⟨ψ|U|ψ⟩.
The imaginary part is obtained by applying the same procedure to
1
√
2(|0⟩⊗|ψ⟩−i|1⟩⊗U|ψ⟩
This is the method used in [1], and the reader may wish to contemplate its
eﬃciency in the context of this simple model. Note that the Hadamard test
enables this quantum computation to estimate the trace of any unitary ma-
trix U by repeated trials that estimate individual matrix entries ⟨ψ|U|ψ⟩. We
shall return to quantum algorithms for the Jones polynomial and other knot
polynomials in a subsequent paper.
5
