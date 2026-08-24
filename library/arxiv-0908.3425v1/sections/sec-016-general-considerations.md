---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer"
section_id: sec-016-general-considerations
section_title: "General considerations"
section_number: null
pages: 21-22
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer — We provide an introduction to the basic concepts of chiral pe rturbation theory and discuss some"
---
Let us consider a physical system described by a Lagrangian w hich is invariant under a compact Lie
group G. We assume the ground state of the system to be invariant unde r only a subgroup H of G,
giving rise to n =nG −nH Goldstone bosons. Each of these Goldstone bosons will be des cribed by an
independent ﬁeld φi which is a smooth real function on Minkowski space M 4. These ﬁelds are collected
in an n-component vector Φ = ( φ1, · · ·,φ n), deﬁning the vector space M1. Our aim is to ﬁnd a mapping
ϕ which uniquely associates with each pair ( g, Φ) ∈G ×M1 an element ϕ(g, Φ) ∈M1 with the following
properties:
ϕ(e, Φ) = Φ ∀ Φ ∈M1, eidentity of G, (82)
ϕ(g1,ϕ (g2, Φ)) = ϕ(g1g2, Φ) ∀ g1,g 2 ∈G, ∀ Φ ∈M1. (83)
Such a mapping deﬁnes an operation of the group G on M1. The construction proceeds as follows
[Leutwyler, 1992]. Let Φ = 0 denote the “origin” of M1 which, in a theory containing Goldstone bosons
only, loosely speaking corresponds to the ground state conﬁ guration. Since the ground state is supposed
to be invariant under the subgroup H we require the mapping ϕ to be such that all elements h ∈ H
map the origin onto itself. In this context the subgroup H is also known as the little group of Φ = 0.
We will establish a connection between the Goldstone boson ﬁ elds and the set of all left cosets
{gH |g ∈ G} which is also referred to as the quotient G/H. For a subgroup H of G the set gH =
21
{gh|h ∈ H} deﬁnes the left coset of g (with an analogous deﬁnition for the right coset) which is on e
element of G/H. For our purposes we need the property that cosets either com pletely overlap or are
completely disjoint, i.e, the quotient is a set whose elemen ts themselves are sets of group elements, and
these sets are completely disjoint. Under all elements of a g iven coset gH the origin is mapped onto
the same vector in /CA
n:
ϕ(gh, 0) = ϕ(g,ϕ (h, 0)) = ϕ(g, 0) ∀ g ∈G andh ∈H.
Secondly, the mapping is injective with respect to the eleme nts of G/H. Consider two elements g and
g′ of G where g′ ⁄∈gH . Let us assume ϕ(g, 0) = ϕ(g′, 0):
0 = ϕ(e, 0) = ϕ(g−1g, 0) = ϕ(g−1,ϕ (g, 0)) = ϕ(g−1,ϕ (g′, 0)) = ϕ(g−1g′, 0).
However, this implies g−1g′ ∈H or g′ ∈gH in contradiction to the assumption g′ ⁄∈gH and therefore
ϕ(g, 0) = ϕ(g′, 0) cannot be true. In other words, the mapping can be inverted on the image of ϕ(g, 0).
The conclusion is that there exists an isomorphic mapping between the quotient G/H and and the
Goldstone boson ﬁelds. Of course, the Goldstone boson ﬁelds are not constant vectors in /CA
n but
functions on Minkowski space. This is accomplished by allow ing the cosets gH to also depend on x.
Now let us discuss the transformation behavior of the Goldst one boson ﬁelds under an arbitrary g ∈
G in terms of the isomorphism established above. To each Φ corr esponds a coset ˜gH with appropriate
˜g. Let f = ˜gh ∈ ˜gH denote a representative of this coset such that
Φ = ϕ(f, 0) = ϕ(˜gh, 0).
Now apply the mapping ϕ(g) to Φ:
ϕ(g, Φ) = ϕ(g,ϕ (˜gh, 0)) = ϕ(g˜gh, 0) = ϕ(f ′, 0) = Φ ′, f ′ ∈g(˜gH ).
In order to obtain the transformed Φ ′ from a given Φ we simply need to multiply the left coset ˜ gH
representing Φ by g in order to obtain the new left coset representing Φ ′:
Φ
g
→ Φ ′
↓ ↑
˜gH
g
→ g˜gH
This procedure uniquely determines the transformation beh avior of the Goldstone bosons up to an
appropriate choice of variables parameterizing the elemen ts of the quotient G/H.
