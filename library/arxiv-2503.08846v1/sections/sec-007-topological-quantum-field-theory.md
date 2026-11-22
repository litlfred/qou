---
doc_id: arxiv-2503.08846v1
doc_title: "A Tutorial on Knots and Quantum Mechanics"
section_id: sec-007-topological-quantum-field-theory
section_title: "Topological Quantum Field Theory"
section_number: null
pages: 13-16
source_pdf: A_Tutorial_on_Knots_and_Quantum_Mechanics.pdf
source_sha256: 18321b615ffc968b
toc_source: outline
doc_brief: "A Tutorial on Knots and Quantum Mechanics — These notes review a description of quantum mechanics in terms of the topology of spaces, basing on the axioms of Topological Quantum Field Theory and path"
---
Topological Quantum Field Theory
Theories whose description does not explicitly or implicitly use the spacetime metric are called topolog-
ical [15, 20]. Metric independence means that observables of such theories do not depend on distances.
This imposes powerful constraints on the theory, one of which is vanishing Hamiltonian.
Recall that the stress-energy tensor can be obtained by the variation of the action of a nongravitational
theory with respect to the background metric:
T µν = −
2
√−g
δS
δgµν
.
(54)
If the theory is metric independent, all the components of the stress-energy tensor are null. Curiously,
pure gravity appears to be a type of topological theory that has vanishing of the stress-energy tensor
13
Figure 2: A schematic depiction of a category (objects and morphisms).
as its dynamical equations. Quantum gravity is also metric-independent in another sense: gravitational
path integral is a sum over all possible metrics.
Distance independence implies a lack of the notion of locality and lack of local degrees of freedom.
Locality is an important feature of quantum field theory, which distinguishes it from quantum mechanics.
Therefore, topological theories are essentially instances of quantum mechanics, which sometimes disguise
themselves as quantum field theories.
One famous example of a TQFT is the Chern-Simons theory, which will be formally introduced in a
later section. It is an example of a gauge theory, whose local degrees of freedom are pure gauge. Gauge
transformations, however, do not affect some global characteristics of fields, which allow for the theory
to contain some nontrivial information. Early studies of Chern-Simons theories (for example in [5,8,20])
connected them with knots. Motivated by those studies, Atiyah gave a very formal definition of TQFTs,
known as Atiyah’s axioms [19].
Atiyah’s definition is very useful to motivate the discussion of quantum mechanics that will follow,
but to introduce it we will need to first review the basic definitions of category theory. Those interested
in learning more about categories and their applications may consult the book [58].
A category (figure 2) consists of objects (A, B, C etc.) and morphisms (f, g, h etc.). Objects can
be anything, for example: sets, spaces, algebraic structures etc. Morphisms are maps between objects
satisfying the following axioms:
• for morphisms f : A →B and g : B →C there exists a composition g◦f : A →C. The composition
is associative;
• for any object A there exists the identity morphism 1A : A →A such that f ◦1A = f or 1A ◦g = g.
This axiom implies that 1A is unique.
Linear spaces and linear operators provide a fundamental example of a category – Vect. This category
is the main subject of the study of linear algebra. Note that in this category the objects are not necessarily
of the same dimension and morphisms are not necessarily square matrices.
Another example is the
category of groups – Grp. Morphisms of the latter are group homomorphisms.
Group representations and homomorphisms are behind the idea of the functor – a map between
categories.
A functor F maps objects into objects and morphisms into morhphisms, preserving the
composition structure. F satisfies the following axioms:
• If A and A are objects in two categories, such that A = F(A) then the identity morphism is
preserved:
F(1A) = 1A ;
(55)
14
• If f : A →B is a morphism in the first category then F maps it into a morphism between images
of A and B in the second category:
F(f) : F(A) →F(B);
(56)
• F preserves the composition of any two morphisms f and g:
F(f ◦g) = F(f) ◦F(g) .
(57)
To define the topological quantum field theory we will need to introduce one more category – the cat-
egory of cobordisms Cob. Cobordisms are compact smooth manifolds with boundaries. If the boundaries
are compact closed manifolds, one can view the cobordism as connecting different boundaries, that is
cobordisms are certain maps between boundaries. Category Cob considers the boundaries as the objects
and the cobordisms as morphisms.
Now, TQFT is a functor Z : Cob →Vect, which associates a complex vector space Z(Σ) to each
d-dimensional smooth compact oriented space Σ and a vector Z(M) ∈Z(Σ) to each d + 1-dimensional
compact oriented space M whose boundary is Σ. If one accepts that the following heuristic Σ is a compact
closed manifold, which is being mapped on a vector space V :
Z :
Σ
−→
Z(Σ) = V ,
(58)
then vectors in V are obtained from all possible higher dimensional manifolds that can be glued to Σ, for
example,
Z :
M
Σ
−→
Z(M) = v ∈V .
(59)
Note that states can be viewed as cobordisms from a trivial(empty) boundary to Σ. The existence of
infinitely many M explains why Σ is a sort of a vector space.
TQFT functor Z satisfies the following axioms:
• For a given Σ, manifold Σ∗, which corresponds to the same manifold, but with the opposite choice
of the orientation, is mapped to the dual space of Z(Σ):
Z(Σ∗) = Z(Σ)∗;
(60)
• a disjoint union of boundaries Σ1 ⊔Σ2 is mapped to a tensor product of vector spaces:
Z(Σ1 ⊔Σ2) = Z(Σ1) ⊗Z(Σ2) ;
(61)
• A composition of cobordisms, that is a pair of manifolds M1 (∂M1 = Σ1 ⊔Σ2) and M2 (∂M2 =
Σ2 ⊔Σ3) with an identical boundary component Σ2, is mapped to the product of linear maps:
Z(M2 ◦Σ2 M1) = Z(M2) · Z(M1) ;
(62)
(Note that for this to be consistent, Σ2 must be taken with opposite orientations in M1 and M2.
This axiom completes the general axiom of a functor by specifying the map Z(◦).)
• If Σ is trivial than its image are complex numbers C:
Z(∅) = C ;
(63)
15
• If I is an interval [0, 1] then the image of the manifold Σ × I is the identity map on Z(Σ):
Z(Σ × I) = 1Z(Σ) .
(64)
Equipped with Atiyah’s axioms we can now start thinking of elements of linear algebra as topological
spaces. We have already drew a vector (59) as a manifold glued to a given boundary. It is not hard to
imagine that an operator O acting on a specific vector in the same vector space should be something of
the following kind:
O :
v =
M
Σ
−→
Σ
Σ
Σ
_
= O · v
(65)
This has an apparent analogy with tensor networks and classical and quantum circuits, where application
of an operator (gate) is expressed by a diagram
O :
ψ
−→
O
ψ
.
(66)
In the TQFT presentation the lines of the evolution are thickened to become spaces, whose nontriv-
ial topological features are the gates.
Moreover, states gain their own space presentation that holds
information about their structure.
The axioms also instruct us about the inner product: If by gluing a pair of manifolds along a common
appropriately oriented boundary we get a manifold with no boundary, the result should correspond to
a C-number. Indeed, in this case, the boundary of a closed manifold is an empty space, so the functor
maps it to a number. The following diagram illustrates a situation, in which this happens:
M
M'
−→
≡⟨ψ|ψ′⟩.
(67)
The closed manifold represents the inner product of a pair of states.
Another useful trick is the computation of the trace of an operator. For an endomorphism, that is
for a linear operators that maps a space to itself, the trace can be computed by gluing together two of
its boundaries (closing the space on itself). The following example,
Tr



=
,
(68)
can be thought as computing the trace of an identity operator, which gives the dimension of the space
associated with the boundary. Note that all the above pictures are rather heuristic as the boundaries
themselves appear to have boundaries, which is not a true representation of the situation we assume in
the TQFT. However, if, in the last example, the TQFT is two-dimensional, and the boundary is a circle,
then the trace is indeed a torus.
In the following sections we will give explicit examples of TQFT, which will allow to compute all the
data of the linear algebra exactly, preserving the general topological interpretation.
