---
doc_id: arxiv-quant-ph-0606114v3
doc_title: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation"
section_id: sec-021-trinion
section_title: "Trinion"
section_number: null
pages: 43-51
source_pdf: 0606114v3.pdf
source_sha256: a8e08c457b65c728
toc_source: inferred
doc_brief: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation — We review the q-deformed spin network approach to Topological Quantum Field Theory and apply these methods"
---
Figure 17 - Decomposition of a Surface into Trinions
a
b
c
d
e
f
a
b
c
ε
V(           )
V(                                )
ε
Figure 18 - Trivalent Vectors
=
Figure 19 - Trinion Associativity
A
B
C
A
B
C
=
Figure 20 - Tube Twist
From the point of view that we shall take in this paper, the key to the
mathematical structure of three-dimensional TQFT lies in the trivalent graphs,
including the braiding of grapical arcs. We can think of these braided graphs
as representing idealized Feynman diagrams, with the trivalent vertex as the
basic particle interaction vertex, and the braiding of lines representing an in-
teraction resulting from an exchange of particles. In this view one thinks of
the particles as moving in a two-dimensional medium, and the diagrams of
braiding and trivalent vertex interactions as indications of the temporal events
in the system, with time indicated in the direction of the morphisms in the
category. Adding such graphs to the category of knots and links is an exten-
sion of the tangle category where one has already extended braids to allow any
embedding of strands and circles that start in n ordered points and end in
m ordered points. The tangle category includes the braid category and the
Temperley-Lieb category. These are both included in the category of braided
trivalent graphs.
Thinking of the basic trivalent vertex as the form of a particle interaction
there will be a set of particle states that can label each arc incident to the
vertex. In Figure 18 we illustrate the labeling of the trivalent graphs by such
particle states. In the next two sections we will see speciﬁc rules for labeling
such states. Here it suﬃces to note that there will be some restrictions on these
labels, so that a trivalent vertex has a set of possible labelings. Similarly, any
trivalent graph will have a set of admissible labelings. These are the possible
particle processes that this graph can support. We take the set of admissible
labelings of a given graph G as a basis for a vector space V (G) over the
complex numbers. This vector space is the space of processes associated with
the graph G. Given a surface S and a decomposition t of the surface into
trinions, we have the associated graph G(S, t) and hence a vector space of
processes V (G(S, t)). It is desirable to have this vector space independent of
the particular decomposition into trinions. If this can be accomplished, then
the set of vector spaces and linear mappings associated to the surfaces can
consitute a functor from the category of cobordisms of one-manifolds to vector
spaces, and hence gives rise to a one-dimensional topological quantum ﬁeld
theory. To this end we need some properties of the particle interactions that
will be described below.
A spin network is, by deﬁnition a lableled trivalent graph in a category of
graphs that satisfy the properties outlined in the previous paragraph. We shall
detail the requirements below.
The simplest case of this idea is C. N. Yang’s original interpretation of the
Yang-Baxter Equation [80]. Yang articulated a quantum ﬁeld theory in one
dimension of space and one dimension of time in which the R-matrix giving the
scattering ampitudes for an interaction of two particles whose (let us say) spins
corresponded to the matrix indices so that Rcd
ab is the amplitude for particles of
spin a and spin b to interact and produce particles of spin c and d. Since these
interactions are between particles in a line, one takes the convention that the
particle with spin a is to the left of the particle with spin b, and the particle with
spin c is to the left of the particle with spin d. If one follows the concatenation
of such interactions, then there is an underlying permutation that is obtained
by following strands from the bottom to the top of the diagram (thinking of
time as moving up the page). Yang designed the Yang-Baxter equation for R
so that the amplitudes for a composite process depend only on the underlying
permutation corresponding to the process and not on the individual sequences
of interactions.
In taking over the Yang-Baxter equation for topological purposes, we can
use the same interpretation, but think of the diagrams with their under- and
over-crossings as modeling events in a spacetime with two dimensions of space
and one dimension of time. The extra spatial dimension is taken in displacing
the woven strands perpendicular to the page, and allows us to use braiding
operators R and R−1 as scattering matrices. Taking this picture to heart, one
can add other particle properties to the idealized theory. In particular one
can add fusion and creation vertices where in fusion two particles interact to
become a single particle and in creation one particle changes (decays) into two
particles. These are the trivalent vertices discussed above. Matrix elements
corresponding to trivalent vertices can represent these interactions. See Figure
21.
Figure 21 -Creation and Fusion
Once one introduces trivalent vertices for fusion and creation, there is the
question how these interactions will behave in respect to the braiding operators.
There will be a matrix expression for the compositions of braiding and fusion or
creation as indicated in Figure 22. Here we will restrict ourselves to showing the
diagrammatics with the intent of giving the reader a ﬂavor of these structures.
It is natural to assume that braiding intertwines with creation as shown in
Figure 24 (similarly with fusion). This intertwining identity is clearly the sort
of thing that a topologist will love, since it indicates that the diagrams can
be interpreted as embeddings of graphs in three-dimensional space, and it ﬁts
with our interpretation of the vertices in terms of trinions. Figure 22 illustrates
the Yang-Baxter equation. The intertwining identity is an assumption like the
Yang-Baxter equation itself, that simpliﬁes the mathematical structure of the
model.
=
R
I
R
I
R
I
R
I
R
I
R
I
R
I
R
I
Figure 22 - YangBaxterEquation
= R
Figure 23 - Braiding
=
Figure 24 - Intertwining
It is to be expected that there will be an operator that expresses the re-
coupling of vertex interactions as shown in Figure 25 and labeled by Q. This
corresponds to the associativity at the level of trinion combinations shown in
Figure 19. The actual formalism of such an operator will parallel the mathe-
matics of recoupling for angular momentum. See for example [36]. If one just
considers the abstract structure of recoupling then one sees that for trees with
four branches (each with a single root) there is a cycle of length ﬁve as shown
in Figure 26. One can start with any pattern of three vertex interactions and
go through a sequence of ﬁve recouplings that bring one back to the same
tree from which one started. It is a natural simplifying axiom to assume that
this composition is the identity mapping. This axiom is called the pentagon
identity.
F
Figure 25 - Recoupling
F
F F
F
F
Figure 26 - Pentagon Identity
Finally there is a hexagonal cycle of interactions between braiding, recou-
pling and the intertwining identity as shown in Figure 27. One says that the
interactions satisfy the hexagon identity if this composition is the identity.
=
R
R
R
F
F
F
Figure 27 - Hexagon Identity
A graphical three-dimensional topological quantum ﬁeld theory is an algebra
of interactions that satisﬁes the Yang-Baxter equation, the intertwining iden-
tity, the pentagon identity and the hexagon identity. There is not room in this
summary to detail the way that these properties ﬁt into the topology of knots
and three-dimensional manifolds, but a sketch is in order. For the case of topo-
logical quantum ﬁeld theory related to the group SU(2) there is a construction
based entirely on the combinatorial topology of the bracket polynomial (See
Sections 7,9 and 10 of this article.). See [41, 36] for more information on this
approach.
Now return to Figure 17 where we illustrate trinions, shown in relation
to a trivalent vertex, and a surface of genus three that is decomposed into
four trinions.
It turns out that the vector space V (Sg) = V (G(Sg, t)) to
a surface with a trinion decomposition as t described above, and deﬁned in
terms of the graphical topological quantum ﬁeld theory, does not depend upon
the choice of trinion decomposition. This independence is guaranteed by the
braiding, hexagon and pentagon identities.
One can then associate a well-
deﬁned vector |M⟩in V (Sg) whenenver M is a three manifold whose boundary
is Sg. Furthermore, if a closed three-manifold M3 is decomposed along a surface
Sg into the union of M−and M+ where these parts are otherwise disjoint three-
manifolds with boundary Sg, then the inner product I(M) = ⟨M−|M+⟩is, up
to normalization, an invariant of the three-manifold M3. With the deﬁnition
of graphical topological quantum ﬁeld theory given above, knots and links can
be incorporated as well, so that one obtains a source of invariants I(M3, K)
of knots and links in orientable three-manifolds. Here we see the uses of the
relationships that occur in the higher dimensional cobordism categories, as
descirbed in the previous section.
The invariant I(M3, K) can be formally compared with the Witten [78] integral
Z(M3, K) =
Z
DAe(ik/4π)S(M,A)WK(A).
It can be shown that up to limits of the heuristics, Z(M, K) and I(M3, K) are
essentially equivalent for appropriate choice of gauge group and corresponding
spin networks.
By these graphical reformulations, a three-dimensional TQFT is, at base,
a highly simpliﬁed theory of point particle interactions in 2 + 1 dimensional
spacetime.
It can be used to articulate invariants of knots and links and
invariants of three manifolds. The reader interested in the SU(2) case of this
structure and its implications for invariants of knots and three manifolds can
consult [36, 41, 59, 19, 64]. One expects that physical situations involving 2+1
spacetime will be approximated by such an idealized theory. There are also
applications to 3 + 1 quantum gravity [6, 7, 50]. Aspects of the quantum Hall
eﬀect may be related to topological quantum ﬁeld theory [77]. One can study
a physics in two dimensional space where the braiding of particles or collective
excitations leads to non-trival representations of the Artin braid group. Such
particles are called Anyons. Such TQFT models would describe applicable
physics. One can think about applications of anyons to quantum computing
along the lines of the topoological models described here.
F
