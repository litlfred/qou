---
doc_id: 5s032x
doc_title: "The Standard Model Symmetry and Qubit Entanglement"
section_id: sec-008-three-qubits-and-the-octonionic-hopf-fibration
section_title: "Three Qubits and the Octonionic Hopf Fibration"
section_number: null
pages: 12-13
source_pdf: 5S032X.pdf
source_sha256: 17761383781f7bdc
toc_source: outline
doc_brief: "The Standard Model Symmetry and Qubit Entanglement — quantum description."
---
Three Qubits and the Octonionic Hopf Fibration
Due to the normalization |o0|2 +|o1|2 = 1, an octonionic qubit defines a point on the sphere S15. There again exists
a map taking points of the sphere to the extended octonionic plane,
ho
1 :
S15
−→O ∪{∞}
(o0, o1) −→
o0o−1
1
,
(36)
which can then be projected to S8 by means of
ho
2 : O ∪{∞} −→
S8
o0o−1
1
−→(xi)i=1...9
,
(37)
once more with P9
i=1 x2
i = 1. As before, this is just the map taking (o0, o1) to the ‘Bloch-vector’ coordinates,
h2 ◦h1 (o0, o1) = (xi)i=1...9 .
(38)
This realizes S15 as an S7-fibration over an S8 base,
S15
S7
−→S8,
(39)
and as in the previous case, the map reduces to a projection into the complex subspace of O in case the state is
separable into a single-qubit and two-qubit state. Hence, the base space S8 contains the (projective) state of one
qubit, along with entanglement degrees of freedom, while the fiber contains the state of the leftover two qubits.
C.
Spin(9) and SU(3) × SU(2) × U(1)/Z6
As with the previous two sections, there exists a generalization of the connection between the spin-groups and Hopf
fibrations to the octonionic case. One can arrive at an analogous description of the group Spin(9) in terms of matrices
of the form given in Eq. (15), with Lc replaced by Lo, denoting left-multiplication by octonions. However, we can
also again simply note that the octonionic Hopf fibration can be equivalently given as [62]
S15
S7
−→S8 ≡Spin(9)
Spin(7)
Spin(8)
Spin(7)
−→
Spin(9)
Spin(8).
(40)
Then, one must find the subgroup of Spin(9) respecting a split O ≃C ⊕C3, that is, singling out an octonion
imaginary direction. It was shown by Dubois-Violette and Todorov [27] (see also [26, 63, 64]), and put into a more
explicit form by Krasnov [28], that this is just the gauge group of the Standard Model, SU(3) × SU(2) × U(1)/Z6.
We will not give the full argument here, and refer to the cited literature instead. However, as in the quaternionic
case, there is an intuitive way of viewing the group’s action on the base space of the Hopf fibration. Under the
split O ≃C ⊕C3, the coordinates xi split into two sets, {x1, x2, x9} from the singled-out complex subspace, and
{x3, x4, x5, x6, x7, x8} from the additional octonionic complex directions (the entanglement degrees of freedom). Here,
13
the first set characterizes one qubit, while the second gives the entanglement with the other two. Thus, we must look
at the transformations that do not mix these sets.
As before, the triplet {x1, x2, x9} is acted on by rotations from SO(3) ≃SU(2). We now use the embedding of
U(1) × SU(3) into SU(4), given by
(α, g) −→

α−3
0
0
αg,

(41)
where α ∈U(1) and g ∈SU(3) [28]. With SU(4) ≃Spin(6), this then acts on the six remaining directions, as
required.
Finally, from the above embedding, one sees that the O2-spinor splits into two representations, with the single
factor of C being associated to an SU(3)-singlet of U(1)-charge −1, and the C3 associated to a SU(3) triplet of
U(1)-charge 1
3, both transforming as a doublet under SU(2) [28]. Consequently, the octonionic qubit can be seen
to contain precisely one generation of left-handed particles with the quantum numbers of the Standard Model, after
being split into a leptonic part from the factor C and a quark part from C3.
