---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-005-21-preliminaries
section_title: "Preliminaries"
section_number: 2.1
pages: 6-7
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
Before we present a mathematically-friendly summary of our proposal and the physics behind
it, we need to introduce some notations, especially those relevant to abelian ﬂat connections
that will be central in our discussion.
Consider a closed and connected 3-manifold M3, with ∂M3 =∅. In order to present the
results in full generality, it will be useful to consider the linking pairing on the torsion part
of H1(M3, Z):
𝓁k : TorH1(M3)⊗ TorH1(M3)−→ Q/Z
[a]⊗ [b] ↦−→ #(a∩b′)/n (2.1)
where b′ is a 2-chain such that ∂b′ = nb for an integer n. Such b′ and n exist because [b]
is torsion. As usual, #( a∩b′) denotes the number of intersection points counted with signs
determined by the orientation. Note that the linking form provides an isomorphism between
– 5 –
TorH1(M3) and its Pontryagin dual (TorH1(M3))∗≡ Hom(TorH1(M3),U (1)) via the pairing
e2πi𝓁k(·,·).
The Z2 Weyl group acts on the elements a∈ TorH1(M3, Z) via a↦→− a. The set of
orbits is the set of connected components of abelian ﬂat SU (2) connections on M3 (i.e.,
connections in the image of ρ :Mﬂat (M3,U (1))→M ﬂat (M3,SU (2)) from the embedding
U(1)⊂SU (2)),3
TorH1(M3, Z)/Z2 ∼= π0Mab
ﬂat(M3,SU (2)). (2.2)
It is also useful to introduce a shorthand notation for the stabilizer subgroup:
Wa ≡ StabZ2(a) =
{
Z2, a=−a,
1, otherwise . (2.3)
