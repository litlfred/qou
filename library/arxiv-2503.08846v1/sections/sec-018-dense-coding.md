---
doc_id: arxiv-2503.08846v1
doc_title: "A Tutorial on Knots and Quantum Mechanics"
section_id: sec-018-dense-coding
section_title: "Dense Coding"
section_number: null
pages: 40-42
source_pdf: A_Tutorial_on_Knots_and_Quantum_Mechanics.pdf
source_sha256: 18321b615ffc968b
toc_source: outline
doc_brief: "A Tutorial on Knots and Quantum Mechanics — These notes review a description of quantum mechanics in terms of the topology of spaces, basing on the axioms of Topological Quantum Field Theory and path"
---
Dense Coding
Superdense, or, simply, dense coding is a protocol closely related to quantum teleportation.
It uses
entanglement properties in a very similar way, allowing to use a quantum channel to simultaneously
transmit more than a single bit of classical information. In the textbook version Alice and Bob share an
entangled pair of qubits, so that Bob can encode two classical bits of information, sending only one qubit
to Alice. The circuit diagram of the corresponding protocol is shown in figure 4 (right).
Initially, Bob and Alice share an entangled pair of qubits |Φ+⟩, where we label Φ+
A and Φ+
B Alice’s
and Bob’s qubits respectively. Given two classical bits a and b Bob performs the encoding, applying the
string ZaXb on his qubit. He then sends his qubit to Alice. Alice applies a CNOT on the two qubits she
now possesses and also an Hadamard on the Bob’s qubit. If she now measures both qubits she will find
hers in state |a⟩and Bob’s in state |b⟩.
Let us note that the CNOT and H gate effectively replace the measurement basis by that of the Bell
states. Consequently, there is a simpler (and a bit tautological) version of the protocol, consisting of
application of the ZaXb string and measuring in the Bell basis (163). Then the classical values encoded
by Bob can be read off table 1, provided a specific Bell state as the result of the measurement. The
topological version of this can be expressed by the diagram
B
B
.
(167)
This diagram has three vertical sections. The left section is the initial state |Φ+⟩shared between Alice
and Bob. In the central section Bob applies B[a, b] = ZaXb, which, when appended to |Φ+⟩, transforms
the latter into one of the Bell basis states according to table 1. The right section is the measurement
in the same Bell basis. Therefore, the outcome of the measurement will indeed tell which classical pair
(a, b) was encoded by Bob.
If one finds disappointing the triviality of diagram (167) one can also build a more neat example,
similar to the circuit version shown in figure 4. Let us assume that Bob encodes classical bits using four
braids, as shown in table 2, cf. [102].
40
a
b
Braid
a
b
Braid
0
0
1
0
0
1
1
1
Table 2: Braids used for encoding classical bits.
The CNOT and H gates will be simulated by some nonlocal braiding operation. Let us first assume
that a = 1 and b = 0 are encoded. The protocol can be organized according to the following diagram:
.
(168)
This protocol is split into five sections. The first section, from the left, is state |Φ+⟩, shared by Alice
and Bob. The second section is Bob encoding the classical bits. In the third section Alice applies a
permutation on her qubit, which is an analog of the Hadamard gate. In the forth section a nonlocal
permutation gate is applied, again by Alice, who now has both qubits. This is the “CNOT”. The fifth
section shows the measurement. The diagram tells us that the result in this case will be state |ˆ1⟩on the
top qubit and state |ˆ0⟩on the bottom, where the labels correspond to the nonorthonormal basis (74).
Now let us encode the pair a = 0, b = 1. Using the same protocol we draw
.
(169)
By inspecting the part of the diagram before the measurement one should be able to see that it represents
the state shown in the measurement part. In other words, as a result of the protocol the top qubit is
found in the |ˆ0⟩state and the bottom – in |ˆ1⟩. Now it should be straightforward to conclude that the
remaining two cases a = b = 0 and a = b = 1 will produce pairs |ˆ0ˆ0⟩and |ˆ1ˆ1⟩respectively.
Using the basis |ˆaˆb⟩is not suitable for a physical experiment, so one should pass to an orthogonal
basis instead. As already mentioned, the flaw of the diagrammatic basis used in the present approach
is in the absence of orthogonal diagrams. Therefore one will need to consider linear combinations of the
diagrams. To measure states in the computational basis |ab⟩the encoding transformations should be
appropriate linear combinations of diagrams in table (2). The generalized protocol is then
B[a,b]
a
b
.
(170)
It is straightforward to compute the expansion coefficients of B[a, b] in terms of the braids in table 2. For
41
=⇏
=
Figure 5: Topological operators acting on tensor products of two Hilbert spaces are in general nonunitary.
Contracting an operator with its unitary conjugate creates a topological defect, preventing the result to
be an identity matrix.
example,
B[1,0]
=
1
d
√
d2 −1


−1
d

.
(171)
Note also that the protocol has some cosmetic differences with the protocol in figure 4 (right).
In
particular, in (170), the analog of H is applied before the analog of CNOT. Also the assignments of a/b
to Alice’s/Bob’s qubits are swapped. The reader is invited to redesign the protocol to better match the
one in figure 4.
Let us also mention another subtlety highlighted by protocol (170). Note that sections of the diagram
(vertical gray lines) involve a Hilbert space of eight points, rather than a tensor product of two four-point
Hilbert spaces. This means that the initial two-qubit state is embedded into a large Hilbert space (in
general, of dimension 14). This is not a problem as long as the result of the protocol is restricted to
belong to the four-dimensional two-qubit subspace. It is instructive to check what would happen if a
tensor product of two four-point spaces were used.
First, application of a nonlocal, two-qubit, operation would result in a topological defect – a hole in
the middle:
−→
.
(172)
Such a whole would obstruct realization of the necessary final states: One would not be able to freely move
the lines around. Second, the operator, of the type appearing in (172) would not in general be unitary,
for a similar reason. Figure 5 illustrates the fact that concatenating the operator and its Hermitian
conjugate will not in general produce the identity due to a topological defect.
These comments complement a more naive version of this topological protocol considered in [102].
