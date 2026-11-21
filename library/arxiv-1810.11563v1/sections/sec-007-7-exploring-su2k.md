---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-007-7-exploring-su2k
section_title: "Exploring SU(2K)"
section_number: 7
pages: 11-14
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
toc_source: outline
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
Exploring SU(2K)
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
system A in Brown-Susskind https://arxiv.org/pdf/1701.01107.pdf.
The auxiliary system represents the motion of U(t) on SU(N) as time unfolds. The
classical particle starts at the identity operator I and ends at U.
12
Figure 5: The auxiliary system: The evolution of the unitary operator U(t) can be thought
of as the motion of a classical particle moving through the group space SU(2K).
