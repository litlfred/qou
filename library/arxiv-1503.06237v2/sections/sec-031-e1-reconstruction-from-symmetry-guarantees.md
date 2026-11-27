---
doc_id: arxiv-1503.06237v2
doc_title: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence"
section_id: sec-031-e1-reconstruction-from-symmetry-guarantees
section_title: "E.1 Reconstruction from symmetry guarantees"
section_number: null
pages: 58-61
source_pdf: 1503.06237v2.pdf
source_sha256: 55572e7133514f4a
toc_source: outline
doc_brief: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence — We propose a family of exactly solvable toy models for the AdS/CFT correspondence based on a novel"
---
The greedy entanglement wedge falls short of the expectations for a geometric entan-
glement wedge in certain ways. For instance, in the scenario where the minimal surface
separatingA fromAc is well deﬁned, we expectE[A]∪E [Ac] to contain the full lattice.
– 56 –
00.10.20.30.40.50.60.70.80.91
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Erasure probability
Central qubit recovery probability
n=1
n=3
n=5
n=7
n=9
(a) Holographic pentagon code
00.20.40.60.81
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Erasure probability
Central qubit recovery probability
n=1
n=3
n=5
n=7
n=9
 (b) Pentagon/hexagon code
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Erasure probability
Central qubit recovery probability
n=1
n=3
n=5
n=7
n=9
 (c) Single qubit hexagon code
Figure 26 . Here we present Monte Carlo simulation for the probability of the central tensor
being incorporated by the greedy algorithm applied to a holographic code. The greedy algo-
rithm is applied to a region A constructed by randomly taking each boundary physical index
to belong to A with probability p. We plot the central tensor containment probability in the
greedy wedge according to the lattice radius (i.e. the distance from the central tensor at which
the a priory inﬁnite network is truncated). (a) We consider the holographic pentagon code
of ﬁgure 4b. Numerical results remains consistent with the existence of ﬁve possible weight 4
representations of the string-like logical operators acting on the central qubit. (b) We focus
on the pentagon/hexagon code of ﬁgure 17a which has an erasure threshold in terms of the
recoverabilty. We observe some oscillatory behavior due to the fact that tensor ‘layers’ added
alternate between pentagons and hexagons. (c) We present numerical data for the greedy
algorithm applied to the 1 qubit hexagon code of ﬁgure 17b which corresponds to a tensor
network identical to the holographic hexagon state except for having a single pentagon at its
center.
Our ﬁrst example of reconstruction beyond the greedy wedge involves a family of holo-
graphic stabilizer codes with a single logical qudit. In this case, perfect reconstruction
on either A or its complement Ac can be guaranteed by exploiting a symmetry.
Particularly, the three qutrit stabilizer code of section A.2 is of CSS [60] type, a
property which we can show is inherited by any derived holographic code by following
the arguments of section 5.7. Furthermore, the qutrit Hadamard operator H is a
symmetry of the qutrit code meaning that applying H to all tensor indices preserves
the tensor. The Hadamard operator is symmetric, unitary but generally not Hermitian
9. and is speciﬁed by its action on the generators X and Z
HXH† =Z† HZH† =X. (E.1)
The local symmetry of the tensors gives rise to a global symmetry on the full
9For general qudits, the Hadamard gate is given by H = 1√
d
∑
i,jωij|i⟩⟨j|, where ω =e2πi/d.
– 57 –
(a) From local to global symme-
try
(b) Empty greedy wedge
Figure 27 . In (a) we represent a bipartite network composed of tensors with a symmetry
H and H∗. We alternate applying H (solid squares) and H∗ (hollow squares) to all legs of
tensors in the bipartite tensor network. In (b) we represent the same tensor network where a
portion A of the boundary was marked with hollow dots and its complement Ac was marked
with full dots. The regions A and Ac have been chosen such that the greedy algorithm does
not progress on either. The greedy algorithm will recover the full network when initiated
from the full boundary showing that the network indeed corresponds to a holographic code.
tensor network10. To see this, we multiply each tensor leg either by H or its inverse
H† = H∗. Since each individual tensor is invariant under such an action, the full
tensor network should be invariant. Furthermore, if we assume that the tensor network
graph is bipartite we may alternate multiplication by H and H† such that these may
locally cancel on all contracted indices, as depicted in ﬁgure 27a. We are then left
with a symmetry acting exclusively on the free bulk and boundary legs of the tensor
network. This symmetry guarantees a form of duality between X-type logical operator
and Z-type logical operators where dual operators have exactly the same support.
Theorem 1 in of Ref. [64] precisely relates the number of independent logical
operators supported on complementary subsets of qudits. Their result applies to general
subsystem codes and includes a sharper claim for CSS codes [65]. In particular, for any
subsetA of qudits, one may deﬁne 𝓁(A) to be the number of independent Pauli logical
operators supported exclusively on A.
Lemma 1. Given a stabilizer code withk logical qubits,𝓁(A)+𝓁(Ac) = 2k. Furthermore
if the code is of CSS type, we have 𝓁Z(A) +𝓁X(Ac) = k = 𝓁Z(Ac) +𝓁X(A), where 𝓁X
and 𝓁Z denote the number of X-type and Z-type generators respectively.
10Here we limit ourselves to provide the simplest example which conveys the general spirit of deriving
global symmetries from local tensor symmetries [61]. The state of the art for this line of reasoning in
tensor networks can be found in [62, 63].
– 58 –
This is called the cleaning lemma for stabilizer codes and applies to prime dimension
qudits11.
Assume that we are dealing with a CSS code with a single logical qudit, k = 1
and a Hadamard type symmetry which guarantees 𝓁X(A) =𝓁Z(A). From this we may
exclude the case 𝓁(A) = 𝓁(Ac) = 1 and conclude that the full logical algebra may
be reconstructed either on A or on Ac. This conclusion is analogous to E[A]∪E [Ac]
covering the full bulk, which is expected from the usual geometric entanglement wedge.
In contrast, the greedy algorithm does not provide such a guarantee for the greedy
entanglement wedge. Figure 27b illustrates a partition of the boundary of a tensor
network into two regions such that the greedy algorithm does not make progress in
either region. The same tensor network may be associated to a CSS type stabilizer
code with self-duality properties where all the previously exposed arguments apply.
The same cleaning lemma may be used to guarantee that when|Ac| = 4 qubits are
deleted, at least 2k− 8 independent logical Pauli operators can be reconstructed on A,
wherek is the number of logical qubits in the code 12. In the context of the example of
ﬁgure 16b, even though the greedy entanglement wedge of A lacks a large number of
tensors, the number of missing generators to reconstructed the full algebra is small.
