---
doc_id: arxiv-0904.1556v2
doc_title: "The Algebra of Grand Uniﬁed Theories"
section_id: sec-003-21-isospin-and-su2
section_title: "Isospin and SU(2)"
section_number: 2.1
pages: 6-13
source_pdf: 0904.1556v2.pdf
source_sha256: a1a43786d817f085
doc_brief: "The Algebra of Grand Unified Theories — The Standard Model is the best tested and most widely accepte d theory of elementary particles we have today."
---
Because like charges repel, it is remarkable that the atomic nucleus s tays together.
After all, the protons are all positively charged and are repelled fro m each other
electrically. To hold these particles so closely together, physicists h ypothesized a
new force, the strong force , strong enough to overcome the electric repulsion of
the protons. It must be strongest only at short distances (abou t 10 −15 m), and then
it must fall oﬀ rapidly, for protons are repelled electrically unless the ir separation is
that small. Neutrons must also experience it, because they are bou nd to the nucleus
as well.
Physicists spent several decades trying to understand the stro ng force; it was
one of the principal problems in physics in the mid-twentieth century . About 1932,
Werner Heisenberg, pioneer in quantum mechanics, discovered one of the ﬁrst clues
to its nature. He proposed, in [15], that the proton and neutron mig ht really be two
states of the same particle, now called the nucleon. In modern terms, he attempted
to unify the proton and neutron.
To understand how, we need to know a little quantum mechanics. In q uantum
mechanics, the state of any physical system is given by a unit vecto r in a complex
Hilbert space, and it is possible to take complex linear combinations of t he system
6
in diﬀerent states. For example, the state for a quantum system, like a particle on
a line, is a complex-valued function
ψ ∈L2(R),
or if the particle is conﬁned to a 1-dimensional box, so that its positio n lies in the
unit interval [0, 1], then its state lives in the Hilbert space L2([0, 1]).
We have special rules for combining quantum systems. If, say, we h ave two
particles in a box, particle 1 and particle 2, then the state is a functio n of both
particle 1’s position and particle 2’s:
ψ ∈L2([0, 1] × [0, 1]),
but this is isomorphic to the tensor product of particle 1’s Hilbert spa ce with particle
2’s:
L2([0, 1] × [0, 1]) ∼
=L2([0, 1] ⊗L2([0, 1]).
This is how we combine systems in general. If a system consists of one part with
Hilbert space V and another part with Hilbert space W , their tensor product V ⊗W
is the Hilbert space of the combined system. Heuristically,
and = ⊗.
We just discussed the Hilbert space for two particles in a single box. W e now
consider the Hilbert space for a single particle in two boxes, by which w e mean a
particle that is in one box, say [0 , 1], or in another box, say [2, 3]. The Hilbert space
here is
L2([0, 1] ∪ [2, 3]) ∼
=L2([0, 1]) ⊕L2([2, 3]).
In general, if a system’s state can lie in a Hilbert space V or in a Hilbert space W ,
the total Hilbert space is then
V ⊕W.
Heuristically,
or = ⊕.
Back to nucleons. According to Heisenberg’s theory, a nucleon is a p roton or
a neutron. If we use the simplest nontrivial Hilbert space for both t he proton and
neutron, namely C, then the Hilbert space for the nucleon should be
C2 ∼
= C ⊕ C.
The proton and neutron then correspond to basis vectors of this Hilbert space:
p =
( 1
0
)
∈ C2
and
n =
(
0
1
)
∈ C2.
But, we can also have a nucleon in a linear combination of these states . More
precisely, the state of the nucleon can be represented by any unit vector in C2.
The inner product in C2 then allows us to compute probabilities, using the
following rule coming from quantum mechanics: the probability that a s ystem in
state ψ ∈H, a given Hilbert space, will be observed in state φ ∈H is
|⟨ψ,φ ⟩|2.
7
Since p andn are orthogonal, there is no chance of seeing a proton as a neutron or
vice versa, but for a nucleon in the state
αp +βn ∈ C2,
there is probability |α|2 that measurement will result in ﬁnding a proton, and |β|2
that measurement will result in ﬁnding a neutron. The condition that our state be
a unit vector ensures that these probabilities add to 1.
In order for this to be interesting, however, there must be proce sses that can
turn protons and neutrons into diﬀerent states of the nucleon. O therwise, there
would be no point in having the full C2 space of states. Conversely, if there are
processes which can change protons into neutrons and back, it tu rns out we need
all of C2 to describe them.
Heisenberg believed in such processes, because of an analogy betw een nuclear
physics and atomic physics. The analogy turned out to be poor, bas ed on the faulty
notion that the neutron was composed of a proton and an electron , but the idea of
the nucleon with states in C2 proved to be a breakthrough.
The reason is that in 1936 a paper by Cassen and Condon [7] appeare d suggesting
that the nucleon’s Hilbert space C2 is acted on by the symmetry group SU(2). They
emphasized the analogy between this and the spin of the electron, w hich is also
described by vectors in C2, acted on by the double cover of the 3d rotation group,
which is also SU(2). In keeping with this analogy, the property that d istinguishes
the proton and neutron states of a nucleon was dubbed isospin. The proton was
declared the isospin up state or I3 = 1
2 state, and the neutron was declared the
isospin down or I3 = − 1
2 state. Cassen and Condon’s paper put isospin on its
way to becoming a useful tool in nuclear physics.
Isospin proved useful because it formalized the following idea, which emerged
from empirical data around the time of Cassen and Condon’s paper. Namely: the
strong force, unlike the electromagnetic force, is the same wheth er the particles
involved are protons or neutrons. Protons and neutrons are inte rchangeable, as
long as we neglect the small diﬀerence in their mass, and most importa ntly, as long
as we neglect electromagnetic eﬀects. One can phrase this idea in te rms of group
representation theory as follows: the strong force is invariant under the action of
SU(2).
Though this idea was later seen to be an oversimpliﬁcation, it foresha dowed
modern ideas about uniﬁcation. The proton, living in the representa tion C of
the trivial group, and the neutron, living in a diﬀerent representat ion C of the
trivial group, were uniﬁed into the nucleon, with representation C2 of SU(2). These
symmetries hold for the strong force, but not for electromagnet ism: we say this
force ‘breaks’ SU(2) symmetry.
But what does it mean, exactly, to say that a force is invariant unde r the action
of some group? It means that when we are studying particles intera cting via this
force, the Hilbert space of each particle should be equipped with a un itary represen-
tation of this group. Moreover, any physical process caused by t his force should be
described by an ‘intertwining operator’: that is, a linear operator th at respects the
action of this group. A bit more precisely, suppose V andW are ﬁnite-dimensional
Hilbert spaces on which some group G acts as unitary operators. Then a linear
operator F :V →W is an intertwining operator if
F (gψ) = gF (ψ)
for every ψ ∈V and g ∈G.
8
Quite generally, symmetries give rise to conserved quantities. In qu antum me-
chanics this works as follows. Suppose that G is a Lie group with a unitary rep-
resentation on the ﬁnite-dimensional Hilbert spaces V and W . Then V and W
automatically become representations of g, the Lie algebra of G, and any intertwin-
ing operator F :V →W respects the action of g. In other words,
F (Tψ ) = TF (ψ)
for every ψ ∈V and T ∈ g. Next suppose that ψ ∈V is an eigenvector of T :
Tψ =iλψ
for some real number λ. Then it is easy to check F (ψ) is again an eigenvector of T
with the same eigenvalue:
TF (ψ) = iλF (ψ).
So, the number λ is ‘conserved’ by the operator F .
The elementT ∈ g will act as a skew-adjoint operator on any unitary representa-
tion of G. Physicists prefer to work with self-adjoint operators since thes e have real
eigenvalues. In quantum mechanics, self-adjoint operators are c alled ‘observables’.
We can get an observable by dividing T byi.
In Casson and Condon’s isospin theory of the strong interaction, t he symmetry
group G is SU(2). Here isospin, or more precisely I3, arises as above: it is just the
eigenvalue of a certain element of su(2), divided by i to get a real number. Because
any physical process caused by the strong force is described by a n intertwining
operator, isospin is conserved . So, the total I3 of any system remains unchanged
after a process that involves only strong interactions.
Nevertheless, for the states in C2 that mix protons and neutrons to have any
meaning, there must be a mechanism which can convert protons into neutrons and
vice versa. Mathematically, we have a way to do this: the action of SU (2). What
does this correspond to, physically?
The answer originates in the work of Hideki Yukawa. In the early 193 0s, he pre-
dicted the existence of a particle that mediates the strong force, much as the photon
mediates the electromagnetic force. From known properties of th e strong force, he
was able to predict that this particle should be about 200 times as mas sive as the
electron, or about a tenth the mass of a proton. He predicted tha t experimentalists
would ﬁnd a particle with a mass in this range, and that it would interact strongly
when it collided with nuclei.
Partially because of the intervention of World War II, it took over te n years for
Yukawa’s prediction to be vindicated. After a famous false alarm (se e Section 2.5),
it became clear by 1947 that a particle with the expected properties had been found.
It was called the pion and it came in three varieties: one with positive charge, the
π+, one neutral, the π0, and one with negative charge, the π−.
The pion proved to be the mechanism that can transform nucleons. To wit, we
observe processes such as those in Figure 1, where we have drawn the Feynman
diagrams which depict the nucleons absorbing pions, transforming w here they are
allowed to by charge conservation.
9
π − p
n
π + n
p
π− +p →n π + +n →p
π 0 p
p
π 0 n
n
π0 +p →p π 0 +n →n
Figure 1: The nucleons absorbing pions.
Because of isospin conservation, we can measure the I3 of a pion by looking at
these interactions with the nucleons. It turns out that the I3 of a pion is the same
as its charge:
Pion I3
π+ +1
π0 0
π− −1
Here we pause, because we can see the clearest example of a patte rn that lies at the
heart of the Standard Model. It is the relationship between isospin I3 and charge
Q. For the pion, isospin and charge are equal:
Q(π) = I3(π).
But they are also related for the nucleon, though in a subtler way:
Nucleon I3 Charge
p 1
2 1
n − 1
2 0
10
The relationship for nucleons is
Q(N ) = I3(N ) + 1
2.
This is nearly the most general relationship. It turns out that, for any given family
of particles that diﬀer only by I3, we have the Gell-Mann–Nishijima formula :
Q =I3 +Y/ 2
where the charge Q and isospin I3 depend on the particle, but a new quantity,
the hypercharge Y , depends only on the family. For example, pions all have
hyperchargeY = 0, while nucleons both have hypercharge Y = 1.
Mathematically,Y being constant on ‘families’ just means it is constant on rep-
resentations of the isospin symmetry group, SU(2). The three pio ns, like the proton
and neutron, are nearly identical in terms of mass and their strong interactions. In
Heisenberg’s theory, the diﬀerent pions are just diﬀerent isospin s tates of the same
particle. Since there are three, they have to span a three-dimens ional representation
of SU(2).
Up to isomorphism, there is only one three-dimensional complex irrep of SU(2),
which is Sym 2C2, the symmetric tensors of rank 2. In general, the unique ( n + 1)-
dimensional irrep of SU(2) is given by Sym nC2. Physicists call this the spin-n/2
representation of SU(2), or in the present context, the ‘isospin- n/2 representa-
tion’. This representation has a basis of vectors where I3 ranges from −n/2 to n/2
in integer steps. Nucleons lie in the isospin- 1
2 representation, while pions lie in the
isospin-1 representation.
This sets up an interesting puzzle. We know two ways to transform n ucleons:
the mathematical action of SU(2), and their physical interactions with pions. How
are these related?
The answer lies in the representation theory. Just as the two nucle ons span the
two-dimensional irrep of C2 of SU(2), the pions span the three-dimensional irrep
Sym2C2 of SU(2). But there is another way to write this representation wh ich sheds
light on the pions and the way they interact with nucleons: because S U(2) is itself
a three-dimensional real manifold, its Lie algebra su(2) is a three-dimensional real
vector space. SU(2) acts on itself by conjugation, which ﬁxes the identity and thus
induces linear transformations of su(2), giving a representation of SU(2) on su(2)
called the adjoint representation.
For simple Lie groups such as SU(2), the adjoint representation is ir reducible.
Thus su(2) is a three-dimensional real irrep of SU(2). This is diﬀerent from the
three-dimensional complex irrep Sym 2C2, but very related. Indeed, Sym 2C2 is just
the complexiﬁcation of su(2):
Sym2C2 ∼
= C ⊗ su(2) ∼
= sl(2, C).
The pions thus live in sl(2, C), a complex Lie algebra, and this acts on C2
because SU(2) does. To be precise, Lie group representations ind uce Lie algebra
representations, so the real Lie algebra su(2) has a representation on C2. This
then extends to a representation of the complex Lie algebra sl(2, C). And this
representation is even familiar—it is the fundamental representat ion of sl(2, C) on
C2.
Quite generally, whenever g is the Lie algebra of a Lie group G, and ρ:G ×V →
V is a representation of G on some ﬁnite-dimensional vector space V , we get a
representation of the Lie algebra g on V , which we can think of as a linear map
dρ: g ⊗V →V.
11
And this map is actually an intertwining operator, meaning that it comm utes with
the action of G: since g andV are both representations of G this is a sensible thing
to say, and it is easy to check.
Pions act on nucleons via precisely such an intertwining operator:
sl(2, C) ⊗ C2 → C2.
So, the interaction between pions and nucleons arises naturally fro m the action of
SU(2) on C2 after we complexify the Lie algebra of this group!
Physicists have invented a nice way to depict such intertwining opera tors—
F eynman diagrams:
π N
N ′
Figure 2: A nucleon absorbs a pion.
Here we see a nucleon coming in, absorbing a pion, and leaving. That is, this
diagram depicts a basic interaction between pions and nucleons.
Feynman diagrams are calculational tools in physics, though to actu ally use them
as such, we need quantum ﬁeld theory. Then, instead of just stan ding for intertwin-
ing operators between representations of compact groups such as SU(2), they depict
intertwining operators between representations of the product of this group and the
Poincar´ e group, which describes the symmetries of spacetime. Un fortunately, the
details are beyond the scope of this paper. By ignoring the Poincar´ e group, we are,
in the language of physics, restricting our attention to ‘internal de grees of freedom’,
and their ‘internal’ (i.e., gauge) symmetries.
Nonetheless, we can put basic interactions like the one in ﬁgure 2 tog ether to
form more complicated ones, like this:
p
n
n
p
π −
12
Here, two nucleons interact by exchanging pions. This is the mechan ism for the
strong force proposed by Yukawa, still considered approximately right today. Better,
though, it depicts all the representation-theoretic ingredients o f a modern gauge
theory in physics. That is, it shows two nucleons, which live in a repres entation C2
of the gauge group SU(2), interacting by the exchange of a pion, w hich lives in the
complexiﬁed adjoint rep, C ⊗ su(2). In the coming sections we will see how these
ideas underlie the Standard Model.
