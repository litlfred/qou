---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-014-13-outline
section_title: "Outline"
section_number: 1.3
pages: 23-24
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.992
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
The dissertation is organized as follows.

In chapter [1](#ChapPIMC){reference-type="ref" reference="ChapPIMC"}, I introduce the framework of PIMC first, then I introduce the detailed form of the Hamiltonian we used and its model (Hilbert) space, the trial wave function, the short-time approximation of the propagator and the time step error structure of our calculation. After writing down the details of all the calculations and equations which are suitable for PIMC simulations first, I then describe how the path is calculated and efficiently updated. Particularly, I describe how the path is efficiently calculated by introducing the path diagrams, which visualize the path and make the calculation more accessible than merely the equations alone. The sign problem is discussed, too.

In chapter [\[compalgorithm\]](#compalgorithm){reference-type="ref" reference="compalgorithm"}, I describe the Monte Carlo sampling techniques used in the PIMC. I begin by introducing the Markov chain Monte Carlo and the Metropolis algorithm. I introduce how they are connected to several sampling methods used in PIMC calculations, particularly the multi-level sampling which is efficient and is mostly used. Other sampling methods are introduced, too. I describe how the path is efficiently updated and the sampling strategies implemented in the code.

In chapter [\[RsDs\]](#RsDs){reference-type="ref" reference="RsDs"}, I show the results of the ground state PIMC calculations of the light nuclei up to $^4$He. I introduce how I choose the total imaginary time $\tau$, time step $\Delta \tau$ and the cost of the computation. I show the PIMC results of ground state energy which is in agreement with GFMC and AFDMC results. I also show how to verify if the ground state has been really reached. After presenting the results of the ground state energy, I show results of the operators which do not commute with the Hamiltonian but are also important, such as root-mean-square radii, particle number density and angle averaged Euclidean response functions for single-nucleon couplings.

The summary and outlook of this work are finally given in chapter [\[secSumOutlook\]](#secSumOutlook){reference-type="ref" reference="secSumOutlook"}.

# Path Integral Quantum Monte Carlo {#ChapPIMC}
