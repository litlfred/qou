---
doc_id: arxiv-2503.08846v1
doc_title: "A Tutorial on Knots and Quantum Mechanics"
section_id: sec-012-topological-tangling-and-quantum-entanglement
section_title: "Topological Tangling and Quantum Entanglement"
section_number: null
pages: 24-26
source_pdf: A_Tutorial_on_Knots_and_Quantum_Mechanics.pdf
source_sha256: 18321b615ffc968b
toc_source: outline
doc_brief: "A Tutorial on Knots and Quantum Mechanics — These notes review a description of quantum mechanics in terms of the topology of spaces, basing on the axioms of Topological Quantum Field Theory and path"
---
Topological Tangling and Quantum Entanglement
Quantum entanglement is a property of quantum mechanical systems quantified by correlations.
A
canonical example of quantum entanglement is the correlation in the Einstein-Podolsky-Rosen (EPR) or
Bell pair [90]. An EPR-Bell pair can be represented by a pair of spins in the state
|Φ+⟩:=
1
√
2 (|0⟩⊗|0⟩+ |1⟩⊗|1⟩) .
(102)
24
Either of the spins can be measured in the state |0⟩or |1⟩with a 50 percent probability. The correlation
is exhibited in the property that if one spin is measured in either of the two states, the state of the other,
upon the first measurement, will be known with a 100 percent probability.
As a first take let us discuss how an EPR-Bell pair can be described in a topological setup. For this
let us explicitly compute the coefficients of state (98) in the standard spin-orientation (computational)
basis using methods of section 3.2.
In order to compute the coefficient of the basis element |0⟩⊗|0⟩we need to glue two |0⟩states from
basis (77) to the open ends of state (98).4 The result is
⟨00|Φ⟩= 1
d2
= d2
d2 = 1 .
(103)
It is not much harder to compute the coefficient of |01⟩. The only difference is that state |1⟩is given by
a linear combination, so there will be two terms:
⟨01|Φ⟩=
1
√
d2 −1
1
d
−
1
d2

= 0 .
(104)
Coefficient of |10⟩and |11⟩basis vectors are computed in a similar fashion. Altogether, we find
|Φ⟩= |00⟩+ |11⟩,
(105)
that is |Φ⟩is the EPR-Bell pair |Φ+⟩up to a normalization.
Another way to see that (98) is the state |Φ+⟩is to notice that by slightly bending the diagram we
can transform the state into an operator
.
(106)
By the TQFT axioms, this must be the identity operator on the 4-point Hilbert space, which has dimen-
sion two. Therefore, it is
|0⟩⟨0| + |1⟩⟨1| .
(107)
Conjugating the bra vector in this expression, that is transforming the operator into a state in a tensor
product of two copies of the the Hilbert space, produces state (105).
Let us consider another example – a state in a product of two 4-point Hilbert spaces given by the
diagram
.
(108)
It is clear that such state should be simply state |00⟩up to normalization. This state is a product state
with no correlations between spins. In any state of the form |ψ1⟩⊗|ψ2⟩measurements of the two parts
are completely independent.
The two examples above illustrate a few properties of the topological description: First, correlations
are expressed by lines (spaces) connecting parts of the system. Second, lack of connection means absence
of correlations, with disconnected topological spaces representing product states. These observations can
be generalized in a more general TQFT setting. Consider a pair of states in a tensor product of two
Hilbert spaces corresponding to two manifolds ΣA and ΣB:
|Ψ1⟩=
ΣA
ΣB
,
|Ψ2⟩=
ΣA
ΣB
.
(109)
4From now on we will use simplified notations for the tensor products, e.g. |00⟩≡|0⟩⊗|0⟩.
25
In the first case the interiors of ΣA and ΣB are filled in such a way that the two boundaries remain
disconnected. In the second, a cobordism fills the space between the two.
States |Ψ1⟩and |Ψ2⟩illustrate two classes of states in quantum theory: separable and entangled.
Separable state can be cast as a tensor product |Ψ1⟩= |ψA⟩⊗|ψB⟩, with the two factors identifiable from
the above diagram. An entangled state is the state in which such a factorization is not possible. In the
next section we will give a formal proof of entanglement of |Ψ1⟩and |Ψ2⟩based on the derivation of von
Neumann entropy.
The picture, in which entanglement emerged as space connecting subsystems is a recurring theme in
different areas of theoretical physics in recent years. One example is the ER=EPR proposal by Juan
Maldacena and Leonard Susskind [91], in which an EPR pair is compared with the Einstein-Rosen (ER)
bridge – a wormhole solution of general relativity [92,93]. A wormhole is a state of the Universe similar
to (98): the existence of a spatial bridge between two subuniverses implies the existence of quantum
correlations between them. A similar idea is the “emergence of space from entanglement” in the context
of AdS/CFT correspondence [94]. The latter states a duality between a nongravitational theory in some
space Σ and a gravitational theory in some M such that Σ = ∂M, is the boundary of M. In this context
entanglement between different parts of Σ corresponds to specific geometries of the spacetime manifold
M.
