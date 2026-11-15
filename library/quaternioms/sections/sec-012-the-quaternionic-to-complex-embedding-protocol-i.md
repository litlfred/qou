---
doc_id: quaternioms
doc_title: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations"
section_id: sec-012-the-quaternionic-to-complex-embedding-protocol-i
section_title: "The Quaternionic-to-Complex Embedding Protocol in Practice"
section_number: null
pages: 11-14
source_pdf: quaternioms.pdf
source_sha256: becedcbc858611dd
toc_source: outline
doc_brief: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations — 45 sections: Front matter; Introduction; Extended Related Work"
---
A foundational result is the embedding of quaternionic quantum circuits into complex
ones with minimal overhead [6]. This theoretical equivalence, established in Chapter 3 [5],
states that any computation on n quaternionic qubits can be simulated by a standard complex
circuit with n + 1 qubits [6]. This mapping effectively realizes quaternionic logic on conventio-
nal platforms:
Hn
H −→Hn+1
C
.
(4)
To put this embedding protocol into practice, we need concrete procedures to trans-
form quaternionic states into complex qubit states and quaternionic gates into sequences
of standard complex gates. This effectively turns any standard quantum computer into a
“virtual” quaternionic quantum computer.
Mapping Quaternionic States to Complex Qubit States
As discussed in Chapter 3 [5], a single quaternion q = a + bi + cj + dk can be expressed
as q = z1 + z2j, where z1 = a + bi and z2 = c + di are complex numbers. A single
quaternionic qubit (quaternionic qubit) state |ψ⟩H = qA|0⟩+ qB|1⟩can thus be mapped to
a state in a 2-qubit complex Hilbert space H2
C.
Let’s explicitly deﬁne this mapping for a single quaternionic qubit. Given |ψ⟩H =
(a0 + a1i + a2j + a3k)|0⟩+ (b0 + b1i + b2j + b3k)|1⟩. We can rewrite this using complex
components: qA = (a0 + a1i) + (a2 + a3i)j = zA0 + zA1j qB = (b0 + b1i) + (b2 + b3i)j =
zB0 + zB1j.
The mapping to two complex qubits, say Q0 and Q1, can be constructed as follows:
|ψ⟩H
7→
|ψ⟩C = zA0|00⟩+ zB0|01⟩+ zA1|10⟩+ zB1|11⟩
(5)
Here, |00⟩represents the state |0⟩Q0|0⟩Q1, and so on. This mapping essentially treats the
j and k components of the quaternions as encoded within an additional complex qubit.
The normalization condition |qA|2 + |qB|2 = 1 in H translates directly to |zA0|2 + |zB0|2 +
|zA1|2 + |zB1|2 = 1 in C, ensuring probabilistic consistency. For n quaternionic qubits, this
requires 2n complex qubits for the most straightforward embedding, or n + 1 complex
qubits with an ancilla for a more optimized embedding [6].
The translation of quaternionic gates to complex gates is achieved by representing the
quaternionic matrices using complex block matrices. A 2 × 2 quaternionic unitary matrix
U =
 
q11
q12
q21
q22
!
, where qmn = zmn0 + zmn1j, can be transformed into a 4 × 4 complex
unitary matrix acting on two complex qubits [6]:
U 7→UC =
 
A
B
−¯B
¯A
!
(6)
where A =
 
z110
z120
z210
z220
!
and B =
 
z111
z121
z211
z221
!
are 2 × 2 complex matrices.
This UC matrix can then be decomposed into a sequence of standard single- and
two-qubit gates (e.g., Clifford+ T gates) using existing quantum circuit synthesis tech-
niques [70,71]. For example, a single quaternionic rotation, which is represented by a
2 × 2 quaternionic matrix, would be implemented as a 4 × 4 complex unitary acting on
two qubits. This 4 × 4 matrix would then be decomposed into a number of elementary
gates. While this introduces an overhead in the number of physical gates, it is a polyno-
mial overhead, confirming the complexity-theoretic equivalence between quaternionic
and complex quantum computing [7].
Circuit Diagrams and Practical Implications
To complement Equations (5) and (6), which deﬁne the quaternionic-to-complex
embedding at the level of matrices and state spaces, it is helpful to have a circuit-level
picture. Figure 2 provides such a schematic view of how a circuit on n logical quaternionic
qubits is simulated by a circuit on n + 1 complex qubits, closely following the simulation
scheme of Fernandez and Schneeberger [6].
|ψ⟩H ∈Hn
H
Quaternionic circuit
UH
UH|ψ⟩H
|Ψ⟩∈Hn+1
C
Embedded complex circuit
UC
UC|Ψ⟩
state
embedding
state
embedding
UC simulates UH via the quaternionic-to-complex embedding described in this subsection.
Figure 2. Schematic quaternionic-to-complex embedding of a circuit on n quaternionic qubits into a
complex circuit on n + 1 qubits. The dashed arrows indicate the embedding of quaternionic states
into complex states, while the lower circuit is implemented with standard complex quantum gates.
Consider a simple example: a single quaternionic Hadamard gate:
HH =
1
√
2
 
1
1
j
−j
!
.
We ﬁrst rewrite HH in the form A + Bj, separating the “real” and “j” parts:
HH =
 
1/
√
2
1/
√
2
0
0
!
+ j
 
0
0
1/
√
2
−1/
√
2
!
.
Thus
A =
1
√
2
 
1
1
0
0
!
,
B =
1
√
2
 
0
0
1
−1
!
,
so that HH = A + Bj with A, B real matrices. The embedding deﬁned in Equation (A1) lifts
this to a 4 × 4 complex matrix via the block form:
HC =
 
A
B
−¯B
¯A
!
,
and, since A and B are real, ¯A = A and ¯B = B. Writing out the blocks explicitly gives
the following:
HC =
1
√
2





1
1
0
0
0
0
1
−1
0
0
1
1
−1
1
0
0




.
(7)
It is straightforward to check that H†
CHC = I4, so HC is unitary.
This 4 × 4 complex unitary would then be compiled into a sequence of standard
quantum gates (e.g., CNOTs, single-qubit rotations) on a 2-qubit register.
Practical Implications for Quaternionic Simulation:
•
Resource Overhead: Each logical quaternionic qubit requires two physical complex
qubits. An algorithm operating on N quaternionic qubits would thus require 2N
complex qubits (or N + 1 for the optimized ancilla method [6]). This linear overhead
makes simulation feasible for moderate N.
•
Gate Depth and Fidelity: Each quaternionic gate translates to a ﬁxed number of stan-
dard complex gates. While this increases the overall circuit depth, it’s a constant factor
overhead per logical gate, meaning total error accumulation remains manageable
within fault-tolerance thresholds for complex systems.
•
Hardware Compatibility: This protocol makes quaternionic quantum computing
immediately compatible with any existing universal quantum computing platform
(superconducting, trapped-ion, photonic, etc.), as it merely requires standard gate sets.
•
Algorithm Development: Researchers can develop and test quaternionic quantum
algorithms using existing quantum simulators and hardware, leveraging the richer
algebraic structure for potential optimization or physical simulation, even if the
underlying hardware is complex-valued.
This embedding highlights that quaternionic quantum computing is not a fundamen-
tally new computational power, but rather a different, potentially more natural or efﬁcient,
way to program existing quantum hardware for certain tasks involving SU(2) symmetries.
