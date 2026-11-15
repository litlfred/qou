---
doc_id: arxiv-2503.08846v1
doc_title: "A Tutorial on Knots and Quantum Mechanics"
section_id: sec-014-entropy-of-entanglement
section_title: "Entropy of Entanglement"
section_number: null
pages: 33-36
source_pdf: A_Tutorial_on_Knots_and_Quantum_Mechanics.pdf
source_sha256: 18321b615ffc968b
toc_source: outline
doc_brief: "A Tutorial on Knots and Quantum Mechanics — These notes review a description of quantum mechanics in terms of the topology of spaces, basing on the axioms of Topological Quantum Field Theory and path"
---
Entropy of Entanglement
So far we avoided working with a precise quantitative measure of entanglement. In this section we will
discuss the von Neumann entropy, which provides one of the most common measures, and try to explain
why it is natural for the topological formulation of quantum mechanics.
The von Neumann, or entanglement entropy is defined in terms of density matrices. If a state is
pure, that is we have complete access to the information about it, encapsulated in a vector |Ψ⟩, then the
density matrix associated with the state is given by the “square” of the state vector:
ρ = |Ψ⟩⟨Ψ| .
(135)
It is useful to already have a topological interpretation of the basic definitions. Pure state is a state
isolated from the environment, that is lacking any correlations with anything that is not the state itself.
In the TQFT language this means that, as a space, the state cannot have a component that is connected
with something that is not the state (compactness). Consider an example of a bipartite state:
|Ψ⟩=
ΣA
ΣB
.
(136)
The density matrix (a square of the state vector) can be drawn as two copies of the same state:
ρ =
ΣA
ΣB
ΣA
ΣB
_
_
.
(137)
Let us think of the diagram as being a generic topological space, with possible nontrivial features inside.
One can draw the second copy oriented in a different way remembering that one of the copies should be
conjugated.
State (136) belongs to a product of subspaces HΣA and HΣB. One can define the reduced density
matrix which is an effective description of the original state only in terms of one of the subsystems. For
subsystem A the reduced density matrix is defined as
ρA := Tr HΣB ρ ,
(138)
where the trace is calculated with respect to the subsystem B. This partial trace operation is equivalent
to the matrix multiplication of two state tensors, cf. (111):
(ρA)iAjA =
X
iB
ciAiBc†
iBjA .
(139)
This operation can be interpreted as gluing two copies of state |Ψ⟩in (137) along the boundary manifold
ΣB. The result is a space connecting two boundaries ΣA (cf. [84,89]):
ρA =
ΣA
ΣA
_
.
(140)
33
Note that, given the reduced density matrix, recovering the state vector |ψA⟩is not generally possible.
It is clear in the example above that there is no obvious |ψA⟩such that ρA = |ψA⟩⟨ψA|. In other words, ρA
describes not a pure, but a mixed state. In the mixed state subsystem A has correlations with subsystem
B, but the degrees of freedom of B are hidden in the description provided by the density matrix ρA.
We can also see that if the original state |Ψ⟩is entangled with respect to some bipartition, as alleged
by (136), the reduced density matrix of either of the subsystems is mixed.
Given a bipartition and a reduced density matrix, say ρA, the von Neumann entropy is given by
SvN = −Tr HΣAρA log ρA .
(141)
To appreciate this formula let us formally compute the entropy for state (136) and another state
|Φ⟩=
ΣA
ΣB
.
(142)
For state |Φ⟩we can introduce the density matrix and the reduced density matrix in the same way
as for state |Ψ⟩above. In particular,
ρA(Φ) =

ΣB

×
ΣA
ΣA
_
,
(143)
where the prefactor is a closed manifold (C-number) corresponding to the trace of ρ(Φ) over HΣB. Density
matrices (140) and (143) need to be normalized, Tr HΣA ρA = 1. It is not hard to see that the normalized
density matrices have the form
¯ρA(Φ) =

ΣA
−1
ΣA
ΣA
_
,
¯ρA(Ψ) =
h
i−1
ΣA
ΣA
_
.
(144)
The bars over ρ now indicate that the matrices are normalized. The prefactor of the second density
matrix is the result of the gluing the top and the bottom boundaries of (140). It is also a closed manifold
representing a C-number.
To apply the von Neumann formula to matrices in the diagrammatic form, it is convenient to apply
the technique called replica trick [89]. It is based on the following relation:
Tr ρ log ρ = lim
n→1
d
dnTr ρn .
(145)
The procedure involves computing the analytic dependence of the trace of the n-th power of ρ and taking
the derivative, with a subsequent limit n →1. However, thinking in terms of the topological presentation,
it is easy to concatenate spaces and compute Tr ρn when n is integer, but not cutting them for fractional n.
In other words, in general, one would need to assume some analytical continuation in n before computing
the derivative and the limit. In many situations that we will consider, it will be easy to do this, because
n-dependence will only be present in the prefactors, and not in the matrices.
Let us assume that the cylinder representing state |Ψ⟩has translational invariance along its axis. In
fact, for the following, one assumes a weaker condition that ρ2
A(Ψ) ∝ρA(Ψ) that is the condition of a
general projector. (We will not assume anything about |Φ⟩.) It is a simple exercise to show that
¯ρn
A(Φ) =

ΣA
−1
ΣA
ΣA
_
,
¯ρn
A(Ψ) =
h
i−n
ΣA
ΣA
_
.
(146)
34
Importantly, the matrix structure appearing in the above expressions does not depend on n: the same
matrices appear on the right hand side. For |Φ⟩, even the prefactor is n-independent. Consequently,
Tr ¯ρn
A(Φ) = 1 ,
Tr ¯ρn
A(Ψ) =
"
#1−n
.
(147)
Analytical continuation is straightforward for these expressions and one obtains
SvN(Φ) = 0 ,
SvN(Ψ) = log
"
#
.
(148)
Let us discuss these results.
First, as any good measure of entanglement should do, SvN vanishes on separable states. It is easy
to verify this for any pure states also without invoking topology, but a lesson to learn here is that the
von Neumann formula is constructed in such a way that it vanishes on everything that is factorized, or
disconnected in terms of topology. This observation can assist in constructing other interesting quantities
assessing entanglement, e.g. [59,102].
Second, if the state is not separable, replica trick allows us to calculate the expression for the en-
tropy easily if the space has translation symmetry along the “evolution” axis. In this case, the number
corresponding to the closed manifold in the argument of log in (148) is simply the trace of the identity
operator on the Hilbert space HΣA, that is
SvN(Ψ) = log dim HΣA .
(149)
In particular, for state (98) SvN(Ψ) = log 2, as it should be for a Bell state.
Let us slightly generalize this result for the class of reduced density matrices that are projectors. In
terms of the one-dimensional TQFT of section 3.2, we will be interested in states of the form [86]
m
l
.
(150)
This diagram shows a state in a Hilbert space, which is a tensor product of two copies of the Hilbert space
of l + m points. The state corresponds to a space with l lines connecting points belonging to the same
boundary, and m lines connecting different boundaries, and is a characteristic example of a connectome
class. Color shading is used to indicate different Hilbert spaces and subspaces within them.
The reduced density matrix, say, of the left subspace in this connectome state is expressed by the
following diagram:
ρL =
= dl/2
.
(151)
As a result of partial-tracing, shown above, some of the lines turned closed loops and were replaced by
numerical factors according to the rules spelled in section 3.2. The reduced density matrix looks similar
to the original state, but the left and the right boundaries are now copies of the Hilbert space HL (or
rather HL and its dual H∗
L).
We can normalize the reduced density matrix:
¯ρL =
1
Dmdl/2
m
l
.
(152)
35
Note that normalizing it, we get again l/2 trivially closed loops (replaced by numerical factors) and m
loops winding a nontrivial loop that appears when one computes the trace of the diagram (see comments at
the end of sections 3.2 and 3.3 about tracelike closure of diagrams in the topological quantum mechanical
model). To properly evaluate the traces here one takes Markov trace for the subspace of l points and
normal trace for the subspace of m points. For the latter, the result will be a trace of the identity on the
subspace of m points, that is the dimension Dm of that space.
Next, we compute the n-th power of this matrix:
¯ρn
L =
1
Dnmdl/2
m
l
.
(153)
Any power of ¯ρL has the same matrix structure because it is proportional to a projector. The only thing
that distinguishes ρn
L from ρL is the normalization coefficient. Then
Tr ¯ρn
L =
1
Dnmdl/2 Tr
m
l
=
1
Dnm
Tr
m
=
1
Dn−1
m
.
(154)
Computing the entropy using the replica formula yields
SvN = log Dm .
(155)
That is the entropy is given by the logarithm of the dimension of the subspace of the Hilbert space that,
in the given state, is “correlated” with the other part of the system. Put differently, the entropy is a
function of the number of connections between the left and the right subsystems.
The function expressing the entropy of a state like (150) takes a particularly simple form in the limit
considered in section 3.4. Take k →∞and then l →∞and m →∞. In this limit logarithm of Dm is
log Dm ≃m log 2 ,
(156)
that is the entropy is indeed counting the number of connections between the two parties.
The main observation of this section is that the von Neumann entropy can be expressed as the amount
of connectivity that exists between parties. Let us give another version of this relation. In the context of
one-dimensional TQFT and a state expressed by lines connecting left and right subsystems let us draw
an arbitrary curve that encircles one of the subsystems, as in (122). We can choose any curve, but let
us take the one, which crosses the minimal number of lines. In the limit considered above the entropy is
given by log 2 times the number of crossed lines. In the three-dimensional TQFT one should respectively
find a surface that encloses one of the spheres and cuts the minimal number of lines.
The above definition only works for states of the connectome type (150) and more, importantly in the
limit of large k and large number of lines. The reason to introduce such a definition will be explained in
section 6.2 when we will mention connections with quantum gravity and Ryu-Takayanagi formula [103].
