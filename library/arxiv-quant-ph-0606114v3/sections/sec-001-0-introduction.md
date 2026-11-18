---
doc_id: arxiv-quant-ph-0606114v3
doc_title: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation"
section_id: sec-001-0-introduction
section_title: "Introduction"
section_number: 0
pages: 2-6
source_pdf: 0606114v3.pdf
source_sha256: a8e08c457b65c728
toc_source: inferred
doc_brief: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation — We review the q-deformed spin network approach to Topological Quantum Field Theory and apply these methods"
---
Introduction
This paper describes the background for topological quantum computing in
terms of Temperley–Lieb recoupling theory. This is a recoupling theory that
generalizes standard angular momentum recoupling theory, generalizes the
Penrose theory of spin networks and is inherently topological. Temperley–Lieb
recoupling Theory is based on the bracket polynomial model [34, 41] for the
Jones polynomial. It is built in terms of diagrammatic combinatorial topology.
The same structure can be explained in terms of the SU(2)q quantum group,
and has relationships with functional integration and Witten’s approach to
topological quantum ﬁeld theory. Nevertheless, the approach given here will
be unrelentingly elementary. Elementary, does not necessarily mean simple.
In this case an architecture is built from simple beginnings and this archic-
tecture and its recoupling language can be applied to many things including,
e.g. colored Jones polynomials, Witten–Reshetikhin–Turaev invariants of three
manifolds, topological quantum ﬁeld theory and quantum computing.
In quantum computing, the application is most interesting because the
simplest non-trivial example of this Temperley–Lieb recoupling Theory gives
the so-called Fibonacci model. The recoupling theory yields representations
of the Artin Braid group into unitary groups U(n) where n is a Fibonacci
number. These representations are dense in the unitary group, and can be
used to model quantum computation universally in terms of representations of
the braid group. Hence the term: topological quantum computation.
In this paper, we outline the basics of the TL-Recoupling Theory, and
show explicitly how the Fibonacci model arises from it. The diagrammatic
computations in the section 9 are completely self-contained and can be used
by a reader who has just learned the bracket polynomial, and wants to see how
these dense unitary braid group representations arise from it. The outline of
the parts of this paper is give below.
1. Knots and Braids
2. Quantum Mechanics and Quantum Computation
3. SU(2) Representations of the Artin Braid Group
4. The Bracket Polynomial and the Jones Polynomial
5. Quantum Topology, Cobordism Categories, Temperley-Lieb Algebra and
Topological Quantum Field Theory
6. Braiding and Topological Quantum Field Theory
7. Spin Networks and Temperley-Lieb Recoupling Theory
8. Fibonacci Particles
9. The Fibonacci Recoupling Model
10. Quantum Computation of Colored Jones Polynomials and the Witten-
Reshetikhin-Turaev Invariant
We should point out that most of the results in this paper are either new,
or are new points of view on known results. The material on SU(2) represen-
tations of the Artin braid group is new, and the relationship of this material
to the recoupling theory is new. See Theorem 1 in Section 3. The treatment
of elementary cobordism categories is well-known, but new in the context of
quantum information theory. The reformulation of Temperley-Lieb recoupling
theory for the purpose of producing unitary braid group representations is
new for quantum information theory, and directly related to much of the re-
cent work of Freedman and his collaborators. In Theorem 2 in Section 7 we
give a general method to obtain unitary representations at roots of unity us-
ing the recoupling theory. The treatment of the Fibonacci model in terms
of two-strand recoupling theory is new and at the same time, the most ele-
mentary non-trivial example of the recoupling theory. The models in section
10 for quantum computation of colored Jones polynomials and for quantum
computation of the Witten-Reshetikhin-Turaev invariant are new. They take
a particularly simple aspect in this context.
Here is a very condensed presentation of how unitary representations of the
braid group are constructed via topological quantum ﬁeld theoretic methods.
One has a mathematical particle with label P that can interact with itself to
produce either itself labeled P or itself with the null label ∗. When ∗interacts
with P the result is always P. When ∗interacts with ∗the result is always ∗.
One considers process spaces where a row of particles labeled P can successively
interact subject to the restriction that the end result is P. For example the
space V [(ab)c] denotes the space of interactions of three particles labeled P.
The particles are placed in the positions a, b, c. Thus we begin with (PP)P.
In a typical sequence of interactions, the ﬁrst two P’s interact to produce a ∗,
and the ∗interacts with P to produce P.
(PP)P −→(∗)P −→P.
In another possibility, the ﬁrst two P’s interact to produce a P, and the P
interacts with P to produce P.
(PP)P −→(P)P −→P.
It follows from this analysis that the space of linear combinations of processes
V [(ab)c] is two dimensional. The two processes we have just described can
be taken to be the qubit basis for this space. One obtains a representation
of the three strand Artin braid group on V [(ab)c] by assigning appropriate
phase changes to each of the generating processes. One can think of these
phases as corresponding to the interchange of the particles labeled a and b in
the association (ab)c. The other operator for this representation corresponds
to the interchange of b and c. This interchange is accomplished by a unitary
change of basis mapping
F : V [(ab)c] −→V [a(bc)].
If
A : V [(ab)c] −→V [(ba)c]
is the ﬁrst braiding operator (corresponding to an interchange of the ﬁrst two
particles in the association) then the second operator
B : V [(ab)c] −→V [(ac)b]
is accomplished via the formula B = F −1RF where the R in this formula acts
in the second vector space V [a(bc)] to apply the phases for the interchange of
b and c. These issues are illustrated in Figure 1, where the parenthesization
of the particles is indicated by circles and by also by trees. The trees can be
taken to indicate patterns of particle interaction, where two particles interact
at the branch of a binary tree to produce the particle product at the root. See
also Figure 28 for an illustration of the braiding B = F −1RF
In this scheme, vector spaces corresponding to associated strings of particle
interactions are interrelated by recoupling transformations that generalize the
mapping F indicated above. A full representation of the Artin braid group
on each space is deﬁned in terms of the local interchange phase gates and the
recoupling transformations. These gates and transformations have to satisfy
a number of identities in order to produce a well-deﬁned representation of the
braid group. These identities were discovered originally in relation to topolog-
ical quantum ﬁeld theory. In our approach the structure of phase gates and
recoupling transformations arise naturally from the structure of the bracket
model for the Jones polynomial. Thus we obtain a knot-theoretic basis for
topological quantum computing.
F
R
Figure 1 - Braiding Anyons.
Aspects of the quantum Hall eﬀect are related to topological quantum
ﬁeld theory [77, 23, 14, 15], where, in two dimensional space, the braiding of
quasi-particles or collective excitations leads to non-trival representations of
the Artin braid group. Such particles are called Anyons. It is hoped that the
mathematics we explain here will form the bridge between theoretical models
of anyons and their applications to quantum computing.
Acknowledgement. The ﬁrst author thanks the National Science Founda-
tion for support of this research under NSF Grant DMS-0245588. Much of
this eﬀort was sponsored by the Defense Advanced Research Projects Agency
(DARPA) and Air Force Research Laboratory, Air Force Materiel Command,
USAF, under agreement F30602-01-2-05022. The U.S. Government is autho-
rized to reproduce and distribute reprints for Government purposes notwith-
standing any copyright annotations thereon. The views and conclusions con-
tained herein are those of the authors and should not be interpreted as nec-
essarily representing the oﬃcial policies or endorsements, either expressed or
implied, of the Defense Advanced Research Projects Agency, the Air Force
Research Laboratory, or the U.S. Government. (Copyright 2006.) It gives the
authors pleasure to thank the Newton Institute in Cambridge England and ISI
in Torino, Italy for their hospitality during the inception of this research and
to thank Hilary Carteret for useful conversations.
