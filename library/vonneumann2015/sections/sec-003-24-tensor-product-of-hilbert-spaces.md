---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-003-24-tensor-product-of-hilbert-spaces
section_title: "Tensor product of Hilbert Spaces."
section_number: 2.4
pages: 10-12
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
Tensor product of Hilbert Spaces.
If H and K are Hilbert spaces one may form their algebraic tensor product
H ⊗alg K (in the category of complex vector spaces). On this vector space
one deﬁnes the sesquilinear form ⟨, ⟩by:
⟨ξ ⊗η, ξ′ ⊗η′⟩= ⟨ξ, ξ′⟩⟨η, η′⟩
and observes that this form is positive deﬁnite. The Hilbert space tensor
product H ⊗K is then the completion of H ⊗alg K. It is easy to see that if
a ∈B(H), b ∈B(K), there is a bounded operator a ⊗b on H ⊗K deﬁned by
a ⊗b(ξ ⊗η) = aξ ⊗bη.
Exercise 2.4.1. Let L2(X, H, µ) be the Hilbert space of measurable square
integrable functions (up to null sets) f : X →H, with H a separable Hilbert
space. For each ξ ∈H and f ∈L2(X, µ) let fξ ∈L2(X, H, µ) be deﬁned
by fξ(x) = f(x)ξ. Show that the map ξ ⊗f 7→fξ deﬁnes a unitary from
H ⊗L2(X, µ) onto L2(X, H, µ).
10
Chapter 3
The deﬁnition of a von Neumann
algebra.
3.1
Topologies on B(H)
1. The norm or uniform topology is given by the norm ||a|| deﬁned in
the previous chapter.
2. The topology on B(H) of pointwise convergence on H is called the
strong operator topology. A basis of neighbourhoods of a ∈B(H) is
formed by the
N(a, ξ1, ξ2, ..., ξn, ϵ) = {b : ||(b −a)ξi|| < ϵ
∀i = 1, · · · , n}
3. The weak operator topology is formed by the basic neighbourhoods
N(a, ξ1, ξ2, ..., ξn, η1, η2, .., ηn, ϵ) = {b : |⟨(b−a)ξi, ηi⟩| < ϵ
∀i = 1, · · · , n}
Note that this weak topology is the topology of pointwise convergence on H
in the “weak topology” on H deﬁned in the obvious way by the inner product.
The unit ball of H is compact in the weak topology and the unit ball
of B(H) is compact in the weak operator topology. These assertions follow
easily from Tychonoﬀ’s theorem by embedding the unit balls in products of
discs using Hilbert space duality.
Exercise 3.1.1. Show that we have the following ordering of the topologies
(strict in inﬁnite dimensions).
(weak operator topology) < (strong operator topology) < (norm topology)
Note that a weaker topology has less open sets so that if a set is closed in
the weak topology it is necessarily closed in the strong and norm topologies.
11
