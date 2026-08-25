---
doc_id: quaternioms
doc_title: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations"
section_id: sec-010-octonionic-formalism
section_title: "Octonionic Formalism"
section_number: null
pages: 9-11
source_pdf: quaternioms.pdf
source_sha256: becedcbc858611dd
doc_brief: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations — 40 sections: Introduction; Extended Related Work; Introduction: Bridging"
---
In the octonionic case, there is comparatively little work at the level of quantum
information. Our starting point here is the general discussion of octonions in physics
Quantum Rep. 2025, 7, 55 9 of 40
in [2] and the measurement-only scheme of Freedman, Shokrian-Zini, and Wang [ 9], which
realizes universal quantum computation using equiangular projections associated with O.
The goal of this section is not to propose a new measurement-only model, but rather to
analyse, from ﬁrst principles, which parts of the standard gate-based quantum computing
framework survive if one insists on using O as a scalar ﬁeld and where fundamental
obstructions arise.
Right O-modules and basic obstructions.
If scalars are taken in O, three structural hurdles appear, namely: (i) The adjoint
relation ⟨ψ , Aφ ⟩ = ⟨A† ψ , φ ⟩ becomes parenthesization-dependent; (ii) Multipartite tensor
products are not canonically associative; (iii) Dynamics acquires intrinsic path dependence
via the associator [x, y, z] = ( xy)z − x(yz).
Path-ordered evolution and Magnus-like series with associators.
For time-dependent H(t) ∈ O, we deﬁne the following:
U(t) = P exp
(
− i
¯h
∫ t
0
H(τ ) dτ
)
, (3)
with a ﬁxed parenthesization rule encoded by the path-ordering symbol P. A Magnus-like
expansion contains, beyond nested commutators, explicit associator terms:
U(t) = exp
(
Ω 1 + Ω 2 + Ω 3 + · · ·
)
,
Ω 1 = − i
¯h
∫ t
0
H(τ ) dτ , Ω 2 ∼
∫∫
[H(τ 1), H(τ 2)] dτ 1dτ 2 +
∫∫
[x, y, z] dµ ,
so different slicing/orderings of the same control can yield distinct U(t) if the sampled
triples have a nonzero associator (Lemma 2).
Non-associative tensor products.
For right O-modules HA, HB, HC, the scalar action needed to deﬁne (HA ⊗ HB) ⊗ HC
vs. HA ⊗ (HB ⊗ H C) depends on parenthesization. Absent a canonical isomorphism,
“wiring” subsystems is rule-dependent (Theorem 3), which breaks scalable circuit composi-
tion unless we restrict to associative subalgebras.
Foundational scope of the hypercomplex models.
Our use of quaternionic and octonionic amplitudes does not amount to a proposal to
replace the standard complex formulation of quantum mechanics. Throughout this work,
the basic Dirac–von Neumann framework—complex Hilbert spaces, Born-rule probabilities,
and unitary dynamics—is taken as the underlying physical theory . The hypercomplex mod-
els introduced in Sections 2.6 and 2.7 are understood as alternative algebraic presentations
and computational encodings of ﬁnite-dimensional quantum systems, which are always
equipped with explicit embeddings into ordinary complex quantum mechanics (see, e.g.,
Appendix A). In particular, any protocol we describe can be simulated within the usual
qubit model with only polynomial overhead, so all operational predictions ultimately live
inside standard complex quantum theory .
Relation to quaternionic and octonionic quantum mechanics.
Quaternionic quantum mechanics has a long history in which states are rays of a
quaternionic Hilbert space and observables are quaternion-linear operators [ 3,4]. More
recent work shows that such theories admit embeddings into complex quantum theory:
observable probabilities and dynamical maps can be reproduced by complex POVMs and
channels on a suitably enlarged Hilbert space [ 2]. This supports the view that quater-
nionic amplitudes provide an alternative description inside complex quantum mechanics,
rather than an empirically distinct theory . For the octonionic case the situation is even
more delicate: non-associativity makes it highly nontrivial to deﬁne Hilbert spaces, scalar
Quantum Rep. 2025, 7, 55 10 of 40
products, and a satisfactory spectral theory , and existing formulations resolve these issues
only in restricted settings [ 20]. Our approach deliberately avoids taking a stand on these
foundational questions. Instead, the octonionic structures we use are ﬁnite-dimensional
models that, by construction, are realised as encoded subspaces of complex Hilbert space,
where probabilities are still computed using the standard Born rule.
Computational motivation, advantages, and complications.
From the perspective of quantum computation, the motivation for introducing quater-
nionic and octonionic structures is structural rather than to obtain computational power
beyond BQP . Quaternionic amplitudes offer a compact parametrisation of SU(2) rotations
and spinor degrees of freedom, and they arise naturally in axiomatic reconstructions of
ﬁnite-dimensional quantum theory and in information-theoretic comparisons of real, com-
plex, and quaternionic models [ 2]. Octonionic amplitudes, in turn, organise G2 symmetries
and continuous families of equiangular projections that underlie certain measurement-only
and topological schemes for quantum computation [ 9]. Hypercomplex circuit models,
therefore, provide a language in which symmetry , geometry , and measurement structure
can be expressed more economically than in a purely complex parametrisation. At the same
time, passing to H and especially to O brings additional complications: non-commutativity
and non-associativity make tensor products, time ordering, and the deﬁnition of observ-
ables more subtle, and impose strong constraints on physically reasonable dynamics and
measurements. By making the embeddings into complex Hilbert space explicit, our later
complexity-theoretic results show that, once these constraints are properly accounted for,
the resulting models remain polynomially equivalent to standard qubit-based quantum
computation. The beneﬁt of the generalisation is thus a reﬁned understanding of which
algebraic structures and symmetry constraints can be made manifest within the usual qubit
framework, rather than an asymptotic speed-up over the complex model.
