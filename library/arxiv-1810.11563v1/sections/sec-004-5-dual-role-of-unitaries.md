---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-004-5-dual-role-of-unitaries
section_title: "Dual Role of Unitaries"
section_number: 5
pages: 9-14
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
Complexity can be deﬁned for states 2, but in many ways it is more natural to start with
the complexity of operations that you can do to a system. That means the complexity
of unitary operators. Unitary matrices have a dual role in quantum information theory.
First of all they are the matrix representation of unitary operators,
U =
∑
Uij|i⟩⟨j| (5.9)
1There are still details associated with how precisely a product of gates must approximate a target
state.
2We continue to work with systems of K qubits. The space of states is 2 K dimensional.
8
Secondly they can be used to represent maximally entangled states of 2 K qubits,
|Ψ⟩ =
∑
Uij|i⟩|¯j⟩ (5.10)
3 In asking about the complexity of unitary operators we are also asking about the com-
plexity of maximally entangled states 4,
The space of (special ) unitary operators is SU (2K). It is much bigger than the space
of states CP (2K− 1). Let’s begin with a crude estimate of its size. A unitary matrix in
SU (N) has (N 2− 1) real parameters. If each parameter can take on m values the number
of unitary operators is
#unitaries =m(N 2−1)
Setting N = 2K,
#unitaries = m(4K−1)
log (#unitaries) ≈ 4K logm (5.11)
This is the same pattern that we saw for states except that 2 K is replaced by 4K.
6 Volume of SU (2K)
Let’s make a more reﬁned calculation of the number of operators in SU (N) by dividing
its volume by the volume of an epsilon ball of the same dimensionality (the dimension of
SU (N) isN 2−1.). The volume of SU (N) is https://arxiv.org/abs/math-ph/0210033
V [SU (N)] = 2π
(N +2)(N−1)
2
1!2!3!....(N− 1)! (6.12)
3The bar in ¯J indicates time reversal or in relativistic quantum ﬁeld theory the CPT operation.
4In the case of maximally entangled systems I mean a restricted form of complexity in which gates
are only permitted to act on each side of the entangled system separately, thus preserving the maximal
entanglement.
9
The volume of an epsilon-ball of dimension N 2− 1 is
π
N 2−1
2
(N 2−1
2
)
!
Using Stirling’s formula, and identifying the number of unitary operatos with the number
of epsilon-balls in SU (N)
#unitaries ≈
(N
ϵ2
)N 2
2
=
(2K
ϵ2
)4K/2
(6.13)
Taking the logarithm,
log (#unitaries)≈ 4K
2 K log 2 + 4K log 1
ϵ (6.14)
which is comparable to 5.11. Again, we see the strong exponential dependence on K and
the weak logarithmic dependence on ϵ. The log 1
ϵ term is multiplied by the dimension of
the space.
7 Exploring SU (2K)
We’ve seen that the space of unitary operators is gigantic. Now I want to discuss how
to move through it. I’ve already hinted that we don’t make big complexity jumps, but
instead move in little steps called gates. A sequence of gates is called a circuit although it
has nothing to do with periodicity. It’s just a name.
Deﬁnition:
A k-local gate is a nontrivial k-qubit unitary operator chosen from some allowed uni-
versal gate set. We assume that if g is in allowed set, so is g†.
Figure 1 is a schematic representation of a 2-qubit gate.
10
Figure 1: Time ﬂows from left to right. A gate acts on an incoming state of two-qubits to
give an outgoing state.
Gates can be assembled into quantum circuits in the manner shown in ﬁgure 2.
Figure 2: k-local all-to-all circuit
A k-local circuit is one made of k-local gates. k-locality is not the same as spatial
locality although spatially local circuits are special cases of k-local circuits. In a spatially
local circuit the qubits are arranged on a spatial lattice of some dimensionality. Gates are
permitted only between near neigbors on the lattice. An example of a k-local and spatially
local circuit is shown in ﬁgure 3.
Figure 3: Spatially local circuit
Such circuits would be valuable for simulating condensed matter systems but they are
not the kind of circuits we will be interested in.
11
Deﬁnition A k-local all-to-all circuit is one which is k-local but permits any group of
k qubits to interact. Figure 2 is 2-local and all-to-all.
In ﬁgure 2 the gates act in series, one gate at a time, but it is more eﬃcient to allow
parallel action of gates. The standard k-local all-to-all circuit architecture is shown in
ﬁgure 4.
Figure 4: Standard circuit architecture. Note that in each step the gates all commute
because they act on non-overlapping qubits.
The rule is that at each step the qubits are grouped into pairs and each pair interacts
by means of a two-qubit gate.
We imagine that such a circuit is equipped with a clock, and with each tick of the clock
K/2 gates act. We’ll call this a “step.” The number of steps in a circuit is called its depth
D. The depth of the circuit in ﬁgure 4 is D = 5. The number of gates in the circuit is KD
2 .
Between steps the qubits may be permuted so that any pair can potentially interact. A
circuit of this type can be called k-local (2-local in ﬁgure 4) and all-to-all. The meaning of
all-to-all is that any pair of qubits can potentially interact. Note that in a given time-step
the diﬀerent gates commute because they act on non-overlapping qubit pairs .
If we measure time τ in units of steps then the number of gates that act per unit time
is K/2.
A given circuit prepares a particular unitary operator U. Preparing U by a series of
steps can be viewed as a discrete motion of a ﬁctitious classical particle, called the auxiliary
systemA in Brown-Susskind https://arxiv.org/pdf/1701.01107.pdf.
The auxiliary system represents the motion of U(t) on SU (N) as time unfolds. The
classical particle starts at the identity operator I and ends at U.
12
Figure 5: The auxiliary system: The evolution of the unitary operator U(t) can be thought
of as the motion of a classical particle moving through the group space SU (2K).
