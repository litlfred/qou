---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-023-efficient-algorithm-to-measure-ccnr-negativity-m
section_title: "Efficient algorithm to measure CCNR negativity moment"
section_number: null
pages: 31-32
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
Efficient algorithm to measure CCNR negativity moment
We now study the measurement complexity of the CCNR negativity moment
C4(ρ) = 1
2[−ln(r4) −3S2(ρ)] ,
(88)
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
31
with
r4 = tr(S1,2
A S3,4
A ⊗S1,3
B S2,4
B ρ⊗4) .
(89)
Notably, the different SWAPs Si,j
A act on different qubits. Thus, in contrast to the PT moments,
one can measure r4 using destructive Bell measurements instead of SWAP test [42]. We show the
measurement setup using Bell measurements in Fig. S2.
Figure S2: Bell measurements to measure expectation value of CCNR negativity moment r4 for state ρ. Uses 4
copies of ρ and O(1) depth.
Proposition 3 (Efficient CCNR negativity moment). For a given (mixed) n-qubit state ρ, there
exists an efficient algorithm to measure r4(ρ) to additive precision ϵ with failure probability δ
using O(ϵ−2 log(2/δ)) copies of ρ, O(1) circuit depth, O(1) CNOT and Hadamard gates, and
O(Nϵ−2 log(2/δ)) classical post-processing time.
Proof. This follows directly from the fact that r4 = tr(S1,2
A S3,4
A ⊗S1,3
B S2,4
B ρ⊗4) can be implemented by
a tensor product of SWAPs S1,2
A , each acting on a different set of qubits. It is known that the Bell
measurements correspond to measurements in the eigenbasis of the SWAP operator. Thus, from Bell
measurements as shown in Fig. S2 and classical post-processing one can compute r4. In particular,
for every qubit pair where one applies the CNOT and Hadamard gate, assign −1 to outcome |11⟩,
and +1 else. Then, multiply all mapped ±1 together, which is the estimator of the expectation value.
As each outcome has range ±1 and thus ∆λ = 2, the dependence on ϵ and δ follows from Hoeffding’s
inequality similar to Eq. (86).
