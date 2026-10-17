---
doc_id: arxiv-1012.5432v4
doc_title: "quant-ph Towards Topological Quantum Computation? -"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-11
source_pdf: 1012.5432v4.pdf
source_sha256: ec5f6da1f813649e
toc_source: outline
---
quant-ph
Towards Topological Quantum Computation? -
Knotting and Fusing Flux Tubes
Meagan B. Thompson
1
arXiv:1012.5432v4  [quant-ph]  26 Dec 2012
Abstract
Models for topological quantum computation are based on braiding and fusing anyons (quasi-
particles of fractional statistics) in (2+1)-D. The anyons that can exist in a physical theory are
determined by the symmetry group of the Hamiltonian. Speciﬁcally, any theory of anyons must have
braiding and fusion rules that satisfy consistency conditions known as the pentagon and hexagon
equations (collectively, the Seiberg-Moore Polynomial Equations.) Maclane’s coherence theorem
states these are in fact all that is required in order to achieve commutativity of all combinations of
fusion and braiding (i.e. a consistent physical theory). Two applications of the Hexagon Equation
yield the Yang-Baxter Equation(YBE) familiar from statistical mechanics: σjσj+1σj = σj+1σjσj+1
where the σi are the abstract braid group generators. It is an unsolved mathematical problem
to determine in general all the matrix solutions to the YBE. In the case that the Hamiltonian
undergoes spontaneous symmetry breaking of the full symmetry group G to a ﬁnite residual gauge
group H, however, solutions are given by representations of the quantum double D(H) of the
subgroup. The quasi-triangular Hopf Algebra D(H) is obtained from Drinfeld’s quantum double
construction applied to the algebra F(H) of functions on the ﬁnite group H. As a vector space,
D(H) = F(H) ⊗C[H] = C(H × H) where C[H] is the group algebra over the complex numbers
and C(H × H) is the space of C-valued functions on H × H.
A major new contribution of this work is a program written in MAGMA to compute the particles
(and their properties - including spin) that can exist in a system with an arbitrary ﬁnite residual
gauge group, in addition to the braiding and fusion rules for those particles. We compute explicitly
the fusion rules for two non-abelian group doubles suggested for universal quantum computation:
S3 and A5, and discover some interesting results, subsystems, and symmetries in the tables. SO(3)4
(the restriction of Chern-Simons theory SU(2)4) and its mirror image are discovered as 3-particle
subsystems in the 8-particle S3 quantum double. The tables demonstrate that both S3 and A5
anyons are all Majorana, but this is not the case for all ﬁnite groups. In the appendices, the
quantum doubles for the remaining nonabelian subgroups of SO(3) - S4, A4, and D4 (the second
in the inﬁnite family Dn) - are tabulated and analyzed. In addition, the probabilities of obtaining
any given fusion product in quantum computation applications are determined and programmed
in MAGMA. Throughout, connections to possible experiments are mentioned.
Keywords: topological quantum computation, quantum physics, condensed matter
2
I.
INTRODUCTION
Richard Feynman in 1982 was the ﬁrst to conceive of the idea of a computer based on
quantum mechanics as potentially oﬀering more computational power than computers based
on just classical physics. [1] As computer components are beginning to attain distances on
which quantum mechanical eﬀects can no longer be ignored, continued size reduction would
necessitate the design of a system that thrives on quantum mechanical distance scales. In
addition, subsequent developments in algorithms have shown that certain problems believed
to be classically computationally intractable would be eﬃciently solvable on a quantum com-
puter. (Notably, quantum algorithms for factoring large numbers and ﬁnding discrete logs
eﬃciently [2] would be able to decipher RSA and Diﬃe-Hellman, a fact which would have
radical implications for the security of data ranging from credit cards to electronic commu-
nication). These algorithms would suggest even the asymptotic computational power of a
device is inextricably linked to the underlying physical mechanisms governing its operation
in this more general framework. (The Church-Turing thesis asserts that all classical devices
lead to the same asymptotic complexity.)
The main idea of topological quantum computation is to exploit in an automatically
scalable way the physics of the underlying system to obtain computations that are inherently
protected from errors. Thus the issue of quantum error correction on the software level is
sidestepped to a certain extent as error-prevention is a physical property of the system
(eﬀectively hardwired). From the computational perspective, the Threshold Theorem (as
discovered by A. Steane in [3] and D. Aharonov and M. Ben-Or in [4]) guarantees that
errorless quantum computation can be achieved using quantum error correction as long as the
original error rate is below a ﬁxed threshold. However, even if the current threshold estimate
(1 part in 10−4) is attainable, the overhead required to accomplish the error correction
procedure is impractical - in general, thousands of qubits are required in order to obtain
the desired control over one. As it stands, topological accuracy may even be necessary to
achieve the threshold.
Information is stored in the global topology of the system and processed via fusion and
braiding. Since the environment interacts locally and the global topology of the system is
not eﬀected by local perturbations, the system is inherently protected against decoherence.
3
II.
(2+1)-DIMENSIONAL
TOPOLOGICAL
GAUGE
THEORIES
SET
THE
STAGE FOR QUANTUM COMPUTATION
The systems in which topology acts to our advantage are those that are eﬀectively (2+1)-
dimensional. The striking accuracy that can be achieved in topological systems for even
classical electronics applications is very promising for the potential accuracy of a topological
quantum computer. For example, the resistivity in the IQHE is accurate to 1 part in 109 [5]
- It was even selected by NIST as the standard of measurement for resistance. Replicating
that type of inherent accuracy in the actual computations of a quantum computer would
be an immense advantage over standard classical computations, regardless of asymptotic
computational complexity.
In three spatial dimensions, particles can be classiﬁed as bosons or fermions according
to whether they have integer or half-integer spin respectively - those are the only two pos-
sibilities. However, F. Wilczek showed that in two dimensions the structure can be much
richer and in fact quasiparticles (anyons) of more general spin and exchange statistics can
exist. [6]
The basic mechanism behind Topological Quantum Computation is to interchange and
fuse these anyons in a controlled manner to achieve computations. The term any-ons, orig-
inally coined by F. Wilczek, refers to the fact that these quasiparticles are a generalization
of bosons and fermions in which the particles in abelian theories acquire “any” (rational)
phase θ when they are interchanged. Bosons correspond to θ = 0 and fermions correspond
to θ = π. Stability restricts θ to be any rational value. In non-abelian theories the ﬁelds can
even transform according to a higher-dimensional representation. It is in fact non-abelian
theories hold the most promise for quantum computation. Anyons have been observed in
a few diﬀerent contexts in nature, notably in observations of the Fractional Quantum Hall
Eﬀect (FQHE) and are postulated to appear in a number of other diﬀerent models which
have yet to be experimentally tested.
Any physical topological theory is speciﬁed by the braiding rules and fusion rules. From
the mathematical perspective, the braiding and fusion rules must satisfy certain consistency
conditions known as the Seiberg-Moore Polynomial Equations (also known as the pentagon
and hexagon equations). Maclane’s coherence theorem states these are in fact all that is
required in order to achieve commutativity of all combinations of fusion and braiding (i.e.
4
a consistent physical theory). The two main operations required for topological quantum
computation are these knotting and fusion operations.
A.
Knots
Knot theory originally began with the suggestion of Lord Kelvin that the fundamental
building blocks of matter were knots in the ether. While the original incarnation of Kelvin’s
idea was not quite physically grounded, it spawned a research program in mathematics
that led to many exciting discoveries. As a result, knots have been extensively studied and
tabulated. The eﬀort received a boost with computer algebra in the 1990s with, among
others, J. Weeks’s computer program to compute various knot invariants. [7]
With the advent of relativity, physicists showed that space and time are linked and thus
spacetime in everyday experience is in fact inherently 4-dimensional. However, a modiﬁca-
tion of Kelvin’s idea may have an element of truth in that in (2+1)-dimensions a conﬁgura-
tion of fundamental excitations/particles in particular systems can be described by a knot
rather than the individual excitations/particles. Speciﬁcally, knotting is one of the basic
mechanisms by which fundamental excitations can be used to achieve topological quantum
computation.
Specializing to particular systems may on the surface appear less fundamental than con-
sidering the elementary particle constituents of matter in a vacuum. However, it may have
more to do with particle physics than it would seem on ﬁrst inspection - In recent years, it has
been shown that classical notions of the vacuum are false. The vacuum is not a stationary
medium characterized by the absence of particles and interaction, but rather it is permeated
by the quark-antiquark QCD condensate and seething with virtual particle-antiparticle pair
production. In addition, it has been shown that the equations of electromagnetism can be
obtained as an eﬀective ﬁeld theory, analogous to those in condensed matter. Thus eﬀective
ﬁeld theories may in fact be the only ultimate physical reality. In any event, eﬀective ﬁeld
theories play a key role in topological physics.
5
B.
Fusion
Fusion rules are necessary to determine the experimental feasibility of any anyon proposal.
In particular, if diﬀerent anyon conﬁgurations in the proposal have diﬀerent cumulative
long-range fusion rules, the environment will be able to distinguish the states, resulting in
decoherence. In addition, fusion is the primary means of readout in Kitaev’s, Preskill’s,
and Mochon’s suggestions for universal quantum computation based on ﬁnite groups. Thus
it is important to understand the fusion rules well in order to build anyon computers.
Furthermore, the anyon properties of spin, charge, and magnetic ﬂux are determined by
their particle types (superselection sectors) and these similarly are important to keep in
mind in the design of experimental realizations of anyons.
To this end, this paper will
culminate with an original program in MAGMA to determine the particles permitted by
the theory, the properties of those particles, and the fusion rules given the arbitrary (ﬁnite)
symmetry group of the Hamiltonian.
In order to understand the program, it is necessary to recall the underlying physical
mechanisms governing (2+1)-dimensional discrete gauge theories. To this end, a motiva-
tional example of the Aharonov-Bohm Eﬀect in quantum electrodynamics (QED) is brieﬂy
described as a transition to the mechanism behind how subgroups of the (truncated) braid
group B(n, m) (n, m ∈Z≥1) of anyons give rise to particles with diﬀerent charges and ﬂuxes
in 2D. [8] Bais and deWild showed that the appropriate mathematical language for discussing
braid groups is quasi-triangular Hopf algebras in the quasitensor category structure. [8] The
particles are determined by the irreducible representations of a particular quasi-triangular
Hopf algebra obtained by Drinfeld’s Quantum Double Construction.
In Section C, the abelian theories Z/NZ and the non-abelian theories S3 and A5 will
be analyzed in depth. S3 and A5 are non-abelian ﬁnite subgroups of SO(3) (and SU(3))
that could be key from the perspective of universal quantum computation. The particles
(deﬁned by charges and magnetic ﬂuxes) and the fusion rules (from the comultiplication
of irreducible representations of the quantum double) that can exist in these theories will
be determined explicitly using the MAGMA program provided in Appendix A. In addition,
the spins of the particles will be computed. A number of interesting results are found from
the resulting tables. In particular, some subsystems are discovered that are interesting from
either a mathematical or quantum computation perspective. The emphasis is on theories
6
that are physically relevant.
An overview of the MAGMA program and a summary of
the main results is provided. The actual MAGMA code is included in Appendix A and
the tabulation of the quantum doubles for the next dihedral subgroup and the remaining
non-dihedral subgroups of SO(3) is completed in Appendix B.
Finally, possible experimental implementations and applications to universal quantum
computation will be discussed. The probabilities of obtaining certain fusion products in the
quantum computation scheme will be derived. The resulting probabilities are implemented
in the MAGMA code included in Appendix A.
III.
MOTIVATION: TOPOLOGICAL EFFECTS IN PHYSICS
Conservation laws are critical to many physics analyses as they often simplify calculations
dramatically and aid intuition. No¨ether’s Theorem states that for every symmetry of the
Hamiltonian, there is a conserved current and provides an explicit formula for calculating the
conserved current. However, it turns out that this list is not exhaustive - In fact, topological
conservation laws can arise that cannot be traced to an underlying No¨ether current.
There are two major manifestations of topological eﬀects - in coordinate space, the
Aharonov-Bohm Eﬀect, and in momentum space, the Berry phase.
A.
Aharonov-Bohm Eﬀect
As motivation, recall the Aharonov-Bohm eﬀect in quantum electrodynamics. [9] Initially,
gauge ﬁelds were introduced into classical physics as auxiliary ﬁelds to aid calculations -
While they were present in the canonical formalism, they were not necessary and did not
appear in the classical equations of motion (Maxwell’s equations in the case of electromag-
netism). However, quantum mechanics promotes observables to operators and mandates
the use of the canonical formalism. As a result, the topology of the gauge ﬁelds can indeed
have observable physical consequences. In particular, in quantum mechanics, electrons be-
come waves which exhibit an interference pattern. Aharonov and Bohm predicted that a
change in the gauge ﬁelds (by for example, the introduction of a solenoid in between the two
beams) will cause a shift in the interference pattern observed. As quantum mechanics only
permits local interactions among ﬁelds and the two electron beams do not pass through the
7
region in which the gauge ﬁelds are nontrivial, the use of the vector potential in this case is
inescapable.
While ﬁrst introduced as a Gedanken-experiment for demonstrating the inﬂuence of topo-
logical defects on physical systems, the Aharonov-Bohm Eﬀect has now been veriﬁed by
many actual physical experiments (including a 1998 experiment using magnetostatic metal
rings [10]). The typical experiment demonstrating the Aharonov-Bohm eﬀect is the 2 slit
electron diﬀraction experiment in which electrons are ﬁred at the slits one at a time and
the diﬀraction pattern on a screen a ﬁxed distance away is measured. A change in the
interference pattern is observed when a solenoid (ideally, inﬁnitely long so the magnetic
ﬁeld completely vanishes outside the solenoid) is placed in between the two slits. Thus it is
found that the vector potential itself has intrinsic physical meaning in this eﬀectively two
dimensional setting, not just the curl as originally supposed in classical electrodynamics.
Formally, Feynman’s path integral method can be applied to to the system at hand. The
phase for the interference term is determined by the path diﬀerence between the two electron
beams. The degree of the eﬀect is thus determined by the integral of the vector potential
around a loop surrounding the solenoid.
Given a non-simply connected system, if the gauge potential is changed by an amount
δA, then the resulting change in the wave equation is only invariant if
H
δA(r) · dr = n h
ej
where n is an integer. Thus the fractional part of
e
h
H
A(r) · dr has measurable physical
consequences.
In broken gauge theories, the ﬂux is quantized - In order to ensure the wave function is
single valued, the vector potential can only encircle the solenoid an integer number of times.
Note that this is a purely topological eﬀect as it is determined solely by the winding number
of the path. (In mathematical terms: the path integral exponent corresponds to an element
of the fundamental group of the space . Speciﬁcally, the solenoid is a puncture in the plane
(the third dimension is trivialized) so π1(R2 \0×R) = π1(S1) = Z.) Thus topology can play
an inﬂuential role in determining quantum physics phenomena. In fact, since topological
interactions are by nature robust against local perturbations, harnessing this resource for
quantum computation could lead to a fault-tolerant quantum computer.
8
FIG. 1: Two particles undergo ﬂux metamorphosis when exchanged. All nontrivial gauge trans-
formations occur in the “Dirac strings” of the particles, denoted here by the lighter lines going oﬀ
to inﬁnity. (a.) h1, h2 ∈H (b.)-(c.) h2 is moved counterclockwise around h1. (d) h′
2 = h1h2h−1
1 .
B.
Flux Metamorphosis
In this paper, the topological eﬀects arising from Hamiltonians in (2+1)-dimensions with
ﬁnite symmetry groups will be considered. Let H be a nonabelian group. The basic idea
is as follows: Consider two particles with ﬂuxes in the residual gauge group: h1, h2 ∈H.
Fluxes introduce a nontrivial holonomy on the set of ground states that eﬀects any test
particle whose path winds around the ﬂux. WLOG take all the nontrivial parallel transport
to occur in a single strand, the Dirac string attached to the particle. (This corresponds to
ﬁxing the gauge.) The Dirac string will be represented as a single thick line in the vertical
direction for all particles.
Now, the long range ﬂux of the two particles combined is h1h2. Exchanging the two
particles counterclockwise, the particle with ﬂux h2 passes through the Dirac string of the
particle with ﬂux h1. Thus the ﬂux of the particle with ﬂux h2 will change to a new ﬂux, call
it h′
2. Interchanging the particles should not have an eﬀect on their cumulative long-range
topological quantum numbers. Thus, when the two particles are exchanged counterclockwise,
the cumulative ﬂux of the two particles should remain equal to h1h2. Thus the relation
h′
2h1 = h1h2 is obtained, or h′
2 = h1h2h−1
1 . This eﬀect is called ﬂux metamorphosis and
applies to any 2D topological theory based on a non-Abelian group.
9
IV.
PHYSICS: HAMILTONIAN DESCRIPTION
Modern physics has evolved closer to group theory as Hamiltonians can be classiﬁed solely
on the basis of their symmetry groups and particle content. In fact, the current standard
model is based on the Hamiltonian described by the gauge symmetry group SU(3)×SU(2)×
U(1). The symmetry groups seen in nature are given by spontaneous symmetry breaking
(SSB) of this gauge group to subgroups. SU(3) is the strong force and SU(2) × U(1) is
the electroweak force. Electromagnetism arises in SSB of the SU(2) × U(1) part to a U(1)
subgroup which involves both SU(2) and U(1) components. (The W ± bosons of the weak
force are charged, so the U(1) cannot be cleanly separated from the SU(2) to be interpreted
as charge.) In fact, superconductivity (also likely to be critical for quantum computation)
corresponds to the further SSB of the U(1) electromagnetic gauge group to a subgroup.
This section will be devoted to understanding the underlying Physical foundations behind
the existence of the particles. First, SSB will be deﬁned and a generic Hamiltonian for
a physical system is provided. Then the restriction is made to the case of n particles in
(2 + 1)-dimensional spacetime and the symmetry groups that can occur for this restricted
class of systems are determined.
A.
Hamiltonian
Since the Hamiltonian of the system as a whole has to transform as a singlet under the
representations of the symmetry group, the representations limit the types of terms that can
occur in the Hamiltonian. In fact, the speciﬁcation of a symmetry group and the particles
that are actually present determines the Hamiltonian uniquely. In (2+1)-dimensional gauge
theories based on ﬁnite groups, the particles must satisfy consistency conditions so that
braiding and fusion between three particles commute. The consistency requirements restrict
the types of particles that can possibly exist in the theory.
To be explicit, the generic action in the Yang-Mills-Higgs theory can be written as
S = SY MH + Smatter
In quantum ﬁeld theory there are two types of symmetries:
10
1. global symmetries (physical symmetries of the theory, which have an associated con-
served No¨ether current) and
2. local gauge symmetries (nonphysical redundancies in the coordinates chosen, so do
not have a conserved No¨ether current).
Suppose the action S (equivalently Hamiltonian, Lagrangian) has symmetry group G.
In the former case 1, if the global symmetry is broken to a ﬁnite subgroup then according
to Goldstone’s theorem a massless particle (a Goldstone boson) is created for every broken
symmetry generator. The emphasis in this thesis is on the latter case 2, in which the vector
gauge ﬁelds (usually originally massless) acquire mass through the Higgs mechanism.
B.
Symmetry Breaking
