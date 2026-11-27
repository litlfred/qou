---
doc_id: arxiv-1503.06237v2
doc_title: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence"
section_id: sec-001-2-isometries-and-perfect-tensors
section_title: "Isometries and perfect tensors"
section_number: 2
pages: 5-8
source_pdf: 1503.06237v2.pdf
source_sha256: 55572e7133514f4a
toc_source: outline
doc_brief: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence — We propose a family of exactly solvable toy models for the AdS/CFT correspondence based on a novel"
---
In this section we review some tools which will be used in our constructions of holo-
graphic states and codes. We begin with a standard deﬁnition:
Deﬁnition 1. SayHA andHB are two Hilbert spaces, not necessarily of the same
dimensionality. An isometry fromHA toHB is a linear map T :HA↦→H B with the
property that it preserves the inner product.
IfHA andHB have ﬁnite dimensionality, as we will assume throughout this paper,
then it immediately follows that such aT can exist only if their dimensionalities dim(A)
and dim(B) obey dim(A)≤ dim(B). In the special case where dim( A) = dim(B), T
is just a unitary transformation. Clearly the composition of two isometries is also an
isometry.
If T :HA↦→H B is an isometry, then T†T is the identity on HA and TT† is a
projector mappingHB to the range of T . We may represent the map T as a two-index
tensor acting as
T :|a⟩↦→
∑
b
|b⟩Tba, (2.1)
where{|a⟩} denotes a complete orthonormal basis for HA and{|b⟩} forHB. Then T
is an isometry if and only if ∑
b
T†
a′bTba =δa′a. (2.2)
We represent this graphically in ﬁgure 1, following the convention that operators are
ordered from left to right, so that in the ﬁgure T† is applied after T . We will call a
tensor obeying (2.2) an isometric tensor.
– 3 –
Figure 1 . Diagrammatic tensor notation, here showing that T is an isometry.
Isometric tensors have the property that any operator O acting on its “incoming”
leg, can be replaced by an equal norm operatorO′ acting on its “outgoing” leg, because
TO =TOT†T = (TOT†)T≡O′T ; (2.3)
we illustrate this property in ﬁgure 2. This operation is essential for what follows,
Figure 2 . Operator pushing through an isometric tensor.
and we will often describe it as “pushing an operator through a tensor”. It is also
easy to check a useful converse of operator pushing: If the two-index tensor T has the
property that any unitary transformation U contracted with its incoming index can
be replaced by a corresponding unitary transformationU′ contracted with its outgoing
index (i.e., TU = U′T ), then T obeys (2.2) up to a scalar factor, and therefore must
be proportional to an isometric tensor.
Figure 3 . If HA =HA2⊗H A1, then we can move one of the factors to the output while
preserving the isometric structure.
Another important property of isometric tensors is that if the input Hilbert space
factorizes, we may reinterpret an input factor as an output factor while preserving
(2.2), up to an overall rescaling. That is, if T :HA2⊗HA1↦→H B is an isometric map,
– 4 –
acting on a basis according to
T :|a2a1⟩↦→
∑
b
|b⟩Tba2a1, (2.4)
then ˜T :HA1↦→H B⊗HA2 acting as
˜T :|a1⟩↦→
∑
ba2
|ba2⟩Tba2a1 (2.5)
obeys ˜T† ˜T = dim(A2)IA1. We illustrate this property in ﬁgure 3.
In this paper we will be interested in a special class of isometric tensors, which we
will call perfect tensors. To formulate the concept of a perfect tensor, ﬁrst note that
we may divide the m indices of a tensor Ta1a2...am into a set A and a complementary
set Ac. We use|A| to denote the cardinality of the set A; hence|A| +|Ac| =m. Then
T may be regarded as a linear map from the span of the indices in A to the span of
the indices in Ac. We will usually assume that each index ranges over v values, and
we will use A to denote both the set of |A| indices and the corresponding vector space
with dimension v|A|; thus we say T maps A to Ac.
Deﬁnition 2. A 2n-index tensor Ta1a2...a2n is a perfect tensor if, for any bipartition
of its indices into a set A and complementary set Ac with|A|≤| Ac|,T is proportional
to an isometric tensor from A to Ac.
It is not obvious that nontrivial perfect tensors exist, but they do! Note that for
T to be perfect it suﬃces for T to be a unitary transformation when |A| =|Ac| = n;
in that case the property illustrated in ﬁgure 3 ensures that T is proportional to an
isometric tensor for|A|< n. In Appendix A we describe perfect tensors explicitly for
the case n = 3, v = 2 and for the case n = 2, v = 3; other cases with larger n and v
are also discussed there. To keep our discussion concrete, we will focus especially on
the six-index tensor for qubits ( v = 2)1, but much of what we say applies to arbitrary
2n-index perfect tensors.
Perfect tensors are related to other notable ideas in quantum information theory.
In general, a tensor T with m indices, each ranging over v values, describes a pure
quantum state|ψ⟩ of m v-dimensional spins, where, up to a normalization factor,
|ψ⟩ =
∑
a1,a2,...,am
Ta1a2...am|a1a2...a m⟩. (2.6)
1This can be obtained from the encoding map of the 5-qubit code.
– 5 –
A perfect tensor describes a pure state of 2 n spins with a special property — any set
of n spins is maximally entangled with the complementary set of n spins. Such states
have been called absolutely maximally entangled (AME) states [29, 30]. Conversely any
AME state deﬁnes a perfect tensor. Regarded as a linear map from one spin to 2 n− 1
spins, a perfect tensor is the isometric encoding map of a quantum error-correcting code
which encodes a single logical spin in a block of 2n− 1 physical spins, where the logical
spin is protected against the erasure of anyn−1 physical spins. Because n is more than
half of all the physical spins, this is the best possible protection against erasure errors
compatible with the no-cloning principle. In coding terminology this code has distance
n and is denoted [[m,k,d ]]v = [[2n− 1, 1,n ]]v, where m is the number of physical spins
in the code block, k is the number of protected logical spins, andd is the code distance.
This code is also the basis for a quantum-secret-sharing scheme called a (( n, 2n− 1))
threshold scheme [31]; code states have the property that a party holding any n− 1
spins has no information about the logical spin, while a party holding any n spins has
complete information about the logical spin (because erasure of the remaining n− 1
spins is correctable).
