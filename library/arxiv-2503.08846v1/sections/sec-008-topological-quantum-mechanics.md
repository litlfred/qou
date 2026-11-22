---
doc_id: arxiv-2503.08846v1
doc_title: "A Tutorial on Knots and Quantum Mechanics"
section_id: sec-008-topological-quantum-mechanics
section_title: "Topological Quantum Mechanics"
section_number: null
pages: 16-19
source_pdf: A_Tutorial_on_Knots_and_Quantum_Mechanics.pdf
source_sha256: 18321b615ffc968b
toc_source: outline
doc_brief: "A Tutorial on Knots and Quantum Mechanics — These notes review a description of quantum mechanics in terms of the topology of spaces, basing on the axioms of Topological Quantum Field Theory and path"
---
Topological Quantum Mechanics
Let us imagine the most simple situation: a one-dimensional TQFT. We will follow a physics-level
exposition in [59]. See [60,61] for a more formal mathematical construction.
16
A 0+1 dimensional quantum field theory is called quantum mechanics, so we will consider a topological
quantum mechanics. In this case, the role of (0-dimensional) Σ will be played by a collection of points.
For our convenience, we will organize the points along a line, as for the braids, or circuit diagrams, since
it will be natural to think of lines attached to the points as their evolution.
Following the TQFT axioms, the states in the Hilbert space associated with a collection of points
must be lines connecting those points. For example,
|ψ⟩=
.
(69)
We would like the Hilbert space to be spanned by all possible ways a given set of points is connected.
Moreover, the above example suggests that we would like also to distinguish connections beyond specifying
which point is connected to which. In particular, we will distinguish the above state |ψ⟩and state
|χ⟩=
,
(70)
which has the same pairs of points connected. In other words, the one-dimensional theory will be implicitly
embedded in three-dimensional space. In terms of the evolution of 0-dimensional particles, one can think
that such particles can pairwise scatter by a right or a left twist, or they can annihilate or be created
in pairs from nothing. Since we want to think of the ket-vectors as initial states, in the ket-states the
particles will be created and the evolution will flow from right to left.
To obtain a bra-state from a ket-state we will reverse the evolution. For state (70) this will take the
form
⟨χ| =
.
(71)
The reversed evolution replaces the right twists by the left ones and vice versa. As we will see this is
necessary if the evolution is unitary.
It is straightforward to compute the scalar products in this model. For states (69) and (70) the scalar
product must produce
⟨χ|ψ⟩=
.
(72)
To complete the definition of this quantum mechanics model we need to specify the dimension of the
Hilbert space and an explicit algebra behind the calculation of scalar products. It must be obvious by now
that the purpose of the construction is to relate quantum states and overlaps with knots, so we can take
advantage of the calculus developed in the previous sections. In particular, we will use the representation
of the braids connected to Jones polynomials, which is based on the skein relation (25).
Let us assume that the above diagrams representing states satisfy skein relations. This means, for
example, that
|χ⟩=
= A
+ A−1
.
(73)
Let us assume that the basis in the Hilbert space is generated only by diagrams with no crossings. Then,
for the 4-point Hilbert space used in the examples above, there are only two basis diagrams:
|e0⟩=
,
|e1⟩=
.
(74)
17
Clearly all other states should be reducible to linear combinations of these two states through the skein
relations.
Generalizing this idea to any even number of points one can notice a connection between the basis
diagrams for the 2n-point Hilbert space and the elements of the Temperley-Lieb algebra TLn. The basis
diagrams are elements of TLn bent in a way to align the points at the top with the points at the bottom:
−→
,
−→
,
· · ·
(75)
Therefore, there are Cn different basis diagrams for the 2n-point Hilbert space, with Cn being the Catalan
numbers (19).
Hermitian conjugation is consistent with the diagrammatic presentation of states if A∗= A−1, that is
A is a complex phase. This is the same condition that we encountered in section 2.4 discussing a matrix
representation of braids. This condition will ensure that the scalar product is positive definite. In order
to compute an overlap of any pair of diagrammatic states we can use the rules of computing the bracket
polynomial summarized at the end of section 2.3. Besides the skein relation the rules include substituting
any disconnected trivial circle by factor d = −A2 −A−2.
Note that if we compute the Gram matrix of basis vectors (74) we will find that it is not diagonal.
Specifically,
⟨e0|e0⟩=
= d2 ,
⟨e0|e1⟩=
= d ,
⟨e1|e1⟩=
= d2 .
(76)
In other words, the basis is not orthogonal. It is straightforward to construct an orthonormal basis using
Gram-Schmidt procedure. For example, the following linear combination of the basis vectors gives two
normalized orhogonal vectors:
|0⟩≡1
d
,
|1⟩≡
1
√
d2 −1

−1
d

.
(77)
Finally, we implicitly assumed that the basis of Temperley-Lieb diagrams is nondegenerate, that is all
the basis vectors are linearly independent. In the example of the 4-point Hilbert space the Gram matrix
shows that it is not always the case. Namely,
det⟨ei|ej⟩= d2(d2 −1)
(78)
vanishes for a few special values, d = 0, ±1. We will further discuss the degeneracy of the Temperley-Lieb
basis in the next section. In general, apart from a finite number of special values of parameters d or A,
one can indeed assume the Temperley-Lieb diagrams to be linearly independent.
We now have a complete description of a quantum mechanics in terms of topological spaces – sets
of open curves. An infinite, but countable set of states in this model have a diagrammatic presentation.
Generic states, however, are only linear combinations of the diagrammatic states. Kauffman’s prescription
for computing the bracket polynomial provides us with the technique to compute arbitrary overlaps of
quantum states and, consequently, matrix elements of any operators represented topologically, such as
one in equation (46).
In the next section we will give a three-dimensional definition of the same quantum mechanical
model, which will allow us to gain additional intuition about the topological presentation. One subtlety,
highlighted by the three-dimensional version, is the calculation of traces of the operators. In the one-
dimensional case, calculation of trace is not intuitive: Closing a braid (an operator) in a tracelike manner,
computes the Markov trace, rather then the ordinary trace. The regular trace should instead be computed
as a sum of all diagonal elements. Embedding the construction in three dimensions clarifies the difference.
18
