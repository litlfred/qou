---
doc_id: 022201-1-online
doc_title: "Efficient algorithms for approximating quantum partition functions"
section_id: sec-003-ii-the-abstract-cluster-expansion
section_title: "THE ABSTRACT CLUSTER EXPANSION"
section_number: II
pages: 3-3
source_pdf: 022201_1_online.pdf
source_sha256: 50331bf18a2bd4d5
toc_source: inferred
doc_brief: "Efficient algorithms for approximating quantum partition functions — 13 sections: Front matter; AFFILIATIONS; ABSTRACT"
---
The cluster expansion is a powerful tool from mathematical physics that allows one to express, via power series expansions, perturbations
of a well-understood reference model. When the perturbations are sufficiently small, the power series expansions are convergent and allow
one to draw many conclusions regarding correlation decay, zero-freeness, and other related properties. This method was originally introduced
by Mayer in the study of imperfect gases19 but has since been greatly abstracted and simplified. The formulation we use is due to Kotecký and
Preiss.20
An abstract polymer model is a triple (C, w, ∼), where C is a countable set whose objects are called polymers, w : C →C is a function that
assigns to each polymer γ ∈C a complex number wγ called the weight of the polymer, and ∼is a symmetric compatibility relation such that
each polymer is incompatible with itself. Equivalently, the incompatibility relation ≁is a symmetric and reflexive relation. A set of polymers is
called admissible if all the polymers in the set are all pairwise compatible. Note that the empty set is admissible. Let G denote the collection of
all admissible sets of polymers from C. Then, the abstract polymer partition function is defined by
Z(C, w) ∶= ∑
Γ∈G
∏
γ∈Γ
wγ.
Our algorithm is based on reformulating the partition function of a quantum spin system in the abstract polymer model language (see Sec. III).
The utility of this is due to the following fact about log(Z(C, w)).
Let Γ be a non-empty ordered tuple of polymers. The incompatibility graph HΓ of Γ is the graph with vertex set Γ and edges between any
two polymers if and only if they are incompatible. Γ is called a cluster if its incompatibility graph HΓ is connected. Let GC denote the set of all
clusters of polymers from C. The abstract cluster expansion20,21 is a formal power series for log Z(C, w) in the variables wγ, defined by
log(Z(C, w)) ∶= ∑
Γ∈GC
φ(HΓ)∏
γ∈Γ
wγ,
where φ(H) denotes the Ursell function of a graph H,
φ(H) ∶=
1
∣V(H)∣!
∑
E⊆E(H)
spanning
connected
(−1)∣E∣.
