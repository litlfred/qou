---
doc_id: arxiv-1301.4504v4
doc_title: "Prepared for submission to JHEP DEDICATED TO JOHN PRESKILL ON THE OCCASION OF HIS 60 TH BIRTHDAY Quantum Computation vs. Firewalls Daniel Harlowa Patrick Haydenb aPrinceton Center "
section_id: sec-006-31-quantum-computing-is-hard
section_title: "Quantum Computing is Hard"
section_number: 3.1
pages: 16-19
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
doc_brief: "DEDICATED TO JOHN PRESKILL ON THE OCCASION OF HIS 60 TH BIRTHDAY Quantum Computation vs. Firewalls Daniel Harlowa Patrick Haydenb aPrinceton Center for Theoretical Science, Princeton University, Princ"
---
We begin with a rather formal discussion of Alice’s computation to illustrate some basic
limitations on what is possible; we will take a more standard approach in the following
subsection. In order to do her computation Alice needs to adjoin the radiation to some
computer, whose initial state lives in a new Hilbert space HC, and then wait for the
natural unitary evolution Ucomp onHR⊗H C to undo UR and put the bits which are
entangled withB into an easily accessible form, let’s say the ﬁrstk qubits of the memory
of the computer. We show this pictorially in ﬁgure 2. For most of this subsection we
will ﬁx the amount of time that the computer runs for, meaning that we will takeUcomp
to be determined by the laws of physics and thus unchangeable. The only way Alice
has any hope of getting the computer to do what she wants is by carefully choosing
its initial state. Without loss of generality she can take this initial state to be pure,
– 15 –
perhaps at the cost of increasing the size of the computer. We will show that no matter
how large she makes her computer, it is very unlikely that she will be able to ﬁnd even
one initial state which does the computation.
More precisely what Alice would like to do is ﬁnd a state |Ψ⟩C which for all b and
h evolves as
Ucomp :UR|bh0⟩R⊗| Ψ⟩C↦→| something⟩⊗| b⟩mem, (3.8)
where|something⟩ is any pure state of the computer and radiation minus the ﬁrst k
bits of the memory. |something⟩ can and will be diﬀerent for diﬀerent h. To estimate
how likely it is that such a |Ψ⟩C exists, we discretize the Hilbert space using the trace
norm. In any Hilbert space H of dimension d we can ﬁnd a ﬁnite set Sϵ⊂H with
the property that any pure state in H is within trace norm distance ϵ of at least one
element of Sϵ. Such a set is called an ϵ-net, and it is not too hard to get an estimate
of how many elements it must have [40]. One ﬁrst observes from (3.7) that half of the
trace norm diﬀerence is weakly bounded by the Hilbert space norm:
|||Ψ2⟩−| Ψ1⟩||2
2 = 2
(
1− cosα
√
1−δ2/4
)
≥
(δ
2
)2
=
(1
2||| Ψ2⟩⟨Ψ2|−| Ψ1⟩⟨Ψ1||| 1
)2
.
(3.9)
Thus an ϵ/2-net for the Hilbert space norm is also an ϵ-net for the trace norm. The
minimal size of an ϵ/2-net for the Hilbert space norm is the number of balls of radius
ϵ/2 centered on points on the unit sphere in R2d that are needed to cover it, which at
large d is proportional to some small power of d times
( 2
ϵ
)2d−1
.18 Intuitively we may
just think of unitary evolution as an inner-product preserving permutation of the
( 2
ϵ
)2d
states.
Applying this now to our discussion of the computer, for ﬁxed b and h the total
number of possible states that could appear on the right hand side of (3.8) is
( 2
ϵ
)2|C||R|
.
The number of possible|something⟩’s is
( 2
ϵ
)2|R||C|2−k
. For a given|Ψ⟩C, the probability
over random choices of Ucomp that (3.8) holds for all 2 k+m values of b and h is then
roughly
( 2
ϵ
)−2|C||R|2m(2k−1)
. The number of available initial states is
( 2
ϵ
)2|C|
, so the
18This is a slight overestimate for the size of the trace norm ϵ-net because the Hilbert space norm
distinguishes between states that diﬀer only by a phase while the trace norm does not. We can ﬁx
this by taking the quotient of the unit S2d by the phase to get to a unit CPd−1, whose volume is just
a negligible power in d times the volume of S2d. This quotient eﬀectively sets α = 0 between any two
states, in which case equation (3.9) tells us that the Hilbert space norm becomes close to one half the
trace norm. The induced metric CPd−1 inherits from R2d will then for small ϵ be the same as one half
the trace norm distance. The upshot is then that the number of balls needed to cover CPd−1 scales
like
( 2
ϵ
)2d−2
.
– 16 –
probability that Alice can ﬁnd one for which (3.8) holds is no more than 19
P =
(2
ϵ
)−2|C|(|R|2m(2k−1)−1)
. (3.10)
For any nontrivial k and|R| = 2n, it is clear that this probability is extraordinarily
small. Making the computer bigger just makes it even more unlikely that the compu-
tation can be done!
What then is Alice to do? One might hope that, although the probability of success
is small for any given computer size, by searching over many values of |C| Alice might
ﬁnd one that works. This is a bad idea; summing (3.10) over |C| produces a ﬁnite sum
whose value remains exponentially small in|R|. Alice can do better however by varying
the running time of the computer. This lets her sample a variety of Ucomp’s without
increasing the size of the Hilbert space. If each Ucomp is diﬀerent, then the longest she
might have to wait to get a Ucomp that works is
t∼e2 log( 2
ϵ)|R||C||H||B|. (3.11)
Although ﬁnite, this is unimaginably long for any reasonable system size. For an
astrophysical black hole in our universe it is something like 10 101040
years.
The timescale (3.11) has a simple physical interpretation; it is the quantum recur-
rence time. This is the timescale over which a quantum system comes close to any
given quantum state, and as we found here is double-exponential in the entropy of the
whole system. In doing the computation this way, Alice is simply waiting around for a
quantum recurrence to do it by pure chance.
Fortunately for civilization, these simple estimates are not the ﬁnal word on quan-
tum computing power. In particular, (3.11) does not really hold unless Ucomp is chosen
randomly at each time step. To the extent that there is some structure in how Ucomp
varies with time, as there is in our world, Alice can take advantage of it to speed up her
computation. Similarly, if the wayUcomp changes with increasing|C| also has structure,
she can use that as well. The lesson of this section however is that without using special
properties of the computer-radiation dynamics, no amount of preparation of the initial
state of her computer will allow Alice to do her computation in any reasonable amount
of time. In the following two sections we will see that by using such physical properties
Alice is able beat the double exponential in computer entropy down to a single expo-
nential in just the radiation entropy, but we will also argue that that is probably all
she gets.
19In this counting we can easily ignore the constraint that orthogonal states must be sent to orthog-
onal states.
– 17 –
As a tangential comment it is interesting to note that the result of this section
is actually special to quantum mechanics; there is a somewhat analogous problem in
classical coding which can easily be solved by making the computer bigger. Say that
we have a classical bit string of length n. There are 2 n such strings, but say we are
interested in some subset of size 2 k. For example this could be the set with a k-bit
message in the ﬁrstk bits and zero for the rest. Acting with some random permutation
on the space of 2 n strings, we can send these 2 k strings to a set of 2 k scrambled
“code words”, which are analogous to some basis for RB in the quantum problem. We
could then imagine adjoining one of our n-bit strings to a c-bit “computer” string, and
then acting with a given permutation of the 2 n+c states of this larger system. This
permutation is the analogue of our Ucomp. The question is then the following: given
this larger permutation, can we ﬁnd a single initial string for the computer such that,
after the permutation is applied, it will send the set of codewords to a set for which
the message is again displayed in the ﬁrst k qubits. It turns out that the answer to
this question is yes; out of the
(2n+c
2k
)
≈ 2(n+c−k+ 1
log 2)2k
(3.12)
possible sets of codewords there are 2(n+c−k)2k
which have the message in the ﬁrstk bits.
Thus for a given initial string for the computer the probability that the permutation
sends a generic set of codewords to a “good” set is
P≈e−2k
, (3.13)
which for ﬁxed k we can easily beat by trying the various 2 c initial states for the
computer. It does require an c∼ 2k-bit computer however.
