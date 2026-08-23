---
doc_id: arxiv-1301.4504v4
doc_title: "Quantum Computation vs. Firewalls"
section_id: sec-008-34-two-counting-arguments
section_title: "Two Counting Arguments"
section_number: 3.4
pages: 26-27
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
doc_brief: "Quantum Computation vs. Firewalls — In this paper we discuss quantum computational restrictions on the types of thought experiments recently used by Almheiri, Marolf, Polchinski, and Sully to argue"
---
So far we have mostly restricted ourselves to thinking about a particular black hole
microstate, which in the previous section we took to be an element of the basis where
Udyn can be constructed out of a polynomial-size quantum circuit. By considering more
general initial states we can prove that for a generic initial state the decoding necessarily
takes exponential time. Restating the setup of the previous section, we can think of
the black hole as a polynomial-size circuit Udyn which acts on a set of microstates |i⟩
as
Udyn|i⟩ = 1√
|B||H|
∑
bh
|b⟩B|h⟩HUR(i)|bh0⟩R. (3.30)
The point here is that we must be able to recover any initial state from the ﬁnal state, so
the unitariesUR(i) must all be distinct elements of the coset U(2n)/U(2n− 2m+k). But
how many initial states are there? If we ignore the coarse-graining that made equation
(3.2) only approximate, then there is a basis of size 2 n+k+m for the total number of
initial states of the black hole. The full set of initial states includes superpositions
however, and we can count them by constructing an ϵ-net like that discussed around
equation (3.9). The total number of initial states then is roughly
( 1
ϵ
)2n+k+m
. The point
then is that this is comparable to the total number of elements in the coset, which
also scales like
( 1
ϵ
)2n+k+m
. Since each state |i⟩ must have its own distinct UR(i), the
23Of course even if she could just time reverse the black hole, the circuit would still take of order the
evaporation time to run. In fact since the black hole is old it would probably take longer to run than
the evaporation. We are not comfortable with this argument as a way out of ﬁrewalls however. Often
when there is a general algorithm that gives a polynomial circuit to do something, special details of
the problem and tricks like parallelization can be exploited to get polynomial increases in the running
speed.
– 25 –
vast majority of initial microstates must be decoded by generic UR’s which necessarily
take time of order 2n+k+m to implement. Being more careful about the coarse-graining
decreases the number of initial states somewhat, but the number is still much too large
for anything more than a vanishingly small fraction to be decodable in polynomial time.
Proponents of the AMPS experiment could still hope for a basis of initial states
where each basis element is easy to decode. A natural basis to try is the one in which
Udyn is polynomial size, but we will present arguments in the following section that
even in this basis the decoding is hard. One could however try to construct such a
basis by taking a basis of ﬁnal states where the decoding is trivial and then evolving it
back with U†
dyn.24 This construction can be disrupted however by taking into account
the coarse-graining in equation (3.2) more carefully. More explicitly, let’s say that
n +k +m = Sinitial/ log 2 + ∆n for some ∆n > 0. The number of initial states is
then double exponential in n +k +m− ∆n. It is then not hard to see that even when
∆n = 1, this set of initial states produces a set ofUR’s which form a doubly-exponential
small fraction of the coset U(2n)/U(2n− 2m+k). If each UR were chosen at random and
independently, it is doubly exponentially unlikely that even one of these states would
produce a UR which can be implemented with a polynomial-size circuit. The initial
states constructed by time reversal of trivial decoding states would not correspond to
black holes; they would be states in some larger Hilbert space involving entanglement
between the black hole and the radiation ﬁeld.
