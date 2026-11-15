---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-034-matrix-product-states-algorithm-for-the-pt-negat
section_title: "Matrix product states algorithm for the PT negativity and the CCNR negativity"
section_number: null
pages: 41-42
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
Matrix product states algorithm for the PT negativity and the CCNR negativity
Given MPS |ψ⟩, we consider the entanglement within ρ = trC(|ψ⟩⟨ψ|), where C is a contiguous
subsystem in the middle of the chain, C = {nA + 1, nA + 2, · · · , nA + nC}, and we take the subsystem
A = {1, 2, · · · , nA} and B is the complement of A in ρ, i.e. the subsystem connected to the right edge.
Both the PT negativity and the CCNR can be efficiently computed in this scenario. The method for
the PT negativity was given in Ref. [91].
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
41
EC =
α
α′
β
β′
Figure S4: MPS contraction to construct EC in Eq. (146).
We first place the orthogonality center at a site i ∈C. Then, we define
EC =
Y
i∈C
Ei
(146)
where Ei is the transfer matrix at site i as defined in Eq. (139). The graphical representation is shown in
Fig. S4. EC can be obtained with computational cost O(nCχ5). We now define the partially transposed
matrix EΓ
C which is obtained from EC by permutation of indices, [EΓ
C](α,β′),(α′,β) = [EC](α,α′),(β,β′).
The spectrum of ρΓ is obtained by diagonalizing EΓ
C with cost O(χ6) [91]. Similarly, the singular
values of the realigned matrix Rρ are obtained by performing SVD on EC (note that the matrix EC
already represents the realigned matrix). Therefore, the total cost to compute the PT negativity and
the CCNR negativity in this setup is O(χ6 + nCχ5).
