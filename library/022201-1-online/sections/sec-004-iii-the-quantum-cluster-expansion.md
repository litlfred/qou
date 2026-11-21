---
doc_id: 022201-1-online
doc_title: "Efficient algorithms for approximating quantum partition functions"
section_id: sec-004-iii-the-quantum-cluster-expansion
section_title: "THE QUANTUM CLUSTER EXPANSION"
section_number: III
pages: 3-4
source_pdf: 022201_1_online.pdf
source_sha256: 50331bf18a2bd4d5
toc_source: inferred
doc_brief: "Efficient algorithms for approximating quantum partition functions — 13 sections: Front matter; AFFILIATIONS; ABSTRACT"
---
In this section, we shall show how the partition function of a quantum spin system admits an abstract polymer representation and hence
an abstract cluster expansion. We return to the more general setting of hypergraphs for the remainder of this section.
Consider a quantum spin system modeled by the hypergraph G = (X, E) with interaction Φ, where at each vertex x of G, there is a
d-dimensional Hilbert space Hx with d < ∞. Recall that Φ assigns a self-adjoint operator Φ(e) on He ∶= ⊗x∈eHx to each hyperedge e of G.
Define a polymer γ in this model to be a multiset (Eγ, mγ) of hyperedges Eγ ⊆E with the multiplicity function mγ : Eγ →Z+ whose support
Eγ induces a connected subgraph. Say that two polymers are compatible if and only if their supporting subgraphs are vertex disjoint. For a
polymer γ, let ∥γ∥∶= ∑e∈Eγmγ(e) denote its size and let ∣γ∣∶= ∣Eγ∣denote the cardinality of its support; by a slight abuse of notation, we will
J. Math. Phys. 62, 022201 (2021); doi: 10.1063/5.0013689
62, 022201-2
© Author(s) 2021
 30 August 2026 09:11:26
Journal of
Mathematical Physics
write γ = {γi}∥γ∥
i=1. With these definitions, the partition function ZG(β) admits an abstract polymer model representation3,22,23 as formalized
by the following lemma:
Lemma 2. The partition function ZG(β) admits the following abstract polymer model representation:
ZG(β) = ∑
Γ∈G
∏
γ∈Γ
wγ,
where
wγ ∶=
(−β)∥γ∥
∥γ∥!∏e∈Eγmγ(e)! Tr
⎡⎢⎢⎢⎢⎣
∑
σ∈S∥γ∥
∥γ∥
∏
i=1
Φ(γσ(i))
⎤⎥⎥⎥⎥⎦
.
Note that S∥γ∥is the symmetric group of degree ∥γ∥, and this assigns an ordering to the product of interactions. We prove Lemma 9 in
Appendix A. Note that the abstract polymer model representation holds as a formal power series in β. As an immediate corollary, we obtain
a cluster expansion for log(ZG(β)).
Corollary 3. The partition function ZG(β) admits the following cluster expansion:
log(ZG(β)) ∶= ∑
Γ∈GC
φ(HΓ)∏
γ∈Γ
wγ.
For algorithms, an important quantity is the truncated cluster expansion for log(ZG(β)),
Tm(ZG(β)) ∶= ∑
Γ∈GC
∥Γ∥<m
φ(HΓ)∏
γ∈Γ
wγ,
where ∥Γ∥∶= ∑γ∈Γ∥γ∥.
