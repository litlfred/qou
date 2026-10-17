---
doc_id: 5s032x
doc_title: "The Standard Model Symmetry and Qubit Entanglement"
section_id: sec-005-the-quaternionic-case-two-qubits
section_title: "The Quaternionic Case: Two Qubits"
section_number: null
pages: 7-9
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
8
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
SL(2, H) and 5 + 1-Dimensional Spacetime
Analogously to Sec. II A, we can write a point in 5 + 1-dimensional Minkowski-space by means of the quaternion
Hermitian matrix
X = 1
2

x0 + x5
x1 −x2i −x3j −x4k
x1 + x2i + x3j + x4k
x0 −x5

,
(21)
whose determinant again gives the 5 + 1-dimensional Minkowski interval, yielding det(X) = 0 →x2
0 −x2
1 −x2
2 −x2
3 −
x2
4 −x2
5 = 0. On these, the Lorentz transformations again act via conjugation by matrices from SL(2, H).
Due to the non-commutativity of the quaternions, some care has to be taken in defining this group. One possibility
here is to take SL(2, H) to be the group of 2 × 2 matrices Mq with quaternionic entries,
Mq =

a b
c d

, a, b, c, d ∈H,
(22)
such that the Dieudonn´e determinant ∆(Mq) =

ad −aca−1b

 is equal to 1 [58]. Alternatively, one can construct the
group via its Lie algebra sl(2, H) [56].
We can now again, appealing to the Bloch representation, suppose each quaternionic qubit to parametrize a lightlike
direction on the heavenly sphere, and obtain the restricted Lorentz group SO+(5, 1). Hence, entangled two-qubit states
give rise to the symmetries of 5 + 1-dimensional Minkowski space [34].
Now suppose we single out a preferred complex structure on H, yielding a split H ≃C ⊕C. Suppose we single out
i and thus, require that the Lorentz transformations commute with it. This will restrict SL(2, H) to SL(2, C), thus
to the symmetries of 3 + 1-dimensional Minkowski space. The extra spatial dimensions in this picture, x3 and x4, are
due to the additional quaternionic imaginary directions j and k, and hence, are “ignored” by singling out a complex
structure.
9
This is the first important point to note: if we want to represent quaternionic quantum mechanics within 3 + 1-
dimensional spacetime, we have to single out a preferred complex structure. Kaluza-Klein like dimensional reduction
can thus be achieved by means of identifying a preferred copy of the complex plane within a higher division algebra.
The motivation for such a singling out might then be given by the need to represent data obtained from such entangled
states in the spacetime emerging from the area-law portion of the entanglement, with respect to which we might think
of additional entanglement as introducing an ‘internal’ geometry.
