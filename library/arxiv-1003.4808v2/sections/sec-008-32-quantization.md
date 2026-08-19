---
doc_id: arxiv-1003.4808v2
doc_title: "Quantum Field Theory and the Volume Conjecture"
section_id: sec-008-32-quantization
section_title: "Quantization"
section_number: 3.2
pages: 16-18
source_pdf: 1003.4808v2.pdf
source_sha256: 72301d4bee491f86
doc_brief: "Quantum Field Theory and the Volume Conjecture — 14 sections: Preliminaries; The many dimensions of the volume ; Parametrized VC"
---
G-connections on Σ:
Mﬂat(G; Σ) =
{ connectionsA on principal FA = 0G-bundle over Σ
}/
gauge equivalence. (3.3)
(Recall that a connection is ﬂat if the curvature FA = dA +A∧A vanishes.) The
precise meaning of the quantization used to obtain HΣ fromMﬂat(G; Σ) will be the
subject of Section 3.2. It depends on the level k = iπℏ−1 (or coupling constant) of
Chern-Simons theory, the only adjustable parameter in the TQFT.
In Chern-Simons theory, one is also interested in colored knots or links embedded
in 3-manifolds. Suppose for the moment that we have compact Chern-Simons theory
with gauge groupG and levelk∈ Z. The intersection of a knot and a boundary surface
Σ shows up as a puncture on Σ and TQFT would assign the boundary S1 surrounding
this puncture in Σ the category of representations of the aﬃne Lie algebra ˆgk,
Z(S1)∼ reps ofˆgk. (3.4)
The deﬁnition of the Hilbert space H(Σ) of a multiple-punctured Σ would then have
to be altered to include the space of homomorphisms between such representations.
For our purposes, however, the complication of knots can be conveniently avoided
by excising the knots and trading representations that color the knots for boundary
conditions on knot complements .
This trick was already mentioned in Section 2.4. In the language of TQFT, it can be
described the following way. Suppose that we have a knot K colored by representation
Rλ inside the closed manifold M. We cut out a tubular neighborhood NK of the knot,
so that
M = (M\NK)∪T 2NK, N K≃D2×S1. (3.5)
Of course,M\NK≃M\K is just the knot complement, andN is topologically a 2-disk
times S1 that contains the knot running through its center. The partition functions
Z(M\K;u; ℏ) and Z(NK;Rλ; ℏ) are both vectors in the boundary Hilbert space HT 2;
therefore, by TQFT,
Z(K⊂M;Rλ; ℏ) =⟨Z(M\K;u; ℏ), Z(NK;Rλ; ℏ)⟩HT2∈ C. (3.6)
15
As we will see in the next section, the Hilbert space HT 2 can be understood as a
space of functions of the variable u that describes the holonomy of ﬂat connections
around the meridian of T 2 (as in Figure 2a). The crucial fact, then, is that the vector
Z(N;Rλ; ℏ)∈H T 2 is only supported on the part of this space with
eu = Hol(µ) = exp
(
iπλ∗ +ρ∗
k
)
. (3.7)
In other words,Z(N;Rλ; ℏ) acts like a delta-functionδ(u−iπλ∗+ρ∗
k ). Therefore, coloring
byRλ is equivalent to restrictingZ(M\K) to an appropriate one-dimensional subspace
ofHT 2:
Z(K⊂M;Rλ; ℏ) =Z(M\K;u; ℏ)
⏐⏐
u=iπλ∗+ρ∗
k
∈ C. (3.8)
Our plan now is to give a complete description ofHT 2 and to explain how the elements
Z(M\K)∈H T 2 may be calculated for knot complements, in the case of Chern-Simons
theory with both compact and complex gauge groups. (The extension to links is
straightforward and will not be mentioned explicitly hereafter.) This will ﬁrst require
a brief discussion of quantization.
3.2 Quantization
The basic problem of quantization begins with a pair ( M,ω ), whereM is a manifold
with symplectic structure ω, called a classical “phase space.” Quantization takes this
pair and constructs a quantum Hilbert space H. Moreover, quantization should map
the algebra of functions on M to an algebraAℏ of operators onH:
(M,ω ) ↝ H (= Hilbert space)
alg. of functions on M ↝ alg. of operators on H
f ↦→ O f :H→H .
(3.9)
The functions onM form a Poisson algebra with respect to the usual pointwise mul-
tiplication of functions and a Lie algebra structure {•,•} induced by the symplectic
structure. Quantization must map this algebra to an associative but noncommutative
algebraAℏ, such that
[Of,Og] =−iℏO{f,g} +... , (3.10)
where [•,•] is the commutator of operators. Here ℏ is a parameter that is involved in
the determination ofH itself as well as the algebra of operators.
Very roughly, the Hilbert spaceH consists of L2 sections of a complex line bundle
overM with curvature 1
ℏω. Locally, these sections are only allowed to depend on half
of the coordinates of M. In a standard physical setup, M can be thought of as the
space of all possible positions xi and momenta pi of particles; thus the elements of H
16
are functions (“wavefunctions”) that depend on either positions or moments, but not
both.
In addition to the construction of H, the process of quantization must also explain
how classical motions or trajectories of a physical system are associated to quantum
states in H. A classical trajectory (or “semiclassical state”) is described by a La-
grangian submanifoldL⊂M . Being Lagrangian means that L is middle-dimensional
andω|L = 0. Let θ be 1-form (called a Liouville 1-form 9) that satisﬁes ω =dθ. Notice
that θ|L is closed. Then the Lagrangian L is called quantizable if
∮
γ
θ∈ 2πℏ Z (3.11)
for any closed cycle γ⊂L . The vector (or wavefunction) Z∈H corresponding toL
can be written as
Z =Z(x) = exp
(i
ℏS0(x) +...
)
, (3.12)
with
S0(x) =
∫ x
x0
θ (3.13)
for some ﬁxed x0 and varying x∈L . Due to the quantization (3.11), the expression
(3.12) is completely well-deﬁned.
Expression (3.12) only deﬁnes Z to leading order in ℏ. To ﬁnd subleading correc-
tions, it is useful to employ a complementary approach. Suppose that the Lagrangian
submanifoldL is cut out by certain equations fi = 0 on M. Quantization promotes
these functions to operators Ofi acting onH, and the vector Z can also be deﬁned as
a solution to the equations
Ofi·Z = 0 ∀i. (3.14)
If theOfi are properly quantized, then the solution to these equations will be the exact
wavefunction.
