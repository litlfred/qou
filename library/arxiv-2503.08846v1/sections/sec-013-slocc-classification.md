---
doc_id: arxiv-2503.08846v1
doc_title: "A Tutorial on Knots and Quantum Mechanics"
section_id: sec-013-slocc-classification
section_title: "SLOCC Classification"
section_number: null
pages: 26-33
source_pdf: A_Tutorial_on_Knots_and_Quantum_Mechanics.pdf
source_sha256: 18321b615ffc968b
toc_source: outline
doc_brief: "A Tutorial on Knots and Quantum Mechanics — These notes review a description of quantum mechanics in terms of the topology of spaces, basing on the axioms of Topological Quantum Field Theory and path"
---
SLOCC Classification
In the previous section we made an observation that disconnected topologies correspond to separable
states in quantum theory, while connected ones are avatars of entangled states. In most cases we would
like to have more information about the system. In particular, one may be interested in quantifying the
amount of the correlation, or detail its structure. It is straightforward to elaborate on the previous idea
and suggest that different kind of topologies encode different types and amounts of entanglement. The
general problem, however, is to make such a classification useful for quantum tasks. By default, topology
suggests an infinite number of different types of entanglement. Quantum Resource Theory, which views
entanglement as a resource that can be used for different quantum tasks, prefers a finite classification.
One very common example of a classification is the one based on Stochastic Local Operations and Clas-
sical Communication (SLOCC) [95]. It is established from the observation that local unitary operations
do not change the amount of entanglement.5 In other words, if there is some amount of entanglement be-
tween parts A and B of the system, then unitary operators acting only on A or only on B will not change
this amount. Conversely local nonunitary, but invertible (stochastic), or invertible nonlocal operations
change the amount of entanglement.
It is somewhat less useful, however, to classify the entanglement through the action of unitaries only.
If one considers a pair of qubits, for example, the action of local unitary operations, realized by SU(2)
matrices, is parameterized by only six real parameters, while one needs seven real parameters for a generic
two-qubit state. This means that there will a continuous family of orbits of quantum states, instead of
discrete classes.
One can extend the class of local operations to include all invertible ones. (Noninvertible ones are
projectors.
Projectors can reduce an entangled state to a separable one.)
For two qubits, a pair of
SL(2) matrices is parameterized by twelve real numbers, sufficient to parameterize any two-qubit state.
Therefore, one may suggest to classify entanglement types by finding the number of all nonequivalent
states modulo action of local invertible operations. If the Hilbert space has the structure H = HN1 ⊗
· · · ⊗HNn, with n subsystems with dimensions Nk, k = 1, . . . , n, the nonequivalent quantum states are
5In this section we will keep the amount of entanglement, or correlation, as some abstract notion, since it depends, in
general, on a specific measure used as a quantifier. In the next section we will focus on entanglement entropy as such a
measure, which will make this discussion more precise.
26
described by the coset
S2(N1+N2+...+Nn)−1
SL(N1) ⊗· · · ⊗SL(Nn) ,
(110)
where Sd is a d-dimensional sphere. For a pair of qudits, n = 2, N1 = N2 = d, local invertible operations
have 4d2 −4 real parameters for the necessary 2d2 −1 need to define a two-qudit state. Consequently,
the entanglement in all bipartite systems can be characterized as belonging to one of a finite number of
SLOCC classes [95]. We will discuss the case of bipartition in detail, while challenges of the multipartite
entanglement classification will be mentioned in section 6.1.
A state in a tensor product of two finite-dimensional Hilbert spaces HA ⊗HB can be characterized
by the coefficient matrix cij:
|Ψ⟩=
X
i,j
cij|ij⟩,
(111)
where the expansion is in orthonormal bases |i⟩and |j⟩of choice in HA and HB respectively. Local
operators OA and OB act on matrix cij appropriately. Note that the rank of the matrix is an invariant
if OA and OB are invertible. Hence, the SLOCC classes can be labeled by the rank.
Schmidt decomposition provides a convenient presentation of the coefficient matrix, useful for quan-
tifying the entanglement:
X
i,j
cij|ij⟩=
min(NA,NB)
X
k=1
p
λk|˜k˜k⟩,
λmin(NA,NB) ≥· · · ≥λ2 ≥λ1 ≥0 .
(112)
Here |˜k⟩are the Schmidt bases, in which matrix elements are “diagonal”. The rank of the coefficient
matrix is the number of strictly positive λk. This defines the SLOCC class the state belongs to. The
magnitudes of λk could be used to quantify the amount of entanglement in each class.
Let us discuss how a similar structure can be built in the topological interpretation of bipartite
entanglement.
This structure will also provide an intuitive notion of its “strength”.
First, we will
give examples of three types of operations appearing in the SLOCC classification, realized in terms of
topologies.
Let us begin with state (98), for which we will also use the alternative diagram (106). Braiding is a
natural topological operation that can be applied to either the left or right set of the boundary points,
converting (106) into a braid. In the construction of section 3.2 braiding is a unitary operation: inverting
the order and the type of the crossings produces the inverse of a braid group element. For example,






†
=
=⇒
=
.
(113)
Natural examples of nonivertible operations are given by the Temperley-Lieb elements. By definition,
Temperley-Lieb elements are projectors:
= d2
.
(114)
It is clear that the above projector applied to the left or to the right of (106) will transform the entangled
state into separable state (108). One of the main results can already be anticipated: The amount of
entanglement depends on the number of lines that connect left and right.
27
A natural example of invertible but nonunitary operations also exists. It should be obvious that the
following state does not correspond to a unitary matrix acting on (106):






†
=
,
but̸
=
.
(115)
This example is not a braid, but a more general tangle. We should expect this state to be invertible.
Even though every point is connected by a line with a point on the same boundary, the line is entangled
with the other boundary through a linking with other lines. The invertibility can be checked explicitly
by computing the expansion of the above state in the computational basis, as we did in equations (103)
and (104):
= (A4 + A−4)2|00⟩+ (1 −A4)2|11⟩.
(116)
It is also useful to check the diagrammatic expansion of this diagram,
A−4
−(A2 −A−2)



+


+ (1 −A4)2
.
(117)
The state is a linear combination of an entangled and a separable states, which implies that it should
have more entanglement than the separable state and less entanglement than state (106). The latter,
being a Bell state, has the maximum possible amount of entanglement.
The difference between the unitary braids and invertible tangles is that the latter do not have local
topological inverses, that is there are no diagrams that, when appended to either side, could untangle the
tangle. This means that there is no way to transform state (116) into state (106) via local topological
operations, while the opposite conversion is straightforward. In Quantum Resource Theory this observa-
tion mirrors the statement that any entangled state can be obtained from the maximally entangled one
with certainty, while the probability of the inverse transformation is finite [95–97].
It is also worth discussing the new diagrams appearing in expansion (117). One finds in the compu-
tational basis that
=
= d|00⟩.
(118)
In other words, both diagrams correspond to the separable state |00⟩, as does the first diagram in (117).
This observation goes against the intuition that the existence of connections between the boundaries
implies correlations, and that the amount of correlations depends on the number of connections. However,
what it really means is that this intuition (and the dependence of the entanglement of the number of
connections) is nonlinear. In particular, a certain minimum amount of connections is needed to establish
correlation, which is a feature of the specific topological quantum mechanics model used here.
Let us clarify the criteria for the minimal connection. If a pair of boundaries of a 1D TQFT are
connected by only two lines than the boundaries are in fact disconnected. This was just seen in the
example studied above:
= 1
d
.
(119)
28
A similar cutting can be applied for any pair of boundaries connected by only a pair of lines. To see why
this happens the diagram can be cut in the middle by inserting a completeness relation. Note that the
completeness relation is formally
=
X
i
|i⟩⟨i| =
0
ED
0
+
1
ED
1
,
(120)
where the identity diagram is cut in the middle by the sum over separable products of basis elements.
The dimension of the 4-point Hilbert space is two, so only two types of insertions appear in the sum.
However, when only two lines are cut, there is only one possible intermediate state:
= 1
d
,
(121)
since the dimension of the 2-point Hilbert space is one (see a discussion of the same point in [20]).
It is important to remember that the two lines can be cut only if these two lines are the only lines
that connect two given boundaries. In terms of diagrams this means that one should be able to draw a
closed contour over the diagram that is crossed by only these two lines and only once, as illustrated by
the following example:
= 1
d
.
(122)
In the 3D formulation of this topological quantum mechanics model this means that one should be able
to draw a 2-sphere which cuts the space into two halves (interior and exterior) and is crossed by only two
lines.
With some intuition gained we can start discussing the classification. We will first give characteristic
representatives of entanglement classes and then explain how other states from each class can be obtained
from the representatives. We will also show how to relate the classification with the SLOCC one and
with the Schmidt decomposition.
In the two-qubit case we have two candidates:
and
,
(123)
which correspond to the separable and the Bell classes respectively (the same two classes that exist for two-
qubit entanglement in the SLOCC classification). Any permutation of points on either side is a unitary
braiding operation, which is merely a local change of basis, which should not affect nonlocal correlations.
Therefore all diagrams obtained from the above by local braiding will belong to the corresponding classes.
More generally, by applying invertible tangles to the diagrams in (123) one can obtain all possible
diagrams which will fall into two classes
OA
OB
and
2PI
,
(124)
where OA and OB are any local operators (tangles) and 2PI are all possible 2-particle-irreducible tangles
(that is diagrams that cannot be cut into two disconnected pieces by cutting any two lines). Both types of
29
states can be obtained by the action of local invertible operators OA ⊗OB on the respective states (123).
This action is class-preserving.
Next, we would like to generalize this example to arbitrary bipartite systems. As we will see this
generalization is not straightforward due to the mentioned nonlinearity of the TQFT model. One way
the nonlinearity manifest itself is in the scaling of the dimension of the system, which grows exponentially
with the number of points on the boundary, as prescribed by (19). If we add a pair of points on the
boundaries and consider the 6-point Hilbert space, the dimension jumps to five.
The generalization
of (123) are
,
,
,
.
(125)
As follows from the above discussion, the first two diagrams are equivalent (they only differ in the
normalization), so there are only three naive topological classes, against five in the SLOCC case. The
three independent diagrams only capture matrices of rank one, two and five. This implies that no diagram
can represent a rank three or rank four matrix. The latter can only be constructed via linear combinations
of diagrams.
To circumvent this problem, we will make the model more “linear” using additional projectors [59].
Since the dimension of the n-point Hilbert space counts the number of possible singlets that can be
formed by the representations of the points, we can note that four spin-one particles can form singlets
in three different ways, four spin 3/2 particles can make four singlets and four spin j particles can
form 2j + 1 singlets.
Therefore to construct Hilbert spaces of arbitrary dimension we should rather
consider representations other than fundamental. However, since the TQFT model was defined only for
particles/Wilson lines in the fundamental representation we should find a way to express the calculations
in terms of the fundamental particles, using tensor products of representations. A useful tool for this is
the Jones-Wenzl (JW) projector, or symmetrizer [3,98,99], which we will now define.
Let us define a recursive series of diagrams, which belong to a Temperley-Lieb algebra:
n
=
n
−
∆n
∆n+1
n
.
(126)
Here the thick line substitutes n normal lines, so the diagrams correspond to an element of TLn+2. The
(n + 2)-line symmetrizer is defined through an embedding of elements of TLn+1. The coefficients of the
recursion relations are
∆−1 = 0 ,
∆0 = 1 ,
∆n+1 = d∆n −∆n−1.
(127)
When appended to a set of n + 2 lines, this projector singles out the representation of spin j = (n + 1)/2.
Let us consider a few examples. The combination
=
−1
d
(128)
makes a j = 1 particle from a pair of spins j = 1/2. Note that the last diagram in the projector is a
projector on a singlet. The above combination has already appeared in the construction of state |1⟩(77).
The fact that it is a projector orthogonal to the singlet projector makes state |1⟩orthogonal to state |0⟩.
30
The projector on the spin 3/2 has the form
=
−
d
d2 −1
 
+
!
+
1
d2 −1
 
, +
!
.
(129)
JW projectors can be used to construct Hilbert spaces (and states) associated with arbitrary represen-
tations. The use of lines in the fundamental representations will give additional advantages for detailing
the internal structure of the states.
The space of four spin j = 1 representations has dimension three and can be constructed using eight
fundamental points and four JW projectors (128). One choice of a basis in this space is
|e0⟩=
,
|e1⟩=
,
|e2⟩=
.
(130)
Note that closing any pair of neighboring inputs or outputs in a JW projector gives zero,
· · ·
· · ·
=
· · ·
· · ·
=
· · ·
· · ·
= 0 .
(131)
An easy way of seeing this is to realize that closing a pair of lines corresponding to projecting onto a
singlet. Then the remaining lines are not enough to form a representation of the maximum spin. Therefore
one can convince oneself that diagrams (130) are the only possibility to close lines without crossings, so
it is a generalization of the qubit Temperley-Lieb basis (123). As in the qubit case, one can construct an
orthonormal qutrit basis. It is convenient to express it in terms of the projectors:
N0|0⟩=
,
N0|1⟩=
,
N2|2⟩=
,
(132)
with easily computable normalization factors N0,1,2. Here the blue boxes project on spin j = 1 repre-
sentation and the pink one – on j = 2, so that the three basis elements are labeled by spins 0, 1 and 2
appearing in the intermediate channel.
The qubit basis (77) can also be cast in a similar way using the JW projectors, with spins 0 and 1
appearing in the intermediate channel. Let us mention again the connection with conformal blocks, such
as (94). The corresponding diagrams can be constructed explicitly with the help of the projectors, for
example,
,
,
.
(133)
The diagrams constructed with lines with different spins also appear in the spin networks proposed by
Roger Penrose as a skeleton of spacetime [100] and later used in the construction of the states of (loop)
quantum gravity [101]. JW projectors take a proper care of the spin summation rules at the junctions.
31
Using Hilbert spaces of representations of different spin, with the help of JW projectors, we can obtain
another generalization of the entanglement classification (123). In the qutrit case the following diagrams
will represent matrices of rank one, two and three, respectively [59]:
,
,
and
.
(134)
This statement can be checked using qutrit basis (132). Moreover, breaking more connections between
left and right will produce states equivalent to the separable state |00⟩expressed by the left diagram
above, similarly to equivalence (119) for the two-qubit diagrams. Therefore for a pair of qutrits we find a
classification analogous to the SLOCC one, based on the ranks of matrices. A generic 2-qutrit state will
fall in one of the tree classes represented by irreducible, 4-particle-irreducible and reducible diagrams.
This picture can be easily generalized to arbitrary 2-qudit situation. For a pair of Hilbert spaces
of dimension 2j + 1 one considers the (4j + 2)-point Hilbert space projected on the subspace of four
spin-j representations with four JW projectors. Considering all possible connections between the two
sets of points by nonintersecting lines (planar diagrams), modulo permutations of points and subject to
constraints (131), as well as generalizations of (119), one obtains a set of diagrams labeling matrices of
rank r = 1, 2, . . . , 2j + 1.6 Constraints (119) will relate all diagrams with at most 2j + 1 lines connecting
left and right Hilbert spaces, so in order to save some drawing, only a half of each diagram needs to be
drawn (the upper half in the conventions of this paper). Summarizing, for H = Cn ⊗Cn one draws
n = 2 :
,
,
n = 3 :
,
,
,
n = 4 :
,
,
,
.
etc. These diagrams explicitly realize the idea that the amount of entanglement is quantified by the
amount of connection that exists between two parties. Let us also note that the approach is directly
generalized to pairs of Hilbert spaces with nonequal dimensions. In the latter case the number of possible
connections will be limited by the the smallest of the two dimensions, as is the case of the matrix rank.
To close this section let us make an important disclaimer. The above analysis has completely ignored
the dependence of the model of the parameter A (or d, or k). As we have seen above, this parameter
introduces additional restrictions on the structure of the TQFT Hilbert spaces. One manifestation of these
restrictions is the dimension of the Hilbert space, which may be smaller than the naive count of singlet
representations given by (19). This happens because some of the vectors become null and disappear from
the Hilbert space. As a result there are additional degeneracies between diagrammatic states, which make
the analysis more subtle. In particular, some invertible operators might become projectors for specific
values of A at roots of unity. We will not enter in the details of such an analysis here. Instead, we will
assume that either the parameter k is not integer, or that it is a sufficiently large integer. (It is safe to
6Note that the equivalence classes of diagrams also correspond to the connectomes of the classical limit of Chern-Simons
theory, discussed in section 3.4, modulo permutations of the points in each Hilbert space factor.
32
assume that it is larger than the number of lines in all states of interest.) In both cases the mentioned
complications do not occur.
Finally, we only considered the case of bipartite entanglement in this section. The situation with the
multipartite entanglement will be mentioned in section 6.1, together with some questions not answered
in this review.
