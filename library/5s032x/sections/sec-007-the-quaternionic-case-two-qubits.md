---
doc_id: 5s032x
doc_title: "The Standard Model Symmetry and Qubit Entanglement"
section_id: sec-007-the-quaternionic-case-two-qubits
section_title: "The Quaternionic Case: Two Qubits"
section_number: null
pages: 7-8
source_pdf: 5S032X.pdf
source_sha256: 17761383781f7bdc
toc_source: outline
doc_brief: "The Standard Model Symmetry and Qubit Entanglement — quantum description."
---
THE QUATERNIONIC CASE: TWO QUBITS
The above construction admits a ready generalization to the quaternionic case. The skew-field of quaternions H can
be obtained from the complex numbers by starting with two complex numbers c0 = r0 + r1i and c1 = r2 + r3i (where
we use bolding to mark quaternion imaginary directions), and introducing j such that j2 = −1, which anticommutes
with i. Then, a quaternion q0 is given by
q0 = c0 + c1j
= r0 + r1i + r2j + r3k,
where we have introduced ij = −ji = k as the third quaternion imaginary unit. This directly entails Hamilton’s
relations
i2 = j2 = k2 = ijk = −1,
which fully define quaternionic multiplication.
Quaternionic conjugation is the operation taking q0 to q∗
0 with
q∗
0 = r0 −r1i −r2j −r3k,
which can be used to define the norm |q0|2 = q0q∗
0. This allows us to define a multiplicative inverse q−1
0
=
q∗
0
|q0|2 ,
making H into a normed division algebra.
An arbitrary two-qubit state can be written in the form
|ψ⟩= c0 |00⟩+ c1 |01⟩+ c2 |10⟩+ c3 |11⟩,
(19)
with |c0|2 + |c1|2 + |c2|2 + |c3|2 = 1. This state is separable if c0c3 = c1c2.
Due to the normalization, each two-qubit state can be represented by a point on the 7-sphere S7. We introduce a
pair of quaternions
q0 = c0 + c1j
q1 = c2 + c3j,
and define the quaternionic Pauli matrices
σq
1 =

0 1
1 0

,
σq
2 =

0
i
−i 0

,
σq
3 =

0
j
−j 0

, σq
4 =

0
k
−k 0

,
σq
5 =

1
0
0 −1

.
(20)
With these, we can define a quaternionic ‘Bloch vector’ with coordinates
xi = ⟨σq
i ⟩ψ = (q∗
0, q∗
1) σq
i

q0
q1

.
A.
