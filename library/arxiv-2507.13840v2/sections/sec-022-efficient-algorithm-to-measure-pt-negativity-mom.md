---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-022-efficient-algorithm-to-measure-pt-negativity-mom
section_title: "Efficient algorithm to measure PT negativity moment"
section_number: null
pages: 30-31
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
30
B Efficient algorithm to measure CCNR negativity moment
31
C Upper bounds for the PT negativity and the CCNR negativity
32
D Upper bound on DF
33
E
Relationship between PT negativity, CCNR negativity, and robustness of entanglement
34
F
Relationship between PT negativity, CCNR negativity, and the Schmidt number
34
G Depth-dependent bound on the PT negativity and the CCNR negativity
35
H Certification of circuit depth
35
I
Entanglement of pseudorandom density matrices and pseudoentanglement
36
J
Schmidt rank testing
37
K Operator Schmidt rank testing
38
L
pα-negativity in Haar random states
39
M PT and realignment moments in translation-invariant MPS
40
N Matrix product states algorithm for the PT negativity and the CCNR negativity
41
O Effects of depolarizing noise on entanglement
42
P
Witnessing entanglement in Werner States
43
A
Efficient algorithm to measure PT negativity moment
Here, we detail the algorithm to measure E4(ρ) = 1
2[−ln p4 +3 ln p2]. In particular, we give an efficient
algorithm to estimate p4, following Refs. [22, 46]. The circuit to measure is sketched in Fig. S1.
Fact A.1 (Efficient PT moment). For a given (mixed) n-qubit state ρ, there exists an efficient algo-
rithm to measure p4(ρ) = tr(ρΓ)4, where ρΓ = (I ⊗Γ)ρ is the partial transpose, to additive precision
ϵ with failure probability δ using O(ϵ−2 log(2/δ)) copies of ρ, O(n) circuit depth, O(n) Toffoli gates, 1
auxiliary qubit, and O(ϵ−2 log(2/δ)) classical post-processing time.
Proof. We measure the PT moment p4 with respect to complementary bipartition A, B. Then, one
can write [46]
p4 = tr(ρΓ)4 = tr(S3,4
A S2,3
A S1,2
A ⊗S1,2
B S2,3
B S3,4
B ρ⊗4)
(83)
where
Si,j
A =
Y
k∈A
(I + σx
i,kσx
j,k + σy
i,kσy
j,k + σz
i,kσz
j,k)
(84)
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
30
swaps copies i and k on bipartition A where σα
j,k is the α ∈{x, y, z} Pauli operator acting on copy j
and qubit k. Note that Si,j
A is simply a product of individual SWAP operations on each qubit pair of
the bipartition. Now, p4 can be measured by performing the SWAP test with operator [46]
P TB
4
= S3,4
A S2,3
A S1,2
A ⊗S1,2
B S2,3
B S3,4
B .
(85)
Here, one implements a controlled version of P TB
4
, where the control acts on an auxiliary qubit with
Hadamard gates before and after the control. As P TB
4
can be decomposed as a product of 3n two
qubit SWAPs, the controlled version of P TB
4
can be implemented by 3n controlled SWAPs, which are
applied consecutively on different qubit pairs of the copies. Then, the state of the ancilla is measured,
with p4 = ⟨σz⟩aux being the expectation value of σz of the ancilla.
Now, we can bound the estimation of ⟨σz⟩aux in terms of additive error ϵ, failure probability δ,
number of measurements L and range of measurement outcomes ∆λ via Hoeffding’s inequality
δ ≡Pr(|ˆσz −⟨σz⟩| ≥ϵ) ≤2 exp
 
−2ϵ2L
∆λ2
!
.
(86)
Now, we have ∆λ = 2 as σz has eigenvalues ±1. Then, by inverting, we get
L ≤2ϵ−2 log(2/δ) .
(87)
As each measurement requires 4 copies of ρ, we need in total O(ϵ−2 log(2/δ)) copies.
The post-
processing only involves counting outcomes, and thus we have O(αϵ−2 log(2/δ)) post-processing time.
Finally, we have to implement 3n controlled SWAPs, each acting with control on the ancilla and a
pair of qubits, which can be implemented on O(n) circuit depth. SWAP gates require 3 CNOTs, and
controlled SWAP gates are implemented using 3 Toffoli gates. Thus, in total we require 9n Toffoli
gates and 2 Hadamard gates.
We note that the algorithm requires coherent control over 4 copies at the same time, but it does not
require tomographically complete measurements or reconstruction of the density matrix. Note that
the other component of E4, namely p2 = tr(ρ2), can be efficiently measured via SWAP tests or Bell
measurements with even lower complexity, requiring only coherent control over 2 copies [38, 42].
|0⟩
H
•
H
ρ
P TB
4
ρ
ρ
ρ
Figure S1: SWAP test to measure expectation value of PT moment P TB
4
of (85) for computing 4th moment of PT
negativity E4(ρ) for state ρ. Uses 4 copies of ρ and a single ancilla. Control-P TB
4
can be implemented as a sequence
of control-SWAP operations between two qubits, using O(n) depth using O(n) Toffoli gates in total.
