---
doc_id: quaternioms
doc_title: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations"
section_id: sec-039-the-breakdown-of-energy-conservation-a-formal-de
section_title: "The Breakdown of Energy Conservation: A Formal Derivation"
section_number: null
pages: 35-36
source_pdf: quaternioms.pdf
source_sha256: becedcbc858611dd
toc_source: outline
doc_brief: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations — 45 sections: Front matter; Introduction; Extended Related Work"
---
One of the most fundamental principles in physics is the connection between sym-
metry and conservation laws, as formalized by Noether’s theorem. In standard quantum
mechanics, the symmetry of physical laws under time translation implies that for any
closed system with a time-independent Hamiltonian, the total energy is conserved. This
principle is a cornerstone of our understanding of the physical world.
This section demonstrates that this fundamental connection between a time-independent
Hamiltonian and energy conservation is severed in a non-associative algebra. We will show
that for a general octonionic system, energy is not conserved, a result that starkly illustrates
the unsuitability of an unconstrained octonionic formalism for describing physical reality
as we know it.
Energy Conservation in an Associative Algebra
To appreciate the departure, we ﬁrst brieﬂy review the proof of energy conservation
in an associative algebra (such as for complex or quaternionic quantum mechanics). The
dynamics of an observable A are described in the Heisenberg picture, where the operator
AH(t) evolves in time. Its equation of motion is derived from the Schrödinger equation:
d
dt AH(t) = i
¯h[H, AH(t)].
(A16)
The conservation of an observable is equivalent to its commuting with the Hamiltonian.
To check for energy conservation, we choose our observable to be the Hamiltonian itself,
AH = H. Since any operator commutes with itself, we have:
d
dt H = i
¯h[H, H] = 0.
(A17)
This rigorously proves that for any closed system described by a time-independent Hamilto-
nian in an associative algebra, the energy is a constant of motion. The proof relies critically
on the associativity of the algebra to ensure the standard product rule for differentiation
leads to the simple commutator form of Equation (A16).
The Modiﬁed Heisenberg Equation in O
When we re-derive the equation of motion without assuming associativity, the stan-
dard product rule for differentiation must be replaced with one valid for non-associative
algebras. This leads to additional terms in the ﬁnal equation. While the full derivation is
beyond the scope of this summary, the resulting modiﬁed Heisenberg equation of motion
for an observable A in an octonionic system has been studied in the literature [90]. The
equation acquires a new term proportional to the associator of the operators:
d
dt A = i
¯h[H, A] + 1
¯h2 [H, H, A].
(A18)
The ﬁrst term is the familiar commutator from the standard Heisenberg equation. pse into
the well-behaved quaternionic quantum mechanics described in Chapter 3 [5]. While this
approach guarantees consistency, we will later analyze the signiﬁcant cost it imposes on
the computational power and ﬂexibility of the model.
