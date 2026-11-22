---
doc_id: arxiv-math-9201302v1
doc_title: "The Quantum G 2 Link Invariant"
section_id: sec-003-22-linearly-recurrent-invariants
section_title: "Linearly recurrent invariants"
section_number: 2.2
pages: 5-6
source_pdf: 9201302v1.pdf
source_sha256: 67987dd432f58488
toc_source: inferred
doc_brief: "The Quantum G_2 Link Invariant — We derive an inductive, combinatorial deﬁnition of a polynomial-valued regular isotopy invariant of links and tangled graphs."
---
Linearly recurrent invariants
The topological invariants presented in this paper are best understood as linearly recurrent invariants.
Let I(G) be some k-valued invariant of some tangled graphs G which are possibly decorated in some way.
There is a natural way to extend the invariant I to an invariant⃗I(B) for graph with boundary B which takes
values in a certain vector space over k which depends only on ∂B. If b is a boundary, then we let F(b) be
the vector space of all k-valued functions on the set of all links with boundary −b. Then if ∂B = b, we can
choose⃗I(B) ∈F(b) to simply be the function which takes B′ to I(B ∪B′). We call the resulting invariant⃗
I the vector invariant associated to the scalar invariant I.
So far, the notion of⃗I is not very interesting because the vector space F(b) may be very large. However,
it may happen that only a small portion of F(b) is needed to understand the original invariant I. We deﬁne
the spanning space Span(b) to be the span of⃗I(B) for all B such that ∂B = b. We say that I is a linearly
recurrent invariant, or a recurrent invariant for short, if Span(b) is ﬁnite-dimensional for all b. The motivation
for the name is that if the dimension of the space Span(b) is small, then it is often possible to deﬁne the
original invariant I recursively by describing the invariant⃗I(b) and the vector space it lives in for only a few
choices of B, a strategy which is similar to the deﬁnition of a linearly recurrent sequence of numbers.
Another more suggestive notation for scalar and vector invariants is bra-ket notation, by analogy with
quantum mechanics. In this notation the value of the scalar invariant for some link or tangled graph G is
⟨G⟩, while the corresponding vector invariant for some link or tangled graph with boundary B is denoted
| B⟩.
As a warm-up for the rest of the paper, we review the derivation and deﬁnition of the Kauﬀman bracket,
a linearly recurrent invariant of regular isotopy of links. We denote the Kauﬀman bracket by ⟨·⟩A1 and by
the bra-ket convention we denote the corresponding vector invariant by | ·⟩A1. We assume that the 4-point
spanning space is 2-dimensional and that the two crossingless tangles with 4 endpoints are a basis, and we
assume that the 0-point spanning space is 1-dimensional. In this case there are necessarily relations:
|
〉A1 = a|
〉A1
|
〉A1 = b|
〉A1 + c|
〉A1
If we assume that the bracket is invariant under the ﬁrst of the regular isotopy moves, we can compute:
|
〉A1 = bc|
〉A1 + (b 2+c 2)|
〉A1 + bc|
〉A1
to obtain the consistency equations:
bc
=
1
abc + b2 + c2
=
0
We must also check the second regular isotopy move. However, by a ubiquitous trick in the theory of linearly
recurrent invariants, if the ket of a crossing is a linear combination of kets of crossingless tangles (or in other
contexts crossingless graphs), the second regular isotopy move is a corollary of the ﬁrst regular isotopy move
(more generally, a corollary of other moves involving vertices). We parameterize the solutions by setting
b = −q1/4, which is slightly peculiar but is natural with hindsight. We obtain the recursive rules described in
the introduction. The invariant is completely determined except for its value at the empty link, which lies at
the base of the recursive rules. The choice of this value is equivalent to the choice of a global normalization
factor. The most natural normalization in the context of this paper is to choose ⟨∅⟩A1 = 1.
