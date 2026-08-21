---
doc_id: arxiv-1301.4504v4
doc_title: "Quantum Computation vs. Firewalls"
section_id: sec-005-3-the-amps-experiment-as-a-quantum-computation
section_title: "The AMPS Experiment as a Quantum Computation"
section_number: 3
pages: 14-16
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
doc_brief: "Quantum Computation vs. Firewalls — In this paper we discuss quantum computational restrictions on the types of thought experiments recently used by Almheiri, Marolf, Polchinski, and Sully to argue"
---
We now begin our discussion of the decoding problem confronting Alice. We will
phrase the discussion in terms of Charlie’s Hilbert space, since for the moment we are
following AMPS and granting that Charlie and Alice must agree on the density matrix
ofHB⊗H R. For simplicity we will throughout model all Hilbert spaces using ﬁnite
numbers of qubits. In the Schmidt basis the state of the old black hole she is interested
in is given by equation (2.4), but this basis is very inconvenient for discussing Alice’s
actions. From here on we will use exclusively a basis for the radiation ﬁeld which is
simple for Alice to work with, and whose elements we will write as
|bhr⟩R≡|b1...b k,h 1...h mr1...r n−k−m⟩R. (3.1)
Here there aren≡ log2|R| total qubits, each of which we assume Alice can manipulate
easily. b1...b k are the ﬁrst k of these qubits, where k is the number of bits in HB,
and m is the number of bits in HH. We can think of k +m as the number of qubits
remaining in the black hole; we will eventually argue that the decoding time is likely of
order 2k+m+n. The ri qubits make up the remainder of the modes which have non-trivial
occupation from the Hawking radiation. Roughly we might expect that
n≈Sinitial/ log 2−k−m, (3.2)
where Sinitial is the horizon area in Planck units of the original black hole prior to
any evaporation. This is something of an underestimate because the computational
basis is local while the information is nonlocal, but this “coarse-graining” enhancement
isn’t large. The radiation mostly comes out in s-wave quanta so it is eﬀectively one-
dimensional. It extends out to a distance L∼M 3 and consists mostly of quanta whose
energy is of order 1/M, so its thermal entropy is n≈LT∼M 2, which is still of order
the initial black hole entropy as we would conclude from (3.2). 17 Perhaps surprisingly
the black hole makes quite eﬃcient use of the information storage capacity available to
it.
We will adopt standard terminology and refer to the basis (3.1) as the computa-
tional basis. In the computational basis we can write the state (2.4) as
|Ψ⟩ = 1√
|B||H|
∑
b,h
|b⟩B|h⟩HUR|bh0⟩R, (3.3)
17We thank Don Page for several useful discussions of this point.
– 13 –
where UR is some complicated unitary transformation on HR. What unitary transfor-
mation it is will depend on the details of quantum gravity, as well as the initial state
of the black hole. For simplicity we have deﬁned it to act on the state where all of
the ri qubits are zero. Clearly the challenge Alice faces is to apply U†
R to the Hawking
radiation, after which it will be easy for her to conﬁrm the entanglement between HB
andHRB. Engineering a particular unitary transformation to act on some set of qubits
is precisely the challenge of quantum computation, and we will henceforth often refer
to Alice’s task as a computation.
So far we have been interpreting HB as the thermal atmosphere of the black hole,
but to actually test the AMPS entanglement it would be silly for Alice to try to decode
all of the atmosphere. Indeed the separation betweenHB andHH is rather ambiguous,
and we are free to push some of the atmosphere modes we are not interested in into
HH. So from here on we will mostly take k to be O(n0). This ostensibly simpliﬁes her
computation, because in any event she only needs to implement UR up to an arbitrary
element ofU(2n−k) acting on the last n−k qubits of the radiation. This simpliﬁcation
turns out to be irrelevant since the dimensionality of the coset U(2n)/U(2n−k) still
scales like 2 2n for k >0, but more importantly it is clear from (3.3) that UR has only
really been deﬁned acting on the 2 k+m-dimensional subspace ofHR spanned by states
of the form|bh0⟩. Its action on the orthogonal subspace can be chosen freely to simplify
the computation provided that it preserves orthogonality, and we will see below that
this reduces the time of Alice’s computation from a naive 2 2n to only 2k+m+n. Since
the black hole is old we have n>k +m, so this is at least 2 2(k+m).
Since the unitary group is continuous it is clear that Alice will not be able to do the
computation exactly. We thus need a good deﬁnition of how “close” she needs to get
to reliably test the entanglement. One standard way to quantify closeness of operators
is the trace norm [39], which for an operator A is deﬁned as
||A||1≡ Tr
(√
A†A
)
. (3.4)
WhenA is hermitian this is just the sum of the absolute values of its eigenvalues. The
motivation for this deﬁnition is as follows: say ρ1 andρ2 are two density matrices, and
Πa is a projection operator for some measurement to give result a. Then
|P1(a)−P2(a)| =|Tr{(ρ1−ρ2)Πa}|≤|| (ρ1−ρ2)||1, (3.5)
so if the trace norm of the diﬀerence of two density operators is less than ϵ then the
probabilities they predict for any experimental result will diﬀer by at mostϵ. The trace
norm of their diﬀerence is clearly preserved by unitary evolution.
– 14 –
B R C
U
C
comp
R
Figure 2 . What the computer does. The connecting lines at the top and bottom indicate
entanglement, and time goes up. The subsystem H goes along for the ride, and after the
computation its puriﬁcation is split between R and C in some complicated way.
If both states are pure then the trace norm of their diﬀerence has a simple inter-
pretation. For any two pure states |Ψ1⟩ and Ψ2 we can write that
|Ψ2⟩ =eiα
(√
1−δ2/4|Ψ1⟩ + δ
2|χ⟩
)
, (3.6)
where|χ⟩ is orthogonal to|Ψ1⟩,α is real, andδ is real and positive. A simple calculation
then shows that
||| Ψ2⟩⟨Ψ2|−| Ψ1⟩⟨Ψ1||| 1 =δ. (3.7)
