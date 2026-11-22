---
doc_id: arxiv-2503.08846v1
doc_title: "A Tutorial on Knots and Quantum Mechanics"
section_id: sec-001-basics-of-knot-theory
section_title: "Basics of knot theory"
section_number: null
pages: 4-6
source_pdf: A_Tutorial_on_Knots_and_Quantum_Mechanics.pdf
source_sha256: 18321b615ffc968b
toc_source: outline
doc_brief: "A Tutorial on Knots and Quantum Mechanics — These notes review a description of quantum mechanics in terms of the topology of spaces, basing on the axioms of Topological Quantum Field Theory and path"
---
Basics of knot theory
In this section we give a minimal introduction to knots and their topological invariants, necessary to
make quantum mechanical computations. Introductory material into knot theory can be found in these
books [18,42,43].
We understand a knot K as a map of a circle S1 into an ambient three-dimensional space R3. For
example:2
K :
−→
.
(1)
The trivial map takes S1 into a circle in R3, which is called the unknot.
Similarly, we define a link through a collection of circles, L : S1 × S1 × · · · × S1 →R3:
L :
−→
.
(2)
We will use the notion of a knot (or link) diagram, which is a projection of a three-dimensional knot
(link) on any two dimensional plane, as the following diagram intends to illustrate:
−→
.
(3)
In most cases the projection will produce a number of ambiguous points corresponding to apparent
intersections of lines. In order to maintain the full information about the topology the intersections of
the diagram are resolved into one of the two possibilities,
or ,
,
(4)
keeping track of which of the lines appears on top of the other in the projection.
The same knot or link can give origin to a pair of apparently distinct knot diagrams, so one could be
interested in introducing an equivalence relation on the diagrams, namely any two diagrams should be
equivalent if they come from projections of two homeomorphic (3D-equivalent) knots or links.
2The 3D pictures of knots were obtained from Wikimedia Commons.
4
A theorem proven by James Alexander and Garland Briggs (and independently by Kurt Reidemeister)
states that a pair of diagrams correspond to the same knot or link if they can be transformed into each
other through a sequence of the following three Reidemeister moves:
↔
↔
↔
I move
II move
III move
.
(5)
Then the central problem of knot theory is to understand how many different knots exist and to
classify them. In particular, if one draws a pair of random diagrams one might wonder if the diagrams
correspond to the same knot or link, or, similarly, whether any of the diagrams represent an unknot,
the trivial knot. Anticipating quantum mechanical applications of knot theory, one may formulate the
classification problem as finding all possible ways of tangling of the unknot.
Distinguishing a pair of knots requires a discriminator, or a hash function, that, when evaluated on
a pair of knots, would produce the same key (the same value) if two knots are the same, and, ideally,
different keys (values) if the knots are different. Such a function is called topological invariant. It should
not be sensitive to smooth deformations of the knot that do not change its topology.
Preferably, the output of a topological invariant is a simple, computable object. A limited number of
such functions is known. One of them is the linking number introduced by Carl Friedrich Gauss in the
first half of the 19th century. This invariant can be derived in physics by substituting the Biot-Savart
law,
B(r2) = µ0I
4π
Z
γ1
dr1 × (r2 −r1)
|r2 −r1|3
,
(6)
for a magnetic field created by a current I flowing in a circuit γ1, parameterized by vector r1, into the
Ampere’s law,
Z
γ2
B(r2) · dr2 = µ0 ℓI ,
(7)
where ℓis computing the algebraic sum of the number of times current I crosses a surface bounded by a
closed circuit γ2. All physics cancels from the result and one obtains the Gauss’ formula:
ℓ=
1
4π
Z
γ1
Z
γ2
(dr1 × (r2 −r1)) · dr2
|r2 −r1|3
.
(8)
Although it appears as a complicated double integral, the result is a simple counting of the number of
times circuit γ1 passes through circuit γ2, taking into account the orientations of both circuits. The result
does not depend on smooth deformations of γ1 and γ2, that is deformations that do not make the two
circuits cross each other.
As is clear from its definition, Gauss’ linking number ℓdefines a topological invariant of a two-
component link, which means that it is not applicable to the proper knots and to links with more than
two components. Moreover, it is not hard to find an example of two topologically distinct links with the
same linking number. One example is provided by the Whitehead link
,
(9)
which has zero linking number.
More powerful invariants were discovered in the 20th century. In 1920s Alexander used homology
methods to introduce an invariant of knots and links that evaluates to a polynomial of a single param-
eter [44]. Alexander’s polynomial has a much higher resolution power, but still gives same values for
5
many nonequivalent knots. A stronger polynomial invariant was discovered by Vaughan Jones in 1980s
by studying von Neumann algebras [3, 45]. Even stronger generalizations appeared shortly after. The
two-variable colored HOMFLY-PT polynomial, named after Jim Hoste, Adrian Ocneanu, Kenneth Mil-
let, Peter Freyd, William Lickorish, David Yetter as well as after Jozef Przytycki and Pawel Traczyk is
believed to be powerful enough to distinguish any pair of knots or links [46,47].
In the remaining part of this section we will introduce the Jones polynomial and review several
methods of computing it.
