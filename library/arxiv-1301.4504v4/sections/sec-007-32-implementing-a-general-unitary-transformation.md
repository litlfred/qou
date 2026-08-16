---
doc_id: arxiv-1301.4504v4
doc_title: "Prepared for submission to JHEP DEDICATED TO JOHN PRESKILL ON THE OCCASION OF HIS 60 TH BIRTHDAY Quantum Computation vs. Firewalls Daniel Harlowa Patrick Haydenb aPrinceton Center "
section_id: sec-007-32-implementing-a-general-unitary-transformation
section_title: "Implementing a General Unitary Transformation with Quantum Gates"
section_number: 3.2
pages: 19-26
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
doc_brief: "DEDICATED TO JOHN PRESKILL ON THE OCCASION OF HIS 60 TH BIRTHDAY Quantum Computation vs. Firewalls Daniel Harlowa Patrick Haydenb aPrinceton Center for Theoretical Science, Princeton University, Princ"
---
In our world, the result of the previous section, that doing a quantum computation at
worst takes a time which is double exponential in the entropy of the computer, had
better not be optimal if we are ever to do any quantum computation at all. It can
be improved upon of course, and the reason is that locality of interactions makes the
dependence ofUcomp on time and computer size very special indeed.20 Since no quantum
computer has yet been built we do not know exactly how one might be implemented
physically, but there is a widely accepted model for quantum computation called the
quantum circuit model. In the quantum circuit model one imagines having a “quantum
20This subsection is entirely pedagogical and contains no original material, good references are
[41–43].
– 18 –
memory” consisting of n qubits, on which one can easily act with some ﬁnite set of
one- or two-qubit unitary transformations, called quantum gates, on any qubit or pair
of qubits. The computer builds up larger unitary transformations by applying the
various gates successively. Interestingly the number of diﬀerent types of gates needed
to generate arbitrary unitary transformations with high precision is quite small. In fact,
one is suﬃcient provided it is generic enough and that it can be applied to any two of
the qubits (and in either order on those two). A set of gates having this property is
called universal. A speciﬁc set of three gates which is universal is the Hadamard gate,
which acts on a single qubit as
H|0⟩ = 1√
2 (|0⟩ +|1⟩)
H|1⟩ = 1√
2 (|0⟩−| 1⟩), (3.14)
the Z1/4 gate which acts on a single qubit as 21
Z1/4|0⟩ =|0⟩
Z1/4|1⟩ =e
iπ
4|1⟩, (3.15)
and the CNOT gate Ucnot, for “controlled not”, which acts on two qubits as
Ucnot|b1,b 2⟩ =|b1,b 1 +b2⟩ (3.16)
with the addition being mod 2. This gate ﬂips the second bit if and only if the ﬁrst bit
is 1. There is a standard graphical notation for representing circuits, which we have
already used in ﬁgure 2, and we illustrate it some more in ﬁgure 3.
We can now ask how many gates are needed to make a complicated unitary trans-
formation likeUR in equation (3.3). This is a good measure of the amount of time/space
needed to actually do the computation, since we can imagine that the gates can be im-
plemented one after another in a time that scales at most as a small power of n. For
a set of f fundamental gates, the number of circuits we can make which use T total
gates is clearly ((n
2
)
f
)T
≈ (n2f)T. (3.17)
21In this equation we see the unfortunate but standard convention in quantum computation theory
that the Pauli-z operator, usually written as Z, acts as Z|0⟩ =|0⟩ and Z|1⟩ =−|1⟩. The Hadamard
operator can then be interpreted as switching from the Z eigenbasis to the X eigenbasis. As an
example it is worth seeing to see how to build the Pauli operators X, Y , and Z out of H and Z 1/4
gates.
– 19 –
H Z
14
H
Figure 3 . The standard representations of the three gates described in the text, as well as
a simple circuit that maps the product basis |b1,b 2⟩ to a basis each element of which has the
two qubits maximally entangled. In the CNOT gate the addition is done at the hollow circle.
To proceed further we need some basic idea of size and distance for the unitary
group. The unitary group on n qubits is a compact manifold of dimension 2 2n, and we
can parametrize its elements as
U =ei ∑22n
a=1cata
. (3.18)
Here ta are generators of the Lie algebra of U(2n), and we can very roughly think of
the ca’s as parametrizing a unit cube in R22n
. Also roughly we can think of linear
distance in this unit cube as a measure of distance between the unitaries. For example
say we wish to compute the diﬀerence between acting on some pure state |Ψ⟩ with two
diﬀerent unitary matrices U1 and U2 and then projecting onto some other state χ:
⟨χ|(U1−U2)|Ψ⟩ =⟨χ|
(
I−U2U†
1
)
U1|Ψ⟩≈− i⟨χ|
∑
a
δcataU1|Ψ⟩. (3.19)
If the sum of the squares of the δca’s is less than ϵ2, the right hand side will be at most
some low order polynomial in 2 n times ϵ. This polynomial is irrelevant as we now see.
Around each of our (n2f)T circuits we can imagine a ball of radius ϵ in R22n
. The
volume of all the balls together will be of order the full volume of the unitary group
when
(n2f)Tϵ22n
≈ 1. (3.20)
Thus we see that in order to be able to make generic elements ofU(2n) we need at least
T∼ 22n log
(1
ϵ
)
(3.21)
gates, where we have kept only the leading dependence on n and ϵ. As promised,
because ϵ appears inside a logarithm the crude nature of our deﬁnition of distance has
– 20 –
not mattered. More importantly, we see that the number of gates is now only a single
exponential in (twice) the entropy. The fact that this crude counting bound can be
achieved by an appropriate sequence of gates is known as the Solovay-Kitaev theorem.
So the quantum circuit model is able to do arbitrary quantum computations much
faster than our calculation of the previous section suggested; this is essentially because
locality enables us to dynamically isolate parts of of the computer in such a way that we
can push the chaos of the system into heating the environment (not explicitly modeled
here) instead of messing up our computation.
Given that we have so quickly beaten down a double exponential to a single expo-
nential, one might be optimistic that further reduction in computing time is possible.
Unfortunately, in our universe that does not seem to be the case. Simple modiﬁcations
of the quantum circuit model such as changing the set of fundamental gates or con-
sidering higher spin fundamental objects instead of qubits, for example qutrits, make
only small modiﬁcations to the analysis and don’t change the main 2 2n scaling. One
could imagine trying to engineer gates that act on some ﬁnite fraction of the n qubits
all at once, perhaps by connecting them all together with wires or something, but it
is easy to see that any such construction requires a number of wires exponential in n.
One could also try to parallelize by applying gates on non-overlapping qubits simul-
taneously whenever possible, as well as adding additional “ancillary” qubits. As long
as the number of extra qubits scales like some power of n, however, it is clear they
cannot beat the 2 2n. Even with exponentially many ancilla or wires just the travel
time between the various parts of the computer will be exponential in n. In the face of
these diﬃculties the reader might be tempted to try using some sort of exotic nonlocal
system like a black hole to do the computation, but this would just give up what the
circuit model accomplished and most likely return us to even worse situation of the
previous section. In this paper we will adopt the widely held point of view that the
quantum circuit model accurately describes what are physically realistic expectations
for the power of a quantum computer.
Thus ifUR has no special structure, we do not expect Alice to be able to implement
it (or its inverse) in time shorter than 2 2n. As discussed below equation (3.3) however,
UR was deﬁned only by its action on a subspace of dimension 2 k+m. In studying the
complexity of UR we are free to quotient U(2n) by multiplication on the right by a
block diagonal matrix which acts as the identity on the subspace spanned by states
of the form |bh0⟩. The dimensionality of this quotient is 2 k+m+n, and since it is good
enough to ﬁnd a circuit which produces any element of the coset containing UR the
counting argument of this section suggests that Alice will be able to use a decoding
– 21 –
circuit implementable in a time scaling like
T∼ 2k+m+n. (3.22)
3.3 Why is Alice’s Computation Slower than the Black Hole Dynamics?
We now turn to the question of whether or not the black hole dynamics constrain UR
in any way that could help Alice implement it faster. One thing we know about the
black hole is that it produces the state (3.3) relatively quickly, in a time that scales
like n3/2 for a Schwarzschild black hole. This seems to suggest that Alice might be
able implement U†
R quickly by some sort of time-reversal. This turns out not to be the
case. To explain this we introduce a slightly more detailed model of the dynamics that
produce the state (3.3).
To describe the evaporation process it is clearly necessary to have a Hilbert space
in which the we can have black holes of diﬀerent sizes. We can write this as
H =⊕
nf
n=0
(
HBH,nf−n⊗HR,n
)
. (3.23)
Here the subscriptsn andnf−n indicate the number of qubits in the indicated Hilbert
spaces. The dimensionality ofH isnf2nf . We can imagine starting in the subspace with
n = 0 and then in each time-step acting with a unitary transformation that increases
n by one. We will take the evolution on the radiation to be trivial. The black hole
becomes old after nf/2 steps. This “adiabatic” model of evaporation assumes equation
(3.2) is exact and does not involve any energetics but, as discussed below equation
(3.2), it is not a bad approximation for the decay of a Schwarzschild black hole: the
number of Hawking quanta produced is of order the entropy of the black hole, and so
is their coarse-grained entropy.
An actual black hole formed in collapse will have some width in energy, which here
means a width inn, but by ignoring this we can make a further simpliﬁcation. Starting
in one of the 2 nf states with n = 0, the evolution never produces superpositions of
diﬀerent n. So we can actually recast the whole dynamics as unitary evolution on a
smaller Hilbert space of dimension 2 nf , but in which the interpretation of subfactors
changes with time. We illustrate this with a circuit diagram in ﬁgure 4.
With this simpliﬁcation we can now combine all of the timesteps together into one
big unitary matrix Udyn acting on our 2 nf dimensional Hilbert space. The matrix UR
appearing in the state (3.3), which we now interpret as having been produced by Udyn,
will (unlike Udyn) depend rather sensitively on the initial state, and since Alice only
needs to be able to do the computation for some particular initial state we will for
simplicity choose it to just have all the bits set to zero. For n> nf
2 we then expect
Udyn|00000⟩init≈ 1√
|B||H|
∑
b,h
|b⟩B|h⟩HUR|bh0⟩R. (3.24)
– 22 –
Figure 4 . The black hole dynamics for a 7-bit black hole. With each step the subfactor we
interpret as the radiation gets larger.
So this equation tells us something about UR, whose complexity we are interested
in understanding. To proceed further we need to make some sort of assumption about
Udyn. This is a question about the dynamics of quantum gravity so we can’t say
anything too precise, but for those black holes which are well understood in matrix
theory [44] or AdS/CFT [24, 45, 46] the dynamics are always some matrix quantum
mechanics or matrix ﬁeld theory. Theories of this type can usually be simulated by
polynomial-sized quantum circuits [47–50], so it seems quite reasonable to assume that
Udyn can be generated by a polynomial number of gates. 22 Such circuits are usually
called “small”, so more precisely we want to know the following: does the existence of a
small circuit forUdyn imply the existence of a small circuit for UR? If the answer is yes,
then our model would imply that Alice can decode RB out of the Hawking radiation
fairly easily.
It is clear that acting on the state |00000⟩init we can easily decompose Udyn into
URUmix, where Umix is a simple circuit that entangles the ﬁrst four subfactors in
|00000⟩init:
Umix|00000⟩init = 1√
|B||H|
∑
b,h
|b⟩B|h⟩H|bh0⟩R. (3.25)
Umix is very easy to implement, we can just use the circuit on the right in ﬁgure 3
22Technically this also assumes that the mapping from the “microscopic” degrees of freedom on
which the quantum mechanics looks simple to the “macroscopic” basis (3.1) is relatively simple. For
low energy ﬁelds outside the horizon this seems plausible to us, for example in AdS/CFT the well-
known construction of [51] seems to accomplish this in a straightforward way for operators outside the
horizon. We discuss this more in section (6) below.
– 23 –
nf−n times for a total of 2(nf−n) gates. We can then deﬁne a new operator
˜UR =UdynU†
mix, (3.26)
which has the property that
˜UR
1√
|B||H|
∑
b,h
|b⟩B|h⟩H|bh0⟩R = 1√
|B||H|
∑
b,h
|b⟩B|h⟩HUR|bh0⟩R. (3.27)
˜UR can obviously be implemented with a small circuit, and it apparently seems to be
exactly what Alice needs; she can just apply the inverse circuit to the state (3.3) and
the decoding is accomplished. Unfortunately for her this does not work. Although the
operator ˜UR appears to only act on the radiation, the circuit this construction provides
involves gates that act on all of the qubits. While she is doing the decoding Alice does
not have access to the qubits in B and H, so she cannot directly use them. Of course,
if the circuit really acted as the identity operator on B andH for any initial state this
would not matter, she could just throw in some ancillary qubits in an arbitrary state to
replace those in B andH and still use the ˜U†
R to undo UR. The problem is that (3.27)
holds only when ˜UR acts on the particular state 1√
|B||H|
∑
b,h|b⟩B|h⟩H|bh0⟩R. This can
be traced back to the fact that the deﬁnition of UR in the ﬁrst place depended on the
initial state of the black hole on which Udyn acts.
Although Alice cannot use these small circuits to decode the entanglement, she
can move it around. For example acting with a CNOT gate three times on two qubits,
switching which qubit is the “control” qubit each time, exchanges the pair:
|b1,b 2⟩→| b1,b 1 +b2⟩→| b2,b 1 +b2⟩→| b2,b 1⟩, (3.28)
so by adjoining a set of n ancillary qubits to the state|Ψ⟩, Alice can use this operation
to achieve
1√
|B||H|
∑
b,h
|b⟩B|h⟩HUR|bh0⟩R|000⟩anc→ 1√
|B||H|
∑
b,h
|b⟩B|h⟩H|000⟩RUR|bh0⟩anc.
(3.29)
This trivializes the state of the radiation, but of course doesn’t really accomplish much
since testing the entanglement still requires undoing UR. It does show however that
Alice can move the quantum information from the radiation to a more “stable” quantum
memory in a short amount of time.
The lesson of this section is that because Alice does not have access to all of the
qubits in the system, she is unable to simply time-reverse the black hole dynamics and
extract RB in a time that is polynomial in the entropy. Without such a simple con-
struction, she will in general be left with no option but to brute-force her construction
– 24 –
of U†
R using of order 2n+k+m gates.23 It is still possible that some yet-unknown special
features of black hole dynamics will conspire to provide a simple circuit for UR, but it
would be rather surprising. After all there are many ways a unitary could be atypical,
and most still require exponentially many gates. In the following section we will see
that for some analogous questions in the theory of error-correcting codes, within the
context of simple circuits with O(n2) gates it is possible to run into problems which
almost certainly take exponential time to solve. These results will unfortunately not
be directly applicable here, but by recasting Alice’s decoding task as an error correc-
tion problem we will be able to get more intuition about how the exponential arises.
We will also see that being able to eﬃciently perform a decoding very similar to UR
would have very unlikely implications for the complexity class Quantum Statistical
Zero-Knowledge.
